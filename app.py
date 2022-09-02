from flask import Flask
from utils import *

# create apllication
app = Flask(__name__)


# create page with all candidates
@app.route("/")
def all_candidate():
    return f"<pre>{get_all()}</pre>"


# create page with candidates by pk
@app.route("/candidates/<int:pk>")
def candidates_by_pk_page(pk):
    return f"<pre>{get_by_pk(pk)}</pre>"


# create page with all candidates by skills
@app.route("/skills/<skill>/")
def candidates_by_skill_page(skill):
    return f"<pre>{get_by_skill(skill)}</pre>"


if __name__ == '__main__':
    #run app
    app.run()
