import abc


class Stack:
    
    __metaclass__ = abc.ABCMeta

    @abc.abstactMethod
    def __str__(self):
        pass
    
    @abc.abstactMethod
    def push(self, elem):
        pass
    
    @abc.abstactMethod
    def pop(self):
        pass
    
    @abc.abstactMethod
    def push_n(self, n):
        pass
    
    @abc.abstactMethod
    def pop_n(self, n):
        pass
    
    @abc.abstactMethod
    def copy(self, stack):
        pass
    
    @abc.abstactMethod
    def copy_n(self, stack, n):
        pass