import requests
import os

apikey = os.environ.get('OPENAI_API_KEY')


def download_image(
    url, 
    file_name, 
    headers ={
        "User-Agent": "Chrome/51.0.2704.103",
    }):
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the image
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)

