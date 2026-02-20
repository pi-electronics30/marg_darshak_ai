import csv
import time
import os

class AnomalyLogger:
    def __init__(self, file_path='marg_darshak_ai.csv'):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'Anomaly_Type', 'Confidence'])

    def log(self, anomaly_type, confidence):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.file_path, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, anomaly_type, f"{confidence:.2f}"])
                f.flush()
        except Exception as e:
            print(f"Logging Error: {e}")
