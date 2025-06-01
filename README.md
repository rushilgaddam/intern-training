# Intern Training Project – Lighthouse Avionics

Welcome to your first independent engineering task. This project is designed to introduce you to a multi-component software system that integrates network scanning, video streaming, backend services, and a frontend interface – much like the systems we build at Lighthouse.

Please read the entire document before starting.

---

## Objective

Build a complete application that:

1. Detects your smartphone on the Lighthouse network.
2. Pulls and restreams video from an IP webcam app on your phone.
3. Displays the video stream on a web interface.
4. Tracks and logs object detection (specifically, people) from the video stream.
5. Displays real-time and historical statistics through a frontend dashboard.

You are expected to work independently. Use online resources and AI tools freely, but **do not collaborate** with other interns.

---

## 🔧 Setup Instructions

### 1. Network & Webcam Setup

- Connect to the Lighthouse WiFi on your mobile device: `Lyman4621`
- Your desktop should be hardwired to the Lighthouse network, but connect to the same WiFi if not.
- Install an IP webcam app on your phone (such as "IP Webcam" on Android).
- Configure the app to stream over the network (usually via `http://<phone_ip>:port/video`).
- Note your phone’s MAC address and video stream URL.

---

### 2. Network Detection Script

Write a Python script that:

- Periodically (e.g. every 60 seconds) scans the network to detect your phone via MAC address.
- When your phone is present, automatically starts the video restream process.

**❗ Do not scan the network continuously** – this could cause network issues.

---

### 3. Video Restreaming

When the phone is detected:

- Begin pulling the video stream from the phone.
- Develop a restreamer to relay the feed to a local endpoint and supports multiple connetions.
- This restream will be used by both your object detection service and your website.

---

### 4. Object Detection Service

Create a second service that:

- Subscribes to the restreamed video feed.
- Performs **real-time person detection** using a stock model from [Ultralytics](https://github.com/ultralytics/ultralytics).
- Logs to a database:
  - Whether a frame was processed.
  - How many people were detected.

**Tips:**
- Both GPU or CPU detecion is acceptable.
- Drop frames if needed to keep processing near real-time.

---

### 5. Backend: Django

Create a Django server that:

- Stores and retrieves all person detection and frame statistics.
- Exposes a REST API to serve this data to the frontend.

Database should include:
- Total frames processed
- Total people detected
- Average people per frame (calculated server-side or client-side)

---

### 6. Frontend: Vue.js + Vuetify 3

Create a simple single-page Vue.js application that:

- Embeds the live video stream.
- Displays:
  - Total frames processed
  - Total people detected
  - Average people per frame
- Statistics should update realtime to the frontend (recommend websockets).

Style it to resemble [lighthouseavionics.com](http://lighthouseavionics.com) in color and layout.

---

## ✅ Evaluation Criteria

We will test your system by:

1. Reviewing and running all scripts and services.
2. Observing functionality across multiple web clients.
3. Evaluating robustness during phone disconnects/reconnects.
4. Ensuring database values are correctly stored and persisted.
5. Reviewing your code and asking for changes via pull request.

---

## Notes

- The Lighthouse network password is `Lyman4621`.
- Please let a full time engineer know when you are ready for a code review.
- You may structure the services however you'd like (single or multi-process).
- Logs, error handling, and robustness are important.
- Keep your code clean and modular.
- Commit frequently and include meaningful messages.
- Upload your code to your personal private GitHub repository.
- Feel free to look at other Lighthouse Avionics Organization repositories for potential example implementations.

Good luck and have fun!
