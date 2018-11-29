from type import *
from type.Arrow import *
from type.Type import *
from type.Ptr import *

from abc import *

class VarManager:
    tt = None
    mm = None
    
    def __init__(self, type_table, value_table):
        """ 후에 env_table 등 추가!
        """
        tt = type_table
        mm = value_table
        
    def __str__(self):
        return "Variable Manager"

        
class Var:
    """Var, type_index is index from TypeTable
    내부 클래스를 정의함으로써 type_table을 받아서 쓸 수 있게 되었다.
    내부 클래스를 정의함으로써 val_table을 받아서 쓸 수 있게 되었다.
    두 table은 무조건 Table type이므로 Table interface의 함수를 쓸 수 있다!
    """
    value_index = -1
    name = ""
    type_index = -1
    
        
    def get_value_index(self):
        return self.value_index

    def get_name(self):
        return self.name

    def get_type_index(self):
        return self.type_index
