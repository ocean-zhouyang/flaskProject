from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World'

def hello_world1():
    return "hello world11111"
app.add_url_rule('/hello1', '', hello_world1)

@app.route('/hello/<name>')
def hello_guest(name):
    return 'Hello %s!' % name


@app.route('/hello/testint/<int:age>')
def hello_test1(age):
    return '输入的数字是 %s' % age

@app.route('/hello/testfloat/<float:num>')
def hello_test2(num):
    return '输入的浮点数是 %s' % num

@app.route('/hello/testpath/<path:url>')
def hello_test3(url):
    return '输入的地址是 %s' % url

if __name__ == '__main__':

    app.run(debug=True)
