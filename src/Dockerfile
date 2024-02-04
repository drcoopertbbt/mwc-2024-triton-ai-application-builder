FROM nvcr.io/nvidia/tritonserver:23.05-py3-sdk

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Create an empty file to tail
RUN touch /dev/null

# Use tail to follow the empty file indefinitely
CMD ["tail", "-f", "/dev/null"]
