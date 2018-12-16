""" eval module containing Interp class.
@authorized by Genne Chung
containing basic interpreter.

* uses lambda functions for interpretation
* uses dictionaries for switching function.
"""

from Interpreter.var import *

from Interpreter.grammar.expr import *
from Interpreter.grammar.value import *
from Interpreter.type.Type import CharClass, FloatClass, IntClass
from Interpreter.type.Ptr import Ptr
from Interpreter.type.Arrow import Arrow
from Interpreter.table.EnvTable import EnvTable
from Interpreter.table.HistoryTable import HistoryTable
from Interpreter.table.TypeTable import TypeTable
from Interpreter.table.ValueTable import ValueTable
from Util.Debug import Debug

log = Debug("Interp")


class Interp:
    vm = None

    def check_numeric(self, expr):
        """
        Check numeric for expression (ExprV)
        :param expr:
        :return:
        """
        if type(expr) == IntV or type(expr) == FloatV:
            return True
        else:
            return False

    def check_numeric_for_Type(self, type_class):
        """
        Check numeric for Type
        :param type_class:
        :return:
        """
        if type(type_class) == IntClass or type(type_class) == FloatClass:
            return True
        else:
            return False

    def return_value(self, expr):
        return expr

    def return_ptr_value(self, expr):
        if type(expr.get_id()) != Id:
            return ErrV("It should be Id type in PtrV")

        ptr_var = self.vm.env.get(self.vm.find_index_by_name(expr.get_id().id_name))
        if type(self.vm.tt.get(ptr_var.get_type_index())) != Ptr:
            return ErrV("Type should be Pointer value in PtrV")

        index_int_v = self.interp(expr.get_index())
        if type(index_int_v) == ErrV:
            return index_int_v

        if type(index_int_v) != IntV:
            return ErrV("Array index is not Int Value!")

        return self.vm.get_ptr_var(expr.get_id().id_name, index_int_v.value)

    def printf(self, expr):
        interpreted_args = []
        for arg in expr.args:
            arg_v = self.interp(arg)
            if type(arg_v) == ErrV:
                return arg_v

            interpreted_args.append(self.interp(arg).value)

        argument_tuple = tuple(interpreted_args)

        try:
            print(expr.format_string % argument_tuple)
        except TypeError:
            return ErrV("Print Type Error!")

        return VoidV("Print")

    def ela_if(self, expr):
        is_true = self.interp(expr.cond)
        if type(is_true) == ErrV:
            return is_true

        if type(is_true) != BoolV:
            return ErrV("condition should be boolean type!")

        return IfV(is_true.value)
    
    def ae_two(self, expr, op):
        l = self.interp(expr.left)
        r = self.interp(expr.right)
        ret_type = self.ae_type_checker(type(l), type(r))
        if type(ret_type) == ErrV:
            return ret_type
        ret_val = op(
            l.value,
            r.value
        )

        if ret_type == IntV:
            ret_val = int(ret_val)
        return ret_type(ret_val)

    def ae_one(self, expr, op):
        vm_index = self.vm.find_index_by_name(expr.id_expr.id_name)
        var = self.vm.env.get(vm_index)
        value = self.vm.memory.get(var.get_value_index())

        var_type = self.vm.tt.get(var.get_type_index())
        if self.check_numeric_for_Type(var_type):
            op_ed = op(value.value)
            value.set(op_ed)
            set_val = value
        else:
            return ErrV("AE should be with Numeric only!")

        self.vm.set_var_by_index(vm_index, set_val)
        return VoidV("Set " + str(op))

    def inc(self, expr):
        return self.ae_one(expr, lambda x: x + 1)

    def dec(self, expr):
        return self.ae_one(expr, lambda x: x - 1)

    def ela_not(self, expr):
        bool_expr = self.interp(expr.bool_expr)
        if type(bool_expr) == ErrV:
            return bool_expr

        if type(bool_expr) != BoolV:
            return ErrV("! should be with boolean expression!")

        return BoolV(not bool_expr.value)

    def cond_two(self, expr, op):
        l = self.interp(expr.left)
        r = self.interp(expr.right)

        # check error
        if type(l) == ErrV:
            return l
        if type(r) == ErrV:
            return r

        # check type
        if self.check_numeric(l) and self.check_numeric(r):
            ret_val = BoolV(
                op(l.value, r.value)
            )
        else:
            ret_val = ErrV("Only Numerics are allowed on Condition")

        return ret_val

    def ae_type_checker(self, l_type, r_type):
        """
        check return type
        :param l_value: ExprV
        :param r_value: ExprV
        :return: 최종 흡수된 타입! 혹은 Err
        """
        if l_type == IntV and r_type == IntV:
            return IntV
        elif l_type == FloatV and r_type == IntV:
            return FloatV
        elif l_type == IntV and r_type == FloatV:
            return FloatV
        elif l_type == FloatV and r_type == FloatV:
            return FloatV
        else:
            return ErrV("AE should be held with two numeric values!")
    
    def add(self, expr):
        return self.ae_two(expr, lambda x, y: x + y)
    
    def sub(self, expr):
        return self.ae_two(expr, lambda x, y: x - y)
    
    def mul(self, expr):
        return self.ae_two(expr, lambda x, y: x * y)
    
    def div(self, expr):
        return self.ae_two(expr, lambda x, y: x / y)

    def cond_g(self, expr):
        return self.cond_two(expr, lambda x, y: x > y)

    def cond_l(self, expr):
        return self.cond_two(expr, lambda x, y: x < y)

    def cond_e(self, expr):
        return self.cond_two(expr, lambda x, y: x == y)

    def cond_ge(self, expr):
        return self.cond_two(expr, lambda x, y: x >= y)

    def cond_le(self, expr):
        return self.cond_two(expr, lambda x, y: x <= y)

    def cond_ne(self, expr):
        return self.cond_two(expr, lambda x, y: x != y)
    
    def set_val(self, expr):
        """
        만약 expr.id_expr가 리스트 타입인 경우, [ptr, ptr index] 이므로 해당 액션을 넘겨준다.
        :param expr:
        :return:
        """
        ptr_flag = False
        if type(expr.id_expr) == list:
            id_expr = expr.id_expr[0]
            ptr_flag = True
        else:
            id_expr = expr.id_expr
        
        if type(id_expr) != Id:
            return ErrV("Variable is not Id type")
        else:
            expr_v = {
                IntV: IntClass,
                CharV: CharClass,
                FloatV: FloatClass,
                ArrowV: Arrow,
                PtrV: Ptr,
            }

            if ptr_flag:
                var = self.vm.env.get(self.vm.find_index_by_name(id_expr.id_name))
                value = self.interp(expr.expr)
                elem_type = self.vm.tt.get(var.get_type_index()).element_type
                if type(elem_type) != expr_v[type(value)]:
                    if type(elem_type) == FloatClass and expr_v[type(value)] == IntClass:
                        value = FloatV(value.value)
                        pass
                    else:
                        return ErrV("Ooooo. Variable type is wrong")

                ptr_index = self.interp(expr.id_expr[1])
                if type(ptr_index) != IntV:
                    return ErrV("Array type index should be Int!")

                self.vm.set_ptr_var(id_expr.id_name,
                                    ptr_index.value,
                                    value)
            else:
                var = self.vm.env.get(self.vm.find_index_by_name(id_expr.id_name))
                value = self.interp(expr.expr)
                if type(value) == ErrV:
                    return value

                var_type = self.vm.tt.get(var.get_type_index())
                if type(var_type) != expr_v[type(value)]:
                    if type(var_type) == FloatClass and expr_v[type(value)] == IntClass:
                        value = FloatV(value.value)
                        pass
                    else:
                        return ErrV("Ooooo. Variable type is wrong")
                self.vm.set_var(id_expr.id_name, value)

        return VoidV("Successfully set value")

    def decl_and_set(self, expr):
        """
        만약 expr.expr이 []라면 ptr타입인거임. 이거 체크 역시 해 줘야 함.

        * TODO: 이 중에서 set과 타입이 안 맞으면 제껴야함.
        :param expr:
        :return:
        """

        if type(expr.id_type) == Ptr:
            if expr.id_type.array_size != len(expr.expr):
                return ErrV("Array size is incorrect!")
            self.interp(Decl(expr.id_expr, expr.id_type))
            ret = None
            for i in range(len(expr.expr)):
                ret = self.interp(Set([expr.id_expr, i], expr.expr[i]))
            return ret
            # PTR 타입인 경우. 귀찮으니 지금은 넘어가자
        else:
            res = self.interp(Decl(expr.id_expr, expr.id_type))
            if type(res) == ErrV:
                return res
            return self.interp(Set(expr.id_expr, expr.expr))

    def id(self, expr):
        index = self.vm.find_index_by_name(expr.id_name)
        if index == -1:
            return ErrV("Free Identifier!")
        var = self.vm.env.get(index)
        value = self.vm.memory.get(var.get_value_index())

        return value

    def app(self, expr):

        types = {
            IntV: IntClass,
            CharV: CharClass,
            FloatV: FloatClass,
            PtrV: Ptr,
        }
        if type(expr.fun_name) != Id:
            return ErrV("Function name bucket should be Id")

        arrow_var = self.vm.env.get(self.vm.find_index_by_name(expr.fun_name.id_name))
        arrow_type = self.vm.tt.get(arrow_var.get_type_index())

        # check type of function
        if type(arrow_type) != Arrow:
            return ErrV("Type of function name should be ArrowT")

        param_index = 0
        param_value_type = None
        param_v = []
        for param in expr.param_values:
            interp_fin_param = self.interp(param)

            # check interpped_param is error
            if type(interp_fin_param) == ErrV:
                return interp_fin_param

            # check type of params
            if type(arrow_type.params[param_index]) != types[type(interp_fin_param)]:

                # check type OF PTR
                if type(arrow_type.params[param_index]) == Ptr:  # consider dynamic Ptr
                    param_value_type = self.get_type_of_id(param)
                    if type(arrow_type.params[param_index].element_type) == type(param_value_type.element_type):
                        pass
                    else:
                        return ErrV("In Function Appliation, Type of Ptr's element is different!")
                else:
                    print(type(arrow_type.params[param_index]))
                    print(str(arrow_type.params[param_index]))
                    return ErrV("Type of function parameters are different!")

            param_v.append(interp_fin_param)
            param_index += 1

        # TODO: should make new env with param_v
        new_env = EnvTable()
        temp_vm = VarManager(self.vm.tt, self.vm.histories, new_env, self.vm.memory, self.vm.proc)

        (names, statement) = self.vm.memory.get(arrow_var.get_value_index()).value

        for i in range(len(names)):
            param_name = names[i]
            param_type = arrow_type.params[i]
            param_value = param_v[i]

            if type(param_type) == IntClass:
                temp_vm.new_int(param_name.id_name, param_value)
            elif type(param_type) == FloatClass:
                temp_vm.new_float(param_name.id_name, param_value)
            elif type(param_type) == CharClass:
                temp_vm.new_char(param_name.id_name, param_value)
            elif type(param_type) == Ptr:
                temp_vm.new_ptr(param_name.id_name, param_value_type.element_type, param_value_type.array_size)
                ptr_index = self.vm.get_var_by_name(param.id_name).get_value_index()
                for i in range(param_value_type.array_size):
                    temp_vm.set_ptr_var(param_name.id_name, i, temp_vm.memory.get(i + ptr_index))
            else:
                return ErrV("Parameter Value is STRANGE")

        return AppV(temp_vm.env, statement.value)

    def get_type_of_id(self, expr):
        if type(expr) != Id:
            return ErrV("This function is only for Id")
        else:
            name = expr.id_name
            var = self.vm.get_var_by_name(name)
            return self.vm.tt.get(var.get_type_index())

    def fun(self, expr):
        new_var = self.interp(DeclAndSet(
            expr.fun_name,
            Arrow(expr.arg_types, expr.ret_type),
            ArrowV(expr.arg_names, IntV(expr.statement))
        ))

        if type(new_var) == ErrV:
            return new_var
        return VoidV("Function Set")

    def ela_for(self, expr):
        ret_val = self.interp(expr.init)
        if type(ret_val) == ErrV:
            return ret_val
        return ForV(ret_val)

    def ret(self, expr):
        ret_val = self.interp(expr.ret_val)
        if type(ret_val) == ErrV:
            return ret_val
        return RetV(ret_val)
    
    def decl(self, expr):
        id_expr = expr.id

        if type(id_expr) != Id:
            return ErrV("Variable is not Id type")

        else:
            index = self.vm.find_index_by_name(id_expr.id_name)
            if index != -1:
                return ErrV("Duplicate Name Error")

            # TODO: Check type !!
            type_of_id_type = type(expr.id_type)
            if type_of_id_type == IntClass:
                self.vm.new_int(id_expr.id_name, IntV(None))
            elif type_of_id_type == FloatClass:
                self.vm.new_float(id_expr.id_name, FloatV(None))
            elif type_of_id_type == CharClass:
                self.vm.new_char(id_expr.id_name, CharV(None))
            elif type_of_id_type == Ptr:
                array_size = self.interp(expr.id_type.array_size)
                if type(array_size) != IntV:
                    return ErrV("Array type size should be Int!")

                self.vm.new_ptr(
                    id_expr.id_name,
                    expr.id_type.element_type,
                    array_size.value
                )
            elif type_of_id_type == Arrow:
                ind = self.vm.new_arrow(
                    id_expr.id_name,
                    expr.id_type.params,
                    expr.id_type.ret,
                    ArrowV([], IntV(None))
                )
            else:
                return ErrV("No Type")

            return VoidV("Declaration Over")

    def __init__(self):
        tt = TypeTable()
        memory = ValueTable()
        env = EnvTable()
        histories = HistoryTable()
        proc = 0
        self.vm = VarManager(tt, histories, env, memory, proc)

    def eval(self, expr, line):
        """
        MAIN FUNCTION CALLED WITH INTERP
        :param expr: expression
        :param line: used for proc.
        :return: interped value
        """
        self.vm.set_proc(line)
        return self.interp(expr)

    def interp(self, expr):
        switch = {
            IntV: self.return_value,
            FloatV: self.return_value,
            CharV: self.return_value,
            ErrV: self.return_value,
            ArrowV: self.return_value,
            AppV: self.return_value,
            RetV: self.return_value,
            BoolV: self.return_value,
            PtrV: self.return_ptr_value,
            Add: self.add,
            Sub: self.sub,
            Mul: self.mul,
            Div: self.div,
            Set: self.set_val,
            Decl: self.decl,
            Id: self.id,
            DeclAndSet: self.decl_and_set,
            CondE: self.cond_e,
            CondG: self.cond_g,
            CondL: self.cond_l,
            CondGE: self.cond_ge,
            CondLE: self.cond_le,
            CondNE: self.cond_ne,
            If: self.ela_if,
            Print: self.printf,
            Fun: self.fun,
            Inc: self.inc,
            Dec: self.dec,
            Not: self.ela_not,
            For: self.ela_for,
            App: self.app,
            Ret: self.ret,
        }
        
        return switch[type(expr)](expr)

