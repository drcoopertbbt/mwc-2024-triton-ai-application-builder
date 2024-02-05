# Use the NVIDIA genai-notebook-server image
FROM nvcr.io/nvidia/aiworkflows/genai-notebook-server:latest

# Set the working directory
WORKDIR /notebook

# Copy the notebook files
COPY . /notebook

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Adjust permissions to allow for an arbitrary user to run the app
RUN chmod -R 777 /notebook

# Start the notebook server
CMD ["start-notebook.sh"] 