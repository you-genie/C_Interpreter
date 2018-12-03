""" test module
@authorized by Genne Chung
"""

from expr import *
from value import *

one_line = Add(IntV(13), IntV(15))

two_line = Add(Sub(IntV(14), FloatV(0.7)), CharV('c'))
three_line = Decl(Id("YEAH"))
four_line = Set(Id("YEAH"), IntV(13))

print(one_line)
print(two_line)
print(three_line)
print(four_line)