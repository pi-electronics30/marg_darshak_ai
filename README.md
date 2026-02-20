# MARG-DARSHAK AI

# 🛣️ Marg-Darshak AI

**Real-Time Road Anomaly Detection & Accident Prevention System** *Developed for the Bharat AI-SoC Student Challenge (Problem Statement 3)*

---

## 📝 Overview
**Marg-Darshak AI** is an Edge-AI solution designed to enhance road safety by detecting potholes, cracks, and road debris in real-time. Built on the **Raspberry Pi 5** and optimized using **YOLOv8n**, this system provides preemptive visual alerts to drivers, significantly reducing the risk of accidents caused by sudden maneuvering.

## 🚀 Key Features
- **Real-Time Detection:** Low-latency detection of road hazards at 15-22 FPS.
- **Edge Intelligence:** Fully localized processing on Raspberry Pi 5—No internet required.
- **Accident Prevention:** Visual "Collision Risk" alerts based on hazard proximity.
- **Automated Logging:** Generates `road_report.csv` for municipal maintenance and "Blackspot" identification.
- **Optimized Performance:** Uses INT8 Quantization and XNNPACK delegates for maximum hardware efficiency.

## 🛠️ Tech Stack
- **Hardware:** Raspberry Pi 5 (8GB LPDDR5 RAM)
- **Architecture:** YOLOv8n (Anchor-Free Detection)
- **Inference Engine:** TensorFlow Lite (TFLite Runtime)
- **Languages/Libs:** Python 3.11, OpenCV, NumPy

## 📁 Project Structure
```text
Marg-Darshak-AI/

|___main.py              #main excution script
├── src/
│   |__video.py          # to use a video as source to detect road anomaly
│   ├── camera.py        # Frame acquisition & preprocessing
│   ├── inference.py     # TFLite Engine & YOLOv8n logic
│   └── logger.py        # CSV Reporting & Alert system
├── models/
│   └── yolov8n_int8.tflite # Custom Optimized Model File
├── data/
│   └── road_sample.mp4  # Testing dataset
├── README.md
└── requirements.txt
