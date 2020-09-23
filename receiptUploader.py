# Jacob Lucke
#
# Adapted from https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-print-text
#

import os
import json
import sys
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

ocr_url = endpoint + "vision/v3.0/ocr"

params = {'language': 'unk', 'detectOrientation': 'true'}

### Image from url
# Set image_url to the URL of an image that you want to analyze.
# image_url = "https://static01.nyt.com/images/2019/04/03/business/03wholefoods2/03wholefoods2-jumbo.jpg"
# headers = {'Ocp-Apim-Subscription-Key': subscription_key}
# data = {'url': image_url}
# response = requests.post(ocr_url, headers=headers, params=params, json=data)
# response.raise_for_status()
###

### Image from local storage
image_path = "image.png"
# Read the image into a byte array
image_data = open(image_path, "rb").read()
# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
# put the byte array into your post request
response = requests.post(ocr_url, headers=headers, params=params, data = image_data)
###

analysis = response.json()

# Extract the word bounding boxes and text.
file = open("Test.json", "w+")
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
            text = word_info["text"]
            file.write(text.encode('utf-8') + ' ')
        file.write('\n')
word_infos

file.close()