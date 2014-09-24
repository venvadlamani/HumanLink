#!/bin/bash

# Symlink this script to pre-commit:
# 1. Go to project root
# 2. cd .git/hooks
# 3. ln -s ../../bin/git_pre_commit.bash pre-commit

echo 'Running pre-commit...'

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.py$')
if [ -n "$FILES" ]; then
  flake8 $FILES
fi

if [ $? -ne 0 ]; then
  echo -e "\n$(tput setaf 1)flake8 reported errors. Please fix them.$(tput sgr 0)"
  echo -e "If these errors are irrelevant, or if you want to \
bypass these (not recommended),
you can commit with: git commit -n ..."
  echo
  exit 1
fi

echo -e "Done running pre-commit.\n"
