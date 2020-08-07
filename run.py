from app import app
from redis import Redis


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
