#analyze_me/views.py       2020/9/17   M.O
from flask import request, redirect, url_for, \
    render_template, flash, session
from analyze_me import app

#トップページ
@app.route('/')
def index():
    return render_template('index.html')

#個人情報(過去log)ページ
@app.route('/log')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/log.html')

#アナライザリスト
@app.route('/list')
def analyzer_list():
    return render_template('analyzer/list.html')

#アナライザ説明
@app.route('/description')
def description():
    return render_template('analyzer/description.html')

#アナライザ本体
@app.route('/analyzer')



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
