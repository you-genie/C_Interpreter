from Parser.Parser import Parser as ELAParser
from Parser.Util.ASTName import ASTName
from Parser.YaccRule import *
from Interpreter.eval import Interp as ELAInterpreter
from Interpreter.grammar.expr import *
from Interpreter.grammar.value import *
from Interpreter.type.Type import *
from Interpreter.type.Ptr import Ptr
from Converter.converter import Converter as ELAConverter
import copy

debug = True

class Interface():

    def __init__(self, func):
        converter = ELAConverter()
        self.func = func
        self.current = self._getin_(self.func[0])
        #scope is a list of tuple(node, environment)
        self.scope = list()
        self.interp = ELAInterpreter()
        for index in range(0, len(self.func)):
            target = self.func[index]
            if debug: print(target.get_child('id').get_data())
            arg_types = list(map(lambda x: converter.translate(x.get_child('id')), target.get_child('params').get_data()))
            arg_names = list(map(lambda x: converter.translate(x.get_child('type')), target.get_child('params').get_data()))
            self.interp.eval(Fun(converter.translate(target.get_child('type')),
                converter.translate(target.get_child('id')), arg_names, arg_types, index), target.get_lineno())

    # return true when it's last line to be executed or type error
    def interp_line(self):
        #end of program
        if self.current == None: return 0

        result = 1

        lineno = self.current.get_lineno()

        if debug: print("lineno : ", lineno)

        result = self._interp_(self.current)

        if debug: print("--------------------------------------------------------")

        return result


    def _interp_(self, current):
        result = 1
        name = current.get_name()
        lineno = current.get_lineno()
        converter = ELAConverter()

        if debug:
            #print(current)
            print(converter.translate(current))

        if converter.has_app(current):
            return self._remove_app_(current)

        ret = None

        if name == ASTName.LINEBREAK:
            self.current = self._nextline_(current)
            return 1
        elif name == ASTName.DECL:
            decl_type = None
            if current.get_child('type').get_name() == ASTName.INT:
                decl_type = Int
            elif current.get_child('type').get_name() == ASTName.FLOAT:
                decl_type = Float

            for aid in current.get_child('ids').get_data():
                if aid.get_name() == ASTName.ID:
                    ret = self.interp.eval(Decl(converter.translate(aid), decl_type), lineno)
                elif aid.get_name() == ASTName.ARRAY:
                    ret = self.interp.eval(Decl(converter.translate(aid.get_child('id')), Ptr(decl_type, converter.translate(aid.get_child('index')))), lineno)
                if ret == ErrV: break
        elif name == ASTName.FOR:
            if current.get_child('inited').get_data() == None: ret = self.interp.eval(converter.translate(current), lineno)
            else: ret = ForV(None)
        else:
            ret = self.interp.eval(converter.translate(current), lineno)


        if debug:
            print(ret)
            print(self.interp.vm.env_to_string())


        if type(ret) == VoidV:
            self.current = self._nextline_(current)
        elif type(ret) == IfV:
            if ret.value:
                new_env = copy.deepcopy(self.interp.vm.env)
                self.scope.append((self._nextline_(current), new_env))
                self.current = self._getin_(current)
            else:
                if self.current.get_child('else').get_data() != None:
                    self.current = self.current.get_child('else').get_data()
                else: self.current = self._nextline_(current)
        elif type(ret) == ForV:
            if current.get_child('inited').get_data() == None:
                current.get_child('inited').data = 1
                condV = self.interp.eval(converter.translate(current.get_child('cond')), lineno)
                if condV.value:
                    self.scope.append((copy.deepcopy(current), self.interp.vm.env))
                    self.current = self._getin_(current)
                else:
                    self.current = self._nextline_(current)
            else:
                self.interp.eval(converter.translate(current.get_child('iter')), lineno)
                condV = self.interp.eval(converter.translate(current.get_child('cond')), lineno)
                if condV.value:
                    self.scope.append((copy.deepcopy(current), self.interp.vm.env))
                    self.current = self._getin_(current)
                else:
                    self.current = self._nextline_(current)
        elif type(ret) == RetV:
            a_tuple = self.scope.pop()
            self.current = a_tuple[0]
            self.interp.vm.env = a_tuple[1]
            converter.find_and_replace_rax(self.current, ret.value)
        elif type(ret) == AppV: result = -1
        elif type(ret) == ErrV: result = -1
        else: result = -1

        return result


    def _remove_app_(self, current):
        converter = ELAConverter()

        ret_node = copy.deepcopy(current)
        target = converter.get_app(ret_node)
        if target.get_parent() == None:
            self.scope.append((ret_node.next, copy.deepcopy(self.interp.vm.env)))
        else:
            self.scope.append((ret_node, copy.deepcopy(self.interp.vm.env)))
            target.RAX = 1

        ret = self.interp.eval(converter.translate(target), ret_node.get_lineno())
        if type(ret) == AppV:
            self.interp.vm.env = ret.get_env()
            self.current = self._getin_(self.func[ret.get_statement()])
            return 1
        else:
            return -1


    def _nextline_(self, current):
        if current.next == None:
            if len(self.scope) == 0:
                return None
            else:
                a_tuple = self.scope.pop()
                self.interp.vm.env = a_tuple[1]
                return a_tuple[0]
        else:
            target = copy.deepcopy(current.next)
            return target


    def _getin_(self, current):
        if current.get_child('body') != None:
            target = copy.deepcopy(current.get_child('body').get_data()[0])
            return target


    def print_variable(self, tar):
        value = self.interp.vm.env.print_element(self.interp.vm.env.find_index_by_name(tar))


    def trace_variable(self, tar):
        print(self.interp.vm.get_history(tar))


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
    parser = ELAParser(open('test.c', 'r'))
    interface = Interface(parser.parse())

    #parser.print_result()

    while True:
        ret = parse_command(input(">> "))
        interp_ret = 1
        if ret[0] == 1:
            for i in range(0, ret[1]):
                interp_ret = interface.interp_line()
                if interp_ret == 0 or interp_ret == -1: break
        elif ret[0] == 2:
            interface.print_variable(ret[1])
        elif ret[0] == 3:
            interface.trace_variable(ret[1])

        if interp_ret == 0:
            print("End Of Program")
            break
        elif interp_ret == -1:
            print("ERROR")
            break


do_interprete()