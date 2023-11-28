'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-11-28 11:30:10
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-11-28 14:00:24
FilePath: /plant_image_collator/src/main/app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv
import numpy as np
import pandas as pd
from datetime import datetime

def init_check():
    print("init check")
    return True

def take_photo(times:int = 10):
    # open camera
    cap = cv.VideoCapture(0)
    cnt = 0
    while cnt<times:
        ret, frame = cap.read()
        if cnt == times-1:
            print("take photo")

            cv.imwrite(f"./data/{datetime.now()}.jpg", frame)
        cnt += 1
    # close camera
    cap.release()

if __name__ == "__main__":
    init_check()
    print("main")
    while True:
        try:
            print("try")
            take_photo()
            break
        except Exception as e:
            print(e)
            break