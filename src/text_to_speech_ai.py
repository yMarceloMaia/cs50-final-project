import torch
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import wave

def text_to_speech_ai(text):
    print("Starting audio ai")
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    config = XttsConfig()
    config.load_json("D:\XTTS-v2/config.json")
    model = Xtts.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="D:\XTTS-v2", eval=True)
    # model.cuda(device)

    outputs = model.synthesize(
        text,
        config,
        speaker_wav="D:\CS50-FINAL-PROJECT/output.wav",
        gpt_cond_len=3,
        language="en",
    )

    wav_form = outputs["wav"]

    filename = "tts.wav"
    sample_rate = 23000
    sample_width = 2
    num_channels = 1

    wf = wave.open(filename, "wb")
    wf.setnchannels(num_channels)
    wf.setframerate(sample_rate)
    wf.setsampwidth(sample_width)

    max_amplitude = max(abs(wav_form))
    wav_form_normalized = wav_form / max_amplitude
    wav_form_int = (wav_form_normalized * 32767).astype('int16')
    wf.writeframes(wav_form_int.tobytes())

    wf.close()
    print("Audio ai finished")