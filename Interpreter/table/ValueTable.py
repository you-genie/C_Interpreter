"""ValueTable
@authorized by Genne Chung
@description: for saving "values", especially on array values
그냥 메모리이다.
"""

from .Table import *

import sys
sys.path.insert(0, "../")


class ValueTable(Table):
    values = []
            
    def __str__(self):
        ret_str = self.create_header("Main Memory")
        
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
        
    def set_val(self, index, val):
        if index < 0 and index >= len(self.values):
            return -1
        else:
            self.values[index] = val
        
    def push(self, elem):
        self.values.append(elem)
        return len(self.values) - 1
    
    def pop(self):
        return self.values.pop()
    
    def print_element(self, index):
        print(self.values[index])
