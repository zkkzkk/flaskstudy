from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def home():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()