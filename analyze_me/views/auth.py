#analyze_me/views/auth.py       2020/12/01   M.O
#ログイン関連用viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session, Blueprint
#from functools import wraps
from analyze_me.services import auth_service

auth = Blueprint('auth', __name__)

#ユーザデータ登録
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':            #ログイン画面入力時
        user = auth_service.signup(request.form)
        if user == 'empty':
            flash('未記入の項目があります')
            return render_template('auth/signup.html')
        elif user:
            flash('このユーザIDはすでに登録されています')
            return redirect(url_for('auth.login'))
        else:
            flash('新規登録に成功しました')
            return redirect(url_for('auth.login'))
    return render_template('auth/signup.html')    #サインアップ画面遷移時、入力エラー時

#ログイン
@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':            #ログイン画面入力時
        user = auth_service.login(request.form)
        if user == 'empty':
            flash('未記入の項目があります')
            return render_template('auth/login.html')
        if not user:
            flash('ユーザIDもしくはパスワードに誤りがあります')
            return render_template('auth/login.html')
        else:
            #session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('views.show_logs'))
    return render_template('auth/login.html')    #ログイン画面遷移時、入力エラー時

#ログアウト
@auth.route('/logout')
def logout():
    #session.pop('logged_in', None)
    auth_service.logout()
    flash('ログアウトしました')
    return redirect(url_for('views.index'))


#ログイン承認デレコーダ
"""
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return inner
"""
