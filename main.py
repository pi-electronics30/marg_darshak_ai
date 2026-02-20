import cv2
import time
from src.camera import Camera
from src.inference import RoadInference
from src.logger import AnomalyLogger

def run_project():
    print("--- MARG DARSHAK AI PROGRAM ENABLED")
    try:
        # Strictly video file mode
        cam = Camera(source="road_sample.mp4") 
        engine = RoadInference(model_path="src/models/best_int8.tflite")
        logger = AnomalyLogger()
        
 
        class_names = ["Pothole", "Crack", "Debris", "Road Anomaly"]
    except Exception as e:
        print(f"Init Error: {e}"); return

    while True:
        ret, frame = cam.get_frame()
        if not ret: 
            print("Video ended or error.")
            break

        start_t = time.time()
        detections, m_size = engine.detect(frame)
        h_f, w_f = frame.shape[:2]
        mw, mh = m_size

        for det in detections:
            # Check for standard YOLOv8 output length
            if len(det) < 6: continue
            
            x_c, y_c, bw, bh, conf, cls_id = det
            idx = int(cls_id)

            # --- COORDINATES SCALING ---
            if x_c <= 1.0: # Normalized scale
                x1, y1 = int((x_c - bw/2) * w_f), int((y_c - bh/2) * h_f)
                x2, y2 = int((x_c + bw/2) * w_f), int((y_c + bh/2) * h_f)
            else: # Pixel scale (320x320)
                x1, y1 = int((x_c - bw/2) * w_f / mw), int((y_c - bh/2) * h_f / mh)
                x2, y2 = int((x_c + bw/2) * w_f / mw), int((y_c + bh/2) * h_f / mh)

            # --- CLASS LABEL LOGIC ---
                      if idx < len(class_names):
                name = class_names[idx]
            else:
                name = "Pothole" # Default label for demo

            # Colors: Red for Pothole, Yellow for Crack
            color = (0, 0, 255) if "Pothole" in name else (0, 255, 255)

            # Draw Box and Label
            cv2.rectangle(frame, (max(0, x1), max(0, y1)), (min(w_f, x2), min(h_f, y2)), color, 3)
            label = f"{name} {int(conf*100)}%"
            cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            
            # Log results in CSV
            if conf > 0.45:
                logger.log(name, conf)

        # FPS calculation
        fps = 1.0 / (time.time() - start_t)
        cv2.putText(frame, f"FPS: {fps:.1f}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Bharat_SOC - Video Demo", frame)
        
        # 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_project()
