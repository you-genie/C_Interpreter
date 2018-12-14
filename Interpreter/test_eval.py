
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


def interface(grammar, proc):
    a.vm.set_proc(proc)
    print(a.interp(grammar))
    print(a.vm.env_to_string())

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


print(a.vm.env_to_string())


test = Decl(Id("X"), Float)
test_sub = Set(Id("X"), Sub(IntV(15), FloatV(12.3)))

test_set_val = Set(Id("X"), IntV(4))
test_add = Set(Id("X"), Add(IntV(15), FloatV(3.5)))
interface(test, 1)
a.interp(test)
a.vm.set_proc(1)
# a.interp(test_set_val)
a.vm.set_proc(2)
a.interp(test_add)

interface(CondE(IntV(15), FloatV(15)), 4)
interface(If(CondG(IntV(15), CharV(16))), 5)
interface(DeclAndSet(Id("Y"), Int, IntV(13)), 7)
interface(Fun(Int, "function", [Int, Char], 1), 8)

interface(Print("I set X this value %f", [Id("Y")]), 6)

# print(a.vm.env_to_string())
# print(a.vm.get_history("X"))


# test3 = DeclAndSet(Id("set"), Int, Sub(IntV(14), IntV(19)))
test4 = Set(Id("Y"), CharV('d'))

test1 = Decl([Id("Y")], Char)


# a.interp(test)

# print(a.vm.env_to_string())
# a.interp(test1)
# print(a.vm.env_to_string())

# a.interp(test_set_val)
# a.interp(test_add)
# a.interp(test5)

# print(a.vm.env_to_string())
# print(a.vm.get_history("set"))


