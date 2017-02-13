# Graph Theory Playground
[![Build Status](https://travis-ci.org/lypnol/graph-theory.svg?branch=master)](https://travis-ci.org/lypnol/graph-theory)

Some graph theory algorithms with CI scoring

## How to play
Add your python submission file to `problem-#/submissions` folder.  
Example of submission file:

```python
from submission import Submission

class MyAwesomeSubmission(Submission):

    def author(self):
        return 'unique name'

    def run(self, input):
        # input and output format are given in the
        # README file inside problem folder

        ...

        return output
```

once your `run` function is completed, you can run `python main.py` to see your ranking.

## How to add a problem
Add a new folder `problem-[n+1]` with a README file and a `judge.py` file where you can specify how submissions could be validated and scored.  
Example of `judge.py` file:

```python
from judge import Judge

class MyAwesomeProblem(Judge):

    def name(self):
        return 'unique name'

    def generate_input(self):
        # Generates a test input object
        # You can use optionally randomize inputs
        ...

    def validate(self, input, output):
        # Validates a submission output
        # should return a boolean
        ...

    def score(self, input, output):
        # Scores a submission
        # should return a number
        ...

    def compare(self, a, b):
        # Compares Scores
        # Should return 1  if a is better than b
        #               0  if a and b are the same
        #               -1 if b is better than a
        ...
```
