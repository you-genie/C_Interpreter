from type import *
from type.Arrow import *
from type.Type import *
from type.Ptr import *
from table import *

from abc import *

class VarManager:
    tt = None
    env = None
    histories = None
    memory = None
    
    def __init__(self, type_table, history_table, env_table, value_table):
        """ 후에 env_table, stack 등 추가!
        """
        self.tt = type_table
        self.env = env_table
        self.histories = history_table
        self.memory = value_table
        
    def __str__(self):
        return "Variable Manager"
    
    def toString(self, var):
        return "{} {} = {}".format(
            self.tt.get(var.get_type_index()), 
            var.get_name(), 
            self.memory.get(var.get_value_index())
        )
    
    def new_int(self, name_str, num_val):
        """ generate new integer value 
        """
        # TODO: set value in memory and get index
        # TODO: set 

        
class Var:
    """Var, type_index is index from TypeTable
    내부 클래스를 정의함으로써 type_table을 받아서 쓸 수 있게 되었다.
    내부 클래스를 정의함으로써 val_table을 받아서 쓸 수 있게 되었다.
    두 table은 무조건 Table type이므로 Table interface의 함수를 쓸 수 있다!
    
    * 타입은 바뀌면 안되므로 set_type 넣지 않음.
    * 마찬가지의 이유로 set_name 넣지 않음.
    * 역시 같은 이유로 set_history_index 넣지 않음.
    """
    value_index = -1
    name = ""
    type_index = -1
    history_index = -1
    
    def __init__(self, name, type_index, value_index, history_index):
        self.name = name
        self.value_index = value_index
        self.type_index = type_index
        self.history_index = history_index
        
    def get_value_index(self):
        return self.value_index
    
    def set_value_index(self, new_index):
        self.value_index = new_index

    def get_name(self):
        return self.name

    def get_type_index(self):
        return self.type_index
    
    def get_history_index(self):
        return self.history_index
