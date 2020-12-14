#analyze_me/analyzes.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint, g
#from flask_login import login_required
#from analyze_me import db
#from analyze_me.models.user import User

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

"""
#グローバル関数設定
@analyzes.before_request
def setting_analyzer():
    g.ana = None
"""

#アナライザリスト
@analyzes.route('/list/')
def analyzer_list():
    return render_template('analyzer/list.html')

#アナライザ選択
@analyzes.route('/list/<ex_id>')
def analyzer_select(ex_id):
    if id:
        session['ex_id'] = ex_id
        session['que'] = 0
        print("SESSION[EX_ID]: {}, SESSION[QUE]: {}".format(session['ex_id'], session['que']))
        return redirect(url_for('examin.description', ex_id=ex_id))
    return redirect(url_for('analyzer_list'))





