import sys
sys.path.insert(0, "../../Util")

from Type import *


class Arrow(Type):
    
    params = []
    ret = Int
    
    def __init__(self, types, type_ret):
        self.params = types
        self.ret = type_ret
        
    def __str__(self):
        params_str = ""
        for param in params:
            params_str += param
            params_str += " "
        params_str.strip()
        return "({}) -> {}".format(params_str, self.ret)
    