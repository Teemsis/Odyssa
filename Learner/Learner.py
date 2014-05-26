#Abstract class
class Learner:
    
    def __init__(self):
        raise Exception("Abstract class 'Learner' can't be instancied")
    
    def run(self):
        raise Exception("Abstract method must be implemented")