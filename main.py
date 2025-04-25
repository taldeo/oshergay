import socket
from flask import Flask
hostpc = socket.gethostname()

app = Flask(__name__)
@app.route("/")
def home():
    return f"Hello from {hostpc}"
@app.route("/about")
def about():
    return f"osher is gay"
app.run(host="0.0.0.0", port=5000, debug=True)