from submission import Submission
import random
import time

def calculate_length(permutation, matrix):
    n = len(permutation)
    length = 0
    for i in range(n-1):
        length += matrix[permutation[i]][permutation[i+1]]
    length += matrix[permutation[-1]][permutation[0]]
    return length

def glouton(graphe, depart=None):
    sommets = list(graphe.keys())
    if depart is None:
        depart = sommets.pop()
    else:
        sommets.remove(depart)
    circuit = [depart]
    position = depart
    while sommets:
        # selection du plus proche
        min_l = float("inf")
        closest_s = None
        for s in sommets:
            if graphe[position][s] < min_l:
                closest_s = s
                min_l = graphe[position][s]
        sommets.remove(closest_s)
        circuit.append(closest_s)
        position = closest_s
    return circuit, calculate_length(circuit, graphe)

def glouton_all_starts(graphe):
    sommets = list(graphe.keys())
    best_s = min([glouton(graphe, depart=s) for s in sommets], key=lambda x: x[1])
    return best_s

def opt_two(matrix, time_limit = 1.5):
    solution, length = glouton_all_starts(matrix)
    return solution, length
    start = time.time()
    i = 0
    last_improve = 0
    n = len(matrix)

    while True:
        i += 1
        if i % 10 == 0:
            if time.time() - start > time_limit:
                return solution, length
        n = len(matrix.keys())
        elt1, elt2 = random.sample(range(n), 2)
        sol = solution[:]
        sol[elt1], sol[elt2] = sol[elt2], sol[elt1]
        # temp_partial_sol = list(reversed(sol[min(elt1, elt2) + 1:max(elt1, elt2)]))
        # for i in range(min(elt1, elt2) + 1, max(elt1, elt2)):
        #     sol[i] = temp_partial_sol[i - (min(elt1, elt2) + 1)]
        new_l = calculate_length(sol, matrix)
        if new_l < length:
            last_improve = 0
            solution = sol
            length = new_l
        elif new_l == length:
            last_improve += 1

class CocoOpt2(Submission):

    def author(self):
        return "coco-opt-2-lame"

    def run(self, input):
        path, length = opt_two(input)
        return path
