#!/bin/bash

REPO_DIR="~/piwrgb"

cd $REPO_DIR

# Check for updates
git fetch
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})

if [ $LOCAL != $REMOTE ]; then
    echo "Changes detected. Updating repository."

    # Pull the latest changes
    git pull

else
    echo "No changes detected."
fi
