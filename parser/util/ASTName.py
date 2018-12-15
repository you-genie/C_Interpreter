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
	IDS = 5

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

	NOT = 17
	EQ = 18
	NEQ = 19
	LESS = 20
	LESSEQ = 21
	GREATER = 22
	GREATEREQ = 23

	# Condition
	IF = 24
	ELSE = 25
	BODY = 26
	
	# Loop
	FOR = 27

	# Function
	FUNCDEFINE = 28
	PARAM = 29
	PARAMS = 30
	RET = 31

	FUNCCALL = 32
	ARGS = 33

	# Print
	PRINT = 34

	# Temp
	RAX = 35

	# Line break
	# LINEBREAK = 36

	# Error
	ERROR = 37

















