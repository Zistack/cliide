function is-struct
{
	test -e struct.hpp -a -e type.hpp
}

function is-typedef
{
	test ! -e struct.hpp -a -e type.hpp
}
