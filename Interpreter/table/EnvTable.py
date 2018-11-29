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
    
    def create_ret_str(self):
        return self.create_header("Env Table")
    
    def simpleStr(self, tt, memory):
        ret_str = self.create_ret_str()
        
        for i in range(len(self.variables)):
            ret_str += "<{}> ({}) {} = {}".format(
                i,
                tt.get(self.variables[i].get_type_index()),
                self.variables[i].get_name(),
                memory.get(self.variables[i].get_value_index())
            )
            ret_str += "\n"
        
        ret_str += "-------------------------\n"
        return ret_str
        
    def __str__(self):
        ret_str = self.create_ret_str()
        
        for i in range(len(self.variables)):
            ret_str += "<{}> tt[{}] | Name: {} | memory[{}]".format(
                i,
                self.variables[i].get_type_index(),
                self.variables[i].get_name(),
                self.variables[i].get_value_index()
            )
            ret_str += "\n"
        
        ret_str += "-------------------------\n"
        return ret_str
    
    def get(self, index):
        if index < 0 and index >= len(self.variables):
            return -1
        else:
            return self.variables[index]
        
    def push(self, elem):
        self.variables.append(elem)
        return len(self.variables) - 1
    
    def pop(self):
        return self.variables.pop()
    
    def print_element(self, index):
        print(self.variables[index])
