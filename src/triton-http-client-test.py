import numpy as np
import tritonclient.http as httpclient

try:
    # Update the URL to use the route exposed by OpenShift
    triton_client = httpclient.InferenceServerClient(url="http://triton-http-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com", verbose=True)
except Exception as e:
    print("channel creation failed: " + str(e))

model_name = "simple"

# Create the data for the two input tensors. Initialize the first
# to unique integers and the second to all ones.
input0_data = np.arange(start=0, stop=16, dtype=np.int32)
input1_data = np.ones(shape=(16,), dtype=np.int32)

inputs = []
# Use `httpclient` for creating InferInput objects
inputs.append(httpclient.InferInput('INPUT0', [16], "INT32"))
inputs.append(httpclient.InferInput('INPUT1', [16], "INT32"))

# Initialize the data
inputs[0].set_data_from_numpy(input0_data)
inputs[1].set_data_from_numpy(input1_data)

outputs = []
# Use `httpclient` for creating InferRequestedOutput objects
outputs.append(httpclient.InferRequestedOutput('OUTPUT0'))
outputs.append(httpclient.InferRequestedOutput('OUTPUT1'))

# Run inference
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
