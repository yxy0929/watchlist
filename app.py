from flask import Flask
from flask import render_template


app = Flask(__name__)

name = 'yexiangyang'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},

]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
# @app.route('/')
# @app.route('/index')
# @app.route('/home')
# def hello_world():
#    return '<h1>Hello YiLin!</h1><img src="http://helloflask.com/totoro.gif">'


# @app.route('/user/<name>')
# def user_page(name):
#     return 'User %s' % name


# @app.route('/test')
# def test_url_for():
#     return 'Test page'


if __name__ == '__main__':
    app.run()
