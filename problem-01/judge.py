from judge import Judge

import networkx as nx
import random

class Problem01Judge(Judge):

    def name(self):
        return "Problem-01 Judge"

    def config(self):
        return {
            'default_inputs': 1000
        }

    def generate_input(self):
        n = random.randint(8, 20)
        m = random.randint(10, 40)
        nxgraph = nx.gnm_random_graph(n, m)
        g = {v: list(nxgraph[v]) for v in nxgraph}

        start = random.choice(list(g.keys()))

        return (g, start)

    def validate(self, input, output):

        def is_valid_move(graph, u, v):
            if u not in graph or v not in graph or v not in graph[u]:
                return False
            return True

        def is_complete_path(graph, path, start):
            return path and set(path) == set(nx.node_connected_component(nx.Graph(graph), start))

        (graph, start), path = input, output

        # Vérifier la téléportation
        for i in range(len(path) - 1):
            if not is_valid_move(graph, path[i], path[i+1]):
                return False

        # Vérifier la connexité
        if not is_complete_path(graph, path, start):
            return False

        return True


    def score(self, input, output):
        return len(output)

    def compare(self, a, b):
        if a > b:
            return -1
        elif a < b:
            return 1
        return 0
