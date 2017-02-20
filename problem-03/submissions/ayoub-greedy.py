from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'ayoub'

    def run(self, input):
        graph = input

        def calc_length(p):
            s = 0
            for i in range(len(p)):
                s += graph[p[i]][p[(i+1) % len(p)]]
            return s

        min_path = []
        min_len = float('inf')
        for s in graph:
            current = s
            visited = { s }
            path = [s]
            while len(visited) != len(graph):
                m = float('inf')
                n = None
                for v in graph[current]:
                    if v not in visited and graph[current][v] < m:
                        m = graph[current][v]
                        n = v

                current = n
                path.append(current)
                visited.add(current)

            l = calc_length(path)
            if l < min_len:
                min_len = l
                min_path = path

        return min_path
