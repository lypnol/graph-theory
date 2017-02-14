from submission import Submission
import collections
import random

class JonGreedySubmission(Submission):

    def author(self):
        return 'jon-greedy'

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

            def graph(self):
                return self._graph

        class ShuffledTraveler(Traveler):

            def __init__(self, graph, start_point):
                super().__init__(graph, start_point)

            def possibilities(self):
                l = super().possibilities()[:]
                random.shuffle(l)
                return l

        def connected_component_greedy(traveler):
            graph = traveler.graph() # This could be replaced by a pre-exploration of the graph
            visited = {traveler.current()}
            while True:
                # Find nearest unvisited node
                next_to_visit = None
                explored = set()
                to_explore = collections.deque()
                to_explore.append(traveler.current())
                parent = dict()
                while len(to_explore) > 0:
                    current = to_explore.popleft()
                    explored.add(current)
                    if current not in visited:
                        next_to_visit = current
                        break
                    for successor in graph[current]:
                        if successor not in explored and successor not in to_explore:
                            to_explore.append(successor)
                            parent[successor] = current
                if next_to_visit == None:
                    break

                # Find path to go to next_to_visit, using parent dict
                path = [next_to_visit]
                while parent[path[-1]] != traveler.current():
                    path.append(parent[path[-1]])
                # Follow the path
                while len(path) > 0:
                    traveler.goto(path.pop())

                visited.add(traveler.current())
            return visited

        graph, start = input
        traveler = ShuffledTraveler(graph, start)
        connected_component_greedy(traveler)
        return traveler.travel_path()
