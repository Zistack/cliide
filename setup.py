#!/bin/python

from setuptools import setup, find_packages

setup (
	name = 'CLIIDE',
	author = 'Zistack',
	description =
		'CLIIDE, the Commmand Line Interface Interactive Development '
		'Environment for C++.',
	license = 'GPLv3',

	package_dir = {
		'': 'src'
	},
	packages = find_packages (where = 'src'),
	package_data = {
		'cliide/files': ['*']
	},
	entry_points = {
		'console_scripts': [
			'cliide = CLIIDE.Main:main'
		]
	}
)
