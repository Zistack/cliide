from enum import IntEnum, unique

@unique
class Stage (IntEnum):
	children = 1
	static_values = 2
	typedec = 3
	typedef = 4
	declarations = 5
	definitions = 6
	done = 7
