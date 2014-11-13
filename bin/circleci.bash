#!/usr/bin/env bash

# This file contains scripts that are run by CircleCi.
# Check circle.yml to see how they are being used.

# Dependencies pre.
function dep_pre {
    # GAE
    curl -o $HOME/gae.zip https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.15.zip
    unzip -q -d $HOME $HOME/gae.zip

    npm install -g bower
    npm install -g gulp
}

# Dependencies post.
function dep_post {
    # Front-end components
    bower install
    gulp compile
}

# Deployment.
function deploy {
    app_id=$1
    $HOME/google_appengine/appcfg.py \
        -v --application=$app_id \
        --oauth2_refresh_token=$GAE_OAUTH_TOKEN \
        update .
    echo "Deployed to $app_id"
}

function tests {
    echo "No tests at the moment."
}

function usage {
    echo "Unknown option."
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

