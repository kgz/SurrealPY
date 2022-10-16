from urllib import request

from flask import Flask, request

app=Flask(__name__)




@app.route("/log")
def index():
    print(request)

    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, port=80, host= '0.0.0.0')