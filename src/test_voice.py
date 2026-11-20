import pyttsx3

# Initialisation du moteur vocal
engine = pyttsx3.init()

# Configuration de la voix
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Test vocal
engine.say("Hello! Welcome to AI Hand Gesture to Voice Converter.")

# Exécution
engine.runAndWait()