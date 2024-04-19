import json
import boto3

prompt = """
Write general concepts and their basics for Machine learning in the style of 50CENT the rapper.
"""
bedrock = boto3.client(service_name='bedrock-runtime')

payload={
    "prompt": "[INST]"+ prompt +"[/INST]",
    "temperature": 0.1,
    "top_p": 0.9,
}
body=json.dumps(payload) # the sent request
model_id="mistral.mixtral-8x7b-instruct-v0:1"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
response_text=response_body # the key of the response 
print(response_text)