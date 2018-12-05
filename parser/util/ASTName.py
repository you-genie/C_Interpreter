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

	EQ = 15
	LESS = 16
	LESSEQ = 17
	GREATER = 18
	GREATEREQ = 19

	IF = 20
	ELSE = 21
	BODY = 22
	
	FOR = 23

	FUNCDEFINE = 24
	FUNCCALL = 25
	RET = 26
	
	INCR = 27
	DECR = 28

	PARAM = 29
	PARAMS = 30

	ARGS = 31
	PRINT = 32
	STR = 33
