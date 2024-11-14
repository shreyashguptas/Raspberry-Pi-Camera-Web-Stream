# Raspberry Pi Camera Web Stream

This project sets up a live web stream from a Raspberry Pi camera module that can be accessed from any device on your local network through a web browser.

## Hardware Requirements

- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- Raspberry Pi Camera Module (tested with OV5647 camera)
- Power supply for Raspberry Pi
- MicroSD card (minimum 8GB recommended)
- Network connection (WiFi or Ethernet)

## Software Requirements

- Raspberry Pi OS (tested on Debian 12 Bookworm)
- Python 3.x
- Web browser on client device

## Initial Setup

### 1. Raspberry Pi OS Installation
1. Download and install [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Flash Raspberry Pi OS (64-bit recommended) to your microSD card
3. Configure WiFi and SSH during flashing if needed

### 2. Camera Setup
1. Connect the camera module to the Raspberry Pi's camera port
2. Enable the camera interface: