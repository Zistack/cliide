from collections import defaultdict

from CLIIDE . ProgressMap import ProgressMap
from CLIIDE . Stage import Stage

import CLIIDE . Util as Util
import CLIIDE . Class as Class

def getClass (input_stream, classPredicate):

	string = ''

	while (Util . test (input_stream, classPredicate)):

		string += input_stream . get ()

	if (not string):

		raise SyntaxError (
			"Unexpected EOF",
			input_stream . position ()
		)

	return string

def getIdentifier (input_stream):

	identifier = Util . expect (input_stream, Class . isAlphaNum)

	while (Util . test (input_stream, Class . isIdentifier)):

		identifier += input_stream . get ()

	return identifier

def getStage (input_stream):

	stage = getClass (input_stream, Class . isAlpha)

	if (stage not in Stage . __members__):

		raise SyntaxError (
			"'" + stage + "' is not a valid stage identifier",
			input_stream . position ()
		)

	return Stage [stage]

def getStageDependencies (input_stream):

	stage_dependencies = ProgressMap ()

	while (True):

		module_name = getIdentifier (input_stream)
		Util . skipWhitespace (input_stream)

		Util . expect (input_stream, '.')
		Util . skipWhitespace (input_stream)

		module_stage = getStage (input_stream)
		Util . skipWhitespace (input_stream)

		stage_dependencies . update (module_name, module_stage)

		if (Util . test (input_stream, ',')):

			input_stream . get ()
			Util . skipWhitespace (input_stream)
			continue;

		else:

			return stage_dependencies

def getModuleDependencies (input_stream):

	module_dependencies = defaultdict (ProgressMap)

	while (True):

		stage = getStage (input_stream)
		Util . skipWhitespace (input_stream)

		Util . expect (input_stream, ':')
		Util . skipWhitespace (input_stream)

		module_dependencies [stage] = getStageDependencies (input_stream)

		if (input_stream . atEOF ()):

			return module_dependencies

		else:

			continue
