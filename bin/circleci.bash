#!/usr/bin/env bash

# This file contains scripts that are run by CircleCi.
# Check circle.yml to see how they are being used.

GAE=$HOME/google_appengine/
GSUTIL=$HOME/gsutil/

# Dependencies pre.
function dep_pre {
    echo ">>> bower and gulp install"
    npm install -g bower
    npm install -g gulp
}

# Dependencies post.
function dep_post {
    # Front-end components
    bower install
    gulp compile

}

function gae_deps {
    # GAE
    if [ ! -d "$GAE" ]; then
      echo ">>> Downloading App Engine SDK..."
      curl -o $HOME/gae.zip https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.15.zip
      unzip -q -d $HOME $HOME/gae.zip
    fi

    # Google Cloud Storage
    if [ ! -d "$GSUTIL" ]; then
      echo ">>> Downloading gsutil..."
      curl -o $HOME/gsutil.zip https://storage.googleapis.com/pub/gsutil.zip
      unzip -q -d $HOME $HOME/gsutil.zip
    fi
    # Replacing the oauth token like this because there is
    # no other easy way.
    sed "s@\$GS_OAUTH_TOKEN@$GS_OAUTH_TOKEN@" bin/.circleci_boto > $HOME/.boto
    echo ">>> Downloading configs.py"
    $GSUTIL/gsutil cp gs://humanlink-private/configs.py .

    # pip dependencies
    echo '>>> Creating a new virtualenv...'
    virtualenv-2.7 venv
    echo '>>> Installing venv libraries'
    ./venv/bin/pip install requests
    ./venv/bin/pip install mandrill
}

# Deployment.
function deploy {
    gae_deps
    app_id=$1
    $GAE/appcfg.py \
        -v --application=$app_id \
        --oauth2_refresh_token=$GAE_OAUTH_TOKEN \
        update .
    echo ">>> Deployed to $app_id"
    rm -f configs.py
}

function tests {
    echo ">>> No tests at the moment."
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

