from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 这是一个简单的用户数据库，实际应用中应该使用数据库管理用户
users = {'admin': '123456'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        # 登录成功，重定向到用户的博客页面
        return redirect(url_for('blog', username=username))
    else:
        # 登录失败，返回登录页面并显示错误消息
        return render_template('index.html', error='Invalid username or password')

@app.route('/blog/<username>')
def blog(username):
    return render_template('blog.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
