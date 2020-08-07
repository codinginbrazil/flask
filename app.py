from redis import Redis
from flask import Flask

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

""" Sobrescreve função,
    Ou seja, @app.route() sobrescreve index()
"""


@app.route("/")
def index():
    redis.incr('hits')
    return "Flask is Fun %s time(s)" % redis.get("hits")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
