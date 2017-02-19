from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'ayoub'

    def run(self, input):
        graph = input

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

            while (left is not None) or (right is not None):
                if left is not None:
                    path.insert(0, left)
                if right is not None:
                    path.append(right)

                if left is not None:
                    left = closest(left, visited)
                    visited.add(left)

                if right is not None:
                    right = closest(right, visited)
                    visited.add(right)

            return path

        min_l = float('inf')
        min_p = []
        for s in graph:
            path = traversal(s)
            l = sum([graph[path[i]][path[i+1]] for i in range(len(path) - 1)])
            if l < min_l:
                min_l = l
                min_p = [path]
            elif l == min_l:
                min_p.append(path)

        min_p = sorted(min_p, key=lambda x: len(x))

        return min_p[0]
