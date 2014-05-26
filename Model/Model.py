#Abstract class
class Model:
    
    def __init__(self):
        self.data = None
        self.learner = None
        self.simulator = None
        raise Exception("Abstract class 'Model' can't be instancied")
    
    def simulate(self):
        raise Exception("Abstract method must be implemented")
    
    def learn(self, data):
        raise Exception("Abstract method must be implemented")