from flask import Flask, request, url_for, \
    render_template, flash, abort, redirect
from models import User
app = Flask(__name__)
# 使用消息提示时需调用secret_key，flask使用他对消息加密
app.secret_key = '213'

@app.route('/')
def index():
    """这是主页，试验用户访问首页时自动跳转至add方法"""
    return redirect(url_for('add'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    # return '<h1>Hello World!</h1>'
    # content = "Hello FFFFlask!"
    # flash消息提示
    flash("Helloooo Flask!")
    if request.method == 'POST':
        a = request.form['adder1']
        b = request.form['adder2']
        a = int(a)
        b = int(b)
        c = a + b
        return render_template("index.html", message=str(c))
    # return render_template("index.html", content=content)
    return render_template("index.html")



@app.route('/user')
# def hello_user():
#     return 'Hellooooo user'
# /user?id=1
def user_index():
    user = User(1, 'ToddCombs')
    return render_template("user_index.html", user=user)

# 判断入参user_id是否为1，是则user=todd,否则返回user_id.html
@app.route('/query_userr/<user_id>')
def query_userr(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'todd')
    return render_template("user_id.html", user=user)

@app.route('/userr')  # 模板的基础
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, 'toddCombs' + str(i))
        users.append(user)
    return render_template("user_list.html", users=users)

# 定义路由，继承html页面头部和脚部模板
@app.route('/one')
def one_base():
    return render_template("one_base.html")
@app.route('/two')
def two_base():
    return render_template("two_base.html")


# 获取参数
@app.route('/users/<id>')
def user_id(id):
    return 'hello user:' + id
# 获取参数的常用方法
@app.route('/query_user')
# /query_user?id=1
def query_user():
    id = request.args.get('id')
    return 'query user:' + id
# 反向路由，日常应用较多
@app.route('/query_url')
def query_url():
    return 'query url:' + url_for('query_user')


# 消息提示相关逻辑
@app.route('/login', methods=['POST'])
def login():
    """获取用户输入的用户名和密码"""
    form = request.form
    username = form.get('username')
    password = form.get('password')
    # 判断逻辑
    if not username:
        flash("请输入用户名")
        return render_template("index.html")
    if not password:
        flash("请输入密码")
        return render_template("index.html")
    if username == 'toddcombs' and password == '111111':
        flash("登陆成功")
        return render_template("index.html")
    else:
        flash("用户名/密码错误")
        return render_template("index.html")

# 异常提示信息的装饰器，可以让404错误返回更友好
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
# 异常处理：获取用户id如果=1，则返回正常页面，否泽调用abort函数返回指定404页
# /use/1
@app.route('/use/<use_id>')
def use(use_id):
    if int(use_id) == 1:
        return render_template("use.html")
    else:
        # abort()函数用于提前退出一个请求，并用指定的错误码返回。
        abort(404)



if __name__ == '__main__':
    app.run()
