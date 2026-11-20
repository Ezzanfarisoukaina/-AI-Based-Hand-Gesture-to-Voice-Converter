import pyttsx3
import time

messages = [
    "Good!",
    "Victory!",
    "Hello!",
    "No!",
    "Everything is OK!"
]

for message in messages:

    print("Speaking:", message)

    engine = pyttsx3.init(driverName="sapi5")

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    engine.say(message)
    engine.runAndWait()

    engine.stop()
    del engine

    time.sleep(1)

print("All messages completed!")