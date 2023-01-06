import requests
import json
import base64
import os

# DALL-E API endpoint
API_ENDPOINT = "https://api.openai.com/v1/images/generations"

# Your OpenAI API key
API_KEY = "your api key"

# The prompt to use as input to DALL-E
prompt = "your API prompt string"

# Make the API request
response = requests.post(
    API_ENDPOINT,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    },
    json={
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512",
        "response_format": "url"
    }
)

# Check the status code of the response
if response.status_code != 200:
    raise Exception("Failed to generate image")

# Get the image URL from the response
image_url = response.json()["data"][0]["url"]

# Download the image
response = requests.get(image_url)
image_data = response.content

#prompt for file name, added for overwrite problems
file=input("file name")

# Save the image to a file in PNG format
with open(file, "wb") as f:
    f.write(image_data)
