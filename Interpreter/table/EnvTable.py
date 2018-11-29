"""TypeTable
@authorized by Genne Chung
@description: save Type values
"""

from .Table import *

import sys
sys.path.insert(0, "../")

from type import *
from type.Type import *


class EnvTable(Table):
    variables = []
        
    def __str__(self):
        ret_str = ""
        ret_str += "**************************\n"
        ret_str += "******* Env Table *******\n"
        ret_str += "**************************\n"
        
        for i in range(len(self.variables)):
            ret_str += "<{}> {}".format(i, str(self.variables[i]))
            ret_str += "\n"
        
        ret_str += "**************************\n"
        return ret_str
    
    def get(self, index):
        if index < 0 and index >= len(self.variables):
            return -1
        else:
            return self.variables[index]
        
    def push(self, elem):
        self.variables.append(elem)
        return len(self.variables)
    
    def pop(self):
        return self.variables.pop()
    
    def print_element(self, index):
        print(self.variables[index])
