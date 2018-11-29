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
    
    def get_ptr_value_str(self, var, tt, memory):
        ptr_type = tt.get(var.get_type_index())
        ret_str = "["
        for i in range(ptr_type.array_size - 1):
            ret_str += str(memory.get(var.get_value_index() + i))
            ret_str += ", "
        ret_str += str(memory.get(var.get_value_index() + ptr_type.array_size - 1))
        ret_str += "]"
        
        return ret_str
            
    
    def simpleStr(self, tt, memory):
        ret_str = self.create_ret_str()
        
        for i in range(len(self.variables)):
            var = self.variables[i]
            if var.get_type_index() > 2:
                if tt.get(var.get_type_index()).__name__() == Name.PTR:
                    ret_str += "<{}> ({}) {} = {}".format(
                        i,
                        tt.get(var.get_type_index()),
                        var.get_name(),
                        self.get_ptr_value_str(var, tt, memory)
                    )
                    ret_str += "\n"
            else: 
                ret_str += "<{}> ({}) {} = {}".format(
                    i,
                    tt.get(var.get_type_index()),
                    var.get_name(),
                    memory.get(var.get_value_index())
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
    
    def find_index_with_name(self, name_str):
        for i in range(len(self.variables)):
            if name_str == self.variables[i].get_name():
                return i 
        return -1 # 그런 변수 없음
    
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
