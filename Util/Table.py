"""Table Interface
@authorized by Genne Chung
overrided by EnvTable, TypeTable, HistoryTable, etc
"""

import abc


class Table:

    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def get_element(self, index):
        pass
    
    @abc.abstractmethod
    def push(self, elem):
        pass
    
    @abc.abstractmethod
    def pop(self):
        pass
    
    @abc.abstractmethod
    def print_element(self, index):
        pass
    