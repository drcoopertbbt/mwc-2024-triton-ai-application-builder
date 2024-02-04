import numpy as np
import tritonclient.http as httpclient

try:
    triton_client = httpclient.InferenceServerClient(url="triton-http-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com", verbose=True)
except Exception as e:
    print("channel creation failed: " + str(e))

model_name = "simple"

# Adjust the data for the input tensors to comply with the batch size limit
input0_data = np.arange(start=0, stop=8, dtype=np.int32)  # Adjusted shape [8]
input1_data = np.ones(shape=(8,), dtype=np.int32)  # Adjusted shape [8]

inputs = []
inputs.append(httpclient.InferInput('INPUT0', [8], "INT32"))  # Adjusted shape [8]
inputs.append(httpclient.InferInput('INPUT1', [8], "INT32"))  # Adjusted shape [8]

# Initialize the data
inputs[0].set_data_from_numpy(input0_data)
inputs[1].set_data_from_numpy(input1_data)

outputs = []
outputs.append(httpclient.InferRequestedOutput('OUTPUT0'))
outputs.append(httpclient.InferRequestedOutput('OUTPUT1'))

# Run inference with the adjusted batch size
results = triton_client.infer(model_name=model_name,
                inputs=inputs,
                outputs=outputs)

# Get the output arrays from the results
output0_data = results.as_numpy('OUTPUT0')
output1_data = results.as_numpy('OUTPUT1')

print('input0_data: ', input0_data)
print('input1_data: ', input1_data)
print('output0_data: ', output0_data)
print('output1_data: ', output1_data)
