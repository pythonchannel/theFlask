from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    '''打开浏览器默认是进入这个方法'''
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/index')
def index():
    '''后面追加index是进入这个方法'''
    return 'hello world index'


@app.route('/search/<keyword>')
def search(keyword):
    '''尖括号里面可以输入变量字符串'''
    return 'hello world %s' % keyword


@app.route('/plus')
def doPlus():
    return '666'


@app.route('/plus')
def doPlus2(name):
    return '777'


@app.route('/add')
def doAdd():
    print('打印全部参数:%s' % request.args)
    # request.args 就是全部参数的字典
    if 'one' not in request.args:
        return '没有请求参数one'

    if 'two' not in request.args:
        return '没有请求参数two'

    try:
        one = int(request.args.get('one'))
        two = int(request.args.get('two'))
        result = '结果是:%d' % (one + two)
        return render_template('result.html', show=result)
    except Exception as e:
        result = '错误信息：%s' % e.args
        return render_template('result.html', show=result)


@app.route('/mul')
def doMul():
    print('打印全部参数:%s' % request.args)
    # request.args 就是全部参数的字典
    if 'one' not in request.args:
        return '没有请求参数one'

    if 'two' not in request.args:
        return '没有请求参数two'

    try:
        one = int(request.args.get('one'))
        two = int(request.args.get('two'))

        result = '结果是:%d' % (one * two)
        return render_template('result.html', arg1=one, arg2=two, show=result)
    except Exception as e:
        result = '错误信息：%s' % e.args
        return render_template('result.html', show=result)


@app.route('/comp')
def doComp():
    print('打印全部参数:%s' % request.args)
    # request.args 就是全部参数的字典
    if 'one' not in request.args:
        return '没有请求参数one'

    if 'two' not in request.args:
        return '没有请求参数two'

    try:
        one = int(request.args.get('one'))
        two = int(request.args.get('two'))
        mode = request.args.get('mode')
        result = 0
        mode_word = ''
        if '+' == mode:
            result = one + two
            mode_word = '加法'
        elif '-' == mode:
            result = one + two
            mode_word = '减法'
        elif '*' == mode:
            result = one * two
            mode_word = '乘法'
        elif '/' == mode:
            result = one / two
            mode_word = '除法'
        else:
            result = '计算方式无效'
            mode_word = '计算方式无效'

        result = '结果是:%s' % str(result)
        return render_template('result.html', arg1=one, arg2=two, mode_word=mode_word, show=result)
    except Exception as e:
        result = '错误信息：%s' % e.args
        return render_template('result.html', show=result)


if __name__ == '__main__':
    app.run()
