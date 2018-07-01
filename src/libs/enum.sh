function print-typedef
{
	local type="${1}"

	echo 'using T = '"${type}"';'
}

function print-constant
{
	local name="${1}"
	local value="${2}"

	echo 'const T '"${name}"' = '"${value}"';'
}
