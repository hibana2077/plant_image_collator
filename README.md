<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-11-28 10:50:46
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-11-30 11:55:07
 * @FilePath: /plant_image_collator/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# plant image collator

This project is a simple tool to collate images of plants into a single image on Raspberry Pi zero 2 W. It is intended to be used to create a single image of a plant from multiple images taken from different angles.

## Hardware

### As Server

- Computer or other Single Board Computer(1GB RAM up)

### As Collator

- Raspberry Pi zero 2 W
- Raspberry Pi camera module(IMX219)
- SD card

## Installation

### Computer or SBC setup

#### Windows

1. Install `docker` and `docker-compose`.
2. Use `git clone https://github.com/hibana2077/plant_image_collator.git` to clone this repository.
3. Use `docker-compose up -d --build` to build and start the container.
4. Open `http://localhost:3000` in your browser to use web interface.

#### Linux(MacOS and SBC)

1. Install `docker` and `docker-compose`.
2. Use `git clone https://github.com/hibana2077/plant_image_collator.git` to clone this repository.
3. Use `docker-compose up -d --build` to build and start the container.
4. Open `http://localhost:3000` in your browser to use web interface.

### Raspberry Pi setup

1. Use Raspberry Pi Imager to flash Raspberry Pi OS Lite(32 bit) to SD card.
2. Before flashing, press `ctrl+shift+x` to open advanced options and set `hostname` to `<your hostname>`, and set `wifi` to your wifi network, also set `ssh` to enable.
3. After flashing, insert the SD card into Raspberry Pi zero 2 W and power on.
4. Use `ssh pi@<your hostname>.local` to connect to Raspberry Pi, and type `<your password>` to login.
5. Edit `/boot/config.txt` and add `camera_auto_detect=0` `dtoverlay=imx219` to the end of the file.
6. Use `sudo raspi-config` to open Raspberry Pi configuration tool, and set `Interfacing Options` -> `Camera` to enable.
7. Use `sudo reboot` to reboot Raspberry Pi.
8. Use `libcamera-jpeg -o test.jpg` to test camera module, and use `scp pi@<your hostname>.local:test.jpg .` to download the test image to your computer.
9. Use `sudo apt update` and `sudo apt upgrade` to update Raspberry Pi OS.
10. Use `sudo apt install git` to install git.
11. Use `git clone https://github.com/hibana2077/plant_image_collator.git && cd plant_image_collator` to clone this repository.
12. Use `sudo bash ./raspberry_pi_setup.sh` to setup Raspberry Pi.

