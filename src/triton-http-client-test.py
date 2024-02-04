import numpy as np
import tritonclient.http as httpclient
import time  # Importing time module for sleep

try:
    print("Attempting to connect to Triton Inference Server...")
    triton_client = httpclient.InferenceServerClient(url="triton-http-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com", verbose=True)
    print("Successfully connected to Triton Inference Server.")
except Exception as e:
    print("Channel creation failed: ", str(e))
    exit()

model_name = "simple"
print(f"Preparing inference request for model '{model_name}'...")

# Creating a batch of data with shape [8, 16] for each input tensor
input0_data = np.random.randint(low=0, high=100, size=(8, 16), dtype=np.int32)
input1_data = np.random.randint(low=0, high=100, size=(8, 16), dtype=np.int32)

print("Input0 Data Shape:", input0_data.shape)
print("Input1 Data Shape:", input1_data.shape)

# Creating the input data for the request
inputs = []
inputs.append(httpclient.InferInput('INPUT0', [8, 16], "INT32"))
inputs.append(httpclient.InferInput('INPUT1', [8, 16], "INT32"))

# Initialize the data
inputs[0].set_data_from_numpy(input0_data)
inputs[1].set_data_from_numpy(input1_data)

print("Inputs prepared, setting up outputs...")

outputs = []
outputs.append(httpclient.InferRequestedOutput('OUTPUT0'))
outputs.append(httpclient.InferRequestedOutput('OUTPUT1'))

print("Outputs set up, sending inference request...")

# Run inference
try:
    results = triton_client.infer(model_name=model_name,
                                  inputs=inputs,
                                  outputs=outputs)
    print("Inference request completed successfully.")
    
    # Extracting and printing the results
    output0_data = results.as_numpy('OUTPUT0')
    output1_data = results.as_numpy('OUTPUT1')
    
    print('Output0 Data Shape:', output0_data.shape)
    print('Output1 Data Shape:', output1_data.shape)
    print('Output0 Data: ', output0_data)
    print('Output1 Data: ', output1_data)
except Exception as e:
    print("Inference failed: ", str(e))

# Keep the script running indefinitely to prevent the container from exiting
print("Script execution completed. Entering infinite sleep to prevent pod from exiting.")
while True:
    time.sleep(2073600)  # Sleep for a long time (24 days) before the loop checks again
