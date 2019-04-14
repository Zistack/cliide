def isAlpha (c):

	return (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')

def isDigit (c):

	return c >= '0' and c <= '9'

def isAlphaNum (c):

	return isAlpha (c) or isDigit (c)

def isWhitespace (c):

	return c == ' ' or c == '\t' or c == '\n' or c == '\r'

def isIdentifier (c):

	return isAlphaNum (c) or c == '_'
