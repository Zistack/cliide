import codecs
from pkg_resources import resource_filename, resource_stream
from shutil import copy

# Helper functions

def filterResource (resource_name, replacements, output_stream):

	with resource_stream ('CLIIDE', resource_name) as resource:

		for line in codecs.iterdecode (resource, encoding = 'utf-8'):

			for word, replacement in replacements . items ():

				line = line . replace (word, replacement)

			output_stream . write (line)

# Actual functionality

def writeGitIgnore (path):

	copy (
		resource_filename ('CLIIDE', 'files/gitignore'),
		str (path . joinpath ('.gitignore'))
	)

def writeBuildGitIgnore (path):

	copy (
		resource_filename ('CLIIDE', 'files/build.gitignore'),
		str (path . joinpath ('.gitignore'))
	)

def printProjectMakefile (project_name, output_stream):

	filterResource (
		'files/project.makefile',
		{'project_name': project_name},
		output_stream
	)

def writeProjectMakefile (path, project_name):

	with path . joinpath ('Makefile') . open ('w') as makefile:

		printProjectMakefile (project_name, makefile)

def printProjectMakefileIncludes (project_name, output_stream):

	filterResource (
		'files/project.includes',
		{'project_name': project_name},
		output_stream
	)

def writeProjectMakefileIncludes (path, project_name):

	with path . joinpath ('.makefile-includes') . open ('w') as makefile_includes:

		printProjectMakefileIncludes (project_name, makefile_includes)

def printHeaderDefinitions (project_name, module_name, output_stream):

	filterResource (
		'files/module.definitions',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

	filterResource (
		'files/header.definitions',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

def writeHeaderDefinitions (path, project_name, module_name):

	with path . joinpath ('.definitions') . open ('w') as definitions:

		printHeaderDefinitions (project_name, module_name, definitions)

def printHeaderRules (project_name, module_name, output_stream):

	filterResource (
		'files/module.rules',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

	filterResource (
		'files/header.rules',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

def writeHeaderRules (path, project_name, module_name):

	with path . joinpath ('.rules') . open ('w') as rules:

		printHeaderRules (project_name, module_name, rules)

def printBinaryDefinitions (project_name, module_name, output_stream):

	filterResource (
		'files/module.definitions',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

	filterResource (
		'files/binary.definitions',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

def writeBinaryDefinitions (path, project_name, module_name):

	with path . joinpath ('.definitions') . open ('w') as definitions:

		printBinaryDefinitions (project_name, module_name, definitions)

def printBinaryRules (project_name, module_name, output_stream):

	filterResource (
		'files/module.rules',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

	filterResource (
		'files/binary.rules',
		{'project_name': project_name, 'module_name': module_name},
		output_stream
	)

def writeBinaryRules (path, project_name, module_name):

	with path . joinpath ('.rules') . open ('w') as rules:

		printBinaryRules (project_name, module_name, rules)

def writeMain (path):

	copy (
		resource_filename ('CLIIDE', 'files/main.hpp'),
		str (path . joinpath ('main.hpp'))
	)

def writeStructDeclaration (path):

	copy (
		resource_filename ('CLIIDE', 'files/struct.decl.hpp'),
		str (path . joinpath ('struct.decl.hpp'))
	)

def writeStructDefinition (path):

	copy (
		resource_filename ('CLIIDE', 'files/struct.def.hpp'),
		str (path . joinpath ('struct.def.hpp'))
	)

def writeTypeDefinition (path):

	copy (
		resource_filename ('CLIIDE', 'files/type.def.hpp'),
		str (path . joinpath ('type.def.hpp'))
	)

def printStaticValue (name, output_stream):

	filterResource (
		'files/VALUE.value.hpp',
		{'VALUE': name},
		output_stream
	)

def writeStaticValue (name):

	with open (name + '.value.hpp', 'w') as static_value:

		printStaticValue (name, static_value)

def printMemberFunctionDefinition (name, output_stream):

	filterResource (
		'files/member.def.hpp',
		{'member': name},
		output_stream
	)

def writeMemberFunctionDefinition (name):

	with open (name + '.def.hpp', 'w') as member_def:

		printMemberFunctionDefinition (name, member_def)

def printBareFunctionDeclaration (name, output_stream):

	filterResource (
		'files/function.dec.hpp',
		{'function': name},
		output_stream
	)

def writeBareFunctionDeclaration (name):

	with open (name + '.dec.hpp', 'w') as function_dec:

		printBareFunctionDeclaration (name, function_dec)

def printBareFunctionDefinition (name, output_stream):

	filterResource (
		'files/function.def.hpp',
		{'function': name},
		output_stream
	)

def writeBareFunctionDefinition (name):

	with open (name + '.def.hpp', 'w') as function_def:

		printBareFunctionDefinition (name, function_def)

def printConstantDefinition (name, output_stream):

	filterResource (
		'files/CONSTANT.def.hpp',
		{'CONSTANT': name},
		output_stream
	)

def writeConstantDefinition (name):

	with open (name + '.def.hpp', 'w') as constant_def:

		printConstantDefinition (name, constant_def)
