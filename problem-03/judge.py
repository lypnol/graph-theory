from judge import Judge

from random import randint
from collections import defaultdict, Counter

class Problem03Judge(Judge):

    def name(self):
        return "Travelling salseman approximative"

    def config(self):
        return {
            'default_inputs': 10,
            'input_sizes': [50, 100, 150],
            'timeout': 2
        }

    def random_matrix(self, n):
        matrix = defaultdict(dict)
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = randint(0, 50)
                    matrix[j][i] = randint(0, 50)
        return matrix

    def generate_input(self, size=50):
        return self.random_matrix(size)

    def validate(self, input, output):
        return Counter(output) == Counter(input.keys())

    def _calculate_length(self, permutation, matrix):
        n = len(permutation)
        length = 0
        for i in range(n-1):
            length += matrix[permutation[i]][permutation[i+1]]
        length += matrix[permutation[-1]][permutation[0]]
        return length

    def score(self, input, output, runtime):
        return self._calculate_length(output, input)

    def compare(self, a, b):
        if a > b:
            return -1
        elif a < b:
            return 1
        return 0
