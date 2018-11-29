from type import *
from type.Arrow import *
from type.Type import *
from type.Ptr import *
from table import *
from table.Table import *
from table.TypeTable import *


class VarManager:
    # tt는 **반드시** Table 타입이다.
    tt = None
    
    def __init__(self, table):
        """ table Type should be Table type.
        """
        self.tt = table;

        
    class Var:
        """Var, type_index is index from TypeTable
        내부 클래스를 정의함으로써 var_table을 받아서 쓸 수 있게 되었다.
        var_table은 무조건 Table type이므로 Table interface의 함수를 쓸 수 있다!
        """
        value = 0
        name = ""
        type_index = -1 

        @abstractmethod
        def __str__(self):
            return "{} {} = {}".format(
                str(self.tt.get(self.type_index)), self.name, str(self.value))

        @abstractmethod
        def get_value(self):
            return self.value

        @abstractmethod
        def get_name(self):
            return self.name

        @abstractmethod
        def get_type(self):
            return self.tt.get(self.var_t)


    class IntV(Var):
        value = 0
        name = ""
        type_index = 0

        def __init__(self, name, num):
            self.name = name
            self.value = num


    class FloatV(Var):
        value = 0
        name = ""
        type_index = 1
        
        def __init__(self, name, num):
            self.name = name
            self.value = num
        

    class CharV(Var):
        value = 0
        name = ""
        type_index = 2

        def __init__(self, name, char_value):
            self.name = name
            self.value = char_value


    class PtrV(Var):
        value = 0
        name = ""
        type_index = None

        def __init__(self, name, elem_type, elem_num):
            self.name = name
            self.var_t = Ptr(elem_type, elem_num)

        def __init__(self, name, elem_type, elem_num, data)
               