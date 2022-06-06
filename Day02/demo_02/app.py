from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Flask</h1> <br><h2>第二標題</h2>"

@app.route("/error")
def error():
    raise RuntimeError

if __name__ == "__main__":
    app.run(debug=True)