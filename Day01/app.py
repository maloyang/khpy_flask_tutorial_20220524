# -*- coding: utf-8 -*-

from flask import Flask, request, abort, render_template, Response

#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route("/", methods=['GET'])
def basic_url():
    return 'hello'


@app.route("/hello", methods=['GET'])
def hello():
    name = request.args.get('name')
    return 'hello ' + name


if __name__ == "__main__":
    app.run()
