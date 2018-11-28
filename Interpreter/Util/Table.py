import abc


class Table:

    __metaclass__ = abc.ABCMeta
    
    @abc.abstactMethod
    def __str__(self):
        pass

    @abc.absstractMethod
    def get_element(self, index):
        pass
    
    @abc.abstractMethod
    def push(self, elem):
        pass
    
    @abc.abstractMethod
    def pop(self, elem):
        pass
    
    @abc.abstactMethod
    def print_element(self, index):
        pass
    