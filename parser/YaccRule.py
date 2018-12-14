"""Yacc Grammar : The grammar for LALR(1) parser given tokenized input by lex rule.
For inambiguousity, no grammar occurs reduce/shift and reduce/reduce conflicts.

@authorized by Shasha Bae
"else" part is not fully implemented yet because it is not shown in code.c
"""

from .LexRule import tokens
from parser.util.Statement_Tree import AST
from parser.util.ASTName import ASTName
from parser.util.State import State, StateName


state = State()


# Error handling
def p_error(token):
	if token is not None:
		print ("(Yacc) Line %s, illegal token %s" % (token.lineno, token.value))
	else:
		print('Unexpected end of input');


#################################################################
#																#
#					<basic statement CGF>						#
#																#
#################################################################
def p_expression(p):
	'''	
	expression 	:	inline semicolons
				|	block
				|	L_CURLY_BRACKET
				|	R_CURLY_BRACKET
				|	
	'''

	#print("\n")
	node = None

	if len(p) == 1:		# Just newline
		p[0] = None

	else:				
		if p[1] == '}':		# It means the close of current scope
			node = state.pop_state()

			# link node with next pointer
			if node.name == ASTName.FUNCDEFINE:
				current_body = None
				for body_element in node.get_child('body').data:
					if node.next == None:
						node.next = body_element

					else:
						if current_body != None:
							current_body.next = body_element

					current_body = body_element


		else:			

			# set current state node as the state of the current procedure
			if state.get_state() == StateName.NONE:		# there is no scope
				node = p[1]
			else:									# there is some scope above this statement
				node = state.node()
				node.get_child('body').data.append(p[1])


			if state.get_flag():					# True if new 'if', 'for', 'function definition' is occured
				node = p[1]
				if node.name == ASTName.IF:
					state.set_state(state_name = 'if', node = node)
				elif node.name == ASTName.ELSE:
					state.set_state(state_name = 'else', node = node)
				elif node.name == ASTName.FOR:
					state.set_state(state_name = 'for', node = node)
				elif node.name == ASTName.FUNCDEFINE:
					state.set_state(state_name = 'function', node = node)

				state.set_flag(False)

			#node = state.root_node()

	
		# if node == None and p[1] != '}':
		# 	node = p[1]
		if state.get_state() != StateName.NONE:
			node = None
		p[0] = node


def p_inline(p):
	'''
	inline 	:	declaration
			|	assign
			|	print
			|	return
	'''

	p[0] = p[1]


def p_block(p):
	'''
	block 	:	if
			|	else
			|	for
			|	function_define
	'''

	p[0] = p[1]


def p_semicolons(p):
	'''
	semicolons 	:	SEMICOLON more_semicolon
	'''


def p_more_semicolon(p):
	'''
	more_semicolon 	:	SEMICOLON more_semicolon
					|	
	'''


#################################################################
#																#
#						<declaration CGF>						#
#																#
#################################################################
def p_declaration(p):
	''' 
	declaration 	:	type variables
	'''

	node = AST(name = ASTName.DECL, lineno = p.lineno(0))
	node.add_child('type', p[1])
	node.add_child('ids', p[2])

	p[0] = node

#################################################################
#																#
#							<type CGF>							#
#																#
#################################################################
def p_type(p):
	''' 
	type 	:	INT 
			|	INT MULTIPLY
			|	FLOAT
			|	FLOAT MULTIPLY
	'''

	node = None

	if p[1] == 'int' and len(p) == 2:
		node = AST(name=ASTName.INT, lineno = p.lineno(0))
	if p[1] == 'int' and len(p) == 3:
		node = AST(name=ASTName.INTP, lineno = p.lineno(0))
	if p[1] == 'float' and len(p) == 2:
		node = AST(name=ASTName.FLOAT, lineno = p.lineno(0))
	if p[1] == 'float' and len(p) == 3:
		node = AST(name=ASTName.FLOATP, lineno = p.lineno(0))

	p[0] = node


#################################################################
#																#
#						<variable CGF>							#
#																#
#################################################################
def p_variables(p):
	'''
	variables 	:	variable more_variable
	'''

	variable_list = [p[1]] + p[2]
	node = AST(name = ASTName.IDS, data = variable_list, lineno = p.lineno(0))

	p[0] = node


def p_variable(p):
	''' 
	variable 	:	primitive
				|	constructor
	'''
	
	p[0] = p[1]


def p_more_variable(p):
	''' 
	more_variable 	:	COMMA variable more_variable
					|	
	'''

	p[0] = []
	if len(p) != 1:
		p[0] = [p[2]] + p[3]


def p_primitive(p):
	'''
	primitive 	:	ID
	'''

	node = AST(name=ASTName.ID, data=p[1], lineno = p.lineno(0))

	p[0] = node


def p_constructor(p):
	'''
	constructor  	:	array
	'''

	p[0] = p[1]


