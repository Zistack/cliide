#INCLUDE (libs/struct.sh)
#INCLUDE (libs/function.sh)
#INCLUDE (libs/enum.sh)
#INCLUDE (libs/makefile.sh)

function create-struct
{
	local name="${1}"

	mkdir -p "${name}"

	print-struct-definition > "${name}"/struct.hpp
}

function create-function
{
	local name="${1}"

	print-function "${name}" > "${name}".hpp
}

function create-module
{
	local name="${1}"

	mkdir -p "${name}"
}

function create-typedef
{
	local name="${1}"
	local type="${2}"

	if [ -z "${type}" ]
	then
		type='/* type */'
	fi

	mkdir -p "${name}"

	print-typedef "${type}" > "${name}"/type.hpp
}

function create-constant
{
	local name="${1}"
	local value="${2}"

	if [ -z "${value}" ]
	then
		value='/* value */'
	fi

	print-constant "${name}" "${value}" > "${name}".hpp
}

function create-project
{
	local name="${1}"

	mkdir -p "${name}"/build
	mkdir -p "${name}"/src
	mkdir -p "${name}"/bin
	mkdir -p "${name}"/inc
	mkdir -p "${name}"/doc

	print-project-makefile > "${name}"/build/Makefile

	cat > "${name}"/build/gen-bin.sh <<'EOF'
#COMPILE (scripts/gen-bin.sh)
EOF
	chmod +x "${name}"/build/gen-bin.sh

	cat > "${name}"/build/gen-hdr.sh <<'EOF'
#COMPILE (scripts/gen-hdr.sh)
EOF
	chmod +x "${name}"/build/gen-hdr.sh

	cat > "${name}"/build/format.sh <<'EOF'
#COMPILE (scripts/format.sh)
EOF
	chmod +x "${name}"/build/format.sh

	cat > "${name}"/build/.gitignore <<'EOF'
#COMPILE (files/build.gitignore)
EOF

	cat > "${name}"/.clang-format <<'EOF'
#COMPILE (files/clang-format)
EOF

	cat > "${name}"/inc/.gitignore <<'EOF'
#COMPILE(files/gitignore)
EOF

	cat > "${name}"/bin/.gitignore <<'EOF'
#COMPILE(files/gitignore)
EOF
}

function create-binary
{
	local name="${1}"

	mkdir -p "${name}"/.build
	touch "${name}"/include.hpp
	print-main > "${name}"/main.hpp
	print-binary-makefile "${name}" > "${name}"/.makefile

	cat > "${name}"/.build/.gitignore <<'EOF'
#COMPILE(files/gitignore)
EOF
}

function create-header
{
	local name="${1}"

	mkdir -p "${name}"/.build
	touch "${name}"/include.hpp
	print-header-makefile "${name}" > "${name}"/.makefile

	cat > "${name}"/.build/.gitignore <<'EOF'
#COMPILE(files/gitignore)
EOF
}
