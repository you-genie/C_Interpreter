""" eval module containing Interp class.
@authorized by Genne Chung
containing basic interpreter.

* uses lambda functions for interpretation
* uses dictionaries for switching function.
"""

from Interpreter.var import *
from table import *
from table.TypeTable import *
from table.HistoryTable import *
from table.ValueTable import *
from table.EnvTable import *
from grammar.value import *

from Interpreter.grammar.expr import *
from Interpreter.grammar.value import CharV, FloatV, IntV
from Interpreter.type.Type import CharClass, FloatClass, IntClass


class Interp:
    vm = None

    def return_value(self, expr):
        return expr
    
    def ae_two(self, expr, op):
        return op(
            self.interp(expr.left).value,
            self.interp(expr.right).value
        )
    
    def add(self, expr):
        return self.ae_two(expr, lambda x, y: x + y)
    
    def sub(self, expr):
        return self.ae_two(expr, lambda x, y: x - y)
    
    def mul(self, expr):
        return self.ae_two(expr, lambda x, y: x * y)
    
    def div(self, expr):
        return self.ae_two(expr, lambda x, y: x / y)
    
    def with_(self, expr):
        id_expr = expr.id_expr
        
        if type(id_expr) != Id:
            return Err("Variable is not Id type")
        else:
            value = self.interp(expr.val)
            if type(value) == IntV:
                self.vm.new_int(id_expr.id_name, value)
            elif type(value) == FloatV:
                self.vm.new_float(id_expr.id_name, value)
            elif type(value) == CharV:
                self.vm.new_char(id_expr.id_name, value)
            else:
                return Err("Value is not ExprV type " + str(type(value)))
            return self.interp(expr.expr)
    
    def set_val(self, expr):
        id_expr = expr.id_expr
        
        if type(id_expr) != Id:
            return Err("Variable is not Id type")
        else:
            self.vm.set_var(
                id_expr.id_name,
                self.interp(expr.expr))
            
    def id(self, expr):
        var = self.vm.env.get(
            self.vm.find_index_by_name(expr.id_name))
        value = self.vm.memory.get(var.get_value_index())
        return value
    
    def decl(self, expr):
        ids = expr.ids
        types = {
            IntClass: self.vm.new_int,
            FloatClass: self.vm.new_float,
            CharClass: self.vm.new_char
        }

        for id_expr in ids:
            if type(id_expr) != Id:
                return Err("Variable is not Id type")
            else:
                types[type(expr.id_type)](id_expr.id_name, None)
    
    def __init__(self, tt, histories, env, memory, proc):
        self.vm = VarManager(tt, histories, env, memory, proc)

    def interp(self, expr):
        switch = {
            IntV: self.return_value,
            FloatV: self.return_value,
            CharV: self.return_value,
            Add: self.add,
            Sub: self.sub,
            Mul: self.mul,
            Div: self.div,
            Set: self.set_val,
            Decl: self.decl,
            Id: self.id,
            With: self.with_
        }
        
        return switch[type(expr)](expr)

