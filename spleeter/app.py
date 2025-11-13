from flask import Flask, request, jsonify
from spleeter.separator import Separator
import os

app = Flask(__name__)
separator = Separator('spleeter:2stems')

@app.route("/separate", methods=["POST"])
def separate():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio = request.files['file']
    filename = audio.filename
    input_path = f"/app/input/{filename}"
    output_path = f"/app/output/{filename}"

    os.makedirs("/app/input", exist_ok=True)
    os.makedirs("/app/output", exist_ok=True)

    audio.save(input_path)
    separator.separate_to_file(input_path, "/app/output")

    return jsonify({"message": f"File processed: {filename}"}), 200

@app.route("/", methods=["GET"])
def home():
    return "✅ Spleeter API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
