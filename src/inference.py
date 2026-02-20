import numpy as np
import cv2
from tflite_runtime.interpreter import Interpreter

class RoadInference:
    def __init__(self, model_path):
        # Pi 5 optimization: use 4 threads
        self.interpreter = Interpreter(model_path=model_path, num_threads=4)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.h, self.w = self.input_details[0]['shape'][1], self.input_details[0]['shape'][2]
        self.is_float = self.input_details[0]['dtype'] == np.float32

    def detect(self, frame):
        # Resize frame to model input size
        img_resized = cv2.resize(frame, (self.w, self.h))
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        input_data = np.expand_dims(img_rgb, axis=0)

        if self.is_float:
            input_data = input_data.astype(np.float32) / 255.0

        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()

        output = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        
        # YOLOv8 format adjustment: transpose if necessary
        if output.shape[0] < output.shape[1]:
            output = output.transpose()

        detections = []
        for row in output:
            scores = row[4:]
            if scores.size == 0: continue
            conf = np.max(scores)
            if conf > 0.35: # Confidence Threshold
                cls_id = np.argmax(scores)
                # Format: [x_center, y_center, width, height, confidence, class_id]
                detections.append([row[0], row[1], row[2], row[3], conf, cls_id])
        
        return detections, (self.w, self.h)
