<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-11-28 10:50:46
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-12-02 15:16:00
 * @FilePath: /plant_image_collator/README.md
 * @Description: This is a project for plant image collator.
-->

# GreenMerge (Plant Image Collator)

![python](https://img.shields.io/badge/python-3.10-blue?style=plastic-square&logo=python)
![pandas](https://img.shields.io/badge/pandas-1.3.3-150458?style=plastic-square&logo=pandas)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9.1-EE4C2C?style=plastic-square&logo=pytorch)
![fastapi](https://img.shields.io/badge/fastapi-0.85.1-009688?style=plastic-square&logo=fastapi)
![mongodb](https://img.shields.io/badge/mongodb-4.4.6-47A248?style=plastic-square&logo=mongodb)
![docker](https://img.shields.io/badge/docker-20.10.8-2496ED?style=plastic-square&logo=docker)
![lisence](https://img.shields.io/github/license/hibana2077/plant_image_collator?style=plastic-square)

GreenMerge is a plant image collator for plant phenotyping. It can be used to collect plant images from multiple IoT devices and store them in a database. It also provides a web interface for users to view and download images.

## ✨ Key Features

- **Support for Multiple IoT Devices**: Seamlessly compatible with a variety of IoT devices, including Raspberry Pi, Arduino, and more. [Learn More](./supported_devices.md)
- **Extensive Image Format Support**: Accommodates a wide range of popular image formats, such as JPG, PNG, ensuring flexible image processing.
- **User-Friendly Web Interface**: Provides an intuitive web interface for users to easily view and download images.
- **Collator Status Monitoring**: Enables real-time monitoring of the collator's status, ensuring smooth operation and high efficiency.

## 🛠️ Hardware Requirements

### Server

- Any system capable of running Docker and Docker-compose. This includes computers and single-board computers (SBCs) with the following specifications:
  - Operating System: Must support Docker (Linux, Windows, macOS).
  - Processor: Compatible with ARM64 architecture (for ARM64 OS, requires a CPU greater than ARMv8.2).
  - Memory: Minimum of 1GB RAM.

### Collator

- The collator can be either a Single Board Computer (SBC) or a Microcontroller Unit (MCU):
  - **SBC Option**:
    - Must be Linux-compatible and equipped with a camera.
    - Examples include Raspberry Pi Zero 2 W with a camera module like Raspberry Pi camera (IMX219).
    - Storage: SD card or appropriate storage medium for the SBC.

  - **MCU Option**:
    - Must support MicroPython and be equipped with a camera.
    - Suitable for MCUs that can handle image capture and basic processing.
    - Camera compatibility is essential for effective image collation.

These hardware setups ensure smooth operation of GreenMerge, allowing for efficient image collection and processing across different environments.

## Installation

### Server Setup

The setup process is similar across Windows, Linux, macOS, and Single Board Computers (SBCs). Follow these steps:

1. **Install Docker and Docker-Compose**:
   - For Windows/Linux/macOS, download and install Docker and Docker-Compose from their official websites.
   - For SBCs, ensure the OS supports Docker and install them accordingly.

2. **Clone the Repository**:
   - Use the command `git clone https://github.com/hibana2077/plant_image_collator.git` to clone the GreenMerge repository to your local system.

3. **Build and Start the Container**:
    - Navigate to the `plant_image_collator/server` directory.
    - Run `docker-compose up -d --build`. This command builds and starts the container in detached mode.

4. **Access the Web Interface**:
   - Once the container is running, open your web browser and go to `http://localhost:8501` or `http://<your ip address>:8501` to access the web interface.

This installation process sets up the GreenMerge server, allowing you to start managing and collating plant images effectively.

### Collator setup

#### Raspberry Pi Series

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

