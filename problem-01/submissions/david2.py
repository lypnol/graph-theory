from submission import Submission

# libs
import queue

class DavidNGSubmission(Submission):
    def author(self):
        return 'div-ng'

    def run(self, input):
        graph, start = input
        print("graph", graph, "| start", start)

        # path est le chemin que l'on parcourt
        path = [start]
        # q est une pile contenant les noeuds visités
        q = queue.LifoQueue()
        q.put(start)

        # on retient la liste des noeuds visités et la liste des noeuds à visiter
        visited = {start}
        to_visit = set(graph[start])

        # pos contient la position du joueur dans le labyrinthe
        pos = start

        # on continue le parcours tant que la liste des noeuds à visiter n'est pas vide
        while to_visit:
            # on retourne en arrière tant qu'on n'a rien à visiter
            while True:
                # liste des noeuds à visiter à proximité
                next_nodes = set(graph[pos]) & to_visit

                if next_nodes:
                    # on en a un à visiter
                    pos = next_nodes.pop()
                    path.append(pos)
                    q.put(pos)
                    # on peut sortir de la boucle
                    break

                # on n'a rien à visiter ici :'(
                # on retourne en arrière
                next_pos = q.get()
                if next_pos != pos:
                    pos = next_pos
                    path.append(pos)
                    q.put(pos)


            # pos est un nouveau noeud jamais visité
            to_visit.remove(pos)
            visited.add(pos)

            # il faudra visiter les voisins pas encore visités
            next_to_visit = set(graph[pos]) - visited
            to_visit.update(next_to_visit)

        return path
