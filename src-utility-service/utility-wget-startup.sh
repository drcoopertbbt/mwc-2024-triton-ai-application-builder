#!/bin/bash

# utility-wget-startup.sh

# Define where to save the downloaded file
DOWNLOAD_PATH="/app/model_repository_zip_files/simple.zip"

# Ensure the directory exists to avoid download issues
mkdir -p "/app/model_repository_zip_files"

# Check if the directory exists and report status
if [ -d "/app/model_repository_zip_files" ]; then
  echo "/app/model_repository_zip_files exists and is accessible."
else
  echo "/app/model_repository_zip_files does not exist or is not accessible."
  # If the directory can't be accessed or created, exit to avoid further errors
  exit 1
fi

# Download the file
if wget -O "${DOWNLOAD_PATH}" "https://github.com/drcoopertbbt/mwc-2024-ngc-models-download-test/raw/main/simple.zip"; then
  echo "Download completed successfully."
  # Unzip the file into the model_repository directory
  unzip "${DOWNLOAD_PATH}" -d /app/model_repository
else
  echo "Download failed."
  exit 1
fi

# Start the application
exec gunicorn -b 0.0.0.0:8080 app:app
