
# AI-Based Hand Gesture to Voice Converter 🤖🖐️

A real-time AI-powered application that recognizes hand gestures using a webcam and converts them into text and spoken messages.

The project combines Computer Vision, Machine Learning, and Text-to-Speech technologies to make communication more interactive and accessible.

## ✨ Features

- Real-time hand detection using a webcam.
- Hand landmark extraction using MediaPipe.
- Hand gesture classification using Random Forest.
- Gesture-to-text conversion.
- Text-to-Speech output.
- Five supported hand gestures.

## 🖐️ Supported Gestures

| Gesture | Message |
|---|---|
| THUMB_UP 👍 | Good! |
| OPEN_PALM ✋ | Hello! |
| FIST ✊ | No! |
| PEACE ✌️ | Victory! |
| OK 👌 | Everything is OK! |

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Scikit-learn
- Joblib
- pyttsx3

## 🧠 Machine Learning Model

The project uses a Random Forest Classifier to recognize hand gestures.

- Dataset: 1,000 samples
- Number of gestures: 5
- Features: 63 numerical features extracted from 21 hand landmarks
- Training samples: 800
- Testing samples: 200
- Test accuracy: 100%

*Note: The reported accuracy is based on the current test split. Further testing with different users, lighting conditions, and environments is recommended.*

## 📁 Project Structure

```text
HandGestureAI/
│
├── data/
│   └── gestures/
│       └── gestures.csv
│
├── models/
│   └── gesture_model.pkl
│
├── src/
│   ├── data_collection.py
│   ├── train_model.py
│   ├── prediction.py
│   ├── text_mapping.py
│   ├── test_voice.py
│   └── test_multiple_voice.py
│
├── camera.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ezzanfarisoukaina/-AI-Based-Hand-Gesture-to-Voice-Converter.git
```

### 2. Navigate to the project folder

```bash
cd -AI-Based-Hand-Gesture-to-Voice-Converter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the real-time gesture recognition application:

```bash
python src/prediction.py
```

Make sure your webcam is connected and available.

## 🎯 Project Objective

The main objective is to explore how Artificial Intelligence and Computer Vision can transform hand gestures into understandable text and speech in real time.

## 👩‍💻 Author

**Soukaina Ezzanfari**

Master's Student in Computer Science and Data Analysis.

---

⭐ If you find this project interesting, feel free to star the repository!
