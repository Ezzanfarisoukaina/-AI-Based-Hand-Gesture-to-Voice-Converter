
import cv2
import mediapipe as mp
import csv
import os

# Configuration MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Configuration Dataset
GESTURE_NAME = "OK"
SAMPLES_TO_COLLECT = 200

DATA_DIR = "data/gestures"
os.makedirs(DATA_DIR, exist_ok=True)

CSV_FILE = os.path.join(DATA_DIR, "gestures.csv")

# Enregistrer les donnees
file_exists = os.path.isfile(CSV_FILE)

with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        header = ["label"]
        for i in range(21):
            header += [f"x{i}", f"y{i}", f"z{i}"]
        writer.writerow(header)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erreur webcam")
        exit()

    collected = 0
    recording = False

    print("Place ta main en position THUMB_UP")
    print("Appuie sur S pour commencer")
    print("Appuie sur Q pour quitter")

    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                if recording and collected < SAMPLES_TO_COLLECT:

                    row = [GESTURE_NAME]

                    for landmark in hand_landmarks.landmark:
                        row.extend([
                            landmark.x,
                            landmark.y,
                            landmark.z
                        ])

                    writer.writerow(row)
                    collected += 1

        if collected >= SAMPLES_TO_COLLECT:
            recording = False

        cv2.putText(
            frame,
            f"Gesture: {GESTURE_NAME}",
            (10, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Samples: {collected}/{SAMPLES_TO_COLLECT}",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.imshow("Dataset Collection", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            recording = True

        if key == ord("q"):
            break

    cap.release()

hands.close()
cv2.destroyAllWindows()

print(f"Collection terminee : {collected} samples")
