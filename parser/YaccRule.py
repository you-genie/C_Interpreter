from LexRule import tokens
from Statement_Tree import AST
from util.ASTName import ASTName

# Error handling
def p_error(token):
	if token is not None:
		print ("Line %s, illegal token %s" % (token.lineno, token.value))
	else:
		print('Unexpected end of input');


# Expression
def p_expression(p):
	'''	
	expression 	:	inline semicolons
				|	block
				|	L_CURLY_BRACKET
				|	R_CURLY_BRACKET
				|	semicolons
				|	
	'''

	print("\n")
	if len(p) != 1:
		p[0] = p[1]
	else:
		p[0] = None


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

	# p[0] = p[1:]


def p_more_semicolon(p):
	'''
	more_semicolon 	:	SEMICOLON more_semicolon
					|	
	'''

	# p[0] = p[1:]


#################################################################
#																#
#						<declaration CGF>						#
#																#
#################################################################
def p_declaration(p):
	''' 
	declaration 	:	type variables
	'''

	node = AST(name = ASTName.DECL)
	node.add_child('type', p[1])
	node.add_child('vars', p[2])

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
		node = AST(name=ASTName.INT)
	if p[1] == 'int' and len(p) == 3:
		node = AST(name=ASTName.INTP)
	if p[1] == 'float' and len(p) == 2:
		node = AST(name=ASTName.FLOAT)
	if p[1] == 'float' and len(p) == 3:
		node = AST(name=ASTName.FLOATP)

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
	node = AST(name = ASTName.VARS, data = variable_list)

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

	node = AST(name=ASTName.ID, data=p[1])

	p[0] = node


def p_constructor(p):
	'''
	constructor  	:	array
	'''

	p[0] = p[1]


def p_array(p):
	'''
	array 	:	ID L_SQUARE_BRACKET value R_SQUARE_BRACKET
	'''

	node = AST(name=ASTName.ARRAY)

	node.add_child('id', AST(name = ASTName.ID, data = p[1]))
	node.add_child('size', p[3])

	p[0] = node


def p_value(p):
	'''
	value 	:	value_
			|	operation
	'''

	p[0] = p[1]


def p_value_(p):
	'''
	value_ 	:	variable
			|	function_call
			|	number
	'''

	p[0] = p[1]

	
def p_number(p):
	'''
	number 	:	NUMBER
	'''

	node = AST(name = ASTName.NUM, data = p[1])
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
	
	node = AST(name = ASTName.ASSIGN)
	node.add_child('var', p[1])
	node.add_child('value', p[3])

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
				|	calculation
	'''
	
	node = None

	if len(p) == 4:
		node = p[2]
	else:
		node = p[1]

	p[0] = node



def p_compare(p):
	'''	
	compare 	:	factor EQUAL factor
				|	factor LESS factor
				|	factor LESS_EQUAL factor
				|	factor GREATER factor
				|	factor GREATER_EQUAL factor
	
	'''

	node = None

	if p[2] == '==':
		node = AST(name = ASTName.EQ)
	elif p[2] == '<':
		node = AST(name = ASTName.LESS)
	elif p[2] == '<=':
		node = AST(name = ASTName.LESSEQ)
	elif p[2] == '>':
		node = AST(name = ASTName.GREATER)
	elif p[2] == '>=':
		node = AST(name = ASTName.GREATEREQ)

	node.add_child('left', p[1])
	node.add_child('right', p[3])

	p[0] = node


def p_calculation(p):
	''' 
	calculation 	:	calculation_ PLUS term_
					|	calculation_ MINUS term_
					|	variable INCREAMENT
					|	variable DECREAMENT
					|	term
	'''

	node = None

	if len(p) == 4:
		ast_name = ASTName.PLUS if p[2] == '+' else ASTName.MINUS
		node = AST(name = ast_name)
		node.add_child('left', p[1])
		node.add_child('right', p[3])

	elif len(p) == 3:
		node = AST(name = ASTName.INC)
		node.add_child('var', p[1])

	elif len(p) == 2:
		node = p[1]


	p[0] = node


def p_calculation_(p):
	''' 
	calculation_ 	:	calculation_ PLUS term_
					|	calculation_ MINUS term_
					|	term_
	'''

	node = None

	if len(p) == 4:
		ast_name = ASTName.PLUS if p[2] == '+' else ASTName.MINUS
		node = AST(name = ast_name)
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
	node = AST(name = ast_name)
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
		node = AST(name = ast_name)
		node.add_child('left', p[1])
		node.add_child('right', p[3])
	elif len(p) == 2:
		node = p[1]

	p[0] = node


def p_factor(p):
	'''
	factor 	:	value_
	'''

	p[0] = p[1]


#################################################################
#																#
#						<function CGF>							#
#																#
#################################################################
def p_function_call(p):
	''' 
	function_call 	:	ID L_PAREN arguments R_PAREN
	'''
	
	p[0] = p[1:]


def p_arguments(p):
	''' 
	arguments 	:	argument more_argument
				|	VOID
				|
	'''
	
	p[0] = p[1:]


def p_argument(p):
	''' 
	argument 	:	value
	'''
	
	p[0] = p[1:]


def p_more_argument(p):
	'''
	more_argument 	:	COMMA argument
					|	
	'''

	p[0] = p[1:]


#################################################################
#																#
#						<print CGF>								#
#																#
#################################################################
def p_print(p):
	''' 
	print 	:	PRINT L_PAREN STRING more_variable R_PAREN
	'''
	
	p[0] = p[1:]

	
#################################################################
#																#
#					<function_define CGF>						#
#																#
#################################################################
def p_function_define(p):
	''' 
	function_define 	:	function_define_ L_CURLY_BRACKET
						|	function_define_
	'''
	 
	p[0] = p[1:]


def p_function_define_(p):
	''' 
	function_define_ 	:	type ID L_PAREN parameters R_PAREN 
	'''
	 
	p[0] = p[1:]


def p_parameters(p):
	'''
	parameters	:	parameter more_parameter
				|	VOID
				|
	'''

	p[0] = p[1:]


def p_parameter(p):
	'''
	parameter	:	type ID
	'''

	p[0] = p[1:]


def p_more_parameter(p):
	'''
	more_parameter	:	COMMA parameter
					|	
	'''

	p[0] = p[1:]


def p_return(p):
	''' 
	return 	:	RETURN value
	'''
	
	p[0] = p[1:]


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
	
	p[0] = p[1:]


def p_if_(p):
	''' 
	if_ 	:	IF L_PAREN operation R_PAREN
	'''
	
	p[0] = p[1:]


def p_else(p):
	''' 
	else 	:	R_CURLY_BRACKET else_ L_CURLY_BRACKET
			|	else_ L_CURLY_BRACKET
			|	else_
	'''
	
	p[0] = p[1:]


def p_else_(p):
	''' 
	else_ 	:	ELSE 
	'''
	
	p[0] = p[1:]


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
	
	p[0] = p[1:]


def p_for_(p):
	''' 
	for_ 	:	FOR L_PAREN assign SEMICOLON operation SEMICOLON operation R_PAREN
	'''
	
	p[0] = p[1:]




















