from flask import Flask
from flask import url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def hello_world():
    return '<h1>Hello YiLin!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User %s' % name


@app.route('/test')
def test_url_for():
    return 'Test page'


if __name__ == '__main__':
    app.run()
