'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-11-28 11:30:10
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-11-30 10:56:33
FilePath: /plant_image_collator/src/main/app.py
Description: This is a main file for plant_image_collator
'''
import requests
import base64
import os
import yaml
from time import sleep
from PIL import Image
from io import BytesIO
from datetime import datetime

URL = "http://localhost:5000/"

def init():
    # load config
    config = dict()
    with open("config.yaml", "r") as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    # check config
    if config["verbose"]:
        print(config)
    return config

def take_photo(encoding:str = "jpg"):
    # Use raspberry pi libcamera-jpeg tools to take photo
    status = os.system(f"raspistill -o ./test.{encoding} -e {encoding}")
    if status == 0:
        print("take photo success")
        return True
    else:
        print("take photo fail")
        return False

def send_photo(encoding:str = "jpg"):
    data = {
        "photo": None,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with Image.open(f"./test.{encoding}") as image:
        # Create a buffer to hold the bytes
        buffer = BytesIO()
        
        # Save the image as JPEG to the buffer
        image.save(buffer, format=image.format)
        
        # Retrieve the bytes from the buffer
        image_bytes = buffer.getvalue()
        
        # Convert the bytes to base64
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Save to data
        data["photo"] = image_base64
    # Send request
    response = requests.post(URL, json=data)
    print(response.text)
    if response.status_code == 200:
        print("success")
        return True
    else:
        print("fail")
        return False
        
def send_discord_webhook(discord_webhook_url:str, content:str):
    data = {
        "username": "Plant Image Collator Notification",
        "content": content,
        "avatar_url": "../img/logo.png"
    }
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code == 200:
        print("success")
        return True
    else:
        print("fail")
        return False

if __name__ == "__main__":
    config = init()
    while True:
        try:
            print("try")
            photo = take_photo()
            if photo:
                send_photo()
                sleep(config["interval"])
            break
        except Exception as e:
            print(e)
            break