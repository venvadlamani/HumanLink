#!/bin/bash

# Symlink this script to pre-commit:
# 1. Go to project root
# 2. cd .git/hooks
# 3. ln -s ../../bin/git_pre_commit.bash pre-commit

echo 'Running pre-commit...'

FLAKE_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.py$')
FLAKE_ST=$?
if [ -n "$FILES" ]; then
  flake8 $FILES
fi

JSFILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.js$')
JSHINT_ST=$?
if [ -n "$JSFILES" ]; then
    jshint $JSFILES
fi

if [[ $FLAKE_ST -ne 0 || $JSHINT_ST -ne 0 ]]; then
  echo -e "\n$(tput setaf 1)flake8 or jshint reported errors. Please fix them.$(tput sgr 0)"
  echo -e "If these errors are irrelevant, or if you want to \
bypass these (not recommended),
you can commit with: git commit -n ..."
  echo
  exit 1
fi

echo -e "Done running pre-commit.\n"
