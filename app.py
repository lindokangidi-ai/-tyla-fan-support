import os
import requests
from flask import Flask

app = Flask(__name__)


def get_token():
    return "".join(
        os.environ.get("X_ACCESS_TOKEN", "").split()
    )


@app.route("/")
def home():
    return "Tyla Fan Support is online."


@app.route("/health")
def health():
    return "OK"


@app.route("/test")
def test():
    token = get_token()

    if not token:
        return "X_ACCESS_TOKEN is missing from Render.", 500

    try:
        response = requests.get(
            "https://api.x.com/2/users/me",
            headers={
                "Authorization": "Bearer " + token
            },
            timeout=30
        )

        return (
            "X connection status: "
            + str(response.status_code)
            + "<br>Response: "
            + response.text
        )

    except Exception as error:
        return "Connection error: " + str(error), 500


@app.route("/post")
def post():
    token = get_token()

    if not token:
        return "X_ACCESS_TOKEN is missing from Render.", 500

    try:
        response = requests.post(
            "https://api.x.com/2/tweets",
            headers={
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"
            },
            json={
                "text": "Tyla Fan Support is officially online! 💗🔥"
            },
            timeout=30
        )

        return (
            "X post status: "
            + str(response.status_code)
            + "<br>Response: "
            + response.text
        )

    except Exception as error:
        return "Posting error: " + str(error), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
