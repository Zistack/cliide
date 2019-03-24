module_name-include-flags ::= -I $(project_name-src-dir) $(module_name-inc-dir-flags)

module_name-top-file ::= $(module_name-path)/.build/module_name.hpp
module_name-build-file ::= $(module_name-path)/.build/module_name.hpp.gch

module_name-include-file ::= $(project_name-inc-dir)/module_name.hpp
module_name-include-path ::= $(project_name-inc-dir)/module_name
module_name-include-files ::= \
	$(module_name-header-files:$(module_name-path)/%=$(module_name-include-path)/%)
module_name-include-directories ::= \
	$(module_name-directories:$(module_name-path)/%=$(module_name-include-path)/%)

module_name-target ::= $(module_name-include-files) $(module_name-include-file)

module_name-install-file ::= $(project_name-header-install-dir)/module_name.hpp
module_name-install-path ::= $(project_name-header-install-dir)/module_name
module_name-install-files ::= \
	$(module_name-header-files:$(module_name-path)/%=$(module_name-install-path)/%)
module_name-install-directories ::= \
	$(module_name-directories:$(module_name-path)/%=$(module_name-install-path)/%)

module_name-install-target ::= $(module_name-install-files) $(module_name-install-file)

.PHONY : module_name
module_name : $(module_name-target)

.PHONY : module_name-clean
module_name-clean :
	rm -rf $(module_name-include-file)
	rm -rf $(module_name-include-files)
	rm -rf $(module_name-include-directories)
	rm -rf $(module_name-build-file)
	rm -rf $(module_name-top-file)

.PHONY : module_name-install
module_name-install : $(module_name-install-target)

.PHONY : module_name-uninstall
module_name-uninstall :
	rm -rf $(module_name-install-file)
	rm -rf $(module_name-install-files)
	rm -rf $(module_name-install-directories)

$(module_name-top-file) : $(module_name-header-files) $(module_name-directories)
	cliide header-include-file $(module_name-path) > $(@)

$(module_name-build-file) : $(module_name-top-file) $(module_name-header-files) $(module_name-dependency-targets)
	$(project_name-CPP) $(module_name-include-flags) $(project_name-CFLAGS) $(module_name-CFLAGS) -c -o $(@) $(<)

$(module_name-include-path)/%.hpp : $(module_name-path)/%.hpp $(module_name-build-file)
	mkdir -p $(dir $(@))
	cp $(<) $(@)

$(module_name-include-file) : $(module_name-top-file) $(module_name-build-file)
	cp $(<) $(@)

$(module_name-install-path)/%.hpp : $(module_name-include-path)/%.hpp $(module_name-dependency-install-targets)
	mkdir -p $(dir $(@))
	cp $(<) $(@)

$(module_name-install-file) : $(module_name-include-file)
	cp $(<) $(@)
