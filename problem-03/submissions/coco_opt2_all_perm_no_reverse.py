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

def opt_two_all(matrix, time_limit = 2.8):
    solution, length = glouton_all_starts(matrix)
    start = time.time()
    iterations = 0
    improvements = 0
    n = len(matrix)
    permutations = [(i, j) for i in range(n) for j in range(i+1, n)]
    improved = True
    while improved:
        perms = list(permutations)
        improved = False
        while perms and not improved:
            iterations += 1
            if iterations % 20 == 0:
                if time.time() - start > time_limit:
                    return solution, length
            elt1, elt2 = random.choice(perms)
            perms.remove((elt1, elt2))
            sol = list(solution)
            sol[elt1], sol[elt2] = sol[elt2], sol[elt1]
            # temp_partial_sol = list(reversed(sol[min(elt1, elt2) + 1:max(elt1, elt2)]))
            # for i in range(min(elt1, elt2) + 1, max(elt1, elt2)):
            #     sol[i] = temp_partial_sol[i - (min(elt1, elt2) + 1)]
            new_l = calculate_length(sol, matrix)
            if new_l < length:
                improvements += 1
                improved = True
                solution = sol
                length = new_l
    return solution, length

class CocoOpt2AllPerms(Submission):

    def author(self):
        return "coco-opt-2-all-no-reverse"

    def run(self, input):
        path, length = opt_two_all(input)
        return path
