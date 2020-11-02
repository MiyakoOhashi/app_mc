#analyze_me/views.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint
from analyze_me import app
#from analyze_me import db
#from analyze_me.models.entries import Entry
from analyze_me.analyzer.fu_check import FU
from analyze_me.views.views import login_required

#グローバル変数設定
#各テストインスタンス
fu = FU()

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

#インスタンスを
@analyzes.url_value_preprocessor
def add_analyzer(endpoint, values):
    #print("エンドポイントは{}".format(endpoint))
    if not endpoint is None:
        global fu
        values["ana"] = fu

#アナライザリスト
@analyzes.route('/list')
def analyzer_list(ana):
    return render_template('analyzer/list.html')

#アナライザ説明
@analyzes.route('/description/<id>')
def description(id, ana):
    return render_template('analyzer/description.html',\
                            id=id, ana=ana)

#アナライザ本体
@analyzes.route('/analyzer/<id>', methods=['GET', 'POST'])
def analyzer(id, ana):
    if request.method == 'POST':
        ans = request.form.get('answer')
        ana.cal(int(ans))
        if ana.que >= ana.q_len:
            return render_template('analyzer/result.html', \
                                   id=id, ana=ana)
    return render_template('analyzer/query.html',\
                                id=id, ana=ana)

