import cv2
import time
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VIDEO_URL = "http://192.168.30.85:4747/video"
latest_frame = None
lock = threading.Lock()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_frames():
    global latest_frame
    cap = cv2.VideoCapture(VIDEO_URL)
    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(1)
            cap.release()
            cap = cv2.VideoCapture(VIDEO_URL)
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
           
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        with lock:
            latest_frame = frame

        time.sleep(0.01)


class VideoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/video_feed':
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
        self.end_headers()
        try:
            while True:
                with lock:
                    frame = latest_frame.copy() if latest_frame is not None else None
                if frame is None:
                    continue
                ret, jpeg = cv2.imencode('.jpg', frame)
                if not ret:
                    continue
                self.wfile.write(b'--frame\r\n')
                self.wfile.write(b'Content-Type: image/jpeg\r\n\r\n')
                self.wfile.write(jpeg.tobytes())
                self.wfile.write(b'\r\n')
                time.sleep(0.03)
        except:
            pass

if __name__ == '__main__':
    threading.Thread(target=capture_frames, daemon=True).start()
    ThreadingHTTPServer(('0.0.0.0', 5001), VideoHandler).serve_forever()
