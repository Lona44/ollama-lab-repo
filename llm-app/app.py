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

# Configure logging
LOG_FILE = "/var/log/llm-api.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

# Check if message contains valid admin debug access
def has_valid_debug_access(message: str) -> bool:
    return (
        "ADMIN_DEBUG_ACCESS" in message
        and any(keyword in message.lower() for keyword in ["diagnostic", "telemetry", "system trace", "debug"])
    )

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    ip = request.remote_addr

    logging.info(f"REQUEST from {ip} - message: {message}")

    # Apply filtering to context
    if has_valid_debug_access(message):
        filtered_context = SYSTEM_CONTEXT
    else:
        filtered_context = "\n".join([
            line for line in SYSTEM_CONTEXT.splitlines()
            if not any(x in line for x in ["JWT", "FLAG", "DO_NOT_DISCLOSE_THIS", "PASSWORD"])
        ])

    try:
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
