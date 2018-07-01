function get-function-declarations
{
	local file="${1}"

	get-function-declarations-state-machine < "${file}" | clang-format
}

function get-function-declarations-state-machine
{
	local state="waiting"

	while IFS='' read -r line
	do
		if [ "${state}" = "waiting" ] && [ -n "${line}" ]
		then
			echo "${line}"
			state="in declaration"
		elif [ "${state}" = "in declaration" ]
		then
			if grep -q '^{$' <<< "${line}"
			then
				echo ';'
				state="in definition"
			else
				echo "${line}"
			fi
		elif [ "${state}" = "in definition" ] && grep -q '^}$' <<< "${line}"
		then
			state="waiting"
		fi
	done
}

function get-struct-declaration
{
	local file="${1}"

	get-struct-declaration-state-machine < "${file}" | clang-format
}

function get-struct-declaration-state-machine
{
	local state="waiting"

	while IFS='' read -r line
	do
		if [ "${state}" = "waiting" ] && [ -n "${line}" ]
		then
			state="in declaration"
		fi

		if [ "${state}" = "in declaration" ]
		then
			if grep -q '^struct T' <<< "${line}"
			then
				echo 'struct T;'
				break
			else
				echo "${line}"
			fi
		fi
	done
}
