from submission import Submission

class JonBfSubmission(Submission):

    def author(self):
        return 'jon-bf'

    def run(self, input):
        graph = input
        start = list(graph.keys())[0]

        def length_of_path(path, wgraph):
            return sum(wgraph[path[i]][path[i+1]] for i in range(len(path)-1))

        def permutations(elements):
            if len(elements) < 2:
                yield list(elements)
            else:
                for element in elements:
                    for path in permutations(elements - {element}):
                        yield [element] + path

        def salesman_bruteforce(wgraph, start):
            nodes = set(wgraph.keys()) - {start}
            def create_full_path(path):
                full_path = [start] + path + [start]
                return (length_of_path(full_path, wgraph), full_path)
            return min((create_full_path(p) for p in permutations(nodes)), key= lambda x: x[0])

        return salesman_bruteforce(graph, start)[1]
