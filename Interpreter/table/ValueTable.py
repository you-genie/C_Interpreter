"""ValueTable
@authorized by Genne Chung
@description: for saving "values", especially on array values
"""

from .Table import *

import sys
sys.path.insert(0, "../")

from type import *
from type.Type import *


class ValueTable(Table):
    values = []
            
    def __str__(self):
        ret_str = ""
        ret_str += "############################\n"
        ret_str += "######## Main Memory #######\n"
        ret_str += "############################\n"
        
        for i in range(len(self.values)):
            ret_str += "<{}> {}".format(i, str(self.values[i]))
            ret_str += "\n"
        
        ret_str += "############################\n"
        return ret_str
    
    def get(self, index):
        if index < 0 and index >= len(self.values):
            return -1
        else:
            return self.values[index]
        
    def push(self, elem):
        self.values.append(elem)
        return len(self.values)
    
    def pop(self):
        return self.values.pop()
    
    def print_element(self, index):
        print(self.values[index])
