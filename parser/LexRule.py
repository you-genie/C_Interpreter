"""Lex Token : Contains all of the tokens needed in c interpreter. Also defines the counter of line number and column number rules. 

@authorized by Shasha Bae
Referred PLY Tutorial code.
"""

from Parser.Util.SyntaxError import SyntaxError


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
	'NUMBER_INT',
	'NUMBER_FLOAT',
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
	'NOT',
	'EQUAL',
	'NOT_EQUAL',
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

	# Error
	'ERROR' : 'ERROR'
	
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
t_MINUS 			= r'\-'
t_MULTIPLY 			= r'\*'
t_DIVIDE 			= r'\/'
t_INCREAMENT 		= r'\+\+'
t_DECREAMENT 		= r'\-\-'

# Compare operator
t_NOT 				= r'\!'
t_EQUAL 			= r'\=\='
t_NOT_EQUAL 		= r'\!\='
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
	r'\d*\.?\d+'
	try:
		t.value = int(t.value)
		t.type = 'NUMBER_INT'
		return t
	except ValueError:
		pass

	try:
		t.value = float(t.value)
		t.type = 'NUMBER_FLOAT'
		return t
	except ValueError:
		pass

	self.t_error("Not INT or FLOAT: " + t.value)

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
	r'\\.*'
	pass


# Define a rule for tracking line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	

# Define a rult for tracking column numbers
def find_column(input, token):
	i = token.lexpos
	while(i > 0):
		if input[i] == '\n': break
		i -= 1


# Error handling
def t_error(t):
	# print("(Lex) Illegal character %s" % t.value[0])
	#t.lexer.skip(1)
	raise SyntaxError(t.lineno)
	



