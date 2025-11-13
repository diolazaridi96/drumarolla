from spleeter.separator import Separator
import librosa
import os

separator = Separator('spleeter:2stems')

def process_audio_file(filepath):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    separator.separate_to_file(filepath, output_dir)
    
    instrumental_path = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0], "accompaniment.wav")
    
    y, sr = librosa.load(instrumental_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    
    beat_times = librosa.frames_to_time(beats, sr=sr).tolist()
    
    return beat_times
