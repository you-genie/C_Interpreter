import abc


class ExprV:
    value = None
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.__name__() + "V(" + str(self.value) + ")"
    

class IntV(ExprV):
    
    def __name__(self):
        return "Int"
    
    pass
    
class FloatV(ExprV):
    
    def __name__(self):
        return "Float"
    
    pass

class CharV(ExprV):
    
    def __name__(self):
        return "Char"
    
    pass
