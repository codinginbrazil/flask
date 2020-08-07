from app import app
from redis import Redis


redis = Redis(host='redis', port=6379)

""" Sobrescreve função,
    Ou seja, @app.route() sobrescreve index()
"""


@app.route("/")
def index():
    redis.incr("hits")
    return "Flask is Fun %s time(s)" % redis.get("hits")
