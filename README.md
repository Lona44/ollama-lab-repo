# 🧪 Ollama LLM Pentest Lab – Fake AI Company Edition

This repo contains a Dockerized Flask API that simulates an internal endpoint of a fictional AI company using [Ollama](https://ollama.com) locally. It logs LLM chat requests/responses to `/var/log/llm-api.log` for analysis in SIEM tools like Wazuh.

This is part of a broader cybersecurity lab project to simulate realistic enterprise attack surfaces and blue team visibility for LLM security research.

---

## 🛠️ Current Setup

✅ **Ollama runs on the host**  
✅ **Flask app runs inside the VM via Docker Compose**  
✅ **Log file (`/var/log/llm-api.log`) is created and ready for SIEM ingestion**  
✅ **Logrotate is configured and triggered by systemd daily**

> 🔒 Logs include:
> - Source IP
> - Message sent to the LLM
> - Status code & full LLM response JSON
> - Errors (e.g., if Ollama is unreachable)

---

## 🚀 Quick Start

## 🧑‍🎓 For Students / Users

1. **Install Ollama on your host (Mac/Linux)**  
   👉 https://ollama.com/download  
   🧠 Recommended model: `mistral`  
   🛠️ Then run:

   ```bash
   OLLAMA_HOST=0.0.0.0 ollama serve
   ```

   > This makes sure the Flask app inside the VM can reach Ollama on your host machine.

2. **Update `.env` file with your host IP**
   ```env
   OLLAMA_URL=http://192.168.64.1:11434
   ```
   > This IP works by default for Mac + UTM Shared Network setups. Update it if needed.

3. **Run the Flask API inside the VM**
   ```bash
   git clone https://github.com/Lona44/ollama-lab-repo.git
   cd ollama-lab-repo/llm-app
   docker compose up --build
   ```

4. **Send a test prompt**
   ```bash
   curl -X POST http://localhost:5050/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What is the capital of France?"}'
   ```

5. **Check your logs**
   ```bash
   docker exec -it ollama-lab-repo-flask-api-1 cat /var/log/llm-api.log
   ```

---

## 🔁 Log Rotation

Logrotate is already set up with this config:
```bash
/etc/logrotate.d/llm-api
```

You can also trigger it manually:
```bash
rotate-logs
```
This is pre-aliased in `.bashrc` inside the VM.

---

## 🔭 Project Roadmap

This lab simulates a fake AI company’s environment to teach real-world offensive and defensive cybersecurity skills.

| Phase | Component              | Goal                                             | Status  |
|-------|------------------------|--------------------------------------------------|---------|
| ✅    | Flask API + Logging     | Generate meaningful LLM traffic and logs         | Done ✅ |
| 🔜    | SIEM (Wazuh)           | Centralize, parse, and alert on log activity     | Up Next |
| 🔜    | EDR (LimaCharlie)      | Monitor host-level activity and detections       | Soon    |
| 🔜    | AD + Windows VM        | Simulate identity attacks and detection          | Soon    |
| 🔜    | Frontend App           | Create an attackable web surface for the LLM     | Later   |
| 🔜    | Tines Integration      | Automate response and enrich alerts              | Later   |

➡️ A pre-configured Ubuntu VM with the API and logging is coming soon.

---

## 🧠 Why This Exists

The goal is to give cybersecurity students and professionals a **hands-on lab** with:
- Simulated enterprise architecture
- Real LLMs (no fake mocks)
- Defensive visibility + automation tools
- Red/blue/purple team use cases

---

## 📬 Coming Soon

- [ ] Ubuntu VM export with everything pre-installed
- [ ] Walkthrough videos
- [ ] Sample attack + detection scenarios

---
MIT License | Created with ❤️ by @Lona44
