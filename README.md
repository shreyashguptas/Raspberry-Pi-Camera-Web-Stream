# Raspberry Pi Camera Web Stream

This project sets up a live web stream from a Raspberry Pi camera module that can be accessed from any device on your local network through a web browser.

## Hardware Requirements

- Raspberry Pi (tested on [Raspberry Pi 2 Model B](https://www.raspberrypi.com/products/raspberry-pi-2-model-b/)) Any newer Rasberry pi would be much better.
- Camera that supports Raspberry Pi (tested on [Raspberry Pi 5Mp AGP Gddr3 Camera Board Module](https://www.amazon.in/dp/B00E1GGE40))
- Power supply for Raspberry Pi 
- MicroSD card (minimum 4GB recommended)
- Network connection (WiFi or Ethernet)

## Software Requirements

- Raspberry Pi OS (tested on Raspberry Pi OS Lite)
- Python 3.11
- Web browser on local device (I live stream it on my iPad👇)
![Image-of-live-stream-on-the-ipad](Image/iPad-Streaming-Live-Feed.jpeg)

## Initial Setup

### 1. Raspberry Pi OS Installation
1. Download and install [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Flash Raspberry Pi OS (64-bit recommended) to your microSD card
3. Configure WiFi and SSH during flashing if needed (if you do not know what this means then ask ChatGPT.)

### 2. Camera Setup
1. Connect the camera module to the Raspberry Pi's camera port
2. Enable the camera interface:
```bash
sudo raspi-config
```
Navigate to: Interface Options → Camera → Enable → Finish → Reboot (This may look a little different but there is an option I promise)

### 3. System Updates
```bash
sudo apt update && sudo apt upgrade -y
```

### 4. Required Packages Installation
Install all necessary packages:
```bash
# Install system dependencies
sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
```

```bash
# Install Python packages
sudo apt install -y python3-opencv python3-flask python3-picamera2
```

### 5. Firewall Configuration
```bash
# Install UFW if not already installed
sudo apt install ufw
```

```bash
# Enable UFW
sudo ufw enable
```

```bash
# Allow SSH (important to prevent lockout!)
sudo ufw allow ssh
```

```bash
# Allow port 5050 for the web stream
sudo ufw allow 5050/tcp
```

```bash
# Verify settings
sudo ufw status
```

## Project Setup

### 1. Create Project Directory
```bash
mkdir ~/camera_stream
cd ~/camera_stream
```

### 2. Create Python Script
Create `camera_stream.py` and copy the provided code into it.

## Running the Stream

1. Start the stream:
```bash
python3 camera_stream.py
```

2. Access the stream:
- Find your Raspberry Pi's IP address:
```bash
hostname -I
```
- Open a web browser on any device on your local network
- Enter the URL: `http://YOUR_PI_IP:5050`

## Troubleshooting

### Common Issues and Solutions

1. **ModuleNotFoundError**
   - Verify all packages are installed:
   ```bash
   python3 -c "import cv2; print('OpenCV:', cv2.__version__)"
   python3 -c "import flask; print('Flask:', flask.__version__)"
   python3 -c "from picamera2 import Picamera2; print('Picamera2 available')"
   ```

2. **Cannot Access Stream**
   - Verify the server is running:
   ```bash
   netstat -tulpn | grep 5050
   ```
   - Check firewall status:
   ```bash
   sudo ufw status
   ```
   - Verify you're on the same network as the Pi
   - Try pinging the Pi:
   ```bash
   ping YOUR_PI_IP
   ```

3. **Camera Not Detected**
   - Check camera connection
   - Verify camera is enabled:
   ```bash
   vcgencmd get_camera
   ```
   Should show: `supported=1 detected=1`

4. **Permission Denied**
   - Ensure proper permissions:
   ```bash
   sudo usermod -a -G video $USER
   ```
   Then reboot

### What Not to Do

1. **Don't** use pip to install packages when system packages are available
   - Use `apt install python3-package_name` instead of `pip install package_name`

2. **Don't** disable SSH before confirming web stream works
   - Keep SSH access until everything is working

3. **Don't** expose the stream to the internet without proper security
   - This setup is for local network use only

4. **Don't** run the script as root
   - Use proper permissions instead

5. **Don't** use virtual environments for this project
   - System-wide packages work better with Raspberry Pi camera modules

## Security Considerations

- This stream is not encrypted
- Only use on trusted local networks
- Don't expose port 5050 to the internet
- Consider adding authentication if needed

## Performance Tips

1. Adjust resolution in the code if needed
2. Modify the sleep time in `generate_frames()` to change frame rate
3. Use a wired network connection for better performance

## Contributing

Feel free to fork this repository and submit pull requests for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Raspberry Pi Foundation
- Thanks to the developers of picamera2, Flask, and OpenCV

## Support

If you encounter any issues:
1. Check the troubleshooting section
2. Open an issue on GitHub
3. Provide logs and error messages when reporting issues