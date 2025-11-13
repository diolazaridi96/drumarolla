from fastapi import FastAPI, UploadFile, File
import subprocess, os

app = FastAPI()

@app.post("/separate")
async def separate(file: UploadFile = File(...)):
    input_path = f"/tmp/{file.filename}"
    output_dir = "/tmp/output"
    os.makedirs(output_dir, exist_ok=True)

    # Сохраняем файл
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Запускаем spleeter
    try:
        subprocess.run(
            ["spleeter", "separate", "-i", input_path, "-o", output_dir],
            check=True
        )
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

    return {"status": "ok", "output": output_dir}
