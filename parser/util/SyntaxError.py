"""Syntax error exception : Syntax error exception handling

@authorized by Shasha Bae
inherited Exception class
"""

class SyntaxError(Exception):
	def __init__(self, lineno = -1):
		self.lineno = lineno
