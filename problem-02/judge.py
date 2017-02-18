from judge import Judge

from itertools import permutations
import random
import time

class Problem02Judge(Judge):

    def __init__(self):
        self._solved = []

    def _eq(self, inp1, inp2):
        g1, s1 = inp1
        g2, s2 = inp2
        for x in g1:
            for y in g1:
                if g1[x][y] != g2[x][y]:
                    return False
        return s1 == s2

    def _solve(self, input):
        for i, o in self._solved:
            if self._eq(input, i):
                return o
        g, s = input

        shortests = []
        min_length = float('inf')
        for p in permutations([x for x in g.keys() if x != s]):
            l = sum([g[p[i]][p[i+1]] for i in range(len(p) - 1)]) + g[p[-1]][s]
            if l < min_length:
                min_length = l
                shortests = [[s] + list(p) + [s]]
            elif l == min_length:
                min_length = l
                shortests.append([s] + list(p) + [s])

        return shortests

    def name(self):
        return "Problem-02 Judge"

    def config(self):
        return {
            'default_inputs': 100
        }

    def generate_input(self):
        n = 6
        m = [[random.randint(1, 100) if i != j else 0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = m[j][i]

        g = {(x+1): {(y+1): m[x][y] for y in range(n)} for x in range(n)}
        return g, random.randint(1, n)

    def validate(self, input, output):
        possible = self._solve(input)

        for p in possible:
            if tuple(output) == tuple(p):
                return True

        return False


    def score(self, input, output, runtime):
        return runtime * 100000

    def compare(self, a, b):
        if a > b:
            return -1
        elif a < b:
            return 1
        return 0
