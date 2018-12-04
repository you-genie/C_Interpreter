from var import *
from table import *
from table.TypeTable import *
from table.HistoryTable import *
from table.ValueTable import *
from table.EnvTable import *
from eval import *
from grammar.expr import *
from grammar.value import *

from Interpreter.eval import Interp
from Interpreter.grammar.expr import Decl
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
a = Interp(q, tt, histories, env, memory, 0)
print(a.interp(q))
print(a.vm.envToString())

a.interp(z)
print(a.vm.envToString())
print(a.vm.get_history("q"))


