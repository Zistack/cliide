#INCLUDE (libs/list.sh)

function process-module
{
	local module="${1}"

	for dependency in $(cat "${module}"/dependencies 2>/dev/null)
	do
		conditionally-process-module "${dependency}"
	done

	local new_path="${path}"'/'"${module}"

	namespace-do "${module}" "${new_path}" "${command}"
}

function conditionally-process-module
{
	local module="${1}"

	if ! grep -qx "${module}" <<< "${processed_modules}"
	then
		processed_modules="${processed_modules}${module}"$'\n'

		process-module "${module}"
	fi
}

function process-modules
{
	local processed_modules=""

	for new_module in $(list-modules)
	do
		conditionally-process-module "${new_module}"
	done
}

function namespace-do
{
	local module="${1}"
	local path="${2}"
	local command="${3}"

	echo 'namespace '"${module}"
	echo '{'

	cd "${module}"

	(process-modules; "${command}" "${path}") | sed -e 's~^~	~'

	cd ..

	echo '}'
}
