# python libs
import glob, sys, getopt, imp, inspect, datetime, re
from os.path import splitext, basename
from os import walk
import time
import signal

from tabulate import tabulate
import functools
import statistics
import argparse

from submission import Submission
from judge import Judge

show_debug = False

#To print colors in terminal
class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


PROBLEM_PATH_PATTERN  = 'problem-[0-9]*'

def _problem_name(problem_path):
    return problem_path.replace('/','_').replace('-','_')

# Return the list of the contests
# It should be the list of the directories matching problem-<a number>
def _get_problems():
    return sorted(glob.glob(PROBLEM_PATH_PATTERN), key=lambda x: abs(int(x[-2:])))

# Returns the lists of possible submission files for the given problem
def _find_submissions_for_problem(problem_path):
    submission_files = []
    for _, _, files in walk(problem_path + '/submissions'):
        for filename in files:
            submission, ext = splitext(filename)
            if ext == '.py':
                submission_files.append(submission)
    return submission_files

def _load_judge_for_problem(problem_path):
    judge_path = '%s/judge.py' % (problem_path)
    problem = _problem_name(problem_path)
    judge_module = imp.load_source('judge_%s' % (problem), judge_path)

    classes = inspect.getmembers(judge_module, inspect.isclass)
    for _, cls_judge in classes[1:]:
        if issubclass(cls_judge, Judge) and not cls_judge == Judge:
            return cls_judge()

    return None

def _load_submission(problem_path, submission):
    submission_path = '%s/submissions/%s.py' % (problem_path, submission)
    problem = _problem_name(problem_path)
    submission_module = imp.load_source('submission_%s_%s' % (problem, submission), submission_path)

    classes = inspect.getmembers(submission_module, inspect.isclass)
    for _, cls_submission in classes:
        if issubclass(cls_submission, Submission):
            return cls_submission()

    return None

def _load_submissions_for_problem(problem_path):
    submission_files = _find_submissions_for_problem(problem_path)
    problem = _problem_name(problem_path)
    submissions = []
    for submission_file in submission_files:
        submission = _load_submission(problem_path, submission_file)
        if submission is not None:
            submissions.append(submission)
    return submissions

class SubmissionTimeoutException(Exception): pass

def _timeout_handler(signum, frame):
    raise SubmissionTimeoutException

def _run_submission(judge, submission, input):
    starttime = time.time()

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(judge.config()['timeout'])

    output = None
    try:
        output = submission.run(input)
    except SubmissionTimeoutException:
        print("{red}[{judgename}] timed out submission from {author}. {end}".format(
                judgename=judge.name(),
                red=bcolors.RED,
                end=bcolors.ENDC,
                author=author))

    runtime = time.time() - starttime

    author = submission.author()
    if not judge.validate(input, output):
        print("{red}[{judgename}] invalid solution from {author}. {end}\n{output}".format(
                judgename=judge.name(),
                red=bcolors.RED,
                end=bcolors.ENDC,
                author=author,
                output=output))
    else:
        print("{green}[{judgename}] {author} score: {score}{end}\n{output}".format(
                judgename=judge.name(),
                green=bcolors.GREEN,
                score=judge.score(input, output, runtime),
                end=bcolors.ENDC,
                author=author,
                output=output))

    if show_debug:
        if len(submission.get_debug_stack()) > 0:
            more = ''
            if len(stack) > 15:
                more = 'and %s other lines...' % (len(stack) - 15)

            print("{red}[{judgename}] Debug trace for {author}:\n\t{trace}\n\t{more}{end}".format(
                judgename=judge.name(),
                red=bcolors.RED,
                end=bcolors.ENDC,
                trace=submission.get_debug_stack(),
                author=author,
                more=more))

def run_submission_from_author(problem_path, author):
    judge = _load_judge_for_problem(problem_path)
    submissions = _load_submissions_for_problem(problem_path)
    submission = None
    for s in submissions:
        if s.author() == author:
            submission = s
            break
    if not submission:
        return
    _run_submission(judge, submission, judge.generate_input())

