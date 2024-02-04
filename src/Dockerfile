FROM nvcr.io/nvidia/tritonserver:23.05-py3-sdk

WORKDIR /app

# Copy your application and the init script
COPY . /app
COPY init-vscode-server.sh /usr/local/bin/init-vscode-server.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and adjust permissions
RUN useradd -m vscodeuser && \
    chown -R vscodeuser:vscodeuser /app && \
    chmod -R 755 /app && \
    chmod +x /usr/local/bin/init-vscode-server.sh

# Switch to non-root user
USER vscodeuser

# Use the init script as the entry point to create /.vscode-server with correct permissions
ENTRYPOINT ["/usr/local/bin/init-vscode-server.sh"]
CMD ["tail", "-f", "/dev/null"]
