from type import *
from type.Arrow import *
from type.Type import *
from type.Ptr import *
from table import *
from table.HistoryTable import *

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
        
    def get_tt(self):
        return self.tt
    
    def get_env(self):
        return self.env
    
    def get_histories(self):
        return self.histories
    
    def get_memory(self):
        return self.memory

    def __str__(self):
        return "Variable Manager"
    
    def envToString(self):
        return self.env.simpleStr(self.tt, self.memory)
    
    def toString(self, var):
        return "{} {} = {}".format(
            self.tt.get(var.get_type_index()), 
            var.get_name(), 
            self.memory.get(var.get_value_index())
        )
    
    def new_int(self, name_str, num_val):
        """ generate new integer value 
        """
        # TODO: don't need to set type value, get INT type        
        # TODO: call new_var, it will return new variable's index! return that variable.
        return self.new_var(name_str, 0, num_val)
    
    def new_float(self, name_str, num_val):
        return self.new_var(name_str, 1, num_val)
    
    def new_char(self, name_str, char_val):
        return self.new_var(name_str, 2, char_val)
        
    def new_var(self, name_str, type_index, new_val):
        """ generate new variable with given values
        """
        # TODO: set value in memory and get index
        val_index = self.memory.push(new_val)
        
        # TODO: set new History in HistoryTable, and get index of it.
        new_hist = History()
        hist_index = self.histories.push(new_hist)
        
        # TODO: with those values, make new Variable
        new_var = Var(name_str, type_index, val_index, hist_index)
        
        # TODO: Set new variable in EnvTable.
        new_var_index = self.env.push(new_var)
        
        # TODO: return index of new variable.
        return new_var_index
        
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
