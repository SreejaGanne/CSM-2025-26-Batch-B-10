from ultralytics import YOLO
import cv2
import serial
import time

# 🔌 Serial connection
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)
arduino.reset_input_buffer()

# Load YOLO model
model = YOLO("/home/pi/Desktop/tamota disease/student dataset/runs/detect/train/weights/best.pt")

print("Waiting for 'ON' signal from Arduino...")

while True:

    if arduino.in_waiting > 0:
        command = arduino.readline().decode().strip()
        print("Received:", command)

        if command == "ON":

            print("Camera Activated for 5 seconds...")

            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                print("Error: Cannot open webcam")
                continue

            start_time = time.time()
            detected_label = None

            while time.time() - start_time < 5:

                ret, frame = cap.read()
                if not ret:
                    break

                # YOLO Detection
                results = model(frame, conf=0.30)
                annotated_frame = results[0].plot()

                # Get first detected disease
                if len(results[0].boxes) > 0:
                    box = results[0].boxes[0]
                    cls = int(box.cls)
                    detected_label = model.names[cls]

                cv2.imshow("Tomato Disease Detection", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

            print("Camera OFF")

            # 🔥 Send detected disease to Arduino
            if detected_label:
                arduino.write((detected_label + "\n").encode())
                print("Sent to Arduino:", detected_label)
            else:
                print("No disease detected")

            print("Waiting for next ON signal...")

    time.sleep(0.1)
