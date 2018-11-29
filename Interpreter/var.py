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
        return self.new_var(name_str, int(Name.INT), num_val)
    
    def new_float(self, name_str, num_val):
        return self.new_var(name_str, int(Name.FLOAT), num_val)
    
    def new_char(self, name_str, char_val):
        return self.new_var(name_str, int(Name.CHAR), char_val)
    
    def new_ptr(self, name_str, elem_type_index, array_size):
        """ New Array means NEW ARRAY ASSIGNMENT, NOT ALLOCATION
        """
        # TODO: malloc in memory.
        trash = -1
        ptr = self.memory.push(trash)
        for i in range(array_size - 1):
            self.memory.push(trash)
        
        # TODO: Make new Type
        new_ptr_type = Ptr(self.tt.get(elem_type_index), array_size)
        new_type_index = self.tt.push(new_ptr_type)
        
        # TODO: Make new History
        new_hist = History()
        hist_index = self.histories.push(new_hist)
        
        new_var = Var(name_str, new_type_index, ptr, hist_index)
        new_var_index = self.env.push(new_var)
        return new_var_index

    
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
    
    def set_var(self, name_str, new_val):
        index = self.find_index_by_name(name_str)
        if index == -1:
            return -1
        else:
            self.set_var_by_index(index, new_val)
    
    def set_var_by_index(self, env_index, new_val):
        """ Inner Helper function 
        
        * variable index를 받아서(env의 인덱스) variable을 찾고, new_val 넣어줌.
        * inner private function 입니다.
        """
        
        # TODO: find variable from env
        var = self.env.get(env_index)
        
        # TODO: set new value in memory.
        self.memory.set_val(var.get_value_index(), new_val)
        
    def find_index_by_name(self, name_str):
        """ Inner Helper function
        
        * variable name을 받아서 env에서 꺼내줌.
        * variable 이름은 겹치지 않음. 겹침 ㄴㄴ는 인터프리터에서 관리한다. 여기서 해줄 필요 x
        """
        
        return self.env.find_index_with_name(name_str)
        
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
