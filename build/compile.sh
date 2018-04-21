#!/bin/bash

srcdir='../src'
bindir='../bin'

while IFS='' read -r line || test -n "${line}"
do
    
    if grep -q 'COMPILE' <<< "${line}"
    then
	
	cat "${srcdir}/$(sed -e 's~.*COMPILE[ ]*(\(.*\)).*~\1~' <<< "${line}")"
	
    else
	
	echo "${line}"
	
    fi
    
done < "${srcdir}"'/cliide' > "${bindir}"'/cliide'
