FROM nvcr.io/nvidia/tritonserver:23.05-py3-sdk

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/triton-http-client-test.py"]