""" test_var module
@authrized by Genne Chung

* 테스트용 간이 interpreter 모듈. 
* 실제로 하는 일은 없고 헬퍼 functionality 검사.
* interpreter가 없기 때문에 현재는 그냥 테이블을 전부 만들고, proc를 지정해주었다.
"""

from var import *
from table import *
from table.TypeTable import *
from table.HistoryTable import *
from table.ValueTable import *
from table.EnvTable import *

from Interpreter.table.EnvTable import EnvTable
from Interpreter.table.HistoryTable import HistoryTable
from Interpreter.table.TypeTable import TypeTable
from Interpreter.table.ValueTable import ValueTable
from Interpreter.var import VarManager

tt = TypeTable()
memory = ValueTable()
env = EnvTable()
histories = HistoryTable()

Int = int(Name.INT)
Float = int(Name.FLOAT)
Char = int(Name.CHAR)

vm = VarManager(tt, histories, env, memory, 0)

x = vm.new_int("x", 1)

y = vm.new_char("char", 'c')
vm.new_float("oho", 0.01)

vm.set_proc(1)

vm.set_var("x", 2)
vm.new_ptr("a", Char, 5)
print(vm.get_history("a"))

vm.set_ptr_var("a", 0, 'c')
vm.set_ptr_var("a", 1, 'd')
vm.set_proc(2)

vm.set_ptr_var("a", 4, 'e')

# print(vm.envToString())
# print(vm.get_memory())

vm.new_arrow("get_new_array", [Int, Int, Float], Float, 3)
# print(vm.envToString())
# print(vm.get_memory())
# print(vm.get_tt())
vm.set_var("x", 16)
vm.set_proc(2)

print(vm.get_history("a"))
