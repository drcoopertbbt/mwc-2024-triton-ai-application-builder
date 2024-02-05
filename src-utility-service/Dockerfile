FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY ./utility-pod-src ./
COPY ./utility-wget-startup.sh utility-wget-startup.sh

# Prepare model storage directories and ensure they are writable by any user
RUN mkdir -p /app/model_repository_zip_files /app/model_repository && \
    chmod -R g+rwX /app/model_repository_zip_files /app/model_repository && \
    chgrp -R 0 /app/model_repository_zip_files /app/model_repository

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify non-root user
USER 1001

# Start script on container launch
CMD ["./utility-wget-startup.sh"]
