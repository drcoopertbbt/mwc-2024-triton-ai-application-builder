FROM nvcr.io/nvidia/tritonserver:23.05-py3-sdk

# Set work directory
WORKDIR /app

# Copy your application
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Adjust permissions to allow for an arbitrary user to run the app and access the necessary directories
RUN chmod -R 777 /app && \
    mkdir -p /.vscode-server && \
    chmod -R 777 /.vscode-server

# Use the init script to adjust permissions and create directories as needed
COPY init-vscode-server.sh /usr/local/bin/init-vscode-server.sh
RUN chmod +x /usr/local/bin/init-vscode-server.sh

# Ensure the container runs as an arbitrary user comfortably
USER 1000740000

ENTRYPOINT ["/usr/local/bin/init-vscode-server.sh"]
CMD ["tail", "-f", "/dev/null"]