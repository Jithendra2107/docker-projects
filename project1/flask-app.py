from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Learning Project</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
            width: 500px;
        }

        h1 {
            color: #4f46e5;
        }

        .info {
            margin-top: 20px;
            font-size: 18px;
        }

        .label {
            font-weight: bold;
            color: #333;
        }

        .value {
            color: #16a34a;
        }

        .footer {
            margin-top: 20px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Docker Learning Project</h1>

        <div class="info">
            <span class="label">Hostname:</span>
            <span class="value">{{ hostname }}</span>
        </div>

        <div class="info">
            <span class="label">Environment:</span>
            <span class="value">{{ environment }}</span>
        </div>

        <div class="footer">
            Flask + Docker Demo
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        hostname=socket.gethostname(),
        environment=os.getenv("ENV", "local")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
