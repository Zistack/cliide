SHELL=/bin/sh

srcdir = ../src
bindir = ../bin
insdir = $(shell cat insdir)

files = $(shell ls $(srcdir))

.DEFAULT_TARGET : all
all : $(files:%=$(bindir)/%)

$(bindir)/% : $(srcdir)/%
	cp $< $@

.PHONY : clean
clean :
	rm -f $(files:%=$(bindir)/%)

.PHONY : install
install : $(files:%=$(insdir)/%)

$(insdir)/% : $(bindir)/%
	cp $< $@

.PHONY : uninstall
uninstall : 
	rm -f $(files:%=$(insdir)/%)
