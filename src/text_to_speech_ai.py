import torch
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import wave

device = "cuda" if torch.cuda.is_available() else "cpu"

config = XttsConfig()
config.load_json("C:/Users/yuzo/Downloads/cs50/XTTS-v2/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="C:/Users/yuzo/Downloads/cs50/XTTS-v2", eval=True)
model.cuda(device)

outputs = model.synthesize(
    "It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
    config,
    speaker_wav="C:/Users/yuzo/Downloads/cs50/XTTS-v2/samples/en_sample.wav",
    gpt_cond_len=3,
    language="en",
)

wav_form = outputs["wav"]

filename = "tts.wav"
sample_rate = 22050
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