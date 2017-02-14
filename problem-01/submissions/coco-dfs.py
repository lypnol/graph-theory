from submission import Submission
import random


class CocoDfsSubmission(Submission):

    def author(self):
        return 'coco-dfs'

    def run(self, input):

        class ShufflePlayer:
            """
            Joueur qui renvoie une liste aléatoire de ses voisins
            """
            def __init__(self, graph, position=None):
                self.graph = graph
                self.position = position if position is not None else random.choice(list(graph.keys()))
                self.path = [self.position]

            def get_my_neighbours(self):
                neighbours = self.graph[self.position]
                return random.sample(neighbours, len(neighbours))  # random.sample pour eviter de copier la liste

            def go_to(self, point):
                if point in self.get_my_neighbours():  # vérification de la légitimité du déplacement
                    self.position = point
                    self.path.append(point)

        def better_bfs(graph, start=None):
            player = ShufflePlayer(graph, position=start)
            previous_nodes = []
            visited = set()
            to_visit = {player.position}
            while True:
                visited.add(player.position)
                if player.position in to_visit:
                    to_visit.remove(player.position)
                voisins = [s for s in player.get_my_neighbours() if s not in visited]
                for s in voisins:
                    to_visit.add(s)
                if not to_visit:
                    break
                if not voisins:
                    if previous_nodes == []:
                        break # on quitte, on ne peut pas plus remonter
                    s = previous_nodes.pop()
                    player.go_to(s)
                else:
                    previous_nodes.append(player.position)
                    player.go_to(voisins[0])
            return player.path

        graph, start = input

        return better_bfs(graph, start)
