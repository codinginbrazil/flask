from redis import Redis
from flask import render_template
from app import app
from app.models.forms import LoginForm


redis = Redis(host='redis', port=6379)

""" Sobrescreve função,
    Ou seja, @app.route() sobrescreve index()
"""


@app.route("/")
def index():
    redis.incr("hits")
    return render_template('index.html')


@app.route("/index/", defaults={'user': None})
@app.route("/index/<user>")
def user(user):
    redis.incr("hits")
    return render_template('index.html', user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    redis.incr("hits")
    form = LoginForm()
    if form.validate_on_submit(): 
        return "Welcome"
    else: 
        return render_template('login.html', form=form)


@app.route("/welcome", defaults={'name': None})
@app.route("/welcome/<name>")
def welcome(name):
    redis.incr("hits")
    if name:
        return "Welcome, %s" % name
    else:
        return "Welcome! %s time(s)" % redis.get("hits")
