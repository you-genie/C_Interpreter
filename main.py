from Parser.Parser import Parser as ELAParser
from Parser.util.ASTName import ASTName
from Interpreter.eval import Interp as ELAInterpreter
from Interpreter.grammar.expr import *
from Interpreter.type.Type import CharClass, FloatClass, IntClass
from Interpreter.type.Ptr import Ptr
from Converter.converter import Converter as ELAConverter

debug = True

class Interface():

    def __init__(self, func):
        converter = ELAConverter()
        self.func = func
        self.current = self.func[0].get_child('body').get_data()[0]
        self.currentline = self.current.get_lineno()
        self.scope = [self.current]
        self.interp = ELAInterpreter()
        for index in range(0, len(self.func)):
            target = self.func[index]
            if debug: print(target.get_child('id').get_data())
            arg_types = list(map(lambda x: converter.translate(x.get_child('id')), target.get_child('params').get_data()))
            arg_names = list(map(lambda x: converter.translate(x.get_child('type')), target.get_child('params').get_data()))
            self.interp.eval(Fun(target.get_child('type'), target.get_child('id').get_data(), arg_types, arg_names, index), target.get_lineno())

    # return true when it's last line to be executed or type error
    def interp_line(self):
        quit = False

        lineno = self.current.get_lineno()

        if debug: print("lineno : ", lineno, " currentline : ", self.currentline)

        if self.currentline < lineno: pass
        else: quit = self._interp_(self.current)
        self.currentline += 1

        if quit: return True
        else: return False


    def _interp_(self, current):
        isError = False
        name = current.get_name()
        lineno = current.get_lineno()
        converter = ELAConverter()

        if debug:
            print(current)
            print(converter.translate(current))
            

        if name == ASTName.DECL:
            if debug: print("DECL")
            decl_type = None
            if current.get_child('type').get_name() == ASTName.INT:
                decl_type = IntClass
            elif current.get_child('type').get_name() == ASTName.FLOAT:
                decl_type = FloatClass

            for aid in current.get_child('ids').get_data():
                if aid.get_name() == ASTName.ID:
                    self.interp.eval(Decl(aid.get_data(), decl_type), lineno)
                elif aid.get_name() == ASTName.ARRAY:
                    self.interp.eval(Decl(aid.get_child('id').get_data(), Ptr(converter.translate(aid.get_child('index')), decl_type)), lineno)

            self.current = self._nextline_(current)

        return isError


    def _nextline_(self, current):
        if current.next == None: return self.scope.pop()
        else: return current.next


    def print_variable(tar):
        print(tar)


    def trace_variable(tar):
        print(tar)


def parse_command(tar):
    commands = tar.split(' ')
    if commands[0] == 'next':
        if len(commands) == 1:
            return 1, 1
        elif len(commands) == 2:
            return 1, int(commands[1])
        else:
            return 0, 0
    elif commands[0] == 'print':
        if len(commands) == 2:
            return 2, commands[1]
        else:
            return 0, 0
    elif commands[0] == 'trace':
        if len(commands) == 2:
            return 3, commands[1]
        else:
            return 0, 0
    else:
        return 0, 0


def do_interprete():
    parser = ELAParser(open('code.c', 'r'))
    interface = Interface(parser.parse())

    #parser.print_result()

    while True:
        ret = parse_command(input(">> "))
        flag = False
        if ret[0] == 1:
            for i in range(0, ret[1]):
                if interface.interp_line():
                    flag = True
                    break
        elif ret[0] == 2:
            interface.print_variable(ret[1])
        elif ret[0] == 3:
            interface.trace_variable(ret[1])

        if flag:
            break


do_interprete()