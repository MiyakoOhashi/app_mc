#analyze_me/views.py       2020/9/17   M.O
from flask import request, redirect, url_for, \
    render_template, flash, session
from analyze_me import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            return redirect('/')
        return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect('/')
