
import cv2
import mediapipe as mp
import pandas as pd
import joblib
import pyttsx3
import threading
import queue
import time

# ==========================================
# 1. Charger le modele entraine
# ==========================================

model = joblib.load("models/gesture_model.pkl")

print("AI Model loaded successfully!")

# ==========================================
# 2. Text Mapping
# ==========================================

from text_mapping import get_message

# ==========================================
# 3. Systeme vocal dans un Thread separe
# ==========================================

voice_queue = queue.Queue()


def voice_worker():

    while True:

        message = voice_queue.get()

        if message is None:
            voice_queue.task_done()
            break

        try:
            print("Speaking:", message)

            engine = pyttsx3.init(driverName="sapi5")

            engine.setProperty("rate", 150)
            engine.setProperty("volume", 1.0)

            engine.say(message)
            engine.runAndWait()

            engine.stop()
            del engine

            time.sleep(1)

        except Exception as e:
            print("Voice Error:", e)

        finally:
            voice_queue.task_done()



voice_thread = threading.Thread(
    target=voice_worker,
    daemon=True
)

voice_thread.start()

print("Voice engine initialized!")

# ==========================================
# 4. Initialiser MediaPipe
# ==========================================

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ==========================================
# 5. Ouvrir la webcam
# ==========================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: Webcam inaccessible")
    voice_queue.put(None)
    exit()

print("Real-time gesture recognition started!")
print("Press Q to quit.")

# ==========================================
# 6. Liste des caracteristiques
# ==========================================

columns = []

for i in range(21):
    columns.extend([
        f"x{i}",
        f"y{i}",
        f"z{i}"
    ])

# ==========================================
# 7. Variables de controle
# ==========================================

CONFIDENCE_THRESHOLD = 75

last_gesture = None

# ==========================================
# 8. Boucle principale
# ==========================================

try:

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                # Dessiner les points de la main
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                # Extraire les 63 valeurs
                landmarks = []

                for landmark in hand_landmarks.landmark:
                    landmarks.extend([
                        landmark.x,
                        landmark.y,
                        landmark.z
                    ])

                # Transformer en DataFrame
                input_data = pd.DataFrame(
                    [landmarks],
                    columns=columns
                )

                # Prediction
                prediction = model.predict(input_data)[0]

                # Calculer la confidence
                probabilities = model.predict_proba(input_data)[0]

                confidence = max(probabilities) * 100

                # Text Mapping
                message = get_message(prediction)

                # Afficher le geste
                cv2.putText(
                    frame,
                    f"{prediction} ({confidence:.1f}%)",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

                # Afficher le message
                cv2.putText(
                    frame,
                    message,
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 0, 0),
                    2
                )

                # ==================================
                # 9. Text-to-Speech
                # ==================================

                if confidence >= CONFIDENCE_THRESHOLD:

                    if prediction != last_gesture:

                        print("Gesture:", prediction)
                        print("Message:", message)

                        voice_queue.put(message)

                        last_gesture = prediction

        else:

            cv2.putText(
                frame,
                "No Hand Detected",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 0, 255),
                2
            )

            # Reinitialiser pour permettre
            # de prononcer le meme geste apres retrait de la main
            last_gesture = None

        # Afficher la webcam
        cv2.imshow(
            "AI Hand Gesture to Voice Converter",
            frame
        )

        # Quitter avec Q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:

    # ==========================================
    # 10. Liberer les ressources
    # ==========================================

    cap.release()

    hands.close()

    cv2.destroyAllWindows()

    voice_queue.put(None)
    voice_thread.join(timeout=3)

    print("Program stopped.")
