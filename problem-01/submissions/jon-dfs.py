from submission import Submission
import collections
import random

class JonDfsSubmission(Submission):

    def author(self):
        return 'jon-dfs'

    def run(self, input):

        class Traveler(object):

            def __init__(self, graph, start_point):
                if start_point not in graph:
                    raise Exception("Start point not in the graph")
                self._graph = graph
                self._current = start_point
                self._history = [start_point]

            def possibilities(self):
                return self._graph[self._current]

            def goto(self, position):
                if position in self.possibilities():
                    self._current = position
                    self._history.append(position)
                else:
                    raise Exception("Not possible, try again.")

            def current(self):
                return self._current

            def step_count(self):
                return len(self._history) - 1

            def travel_path(self):
                return list(self._history)

        class ShuffledTraveler(Traveler):

            def __init__(self, graph, start_point):
                super().__init__(graph, start_point)

            def possibilities(self):
                l = super().possibilities()[:]
                random.shuffle(l)
                return l

        def connected_component_using_shorter_dfs(traveler):
            visited = {traveler.current()}
            found = set(traveler.possibilities())
            found.add(traveler.current())
            path = [] # Path to the starting point
            while len(visited) < len(found):
                new_found = False
                for node in traveler.possibilities():
                    # Ignore already visited nodes to avoid loops !
                    if node not in visited:
                        path.append(traveler.current())
                        traveler.goto(node)
                        new_found = True
                        break
                if not new_found:
                    if len(path) > 0:
                        traveler.goto(path.pop())
                    else:
                        break
                visited.add(traveler.current())
                found.update(traveler.possibilities())
            return visited

        graph, start = input
        traveler = ShuffledTraveler(graph, start)
        connected_component_using_shorter_dfs(traveler)
        return traveler.travel_path()
