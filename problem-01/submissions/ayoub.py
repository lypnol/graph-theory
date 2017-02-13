from submission import Submission
import random
import networkx as nx

class AyoubSubmission(Submission):

    def author(self):
        return 'ayoub'

    def run(self, input):
        graph, start = input

        V = set()               # Noeuds visités
        S = list(graph.keys())  # Liste de tous les noeuds dans le graph
        N = len(S)              # Nombre total des noeuds dans le graph

        # On défini la table de routage suivante
        # pour tout noeuds u, v du graphe:
        #   route[u][v] = [d, p], où
        #     d est la plus courte distance connue entre u et v (en nombre de pas)
        #     p est le prédécesseur de v qui permet d'atteindre u en empruntant le plus court chemin connu.
        route = {v: {v: [float('inf'), None] for v in graph} for v in graph}

        for v in graph:
            route[v][v][0] = 0

        # noeud de départ
        s = start
        if start is None:
            s = random.choice(S)

        # Cette variable servira à savoir si on se dirige vers un noeud connu
        going_to = None

        current = s
        last = None

        path = []

        while True:
            path.append(current)

            # On marque le noeud courant comme visité
            V.add(current)

            # On met à jour la table de routage
            if last is not None:
                # Pour tout noeud visité on vérifie qu'on a bien le plus court
                # chemin dans la table de routage
                for v in V:
                    if route[v][current][0] > route[v][last][0] + 1:
                        route[v][current][0] = route[v][last][0] + 1
                        route[v][current][1] = last

            # On met à jour la variable last
            last = current

            # Si on se dirige vers un noeud connu on utilise la tablde de routage construite
            if going_to:
                if current == going_to:
                    going_to = None
                else:
                    current = route[going_to][current][1]
                    continue

            # Sinon on choisi le noeud suivant selon la règle suivante:
            #  - Si parmi les successeurs du noeud courant on en trouve des non visités
            #    alors on se déplace vers l'un d'entre eux aléatoirement
            #  - Sinon on regarde dans notre table de routage si on a visité un noeud
            #    qui a des successeurs non visités, alors on s'y rend en utilisant
            #    la table de routage. S'il en existe plusieurs on choisi le plus proche.
            #  - Sinon si aucun noeud visité ne possède de successeurs non visités on s'arrête.
            univisited = [u for u in graph[current] if u not in V]
            if univisited:
                current = random.choice(univisited)
            else:
                U = sorted([v for v in V if [u for u in graph[v] if u not in V]],
                           key=lambda x: route[x][current][0])
                if U:
                    going_to = U[0]
                    current = route[going_to][current][1]
                else:
                    break

        return path
