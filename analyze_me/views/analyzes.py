#analyze_me/analyzes.py       2020/10/07   M.O
#コンテンツ関連viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session
from flask import Blueprint, g
#from analyze_me import db
#from analyze_me.models.entries import Entry
from analyze_me.views.views import login_required

#ブループリント設定
analyzes = Blueprint('analyzes', __name__)

#グローバル関数設定
@analyzes.before_request
def setting_analyzer():
    g.ana = None

#アナライザリスト
@analyzes.route('/list/')
def analyzer_list():
    return render_template('analyzer/list.html')

#アナライザ選択
@analyzes.route('/list/<id>')
def analyzer_select(id):
    if not id is None:
        session['test_start'] = True
        session['id'] = id
        print("SESSION:{}".format(session['test_start']))
        print("SESSION:{}".format(session['id']))
        return redirect(url_for('examin.description', id=id))
    return redirect(url_for('analyzer_list'))





