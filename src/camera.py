import cv2
import threading
import subprocess
import numpy as np

class CAMERA:
    def __init__(self, width=640, height=480, fps=30):
        self.width = width
        self.height = height
        
     
        self.cmd = [
            'rpicam-vid',
            '-t', '0', 
            '--width', str(self.width),
            '--height', str(self.height),
            '--framerate', str(fps),
            '--codec', 'mjpeg',
            '--inline',
            '--nopreview',
            '-o', '-' 
        ]
        
        try:
     
            self.process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, bufsize=10**8)
            print("MARG-DARSHAK AI - rpicam-vid Process Started")
            self.running = True
        except Exception as e:
            print(f"CRITICAL ERROR: Could not start rpicam-vid: {e}")
            self.running = False

        self.frame = None
        self.lock = threading.Lock()
        
    def start(self):
        """Starts the capture thread."""
        if self.running:
            threading.Thread(target=self._update, args=(), daemon=True).start()
        return self

    def _update(self):
        """Reads raw bytes from rpicam-vid pipe and decodes to frame."""
        # Buffer to store frame data
        bytes_data = b''
        while self.running:
          
            chunk = self.process.stdout.read(4096)
            if not chunk:
                break
            bytes_data += chunk
            
           
            a = bytes_data.find(b'\xff\xd8') # SOI
            b = bytes_data.find(b'\xff\xd9') # EOI
            
            if a != -1 and b != -1:
                jpg = bytes_data[a:b+2]
                bytes_data = bytes_data[b+2:]
                

                frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                
                if frame is not None:
                    with self.lock:
                        self.frame = frame

    def get_frame(self):
        with self.lock:
            if self.frame is None:
                return False, None
            return True, self.frame.copy()

    def release(self):
        self.running = False
        if self.process:
            self.process.terminate()
            self.process.wait()
