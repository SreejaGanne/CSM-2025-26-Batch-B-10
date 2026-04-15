🌱 Smart Fertilizer Spraying System with Disease Severity Analysis

An AI + IoT-based smart agriculture system that detects plant disease severity and automatically controls fertilizer spraying for precision farming.

🚀 Overview

This project is an automated agricultural robot that uses computer vision and embedded systems to:

Detect tomato plant disease severity (Low, Medium, High)
Automatically control fertilizer spraying
Reduce manual effort and resource wastage
Promote sustainable farming
🧠 Key Features
🔍 Real-time disease detection using YOLOv8
🤖 Automated fertilizer spraying based on severity
📡 Bluetooth control for wireless monitoring
⚡ Solar-powered energy-efficient system
🚜 Robot movement using DC motors
🎯 Precision agriculture with minimal human intervention
🏗️ System Architecture
Camera → Raspberry Pi → YOLOv8 Model → Severity Prediction
        ↓
   Serial Communication
        ↓
     Arduino → Relay → Pumps → Fertilizer Spraying
🧰 Technologies Used
Python
YOLOv8 (Ultralytics)
PyTorch
Raspberry Pi
Arduino Uno
Embedded C
Bluetooth Module (HC-05)
Relay Module & DC Pumps
📂 Dataset
Total Images: 1500+ tomato plant images
Classes:
Low Severity
Medium Severity
High Severity
Annotation Format: YOLO format
⚙️ Working Process
📷 Capture plant image using USB camera
🧠 YOLOv8 model predicts disease severity
📡 Raspberry Pi sends result to Arduino
⚡ Arduino activates corresponding relay
💧 Fertilizer is sprayed based on severity level
📲 Bluetooth enables manual monitoring/control
🔌 Hardware Components
Raspberry Pi
Arduino Uno
USB Camera
Relay Module
DC Water Pumps
Robot Chassis & Motors
12V Battery
9V Solar Panel
Bluetooth Module (HC-05)
📊 Results
✔ Real-time disease detection
✔ Automated fertilizer spraying
✔ Reduced fertilizer wastage
✔ Improved crop management efficiency
🌍 Applications
Smart Agriculture
Precision Farming
Crop Monitoring Systems
Automated Irrigation & Fertilization
🔮 Future Enhancements
Mobile App integration
Cloud-based monitoring
Multi-crop disease detection
GPS-based navigation
👩‍💻 Author

Sreeja Ganne
AI & ML Student

⭐ If you like this project

Give it a ⭐ on GitHub!
