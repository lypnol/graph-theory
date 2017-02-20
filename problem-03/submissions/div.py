# internal deps
from submission import Submission

class DavidSubmission(Submission):
    def author(self):
        return 'div'


    def run(self, graph):

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

        def length(path):
            """
            return length of the path (extended to a circular one)
            """
            # si l = [1,2,3]
            # zip(l, l[1:]) = [(1,2), (2,3)]
            return sum(graph[x][y] for x,y in zip(path, path[1:])) + graph[path[-1]][path[0]]


        nodes = graph.keys()
        return min((run_from_start(graph, x) for x in nodes), key=length )
