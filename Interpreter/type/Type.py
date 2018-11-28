"""Type Interface
@authorized by Genne Chung
overrided by Arrow, Ptr, Num, Char
"""

import abc


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


class Int(Type):
    
    def __str__(self):
        return "INT"


class Char(Type):
    
    def __str__(self):
        return "CHAR"
