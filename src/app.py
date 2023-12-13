from flask import Flask, render_template, jsonify, send_file
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
        return "True"
    except Exception as error:
        print(error)
        return 'error'
         

@app.route('/get_audio', methods=['GET'])
def get_audio():
    try:
        # Lógica para gerar ou obter o arquivo de áudio
        # Neste exemplo, estamos retornando um arquivo estático de exemplo
        audio_path = 'D:\cs50-final-project/tts.wav'

        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        return f'Erro ao obter o arquivo de áudio: {str(e)}', 500

if __name__ == "__main__":
    app.run(debug=True)
