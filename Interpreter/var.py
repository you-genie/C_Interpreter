""" var module
@authorized by Genne Chung
VarManager, Var class 가지고 있음.
"""

from type import *
from type.Arrow import *
from type.Type import *
from type.Ptr import *
from table import *
from table.HistoryTable import *

from abc import *

class VarManager:
    """ Interpreter가 줄마다 만들어지면서 VarManager를 Type Table, History Table, Env Table, Value Table, 해당 줄 Procedeure과 함께 생성한다.
    
    * 여기서 TypeTable & ValueTable & HistoryTable은 Interpreter가 계속해서 돌려쓰는 값
    * EnvTable의 경우 새 것을 쓸 수도 있고 아닐 수도 있다.
    """
    
    tt = None
    env = None
    histories = None
    memory = None
    proc = -1
    
    def __init__(self, type_table, history_table, env_table, value_table, proc):
        """ 후에 env_table, stack 등 추가!
        """
        self.tt = type_table
        self.env = env_table
        self.histories = history_table
        self.memory = value_table
        self.proc = proc
    
    def get_proc(self):
        return self.proc
    
    def get_tt(self):
        return self.tt
    
    def get_env(self):
        return self.env
    
    def get_histories(self):
        return self.histories
    
    def get_memory(self):
        return self.memory
    
    def set_proc(self, proc):
        self.proc = proc

    def __str__(self):
        return "Variable Manager"
    
    def envToString(self):
        return self.env.simpleStr(self.tt, self.memory)
    
    def toString(self, var):
        if var.get_type_index() < 3:
            return "{} {} = {}".format(
                self.tt.get(var.get_type_index()), 
                var.get_name(), 
                self.memory.get(var.get_value_index())
            )
        elif self.tt.get(var.get_type_index()).__name__() == Name.PTR:
            return "{} {} = {}".format(
                        tt.get(var.get_type_index()),
                        var.get_name(),
                        self.env.get_ptr_value_str(var, self.tt, self.memory)
                    )
        else:
            return "def {}{}: {}".format(
                var.get_name(),
                tt.get(var.get_type_index()),
                self.env.get_arrow_value_str(var, self.memory)
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
        hist_str = "["
        for i in range(array_size - 1):
            self.memory.push(trash)
            hist_str += "-1, "
        hist_str += "-1]"

        # TODO: Make new Type
        new_ptr_type = Ptr(self.tt.get(elem_type_index), array_size)
        new_type_index = self.tt.push(new_ptr_type)
        
        return self.new_var_with_name_type_val(
            name_str, new_type_index, ptr, hist_str)
    
    def new_arrow(self, name_str, param_type_indices, ret_type_index, body_index):
        value_index = self.memory.push(body_index)
        param_types = []
        for param_type_index in param_type_indices:
            param_types.append(self.tt.get(param_type_index))
        
        ret_type = self.tt.get(ret_type_index)
        
        new_arrow_type = Arrow(param_types, ret_type)
        new_type_index = self.tt.push(new_arrow_type)
        
        return self.new_var_with_name_type_val(
            name_str, new_type_index, value_index, body_index)
    
    def new_var_with_name_type_val(
        self, name_str, type_index, value_index, hist_value):
        new_hist = History()
        new_hist.push([self.proc, hist_value])
        hist_index = self.histories.push(new_hist)
        
        new_var = Var(name_str, type_index, value_index, hist_index)
        new_var_index = self.env.push(new_var)
        
        return new_var_index
    
    def new_var(self, name_str, type_index, new_val):
        """ generate new variable with given values
        """
        # TODO: set value in memory and get index
        val_index = self.memory.push(new_val)
        return self.new_var_with_name_type_val(
            name_str, type_index, val_index, str(new_val))
    
    def set_var(self, name_str, new_val):
        index = self.find_index_by_name(name_str)
        if index == -1:
            return -1
        else:
            self.set_var_by_index(index, new_val)
            
    def set_ptr_var(self, name_str, ptr_index, new_val):
        index = self.find_index_by_name(name_str)
        if index == -1:
            return -1
        else:
            var = self.env.get(index)
            if self.tt.get(var.get_type_index()).array_size <= ptr_index :
                return -1
            self.memory.set_val(var.get_value_index() + ptr_index, new_val)
            self.histories.get(var.get_history_index()).push(
                [self.proc, self.env.get_ptr_value_str(var, self.tt, self.memory)])
    
    def set_var_by_index(self, env_index, new_val):
        """ Inner Helper function 
        
        * variable index를 받아서(env의 인덱스) variable을 찾고, new_val 넣어줌.
        * inner private function 입니다.
        """
        
        # TODO: find variable from env
        var = self.env.get(env_index)
        self.histories.get(var.get_history_index()).push([self.proc, new_val])
        # print(self.histories.get(var.get_history_index()))
        
        # TODO: set new value in memory.
        self.memory.set_val(var.get_value_index(), new_val)
        
    def find_index_by_name(self, name_str):
        """ Inner Helper function
        
        * variable name을 받아서 env에서 꺼내줌.
        * variable 이름은 겹치지 않음. 겹침 ㄴㄴ는 인터프리터에서 관리한다. 여기서 해줄 필요 x
        """
        
        return self.env.find_index_with_name(name_str)
    
    def get_history(self, name_str):
        var = self.env.get(self.find_index_by_name(name_str))
        return self.histories.get(var.get_history_index())
        
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
