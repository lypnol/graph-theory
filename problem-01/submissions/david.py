from submission import Submission

class InfiniteLoop(Exception):
    pass

class DavidSubmission(Submission):

    def author(self):
        return 'div'

    def run(self, input):
        graph, start = input

        path = [start] # chemin qui va parcourir tout le graphe
        visited = {start} # ensemble des noeuds de la composante connexe

        pos = start

        # table de routage
        # pour un noeud x
        # elle contient le noeud qui a permis ou permettrait de visiter x pour la 1ere fois
        routes = {x: None for x in list(graph.keys())}
        for s in graph[pos]:
            routes[s] = pos

        # noeuds restants à visiter
        # on fait bien gaffe à faire une copie de la liste
        # histoire d'immutable toussa
        to_visit = [x for x in graph[pos]]

        i = 0

        # les choses serieuses commencent
        while len(to_visit) > 0:

            i+=1
            if i >= 1000:
                raise InfiniteLoop()

            next_pos = to_visit[0]
            # on veut visiter next_pos
            # comment y aller ?

            j = 0
            while next_pos not in graph[pos]:
                j += 1
                if j >= 10:
                    raise InfiniteLoop()

                pos = routes[pos] # on fait marche arrière
                path.append(pos)

            # on est arrivé à un prédécesseur de next_pos
            pos = next_pos
            path.append(next_pos)
            to_visit.remove(next_pos)

            for next_to_visit in graph[next_pos]:
                # on ajoute les successeurs de next_pos a la liste des noeuds à visiter
                if next_to_visit not in visited and next_to_visit not in to_visit:
                    to_visit = [next_to_visit] + to_visit

                # on met a jour la table de routage
                if routes[next_to_visit] is None:
                    routes[next_to_visit] = next_pos

            visited.add(next_pos)

        return path
