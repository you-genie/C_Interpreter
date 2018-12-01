from LexRule import tokens
from Statement_Tree import AST


# Expression
def p_expression(p):
	'''	
	expression 	:	inline SEMICOLON
				|	block
				|
	'''

	p[0] = p[1:]


def p_inline(p):
	'''
	inline 	:	declaration
			|	assign
			|	print
			|	return
			|
	'''

	p[0] = p[1:]


def p_block(p):
	'''
	block 	:	if
			|	for
	'''

	p[0] = p[1:]



#################################################################
#																#
#						<declaration CGF>						#
#																#
#################################################################
def p_declaration(p):
	''' 
	declaration 	:	type argument
	'''

	p[0] = p[1:]

#################################################################
#																#
#							<type CGF>							#
#																#
#################################################################
def p_type(p):
	''' 
	type 	:	INT pointer
			|	FLOAT pointer
	'''

	p[0] = p[1:]


def p_pointer(p):
	'''
	pointer 	:	MULTIPLY
				|
	'''

	p[0] = p[1:]

#################################################################
#																#
#						<variable CGF>							#
#																#
#################################################################
def p_variable(p):
	''' 
	variable 	:	primitive
				|	constructor
	'''
	
	p[0] = p[1:]


def p_more_variable(p):
	''' 
	more_variable 	:	COMMA variable more_variable
					|	
	'''

	p[0] = p[1:]


def p_primitive(p):
	'''
	primitive 	:	ID
	'''

	p[0] = p[1:]


def p_constructor(p):
	'''
	constructor  	:	array
	'''

	p[0] = p[1:]


def p_array(p):
	'''
	array 	:	ID L_SQUARE_BRACKET value R_SQUARE_BRACKET
	'''

	p[0] = p[1:]


def p_value(p):
	'''
	value 	:	value_
			|	operation
	'''

	p[0] = p[1:]


def p_value_(p):
	'''
	value_ 	:	variable
			|	function_call
			|	NUMBER
	'''

	p[0] = p[1:]


#################################################################
#																#
#						<assign CGF>							#
#																#
#################################################################
def p_assign(p):
	''' 
	assign 	:	variable ASSIGN value
	'''
	
	p[0] = p[1:]


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
	
	p[0] = p[1:]



def p_compare(p):
	'''	
	compare 	:	factor EQUAL factor_
				|	factor LESS factor_
				|	factor LESS_EQUAL factor_
				|	factor GREATER factor_
				|	factor GREATER_EQUAL factor_
	
	'''
	p[0] = p[1:]




def p_calculation(p):
	''' 
	calculation 	:	factor calculation_
					|	term
	'''
	
	p[0] = p[1:]


def p_calculation_(p):
	'''
	calculation_ 	:	PLUS factor_
					|	MINUS factor_ 
					|	INCREAMENT
					|	DECREAMENT
	'''

	p[0] = p[1:]


def p_term(p):
	'''
	term 	:	factor term_
	'''

	p[0] = p[1:]


def p_term_(p):
	'''
	term_ 	:	MULTIPLY factor_
			|	DIVIDE factor_
	'''

	p[0] = p[1:]


def p_factor(p):
	'''
	factor 	:	value_
	'''

	p[0] = p[1:]


def p_factor_(p):
	'''
	factor_ 	:	value
	'''

	p[0] = p[1:]


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
	arguments 	:	argument
				|	VOID
				|
	'''
	
	p[0] = p[1:]


def p_argument(p):
	''' 
	argument 	:	variable more_variable
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
#						<return CGF>							#
#																#
#################################################################
def p_return(p):
	''' 
	return 	:	RETURN value
	'''
	
	p[0] = p[1:]


	
#################################################################
#																#
#					<function_define CGF>						#
#																#
#################################################################
# def p_function_define(p):
# 	''' 
# 	function_define 	:	
# 	'''
	 
# 	p[0] = p[1:]


#################################################################
#																#
#							<if CGF>							#
#																#
#################################################################
def p_if(p):
	''' 
	if 	:	IF L_PAREN operation R_PAREN
	'''
	
	p[0] = p[1:]


#################################################################
#																#
#							<for CGF>							#
#																#
#################################################################
def p_for(p):
	''' 
	for 	:	FOR L_PAREN operation SEMICOLON operation SEMICOLON operation R_PAREN
	'''
	
	p[0] = p[1:]