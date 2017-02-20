from submission import Submission

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

def actual_length(path, matrix):
    return sum((matrix[path[i]][path[i+1]] for i in range(len(path) - 1)))


def tsp_backtracking_rec_aux(path, restant, best_length, matrix):
    if not restant:
        return path, calculate_length(path, matrix)
    if actual_length(path, matrix) > best_length:
        return (None, None)
    lengths = [tsp_backtracking_rec_aux(path + [s], restant - {s}, best_length, matrix) for s in restant]
    lengths = [x for x in lengths if x[0] is not None]
    if len(lengths) > 0:
        return min(lengths, key=lambda x: x[1])
    else:
        return (None, None)

def tsp_backtracking_rec(matrix, depart=None):
    sommets = list(matrix.keys())
    _, best_length = glouton_all_starts(matrix)
    if depart is not None:
        sommets.remove(depart)
    else:
        depart = sommets.pop()
    path, length = tsp_backtracking_rec_aux([depart], set(sommets), best_length, matrix)
    return path + [depart]

class CocoBacktracking(Submission):

    def author(self):
        return "coco-backtracking"

    def run(self, input):
        matrix = input
        return tsp_backtracking_rec(matrix)
