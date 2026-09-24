import json
import os
from http.server import BaseHTTPRequestHandler

from google import genai


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}")
            message = (body.get("message") or "").strip()
            history = body.get("history") or []
            api_key = os.environ.get("GEMINI_API_KEY", "")

            if not message:
                self._send(400, {"error": "Empty message"})
                return
            if not api_key:
                self._send(500, {"error": "GEMINI_API_KEY is not set"})
                return

            contents = []
            for item in history:
                role = "model" if item.get("role") == "assistant" else "user"
                text = item.get("content") or ""
                if text:
                    contents.append({"role": role, "parts": [{"text": text}]})
            contents.append({"role": "user", "parts": [{"text": message}]})

            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=contents,
            )
            self._send(200, {"reply": response.text or ""})
        except Exception as e:
            self._send(500, {"error": str(e)})

    def _send(self, status, payload):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))
