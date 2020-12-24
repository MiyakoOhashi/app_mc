#analyze_me/examin.py       2020/11/05   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint, g
from flask_login import login_required, current_user
#from analyze_me.analyzer.fu_check import FU
#from analyze_me.analyzer.eq_check import EQ
#from analyze_me.analyzer.ces_d import CES_D
#from analyze_me.analyzer.poms import POMS
#from analyze_me.analyzer.teg import TEG
from analyze_me.services import analyzer_service

#ブループリント設定
#examin = Blueprint('examin', __name__)

"""
#グローバル関数設定
@examin.before_request
def setting_analyzer():
    if session['ex_id'] == "fu":
        g.ana = FU()
    elif session['ex_id'] == "eq":
        g.ana = EQ()
    elif session['ex_id'] == 'ces':
        g.ana = CES_D()
    elif session['ex_id'] == 'pom':
        g.ana = POMS()
    elif session['ex_id'] == 'teg':
        g.ana = TEG()
    print("EX_ID:{}".format(session['ex_id']))
"""
"""
#説明
@examin.route('/description/<ex_id>')
def description(ex_id):
    analyzer_service.set_param(ex_id, session)
    ana = analyzer_service.setting_analyzer(ex_id)
    return render_template('analyzer/description.html',\
                            ex_id=ex_id, ana=ana)


#結果表示
@examin.route('/result/<ex_id>/<result_id>', methods=['GET'])
@login_required
def result(ex_id, result_id):
    ana = analyzer_service.setting_analyzer(ex_id)
    result = analyzer_service.find_one(ex_id, result_id)
    if ex_id == 'pom' or ex_id == 'teg':
        return render_template('analyzer/result_graph.html', \
                               ex_id=ex_id, ana=ana, result=result)
    else:
        return render_template('analyzer/result.html', \
                                ex_id=ex_id, ana=ana, result=result)

#テスト
@examin.route('/analyzer/<ex_id>', methods=['GET', 'POST'])
@login_required
def analyzer(ex_id):
    ana = analyzer_service.setting_analyzer(ex_id)
    if request.method == 'POST':
        try:
            ans = request.form.get('answer')
            ana.cal(int(ans), session)
            session['que'] += 1
            print("SESSION[QUE]: {}".format(session['que']))
        except TypeError:
            flash('回答が選択されていません。')
        if session['que'] >= len(ana.queries):
            session['judge'] = ana.judge(session['a_sum'])
            print('SESSION: {}'.format(session))
            print('USER_ID: {}'.format(current_user.id))
            result_id = analyzer_service.save(current_user.id, session)
            return redirect(url_for('examin.result', ex_id=ex_id, result_id=result_id))
    return render_template('analyzer/query.html',\
                                ex_id=ex_id, ana=ana)
"""