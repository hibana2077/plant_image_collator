'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-11-28 11:30:10
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-11-28 22:31:23
FilePath: /plant_image_collator/src/main/app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv
import numpy as np
import pandas as pd
import requests
import base64
from datetime import datetime

URL = "http://localhost:5000/"

def init_check():
    print("init check")
    return True

def take_photo(times:int = 10):
    # open camera
    cap = cv.VideoCapture(0)
    cnt = 0
    final_frame = None
    while cnt<times:
        ret, frame = cap.read()
        if cnt == times-1:
            print("take photo")
            final_frame = frame
        cnt += 1
    # close camera
    cap.release()
    cv.destroyAllWindows()
    return final_frame

def send_photo(photo):
    #convert photo to base64
    _, encoded_image = cv.imencode('.jpg', photo)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    #send photo to server
    payload = {
        "image": base64_image,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    r = requests.post(URL, json=payload)
    print("send photo")
    return True

if __name__ == "__main__":
    init_check()
    print("main")
    while True:
        try:
            print("try")
            photo = take_photo()
            break
        except Exception as e:
            print(e)
            break