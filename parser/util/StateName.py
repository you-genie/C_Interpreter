"""StateName class : Represent the name of the state
 
@authorized by Shasha Bae
overides enum class
"""

import enum

class StateName(enum.Enum):
	NONE = 0
	IF = 1
	ELSE = 2
	FOR = 3
	FUNC = 4