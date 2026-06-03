from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "festival": "Pacific DevOps Music Fest",
        "fecha": "15 Agosto 2026",
        "artistas": [
            "Imagine Dragons",
            "Coldplay",
            "Martin Garrix",
            "David Guetta"
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)