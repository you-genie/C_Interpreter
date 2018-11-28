import sys
sys.path.insert(0, "../../Util")

from Type import *
from Arrow import *
from Ptr import *

type_table = [Int(), Char()]
new_ptr = Ptr(type_table[0], 3)
print(new_ptr)

new_arrow = Arrow([type_table[0], type_table[1]], type_table[0])
print(new_arrow)