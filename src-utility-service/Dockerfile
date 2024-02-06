# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# As the next commands are to be run as root, we don't switch to non-root user yet.

# Copy source code and scripts
COPY . .

# Debugging: List contents of /app
RUN ls -la /app/*

# Update permissions for the current user (root at this stage). 
# This is necessary because when building images without root privileges, 
# you might not be able to change file ownership with chown. 
# However, setting read/write/execute permissions might be sufficient 
# depending on your application's needs.
RUN chmod -R g=u /app

# Now switch to user 1001
USER 1001

# Keep the container running indefinitely to allow `oc rsh` access
CMD ["tail", "-f", "/dev/null"]
