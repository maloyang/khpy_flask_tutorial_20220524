
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello flask</h1>"

#-- new add below

@app.route("/user/<name>")
def get_user_name(name):
    return "<h1>Hello, %s!</h1>" %(name)

@app.route("/user/<int:uid>")
def get_user_id(uid):
    if isinstance(uid, int):
        return "<h1>Your ID: %s</h1>" %(uid)
    return "<h1>ID should be int</h1>"

@app.route("/user/<path:path>")
def get_user_path(path):
    return "<h1>Path: %s</h1>" %(path)

if __name__ == "__main__":
    app.run(debug=True, port=8000)