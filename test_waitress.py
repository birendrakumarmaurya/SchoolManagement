from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    return "Waitress is working!"

if __name__ == "__main__":
    print("Serving with Waitress at http://0.0.0.0:80")
    serve(app, host="0.0.0.0", port=80)
