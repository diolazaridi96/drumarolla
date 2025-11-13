import spleeter
import librosa
import numpy as np

def process_audio_file(filepath):
    from spleeter.separator import Separator

    separator = Separator('spleeter:2stems')
    separator.separate_to_file(filepath, 'output')

    drums_path = f"output/{filepath.split('/')[-1].replace('.mp3', '')}/drums.wav"
    y, sr = librosa.load(drums_path)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

    return {"tempo": float(tempo), "beats": beats.tolist()}
