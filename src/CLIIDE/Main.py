from argparse import ArgumentParser

from CLIIDE.Commands import *

def main ():

	parser = ArgumentParser (
		description = "CLIIDE, the Command Line Interface Interactive "
			"Development Environment for C++.  Generates build system and "
			"project structure for you.  Maintains a mapping between "
			"directories and namespaces, saving you the maintenance of "
			"hundreds of lines of tedious boilerplate."
	)

	subparsers = parser . add_subparsers (required=True, dest = 'command')

	# Project commands

	registerCreateProject (subparsers)
	registerCreateHeaderLibrary (subparsers)
	registerCreateBinary (subparsers)
	registerCreateNamespace (subparsers)
	registerCreateStruct (subparsers)
	registerCreateTypedef (subparsers)
	registerCreateStaticValue (subparsers)
	registerCreateMemberFunction (subparsers)
	registerCreateBareFunction (subparsers)
	registerCreateConstant (subparsers)

	# Script commands

	registerPrintHeaderIncludeFile (subparsers)
	registerPrintBinaryIncludeFile (subparsers)

	# Debug commands

	registerPrintProjectMakefile (subparsers)
	registerPrintProjectMakefileIncludes (subparsers)
	registerPrintHeaderMakefile (subparsers)
	registerPrintBinaryMakefile (subparsers)

	args = parser . parse_args ()
	args . function (args)
