#!/bin/bash

# Define where to save the downloaded file
DOWNLOAD_PATH="/app/model_repository_zip_files/simple.zip"

# Ensure the script does not attempt operations requiring root privileges
# Download the file
if wget -O "${DOWNLOAD_PATH}" https://github.com/drcoopertbbt/mwc-ngc-simulator/raw/main/model_repository/simple.zip; then
  echo "Download completed successfully."
  # Unzip the file into the model_repository directory
  unzip "${DOWNLOAD_PATH}" -d /app/model_repository
else
  echo "Download failed."
  exit 1
fi

# Start the application
exec gunicorn -b 0.0.0.0:8080 app:app