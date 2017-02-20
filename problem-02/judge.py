from judge import Judge

from itertools import permutations
import random
import time

class Problem02Judge(Judge):

    def __init__(self):
        self._solved = []

    def _eq(self, inp1, inp2):
        g1 = inp1
        g2 = inp2
        for x in g1:
            for y in g1:
                if g1[x][y] != g2[x][y]:
                    return False
        return True

    def _solve(self, input):
        for i, o in self._solved:
            if self._eq(input, i):
                return o
        g = input
        s = list(g.keys())[0]

        min_length = float('inf')
        for p in permutations([x for x in g.keys() if x != s]):
            l = g[p[0]][s] + sum([g[p[i]][p[i+1]] for i in range(len(p) - 1)]) + g[p[-1]][s]
            min_length = min(min_length, l)

        return min_length

    def name(self):
        return "Problem-02 Judge"

    def config(self):
        return {
            'default_inputs': 100,
            'timeout': 1
        }

    def generate_input(self):
        n = 7
        m = [[random.randint(1, 100) if i != j else 0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = m[j][i]

        g = {(x+1): {(y+1): m[x][y] for y in range(n)} for x in range(n)}
        return g

    def validate(self, input, output):
        length = self._solve(input)
        return sum([input[output[i]][output[i+1]] for i in range(len(output) - 1)]) == length

    def score(self, input, output, runtime):
        return runtime * 100000

    def compare(self, a, b):
        if a > b:
            return -1
        elif a < b:
            return 1
        return 0
