
# Dictionnaire de correspondance entre les gestes et les phrases

GESTURE_MESSAGES = {
    "THUMB_UP": "Good!",
    "OPEN_PALM": "Hello!",
    "FIST": "No!",
    "PEACE": "Victory!",
    "OK": "Everything is OK!"
}


def get_message(gesture):
    """
    Convertir le nom du geste en message.
    """

    return GESTURE_MESSAGES.get(
        gesture,
        "Gesture not recognized"
    )


# Test du Text Mapping
if __name__ == "__main__":

    gestures = [
        "THUMB_UP",
        "OPEN_PALM",
        "FIST",
        "PEACE",
        "OK"
    ]

    for gesture in gestures:
        message = get_message(gesture)

        print(gesture, "---->", message)
