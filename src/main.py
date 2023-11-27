from recorder import recorder
from transcribe import transcribe
from translate import translater

recorder()
text = transcribe()
textTranslated = translater(text)

print(textTranslated)