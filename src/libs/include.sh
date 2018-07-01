#INCLUDE (libs/predicates.sh)
#INCLUDE (libs/parse.sh)

function declare-struct
{
	local path="${1}"

	if is-struct
	then
		get-struct-declaration 'struct.hpp'
	fi
}

function include-typedef-type
{
	local path="${1}"

	if is-typedef
	then
		echo '#include "'"${path}"'/type.hpp"'
	fi
}

function include-struct-definition
{
	local path="${1}"

	if is-struct
	then
		echo '#include "'"${path}"'/struct.hpp"'
	fi
}

function include-constant-definitions
{
	local path="${1}"

	for constant in $(list-constants)
	do
		echo '#include "'"${path}"'/'"${constant}"'"'
	done
}

function declare-functions
{
	local path="${1}"

	if ! is-struct
	then
		for function in $(list-functions)
		do
			get-function-declarations "${function}"
		done
	fi
}

function include-function-definitions
{
	local path="${1}"

	for function in $(list-functions)
	do
		echo '#include "'"${path}"'/'"${function}"'"'
	done
}
