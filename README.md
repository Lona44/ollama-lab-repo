Ollama LLM Lab (Docker + Flask)
This project provides a lightweight local LLM (Large Language Model) lab, connecting a simple Flask API running in a Docker container on a virtual machine (VM) to an Ollama server running on the host machine. This setup allows you to send prompts to a local LLM using Docker with minimal configuration.

Project Structure
bash
Copy
Edit
ollama-llm-lab/
│
├── llm-app/
│   ├── app.py              # Flask API code
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Flask container image
│   └── .env                # Environment variables
│
├── docker-compose.yml      # Spins up the Flask API
└── README.md               # You're reading it
Prerequisites
On the Host Machine:
Ollama installed and running:

bash
Copy
Edit
ollama serve
Ollama must be accessible from the VM. When using UTM on macOS, the host is usually accessible via:

cpp
Copy
Edit
http://192.168.64.1:11434
On the Virtual Machine:
Docker installed:

bash
Copy
Edit
sudo apt update
sudo apt install docker.io
Docker Compose plugin:

bash
Copy
Edit
sudo apt install docker-compose-plugin
Quickstart Guide
Start Ollama on the Host Machine

bash
Copy
Edit
ollama serve
Clone This Repository on the VM

bash
Copy
Edit
git clone https://github.com/Lona44/ollama-lab-repo.git
cd ollama-lab-repo/llm-app
Create or Edit the .env File

Inside the llm-app folder, create a .env file with this line:

ini
Copy
Edit
OLLAMA_URL=http://192.168.64.1:11434
To verify the correct host IP, run this on the VM:

bash
Copy
Edit
ip route | grep default
Run the Flask API

bash
Copy
Edit
docker compose up --build
Send a Test Prompt

bash
Copy
Edit
curl -X POST http://localhost:5050/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is 2 + 2?"}'
Troubleshooting
Docker permission denied?

bash
Copy
Edit
sudo usermod -aG docker $USER
Then log out and log back in.

Ollama connection error?
Ensure it's running on your host and the .env IP is correct.

Why This Setup?
This separation allows:

Full resource usage of the host (e.g., GPU for Ollama)

Safe, sandboxed experimentation in the VM

Easier sharing of a standardized VM environment with others
