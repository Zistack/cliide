from pathlib import Path
from sys import stdout

from CLIIDE import Project, Resource, Module

def registerCreateProject (subparsers):

	parser = subparsers . add_parser (
		'project',
		aliases = ['p'],
		description = 'Creates a new project.'
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the project.  Must also be a valid directory name.'
	)
	parser . set_defaults (function = createProject)

def createProject (args):

	Project . createProject (args . name)

def registerCreateHeaderLibrary (subparsers):

	parser = subparsers . add_parser (
		'header',
		aliases = ['h'],
		description = "Creates a new header library source module.  This "
			"command must be executed in the project's src directory."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the header library.  Must also be a valid '
			'directory name.'
	)
	parser . set_defaults (function = createHeaderLibrary)

def createHeaderLibrary (args):

	Project . createHeaderLibrary (args . name)

def registerCreateBinary (subparsers):

	parser = subparsers . add_parser (
		'binary',
		aliases = ['b'],
		description = "Created a new binary source module.  This command must "
			"be executed in the project's src directoriy."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the binary.  Must also be a valid directory name.'
	)
	parser . set_defaults (function = createBinary)

def createBinary (args):

	Project . createBinary (args . name)

def registerCreateNamespace (subparsers):

	parser = subparsers . add_parser (
		'namespace',
		aliases = ['n'],
		description = "Creates a new namespace.  This command should be "
			"executed within the project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the namespace.'
	)
	parser . set_defaults (function = createNamespace)

def createNamespace (args):

	Project . createNamespace (args . name)

def registerCreateStruct (subparsers):

	parser = subparsers . add_parser (
		'struct',
		aliases = ['s'],
		description = "Creates a new struct source module.  This command "
			"should be executed within the project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the struct.'
	)
	parser . set_defaults (function = createStruct)

def createStruct (args):

	Project . createStruct (args . name)

def registerCreateTypedef (subparsers):

	parser = subparsers . add_parser (
		'typedef',
		aliases = ['t'],
		description = "Creates a new typedef source module.  This command "
			"should be executed within the project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the typedef.'
	)
	parser . set_defaults (function = createTypedef)

def createTypedef (args):

	Project . createTypedef (args . name)

def registerCreateStaticValue (subparsers):

	parser = subparsers . add_parser (
		'value',
		aliases = ['v'],
		description = "Creates a new static value file.  This command should "
			"be executed within the project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the static value.'
	)
	parser . set_defaults (function = createStaticValue)

def createStaticValue (args):

	Project . createStaticValue (args . name)

def registerCreateMemberFunction (subparsers):

	parser = subparsers . add_parser (
		'member',
		aliases = ['m'],
		description = "Creates a new member function definition file.  This "
			"command should be executed within the project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the member function.'
	)
	parser . set_defaults (function = createMemberFunction)

def createMemberFunction (args):

	Project . createMemberFunction (args . name)

def registerCreateBareFunction (subparsers):

	parser = subparsers . add_parser (
		'function',
		aliases = ['f'],
		description = "Creates a function declaration file and function "
			"definition file.  This command should be executed within the "
			"project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the function.'
	)
	parser . set_defaults (function = createBareFunction)

def createBareFunction (args):

	Project . createBareFunction (args . name)

def registerCreateConstant (subparsers):

	parser = subparsers . add_parser (
		'constant',
		aliases = ['c'],
		description = "Creates a constant definition file.  This command "
			"should be executed within the project's source tree."
	)
	parser . add_argument (
		'name',
		type = str,
		help = 'The name of the constant.'
	)
	parser . set_defaults (function = createConstant)

def createConstant (args):

	Project . createConstant (args . name)

def registerPrintProjectMakefile (subparsers):

	parser = subparsers . add_parser (
		'project-makefile',
		description = "Prints a project Makefile to standard output."
	)
	parser . add_argument (
		'project_name',
		type = str,
		help = 'The name of the project.'
	)
	parser . set_defaults (function = printProjectMakefile)

def printProjectMakefile (args):

	Resource . printProjectMakefile (args . project_name, stdout)

def registerPrintProjectMakefileIncludes (subparsers):

	parser = subparsers . add_parser (
		'project-makefile-includes',
		description = "Prints a project .makefile-includes to standard output."
	)
	parser . add_argument (
		'project_name',
		type = str,
		help = 'The name of the project.'
	)
	parser . set_defaults (function = printProjectMakefileIncludes)

def printProjectMakefileIncludes (args):

	Resource . printProjectMakefileIncludes (args . project_name, stdout)

def registerPrintHeaderMakefile (subparsers):

	parser = subparsers . add_parser (
		'header-makefile',
		description = "Prints a header library .makefile to standard output."
	)
	parser . add_argument (
		'project_name',
		type = str,
		help = 'The name of the project.'
	)
	parser . add_argument (
		'module_name',
		type = str,
		help = 'The name of the header library.'
	)
	parser . set_defaults (function = printHeaderMakefile)

def printHeaderMakefile (args):

	Resource . printHeaderMakefile (
		args . project_name,
		args . module_name,
		stdout
	)

def registerPrintBinaryMakefile (subparsers):

	parser = subparsers . add_parser (
		'binary-makefile',
		description = "Prints a binary .makefile to standard output."
	)
	parser . add_argument (
		'project_name',
		type = str,
		help = 'The name of the project.'
	)
	parser . add_argument (
		'module_name',
		type = str,
		help = 'The name of the binary.'
	)
	parser . set_defaults (function = printBinaryMakefile)

def printBinaryMakefile (args):

	Resource . printBinaryMakefile (
		args . project_name,
		args . module_name,
		stdout
	)

def registerPrintHeaderIncludeFile (subparsers):

	parser = subparsers . add_parser (
		'header-include-file',
		description = "Prints a header library's module file to standard "
			"output."
	)
	parser . add_argument (
		'path',
		type = str,
		help = 'Path to the header library source module.'
	)
	parser . set_defaults (function = printHeaderIncludeFile)

def printHeaderIncludeFile (args):

	Module.printHeaderIncludeFile (Path (args . path), stdout)

def registerPrintBinaryIncludeFile (subparsers):

	parser = subparsers . add_parser (
		'binary-include-file',
		description = "Prints a binary's module file to standard output."
	)
	parser . add_argument (
		'path',
		type = str,
		help = 'Path to the binary source module.'
	)
	parser . set_defaults (function = printBinaryIncludeFile)

def printBinaryIncludeFile (args):

	Module.printBinaryIncludeFile (Path (args . path), stdout)
