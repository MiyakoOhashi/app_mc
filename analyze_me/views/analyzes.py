#analyze_me/views.py       2020/10/07   M.O
#コンテンツ関連viewファイル

from flask import request, redirect, url_for, \
    render_template, flash, session
from analyze_me import app
#from analyze_me import db
#from analyze_me.models.entries import Entry

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
def analyze():
    return render_template('analyzer/query.html')
