special='
type.hpp
struct.hpp
main.hpp
include.hpp
'

function list-source-files
{
	find . -mindepth 1 -maxdepth 1 -type f -regex '\./[^.].*\.hpp' |
		sed -e 's~\./~~' |
		grep -vxF "${special}"
}

function list-functions
{
	grep -L '^const T' $(list-source-files)
}

function list-modules
{
	find . -mindepth 1 -maxdepth 1 -type d -regex '^\./[^.].*' | sed -e 's~\./~~'
}

function list-constants
{
	grep -l '^const T' $(list-source-files)
}
