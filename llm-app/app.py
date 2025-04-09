from flask import Flask, request, jsonify
import requests
import logging
import os

app = Flask(__name__)

# Load Ollama URL from environment variable or default to host machine IP
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://192.168.64.1:11434")

# Load internal context (simulating a vulnerability)
CONTEXT_FILE = "context.txt"
SYSTEM_CONTEXT = ""
if os.path.exists(CONTEXT_FILE):
    with open(CONTEXT_FILE, "r") as f:
        SYSTEM_CONTEXT = f.read()

# Redact sensitive lines unless ADMIN_DEBUG_ACCESS is present
def get_filtered_context(user_message):
    if "ADMIN_DEBUG_ACCESS" not in user_message:
        redacted = "\n".join([
            line for line in SYSTEM_CONTEXT.splitlines()
            if not any(secret in line for secret in ["JWT", "FLAG", "DO_NOT_DISCLOSE_THIS", "ADMIN_PASSWORD"])
        ])
        return redacted
    return SYSTEM_CONTEXT

# Configure logging
LOG_FILE = "/var/log/llm-api.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    ip = request.remote_addr

    logging.info(f"REQUEST from {ip} - message: {message}")

    try:
        filtered_context = get_filtered_context(message)

        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": "mistral",
                "messages": [
                    {"role": "system", "content": filtered_context},
                    {"role": "user", "content": message}
                ],
                "stream": False
            }
        )
        json_response = response.json()
        logging.info(f"RESPONSE to {ip} - status: {response.status_code}, body: {json_response}")
        return jsonify(json_response)
    except requests.exceptions.RequestException as e:
        logging.error(f"ERROR from {ip} - {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
