function print-project-makefile
{
	cat <<'EOF'
#COMPILE (files/project.makefile)
EOF
}

function print-header-makefile
{
	local modname="${1}"

	sed -e 's~modname~'"${modname}"'~g' <<'EOF'
#COMPILE (files/header.makefile)
EOF
}

function print-binary-makefile
{
	local modname="${1}"

	sed -e 's~modname~'"${modname}"'~g' <<'EOF'
#COMPILE (files/binary.makefile)
EOF
}
