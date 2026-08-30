from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Tyla Fan Support bot is running."

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "No authorization code received.", 400
    return "Authorization received successfully. You can close this page."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
