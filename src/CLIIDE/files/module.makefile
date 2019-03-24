# User-configurable options

module_name-CFLAGS ::=
module_name-LFLAGS ::=

# Boilerplate that shouldn't be touched

module_name-path ::= $(project_name-src-dir)/module_name

module_name-header-files-and-directories ::= \
	$(patsubst \
		./%,$\
		$(module_name-path)/%,$\
		$(shell \
			cd $(module_name-path); \
			find -type f -regex '\(/[^./][^/]*\)*\.hpp' -or \
				-type d -regex '\(/[^./][^/]*\)*' \
		)$\
	)

module_name-header-files ::= $(filter %.hpp, $(module_name-header-files-and-directories))
module_name-directories ::= $(filter-out %.hpp, $(module_name-header-files-and-directories))

module_name-dependency-candidates ::= \
	$(shell sed -ne 's~\#include *<\(.*\)\.hpp>.*~\1~p' $(module_name-path)/include.hpp)

module_name-dependencies ::= $(filter \
	$(project_name-export-targets),$\
	$(module_name-dependency-candidates)$\
)

module_name-dependency-targets ::= $(foreach \
	module_name-dependency,$\
	$(module_name-dependencies),$\
	$($(module_name-dependency)-target)$\
)

module_name-dependency-install-targets ::= $(foreach \
	module_name-dependency,$\
	$(module_name-dependencies),$\
	$($(module_name-dependency)-install-target)$\
)

module_name-inc-dirs ::= $(project_name-inc-dir) $(project_name-reference-inc-dirs)
module_name-inc-dir-flags ::= $(module_name-inc-dirs:%=-I %)
