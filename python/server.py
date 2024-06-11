import time
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def index():
    time.sleep(2)
    t = int(time.time() * 1000)
    print(t)
    return f"Hello, Python {t}"


fast = False


@app.route("/slow/<slow_seconds>")
@app.route("/slow/")
def slow(slow_seconds=20):
    print(f"slow request received , sleeping {slow_seconds} seconds")
    time.sleep(5)
    print(f"response sent after {slow_seconds} seconds")
    return f"Slow response after {slow_seconds} seconds"


@app.route("/fast/")
def fast():
    print("returning fast response")
    return "returning fast response"


if __name__ == "__main__":
    app.run(debug=True)
