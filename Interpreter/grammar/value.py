""" value module, containing ExprV(interface), IntV, CharV, FloatV.
@authorized by Genne Chung
"""

import abc


class ExprV:
    value = None
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.__name__() + "V(" + str(self.value) + ")"
    

class IntV(ExprV):
    
    def __name__(self):
        return "Int"
    
    pass


class FloatV(ExprV):
    
    def __name__(self):
        return "Float"
    
    pass


class CharV(ExprV):
    
    def __name__(self):
        return "Char"
    
    pass


class VoidV(ExprV):

    def __name__(self):
        return "Void"

    pass


class ErrV(ExprV):

    def __name__(self):
        return "Error"

    def printErr(self):
        print("Error: " + self.value)

    pass


class BoolV(ExprV):

    def __name__(self):
        return "Bool"

    pass


class IfV(ExprV):

    def __name__(self):
        return "If"

    pass


class ForV(ExprV):

    def __name__(self):
        return "For"

    pass