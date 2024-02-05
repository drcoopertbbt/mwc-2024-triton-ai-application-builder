import os
import zipfile
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  # Path to the downloaded zip file
  zip_path = "/downloads/mistral-7b-int4-chat_1.0.zip"

  # Unzip the file
  with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("/downloads")

  # List the contents of the unzipped directory
  contents = os.listdir("/downloads/mistral-7b-int4-chat_1.0")

  # Convert the list of contents to a string
  contents_str = "<br>".join(contents)

  # Return the HTML with the contents of the unzipped directory
  return """
  <!DOCTYPE html>
  <html>
  <head>
    <title>Welcome to My Utility Server</title>
  </head>
  <body>
    <h1>OpenShift AI Model Helper</h1>
    <p>Hosting models</p>
    <h2>Contents of the downloaded file:</h2>
    <p>{}</p>
  </body>
  </html>
  """.format(contents_str)