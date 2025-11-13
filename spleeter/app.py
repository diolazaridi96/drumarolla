from flask import Flask, request, send_file, jsonify
from spleeter.separator import Separator
import os

app = Flask(__name__)
separator = Separator('spleeter:2stems')

UPLOAD_FOLDER = "/tmp/input"
OUTPUT_FOLDER = "/tmp/output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/separate", methods=["POST"])
def separate_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_dir = os.path.join(OUTPUT_FOLDER, os.path.splitext(file.filename)[0])
    file.save(input_path)

    separator.separate_to_file(input_path, output_dir)

    vocals_path = os.path.join(output_dir, "vocals.wav")
    if not os.path.exists(vocals_path):
        return jsonify({"error": "Failed to separate"}), 500

    return send_file(vocals_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
