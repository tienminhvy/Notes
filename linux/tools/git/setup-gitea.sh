#!/bin/bash

REPO_DIR=$PWD;
TOOLS_DIR=$(realpath $0 | grep -Eo '(/.+)/')"..";

function setup_user_info() {
	echo "Setting up user information at "$REPO_DIR
	git config user.name vy.tien;
	git config user.email vy.tien@evolus.vn;
}

if $TOOLS_DIR/git/is-git-repo.sh; then 
	setup_user_info;
	echo "Setting up repository successfully!";
fi;

exit 0;
