#analyze_me/views.py       2020/9/17   M.O
#ログイン関連用viewファイル
from flask import request, redirect, url_for, \
    render_template, flash, session, Blueprint
from flask_login import login_required
from analyze_me.services import analyzer_service, views_service, graph_service

#ブループリント設定
views = Blueprint('views', __name__)

#トップページ
@views.route('/')
def index():
    return render_template('index.html')

#過去ログページ
@views.route('/logs/')
@login_required
def show_logs():
    fu_results = views_service.find_all('fu')
    eq_results = views_service.find_all('eq')
    ces_results = views_service.find_all('ces')
    pom_results = views_service.find_all('pom')
    teg_results = views_service.find_all('teg')
    return render_template('logs/logs.html', fu_results=fu_results, \
                           eq_results=eq_results, ces_results=ces_results, \
                           pom_results=pom_results, teg_results=teg_results)


#グラフ表示
@views.route('/logs/graph_fu/')
def plot_graph():
    response = graph_service.draw_graph('fu')
    return response


#結果表示
@views.route('/result/<ex_id>/No<result_id>/', methods=['GET'])
@login_required
def result(ex_id, result_id):
    ana = analyzer_service.setting_analyzer(ex_id)
    result = views_service.find_one(ex_id, result_id)
    if ex_id == 'pom' or ex_id == 'teg':
        return render_template('logs/result_graph.html', \
                               ex_id=ex_id, ana=ana, result=result)
    else:
        return render_template('logs/result.html', \
                                ex_id=ex_id, ana=ana, result=result)


#表示内容削除
@views.route('/result/delete/<ex_id>/No<result_id>/', methods=['POST'])
@login_required
def delete_result(ex_id, result_id):
    views_service.delete(ex_id, result_id)
    flash('データを削除しました')
    return redirect(url_for('views.show_logs'))


#404エラー時処理
@views.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('views.index'))