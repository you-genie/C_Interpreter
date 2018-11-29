from LexRule import tokens
from Statement_Tree import AST


# Expression
def p_expression(p):
	'''	expression 	:	expression PLUS expression
					|	expression MINUS expression
					|	expression MULTIPLY expression
					|	expression DIVIDE expression
					|	expression INCREAMENT
					|	L_PAREN expression R_PAREN

					|	expression EQUAL expression
					|	expression LESS expression
					|	expression LESS_EQUAL expression
					|	expression GREATER expression
					|	expression GREATER_EQUAL expression
					
					|	type ID L_PAREN type ID expression R_PAREN L_CURLY_BRACKET
					|	COMMA type ID 
					|	RETURN expression
					|	R_CURLY_BRACKET

					|	NUMBER
					|	ID
					|	COMMA ID expression
					|	ID L_SQUARE_BRACKET expression R_SQUARE_BRACKET

					|	VOID
					|	type ID expression
					|	expression ASSIGN expression
					|	type ID L_SQUARE_BRACKET expression R_SQUARE_BRACKET
					
					|	WHILE L_PAREN expression R_PAREN L_CURLY_BRACKET
					|	IF L_PAREN expression R_PAREN L_CURLY_BRACKET
					|	FOR L_PAREN expression SEMICOLON expression SEMICOLON expression R_PAREN L_CURLY_BRACKET

					|	ID L_PAREN STRING R_PAREN

					|	expression SEMICOLON

					|	
					'''


	p[0] = p[1:]

def p_type(p):
	''' type 	:	INT
				|	FLOAT'''
	p[0] = p[1]