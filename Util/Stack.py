import abc


class Stack:
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __str__(self):
        pass
    
    @abc.abstractmethod
    def push(self, elem):
        pass
    
    @abc.abstractmethod
    def pop(self):
        pas
    
    @abc.abstractmethod
    def push_n(self, n):
        pass
    
    @abc.abstractmethod
    def pop_n(self, n):
        pass
    
    @abc.abstractmethod
    def copy(self, stack):
        pass
    
    @abc.abstractmethod
    def copy_n(self, stack, n):
        pass