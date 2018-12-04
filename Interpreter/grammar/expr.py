""" module expr, containing Expr, TwoParamsExpr, Add, Sub, etc. For Grammar.
** Might be unused after **
@authorized by Genne Chung
"""

import abc

from enum import Enum


class Expr:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __name__(self):
        pass

    
class TwoParamsExpr(Expr):
    left = None
    right = None
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.__name__()) + "(" + str(self.left) + ", " + str(self.right) + ")"


class Err(Expr):
    """ This class is for Syntax Error. **Not for Semantic Err**
    """
    err_msg = ""
    
    def __str__(self):
        return "Error: " + self.err_msg
    
    def __init__(self, err_msg):
        self.err_msg = err_msg


class Id(Expr):
    id_name = ""  # should be string type

    def __init__(self, id_name):
        self.id_name = id_name
        
    def __str__(self):
        return "Id(" + self.id_name + ")"
        

class Value(Expr):
    value = None  # -> ExprV
    
    def __init__(self, value):
        self.value = value
        
        
class Add(TwoParamsExpr):
    pass
      

class Sub(TwoParamsExpr):
    pass
    
        
class Div(TwoParamsExpr):
    pass

    
class Mul(TwoParamsExpr):
    pass
    

class Set(Expr):
    id_expr = None  # should be class Id
    expr = None  # sub expr

    def __init__(self, id_expr, expr):
        self.id_expr = id_expr
        self.expr = expr
        
    def __str__(self):
        return "Set(" + str(self.id_expr) + ", " + str(self.expr) + ")"


class With(Expr):
    id_expr = None
    val = None
    expr = None
    
    def __init__(self, id_expr, val, expr):
        self.id_expr = id_expr
        self.val = val
        self.expr = expr
 
 
class Decl(Expr):
    id_expr = None
    id_type = None
    
    def __init__(self, id_expr, id_type):
        self.id_expr = id_expr
        self.id_type = id_type
        
    def __str__(self):
        return "Decl(" + str(self.id_type) + " " + str(self.id_expr) + ")"
