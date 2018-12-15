from flask import Flask, request, redirect, make_response, url_for, session
import click

app = Flask(__name__)
#配合session使用
app.secret_key = '1234567890'

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

@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')

'''模版文件放在template路径下，静态文件存放在static路径下'''


# 获取请求URL中的查询字符串
# 例如http://127.0.0.1:5000/hello1?name=test，页面的内容就是Hello, test
# 如果是http://127.0.0.1:5000/hello1，页面的内容就是Hello, Flask
@app.route('/hello1')
def hello1():
    name = request.args.get('name', 'Flask')
    return '<h1>Hello, %s</h1>' % name

#转换器<转换名:变量名>
@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d</p>' % (2018 - year)

#在访问http://localhost:5000/colors/<color>的时候，如果用户传入的不是blue、white、red，其余任意的字符串都会获得404错误相应
@app.route('/colors/<any(blue, white, red):color>')
def three_colors(color):
    return '<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.</p>'

#也可以通过一个预先定义的列表，来构建URL规则字符串
colors = ['blue', 'white', 'red']
@app.route('/colors1/<any(%s):color>' % str(colors)[1:-1])
def colors1(color):
    return '<p>colors %s</p>' % color

#请求处理钩子
#before_request after_request before_first_request after request after_this_request

@app.before_request
def do_something():
    print("do_something")

#重定向
@app.route('/helloo')
def helloo():
    return redirect('http://www.baidu.com')

#设置cookie
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello1')))
    response.set_cookie('name', name)
    return response

#获取cookie
@app.route('/helllo')
def get_hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    return '<h1>Hello, %s</h1>' % name

#session
@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello1'))

if __name__ == '__main__':
    app.run()
