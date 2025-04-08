```markdown
# Ollama LLM Lab (Docker + Flask)

This project provides a lightweight local LLM (Large Language Model) lab, connecting a simple Flask API running in a Docker container on a virtual machine (VM) to an Ollama server running on the host machine. This setup allows you to send prompts to a local LLM using Docker with minimal configuration.

---

## Project Structure

```
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
```

---

## Prerequisites

- **Host Machine:**
  - [Ollama](https://ollama.com) installed and running:
    ```bash
    ollama serve
    ```
  - Ensure Ollama is accessible from the VM. Typically, the host can be reached at `192.168.64.1` from the VM when using UTM on macOS.

- **Virtual Machine (VM):**
  - Docker installed:
    ```bash
    sudo apt update
    sudo apt install docker.io
    ```
  - Docker Compose plugin:
    ```bash
    sudo apt install docker-compose-plugin
    ```

---

## Quickstart Guide

1. **Start Ollama on the Host Machine:**

   On your host machine:

   ```bash
   ollama serve
   ```

2. **Clone the Repository on the VM:**

   ```bash
   git clone https://github.com/Lona44/ollama-lab-repo.git
   cd ollama-lab-repo/llm-app
   ```

3. **Configure Environment Variables:**

   Edit the `.env` file:

   ```env
   OLLAMA_URL=http://192.168.64.1:11434
   ```

   > To find the host IP from the VM:
   ```bash
   ip route | grep default
   ```

4. **Start the Flask API in Docker:**

   ```bash
   docker compose up --build
   ```

5. **Test the API:**

   ```bash
   curl -X POST http://localhost:5050/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What is 2 + 2?"}'
   ```

---

## Notes

- Ensure the Ollama server is running on the host machine and accessible from the VM.
- Modify `.env` if your host IP is different.
- If you hit Docker permission issues on the VM:

  ```bash
  sudo usermod -aG docker $USER
  ```

  Then log out and back in.

---

This setup provides a clean architecture for working with local LLMs in isolated environments. Perfect for training, testing, or teaching. If you run into any issues, open an issue on GitHub.

---
```
