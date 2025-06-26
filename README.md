
# Komiko MicroAPI

A lightweight, developer-friendly REST API scaffold by [Komiko Labs](https://komikolabs.com/). It’s designed to be instantly useful for testing, prototyping, and educational purposes — no database, no complexity, just clean, modular endpoints.


---

## 🔧 Features

This API includes 6 practical endpoints, all stateless and ready out of the box:

### `/status`
Returns server uptime and current UTC time.
```json
{
  "status": "online",
  "uptime_seconds": 452,
  "server_time_utc": "2025-06-25T20:45:30Z"
}
```

---

### `/echo`
Send it JSON, get it right back. Useful for debugging clients.

**Request:**
```bash
POST /echo
{
  "message": "hello"
}
```

**Response:**
```json
{
  "you_sent": {
    "message": "hello"
  },
  "timestamp": "2025-06-25T20:45:30Z"
}
```

---

### `/whoami`
Returns your IP address, user agent, and request headers.

```json
{
  "ip": "127.0.0.1",
  "user_agent": "Mozilla/5.0...",
  "headers": {
    "accept": "*/*",
    "host": "localhost:8000"
  }
}
```

---

### `/random`
Returns a fresh UUID, a random number, and a short phrase.

```json
{
  "uuid": "e6e0d9f7-9af8-4b7e-bf3d-2a1c1bcd8cb2",
  "number": 73,
  "phrase": "Design it. Build it. Test it. Break it.",
  "timestamp": "2025-06-25T20:45:30Z"
}
```

---

### `/hash`
Returns the MD5 and SHA-256 hash of any input string.

**Request:**
```bash
POST /hash
{
  "input": "komiko"
}
```

**Response:**
```json
{
  "md5": "e2163e6b87cf921e4bb6a3c51be1020f",
  "sha256": "b6b78c8fc24a5098d6a29e960fd87fcf0f27d22ac816d4202090dc84464cb29b"
}
```

---

### `/timestamp`
Returns current UTC time and Unix timestamp.

```json
{
  "utc": "2025-06-25T20:45:30Z",
  "unix": 1750879530
}
```

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/komikolabs/komiko-microapi.git
cd komiko-microapi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the API:
```bash
uvicorn main:app --reload
```

4. Visit:
- Docs UI: http://localhost:8000/docs
- Example: http://localhost:8000/status

---

## 📦 Dependencies

- FastAPI
- Uvicorn

Optional: use [HTTPie](https://httpie.io/) or `curl` to send requests from the command line.

---

## 📄 License

MIT License — free to use, fork, or build on with attribution.  
© 2025 Komiko Labs
