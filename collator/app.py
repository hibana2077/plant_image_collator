'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-11-28 11:30:10
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-12-02 22:52:15
FilePath: /plant_image_collator/src/main/app.py
Description: This is a main file for plant_image_collator
'''
from psutil import cpu_percent, virtual_memory
from requests import post
from base64 import b64encode
from hashlib import sha256
from os import system
from yaml.loader import SafeLoader
from yaml import load
from time import time
from PIL import Image
from io import BytesIO
from datetime import datetime

def init():
    # load config
    config = dict()
    with open("config.yaml", "r") as f:
        config = load(f, Loader=SafeLoader)
    # check config
    if config["verbose"]:
        print(config)
    return config

def take_photo(encoding:str = "jpg"):
    # Use raspberry pi libcamera-jpeg tools to take photo
    status = system(f"libcamera-jpeg -o test.{encoding} -e {encoding} -v 0")
    if status == 0:
        print("take photo success")
        return True
    else:
        print("take photo fail")
        return False

def send_status(config: dict = None):
    data = {
        "cpu": cpu_percent(),
        "memory": virtual_memory().percent,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "node_name": config["node_name"]
    }
    # Send request
    response = post(config['URL']+"status", json=data)
    print(response.text)
    if response.status_code == 200:
        print("success")
        return True
    else:
        print("fail")
        return False

def send_photo(config: dict = None):
    data = {
        "photo": None,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "plant_name": config["plant_name"],
        "node_name": config["node_name"]
    }
    with Image.open(f"./test.{config['encoding']}") as image:
        with BytesIO() as buffer:
            image.save(buffer, format=image.format)
            image_base64 = b64encode(buffer.getvalue()).decode("utf-8")
            data["photo"] = image_base64
    # Send request
    response = post(config['URL']+"photo", json=data)
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
        "avatar_url": "https://github.com/hibana2077/plant_image_collator/blob/main/img/logo.png"
    }
    response = post(discord_webhook_url, json=data)
    if response.status_code == 200:
        print("success")
        return True
    else:
        print("fail")
        return False

def do_sth_make_cpu_busy2():
    # sha256
    for i in range(10000):
        for j in range(1000):
            sha256(str(i*j).encode())

if __name__ == "__main__":
    config = init()
    start_time_photo_phot = time()
    start_time_status = time()
    while True:
        try:
            if time() - start_time_photo > int(config["interval"]):
                start_time_photo = time()
                photo = take_photo(config["encoding"])
                if photo:
                    send_photo(config=config)
                    if config["notify"]:send_discord_webhook(config["notify_webhook"], "Take photo success!")
            if config["send_status"] and time() - start_time_status > (int(config["interval"])//10):
                start_time_status = time()
                send_status(config=config)
        except Exception as e:
            print(e)