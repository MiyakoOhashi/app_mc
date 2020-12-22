#analyze_me/analyzes.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint, g
#from flask_login import login_required
#from analyze_me import db
#from analyze_me.models.user import User
from analyze_me.services import analyzer_service

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

#アナライザリスト
@analyzes.route('/list/')
def analyzer_list():
    return render_template('analyzer/list.html')

#アナライザ選択
@analyzes.route('/list/<ex_id>')
def analyzer_select(ex_id):
    if ex_id:
        analyzer_service.set_param(ex_id, session)
        """
        session['ex_id'] = ex_id
        session['que'] = 0
        session['judge_r'] = None
        session['answers'] = []
        if ex_id == "teg" or ex_id == "pom":        #TEG, POMS
            session['a_sum'] = [ 0, 0, 0, 0, 0, 0 ]
        else:                                       #FU, EQ, CES-D
            session['a_sum'] = 0
        """
        print("SESSION[EX_ID]: {}, SESSION[QUE]: {}".format(session['ex_id'], session['que']))
        print("SESSION[ANS]: {}, SESSION[A_SUM]: {}".format(session['answers'], session['a_sum']))
        return redirect(url_for('examin.description', ex_id=ex_id))
    return redirect(url_for('analyzer_list'))