def p_array(p):
	'''
	array 	:	primitive L_SQUARE_BRACKET value R_SQUARE_BRACKET
	'''

	node = AST(name=ASTName.ARRAY, lineno = p.lineno(0))

	node.add_child('id', p[1])
	node.add_child('index', p[3])

	p[0] = node


def p_value(p):
	'''
	value 	:	value_
			|	operation
	'''

	p[0] = p[1]


def p_value_(p):
	'''
	value_ 	:	L_PAREN value_ R_PAREN
			|	variable
			|	function_call
			|	number
	'''

	node = None

	if len(p) == 4:
		node = p[2]
	else:
		node = p[1]

	p[0] = node

	
def p_number(p):
	'''
	number 	:	NUMBER
	'''

	node = AST(name = ASTName.NUM, data = p[1], lineno = p.lineno(0))
	p[0] = node

#################################################################
#																#
#						<assign CGF>							#
#																#
#################################################################
def p_assign(p):
	''' 
	assign 	:	variable ASSIGN value
	'''
	
	node = AST(name = ASTName.ASSIGN, lineno = p.lineno(0))
	node.add_child('lvalue', p[1])
	node.add_child('rvalue', p[3])

	p[0] = node


#################################################################
#																#
#						<operation CGF>							#
#																#
#################################################################
def p_operation(p):
	''' 
	operation 	:	L_PAREN operation R_PAREN
				|	compare
				|	binary_calc
				|	unary
	'''
	
	node = None

	if len(p) == 4:
		node = p[2]
	else:
		node = p[1]

	p[0] = node


def p_compare(p):
	'''	
	compare 	:	value EQUAL value
				|	value LESS value
				|	value LESS_EQUAL value
				|	value GREATER value
				|	value GREATER_EQUAL value
	
	'''

	node = None

	if p[2] == '==':
		node = AST(name = ASTName.EQ, lineno = p.lineno(0))
	elif p[2] == '<':
		node = AST(name = ASTName.LESS, lineno = p.lineno(0))
	elif p[2] == '<=':
		node = AST(name = ASTName.LESSEQ, lineno = p.lineno(0))
	elif p[2] == '>':
		node = AST(name = ASTName.GREATER, lineno = p.lineno(0))
	elif p[2] == '>=':
		node = AST(name = ASTName.GREATEREQ, lineno = p.lineno(0))

	node.add_child('left', p[1])
	node.add_child('right', p[3])

	p[0] = node


def p_unary(p):
	'''
	unary 	:	variable INCREAMENT
			|	variable DECREAMENT
	'''

	ast_name = ASTName.INCR if p[2] == '++' else ASTName.DECR
	node = AST(name = ast_name, lineno = p.lineno(0))
	node.add_child('id', p[1])

	p[0] = node


def p_binary_calc(p):
	''' 
	binary_calc 	:	binary_calc_ PLUS term_
					|	binary_calc_ MINUS term_
					|	term
	'''

	node = None

	if len(p) == 4:
		ast_name = ASTName.PLUS if p[2] == '+' else ASTName.MINUS
		node = AST(name = ast_name, lineno = p.lineno(0))
		node.add_child('left', p[1])
		node.add_child('right', p[3])

	elif len(p) == 2:
		node = p[1]


	p[0] = node


def p_binary_calc_(p):
	''' 
	binary_calc_ 	:	binary_calc_ PLUS term_
					|	binary_calc_ MINUS term_
					|	term_
	'''

	node = None

	if len(p) == 4:
		ast_name = ASTName.PLUS if p[2] == '+' else ASTName.MINUS
		node = AST(name = ast_name, lineno = p.lineno(0))
		node.add_child('left', p[1])
		node.add_child('right', p[3])
	elif len(p) == 2:
		node = p[1]

	p[0] = node


def p_term(p):
	'''
	term 	:	term_ MULTIPLY factor
			|	term_ DIVIDE factor
	'''

	ast_name = ASTName.MULTI if p[2] == '*' else ASTName.DIV
	node = AST(name = ast_name, lineno = p.lineno(0))
	node.add_child('left', p[1])
	node.add_child('right', p[3])

	p[0] = node


def p_term_(p):
	'''
	term_ 	:	term_ MULTIPLY factor
			|	term_ DIVIDE factor
			|	factor
	'''

	node = None

	if len(p) == 4:
		ast_name = ASTName.MULTI if p[2] == '*' else ASTName.DIV
		node = AST(name = ast_name, lineno = p.lineno(0))
		node.add_child('left', p[1])
		node.add_child('right', p[3])
	elif len(p) == 2:
		node = p[1]

	p[0] = node


def p_factor(p):
	'''
	factor 	:	value
	'''

	p[0] = p[1]


#################################################################
#																#
#							<if CGF>							#
#																#
#################################################################
def p_if(p):
	''' 
	if 	:	if_ L_CURLY_BRACKET 
		|	if_
	'''
	
	p[0] = p[1]


