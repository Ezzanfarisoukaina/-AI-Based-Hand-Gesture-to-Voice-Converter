
import cv2
import mediapipe as mp

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configuration du detecteur
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam")
    exit()

print("Detection des mains demarree !")
print("Appuie sur Q pour quitter.")

while True:
    success, frame = cap.read()

    if not success:
        print("Erreur de lecture")
        break

    frame = cv2.flip(frame, 1)

    # Convertir BGR vers RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detecter les mains
    results = hands.process(rgb_frame)

    # Dessiner les landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

        cv2.putText(
            frame,
            "Hand Detected!",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:
        cv2.putText(
            frame,
            "No Hand Detected",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow("AI Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberer les ressources
cap.release()
hands.close()
cv2.destroyAllWindows()
