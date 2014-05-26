from Data import Data

class TimeSeries(Data):
    
    def __init__(self, time, label, hidden):
        self.time = time
        self.label = label
        self.hidden = hidden
    
    def addSample(self):
        pass
    
    def reSample(self):
        pass
    
    def updatePlot(self, srv, evtData):
        pass
    
    def deletion(self, src, evtData):
        pass
    
    def spy(self):
        pass
    
    def replot(self, src, evtData):
        pass
    
    def deletefcn(self, src, evtData):
        pass