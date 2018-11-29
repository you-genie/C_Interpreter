"""TypeTable
@authorized by Genne Chung
@description: save Type values
"""

from .Table import *

class HistoryTable(Table):
    histories = []
    
    def __str__(self):
            ret_str = self.create_header("Histories")

            for i in range(len(self.histories)):
                ret_str += "<{}> histories: {}".format(i, self.histories[i].size())
                ret_str += "\n"

            ret_str += self.footer
            return ret_str

    def get(self, index):
        if index < 0 and index >= len(self.histories):
            return -1
        else:
            return self.histories[index]

    def push(self, elem):
        self.histories.append(elem)
        return len(self.histories) - 1

    def pop(self):
        return self.values.pop()

    def print_element(self, index):
        print(self.histories[index])
            
class Log:
    proc = -1
    value = -1
    
    def __init__(self, proc, value):
        self.proc = proc
        self.value = value
    
    def __str__(self):
        return str(self.value)

class History(Table):
    logs = []
    
    def __init__(self):
        self.logs = []
        
    def __str__(self):
        ret_str = self.create_header("History")

        for i in range(len(self.logs)):
            ret_str += "<{}> {}".format(
                self.logs[i].proc, 
                str(self.logs[i].value)
            )
            ret_str += "\n"
        
        ret_str += self.footer
        return ret_str
    
    def get(self, index):
        if index < 0 and index >= len(self.logs):
            return -1
        else:
            return self.logs[index]
        
    def size(self):
        return len(self.logs)

    def push(self, elem):
        log = Log(elem[0], elem[1])
        self.logs.append(log)
        return len(self.logs) - 1
    
    def pop(self):
        return self.logs.pop()
    
    def print_element(self, index):
        print(self.logs[index])
