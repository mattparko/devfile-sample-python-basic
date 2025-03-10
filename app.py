from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/healthz')
def healthz():
    return "Health: OK"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
