import enum

class ASTName(enum.Enum):
	DECL = 0
	INT = 1
	INTP = 2
	FLOAT = 3
	FLOATP = 4

	ID = 5
	VARS = 6 
	ARRAY = 7
	VALUE = 8
	NUM = 9

	ASSIGN = 10
	PLUS = 11
	MINUS = 12
	MULTI = 13
	DIV = 14