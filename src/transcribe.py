import speech_recognition as sr

def transcribe():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300

    audio = sr.AudioFile("output.wav")

    with audio as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio_data=audio, language="pt-BR")
    return text