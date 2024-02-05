# Use the NVIDIA genai-model-server image
FROM nvcr.io/nvidia/aiworkflows/genai-model-server:latest

# Set the working directory
WORKDIR /models

# Copy the model files
COPY . /models

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Adjust permissions to allow for an arbitrary user to run the app
RUN chmod -R 777 /models

# Start the model server
CMD ["tritonserver", "--model-repository=/models"]