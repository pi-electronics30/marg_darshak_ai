import cv2

class Camera:
    def __init__(self, source="road_sample.mp4"):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)
        
        if not self.cap.isOpened():
            print(f"CRITICAL ERROR: '{self.source}' file not found!")
        else:
            print(f"MARG-DARSHAK AI - Loading {self.source}")

    def get_frame(self):
        # Video se frame read karega
        ret, frame = self.cap.read()
        if not ret:
                   return True, frame

    def release(self):
        if self.cap:
            self.cap.release()
