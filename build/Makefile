SHELL=/bin/sh

srcdir = ../src
bindir = ../bin

files = $(patsubst %,$(srcdir)/%,$(shell find $(srcdir) -type f))

.DEFAULT_TARGET : all
all : $(bindir)/cliide $(bindir)/debug

$(bindir)/cliide : $(files)
	cd $(srcdir) && ../build/compile.sh cliide > $(@)
	chmod +x $(@)

$(bindir)/debug : $(files)
	cd $(srcdir) && ../build/compile.sh debug > $(@)

.PHONY : clean
clean :
	rm -f $(bindir)/cliide
	rm -f $(bindir)/debug

.PHONY : install
install : /usr/bin/cliide

/usr/bin/cliide : $(bindir)/cliide
	cp $(<) $(@)

.PHONY : uninstall
uninstall :
	rm -f /usr/bin/cliide
