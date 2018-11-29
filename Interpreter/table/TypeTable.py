"""TypeTable
@authorized by Genne Chung
@description: save Type values
"""

from .Table import *

import sys
sys.path.insert(0, "../")

from type import *
from type.Type import *


class TypeTable(Table):
    types = []
    
    def __init__(self):
        self.types = [Int, Float, Char]
        
    def __str__(self):
        ret_str = self.create_header("Type Table")
        
        for i in range(len(self.types)):
            ret_str += "<{}> {}".format(i, str(self.types[i]))
            ret_str += "\n"
        
        ret_str += "-------------------------\n"
        return ret_str
    
    def get(self, index):
        if index < 0 and index >= len(self.types):
            return -1
        else:
            return self.types[index]
        
    def push(self, elem):
        self.types.append(elem)
        return len(self.types) - 1
    
    def pop(self):
        return self.types.pop()
    
    def print_element(self, index):
        print(self.types[index])
