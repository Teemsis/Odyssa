from Data import Data

# try this : import matlibplot.pyplot
# source : http://pandas.pydata.org/pandas-docs/stable/timeseries.html
# source : http://pandas.pydata.org/pandas-docs/stable/visualization.html

class TimeSeries(Data):
    
    __count = 0
    
    def __init__(self, time, label, hidden):
        self.__time = time
        self.__label = label
        #Attribution of a default label value if label given is empty
        if label == "" :
            self.__label = "TimeSeries_label_" + str(TimeSeries.__count)
            TimeSeries.__count += 1
        self.__hidden = hidden
    
    def getTime(self):
        return self.__time
    
    def getLabel(self):
        return self.__label
    
    def getHidden(self):
        return self.__hidden
    
    def setTime(self, time):
        self.__time = time
    
    def setLabel(self, label):
        self.__label = label
    
    def setHidden(self, hidden):
        self.__hidden = hidden
    
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