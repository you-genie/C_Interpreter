import abc

class Tree:

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self):
		pass

	@abc.abstractmethod
	def is_root(self):
		pass

	@abc.abstractmethod
	def add_child(self, child):
		pass

	@abc.abstractmethod
	def add_chidlen(self, children):
		pass

	@abc.abstractmethod
	def preorder_traverse(self):
		pass

	@abc.abstractmethod
	def postorder_traverse(self):
		pass


