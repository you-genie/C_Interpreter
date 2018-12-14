"""Parse : uses implemented lex rule and yacc rule
input : text file
output : the text output of the AST structure per every line. 

@authorized by Shasha Bae
Will be changed according to proper input, and output format.
"""

import ply.lex as lex
import ply.yacc as yacc
from  LexRule import *
from YaccRule import *

# Code for sample text
code = open('../test_code.txt', 'r')
# Original code
code = open('../code.c', 'r')

# Define user lexer, and parser
lexer = lex.lex()
parser = yacc.yacc()

# Run the parser per every line and print it.
while True:
	line = code.readline()
	if not line: break
	result = parser.parse(line, tracking=True)
	print(result)