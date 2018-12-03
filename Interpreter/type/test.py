from .__init__ import *
from Arrow import *
from Ptr import *

type_table = [Int(), Char()]
new_ptr = Ptr(type_table[0], 3)
comp_ptr = Ptr(type_table[0], 3)

print(new_ptr)
print(comp_ptr.is_same_type(new_ptr))

new_arrow = Arrow([type_table[0], type_table[1]], type_table[0])
comp_arrow = Arrow([type_table[0], type_table[0]], type_table[1])
comp_arrow2 = Arrow([type_table[0], type_table[0]], type_table[0])
comp_arrow3 = Arrow([type_table[0], type_table[1]], type_table[0])

print(comp_arrow.is_same_type(new_arrow))
print(comp_arrow2.is_same_type(new_arrow))
print(comp_arrow3.is_same_type(new_arrow))

print(new_arrow)