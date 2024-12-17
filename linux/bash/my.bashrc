# DISPLAY GIT BRANCH

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

USER_HOST="\e[0;32m[\u@\h \e[36m\W\e[32m]";
WORKING_DIR="\[\e[36m\]\w"
GIT_BRANCH="\[\e[1;31m\]\$(parse_git_branch)\[\e[0m\]"

export PS1="$USER_HOST $WORKING_DIR $GIT_BRANCH\$ "