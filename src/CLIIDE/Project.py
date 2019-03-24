from pathlib import Path

from CLIIDE.Resource import *

# Helper functions

def createDir (path, name):

	dir_path = path . joinpath (name)
	dir_path . mkdir (mode = 0o755, exist_ok = True)
	return dir_path

def createOutputDir (path, name):

	dir_path = createDir (path, name)
	writeGitIgnore (dir_path)

def getProjectNameFromSrcDir ():

	src_path = Path ('.') . resolve ()
	if (src_path . name != 'src'):
		# Do a bad thing
		pass

	project_path = src_path . parent
	return project_path . name

# Actual functinality

def createProject (name):

	project_path = createDir (Path (), name)

	build_path = createDir (project_path, 'build')
	writeBuildGitIgnore (build_path)
	writeProjectMakefile (build_path, name)
	writeProjectMakefileIncludes (build_path, name)

	createDir (project_path, 'src')
	createDir (project_path, 'doc')

	createOutputDir (project_path, 'bin')
	createOutputDir (project_path, 'inc')
	createOutputDir (project_path, 'ref')

def createHeaderLibrary (name):

	module_path = createDir (Path (), name)

	module_path . joinpath ('include.hpp') . touch ()
	writeHeaderMakefile (module_path, getProjectNameFromSrcDir (), name)

	build_path = createDir (module_path, '.build')
	writeGitIgnore (build_path)

def createBinary (name):

	module_path = createDir (Path (), name)

	module_path . joinpath ('include.hpp') . touch ()
	writeMain (module_path)
	writeBinaryMakefile (module_path, getProjectNameFromSrcDir (), name)

	build_path = createDir (module_path, '.build')
	writeGitIgnore (build_path)

def createNamespace (name):

	createDir (Path (), name)

def createStruct (name):

	module_path = createDir (Path (), name)
	writeStructDeclaration (module_path)
	writeStructDefinition (module_path)

def createTypedef (name):

	module_path = createDir (Path (), name)
	writeTypeDefinition (module_path)

def createStaticValue (name):

	writeStaticValue (name)

def createMemberFunction (name):

	writeMemberFunctionDefinition (name)

def createBareFunction (name):

	writeBareFunctionDeclaration (name)
	writeBareFunctionDefinition (name)

def createConstant (name):

	writeConstantDefinition (name)
