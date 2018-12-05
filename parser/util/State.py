import enum

class State():

	def __init__(self):
		self.flag = False
		self.states = []
		self.nodes = []

	def state(self):
		if self.states == []:
			return StateName.NONE
		return self.states[-1]

	def root_node(self):
		if self.nodes == []:
			return None
		return self.nodes[0]

	def node(self):
		if self.nodes == []:
			return None
		return self.nodes[-1]

	def get_flag(self):
		return self.flag

	def set_flag(self, flag):
		self.flag = flag

	def set_state(self, state_name, node = None):
		if state_name == 'if':
			self.states.append(StateName.IF)
		elif state_name == 'else':
			self.states.append(StateName.ELSE)
		elif state_name == 'for':
			self.states.append(StateName.FOR)
		elif state_name == 'function':
			self.states.append(StateName.FUNC)
		else:
			raise("No such state name: %s", state_name)

		self.nodes.append(node)
		
	def pop_state(self):
		self.states.pop()
		self.nodes.pop()

class StateName(enum.Enum):
	NONE = 0
	IF = 1
	ELSE = 2
	FOR = 3
	FUNC = 4