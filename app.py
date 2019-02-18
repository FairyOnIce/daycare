from flask import Flask, render_template
import sqlite3 as sql
from prepare_data import TABLENAME

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html", name="working mom")


@app.route("/daycare_table")
def main(name):
    return render_template("main.html",name=name)




@app.route("/hello/<string:name>")
def daycare_table(name):
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from {}".format(TABLENAME))

    rows = cur.fetchall();
    column_names = rows[0].keys()
    return render_template("main.html", name=name,rows=rows, column_names=column_names)



if __name__ == "__main__":
    app.run(debug=True)