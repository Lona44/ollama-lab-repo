# 🧪 Ollama Lab Environment (Localhost API + Remote Ollama)

This is a pre-built lab environment for students to learn and test LLM prompt behavior, logging, and security analysis.

---

## ⚙️ About the Setup

- **Flask API** runs inside a Linux VM (Dockerized)
- **Ollama LLM server** runs on the **host machine** (e.g., your Mac)
- **Requests** are proxied from VM to host
- **Logs** are saved in the VM and automatically rotated via `logrotate`

> 🛠️ *The VM is still being finalized and will be shared soon as a downloadable image for students to import and use directly.*

---

## 💻 Host Setup (macOS)

### 1. Install Ollama

Install via [https://ollama.com](https://ollama.com) or use Homebrew:

```bash
brew install ollama
```

### 2. Run Ollama on all interfaces

```bash
OLLAMA_HOST=0.0.0.0 ollama serve
```

This allows your VM to send requests to your Mac on port `11434`.

---

## 🖥️ VM Setup (When Shared)

1. Clone this repo inside the VM:

```bash
git clone https://github.com/Lona44/ollama-lab-repo.git
cd ollama-lab-repo/llm-app
```

2. Edit the `.env` file:

```env
OLLAMA_URL=http://<host-ip>:11434
```

> Replace `<host-ip>` with your Mac's IP **from the VM’s perspective**, e.g. `192.168.64.1`.

3. Run the Flask API:

```bash
docker compose up --build
```

---

## 🔁 Log Files

All requests and responses are logged to:

```
/var/log/llm-api.log
```

Sample log entry:

```
2025-04-09 01:38:00,730 INFO REQUEST from 172.20.0.1 - message: Who is Jacinda Ardern?
2025-04-09 01:38:05,278 INFO RESPONSE to 172.20.0.1 - status: 200, body: {...}
```

---

## 🔃 Log Rotation (Systemd Managed)

- Log file is rotated automatically **once per day** by `logrotate.timer`
- Rotation settings are configured in:

```
/etc/logrotate.d/llm-api
```

You can manually rotate logs with:

```bash
rotate-logs
```

> *(This is an alias preconfigured in the VM for convenience)*

---

## 📬 Making a Test Request

```bash
curl -X POST http://localhost:5050/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the capital of France?"}'
```

You’ll receive a JSON response and it will be logged in `/var/log/llm-api.log`.

---

## ✅ Summary

This setup is designed to expose students to:

- Containerized API development  
- Real-time LLM interaction and logging  
- Clean separation between LLM backend and frontend  
- Security visibility and future SIEM/EDR integration

> ⚠️ The full VM image with Docker, logging, aliases, and config files will be shared soon. Stay tuned!
