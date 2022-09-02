from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def all_candidate():
    return f"<pre>{get_all()}</pre>"


@app.route("/candidates/<int:pk>")
def candidates_by_pk_page(pk):
    return f"<pre>{get_by_pk(pk)}</pre>"


@app.route("/skills/<skill>/")
def candidates_by_skill_page(skill):
    return f"<pre>{get_by_skill(skill)}</pre>"


if __name__ == '__main__':
    app.run()