def run_submissions_for_problem(problem_path, n=0):
    judge = _load_judge_for_problem(problem_path)
    submissions = _load_submissions_for_problem(problem_path)

    if not n:
        n = judge.config()['default_inputs']

    print("{magenta}{problem}    {number} test input{plural}{end}".format(
            problem=basename(problem_path),
            magenta=bcolors.MAGENTA,
            number=n,
            plural=('s' if n > 1 else ''),
            end=bcolors.ENDC))

    inputs = []
    for _ in range(n):
        inputs.append(judge.generate_input())

    results = {submission.author(): {
        'wins': 0,
        'scores': [],
        'errors': 0,
        'best': None
        } for submission in submissions}

    judge_options = judge.config()

    for input in inputs:
        best_score = None
        for submission in submissions:
            name = submission.author()

            starttime = time.time()

            signal.signal(signal.SIGALRM, _timeout_handler)
            signal.alarm(judge_options['timeout'])

            output = None
            try:
                output = submission.run(input)
            except SubmissionTimeoutException:
                results[name]['errors'] += 1
                continue

            runtime = time.time() - starttime

            if not judge.validate(input, output):
                results[name]['errors'] += 1
            else:
                score = judge.score(input, output, runtime)
                results[name]['scores'].append(score)
                if best_score is None or judge.compare(score, best_score) >= 0:
                    best_score = score

                if results[name]['best'] is None or judge.compare(score, results[name]['best']) >= 0:
                    results[name]['best'] = score

        for name in results:
            if results[name]['scores']:
                score = results[name]['scores'][-1]
                if score == best_score:
                    results[name]['wins'] += 1

    leaderboard = sorted([
                    (name,
                    results[name]['wins'],
                    statistics.mean(results[name]['scores'] or [0]),
                    results[name]['best'])
                    for name in results if results[name]['errors'] == 0],
                    key=lambda x: x[1], reverse=True)

    print("Leaderboard")
    table = []
    for i, (name, wins, mean, best) in enumerate(leaderboard):
        table.append([
            "{}{}{}".format(bcolors.YELLOW, (i + 1), bcolors.ENDC),
            "{}{}{}".format(bcolors.BLUE, name, bcolors.ENDC),
            "{}{}{}".format(bcolors.GREEN, wins, bcolors.ENDC),
            "{:.2f}".format(mean),
            "{}".format(best)])

    headers = ["rank", "name", "wins", "avg", "best"]
    print(tabulate(table, headers=headers))

    fails = sorted([
                    (name,
                    results[name]['errors'],
                    statistics.mean(results[name]['scores'] or [0]),
                    results[name]['best'])
                    for name in results if results[name]['errors'] > 0],
                    key=lambda x: x[1])

    if fails:
        print("\nFailed submissions")
        table = []
        for name, errors, mean, best in fails:
            table.append([
                "{}{}{}".format(bcolors.RED, name, bcolors.ENDC),
                "{}{}{}".format(bcolors.RED, errors, bcolors.ENDC),
                "{}{:.2f}{}".format(bcolors.RED, mean, bcolors.ENDC),
                "{}{}{}".format(bcolors.RED, best, bcolors.ENDC)])

        headers = ["name", "errors", "avg", "best"]
        print(tabulate(table, headers=headers))

def main():
    global show_debug

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Enable debug mode", action="store_true")
    parser.add_argument("-p", "--problem", help="Runs judge system on specific problem", type=int)
    parser.add_argument("-a", "--author", help="Runs submissions from specific author", type=str)
    parser.add_argument("-i", "--inputs", help="Number of generated inputs", type=int, default=0)
    args = parser.parse_args()

    show_debug = args.verbose

    problems = _get_problems()
    problem_path = ''

    if args.problem:
        problem_path = 'problem-%02d' % args.problem

    if problem_path in problems:
        if args.author:
            run_submission_from_author(problem_path, args.author)
        else:
            run_submissions_for_problem(problem_path, args.inputs)
    elif args.problem:
        print("Unkown problem %d" % args.problem)
    elif args.author:
        for problem_path in problems:
            run_submission_from_author(problem_path, args.author)
    else:
        for problem_path in problems:
            run_submissions_for_problem(problem_path, args.inputs)

    return

if __name__ == "__main__":
   main()
