SHELL=/bin/sh

srcdir = ../src
bindir = ../bin

files = $(patsubst %,$(srcdir)/%,$(shell ls -1 $(srcdir)))

.DEFAULT_TARGET : all
all : $(bindir)/cliide

$(bindir)/cliide : $(files)
	cd $(srcdir) && ../build/compile.sh cliide > $(@)
	chmod +x $(@)

.PHONY : clean
clean :
	rm -f $(bindir)/cliide

.PHONY : install
install : /usr/bin/cliide

/usr/bin/cliide : $(bindir)/cliide
	cp $(<) $(@)

.PHONY : uninstall
uninstall :
	rm -f /usr/bin/cliide
