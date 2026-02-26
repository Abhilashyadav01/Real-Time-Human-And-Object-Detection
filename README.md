🛡️ Real-Time Human & Object Detection Suite
An advanced Computer Vision application built with Python, OpenCV, and YOLOv8. This project goes beyond simple detection by implementing behavioral analysis and time-based alerts.

🚀 Key Capabilities
👤 Human Recognition: Instantly identifies human presence and highlights them with green tracking bounds.

📦 Smart Object Labeling: Detects and labels everyday objects (bottles, chairs, laptops, etc.) with high confidence.

📱 Disturbance Alert (Focus Mode): * The system specifically monitors for cell phones.

If a phone is detected, an orange tracking box appears.

If the phone remains in frame for more than 5 minutes, the system triggers a Critical Alert (Red flash and screen warning) to help the user stay focused.

🛠️ Tech Stack
Model: YOLOv8 (Ultralytics)

Framework: Flask (for the web dashboard interface)

Processing: OpenCV & NumPy

Logic: Custom time-delta tracking for disturbance monitoring.

🔧 Installation
Clone the repo.

Install requirements: pip install ultralytics opencv-python flask.

Place yolov8n.pt in the root folder.

Run python app.py.
