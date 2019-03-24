from CLIIDE.Stage import Stage

class ProgressMap:

	def __init__ (this, string = ''):

		this . map = dict ()

		if (string):

			for pair in string . split (','):

				module_name, _, stage_name = pair . partition ('.')

				module_name = module_name . strip ()
				stage_name = stage_name . strip ()

				this . map [module_name] = Stage [stage_name]

	def update (this, module_name, stage):

		this . map [module_name] = stage

	def satisfies (this, dependencies):

		for module, stage in dependencies . map . items ():

			if (module not in this . map):

				return False

			if (this . map [module] < stage):

				return False

		return True
