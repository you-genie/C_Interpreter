from var import *

from Interpreter.type.Type import *
from Interpreter.type.Ptr import Ptr
from Interpreter.type.Arrow import Arrow
from Interpreter.eval import Interp
from Interpreter.grammar.expr import *
from Interpreter.grammar.value import FloatV, IntV
from Interpreter.table.EnvTable import EnvTable
from Interpreter.table.HistoryTable import HistoryTable
from Interpreter.table.TypeTable import TypeTable
from Interpreter.table.ValueTable import ValueTable

tt = TypeTable()
memory = ValueTable()
env = EnvTable()
histories = HistoryTable()

x = IntV(13)
y = Add(IntV(13), IntV(15))
z = Decl(Id("x"), Int)
p = With(Id("x"), IntV(15), Sub(Id("x"), IntV(4)))
q = With(Id("p"),
         FloatV(1.2),
         With(Id("q"),
              IntV(2.3),
              Add(Id("p"), Id("q"))))
z = Set(Id("q"), FloatV(3.1))
test = Decl([Id("X")], Int)
test2 = Decl([Id("a"), Id("b")], Int)
test_set = Set(Id("X"), IntV(15))
a = Interp(tt, histories, env, memory, 0)
print(a.interp(test))
print(a.vm.envToString())

a.interp(test2)
a.interp(test_set)
print(a.vm.envToString())
print(a.vm.get_history("X"))


