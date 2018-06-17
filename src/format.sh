#!/bin/bash

file="${1}"

if ! clang-format ${file} | diff -q ${file} - > /dev/null
then
	tmpfile=$(mktemp)
	clang-format ${file} > ${tmpfile}
	cat ${tmpfile} > ${file}
	rm ${tmpfile}
fi
