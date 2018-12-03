import ply.lex as lex
import ply.yacc as yacc
from  LexRule import *
from YaccRule import *

code = open('test_code.txt', 'r')
code = open('../code.c', 'r')

lexer = lex.lex()

# Debug for lexer
# lexer.input(code.read())
# while 1:
# 	tok = lexer.token()
# 	if not tok: break
# 	print(tok)


parser = yacc.yacc()

while True:
	line = code.readline()
	if not line: break
	result = parser.parse(line)
	print(result)