#!/bin/bash

#INCLUDE (list)
#INCLUDE (namespace)
#INCLUDE (include)

srcdir="${1}"
module="${2}"

cd "${srcdir}"

echo '#pragma once'

echo ''

echo '#include "'"${module}"'/include.hpp"'

echo ''

namespace-do "${module}" "${module}" "include-struct-type"

echo ''

namespace-do "${module}" "${module}" "include-typedef-type"

echo ''

namespace-do "${module}" "${module}" "include-struct-definition"

echo ''

namespace-do "${module}" "${module}" "include-constant-definitions"

echo ''

namespace-do "${module}" "${module}" "declare-functions"

echo ''

namespace-do "${module}" "${module}" "include-function-definitions"
