from Data import Data

class TimeSeries(Data):
    def __init__(self, time, label, hidden):
        self.time = time
        self.label = label
        self.hidden = hidden