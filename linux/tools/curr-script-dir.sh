#!/bin/bash

DIR="$( dirname -- $1; )";   # Get the directory name
DIR="$( realpath -e -- "$DIR"; )";    # Resolve its full path if need be

echo $DIR
