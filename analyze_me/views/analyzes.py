#analyze_me/analyzes.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint
from flask_login import login_required, current_user
from analyze_me.services import analyzer_service

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

#アナライザリスト
@analyzes.route('/list/')
def analyzer_list():
    return render_template('analyzer/list.html')


#説明
@analyzes.route('/description/<ex_id>')
def description(ex_id):
    analyzer_service.set_param(ex_id, session)
    ana = analyzer_service.setting_analyzer(session['ex_id'])
    return render_template('analyzer/description.html', ana=ana)


#テスト
@analyzes.route('/analyzer/<ex_id>', methods=['GET', 'POST'])
@login_required
def analyzer(ex_id):
    ana = analyzer_service.setting_analyzer(session['ex_id'])
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
            return redirect(url_for('views.result', ex_id=ex_id, result_id=result_id))
    return render_template('analyzer/query.html', ana=ana)


#アナライザ選択
"""
@analyzes.route('/list/<ex_id>')
def analyzer_select(ex_id):
    if ex_id:
        #analyzer_service.set_param(ex_id, session)
        #print("SESSION[EX_ID]: {}, SESSION[QUE]: {}".format(session['ex_id'], session['que']))
        #print("SESSION[ANS]: {}, SESSION[A_SUM]: {}".format(session['answers'], session['a_sum']))
        return redirect(url_for('examin.description', ex_id=ex_id))
    return redirect(url_for('analyzer_list'))
"""





