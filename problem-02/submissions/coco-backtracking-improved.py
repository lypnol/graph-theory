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

def tsp_backtracking_closest_neighbours_rec(path, restant, max_length, matrix):
    if not restant:
        return path, calculate_length(path, matrix)
    if actual_length(path, matrix) > max_length:
        return (None, None)
    best_length = max_length
    best_path = None
    for p in restant:  #sorted(restant, key=lambda x: matrix[path[-1]][x]):
        final_path, length = tsp_backtracking_closest_neighbours_rec(path + [p], restant - {p}, max_length, matrix)
        if final_path is not None and length <= best_length:
                max_length = length
                best_length = length
                best_path = final_path
    if best_path is not None:
        return best_path, best_length
    else:
        return (None, None)

def tsp_backtracking_closest_neighbours(matrix):
    sommets = list(matrix.keys())
    _, best_length = glouton_all_starts(matrix)
    s = sommets.pop()
    return tsp_backtracking_closest_neighbours_rec([s], set(sommets), best_length, matrix)

class CocoBacktrackingImproved(Submission):

    def author(self):
        return "coco-backtracking-improved"

    def run(self, input):
        matrix = input
        path, length = tsp_backtracking_closest_neighbours(matrix)
        return path + [path[0]]
