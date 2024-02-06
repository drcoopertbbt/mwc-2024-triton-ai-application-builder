# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY . .

# Create the directory and set permissions
RUN mkdir -p /app/model_repository_zip_files && chmod 777 /app/model_repository_zip_files

# Debugging: List contents of /app
RUN ls -la /app/*

# Start script on container launch
CMD ["./utility-wget-startup.sh"]