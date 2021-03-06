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


class CocoGreedySubmission(Submission):

    def author(self):
        return "coco-greedy"

    def run(self, input):
        circuit, length = glouton(input)
        return circuit
