"""AST class : Node class of AST node. Node have names, data, and childen attributes

@authorized by Shasha Bae
"The categories of children keys" : ""
"""

from Parser.Util.Tree import Tree

class AST(Tree):

	def __init__(self, name, data = None, lineno = -1):
		self.name = name		# ASTName class
		self.data = data		# only NUMBER, ID has data, and body
		self.children = {} 		# Dictionary data structure
		self.lineno = lineno	# Line number
		self.next = None
	
	def __str__(self, level=0):
		indent = "  "
		ret = indent * level + "(line %d) " % self.lineno + "<" + str(self.name) + ">"

		if self.data != None:
			if type(self.data) is list:
				ret += "\n" + indent * (level + 1) + "[\n"
				elements = []
				for elem in self.data:
					elements.append(elem.__str__(level + 2).rstrip())
				ret += ",\n".join(elements)
				ret += "\n" + indent * (level + 1) + "]"
			else:
				ret += " : " + str(self.data)
		
		ret += "\n"

		for child in self.children.values():
			ret += child.__str__(level + 1)
		return ret

	def __repr__(self):
		return self.__str__(level=0)

	def add_child(self, key, child):
		self.children[key] = child

	def get_child(self, key):
		return self.children[key]

	def get_name(self):
		return self.name

	def get_data(self):
		return self.data

	def get_lineno(self):
		return self.lineno

