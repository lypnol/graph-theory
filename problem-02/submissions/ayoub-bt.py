from submission import Submission
from random import choice


class AyoubBFSubmission(Submission):

    def author(self):
        return 'ayoub-backtracking'

    def run(self, input):
        graph = input

        def backtracking_helper(graph, all_nodes=set(), prefix=[], length=0, min_length=[float('inf')], min_path=[None]):
            sprefix = set(prefix)

            # If path is complete
            if sprefix == all_nodes:
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
            sucessors = sorted([n for n in graph[last] if n not in sprefix],
                               key=lambda x: graph[last][x])
            for n in sucessors:
                backtracking_helper(graph, all_nodes, prefix+[n], length+graph[last][n], min_length, min_path)

        def backtracking(graph):
            min_length = [float('inf')]
            min_path = [None]
            s = choice(list(graph.keys()))
            backtracking_helper(graph, all_nodes=set(graph.keys()), prefix=[s], length=0, min_length=min_length, min_path=min_path)
            return min_path[0]

        return backtracking(graph)
