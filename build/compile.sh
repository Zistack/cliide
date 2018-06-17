#!/bin/bash

infile="${1}"

srcdir='../src'
bindir='../bin'

included_files="${infile}"

function process-file
{
	local file="${1}"

	while IFS='' read -r line
	do
		if grep -q '^#INCLUDE *(.*)$' <<< "${line}"
		then
			included_file="$(sed -e 's~^#INCLUDE *(\(.*\))$~\1~' <<< "${line}")"

			if ! grep -q "${included_file}" <<< "${included_files}"
			then
				included_files="${included_files}${included_file}\n"
				process-file "${included_file}"
			fi
		elif grep -q '^#COMPILE *(.*)$' <<< "${line}"
		then
			included_file="$(sed -e 's~^#COMPILE *(\(.*\))$~\1~' <<< "${line}")"

			"${0}" "${included_file}"
		else
			echo "${line}"
		fi
	done < "${file}"
}

process-file "${infile}"
