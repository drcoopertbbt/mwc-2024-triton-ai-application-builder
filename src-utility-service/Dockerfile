# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY ./src-utility-service ./

# Assuming directories are present, skipping the mkdir command
# The chgrp and chmod commands are commented out due to potential permission issues
# RUN chgrp -R 0 model_repository_zip_files model_repository && \
#   chmod -R g=u model_repository_zip_files model_repository

# Install Python dependencies
RUN pip install --no-cache-dir -r utility-pod-src/requirements.txt

# Start script on container launch
CMD ["./utility-wget-startup.sh"]