def p_if_(p):
	''' 
	if_ 	:	IF L_PAREN operation R_PAREN
	'''
	
	node = AST(name = ASTName.IF, lineno = p.lineno(0))
	node.add_child('cond', p[3])
	node.add_child('body', AST(name = ASTName.BODY, data = [], lineno = p.lineno(0)))

	state.set_flag(True)

	p[0] = node


def p_else(p):
	''' 
	else 	:	R_CURLY_BRACKET else_ L_CURLY_BRACKET
			|	else_ L_CURLY_BRACKET
			|	else_
	'''

	node = None

	if len(p) == 4:
		node = p[2]
	elif len(p) == 3 or len(p) == 2:
		node = p[1]
	
	p[0] = node


def p_else_(p):
	''' 
	else_ 	:	ELSE 
	'''

	node = AST(name = ASTName.ELSE)
	node.add_child('body', AST(name = ASTName.BODY, data = [], lineno = p.lineno(0)))

	state.set_flag(True)
	
	p[0] = p[1]


#################################################################
#																#
#							<for CGF>							#
#																#
#################################################################
def p_for(p):
	''' 
	for 	:	for_ L_CURLY_BRACKET
			|	for_
	'''
	
	p[0] = p[1]


def p_for_(p):
	''' 
	for_ 	:	FOR L_PAREN assign SEMICOLON operation SEMICOLON operation R_PAREN
	'''
	
	node = AST(name = ASTName.FOR, lineno = p.lineno(0))
	node.add_child('init', p[3])
	node.add_child('cond', p[5])
	node.add_child('iter', p[7])
	node.add_child('body', AST(name = ASTName.BODY, data = [], lineno = p.lineno(0)))

	state.set_flag(True)

	p[0] = node


#################################################################
#																#
#					<function define CGF>						#
#																#
#################################################################
def p_function_define(p):
	''' 
	function_define 	:	function_define_ L_CURLY_BRACKET
						|	function_define_
	'''
	 
	p[0] = p[1]


def p_function_define_(p):
	''' 
	function_define_ 	:	type primitive L_PAREN parameters R_PAREN 
	'''

	node = AST(name = ASTName.FUNCDEFINE, lineno = p.lineno(0))
	node.add_child('type', p[1])
	node.add_child('id', p[2])
	node.add_child('params', p[4])
	node.add_child('body', AST(name = ASTName.BODY, data = [], lineno = p.lineno(0)))

	state.set_flag(True)

	p[0] = node


def p_parameters(p):
	'''
	parameters	:	parameter more_parameter
				|	VOID
				|
	'''

	param_list = []

	if len(p) == 3:
		param_list = [p[1]] + p[2]

	node = AST(name = ASTName.PARAMS, data = param_list, lineno = p.lineno(0))

	p[0] = node


def p_parameter(p):
	'''
	parameter	:	type primitive
	'''

	node = AST(name = ASTName.PARAM, lineno = p.lineno(0))
	node.add_child('type', p[1])
	node.add_child('id', p[2])

	p[0] = node


def p_more_parameter(p):
	'''
	more_parameter	:	COMMA parameter more_parameter
					|	
	'''

	param_list = []

	if len(p) != 1:
		param_list = [p[2]] + p[3]

	p[0] = param_list


def p_return(p):
	''' 
	return 	:	RETURN value
	'''

	node = AST(name = ASTName.RET, lineno = p.lineno(0))
	node.add_child('value', p[2])
	
	p[0] = node


#################################################################
#																#
#						<function call CGF>						#
#																#
#################################################################
def p_function_call(p):
	''' 
	function_call 	:	primitive L_PAREN arguments R_PAREN
	'''
	
	node = AST(name = ASTName.FUNCCALL, lineno = p.lineno(0))
	node.add_child('id', p[1])
	node.add_child('args', p[3])

	p[0] = node


def p_arguments(p):
	''' 
	arguments 	:	argument more_argument
				|	VOID
				|
	'''
	
	args_list = []

	if len(p) == 3:
		args_list = [p[1]] + p[2]

	node = AST(name = ASTName.ARGS, data = args_list, lineno = p.lineno(0))

	p[0] = node


def p_argument(p):
	''' 
	argument 	:	value
	'''
	
	p[0] = p[1]


def p_more_argument(p):
	'''
	more_argument 	:	COMMA argument more_argument
					|	
	'''

	args_list = []

	if len(p) != 1:
		args_list = [p[2]] + p[3]

	p[0] = args_list


#################################################################
#																#
#						<print CGF>								#
#																#
#################################################################
def p_print(p):
	''' 
	print 	:	PRINT L_PAREN STRING more_variable R_PAREN
	'''
	
	node = AST(name = ASTName.PRINT, lineno = p.lineno(0))
	node.add_child('str', AST(name = ASTName.STR, data = p[3], lineno = p.lineno(0)))
	node.add_child('args', AST(name = ASTName.ARGS, data = p[4], lineno = p.lineno(0)))

	p[0] = node






