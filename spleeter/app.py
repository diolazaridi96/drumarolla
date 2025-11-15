from flask import Flask, request, send_file, jsonify, render_template_string
from spleeter.separator import Separator
import os

app = Flask(__name__)
separator = Separator('spleeter:2stems')

UPLOAD_FOLDER = "/tmp/input"
OUTPUT_FOLDER = "/tmp/output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# HTML-форма для загрузки аудио через браузер
HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>Spleeter Web</title>
</head>
<body>
    <h2>Загрузите аудио для разделения на вокал и инструментал</h2>
    <form action="/separate" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="audio/*" required>
        <input type="submit" value="Отделить вокал">
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/separate", methods=["POST"])
def separate_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_dir = os.path.join(OUTPUT_FOLDER, os.path.splitext(file.filename)[0])
    file.save(input_path)

    try:
        separator.separate_to_file(input_path, output_dir)
    except Exception as e:
        return jsonify({"error": f"Separation failed: {str(e)}"}), 500

    vocals_path = os.path.join(output_dir, "vocals.wav")
    if not os.path.exists(vocals_path):
        return jsonify({"error": "Failed to separate"}), 500

    return send_file(vocals_path, as_attachment=True)

if __name__ == "__main__":
    # Используем порт, который предоставляет Railway
    port = int(os.environ.get("PORT", 6000))
    app.run(host="0.0.0.0", port=port)
