module_name-include-flags ::= -I $(module_name-path) $(module_name-inc-dir-flags)

module_name-top-file ::= $(module_name-path)/.build/main.cpp

module_name-build-file ::= $(module_name-path)/.build/main.o

module_name-bin-file ::= $(project_name-bin-dir)/module_name

module_name-target ::= $(module_name-bin-file)

module_name-install-file ::= $(project_name-binary-install-dir)/module_name

module_name-install-target ::= $(module_name-install-file)

.PHONY : module_name
module_name : $(module_name-target)

.PHONY : module_name-clean
module_name-clean :
	rm -rf $(module_name-bin-file)
	rm -rf $(module_name-build-file)
	rm -rf $(module_name-top-file)

.PHONY : module_name-install
module_name-install : $(module_name-install-target)

.PHONY : module_name-uninstall
module_name-uninstall :
	rm -rf $(module_name-install-file)

$(module_name-top-file) : $(module_name-header-files) $(module_name-directories)
	cliide binary-include-file $(module_name-path) > $(@)

$(module_name-build-file) : $(module_name-top-file) $(module_name-dependency-targets)
	$(project_name-CPP) $(module_name-include-flags) $(project_name-CFLAGS) $(module_name-CFLAGS) -c -o $(@) $(<)

$(module_name-bin-file) : $(module_name-build-file)
	$(project_name-CPP) $(project_name-LFLAGS) $(module_name-LFLAGS) -o $(@) $(<)

$(module_name-install-file) : $(module_name-bin-file) $(module_name-dependency-install-targets)
	cp $(<) $(@)
