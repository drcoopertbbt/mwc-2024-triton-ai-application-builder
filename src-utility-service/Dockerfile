# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts
COPY . .

# Debugging: List contents of /app
RUN ls -la /app/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start script on container launch
CMD ["./utility-wget-startup.sh"]
