#analyze_me/views.py       2020/9/17   M.O
#ログイン関連用viewファイル

from flask import request, redirect, url_for, \
    render_template, flash, session
from analyze_me import app
from functools import wraps

#ログイン承認デレコーダ
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

#トップページ
@app.route('/')
def index():
    return render_template('index.html')

#個人情報(過去log)ページ
@app.route('/log')
@login_required
def show_entries():
    return render_template('entries/log.html')

#ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':            #ログイン画面入力時
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')    #ログイン画面遷移時、入力エラー時

#ログアウト
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('index'))

#404エラー時処理
@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('index'))