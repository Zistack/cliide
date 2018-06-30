SHELL = /bin/sh

incdir = ../inc
srcdir = ../src
bindir = ../bin

WARNINGS = -Wchar-subscripts -Wcomment -Wformat=2 -Winit-self -Wimplicit \
-Wignored-qualifiers -Wmain -Wmissing-braces -Wmissing-include-dirs \
-Wparentheses -Wsequence-point -Wreturn-type -Wswitch -Wtrigraphs -Wunused \
-Wuninitialized -Wstrict-aliasing -Warray-bounds -Wfloat-equal -Wundef \
-Wno-endif-labels -Wpointer-arith -Wtype-limits -Wconversion -Wenum-compare \
-Wsign-conversion -Waddress -Wmissing-field-initializers \
-Wvolatile-register-var -Wno-write-strings -Wsign-promo

CPP = clang++
CFLAGS = $(WARNINGS) -Werror -pipe -I $(incdir)
LFLAGS =

modmkfiles = $(shell find $(srcdir) -type f -name .makefile)
moddirs = $(modmkfiles:$(srcdir)/%/.makefile=%)
modules = $(subst /,-,$(moddirs))
modcleans = $(modules:%=%-clean)
modinstalls = $(modules:%=%-install)
moduninstalls = $(modules:%=%-uninstall)
modformats = $(modules:%=%-format)

include $(modmkfiles)

.DEFAULT_GOAL := all

.PHONY : all
all : $(modules)

.PHONY : clean
clean : $(modcleans)

.PHONE : install
install : $(modinstalls)

.PHONY : uninstall
uninstall : $(moduninstalls)

.PHONY : format
format : $(modformats)
