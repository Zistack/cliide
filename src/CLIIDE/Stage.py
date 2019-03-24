from enum import IntEnum, unique

@unique
class Stage (IntEnum):
	children = 1
	typedec = 2
	static_values = 3
	typedef = 4
	declarations = 5
	definitions = 6
	done = 7
