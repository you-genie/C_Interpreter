"""Parse : uses implemented lex rule and yacc rule
input : text file
output : the text output of the AST structure per every line. 

@authorized by Shasha Bae
Will be changed according to proper input, and output format.
"""

import ply.lex as lex
import ply.yacc as yacc
from .LexRule import *
from .YaccRule import *


class Parser():

	def __init__(self, file):
		self.file = file
		self.result = []
		

	def parse(self):
		# Define user lexer, and parser
		#warnings.filterwarnings("ignore")
		lexer = lex.lex()
		parser = yacc.yacc()

		main_func = None

		# Run the parser per every line and print it.
		while True:
			line = self.file.readline()
			if not line: break
			try:
				result = parser.parse(line, tracking=True)

				# set main function define into first element of the result list
				if result != None:
					if result.name == ASTName.FUNCDEFINE:
						if result.get_child('id').data == 'main':
							main_func = result
							continue
					self.result.append(result)

			except SyntaxError as e:
				line = e.lineno
				# print("error : %d" % line)
				syntax_error = parser.parse("ERROR " + str(line), tracking=False)
				if syntax_error != None:
					self.result.append(result)

			

		if main_func != None:
			self.result = [main_func] + self.result

		return self.result

	def print_result(self):
		result = self.result
		for ast in result:
			print(ast)

	def print_result_next(self):
		result = self.result
		for ast in result:
			print()
			next_node = ast
			while next_node != None:
				print(next_node.name)
				next_node = next_node.next

			

	

if __name__ == "__main__":
	file_name = '../code.c'
	# file_name = '../test_code.txt'
	file = open(file_name, 'r')
	parser = Parser(file)
	parser.parse()
	parser.print_result()
	# parser.print_result_next()












