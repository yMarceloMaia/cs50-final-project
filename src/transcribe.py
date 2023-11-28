import speech_recognition as sr
# command install speech_recognition: pip install SpeechRecognition

def transcribe():
    # instanciando e limitando o threshold
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300

    audio = sr.AudioFile("output.wav")

    with audio as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio_data=audio, language="pt-BR")

    return text