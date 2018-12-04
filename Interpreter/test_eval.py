from var import *

from Interpreter.type.Type import *
from Interpreter.type.Ptr import Ptr
from Interpreter.type.Arrow import Arrow
from Interpreter.eval import Interp
from Interpreter.grammar.expr import *
from Interpreter.grammar.value import FloatV, IntV, CharV
from Interpreter.table.EnvTable import EnvTable
from Interpreter.table.HistoryTable import HistoryTable
from Interpreter.table.TypeTable import TypeTable
from Interpreter.table.ValueTable import ValueTable

tt = TypeTable()
memory = ValueTable()
env = EnvTable()
histories = HistoryTable()

# test = Decl([Id("X")], Int)
# test2 = Decl([Id("a"), Id("b")], Int)
# test_set = Set(Id("X"), IntV(15))
# test_ptr = Decl([Id("array")], Ptr(Int, 3))
# test_ptr_set = Set([Id("array"), 1], CharV('c'))
# test_ptr_set2 = Set([Id("array"), 2], IntV(15))
#
# test_ptr_decl_set = DeclAndSet(Id("arr"), Ptr(Char, 4), [CharV('a'), CharV('b'), IntV('c'), CharV('d')])
#
a = Interp(tt, histories, env, memory, 0)
# print(a.interp(test))
# print(a.vm.env_to_string())
#
# a.interp(test2)
# a.interp(test_ptr)
# # a.interp(test_ptr_set)
# a.interp(test_set)
# print(a.vm.get_history("X"))
#
# a.interp(test_ptr_set)
# a.interp(test_ptr_set2)
#
# a.interp(test_ptr_decl_set)
# print(a.vm.env_to_string())
# print(a.vm.get_history("arr"))

test = Decl([Id("X")], Float)
test2 = Set(Id("X"), Add(IntV(15), CharV('a')))
test3 = DeclAndSet(Id("set"), Int, Sub(IntV(14), IntV(19)))

a.interp(test)
a.interp(test2)
a.interp(test3)

print(a.vm.env_to_string())



