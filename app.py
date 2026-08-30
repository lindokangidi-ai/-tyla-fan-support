import os
from flask import Flask
import requests

app = Flask(__name__)

X_ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")

@app.route("/")
def home():
    return "Tyla Fan Support bot is running."

@app.route("/test")
def test_post():
    if not X_ACCESS_TOKEN:
        return "X_ACCESS_TOKEN is not configured.", 500

    response = requests.post(
        "https://api.x.com/2/tweets",
        headers={
            "Authorization": f"Bearer {X_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "text": "Tyla Fan Support is now online! 💗"
        },
        timeout=30
    )

    if response.status_code == 201:
        return "Test post published successfully! 🎉"

    return f"X API error: {response.status_code} - {response.text}", 500


@app.route("/callback")
def callback():
    return "OAuth callback endpoint is running."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
