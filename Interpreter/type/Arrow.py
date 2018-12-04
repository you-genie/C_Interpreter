"""arrow type, also known as function types
@authorized by Genne Chung
Arrow class overrides Type
"""
from abc import ABC

from .Type import *


class Arrow(Type, ABC):
    
    params = []
    ret = None
    
    def __name__(self):
        return Name.ARROW
        
    def __init__(self, types, type_ret):
        self.params = types
        self.ret = type_ret
        
    def __str__(self):
        params_str = ""
        for i in range(len(self.params) - 1):
            params_str += str(self.params[i])
            params_str += ", "

        params_str += str(self.params[len(self.params) - 1])
        
        return "({}) -> {}".format(params_str, self.ret)
