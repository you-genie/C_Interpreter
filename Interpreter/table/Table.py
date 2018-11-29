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
    