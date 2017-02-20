# internal deps
from submission import Submission

# 3rd party deps
from itertools import permutations

class David2Submission(Submission):
    def author(self):
        return 'div-2'


    def run(self, graph):
        DEPTH = 2

        def length(path):
            """
            return length of the given path
            """
            return sum(graph[x][y] for x,y in zip(path, path[1:]))


        nb_nodes = len(graph.keys())

        # noeuds à visiter
        to_visit = set(graph.keys())

        # path contient le chemin parcouru
        path = []

        # boucle principale : tant qu'il reste des noeuds à visiter
        while len(path) < nb_nodes:

            p = permutations(to_visit, r=min(len(to_visit), DEPTH))
            subpath = list(min(p, key=lambda _path: length(path + list(_path))))
            to_visit = to_visit - set(subpath)
            path += subpath

        return path
