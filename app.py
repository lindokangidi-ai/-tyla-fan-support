import os
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Tyla Fan Support is online."


@app.route("/health")
def health():
    return "OK"


@app.route("/test")
def test():
    token = os.environ.get("X_ACCESS_TOKEN")

    if not token:
        return "X_ACCESS_TOKEN is missing from Render.", 500

    response = requests.get(
        "https://api.x.com/2/users/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=30
    )

    return (
        f"X connection status: {response.status_code}<br>"
        f"Response: {response.text}"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
