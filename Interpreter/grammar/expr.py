import abc

from enum import Enum

names = ["Id", "ExprV", "Add", "Sub", "Mul", "Div", "Set", "Decl"]

class Name(Enum):
    ID = 0
    EXPR_V = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    SET = 6
    DECL = 7
    
    def __int__(self):
        return self.value
    
    def __str__(self):
        return names[self.value]
    

class Expr:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __name__(self):
        pass

    
class TwoParamsExpr(Expr):
    left = None
    right = None
    
    def __name__(self):
        pass
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.__name__()) + "(" + str(self.left) + ", " + str(self.right) + ")"
    

class Id(Expr):
    id_name  = "" # should be string type
    
    def __name__(self):
        return Name.ID

    def __init__(self, id_name):
        self.id_name = id_name
        
    def __str__(self):
        return "Id(" + self.id_name + ")"
        

class Value(Expr):
    value = None# -> ExprV
    
    def __name__(self):
        return Name.EXPR_V
    
    def __init__(self, value):
        self.value = value
        
class Add(TwoParamsExpr):
    
    def __name__(self):
        return Name.ADD

        
class Sub(TwoParamsExpr):
    
    def __name__(self):
        return Name.SUB
    
        
class Div(TwoParamsExpr):
    
    def __name__(self):
        return Name.DIV

class Mul(TwoParamsExpr):
    
    def __name__(self):
        return Name.MUL

class Set(Expr):
    id_expr = None# should be class Id
    expr = None# sub expr
    
    def __name__(self):
        return Name.SET
    
    def __init__(self, id_expr, expr):
        self.id_expr = id_expr
        self.expr = expr
        
    def __str__(self):
        return "Set(" + str(self.id_expr) + ", " + str(self.expr) + ")"
        
class Decl(Expr):
    id_expr = Expr()
    
    def __name__(self):
        return Name.DECL
    
    def __init__(self, id_expr):
        self.id_expr = id_expr
        
    def __str__(self):
        return "Decl(" + str(self.id_expr) + ")"
        