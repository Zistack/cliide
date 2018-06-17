function get-declarations
{
	local file="${1}"

	get-declarations-state-machine < "${file}" | clang-format
}

function get-declarations-state-machine
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
