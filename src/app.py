from flask import Flask, render_template, jsonify, send_file
from main import recorder_and_translate_audio

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
        audio_path = 'D:\cs50-final-project/tts.wav'
        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        return f'Erro ao obter o arquivo de áudio: {str(e)}', 500

if __name__ == "__main__":
    app.run(debug=True)
