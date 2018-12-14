"""TypeTable
@authorized by Genne Chung
@description: save Type values
"""

from .Table import *

import sys
sys.path.insert(0, "../")

from Interpreter.type.Type import *
from Interpreter.type.Arrow import *
from Interpreter.type.Ptr import *

Int_index = 0
Float_index = 1
Char_index = 2

class TypeTable(Table):
    types = []
    
    def __init__(self):
        self.types = [Int, Float, Char]
        
    def __str__(self):
        ret_str = self.create_header("Type Table")
        
        for i in range(len(self.types)):
            ret_str += "<{}> {}".format(i, str(self.types[i]))
            ret_str += "\n"
        
        ret_str += self.footer
        return ret_str

    def check(self, check_type):
        """

        :param check_type: type Type
        :return: index
        """
        for i in range(len(self.types)):
            if self.check_one_type(self.types[i], check_type):
                return i

        return self.push(check_type)

    def check_one_type(self, checked_type, check_type):
        """

        :param check_type: type Type
        :return: boolean
        """
        return checked_type.is_same_type(check_type)

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
