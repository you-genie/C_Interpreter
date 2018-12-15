from Parser.util.ASTName import ASTName
from Interpreter.var import *
from Interpreter.grammar.expr import *
from Interpreter.grammar.value import *
from Interpreter.type.Type import CharClass, FloatClass, IntClass

class Converter():
    def __init__(self):
        pass

    def translate(self, expr):
        if expr.get_name() == ASTName.NUM: return expr
        elif expr.get_name() == ASTName.ID: return Id(expr.get_data())
        elif expr.get_name() == ASTName.ARRAY: return Ptr()
        elif expr.get_name() == ASTName.DECL: return None
        elif expr.get_name() == ASTName.IDS: return None
        elif expr.get_name() == ASTName.INT: return IntClass
        #elif expr.get_name() == ASTName.INTP: return Ptr()
        elif expr.get_name() == ASTName.FLOAT: return FloatClass
        #elif expr.get_name() == ASTName.FLOATP:
        elif expr.get_name() == ASTName.ASSIGN:
            if expr.get_child('lvalue').get_name() == ASTName.INT:
                return Set(self.translate(expr.get_child('lvalue')), self.translate(expr.get_child('rvalue')))
            elif expr.get_child('lvalue').get_name() == ASTName.ARRAY:
                return Set([expr.get_child('lvalue').get_child('id').get_data(), expr.get_child('lvalue').get_child('index').get_data()], translate(expr.get_child('rvalue')))
            else: return None
        elif expr.get_name() == ASTName.PLUS:
            return Add(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.MINUS:
            return Sub(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.MULTI:
            return Mul(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.DIV:
            return Div(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.INCR:
            return Inc(self.translate(expr.get_child('id')))
        elif expr.get_name() == ASTName.DECR:
            return Dec(self.translate(expr.get_child('id')))
        elif expr.get_name() == ASTName.EQ:
            return CondE(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.LESS:
            return CondL(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.LESSEQ:
            return CondLE(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.GREATER:
            return CondG(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.GREATEREQ:
            return CondGE(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.IF:
            return If(self.translate(expr.get_child('cond')))
        elif expr.get_name() == ASTName.FOR:
            return For(self.translate(expr.get_child('init')))
        elif expr.get_name() == ASTName.FUNCDEFINE: return None
        elif expr.get_name() == ASTName.PARAM: return None
        elif expr.get_name() == ASTName.PARAMS: return None
        elif expr.get_name() == ASTName.RET: return None
            #return Ret(self.translate(expr.get_child('value')))
        elif expr.get_name() == ASTName.FUNCCALL: return None
        elif expr.get_name() == ASTName.ARGS:
            return list(map(lambda x: self.translate(x), expr.get_child('args').get_data()))
        elif expr.get_name() == ASTName.PRINT:
            return Print(expr.get_child('str').get_data(), self.translate(expr.get_child('args')))
        else: return None


    def get_app(self, expr):
        if expr.get_name() == ASTName.NUM: return False
        elif expr.get_name() == ASTName.ID: return False
        elif expr.get_name() == ASTName.ARRAY:
            return self._has_app(expr.get_child('index'))
        elif expr.get_name() == ASTName.DECL:
            return self._has_app(expr.get_child('ids'))
        elif expr.get_name() == ASTName.IDS:
            for a_id in expr.get_data():
                if self._has_app(a_id): return True
            return False
        elif (expr.get_name() == ASTName.INT or expr.get_name() == ASTName.INTP or
                expr.get_name() == ASTName.FLOAT or expr.get_name() == ASTName.FLOATP):
            return False
        elif expr.get_name() == ASTName.ASSIGN:
            return self._has_app(expr.get_child('rvalue'))
        elif (expr.get_name() == ASTName.PLUS or expr.get_name() == ASTName.MINUS or
                expr.get_name() == ASTName.MULTI or expr.get_name() == ASTName.DIV or
                expr.get_name() == ASTName.EQ or #expr.get_name() == ASTName.NEQ or
                expr.get_name() == ASTName.LESS or expr.get_name() == ASTName.LESSEQ or
                expr.get_name() == ASTName.GREATER or expr.get_name() == ASTName.GREATEREQ):
            return self._has_app(expr.get_child('left')) or self._has_app(expr.get_child('right'))
        elif (expr.get_name() == ASTName.INCR or expr.get_name()) == ASTName.DECR:
            return self._has_app(expr.get_child('id'))
        elif expr.get_name() == ASTName.IF:
            return self._has_app(expr.get_child('cond'))
        elif expr.get_name() == ASTName.FOR:
            return self._has_app(expr.get_child('init'))
        elif expr.get_name() == ASTName.FUNCDEFINE: return False
        elif expr.get_name() == ASTName.PARAM: return False
        elif expr.get_name() == ASTName.PARAMS: return False
        elif expr.get_name() == ASTName.RET:
            return self._has_app(expr.get_child('value'))
        elif expr.get_name() == ASTName.FUNCCALL:
            return self._has_app(expr.get_child('args'))
        elif expr.get_name() == ASTName.ARGS:
            for arg in expr.get_data():
                if self._has_app(arg): return True
            return False
        elif expr.get_name() == ASTName.PRINT:
            return self._has_app(expr.get_child('args'))
        else: return False


def _has_app(self, expr):
        if expr.get_name() == ASTName.NUM: return False
        elif expr.get_name() == ASTName.ID: return False
        elif expr.get_name() == ASTName.ARRAY:
            return self._has_app(expr.get_child('index'))
        elif expr.get_name() == ASTName.DECL:
            return self._has_app(expr.get_child('ids'))
        elif expr.get_name() == ASTName.IDS:
            for a_id in expr.get_data():
                if self._has_app(a_id): return True
            return False
        elif (expr.get_name() == ASTName.INT or expr.get_name() == ASTName.INTP or
                expr.get_name() == ASTName.FLOAT or expr.get_name() == ASTName.FLOATP):
            return False
        elif expr.get_name() == ASTName.ASSIGN:
            return self._has_app(expr.get_child('rvalue'))
        elif (expr.get_name() == ASTName.PLUS or expr.get_name() == ASTName.MINUS or
                expr.get_name() == ASTName.MULTI or expr.get_name() == ASTName.DIV or
                expr.get_name() == ASTName.EQ or #expr.get_name() == ASTName.NEQ or
                expr.get_name() == ASTName.LESS or expr.get_name() == ASTName.LESSEQ or
                expr.get_name() == ASTName.GREATER or expr.get_name() == ASTName.GREATEREQ):
            return self._has_app(expr.get_child('left')) or self._has_app(expr.get_child('right'))
        elif (expr.get_name() == ASTName.INCR or expr.get_name()) == ASTName.DECR:
            return self._has_app(expr.get_child('id'))
        elif expr.get_name() == ASTName.IF:
            return self._has_app(expr.get_child('cond'))
        elif expr.get_name() == ASTName.FOR:
            return self._has_app(expr.get_child('init'))
        elif expr.get_name() == ASTName.FUNCDEFINE: return False
        elif expr.get_name() == ASTName.PARAM: return False
        elif expr.get_name() == ASTName.PARAMS: return False
        elif expr.get_name() == ASTName.RET:
            return self._has_app(expr.get_child('value'))
        elif expr.get_name() == ASTName.FUNCCALL:
            return self._has_app(expr.get_child('args'))
        elif expr.get_name() == ASTName.ARGS:
            for arg in expr.get_data():
                if self._has_app(arg): return True
            return False
        elif expr.get_name() == ASTName.PRINT:
            return self._has_app(expr.get_child('args'))
        else: return False
