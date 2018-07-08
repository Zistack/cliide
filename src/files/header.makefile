modname-moddepends =
modname-CFLAGS =
modname-LFLAGS =

modname-path = $(srcdir)/modname
modname-files = $(shell find $(modname-path) -type f -regex '\.\./\([^./][^/]*/\)*[^./][^/]*\.hpp')
modname-include-files = $(modname-files:$(srcdir)/%=$(incdir)/%)
modname-install-files = $(modname-files:$(srcdir)/%=/usr/include/%)
modname-directories = $(shell find $(modname-path) -type d -regex '\.\./\([^./][^/]*/\)*[^./][^/]*')
modname-format-files = $(modname-files:$(srcdir)/%=$(modname-path)/.build/%.format)
modname-install-moddepends = $(modname-moddepends:%=%-install)

modname : $(incdir)/modname.hpp $(modname-include-files)
	touch modname

.PHONY : modname-clean
modname-clean :
	rm -rf $(modname-include-files)
	rm -rf $(incdir)/modname
	rm -rf $(incdir)/modname.hpp
	rm -rf $(modname-format-files)
	rm -rf $(modname-path)/.build/modname
	rm -rf $(modname-path)/.build/modname.hpp
	rm -rf $(modname-path)/.build/modname.hpp.gch
	rm -rf modname

.PHONY : modname-install
modname-install : /usr/include/modname.hpp $(modname-install-files)

.PHONY : modname-uninstall
modname-uninstall :
	rm -rf /usr/include/modname.hpp
	rm -rf /usr/include/modname

.PHONY : modname-format
modname-format : $(modname-format-files)

$(incdir)/modname.hpp : $(modname-path)/.build/modname.hpp $(modname-path)/.build/modname.hpp.gch
	cp $(<) $(@)

$(incdir)/modname/%.hpp : $(modname-path)/%.hpp $(modname-path)/.build/modname.hpp.gch
	mkdir -p $(dir $(@))
	cp $(<) $(@)

$(modname-path)/.build/modname.hpp.gch : $(modname-path)/.build/modname.hpp $(modname-moddepends)
	$(CPP) -I $(srcdir) $(CFLAGS) $(modname-CFLAGS) -c -o $(@) $(<)

$(modname-path)/.build/modname.hpp : $(modname-format-files) $(modname-directories)
	./gen-hdr.sh $(srcdir) modname | clang-format > $(@)

$(modname-path)/.build/%.format : $(srcdir)/%
	./format.sh $(<)
	mkdir -p $(dir $(@))
	touch $(@)

/usr/include/%.hpp : $(incdir)/%.hpp $(modname-install-moddepends)
	mkdir -p $(dir $(@))
	cp $(<) $(@)
