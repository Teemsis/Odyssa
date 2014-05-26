from Data import Data

class TimeSeries(Data):
    
    def __init__(self, time, label, hidden):
        self.time = time
        self.label = label
        self.hidden = hidden
    
    def addSample(self):
        raise Exception("This method must be implemented")
    
    def reSample(self):
        raise Exception("This method must be implemented")
    
    def max(self):
        raise Exception("This method must be implemented")
    
    def min(self):
        raise Exception("This method must be implemented")
    
    def updatePlot(self, srv, evtData):
        raise Exception("This method must be implemented")
    
    def deletion(self, src, evtData):
        raise Exception("This method must be implemented")
    
    def spy(self):
        raise Exception("This method must be implemented")
    
    def replot(self, src, evtData):
        raise Exception("This method must be implemented")
    
    def deletefcn(self, src, evtData):
        raise Exception("This method must be implemented")