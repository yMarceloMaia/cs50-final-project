import pyaudio
import wave
import keyboard

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def recorder():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    frames = []
    print("Press 'space' to recorder")
    keyboard.wait("space")
    print("recording...")
    while True:
        if keyboard.is_pressed("space"):
            data = stream.read(CHUNK)
            frames.append(data)
        else:
            break

    pass
    print("recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("output.wav", "wb")
    wf.setnchannels(CHANNELS),
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()