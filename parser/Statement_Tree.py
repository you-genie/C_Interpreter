from util.Tree import Tree

class AST(Tree):

	def __init__(self, name, data = None):
		self.name = name		# ASTName class
		self.data = data		# NUMBER, ID has data
		self.children = {} 		# Dictionary data structure
	
	def __str__(self, level=0, is_list=False):
		ret = "\t" * level + "<" + str(self.name) + ">"

		if self.data != None:
			if type(self.data) is list:
				ret += " [ "
				elements = []
				for elem in self.data:
					elements.append(elem.__str__(0, True))
				ret += ",\t".join(elements)
				ret += " ] "
			else:
				ret += " : " + str(self.data)
		
		if not is_list:
			ret += "\n"

		for child in self.children.values():
			ret += child.__str__(level + 1, is_list)
		return ret

	def __repr__(self):
		return self.__str__(level=0, is_list=False)

	def add_child(self, key, child):
		self.children[key] = child

