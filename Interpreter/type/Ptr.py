"""This is >>Static<< Pointer type, also known as Array
@authorized by Gennne Chung
"""


from .Type import *


class Ptr(Type):
    element_type = Int()
    array_size = 0

    def __init__(self, element_type, array_size):
        self.element_type = element_type
        self.array_size = array_size
        
    def __str__(self):
        return "{}[{}]".format(self.element_type, self.array_size)

