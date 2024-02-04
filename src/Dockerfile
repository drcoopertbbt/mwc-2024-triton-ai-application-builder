FROM nvcr.io/nvidia/tritonserver:23.05-py3-sdk

WORKDIR /app

COPY . /app
COPY init-vscode-server.sh /usr/local/bin/init-vscode-server.sh

RUN pip install --no-cache-dir -r requirements.txt && \
    useradd -m vscodeuser && \
    chown -R vscodeuser:vscodeuser /app /.vscode-server && \
    chmod -R 755 /app && \
    chmod +x /usr/local/bin/init-vscode-server.sh

USER vscodeuser

ENTRYPOINT ["/usr/local/bin/init-vscode-server.sh"]
CMD ["tail", "-f", "/dev/null"]
