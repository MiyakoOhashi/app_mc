#analyze_me/views.py       2020/9/17   M.O
#ログイン関連用viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session, Blueprint
from flask_login import login_required
from analyze_me.services import analyzer_service

#ブループリント設定
views = Blueprint('views', __name__)

#トップページ
@views.route('/')
def index():
    return render_template('index.html')

#個人情報(過去log)ページ
@views.route('/logs')
@login_required
def show_logs():
    fu_results = analyzer_service.find_all('fu')
    eq_results = analyzer_service.find_all('eq')
    return render_template('logs/logs.html', \
                           fu_results=fu_results, \
                           eq_results=eq_results)

#404エラー時処理
@views.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('views.index'))