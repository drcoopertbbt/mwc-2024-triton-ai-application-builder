#!/bin/bash

# Create the VS Code Server directory with the correct permissions
mkdir -p /.vscode-server/bin
chown -R vscodeuser:vscodeuser /.vscode-server

# Execute the command passed to the script
exec "$@"