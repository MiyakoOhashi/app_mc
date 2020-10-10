#analyze_me/views.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from analyze_me import app
#from analyze_me import db
#from analyze_me.models.entries import Entry
from analyze_me.analyzer.fu_check import FU

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
@app.route('/description/<id>')
def description(id):
    return render_template('analyzer/description.html', id=id)

#アナライザ本体
@app.route('/analyzer/<id>', methods=['GET', 'POST'])
def analyzer(id):
    if request.method == 'GET':
        if id == "fu":  # フュージョンチェック
            name = 'FUチェック'
            ana = FU()
        #elif id == "eq":  # 脱中心化チェック
            #analyzer = EQ()
        #elif id == "ces":  # CES-D
            #analyzer = CES_D()
        #elif id == "pom":  # POMS
            #analyzer = POMS()
        #elif id == "teg":  # TEG
            #analyzer = TEG()

    if request.method == 'POST':
        ans = request.form.get('radio')
        ana.cal(ans)
    return render_template('analyzer/query.html',\
                            id=id, ana=ana, name=name)

