from type import *
from type.Arrow import *
from type.Type import *
from type.Ptr import *
from table.TypeTable import *

tt = TypeTable()


class Var:
    """Var, type_index is index from TypeTable
    """
    value = 0
    name = ""
    type_index = -1 
    
    @abstractmethod
    def __str__(self):
        # return "{} {} = {}".format(str(tt.get(self.type_index)), self.name, str(self.value))
        pass
    
    @abstractmethod
    def get_value(self):
        return self.value
    
    @abstractmethod
    def get_name(self):
        return self.name
    
    @abstractmethod
    def get_type(self):
        return self.var_t
    

class IntV(Var):
    value = 0
    name = ""
    var_t = Int
    
    def __init__(self, name, num):
        self.name = name
        self.value = num

        
class CharV(Var):
    value = 0
    name = ""
    var_t = Char
    
    def __init__(self, name, char_value):
        self.name = name
        self.value = char_value
        
        
class PtrV(Var):
    value = 0
    name = ""
    var_t = None
    
    def __init__(self, name, elem_type, elem_num):
        self.name = name
        self.var_t = Ptr(elem_type, elem_num)
    
    def __init__(self, name, elem_type, elem_num, data)
               