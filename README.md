# 🧪 Ollama LLM Lab (Docker + Flask)

This project is a lightweight local LLM lab that connects a simple Flask API to a locally running [Ollama](https://ollama.com/) server (e.g. using Mistral). It lets you send prompts to a local LLM using Docker, with minimal setup.

---

## 🏗️ Project Structure

```
ollama-llm-lab/
│
├── llm-app/
│   ├── app.py              # Flask API code
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Flask container image
│
├── docker-compose.yml      # Spins up the Flask API
└── README.md               # You're reading it
```

---

## 🚀 Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Ollama](https://ollama.com/) installed locally  
  *(run `ollama serve` to start the server)*

---

## 🧪 Quickstart (Test Locally First)

1. **Start Ollama:**

   In a dedicated terminal:
   ```bash
   ollama serve
   ```

2. **Pull your model (e.g. Mistral):**

   Only needs to be done once:
   ```bash
   ollama pull mistral
   ```

3. **Start the Flask API via Docker Compose:**

   In your project folder:
   ```bash
   docker compose up --build
   ```

4. **Test the endpoint:**

   In a new terminal:
   ```bash
   curl -X POST http://localhost:5050/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What is 2 + 2?"}'
   ```

   ✅ You should get a valid LLM response like:
   ```json
   {"message":{"role":"assistant","content":"2 + 2 equals 4."}, ...}
   ```

---

## 🔁 How It Works

- Flask handles `/chat` requests.
- It sends your message to `http://host.docker.internal:11434/api/chat`.
- Ollama processes it using the `mistral` model.
- Flask returns the LLM's response to you.

---

## 🛑 To Stop Everything

```bash
docker compose down
```

To clean everything:
```bash
docker system prune -a
```

---

## 🤖 Example Payload

```bash
curl -X POST http://localhost:5050/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a joke"}'
```

---
