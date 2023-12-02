'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-12-02 22:34:09
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-12-02 22:47:17
FilePath: \plant_image_collator\lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import time
from hashlib import sha256

s = time.time()
def do_sth_make_cpu_busy():
    for i in range(10000):
        for j in range(10000):
            i*j

def do_sth_make_cpu_busy2():
    # sha256
    for i in range(10000):
        for j in range(1000):
            sha256(str(i*j).encode())

do_sth_make_cpu_busy2()
# doubl for loop - 2.5s(mutiple)
e = time.time()
print(e-s)