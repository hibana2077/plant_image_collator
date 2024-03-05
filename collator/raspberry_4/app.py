#sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
#sudo python3 -m pip install --force-reinstall adafruit-blinka --break-system-packages
import board
import neopixel
import time
from psutil import cpu_percent, virtual_memory
from requests import post
from base64 import b64encode
from hashlib import sha256
from os import system
from yaml.loader import SafeLoader
from yaml import load
from time import time,sleep
from PIL import Image
from io import BytesIO
from datetime import datetime
import cv2 as cv

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
    # Use pil take picture
    cap = cv.VideoCapture(0)
    sleep(0.5)  # Wait for 0.5 seconds
    ret, frame = cap.read()
    cv.imwrite(f'test.{encoding}', frame)
    cap.release()
    return True

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

def wavelength_to_rgb(wavelength, gamma=0.8):

    '''This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).
    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

if __name__ == "__main__":
    config = init()
    length = 16
    pixels = neopixel.NeoPixel(board.D18, length, brightness=1, auto_write=False,pixel_order=neopixel.GRB)
    pixels.fill((0, 0, 0))
    pixels.show()
    pixels.fill(wavelength_to_rgb(620))
    pixels.show()
    start_time_photo = time()
    start_time_status = time()
    while True:
        try:
            if time() - start_time_photo > int(config["interval"]):
                print("Take picture!")
                start_time_photo = time()
                pixels.fill((255,255,255))
                pixels.show()
                photo = take_photo(config["encoding"])
                if photo:
                    send_photo(config=config)
                    if config["notify"]:send_discord_webhook(config["notify_webhook"], "Take photo success!")
            # if time() - start_time_status > (int(config["interval"])//10):
            #     start_time_status = time()
            #     send_status(config=config)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            pixels.fill((255, 0, 0))
            pixels.show()
            sleep(0.5)
            pixels.fill((0, 255, 0))
            pixels.show()
            sleep(0.5)
            pixels.fill((0, 0, 255))
            pixels.show()
            sleep(0.5)
            pixels.fill((0, 0, 0))
            pixels.show()
            sleep(0.5)
            break