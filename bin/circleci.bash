#!/usr/bin/env bash

# This file contains scripts that are run by CircleCi.
# Check circle.yml to see how they are being used.

GAE=$HOME/google_appengine/
GSUTIL=$HOME/gsutil/

# GAE SDK.
API_CHECK=https://appengine.google.com/api/updatecheck
SDK_VERSION=$(curl -s $API_CHECK | awk -F '\"' '/release/ {print $2}')
# Remove dots.
SDK_VERSION_B=${SDK_VERSION//./}

SDK_URL=https://storage.googleapis.com/appengine-sdks/
SDK_URL_A="${SDK_URL}featured/google_appengine_${SDK_VERSION}.zip"
SDK_URL_B="${SDK_URL}deprecated/$SDK_VERSION_B/google_appengine_${SDK_VERSION}.zip"

# Dependencies pre.
function dep_pre {
    npm install
    pip install flake8
}

# Dependencies post.
function dep_post {
    # Front-end components
    npm run bower install
    npm run gulp compile
}

function gae_deps {
    # GAE
    if [ ! -d "$GAE" ]; then
      echo ">>> Downloading App Engine SDK..."
      curl -fo $HOME/gae.zip $SDK_URL_A || curl -fo $HOME/gae.zip $SDK_URL_B || exit 1
      unzip -q -d $HOME $HOME/gae.zip
    fi

    # Google Cloud Storage
    if [ ! -d "$GSUTIL" ]; then
      echo ">>> Downloading gsutil..."
      curl -fo $HOME/gsutil.zip https://storage.googleapis.com/pub/gsutil.zip || exit 1
      unzip -q -d $HOME $HOME/gsutil.zip
    fi
    # Replacing the oauth token like this because there is
    # no other easy way.
    sed "s@\$GS_OAUTH_TOKEN@$GS_OAUTH_TOKEN@" bin/.circleci_boto > $HOME/.boto
    echo ">>> Downloading configs.py"
    $GSUTIL/gsutil cp gs://humanlink-private/configs.py .

    # pip dependencies
    echo '>>> Installing pip libraries'
    pip install -t lib/pip -r requirements.txt
}

# Deployment.
function deploy {
    gae_deps
    app_id=$1
    $GAE/appcfg.py \
        -v --application=$app_id \
        --oauth2_refresh_token=$GAE_OAUTH_TOKEN \
        update .
    ST=$?
    rm -f configs.py
    # Fail build if deployment failed.
    if [ $ST -eq 0 ]; then
      echo ">>> Deployed to $app_id"
    else
      echo ">>> Deployment failed. app-id: $app_id"
      exit $ST
    fi
}

# Link checks.
# Consider using: https://pypi.python.org/pypi/git-lint
function lints {
    echo ">>> Running flake8."
    FILES=$(git diff --name-only --diff-filter=ACM HEAD^ HEAD | grep -e '\.py$')
    if [ -n "$FILES" ]; then
      flake8 --exit-zero $FILES
    fi
}

function tests {
  lints
}

function usage {
    echo ">>> Unknown option."
    exit 1
}

# Launcher.
if [ -z "$1" ]; then
  usage
else
  case $1 in
    'dep_pre') dep_pre ;;
    'dep_post') dep_post ;;
    'deploy') deploy $2 ;;
    'tests') tests ;;

    *) usage ;;
  esac
fi

