from LexRule import tokens
from Statement_Tree import AST


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

	p[0] = p[1:]


def p_inline(p):
	'''
	inline 	:	declaration
			|	assign
			|	print
			|	return
	'''

	p[0] = p[1:]


def p_block(p):
	'''
	block 	:	if
			|	else
			|	for
			|	function_define
	'''

	p[0] = p[1:]


def p_semicolons(p):
	'''
	semicolons 	:	SEMICOLON more_semicolon
	'''

	p[0] = p[1:]


def p_more_semicolon(p):
	'''
	more_semicolon 	:	SEMICOLON more_semicolon
					|	
	'''

	p[0] = p[1:]


#################################################################
#																#
#						<declaration CGF>						#
#																#
#################################################################
def p_declaration(p):
	''' 
	declaration 	:	type variables
	'''

	p[0] = p[1:]

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

	p[0] = p[1:]


#################################################################
#																#
#						<variable CGF>							#
#																#
#################################################################
def p_variables(p):
	'''
	variables 	:	variable more_variable
	'''

	p[0] = p[1:]


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
	compare 	:	factor EQUAL factor
				|	factor LESS factor
				|	factor LESS_EQUAL factor
				|	factor GREATER factor
				|	factor GREATER_EQUAL factor
	
	'''
	p[0] = p[1:]


def p_calculation(p):
	''' 
	calculation 	:	calculation_ PLUS term_
					|	calculation_ MINUS term_
					|	ID INCREAMENT
					|	ID DECREAMENT
					|	term
	'''
	 
	p[0] = p[1:]


def p_calculation_(p):
	''' 
	calculation_ 	:	calculation_ PLUS term_
					|	calculation_ MINUS term_
					|	term_
	'''
	 
	p[0] = p[1:]


def p_term(p):
	'''
	term 	:	term_ MULTIPLY factor
			|	term_ DIVIDE factor
	'''

	p[0] = p[1:]


def p_term_(p):
	'''
	term_ 	:	term_ MULTIPLY factor
			|	term_ DIVIDE factor
			|	factor
	'''

	p[0] = p[1:]


def p_factor(p):
	'''
	factor 	:	value_
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




















