import os
import sys
import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from config import COMPUTER_VISION_ENDPOINT, COMPUTER_VISION_SUBSCRIPTION_KEY

# Add your Computer Vision subscription key and endpoint to your environment variables.
subscription_key = COMPUTER_VISION_SUBSCRIPTION_KEY

endpoint = COMPUTER_VISION_ENDPOINT

analyze_url = endpoint + "vision/v3.0/analyze"

# Set image_path to the local path of an image that you want to analyze.
# Sample images are here, if needed:
# https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images
#image_path = "../ch-3/data/train/cat.1.jpg"
image_path = 'IMG_0389.JPG'
# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()