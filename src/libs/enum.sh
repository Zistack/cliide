function print-typedef
{
	local type="${1}"

	echo 'typedef '"${type}"' T;'
}

function print-constant
{
	local name="${1}"
	local value="${2}"

	echo 'const T '"${name}"' = '"${value}"';'
}
