#analyze_me/examin.py       2020/11/05   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint, g
from flask_login import login_required, current_user
from analyze_me import app
#from analyze_me import db
#from analyze_me.models.user import User
from analyze_me.analyzer.fu_check import FU
from analyze_me.analyzer.eq_check import EQ
from analyze_me.analyzer.ces_d import CES_D
from analyze_me.analyzer.poms import POMS
from analyze_me.analyzer.teg import TEG
from analyze_me.views.analyzes import analyzes
from analyze_me.services import analyzer_service
"""
#グローバル変数（各テスト）設定
fu = FU()
eq = EQ()
ces = CES_D()
pom = POMS()
teg = TEG()
"""
#ブループリント設定
examin = Blueprint('examin', __name__)

#グローバル関数設定
@examin.before_request
def setting_analyzer():
    ex_id = session['ex_id']
    if ex_id == "fu":
        g.ana = FU()
    elif ex_id == "eq":
        g.ana = EQ()
    elif ex_id == 'ces':
        g.ana = CES_D()
    elif ex_id == 'pom':
        g.ana = POMS()
    elif ex_id == 'teg':
        g.ana = TEG()
    print("EX_ID:{}".format(ex_id))

"""
#インスタンスセット
@examin.url_value_preprocessor
def add_analyzer(endpoint, values):
    print("エンドポイント:{}".format(endpoint))
    ex_id = session['ex_id']
    if not endpoint is None:
        if ex_id == 'fu':
            global fu
            values['ana'] = fu
        elif ex_id == 'eq':
            global eq
            values['ana'] = eq
        elif ex_id == 'ces':
            global ces
            values['ana'] = ces
        elif ex_id == 'pom':
            global pom
            values['ana'] = pom
        elif ex_id == 'teg':
            global teg
            values['ana'] = teg
"""

#説明
"""
@examin.route('/description/<ex_id>')
@login_required
def description(ex_id):
    user_id = current_user.user_id
    print("USER_ID: {}".format(user_id))
    ana = analyzer_service.create_ana(ex_id, user_id)
    return render_template('analyzer/description.html',\
                            ex_id=ex_id, ana=ana)
"""
@examin.route('/description/<ex_id>')
def description(ex_id):
    return render_template('analyzer/description.html',\
                            ex_id=ex_id, ana=g.ana)



#結果表
@examin.route('/result/<ex_id>/<result_id>', methods=['GET'])
def result(ex_id, result_id):
    result = analyzer_service.find_one(ex_id, result_id)
    if ex_id == 'pom' or ex_id == 'teg':
        return render_template('analyzer/result_graph.html', \
                               ex_id=ex_id, ana=g.ana, result=result)
    else:
        return render_template('analyzer/result.html', \
                                ex_id=ex_id, ana=g.ana, result=result)

#テスト
@examin.route('/analyzer/<ex_id>', methods=['GET', 'POST'])
def analyzer(ex_id):
    if request.method == 'POST':
        try:
            ans = request.form.get('answer')
            g.ana.cal(int(ans), session)
            session['que'] += 1
            print("SESSION[QUE]: {}".format(session['que']))
        except TypeError:
            flash('回答が選択されていません。')
        if session['que'] >= len(g.ana.queries):
            #ana.judge(ana.a_sum)
            session['judge'] = g.ana.judge(session['a_sum'])
            print('SESSION: {}'.format(session))
            print('USER_ID: {}'.format(current_user.id))
            result_id = analyzer_service.save(current_user.id, session)
            return redirect(url_for('examin.result', ex_id=ex_id, result_id=result_id))
    return render_template('analyzer/query.html',\
                                ex_id=ex_id, ana=g.ana)
