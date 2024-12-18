#!/bin/bash

TOOLS_DIR=$(realpath $0 | grep -Eo '(/.+)/')"..";

if ! $TOOLS_DIR/git/is-git-repo.sh; then
	exit 1;
fi

if [ -z "$1" ]; then
	echo "Commit message is required!";
	exit 1;
fi

function add_commit_push() {
	git add .;
	git commit -m "$1";
	git push;
}

add_commit_push "$1";
