import util.Tree as Tree

class AST():
	def __init__(self, data, is_root=False):
		self.data = data
		self.children = []
		self.is_root = is_root
	
	def __str__(self, level=0):
		ret = "\t" * level + self.data + "\n"
		for child in self.children:
			ret += child.__str__(level + 1)
		return ret

	def is_root(self):
		return self.is_root

	def add_child(self, child):
		self.children.append(child)

	def add_chidlen(self, children):
		self.children += children

	def preorder_traverse(self):
		print(self.data,)
		for child in self.children:
			preorder_traverse(child)
 
	def postorder_traverse(self):
		for child in self.children:
			postorder_traverse(child)
		print (self.data,)