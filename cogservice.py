import os
import sys
import requests

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from config import COMPUTER_VISION_ENDPOINT, COMPUTER_VISION_SUBSCRIPTION_KEY

subscription_key = COMPUTER_VISION_SUBSCRIPTION_KEY

endpoint = COMPUTER_VISION_ENDPOINT

analyze_url = endpoint + "vision/v3.0/analyze"


image_path = 'IMG_0389.JPG'
# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()


analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()
