# app.py

from flask import Flask, render_template
from flask import request, json, jsonify

import sqlalchemy
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 由Heroku得到的連結網址是： mysql://b7d32019179b11:6747e9d5@us-cdbr-east-05.cleardb.net/heroku_1fc10f81f51dcb9?reconnect=true
# 我們在Python中使用時，需要調整一下，讓sqlalchemy知道我們指定使用的mysql driver是用哪一套
mysql_db_url = 'mysql+pymysql://spy1hmjzgmohf37t:qo1v8pi7y4kflyoj@wb39lt71kvkgdmw0.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/qm1f2chzljeztwqj'
my_db = create_engine(mysql_db_url)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", title="", name=name)

@app.route('/score/insert', methods=['GET', 'POST'])
def score_insert():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({'result':'NG', 'log':'not name parameter'})

        score = request.args.get('score')
        if not name:
            return jsonify({'result':'NG', 'log':'not score parameter'})

        sql_cmd = "insert into table1 (name, score) values('%s', '%s') " %(
            name, score )

        resultProxy = my_db.execute(sql_cmd)
        return jsonify({'result':'OK', 'log': 'insert:(%s, %s)' %(name, score)})

    except Exception as e:
        print('--> exception: ' + str(e))
        return jsonify({'result':'NG', 'log':str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=8000)