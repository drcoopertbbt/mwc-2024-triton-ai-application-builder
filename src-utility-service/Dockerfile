# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY . .

# Debugging: List contents of /app
RUN ls -la /app/*

# Keep the container running indefinitely to allow `oc rsh` access
CMD ["tail", "-f", "/dev/null"]
