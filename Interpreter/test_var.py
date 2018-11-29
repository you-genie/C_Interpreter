from var import *
from table import *
from table.TypeTable import *
from table.HistoryTable import *
from table.ValueTable import *
from table.EnvTable import *

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
