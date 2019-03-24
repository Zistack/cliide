from CLIIDE.Stage import Stage

class Printer:

	def __init__ (this, module_path, module_name, module):

		this . module_path = module_path

		this . module_name = module_name

		this . module = module

		this . next_stage = module . firstNonemptyStage ()

	def canMakeProgress (this, progress_map):

		if (this . next_stage == Stage ['done']):

			return False

		return progress_map . satisfies (this . module . dependencies [this . next_stage])

	def printNamespace (this, progress_map, output_stream):

		output_stream . write ('namespace ')
		output_stream . write (this . module_name)
		output_stream . write ('\n{\n')

		this . printStages (progress_map, output_stream);

		output_stream . write ('}\n')

	def printStages (this, progress_map, output_stream):

		while (this . canMakeProgress (progress_map)):

			this . module . printStage (this . next_stage, this . module_path, output_stream)

			progress_map . update (this . module_name, this . next_stage)

			this . next_stage += 1
