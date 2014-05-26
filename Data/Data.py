#Abstract class
class Data:
    
    def __init__(self):
        raise Exception("Abstract class 'Data' can't be instancied")
    
    def plot(self):
        raise Exception("Abstract method must be implemented")