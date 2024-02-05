# Use the NVIDIA genai-llm-playground image
FROM nvcr.io/nvidia/aiworkflows/genai-llm-playground:latest

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