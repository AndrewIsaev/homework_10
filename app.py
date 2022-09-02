from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def all_candidate():
    return f"<pre>{get_all()}</pre>"


@app.route("/candidates/<int:pk>")
def candidates_by_pk_page(pk):
    return f"1{get_by_pk(pk)}"


@app.route("/skills/<skill>/")
def candidates_by_skill_page(skill):
    return f"<pre>1{get_by_skill(skill)}</pre>"


@app.route("/asd")
def a():
    return "fdsga"
if __name__ == '__main__':
    app.run()
