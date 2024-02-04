FROM nvcr.io/nvidia/tritonserver:23.05-py3-sdk

# Set work directory
WORKDIR /app

# Copy your application
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN useradd -m vscodeuser && \
    chown -R vscodeuser:vscodeuser /app && \
    chmod -R 755 /app && \
    # Attempt to create the VS Code server directory and adjust permissions
    mkdir -p /.vscode-server && \
    chown -R vscodeuser:vscodeuser /.vscode-server

# Switch to non-root user
USER vscodeuser

# Instead of CMD ["/bin/bash"], use a command to keep the container running
# Use tail to follow an empty file indefinitely
CMD ["tail", "-f", "/dev/null"]
