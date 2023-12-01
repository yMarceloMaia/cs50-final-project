from recorder import recorder
from transcribe import transcribe
from translate import translater
from text_to_speech import text_to_speech

recorder()
text = transcribe()
textTranslated = translater(text)
text_to_speech(textTranslated.text)