from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def all_candidate():
    return f"<pre>{get_all()}</pre>"


if __name__ == '__main__':
    app.run()
