"""Table Interface
@authorized by Genne Chung
overrided by EnvTable, TypeTable, HistoryTable, etc

* TODO: 나중에 시간 나면 push pop 등등의 값들 전부 override가능하게 좀 고쳐놓자
* 코드 드러워죽겟
* ㅁㄴㄹㅇㅂㄴㄹㅇ
"""

import abc


class Table:

    __metaclass__ = abc.ABCMeta
    
    footer = "--------------------------------------------------------"
    
    def create_header(self, name):
        ret_str = ""
        ret_str += "========================================================\n"
        ret_str += "                   {}     \n".format(name)
        ret_str += "========================================================\n"
        return ret_str
    
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def get(self, index):
        pass
    
    @abc.abstractmethod
    def push(self, elem):
        """ RETURN INDEX VALUE!
        """
        pass
    
    @abc.abstractmethod
    def pop(self):
        """ RETURN POPPED VALUE!
        """
        pass
    
    @abc.abstractmethod
    def print_element(self, index):
        pass
    