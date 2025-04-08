# Ollama LLM Pentest Lab

This lab allows you to simulate and test prompt injection attacks in a secure, isolated environment.  
It is built around a local LLM served by Ollama on the **host machine**, with all other services (Flask API, security tooling) running inside a **Ubuntu Server VM**.

---

## 🧠 Architecture Overview

- **Host (Student's Laptop)**
  - Ollama (running `mistral` or another supported model)
  - Accessible at `http://192.168.64.1:11434`

- **Virtual Machine (VM)**
  - Runs Flask API (receives prompts and sends to Ollama)
  - Includes Docker, Docker Compose, and room for expansion:
    - Wazuh (SIEM)
    - LimaCharlie (EDR)
    - Tines (SOAR)
  - VM network mode: **Host-only**, with access to `192.168.64.1` (host)

---

## 🚀 Getting Started

### ✅ Prerequisites

- Mac with UTM installed
- ARM-based Mac (M1/M2) recommended
- Docker installed on the VM
- Ollama installed and running on the **host** machine
- Network is set to **Host-only** in UTM so the VM can reach the host IP `192.168.64.1`

---

## 💾 Setup Instructions

### On Host (Mac)

1. Install [Ollama](https://ollama.com/download)
2. Run in terminal:
   ```bash
   ollama serve
   ollama run mistral
   ```

---

### On the VM

1. SSH into the VM:
   ```bash
   ssh lab_admin@192.168.64.3
   ```

2. Clone the repo:
   ```bash
   git clone https://github.com/Lona44/ollama-lab-repo.git
   cd ollama-lab-repo/llm-app
   ```

3. Create a `.env` file inside `llm-app/`:
   ```env
   OLLAMA_URL=http://192.168.64.1:11434
   ```

4. Build and run the Flask API:
   ```bash
   docker compose up --build
   ```

---

## 🧪 Test it out!

Send a prompt to the Flask API running in the VM, which will forward it to Ollama on the host:

```bash
curl -X POST http://localhost:5050/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is 2 + 2?"}'
```

---

## ⚠️ Troubleshooting

- If Docker gives `permission denied` errors:
  ```bash
  sudo usermod -aG docker lab_admin
  newgrp docker
  ```

- Ensure Ollama is running on the host **before** launching the Flask app in the VM

---

## 🛡️ What’s next?

You can now start building:

- Wazuh dashboards for prompt logging
- Tines workflows for LLM abuse detection
- LimaCharlie rules for outbound data exfiltration

---

## 🙌 Author

Built by [Lona44](https://github.com/Lona44)  
Designed for secure, offline, LLM pentest learning.
