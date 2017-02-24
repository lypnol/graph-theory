from submission import Submission
from random import choice


class AyoubBFSubmission(Submission):

    def author(self):
        return 'ayoub-backtracking'

    def run(self, input):
        graph = input

        def backtracking_helper(graph, heuristic, all_nodes=set(), prefix=[], length=0, min_length=[float('inf')], min_path=[None]):
            prefix_set = set(prefix)

            # If path is complete
            if prefix_set == all_nodes:
                length += graph[prefix[-1]][prefix[0]]
                if length < min_length[0]:
                    min_length[0] = length
                    prefix.append(prefix[0])
                    min_path[0] = prefix
                return

            # If we already exceeded minimum found
            if length >= min_length[0]:
                return

            last = prefix[-1]
            sucessors = [n for n in graph[last] if n not in prefix_set]
            if heuristic is not None:
                sucessors = sorted(sucessors, key=lambda x: heuristic(graph, last, x))

            for n in sucessors:
                backtracking_helper(graph, heuristic, all_nodes, prefix+[n], length+graph[last][n], min_length, min_path)

        def backtracking(graph, heuristic=None):
            min_length = [float('inf')]
            min_path = [None]
            s = choice(list(graph.keys()))
            backtracking_helper(graph, heuristic, all_nodes=set(graph.keys()), prefix=[s], length=0, min_length=min_length, min_path=min_path)
            return min_path[0]

        def closest_heuristic(graph, x, y):
            return graph[x][y]

        def farthest_heuristic(graph, x, y):
            return -graph[x][y]

        return backtracking(graph, closest_heuristic)
