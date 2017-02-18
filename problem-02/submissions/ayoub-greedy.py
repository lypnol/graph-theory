from submission import Submission


class AyoubGreedySubmission(Submission):

    def author(self):
        return 'ayoub-greedy'

    def run(self, input):
        graph, start = input

        def closest(current, exceptions=set()):
            m = float('inf')
            c = None
            for v in graph[current]:
                if v not in exceptions and graph[current][v] < m:
                    m = graph[current][v]
                    c = v
            return c

        def traversal(s):
            path = [s]
            current = s
            visited = { s }

            left = closest(current, visited)
            visited.add(left)
            right = closest(current, visited)
            visited.add(right)

            while left and right:
                path.append(right)
                path.insert(0, left)

                left = closest(left, visited)
                if not left:
                    break
                visited.add(left)

                right = closest(right, visited)
                if not right:
                    break
                visited.add(right)

            d = path.index(start)
            n = len(path)

            return [path[(i + d) % n] for i in range(n)] + [start]

        min_l = float('inf')
        min_p = None
        for s in graph:
            path = traversal(s)
            l = sum([graph[path[i]][path[i+1]] for i in range(len(path) - 1)])
            if l < min_l:
                min_l = l
                min_p = path

        return min_p
