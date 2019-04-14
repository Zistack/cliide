import CLIIDE . Class as Class
import CLIIDE . IO as IO

def expect (input_stream, expected):

	if (isinstance (expected, str)):

		for e in expected:

			try:

				c = input_stream . get ()

			except IO . EOF:

				raise SyntaxError (
					"Unexpected EOF, expected '" + expected + "'",
					input_stream . position ()
				)

			if (c != e):

				raise SyntaxError (
					"Unexpected character '" +
						c +
						"', expected '" +
						expected +
						"'",
					input_stream . position ()
				)

		return expected

	elif (callable (expected)):

		try:

			c = input_stream . get ()

		except IO . EOF:

			raise SyntaxError (
				"Unexpected EOF",
				input_stream . position ()
			)

		if (not expected (c)):

			raise SyntaxError (
				"Unexpected character '" + c + "'",
				input_stream . position ()
			)

		return c

	else:

		raise TypeError (
			"Argument 'expected' should be a string or a predicate"
		)

def test (input_stream, query):

	try:

		c = input_stream . peek ()

	except IO . EOF:

		return False

	if (isinstance (query, str)):

		return c == query

	elif (callable (query)):

		return query (c)

	else:

		raise TypeError ("Argument 'query' should be a string or a predicate")

def skipWhitespace (input_stream):

	while (test (input_stream, Class . isWhitespace)):

		input_stream . get ()
