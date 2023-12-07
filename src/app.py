from flask import Flask, render_template
from threading import Thread
import time
from principal import recorder_and_translate_audio
from recorder import recorder

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_recording')
def start_recording():
    try:
        recorder_and_translate_audio()
        return 'Recording finished.'
    except Exception as error:
        print(error)
        return 'error'
         

if __name__ == "__main__":
    app.run(debug=True)
