from table.TypeTable import *
from type import *
from type.Type import *
from type.Arrow import *
from type.Ptr import *

tt = TypeTable()
int_t = tt.get(0)
char_t = tt.get(1)
new_array = Ptr(int_t, 3)

print(tt)

tt.push(new_array)
print(tt)

new_arrow = Arrow([int_t, char_t, new_array], new_array)
tt.push(new_arrow)
print(tt)

pop_arrow = tt.pop()
print(tt)

new_arrow = Arrow([int_t, pop_arrow], pop_arrow)
tt.push(new_arrow)
print(tt)

new_arrow = Arrow([char_t], char_t)
tt.push(new_arrow)
print(tt)
