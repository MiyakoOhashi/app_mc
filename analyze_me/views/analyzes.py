#analyze_me/views.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint
from analyze_me import app
#from analyze_me import db
#from analyze_me.models.entries import Entry
from analyze_me.views.views import login_required
from analyze_me.analyzer.fu_check import FU
from analyze_me.analyzer.eq_check import EQ
from analyze_me.analyzer.ces_d import CES_D
from analyze_me.views.views import login_required

#グローバル変数設定
#各テストインスタンス
fu = FU()       #FU(フュージョン)チェック
eq = EQ()       #EQ(脱中心化)チェック
ces = CES_D()   #CES-D

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

#インスタンスセット
@analyzes.url_value_preprocessor
def add_analyzer(endpoint, values):
    #print("エンドポイントは{}".format(endpoint))
    if not endpoint is None:
        global fu
        global eq
        global ces
        values["fu"] = fu
        values["eq"] = eq
        values['ces'] = ces

#アナライザリスト
@analyzes.route('/list')
def analyzer_list(fu, eq, ces):
    return render_template('analyzer/list.html')

#アナライザ説明
@analyzes.route('/description/<id>')
def description(id, fu, eq, ces):
    if id == 'fu':
        ana = fu
    elif id == 'eq':
        ana = eq
    elif id == 'ces':
        ana = ces
    return render_template('analyzer/description.html',\
                            id=id, ana=ana)

#アナライザ結果表示
@analyzes.route('/result/<id>', methods=['GET'])
def result(id, fu, eq, ces):
    if id == 'fu':
        ana = fu
    elif id == 'eq':
        ana = eq
    elif id == 'ces':
        ana = ces
    return render_template('analyzer/result.html', \
                           id=id, ana=ana)

#アナライザ本体
@analyzes.route('/analyzer/<id>', methods=['GET', 'POST'])
def analyzer(id, fu, eq, ces):
    if id == 'fu':
        ana = fu
    elif id == 'eq':
        ana = eq
    elif id == 'ces':
        ana = ces

    if request.method == 'POST':
        ans = request.form.get('answer')
        ana.cal(int(ans))
        if ana.que >= ana.q_len:
            ana.judge(ana.a_sum)
            return redirect(url_for('analyzes.result', id=id))
    return render_template('analyzer/query.html',\
                                id=id, ana=ana)

