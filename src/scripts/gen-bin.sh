#!/bin/bash

#INCLUDE (libs/list.sh)
#INCLUDE (libs/namespace.sh)
#INCLUDE (libs/include.sh)

modname_path="${1}"

cd "${modname_path}"

echo '#include "include.hpp"'

echo ''

declare-struct '.'
echo ''
for module in $(list-modules)
do
	namespace-do "${module}" "${module}" "declare-struct"
done

echo ''

include-typedef-type '.'
echo ''
for module in $(list-modules)
do
	namespace-do "${module}" "${module}" "include-typedef-type"
done

echo ''

include-struct-definition '.'
echo ''
for module in $(list-modules)
do
	namespace-do "${module}" "${module}" "include-struct-definition"
done

echo ''

include-constant-definitions '.'
echo ''
for module in $(list-modules)
do
	namespace-do "${module}" "${module}" "include-constant-definitions"
done

echo ''

declare-functions ''
echo ''
for module in $(list-modules)
do
	namespace-do "${module}" "${module}" "declare-functions"
done

echo ''

include-function-definitions '.'
echo ''
for module in $(list-modules)
do
	namespace-do "${module}" "${module}" "include-function-defnitions"
done

echo ''

echo '#include "main.hpp"'
