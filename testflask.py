from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def home():
    return "测试页面"


if __name__ == '__main__':
    app.run()