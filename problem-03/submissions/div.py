# internal deps
from submission import Submission

class DavidSubmission(Submission):
    def author(self):
        return 'div'


    def run(self, input):

        def run_from_start(graph, start):
            """
            renvoie un chemin assez court commencant par start
            """
            # on compte le nombre de sommets
            nb_nodes = len(graph.keys())

            # noeuds à visiter
            to_visit = set(graph.keys()) - {start}

            # path contient le chemin parcouru
            path = [start]

            # pos contient la position actuelle
            pos = start

            # on y va en glouton
            # boucle principale : tant qu'il reste des noeuds à visiter
            while len(path) < nb_nodes:
                # le prochain noeud à visiter est celui qui est le plus proche
                # parmi ceux qu'il faut encore visiter
                pos = min(to_visit, key=lambda x: graph[pos][x])
                to_visit.remove(pos)
                path.append(pos)

            return path

        def length(graph, path):
            """
            return length of the given path
            """
            return sum(graph[x][y] for x,y in zip(path, path[1:]))


        graph = input
        nodes = graph.keys()
        return max((run_from_start(graph, x) for x in nodes), key=lambda path: length(graph, path))
