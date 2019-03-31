from collections import defaultdict, deque
from pathlib import Path, PurePath

from CLIIDE.Printer import Printer
from CLIIDE.ProgressMap import ProgressMap
from CLIIDE.Stage import Stage

class Module:

	def __init__(this, path):
		this . children = dict ()
		this . typedec = ''
		this . static_values = set ()
		this . typedef = ''
		this . declarations = set ()
		this . definitions = set ()

		this . dependencies = defaultdict (ProgressMap)

		for child in path.iterdir ():

			if (child . name . startswith ('.')):
				continue;

			if (child . is_dir ()):

				child_module = Module (child)

				if (not child_module . isEmpty ()):

					this . children [child . name] = child_module

			elif (child . is_file ()):

				if (child . name == 'struct.dec.hpp'):

					this . typedec = child . name

				elif (child . name . endswith ('.value.hpp')):

					this . static_values . add (child . name)

				elif (
					child . name == 'struct.def.hpp' or
					child . name == 'type.def.hpp'
				):

					if (this . typedef):

						# Do a bad thing.
						pass

					this . typedef = child . name

				elif (child . name . endswith ('.dec.hpp')):

					this . declarations . add (child . name)

				elif (child . name . endswith ('.def.hpp')):

					this . definitions . add (child . name)

				elif (child . name == 'deps'):

					with child . open () as depfile:

						for line in depfile:

							if line == '':
								continue

							stage, _, dependencies = line . partition (':')

							stage = stage . strip ()

							this . dependencies [Stage [stage]] = \
								ProgressMap (dependencies)

						#for

					#with

				# if

			# if

		# for

	# __init__

	def isEmpty (this):

		return not (
			this . children or
			this . typedec or
			this . static_values or
			this . typedef or
			this . declarations or
			this . definitions
		)

	def firstNonemptyStage (this):

		if (this . children):
			return Stage ['children']

		if (this . typedec):
			return Stage ['typedec']

		if (this . static_values):
			return Stage ['static_values']

		if (this . typedef):
			return Stage ['typedef']

		if (this . declarations):
			return Stage ['declarations']

		if (this . definitions):
			return Stage ['definitions']

		return Stage ['done']

	def printStage (this, stage, module_path, output_stream):

		Module . stage_table [stage] (this, module_path, output_stream)

	def printStages (this, module_path, output_stream):

		this . printChildren (module_path, output_stream)
		this . printTypeDec (module_path, output_stream)
		this . printStaticValues (module_path, output_stream)
		this . printTypeDef (module_path, output_stream)
		this . printDeclarations (module_path, output_stream)
		this . printDefinitions (module_path, output_stream)

	def printNamespace (this, module_name, module_path, output_stream):

		output_stream . write ('namespace ')
		output_stream . write (module_name)
		output_stream . write ('\n{\n')

		this . printStages (module_path, output_stream)

		output_stream . write ('}\n')

	def printChildren (this, module_path, output_stream):

		progress_map = ProgressMap ()

		children = deque (
			Printer (module_path . joinpath (module_name), module_name, module)
				for module_name, module in this . children . items ()
		)

		while (children):

			next_child = children . popleft ()

			if (next_child . canMakeProgress (progress_map)):

				next_child . printNamespace (progress_map, output_stream)

			if (next_child . next_stage != Stage ['done']):

				children . append (next_child)

		# while

	# printChildren

	def printTypeDec (this, module_path, output_stream):

		if (this . typedec):

			printInclude (module_path, this . typedec, output_stream)

	def printStaticValues (this, module_path, output_stream):

		for static_value in this . static_values:

			printInclude (module_path, static_value, output_stream)

	def printTypeDef (this, module_path, output_stream):

		if (this . typedef):

			printInclude (module_path, this . typedef, output_stream)

	def printDeclarations (this, module_path, output_stream):

		for decaration in this . declarations:

			printInclude (module_path, decaration, output_stream)

	def printDefinitions (this, module_path, output_stream):

		for definition in this . definitions:

			printInclude (module_path, definition, output_stream)

	stage_table = {
		Stage ['children'] : printChildren,
		Stage ['typedec'] : printTypeDec,
		Stage ['static_values'] : printStaticValues,
		Stage ['typedef'] : printTypeDef,
		Stage ['declarations'] : printDeclarations,
		Stage ['definitions'] : printDefinitions
	}

# Module

# Helper functions

def printInclude (module_path, file_name, output_stream):

	output_stream . write ('#include "')
	output_stream . write (module_path . joinpath (file_name) . as_posix ())
	output_stream . write ('"\n')

# Actual functionality

def printHeaderIncludeFile (path, output_stream):

	header_module_name = path . name
	header_module = Module (path)

	output_stream . write ('#pragma once\n')
	output_stream . write ('#include "' + header_module_name + '/include.hpp"\n')

	header_module . printNamespace (
		header_module_name,
		PurePath (header_module_name),
		output_stream
	)

def printBinaryIncludeFile (path, output_stream):

	binary_module = Module (path)

	output_stream . write ('#include "include.hpp"\n')

	binary_module . printStages (PurePath (), output_stream)

	output_stream . write ('#include "main.hpp"\n')
