from submission import Submission
from itertools import permutations


class AyoubBFSubmission(Submission):

    def author(self):
        return 'ayoub-bf'

    def run(self, input):
        g, s = input

        shortest = []
        min_length = float('inf')
        for p in permutations([x for x in g.keys() if x != s]):
            l = g[p[0]][s] + sum([g[p[i]][p[i+1]] for i in range(len(p) - 1)]) + g[p[-1]][s]
            if l < min_length:
                min_length = l
                shortest = [s] + list(p) + [s]

        return shortest
