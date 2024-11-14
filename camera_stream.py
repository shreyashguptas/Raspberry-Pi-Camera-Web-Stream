from picamera2 import Picamera2
from flask import Flask, Response
import cv2
import time
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Changed to DEBUG for more info
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize camera with error handling
try:
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration(main={"size": (800, 600)})
    picam2.configure(camera_config)
    picam2.start()
    logger.info("Camera initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize camera: {e}")
    raise

def generate_frames():
    while True:
        try:
            # Capture frame
            frame = picam2.capture_array()
            
            # Convert to jpg format
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                logger.error("Failed to encode frame")
                continue
                
            frame = buffer.tobytes()
            
            # Yield the frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
        except Exception as e:
            logger.error(f"Error in generate_frames: {e}")
            time.sleep(1)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Pi Camera Stream</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; }
                img { max-width: 100%; height: auto; }
            </style>
        </head>
        <body>
            <h1>Pi Camera Stream</h1>
            <img src="/video_feed" />
        </body>
    </html>
    """

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        logger.info("Starting camera stream server...")
        # Using specific IP and port 5050
        app.run(host='192.168.0.155', port=5050, threaded=True)
    except Exception as e:
        logger.error(f"Server error: {e}")
    finally:
        logger.info("Cleaning up...")
        picam2.stop()
        picam2.close()