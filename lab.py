'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-11-29 00:45:16
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-11-29 00:47:09
FilePath: \plant_image_collator\lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv
import numpy as np
import pandas as pd
import requests
import base64

# take picture and transfer to base64 and transfer back to picture

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
    return final_frame

def convert_photo_to_base64(photo):
    #convert photo to base64
    _, encoded_image = cv.imencode('.jpg', photo)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    return base64_image

def convert_base64_to_photo(base64_image):
    #convert base64 to photo
    base64_image = base64_image.encode('utf-8')
    decoded_image = base64.b64decode(base64_image)
    np_data = np.frombuffer(decoded_image, np.uint8)
    photo = cv.imdecode(np_data, cv.IMREAD_UNCHANGED)
    return photo

if __name__ == "__main__":
    photo = take_photo()
    base64_image = convert_photo_to_base64(photo)
    print(f"base64_image: {base64_image}")
    photo = convert_base64_to_photo(base64_image)
    cv.imshow("photo", photo)
    cv.waitKey(0)
    cv.destroyAllWindows()