from submission import Submission


class ProfSubmission(Submission):

    def author(self):
        return 'prof-greedy'

    def run(self, input):

        def greedynearesttsp(distancematrix, origin=None) :
            nodes = set(distancematrix.keys())
            length = 0
            if origin not in nodes:
                origin = nodes.pop()
            chemin = [origin]
            o=origin
            while len(nodes)>0 :
                distances = distancematrix[o]
                l, o = min((distances[x],x) for x in distances.keys() & nodes)
                length += l
                nodes.remove(o)
                chemin += [o]
            length += distancematrix[o][origin]
            return chemin

        return greedynearesttsp(input)
