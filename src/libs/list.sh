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
	local source_files="$(list-source-files)"

	if [ -n "${source_files}" ]
	then
		grep -L '^const T' ${source_files}
	fi
}

function list-modules
{
	find . -mindepth 1 -maxdepth 1 -type d -regex '^\./[^.].*' | sed -e 's~\./~~'
}

function list-constants
{
	local source_files="$(list-source-files)"

	if [ -n "${source_files}" ]
	then
		grep -l '^const T' ${source_files}
	fi
}
