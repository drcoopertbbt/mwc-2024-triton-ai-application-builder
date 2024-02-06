# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 AS builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY . .

# The previously used chmod command is removed as it is not permitted

# Switch to user 1001 (commonly used non-root user)
# If the base image uses an arbitrary user, this line may not be necessary.
USER 1001

# Debugging: List contents of /app
# This command is now moved below the USER directive
# and will be executed as the non-root user.
RUN ls -la /app/*

# Keep the container running indefinitely to allow `oc rsh` access
CMD ["tail", "-f", "/dev/null"]
