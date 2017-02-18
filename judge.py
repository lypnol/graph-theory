
class Judge(object):

    def name(self):
        return 'Anonymous Judge'

    def config(self):
        return {
            'default_inputs': 1,
            'timeout': 1
        }

    def generate_input(self):
        pass

    def validate(self, input, output):
        pass

    def score(self, input, output, runtime):
        pass

    def compare(self, a, b):
        pass
