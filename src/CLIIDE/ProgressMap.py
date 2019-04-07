from CLIIDE . Stage import Stage
import sys

class ProgressMap:

	def __init__ (this, string = ''):

		this . map = dict ()

		if (string):

			for pair in string . split (','):

				module_name, _, stage_name = pair . partition ('.')

				module_name = module_name . strip ()
				stage_name = stage_name . strip ()

				this . map [module_name] = Stage [stage_name]

	def __repr__ (this):

		return this . map . __repr__ ();

	def validate (this, existing_modules, module_path):

		for module_name in this . map . keys ():

			if (module_name not in existing_modules):

				print (
					"Module '" + module_name + "' does not exist",
					file = sys . stderr
				)
				print (
					"Note: '" +
						module_name +
						"' is referenced by " +
						str (module_path . joinpath ('deps')),
					file = sys . stderr
				)

				sys . exit (1);

	def update (this, module_name, stage):

		this . map [module_name] = stage

	def satisfies (this, dependencies):

		for module, stage in dependencies . map . items ():

			if (module not in this . map):

				return False

			if (this . map [module] < stage):

				return False

		return True
