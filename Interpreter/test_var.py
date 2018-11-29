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

vm = VarManager(tt, histories, env, memory)

x = vm.new_int("x", 1)

y = vm.new_char("char", 'c')
vm.new_float("oho", 0.01)

vm.set_var("x", 2)
vm.new_ptr("a", int(Name.INT), 3)

vm.set_ptr_var("a", 0, 1)
vm.set_ptr_var("a", 1, 2)

print(vm.envToString())
print(vm.get_memory())

vm.new_arrow("get_new_array", [int(Name.INT), int(Name.INT)], int(Name.CHAR), 3)
print(vm.envToString())
print(vm.get_memory())
print(vm.get_tt())
