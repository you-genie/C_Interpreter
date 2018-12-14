"""Tree class : Basic tree metaclass. 

@authorized by Shasha Bae
"""

import abc

class Tree:

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self):
		pass

	@abc.abstractmethod
	def add_child(self, child):
		pass



