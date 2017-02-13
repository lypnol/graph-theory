from submission import Submission
import random


class CocoDFSSubmission(Submission):

    def author(self):
        return 'coco-bfs'

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

        def better_dfs(graph, start=None):
            player = ShufflePlayer(graph, position=start)
            previous_nodes = []
            visited = set()
            to_visit = {player.position}
            while True:
                visited.add(player.position)
                if player.position in to_visit:
                    to_visit.remove(player.position)
                voisins = [s for s in player.get_my_neighbours() if s not in visited]
                if not voisins:
                    if previous_nodes == []:
                        # on quitte, on ne peut pas plus remonter
                        break
                    s = previous_nodes.pop()
                    player.go_to(s)
                else:
                    for s in voisins:
                        to_visit.add(s)
                    previous_nodes.append(player.position)
                    player.go_to(voisins[0])
                if not to_visit:
                    break
            return player.path

        graph, start = input

        return better_dfs(graph, start)
