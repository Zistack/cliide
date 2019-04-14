class EOF (Exception):
	pass

class InputStream:

	def __init__ (this, file):

		this . file = file

		this . filename = file . name
		this . line = 0
		this . column = 0

		this . text = ''

		this . eof = False

	def get (this):

		this . ensureBuffer ()

		r = this . text [this . column]
		this . column += 1
		return r

	def peek (this):

		this . ensureBuffer ()

		return this . text [this . column]

	def ensureBuffer (this):

		if (this . eof):

			raise EOF ()

		if (this . column >= len (this . text)):

			this . text = this . file . readline ()
			this . line += 1
			this . column = 0

		if (this . text == ''):

			this . eof = True
			raise EOF ()

	def atEOF (this):

		if (this . eof):

			return True

		else:

			try:

				this . peek ()

			except IO . EOF:

				return True

			return False

	def position (this):

		return this . filename, this . line, this . column, this . text
