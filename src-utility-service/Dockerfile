# Use Python 3.11 image from Red Hat's registry as a builder
FROM registry.redhat.io/ubi8/python-311 as builder

# Set working directory
WORKDIR /app

# Copy source code and scripts from the src-utility-service directory
# Note: Assuming the BuildConfig's contextDir is set to src-utility-service,
# the COPY command needs to adjust to copy from the current build context
COPY ./utility-pod-src ./ 
COPY ./utility-wget-startup.sh ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start script on container launch
CMD ["./utility-wget-startup.sh"]
