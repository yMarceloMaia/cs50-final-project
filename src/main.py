from recorder import recorder
from transcribe import transcribe
from translate import translater
from text_to_speech import text_to_speech
from text_to_speech_ai import text_to_speech_ai


def recorder_and_translate_audio():
    recorder()
    text = transcribe()
    textTranslated = translater(text)
    text_to_speech_ai(textTranslated.text)
     
