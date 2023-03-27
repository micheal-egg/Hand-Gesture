# Hand Gesture Recognition ✋🤖

A real-time computer vision application built with **Python**, **OpenCV**, and **MediaPipe** that detects hand gestures via webcam and overlays animated emoji-style graphics directly onto the video feed—similar to FaceTime gesture reactions.

This project focuses on learning-by-building, emphasizing how hand landmarks, coordinate systems, and image overlays work together in real-time vision systems.

## 🚀 Features

Real-time hand tracking using MediaPipe

Finger state detection (up/down logic)

Gesture classification:

✋ Palm

✊ Fist

✌️ Peace

🖕 Naughty

👍 Thumbs Up

Transparent PNG emoji overlays

Emoji positioning relative to hand landmarks (e.g., wrist-follow)

Landmark visualization for debugging and learning

## 🛠 Tech Stack

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**

## 📦 Installation & Setup

1. Clone the Repo

    ``` 
    https://github.com/micheal-egg/Hand-Gesture
    cd Hand-Gesture
    ```
2. Create Virtual Environment & Activate It

    ```
    python -m venv venv 
    venv\Scripts\activate
    ```

3. Install Dependencies

    ``` pip install opencv-python mediapipe numpy ```

4. Run the Application 

  `python hand_gestures.py`

5. Quit Application
    Press "Q" in Webcam Window to exit


## 🧩 Challenges & Learnings

The hardest part of this project was getting the hand emojis to appear in the right place and display correctly on the live camera feed. At first, the images showed up in the wrong spots or with black backgrounds, which made the experience feel off.

I worked through this by experimenting, debugging step by step, and learning how the camera feed and hand tracking data relate to each other. By the end, I was able to smoothly place and animate transparent emojis on the screen in real time, which helped me better understand how interactive computer vision projects come together.


