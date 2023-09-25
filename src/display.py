from flask import Flask
import socket

app = Flask(__name__)

# Get the container's hostname, which is unique for each instance
hostname = socket.gethostname()

@app.route("/")
def hello():
    # Use the hostname as a unique identifier
    return f"Hello from Confidential ACI Instance with Hostname: {hostname}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
