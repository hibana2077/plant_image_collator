<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-11-28 10:50:46
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-12-02 15:33:30
 * @FilePath: /plant_image_collator/README.md
 * @Description: This is a project for plant image collator.
-->

# GreenMerge (Plant Image Collator)

![python](https://img.shields.io/badge/python-3.9-blue?style=plastic-square&logo=python)
![pandas](https://img.shields.io/badge/pandas-2.1.3-150458?style=plastic-square&logo=pandas)
![fastapi](https://img.shields.io/badge/fastapi-0.104.1-009688?style=plastic-square&logo=fastapi)
![streamlit](https://img.shields.io/badge/streamlit-1.29.0-FF4B4B?style=plastic-square&logo=streamlit)
![mongodb](https://img.shields.io/badge/mongodb-7.0-47A248?style=plastic-square&logo=mongodb)
![docker](https://img.shields.io/badge/docker-24.0.6-2496ED?style=plastic-square&logo=docker)
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

## 🔧 Installation

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

### Collator Setup

#### Raspberry Pi Series + IMX219 Camera Module

Follow these steps to set up a Raspberry Pi as a collator:

1. **Prepare the SD Card**:
   - Use the Raspberry Pi Imager to flash Raspberry Pi OS Lite (32 bit) onto the SD card.
   - Before flashing, press `Ctrl+Shift+X` to access advanced options. Set your `hostname`, configure `WiFi` credentials, and enable `SSH`.

2. **Initial Raspberry Pi Setup**:
   - Insert the flashed SD card into the Raspberry Pi and power it on.
   - Connect to the Raspberry Pi via SSH: `ssh pi@<your hostname>.local` and log in with your password.

3. **Configure Camera Settings**:
   - Edit the file `/boot/config.txt` and add `camera_auto_detect=0` and `dtoverlay=imx219` at the end.
   - Open the Raspberry Pi configuration tool with `sudo raspi-config`, navigate to `Interfacing Options` -> `Camera`, and enable it.

4. **Update and Install Dependencies**:
   - Update the OS with: `sudo apt update` and `sudo apt upgrade`.
   - Install Git: `sudo apt install git`.

5. **Clone Repository and Setup**:
   - Clone the GreenMerge repository: `git clone https://github.com/hibana2077/plant_image_collator.git && cd plant_image_collator`.
   - Run the setup script: `sudo bash ./raspberry_pi_setup.sh`.
   - Reboot the Raspberry Pi: `sudo reboot`.

6. **Configure Collator Settings**:

    To customization the collator's operations, edit the `collator/config.yaml` file with the following settings:

    - `encoding`: Specify the image format. Example: `"png"`.
    - `interval`: Set the time interval (in seconds) for image capture. Example: `"360"` (for capturing images every 360 seconds).
    - `notify`: Enable or disable notifications. Set to `True` for enabling notifications.
    - `verbose`: Enable detailed logging. Set to `True` for more detailed logs.
    - `node_name`: Define the name of the node. Example: `"NODE_NAME"`.
    - `notify_webhook`: Provide the webhook URL for notifications. Example: `"NOTIFY_WEBHOOK"`.
    - `plant_name`: Name the plant being monitored. Example: `"PLANT_NAME"`.
    - `URL`: Set the URL for the server where images are sent. Example: `"http://YOUR_IP:5000/"`.

7. **Start the Collator**:
   - Start the collator with: `sudo bash ./raspberry_pi_start.sh`.

8. **Test Camera Module**:
   - Test the camera with `libcamera-jpeg -o test.jpg`.
   - Download the test image to your computer with `scp pi@<your hostname>.local:test.jpg .`.

#### ESP32-CAM

(Still under development)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
