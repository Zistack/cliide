modname-moddepends =
modname-CFLAGS =
modname-LFLAGS =

modname-path = $(srcdir)/modname
modname-files = $(shell find $(modname-path) -type f -regex '\.\./\([^./][^/]*/\)*[^./][^/]*\.hpp')
modname-directories = $(shell find $(modname-path) -type d -regex '\.\./\([^./][^/]*/\)*[^./][^/]*')
modname-format-files = $(modname-files:$(srcdir)/%=$(modname-path)/.build/%.format)
modname-install-moddepends = $(modname-moddepends:%=%-install)

modname : $(bindir)/modname
	touch modname

.PHONY : modname-clean
modname-clean :
	rm -rf $(bindir)/modname
	rm -rf $(modname-path)/.build/main.cpp
	rm -rf $(modname-path)/.build/main.o
	rm -rf $(modname-format-files)
	rm -rf $(modname-path)/.build/modname
	rm -rf modname

.PHONY : modname-install
modname-install : /usr/bin/modname

.PHONY : modname-uninstall
modname-uninstall :
	rm -rf /usr/bin/modname

.PHONY : modname-format
modname-format : $(modname-format-files)

$(bindir)/modname : $(modname-path)/.build/main.o
	$(CPP) $(LFLAGS) $(modname-LFLAGS) -o $(@) $(<)

$(modname-path)/.build/main.o : $(modname-path)/.build/main.cpp $(modname-moddepends)
	$(CPP) -I $(modname-path) $(CFLAGS) $(modname-CFLAGS) -c -o $(@) $(<)

$(modname-path)/.build/main.cpp : $(modname-format-files) $(modname-directories)
	./gen-bin.sh $(modname-path) | clang-format > $(@)

$(modname-path)/.build/%.format : $(srcdir)/%
	./format.sh $(<)
	mkdir -p $(dir $(@))
	touch $(@)

/usr/bin/modname : $(bindir)/modname $(modname-install-moddepends)
	cp $(<) $(@)
}
