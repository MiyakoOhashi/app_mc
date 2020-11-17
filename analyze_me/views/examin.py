#analyze_me/examin.py       2020/11/05   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint, g
from analyze_me import app
#from analyze_me import db
#from analyze_me.models.entries import Entry
from analyze_me.views.views import login_required
from analyze_me.analyzer.description import Desc
from analyze_me.analyzer.fu_check import FU
from analyze_me.analyzer.eq_check import EQ
from analyze_me.analyzer.ces_d import CES_D
from analyze_me.analyzer.poms import POMS
from analyze_me.analyzer.teg import TEG
#from analyze_me.views.analyzes import g
from analyze_me.views.analyzes import analyzes

#グローバル変数（各テスト）設定
fu = FU()
eq = EQ()
ces = CES_D()
pom = POMS()
teg = TEG()

#ブループリント設定
examin = Blueprint('examin', __name__)

#インスタンスセット
@examin.url_value_preprocessor
def add_analyzer(endpoint, values):
    print("エンドポイント:{}".format(endpoint))
    print("SESSION:{}".format(session['test_start']))
    test_start = session['test_start']
    id = session['id']
    if not endpoint is None:
        if test_start is True:
            #values["ana"] = g.ana

            if id == 'fu':
                global fu
                values['ana'] = fu
            elif id == 'eq':
                global eq
                values['ana'] = eq
            elif id == 'ces':
                global ces
                values['ana'] = ces
            elif id == 'pom':
                global pom
                values['ana'] = pom
            elif id == 'teg':
                global teg
                values['ana'] = teg


#説明
@examin.route('/description/<id>')
def description(id, ana):
    return render_template('analyzer/description.html',\
                            id=id, ana=ana)

#結果表示
@examin.route('/result/<id>', methods=['GET'])
def result(id, ana):
    if id == 'pom' or id == 'teg':
        return render_template('analyzer/result_graph.html', \
                               id=id, ana=ana)
    else:
        return render_template('analyzer/result.html', \
                                id=id, ana=ana)

#テスト
@examin.route('/analyzer/<id>', methods=['GET', 'POST'])
def analyzer(id, ana):
    if request.method == 'POST':
        ans = request.form.get('answer')
        ana.cal(int(ans))
        if ana.que >= ana.q_len:
            ana.judge(ana.a_sum)
            return redirect(url_for('examin.result', id=id))
    return render_template('analyzer/query.html',\
                                id=id, ana=ana)
