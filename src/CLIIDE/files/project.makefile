# User-configurable options

SHELL ::= /bin/sh

project_name-WARNINGS ::= -Wchar-subscripts -Wcomment -Wformat=2 -Winit-self -Wimplicit \
-Wignored-qualifiers -Wmain -Wmissing-braces -Wmissing-include-dirs \
-Wparentheses -Wsequence-point -Wreturn-type -Wswitch -Wtrigraphs -Wunused \
-Wuninitialized -Wstrict-aliasing -Warray-bounds -Wfloat-equal -Wundef \
-Wno-endif-labels -Wpointer-arith -Wtype-limits -Wconversion -Wenum-compare \
-Wsign-conversion -Waddress -Wmissing-field-initializers \
-Wvolatile-register-var -Wno-write-strings -Wsign-promo

project_name-CPP ::= clang++
project_name-CFLAGS ::= $(project_name-WARNINGS) -Werror -pipe
project_name-LFLAGS ::=

project_name-header-install-dir ::= /usr/local/include
project_name-binary-install-dir ::= /usr/local/bin
project_name-library-install-dir ::= /usr/local/lib

# Boilerplate that should not be touched

ifndef project_name-base-dir
	project_name-base-dir ::= $(realpath ..)
	project_name-previously-included ::=
else
	project_name-target-prefix ::= project_name-
endif

project_name-inc-dir ::= $(project_name-base-dir)/inc
project_name-src-dir ::= $(project_name-base-dir)/src
project_name-bin-dir ::= $(project_name-base-dir)/bin
project_name-ref-dir ::= $(project_name-base-dir)/ref
project_name-build-dir ::= $(project_name-base-dir)/build

include $(project_name-build-dir)/.makefile-includes

project_name-module-cleans = $(project_name-modules:%=%-clean)
project_name-module-installs = $(project_name-modules:%=%-install)
project_name-module-uninstalls = $(project_name-modules:%=%-uninstall)

.DEFAULT_GOAL := all

.PHONY : all
$(project_name-target-prefix)all : $(project_name-modules)

.PHONY : clean
$(project_name-target-prefix)clean : $(project_name-module-cleans)

.PHONE : install
$(project_name-target-prefix)install : $(project_name-module-installs)

.PHONY : uninstall
$(project_name-target-prefix)uninstall : $(project_name-module-uninstalls)
