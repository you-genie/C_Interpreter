import sys
sys.path.insert(0, "../../Util")

from Type import *


class Int(Type):
    
    def __str__(self):
        return "INT"


class Char(Type):
    
    def __str__(self):
        return "Char"
