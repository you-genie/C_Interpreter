import abc


class Type:
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __str__(self):
        """ 형식에 따라
        Int: INT, Char: CHAR, Ptr: T[size], Arrow: (T T T ...) -> T
        """
        pass
    

class Int(Type):
    
    def __str__(self):
        return "INT"


class Char(Type):
    
    def __str__(self):
        return "Char"