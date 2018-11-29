from LexRule import tokens
from Statement_Tree import AST

def p_expression_plus(p):
	'expression : expression PLUS term'
	p[0] = p[1] + p[3]

def p_expression_term(p):
	'expression : term'
	p[0] = p[1]

def p_term_factor(p):
	'term : factor'
	p[0] = p[1]

def p_factor(p):
	'factor : NUMBER'
	p[0] = p[1]
