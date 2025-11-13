import imageio_ffmpeg as ffmpeg
import os
from flask import Flask, request, jsonify
from scripts.process_audio import process_audio_file

# Добавляем ffmpeg в PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg.get_ffmpeg_exe())

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    os.makedirs("uploads", exist_ok=True)
    filepath = f"uploads/{file.filename}"
    file.save(filepath)
    beatmap = process_audio_file(filepath)
    return jsonify({"beatmap": beatmap})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
