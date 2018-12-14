"""ASTName class : Represent the name of the each tree node
 
@authorized by Shasha Bae
overides enum class
"""

import enum

class ASTName(enum.Enum):

	# Operand
	NUM = 0
	ID = 1
	STR = 2
	ARRAY = 3

	# Declaration
	DECL = 4
	VARS = 5

	# Type
	INT = 6
	INTP = 7
	FLOAT = 8
	FLOATP = 9

	# Assignment
	ASSIGN = 10

	# Operation
	PLUS = 11
	MINUS = 12
	MULTI = 13
	DIV = 14
	INCR = 15
	DECR = 16

	EQ = 17
	LESS = 18
	LESSEQ = 19
	GREATER = 20
	GREATEREQ = 21


	# Condition
	IF = 22
	ELSE = 23
	BODY = 24
	
	# Loop
	FOR = 25

	# Function
	FUNCDEFINE = 26
	PARAM = 27
	PARAMS = 28
	RET = 29

	FUNCCALL = 30
	ARGS = 31

	# Print
	PRINT = 32
