#!/bin/bash

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
	exit 0;
fi;

echo "Not a git repository!";
exit 1;
