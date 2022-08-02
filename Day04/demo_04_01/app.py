# app.py

from flask import Flask, render_template
from flask import request, json, jsonify, send_file

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import sqlalchemy
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 由Heroku得到的連結網址是： mysql://spy1hmjzgmohf37t:qo1v8pi7y4kflyoj@wb39lt71kvkgdmw0.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/qm1f2chzljeztwqj
# 我們在Python中使用時，需要調整一下，讓sqlalchemy知道我們指定使用的mysql driver是用哪一套
mysql_db_url = 'mysql+pymysql://spy1hmjzgmohf37t:qo1v8pi7y4kflyoj@wb39lt71kvkgdmw0.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/qm1f2chzljeztwqj'
my_db = create_engine(mysql_db_url)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", title="", name=name)


@app.route('/score', methods=['GET'])
def score_get():
    try:
        sql_cmd_str = "select * from score_table_0802"
        resultProxy = my_db.execute(sql_cmd_str)
        db_data_all = resultProxy.fetchall()
        my_data = dict()
        for item in db_data_all:
            name = item['name']
            score = item['score']
            my_data[name] = score

        return jsonify({'result':'OK', 'data':my_data})

    except Exception as e:
        print('--> exception: ' + str(e))
        return jsonify({'result':'NG', 'log':str(e)})

@app.route('/score/chart', methods=['GET'])
def score_chart():

    # select
    table_name = 'score_table_0802'
    sql_cmd_str = "select * from %s" %(table_name)
    resultProxy=my_db.execute(sql_cmd_str)
    data = resultProxy.fetchall()

    name_list = []
    score_list = []
    for item in data:
        name_list.append(item['name'])
        score_list.append(item['score'])

    # plot
    plt.bar(name_list, score_list)
    plt.xlabel('name')
    plt.ylabel('score')
    plt.grid()
    plt.savefig('img.png')
    plt.close()
    return send_file('img.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, port=8000)