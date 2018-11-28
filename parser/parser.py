import ply.lex as lex
from  lex_rule import *
from yacc_rule import *

code = open('test_code.txt', 'r')
lexer = lex.lex()
lexer.input(code.read())
while 1:
	tok = lexer.token()
	if not tok: break
	print(tok)
