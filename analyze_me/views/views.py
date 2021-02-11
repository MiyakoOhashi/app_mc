#analyze_me/views.py       2020/9/17   M.O
#ログイン関連用viewファイル
from flask import current_app as app
from flask import request, redirect, url_for, \
    render_template, flash, session, Blueprint
from flask_login import login_required
from analyze_me.services import analyzer_service, \
    views_service, graph_service, desc_indivi_service

#ブループリント設定
views = Blueprint('views', __name__)

#トップページ
@views.route('/')
def index():
    return render_template('index.html')

#導入ページ
@views.route('/introduction/')
def intro():
    return render_template('intro.html')

#過去ログページ
@views.route('/logs/')
@login_required
def show_logs():
    fu_results = views_service.find_all('fu')
    eq_results = views_service.find_all('eq')
    ces_results = views_service.find_all('ces')
    pom_results = views_service.find_all('pom')
    teg_results = views_service.find_all('teg')
    ces_date, ces_asum = graph_service.ex_all_data('ces')   # ces-d graph
    fu_date, fu_asum = graph_service.ex_all_data('fu')      # fu graph
    eq_date, eq_asum = graph_service.ex_all_data('eq')      # eq graph
    return render_template('logs/logs.html', fu_results=fu_results, \
                           eq_results=eq_results, ces_results=ces_results, \
                           pom_results=pom_results, teg_results=teg_results, \
                           ces_date=ces_date, ces_asum=ces_asum, fu_date=fu_date, \
                           fu_asum=fu_asum, eq_date=eq_date, eq_asum=eq_asum)


#グラフ表示(log画面):未使用
@views.route('/logs/graph/')
def plot_graph():
    response = graph_service.draw_three_graphs()
    return response


#表示内容削除(log画面)＜通常非表示＞
@views.route('/result/delete/<ex_id>/<result_id>/', methods=['POST'])
@login_required
def delete_result(ex_id, result_id):
    views_service.delete(ex_id, result_id)
    flash('データを削除しました')
    return redirect(url_for('views.show_logs'))


#結果表示
@views.route('/result/<ex_id>/<result_id>/', methods=['GET'])
@login_required
def result(ex_id, result_id):
    ana = analyzer_service.setting_analyzer(ex_id)
    result = views_service.find_one(ex_id, result_id)

    if ex_id == 'pom' or ex_id == 'teg':
        g_fac, g_sum = graph_service.ex_one_data(ex_id, result_id)

        return render_template('logs/result_graph.html', \
                               ex_id=ex_id, result_id=result_id, \
                               ana=ana, result=result, g_fac=g_fac, g_sum=g_sum)
    else:
        return render_template('logs/result.html', \
                                ex_id=ex_id, result_id=result_id, \
                                ana=ana, result=result)


#TEG パラメータ説明
@views.route('/description_<ex_id>/<result_id>/')
def desc_teg(ex_id, result_id):
    if ex_id == "teg":
        desc = desc_indivi_service.Desc_teg()
    return render_template('logs/desc01_teg.html', ex_id=ex_id, result_id=result_id, desc=desc)


#グラフ表示(個別画面＿TEG, POMS):未使用
@views.route('/logs/graph/<ex_id>/<result_id>/')
def plot_graph_indivi(ex_id, result_id):
    response = graph_service.draw_graph(ex_id, result_id)
    return response

#404エラー時処理
@views.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('views.index'))