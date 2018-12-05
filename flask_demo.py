from flask import Flask

app = Flask(__name__)

# 最基本的入口
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# 一个视图函数可以绑定多个URL
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello World!</h1>'

# 动态URL，可以指定默认值
@app.route('/greet', defaults={'name': 'index'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
