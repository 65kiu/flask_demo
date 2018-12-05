from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/ass')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/cc_owefeemgnt', defaults={'name': 'index'})
@app.route('/cc_owefeemgnt/<name>')
def cc_owefeemgnt(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
