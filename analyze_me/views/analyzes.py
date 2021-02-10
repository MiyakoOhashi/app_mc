#analyze_me/analyzes.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import current_app as app
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint
from flask_login import login_required, current_user
from analyze_me.services import analyzer_service

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

#アナライザリスト
@analyzes.route('/analyzers_list/')
def analyzer_list():
    analyzer_service.delete_param()
    return render_template('analyzer/list.html')


#説明
@analyzes.route('/description/<ex_id>')
def description(ex_id):
    analyzer_service.set_param(ex_id)
    ana = analyzer_service.setting_analyzer(session['ex_id'])
    return render_template('analyzer/description.html', ana=ana)


#テスト
@analyzes.route('/analyzer/<ex_id>', methods=['GET', 'POST'])
@login_required
def analyzer(ex_id):
    ana = analyzer_service.setting_analyzer(ex_id)
    if request.method == 'POST':
        try:
            ans = request.form.get('answer')
            ana.cal(int(ans))
            session['que'] += 1
            #print("ただいまの質問：{}".format(session['que']))
            #print("ANSWER：{}".format(session['answers']))
            #print("A_SUM: {}".format(session['a_sum']))
        except TypeError:
            flash('回答が選択されていません。')

        if session['que'] >= len(ana.queries):
            session['judge'] = ana.judge()
            result_id = analyzer_service.save()
            return redirect(url_for('views.result', ex_id=ex_id, result_id=result_id))
    return render_template('analyzer/query.html', ana=ana)







