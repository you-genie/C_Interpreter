"""Type Interface
@authorized by Genne Chung
overrided by Arrow, Ptr, Num, Char
"""

import abc
from abc import ABC

from enum import Enum


class Name(Enum):
    INT = 0
    FLOAT = 1
    CHAR = 2
    ARROW = 3
    PTR = 4
    
    def __int__(self):
        return self.value
    

class Type:
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __str__(self):
        """ 형식에 따라
        Int: INT, Char: CHAR, Ptr: T[size], Arrow: (T T T ...) -> T
        """
        pass
    
    @abc.abstractmethod
    def is_same_type(self, type_cmp):
        return str(type_cmp) == str(self)


class IntClass(Type, ABC):
    
    def __name__(self):
        return Name.INT
    
    def __str__(self):
        return "int"


class CharClass(Type, ABC):
    
    def __name__(self):
        return Name.CHAR
    
    def __str__(self):
        return "char"
    

class FloatClass(Type, ABC):
    
    def __name__(self):
        return Name.FLOAT
    
    def __str__(self):
        return "float"


Int = IntClass()
Char = CharClass()
Float = FloatClass()
