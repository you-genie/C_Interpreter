"""Type Interface
@authorized by Shasha Bae
overides lexer token
"""

# Token class
class LexToken(object):
	def __str__(self):
		return "LexToken({:>20}, {:>10}, {:>4d}, {:>4d})".format(self.type, self.value, self.lineno, self.lexpos)
	def __repr__(self):
		return str(self)
	def skip(self, n):
		self.lexer.skip(n)

# List of tokne names
tokens = [
	# Operand
	'NUMBER',
	'ID',
	'STRING',

	# Punctuation
	'SEMICOLON',
	'COMMA',

	# Assignment
	'ASSIGN',

	# Arithmetic operator
	'PLUS',
	'MINUS',
	'MULTIPLY',
	'DIVIDE',
	'INCREAMENT',
	'DECREAMENT',

	# Compare operator
	'EQUAL',
	'LESS',
	'LESS_EQUAL',
	'GREATER',
	'GREATER_EQUAL',

	# Brackets
	'L_PAREN',
	'R_PAREN',
	'L_CURLY_BRACKET',
	'R_CURLY_BRACKET',
	'L_SQUARE_BRACKET',
	'R_SQUARE_BRACKET',

]

# Reserved
reserved = {
	# Conditional control
	'if'		: 'IF',
	'else'		: 'ELSE',

	# Loop control
	'for'		: 'FOR',

	# Type declaration
	'int'		: 'INT',
	'float'		: 'FLOAT',
	'void'		: 'VOID',

	# Printf function
	'printf' 	: 'PRINT',

	# Return
	'return'	: 'RETURN',
	
}

tokens += reserved.values()

# Regular expression
# Punctuation
t_SEMICOLON 		= r'\;'
t_COMMA				= r'\,'

# Assignment
t_ASSIGN 			= r'\='

# Arithmetic operator
t_PLUS 				= r'\+'
t_MINUS 			= r'-'
t_MULTIPLY 			= r'\*'
t_DIVIDE 			= r'/'
t_INCREAMENT 		= r'\+\+'
t_DECREAMENT 		= r'\-\-'

# Compare operator
t_EQUAL 			= r'\=\='
t_LESS 				= r'\<'
t_LESS_EQUAL 		= r'\<\='
t_GREATER 			= r'\>'
t_GREATER_EQUAL 	= r'\>\='

# Brackets
t_L_PAREN 			= r'\('
t_R_PAREN			= r'\)'
t_L_CURLY_BRACKET 	= r'\{'
t_R_CURLY_BRACKET 	= r'\}'
t_L_SQUARE_BRACKET 	= r'\['
t_R_SQUARE_BRACKET	= r'\]'

# Operand
def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Number %s is too large!" % t.value)
		t.value = 0 
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_STRING(t):
	r'\".*\"'
	return t



# Ignore characters
t_ignore = ' \t'

# Ignore comment
def t_COMMENT(t):
	r'\#.*'
	pass

# Define a rule for tracking line numbers
def t_newline(t):
	r'\n+'
	
	# debug print for yacc
	#print('<<line %d>> ' % t.lexer.lineno)
	
	t.lexer.lineno += len(t.value)

	# debug pring for lex
	# print('<<line %d>> ' % t.lexer.lineno)
	

# Define a rult for tracking column numbers
def find_column(input, token):
	i = token.lexpos
	while(i > 0):
		if input[i] == '\n': break
		i -= 1


# Error handling
def t_error(t):
	print("Illegal character %s'" % t.value[0])
	t.lexer.skip(1)



