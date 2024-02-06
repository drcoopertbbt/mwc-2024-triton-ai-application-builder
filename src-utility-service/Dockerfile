FROM registry.redhat.io/ubi8 AS builder

WORKDIR /app

COPY . .

# Set permissions so that the group 'root' has the same permissions as the owner
# This step should be done before switching to a non-root user
USER root
RUN chmod -R g=u /app/model_repository /app/model_repository_zip_files

# Switch back to a non-root user
USER 1001
