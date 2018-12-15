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


class RetV(ExprV):

    def __name__(self):
        return "Return"

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


class ArrowV(ExprV):

    def __name__(self):
        return "Arrow"

    def __init__(self, params, statement):
        self.value = (params, statement)

    def get_statement(self):
        return self.value[1]

    def get_params(self):
        return self.value[0]

    pass


class AppV(ExprV):

    def __name__(self):
        return "App"

    def __init__(self, env, statement):
        self.value = (env, statement)

    def __str__(self):
        return "AppV(" + str(self.value[0]) + str(self.value[1]) + ")"

    def get_statement(self):
        return self.value[1]

    def get_env(self):
        return self.value[0]

    pass


class PtrV(ExprV):

    def __name__(self):
        return "Ptr"

    def __init__(self, id_expr, index_expr):
        self.value = (id_expr, index_expr)

    def get_id(self):
        return self.value[0]

    def get_index(self):
        return self.value[1]

    def __str__(self):
        return "Ptr(" + str(self.get_id()) + ", " + str(self.get_index()) + ")"

    pass
