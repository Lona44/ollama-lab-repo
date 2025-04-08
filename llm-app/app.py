import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://192.168.64.1:11434")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": "mistral",
                "messages": [{"role": "user", "content": message}],
                "stream": False
            }
        )
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
