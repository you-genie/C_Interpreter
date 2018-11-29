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
            

class History(Table):
    values = []
        
    def __str__(self):
        ret_str = self.create_header("History")

        for i in range(len(self.values)):
            ret_str += "<{}> {}".format(i, str(self.values[i]))
            ret_str += "\n"
        
        ret_str += self.footer
        return ret_str
    
    def get(self, index):
        if index < 0 and index >= len(self.values):
            return -1
        else:
            return self.values[index]
        
    def size(self):
        return len(self.values)

    def push(self, elem):
        self.values.append(elem)
        return len(self.values) - 1
    
    def pop(self):
        return self.values.pop()
    
    def print_element(self, index):
        print(self.values[index])
