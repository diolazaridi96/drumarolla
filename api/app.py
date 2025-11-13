from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/separate', methods=['POST'])
def separate():
    filename = request.json.get('filename')
    # предполагаем, что audio лежит в /audio
    subprocess.run([
        'docker', 'run', '--rm',
        '-v', f'{os.getcwd()}/audio:/input',
        '-v', f'{os.getcwd()}/separated:/output',
        'spleeter:2.4.2',
        'separate', '-i', f'/input/{filename}', '-p', 'spleeter:2stems', '-o', '/output'
    ])
    return jsonify({'status': 'done'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

