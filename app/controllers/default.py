from app import app
from redis import Redis


redis = Redis(host='redis', port=6379)

""" Sobrescreve função,
    Ou seja, @app.route() sobrescreve index()
"""


@app.route("/")
@app.route("/index")
def index():
    redis.incr("hits")
    return "Flask is Fun %s time(s)" % redis.get("hits")


@app.route("/welcome", defaults={'name': None})
@app.route("/welcome/<name>")
def welcome(name):
    if name :
        return "Welcome, %s" % name
    else:
        return "Welcome!"

