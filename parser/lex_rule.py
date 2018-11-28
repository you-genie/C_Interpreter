import ply.lex as lex

# list of tokne names
tokens = (
	'NUMBER',
	'ID',
	'PLUS',
	'MINUS',
	'MULTI',
	'DIVIDE',
)

# regular expression
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'

# reserved
reserved = {
	'if': 'IF',
	'then': 'THEN',
	'else': 'ELSE',
}

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

# ignore characters
t_ignore = ' \t'

# ignore commens
def t_COMMENT(t):
	r'\#.*'
	pass

# define a rule for tracking line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	print('\n')

# define a rult for tracking column numbers
def find_column(input, token):
	i = token.lexpos
	while(i > 0):
		if input[i] == '\n': break
		i -= 1


# error handling
def t_error(t):
	print("Illegal character %s'" % t.value[0])
	t.lexer.skip(1)


# token class
class LexToken(object):
	def __str__(self):
		return "LexToken(%s, %r, %d, %d)" % (self.type, self.value, self.lineno, self.lexpos)
	def __repr__(self):
		return str(self)
	def skip(self, n):
		self.lexer.skip(n)
