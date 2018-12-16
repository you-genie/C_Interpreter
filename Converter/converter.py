from Parser.Util.ASTName import ASTName
from Interpreter.var import *
from Interpreter.grammar.expr import *
from Interpreter.grammar.value import *
from Interpreter.type.Type import CharClass, FloatClass, IntClass

class Converter():
    def __init__(self):
        pass

    def translate(self, expr):
        if expr.get_name() == ASTName.NUM:
            if expr.get_child('type').get_name() == ASTName.INT: return IntV(expr.get_data())
            elif expr.get_child('type').get_name() == ASTName.FLOAT: return FloatV(expr.get_data())
            else: return None
        elif expr.get_name() == ASTName.ID: return Id(expr.get_data())
        elif expr.get_name() == ASTName.ARRAY:
            return PtrV(self.translate(expr.get_child('id')), self.translate(expr.get_child('index')))
        elif expr.get_name() == ASTName.DECL: return None
        elif expr.get_name() == ASTName.IDS: return None
        elif expr.get_name() == ASTName.INT: return Int
        elif expr.get_name() == ASTName.INTP: return Ptr(Int)
        elif expr.get_name() == ASTName.FLOAT: return Float
        elif expr.get_name() == ASTName.FLOATP: return Ptr(Float)
        elif expr.get_name() == ASTName.ASSIGN:
            if expr.get_child('lvalue').get_name() == ASTName.ID:
                return Set(self.translate(expr.get_child('lvalue')), self.translate(expr.get_child('rvalue')))
            elif expr.get_child('lvalue').get_name() == ASTName.ARRAY:
                return Set([self.translate(expr.get_child('lvalue').get_child('id')),
                    self.translate(expr.get_child('lvalue').get_child('index'))], self.translate(expr.get_child('rvalue')))
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
        elif expr.get_name() == ASTName.NOT:
            return Not(self.translate(expr.get_child('value')))
        elif expr.get_name() == ASTName.EQ:
            return CondE(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
        elif expr.get_name() == ASTName.NEQ:
            return CondNE(self.translate(expr.get_child('left')), self.translate(expr.get_child('right')))
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
        elif expr.get_name() == ASTName.RET:
            return Ret(self.translate(expr.get_child('value')))
        elif expr.get_name() == ASTName.FUNCCALL:
            if expr.get_data() != None: return expr.get_data()
            else: return App(self.translate(expr.get_child('id')), self.translate(expr.get_child('args')))
        elif expr.get_name() == ASTName.ARGS:
            return list(map(lambda x: self.translate(x), expr.get_data()))
        elif expr.get_name() == ASTName.PRINT:
            return Print(expr.get_child('str').get_data(), self.translate(expr.get_child('args')))
        elif expr.get_name() == ASTName.ERROR: return None
        else: return None


    def get_app(self, expr):
        if expr.get_name() == ASTName.NUM: return None
        elif expr.get_name() == ASTName.ID: return None
        elif expr.get_name() == ASTName.ARRAY:
            return self.get_app(expr.get_child('index'))
        elif expr.get_name() == ASTName.DECL:
            return self.get_app(expr.get_child('ids'))
        elif expr.get_name() == ASTName.IDS:
            for a_id in expr.get_data():
                if self.has_app(a_id): return self.get_app(a_id)
            return None
        elif (expr.get_name() == ASTName.INT or expr.get_name() == ASTName.INTP or
                expr.get_name() == ASTName.FLOAT or expr.get_name() == ASTName.FLOATP):
            return None
        elif expr.get_name() == ASTName.ASSIGN:
            return self.get_app(expr.get_child('rvalue'))
        elif expr.get_name() == ASTName.NOT:
            return self.get_app(expr.get_child('value'))
        elif (expr.get_name() == ASTName.PLUS or expr.get_name() == ASTName.MINUS or
                expr.get_name() == ASTName.MULTI or expr.get_name() == ASTName.DIV or
                expr.get_name() == ASTName.EQ or expr.get_name() == ASTName.NEQ or
                expr.get_name() == ASTName.LESS or expr.get_name() == ASTName.LESSEQ or
                expr.get_name() == ASTName.GREATER or expr.get_name() == ASTName.GREATEREQ):
            if self.has_app(expr.get_child('left')): return self.get_app(expr.get_child('left'))
            elif self.has_app(expr.get_child('right')): return self.get_app(expr.get_child('right'))
            else: return None
        elif (expr.get_name() == ASTName.INCR or expr.get_name()) == ASTName.DECR:
            return None
        elif expr.get_name() == ASTName.IF:
            return self.get_app(expr.get_child('cond'))
        elif expr.get_name() == ASTName.FOR:
            return self.get_app(expr.get_child('init'))
        elif expr.get_name() == ASTName.FUNCDEFINE: return None
        elif expr.get_name() == ASTName.PARAM: return None
        elif expr.get_name() == ASTName.PARAMS: return None
        elif expr.get_name() == ASTName.RET:
            return self.get_app(expr.get_child('value'))
        elif expr.get_name() == ASTName.FUNCCALL:
            if self.has_app(expr.get_child('args')): return self.get_app(expr.get_child('args'))
            else: return expr
        elif expr.get_name() == ASTName.ARGS:
            for arg in expr.get_data():
                if self.has_app(arg): return self.get_app(arg)
            return None
        elif expr.get_name() == ASTName.PRINT:
            return self.get_app(expr.get_child('args'))
        else: return None


    def has_app(self, expr):
        if expr.get_name() == ASTName.NUM: return False
        elif expr.get_name() == ASTName.ID: return False
        elif expr.get_name() == ASTName.ARRAY:
            return self.has_app(expr.get_child('index'))
        elif expr.get_name() == ASTName.DECL:
            return self.has_app(expr.get_child('ids'))
        elif expr.get_name() == ASTName.IDS:
            for a_id in expr.get_data():
                if self.has_app(a_id): return True
            return False
        elif (expr.get_name() == ASTName.INT or expr.get_name() == ASTName.INTP or
                expr.get_name() == ASTName.FLOAT or expr.get_name() == ASTName.FLOATP):
            return False
        elif expr.get_name() == ASTName.ASSIGN:
            return self.has_app(expr.get_child('rvalue'))
        elif expr.get_name() == ASTName.NOT:
            return self.has_app(expr.get_child('value'))
        elif (expr.get_name() == ASTName.PLUS or expr.get_name() == ASTName.MINUS or
                expr.get_name() == ASTName.MULTI or expr.get_name() == ASTName.DIV or
                expr.get_name() == ASTName.EQ or expr.get_name() == ASTName.NEQ or
                expr.get_name() == ASTName.LESS or expr.get_name() == ASTName.LESSEQ or
                expr.get_name() == ASTName.GREATER or expr.get_name() == ASTName.GREATEREQ):
            return self.has_app(expr.get_child('left')) or self.has_app(expr.get_child('right'))
        elif (expr.get_name() == ASTName.INCR or expr.get_name()) == ASTName.DECR:
            return False
        elif expr.get_name() == ASTName.IF:
            return self.has_app(expr.get_child('cond'))
        elif expr.get_name() == ASTName.FOR:
            return self.has_app(expr.get_child('init'))
        elif expr.get_name() == ASTName.FUNCDEFINE: return False
        elif expr.get_name() == ASTName.PARAM: return False
        elif expr.get_name() == ASTName.PARAMS: return False
        elif expr.get_name() == ASTName.RET:
            return self.has_app(expr.get_child('value'))
        elif expr.get_name() == ASTName.FUNCCALL:
            if expr.get_data() == None: return True
            else: return self.has_app(expr.get_child('args'))
        elif expr.get_name() == ASTName.ARGS:
            for arg in expr.get_data():
                if self.has_app(arg): return True
            return False
        elif expr.get_name() == ASTName.PRINT:
            return self.has_app(expr.get_child('args'))
        else: return False


    def find_and_replace_rax(self, expr, value):
        if expr.get_name() == ASTName.NUM: return False
        elif expr.get_name() == ASTName.ID: return False
        elif expr.get_name() == ASTName.ARRAY:
            return self.find_and_replace_rax(expr.get_child('index'), value)
        elif expr.get_name() == ASTName.DECL:
            return self.find_and_replace_rax(expr.get_child('ids'), value)
        elif expr.get_name() == ASTName.IDS:
            for a_id in expr.get_data():
                if self.find_and_replace_rax(a_id): return True
            return False
        elif (expr.get_name() == ASTName.INT or expr.get_name() == ASTName.INTP or
                expr.get_name() == ASTName.FLOAT or expr.get_name() == ASTName.FLOATP):
            return False
        elif expr.get_name() == ASTName.ASSIGN:
            return self.find_and_replace_rax(expr.get_child('rvalue'), value)
        elif expr.get_name() == ASTName.NOT:
            return self.find_and_replace_rax(expr.get_child('value'), value)
        elif (expr.get_name() == ASTName.PLUS or expr.get_name() == ASTName.MINUS or
                expr.get_name() == ASTName.MULTI or expr.get_name() == ASTName.DIV or
                expr.get_name() == ASTName.EQ or expr.get_name() == ASTName.NEQ or
                expr.get_name() == ASTName.LESS or expr.get_name() == ASTName.LESSEQ or
                expr.get_name() == ASTName.GREATER or expr.get_name() == ASTName.GREATEREQ):
            if self.find_and_replace_rax(expr.get_child('left'), value): return True
            elif self.find_and_replace_rax(expr.get_child('right'), value): return True
            else: return False
        elif (expr.get_name() == ASTName.INCR or expr.get_name()) == ASTName.DECR:
            return False
        elif expr.get_name() == ASTName.IF:
            return self.find_and_replace_rax(expr.get_child('cond'), value)
        elif expr.get_name() == ASTName.FOR:
            return self.find_and_replace_rax(expr.get_child('init'), value)
        elif expr.get_name() == ASTName.FUNCDEFINE: return False
        elif expr.get_name() == ASTName.PARAM: return False
        elif expr.get_name() == ASTName.PARAMS: return False
        elif expr.get_name() == ASTName.RET:
            return self.find_and_replace_rax(expr.get_child('value'), value)
        elif expr.get_name() == ASTName.FUNCCALL:
            if expr.get_RAX() == 1:
                expr.RAX = 0;
                expr.data = value
                return True
            return self.find_and_replace_rax(expr.get_child('args'), value)
        elif expr.get_name() == ASTName.ARGS:
            for arg in expr.get_data():
                if self.find_and_replace_rax(arg, value): return True
            return False
        elif expr.get_name() == ASTName.PRINT:
            return self.find_and_replace_rax(expr.get_child('args'), value)
        else: return False