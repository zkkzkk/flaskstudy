from flask import Flask
import json
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def home():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return json.dumps(t)




if __name__ == '__main__':
    app.run()