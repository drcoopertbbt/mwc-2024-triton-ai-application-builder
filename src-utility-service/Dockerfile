# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY . .

# Debugging: List contents of /app
RUN ls -la /app/*

# It's good practice to not run containers as root if not necessary
# Assume we want to run as UID 1001, but check with your OpenShift cluster for the correct non-root UID
# Additionally, set the appropriate permissions for the non-root user
RUN chown -R 1001:0 /app && \
    chmod -R g=u /app

# Use an unprivileged user to run the application
USER 1001

# Keep the container running indefinitely to allow `oc rsh` access
CMD ["tail", "-f", "/dev/null"]
