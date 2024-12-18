#!/bin/bash

TOOLS_DIR=$(realpath $0 | grep -Eo '(/.+)/')"..";

if [ -z $1 ]; then
	echo "FATAL: File name as the first parameter is required!"
	exit 1;
fi;

cat $TOOLS_DIR"/markdown/sample-docs.md" > $1;
echo "Created $1 file successfully!"
