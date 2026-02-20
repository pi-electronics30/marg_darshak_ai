# MARG-DARSHAK AI

# 🛣️ Marg-Darshak AI

**Real-Time Road Anomaly Detection & Accident Prevention System** *Developed for the Bharat AI-SoC Student Challenge (Problem Statement 3)*

---

##  Overview
**Marg-Darshak AI** is an Edge-AI solution designed to enhance road safety by detecting potholes, cracks, and road debris in real-time. Built on the **Raspberry Pi 5** and optimized using **YOLOv8n**, this system provides preemptive visual alerts to drivers, significantly reducing the risk of accidents caused by sudden maneuvering.

##  Key Features
- **Real-Time Detection:** Low-latency detection of road hazards at 15-22 FPS.
- **Edge Intelligence:** Fully localized processing on Raspberry Pi 5—No internet required.
- **Accident Prevention:** Visual "Collision Risk" alerts based on hazard proximity.
- **Automated Logging:** Generates `road_report.csv` for municipal maintenance and "Blackspot" identification.
- **Optimized Performance:** Uses INT8 Quantization and XNNPACK delegates for maximum hardware efficiency.

##  Tech Stack
- **Hardware:** Raspberry Pi 5 (8GB LPDDR5 RAM)
- **Architecture:** YOLOv8n (Anchor-Free Detection)
- **Inference Engine:** TensorFlow Lite (TFLite Runtime)
- **Languages/Libs:** Python 3.11, OpenCV, NumPy

Technical Spotlight: The best_int8.tflite Model
1. Dataset Origin: GRDDC
The model is trained on the Global Road Damage Detection Challenge (GRDDC) dataset. This is one of the most comprehensive datasets in the world, containing thousands of labeled images from various countries, including India, Japan, and the Czech Republic.

Real-World Diversity: It covers a vast range of road conditions, lighting, and weather scenarios.

Indian Context: Since it includes Indian road data, the model is highly accurate at identifying the specific types of "alligator cracks" and "deep potholes" commonly found in our geography.

2. Architecture: YOLOv8n (Nano)
We chose the YOLOv8n architecture for this specific model because it is Anchor-Free.

Irregular Anomaly Detection: Unlike older models that look for fixed shapes, YOLOv8n identifies the center of a road defect, making it superior at detecting long, winding cracks and non-circular potholes.

C2f Modules: It utilizes Cross-Stage Partial Bottlenecks (C2f) to fusion high-level road features without increasing the computational load on the Raspberry Pi 5.

3. Optimization: INT8 Quantization
The "int8" in the filename signifies that the model has undergone Post-Training Quantization (PTQ).

Size Efficiency: The original FP32 model was compressed by 75%, reducing the storage and RAM footprint significantly.

Hardware Acceleration: By converting weights to 8-bit integers, the model leverages the XNNPACK delegate on the Raspberry Pi 5, achieving a consistent 20 FPS inference speed—essential for high-speed accident prevention.

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
