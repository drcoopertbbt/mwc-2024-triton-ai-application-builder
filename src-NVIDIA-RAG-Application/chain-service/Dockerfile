# Use the NVIDIA chain-server image
FROM nvcr.io/nvidia/aiworkflows/chain-server:latest

# Set work directory
WORKDIR /app

# Copy your application
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Adjust permissions to allow for an arbitrary user
RUN chmod -R 777 /app

# Define the entrypoint and command
ENTRYPOINT ["python"]
CMD ["app.py"]