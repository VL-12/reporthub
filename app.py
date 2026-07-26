from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "ReportHub версия ONE + TWO"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
