from flask import Flask, request, jsonify
import subprocess, os

app = Flask(__name__)

@app.route("/separate", methods=["POST"])
def separate():
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400

    file = request.files["file"]
    input_path = f"/tmp/{file.filename}"
    output_dir = "/tmp/output"
    os.makedirs(output_dir, exist_ok=True)
    file.save(input_path)

    try:
        subprocess.run(
            ["spleeter", "separate", "-i", input_path, "-o", output_dir],
            check=True
        )
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "ok", "output": output_dir})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

