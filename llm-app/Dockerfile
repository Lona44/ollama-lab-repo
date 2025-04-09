FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY context.txt .

RUN mkdir -p /var/log && touch /var/log/llm-api.log

CMD ["python", "app.py"]
