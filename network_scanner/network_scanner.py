import cv2
import time
from ultralytics import YOLO
import requests

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("http://localhost:5001/video_feed")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Warning: Frame not received, retrying...")
        cap.release()
        time.sleep(1)  
        cap = cv2.VideoCapture("http://localhost:5001/video_feed")
        continue

    results = model(frame)

    people = 0
    for det in results[0].boxes.data:
        if int(det[5]) == 0:
            people += 1

    try:
        requests.post('http://localhost:8000/api/log/', json={
            "frame_processed": True,
            "people_detected": people
        }, timeout=1)
    except requests.exceptions.RequestException as e:
        print(f"Warning: Failed to post detection result: {e}")
