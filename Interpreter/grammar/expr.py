""" module expr, containing Expr, TwoParamsExpr, Add, Sub, etc. For Grammar.
** Might be unused after **
@authorized by Genne Chung
"""

import abc
from abc import ABC


class Expr:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __name__(self):
        pass

    
class TwoParamsExpr(Expr, ABC):
    left = None
    right = None
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.__name__()) + "(" + str(self.left) + ", " + str(self.right) + ")"

    pass


class Id(Expr, ABC):
    id_name = ""  # should be string type

    def __init__(self, id_name):
        self.id_name = id_name
        
    def __str__(self):
        return "Id(" + self.id_name + ")"

    pass
        

class Value(Expr, ABC):
    value = None  # -> ExprV
    
    def __init__(self, value):
        self.value = value

    pass
        
        
class Add(TwoParamsExpr, ABC):
    pass
      

class Sub(TwoParamsExpr, ABC):
    pass
    
        
class Div(TwoParamsExpr, ABC):
    pass

    
class Mul(TwoParamsExpr, ABC):
    pass


class CondG(TwoParamsExpr, ABC):
    pass


class CondL(TwoParamsExpr, ABC):
    pass


class CondE(TwoParamsExpr, ABC):
    pass


class CondGE(TwoParamsExpr, ABC):
    pass


class CondLE(TwoParamsExpr, ABC):
    pass
    

class Set(Expr, ABC):
    """
    SET은 list or object를 받는다. 만약에 array size 가 2라면 인덱스가 들어있다는 뜻이다. (이 때문에 그냥 포인터도 물론 가능해지지만, 씀ㅇㄹㅂ몰라)
    """
    id_expr = None  # should be class Id
    expr = None  # sub expr

    def __init__(self, id_expr, expr):
        self.id_expr = id_expr
        self.expr = expr
        
    def __str__(self):
        if type(self.id_expr) == list:
            id_expr_str = str(self.id_expr[0]) + "[" + str(self.id_expr[1]) + "]"
        else:
            id_expr_str = str(self.id_expr)
        return "Set(" + id_expr_str + ", " + str(self.expr) + ")"

    pass
 

class DeclAndSet(Expr, ABC):
    """
    expr이 []인 경우 ptr인 경우밖에 없다. 만약 type(id_type) 이 ptr인 경우 여러 개 읽으면 된다.
    만약에 [] 길이와 ptr array_size? 길이가 다른 경우 err
    """
    id_expr = None
    id_type = None
    expr = None

    def __init__(self, id_expr, id_type, expr):
        self.id_expr = id_expr
        self.id_type = id_type
        self.expr = expr

    def __str__(self):
        if type(self.expr) == list:
            expr_str = "["
            for one_val in self.expr:
                expr_str += str(one_val)
                expr_str += " "
            expr_str += "]"
        else:
            expr_str = str(self.expr)
        return "Declare & Assign(" + str(self.id_type) + " " + str(self.id_expr) + " = " + expr_str

    pass


class Decl(Expr, ABC):
    ids = None # array of Id. GOT IT!
    id_type = None
    
    def __init__(self, ids, id_type):
        self.ids = ids
        self.id_type = id_type
        
    def __str__(self):
        ids_str = ""
        for id in self.ids:
            ids_str += str(id)
        return "Decl(" + str(self.id_type) + " " + ids_str + ")"

    pass


class If(Expr, ABC):
    cond = None

    def __init__(self, cond):
        self.cond = cond

    def __str__(self):
        return "If(" + str(self.cond) + ")"

    pass


class Print(Expr, ABC):
    format_string = None
    args = []

    def __init__(self, string, args):
        self.format_string = string
        self.args = args

    def __str__(self):
        arg_str = ""
        for arg in self.args:
            arg_str += str(arg) + " "
        return "Print(" + str(self.format_string) + arg_str + ")"

    pass


class Fun(Expr, ABC):
    ret_type = None
    fun_name = None
    arg_types = []
    statement = None

    def __init__(self, ret_type, fun_name, arg_types, statement):
        """

        :param ret_type: Return Type, Type Type
        :param fun_name: Function name! string
        :param arg_types: [] of Type
        :param statement: int. Statement index!
        """
        self.ret_type = ret_type
        self.fun_name = fun_name
        self.arg_types = arg_types
        self.statement = statement

    def __str__(self):
        arg_str = ""
        for arg in self.arg_types:
            arg_str += str(arg) + " "
        return "Fun(" + str(self.fun_name) + ": (" + arg_str + ") -> (" + str(self.ret_type) + "))"

    pass
