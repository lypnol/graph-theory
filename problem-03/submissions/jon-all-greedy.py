from submission import Submission

class JonAllGreedyGreedy(Submission):

    def author(self):
        return "jon-all-greedy"

    def run(self, input):

        def salesman_greedy_for_complete_graph_from_node(wgraph, start_node):
            not_found = set(wgraph.keys()) - {start_node}
            path = [start_node]
            path_length = 0
            while len(not_found) > 0:
                nearest_node = min(not_found, key= lambda n: wgraph[path[-1]][n])
                path_length += wgraph[path[-1]][nearest_node]
                path.append(nearest_node)
                not_found.remove(nearest_node)
            # Return to start node
            path_length += wgraph[path[-1]][start_node]
            path.append(path[0])
            return (path_length, path)

        def salesman_greedy_for_complete_graph(wgraph):
            return min(
                    (salesman_greedy_for_complete_graph_from_node(wgraph, start_node)
                            for start_node in wgraph.keys()),
                    key= lambda x: x[0])

        return salesman_greedy_for_complete_graph(input)[1][:-1]
