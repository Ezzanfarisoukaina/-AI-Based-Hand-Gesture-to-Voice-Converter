
# AI-Based Hand Gesture to Voice Converter

An AI-powered Python application that recognizes hand gestures in real time using a webcam and converts them into text and spoken messages.

## Project Overview

This project combines Computer Vision, Machine Learning, and Text-to-Speech technology to create a real-time hand gesture recognition system.

The application detects hand landmarks using MediaPipe, classifies gestures using a trained Random Forest model, maps each gesture to a predefined message, and converts the message into speech.

## Features

- Real-time hand detection using a webcam.
- Hand landmark extraction using MediaPipe (21 landmarks).
- Machine Learning-based gesture classification.
- Gesture-to-text conversion.
- Text-to-Speech output.
- Real-time prediction confidence display.

## Supported Gestures

| Gesture | Generated Message |
|---|---|
| THUMB_UP | Good! |
| OPEN_PALM | Hello! |
| FIST | No! |
| PEACE | Victory! |
| OK | Everything is OK! |

## Technologies Used

- Python 3.11
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Scikit-learn
- Joblib
- pyttsx3

## Machine Learning Model

A Random Forest Classifier was trained using a custom dataset containing 1,000 samples.

- Total samples: 1,000
- Number of gestures: 5
- Samples per gesture: 200
- Training samples: 800
- Testing samples: 200
- Test accuracy: 100%

Note: The reported accuracy is based on a held-out test split from the collected dataset. Further testing under different lighting conditions and with different users is needed to evaluate generalization.

## Project Structure

```text
HandGestureAI/
├── data/
│   └── gestures/
│       └── gestures.csv
├── models/
│   └── gesture_model.pkl
├── src/
│   ├── data_collection.py
│   ├── train_model.py
│   ├── prediction.py
│   ├── text_mapping.py
│   └── test_voice.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/HandGestureAI.git
cd HandGestureAI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python src/prediction.py
```

Make sure your webcam is connected.

Press `Q` to quit the application.

## How It Works

1. The webcam captures real-time video.
2. MediaPipe detects the hand and extracts 21 landmarks.
3. The trained Random Forest model predicts the gesture.
4. The predicted gesture is mapped to a predefined text message.
5. The pyttsx3 engine converts the message into speech.

## Project Goal

The goal is to demonstrate how Computer Vision and Machine Learning can be combined with Speech Synthesis to build an interactive gesture recognition system.

## Author

**Soukaina Ezzanfari**

Master's Student in Engineering in Computer Science and Data Analysis (2IAD)

Interests: Artificial Intelligence, Machine Learning, Data Science and Software Development.
