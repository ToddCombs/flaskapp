from flask import Flask, request, url_for, render_template
from models import User
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return '<h1>Hello World!</h1>'
    content = "Hello FFFFlask!"
    return render_template("index.html", content=content)

@app.route('/user')
# def hello_user():
#     return 'Hellooooo user'
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
def query_user():
    id = request.args.get('id')
    return 'query user:' + id
# 反向路由，日常应用较多
@app.route('/query_url')
def query_url():
    return 'query url:' + url_for('query_user')

if __name__ == '__main__':
    app.run()
