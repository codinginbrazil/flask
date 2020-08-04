from flask import Flask


app = Flask(__name__)

""" Sobrescreve função,
    Ou seja, @app.route() sobrescreve index()
"""


@app.route("/")
def index():
    return "Flask is Fun"


if __name__ == "__main__":
    app.run()
