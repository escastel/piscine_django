#!/bin/bash

if [ $1 ]; then
	curl -s $1 | grep "moved here" | cut -d \" -f 2
else
	echo -e "\033[1;31mError: invalid number of arguments\033[0m"
fi
