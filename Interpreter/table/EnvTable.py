"""EnvTable
@authorized by Genne Chung
@description: save Variable values
"""

from .Table import *

import sys
sys.path.insert(0, "../")

from Interpreter.type.Type import *
from Interpreter.type.Arrow import *
from Util.Debug import Debug

log = Debug("EnvTable")


class EnvTable(Table):

    variables = []

    def __init__(self):
        self.variables = []

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
    
    def get_arrow_value_str(self, var, memory):
        return "proc({})".format(memory.get(var.get_value_index()).get_statement().value)

    def get_arrow_params_str(self, var, memory):
        return "params({})".format(self.params_to_str(memory.get(var.get_value_index()).get_params()))

    def params_to_str(self, params):
        ret_str = ""
        if len(params) > 0:
            for i in range(len(params) - 1):
                ret_str += str(params[i])
                ret_str += ", "

            ret_str += str(params[len(params) - 1])
        return ret_str
    
    def simpleStr(self, tt, memory):
        ret_str = self.create_ret_str()
        
        for i in range(len(self.variables)):
            var = self.variables[i]
            if var.get_type_index() > 2:
                if tt.get(var.get_type_index()).__name__() == Name.PTR:
                    ret_str += "<{}> {} {} = {}".format(
                        i,
                        tt.get(var.get_type_index()),
                        var.get_name(),
                        self.get_ptr_value_str(var, tt, memory)
                    )
                    ret_str += "\n"
                else:
                    ret_str += "<{}> def {}{}: {} {}".format(
                        i,
                        var.get_name(),
                        tt.get(var.get_type_index()),
                        self.get_arrow_params_str(var, memory),
                        self.get_arrow_value_str(var, memory)
                    )
                    ret_str += "\n"
            else:
                ret_str += "<{}> {} {} = {}".format(
                    i,
                    tt.get(var.get_type_index()),
                    var.get_name(),
                    memory.get(var.get_value_index())
                )
                ret_str += "\n"
        
        ret_str += self.footer
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
        
        ret_str += self.footer
        return ret_str
    
    def find_index_with_name(self, name_str):
        for i in range(len(self.variables)):
            if name_str == self.variables[i].get_name():
                return i 
        return -1 # 그런 변수 없음

    def get_arrows(self, tt):
        arrows = []
        for i in range(len(self.variables)):
            var_type = tt.get(self.variables[i].get_type_index())
            if type(var_type) == Arrow:
                arrows.append(self.variables[i])

        return arrows

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
