import openai
from utils import download_image
import os

imgpath = "F:/Pro Documents/The Leet AI/APIs/OpenAI/images/"
prompt = "character design a girl with diamond hair, mist volumetric lightning, black and teal, hyper realistic, 4k, super realistic"
imgname = (prompt if len(prompt) < 256 else prompt[:256]) +".png"

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

download_image(image_url, os.path.join(imgpath, imgname))
print(image_url)
#
