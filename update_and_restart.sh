#!/bin/bash

REPO_DIR="~/piwrgb"
SERVICE_NAME="piwrgb_service"

cd $REPO_DIR

# Check for updates
git fetch
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})

if [ $LOCAL != $REMOTE ]; then
    echo "Changes detected. Updating repository."

    # Stop the running service
    sudo systemctl stop $SERVICE_NAME

    # Pull the latest changes
    git pull

    # Restart the service
    sudo systemctl start $SERVICE_NAME
else
    echo "No changes detected."
fi
