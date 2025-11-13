from flask import Flask, request, send_file, jsonify
import requests
import os

app = Flask(__name__)

SPLEETER_URL = "http://spleeter:6000/separate"

@app.route("/separate", methods=["POST"])
def separate_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    files = {"file": (file.filename, file.read())}

    # Отправляем файл в контейнер Spleeter
    resp = requests.post(SPLEETER_URL, files=files)
    if resp.status_code != 200:
        return jsonify({"error": "Spleeter failed"}), 500

    # Сохраняем возвращённый файл
    output_path = "/tmp/vocals.wav"
    with open(output_path, "wb") as f:
        f.write(resp.content)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


