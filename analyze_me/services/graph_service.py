#analyze_me/services/graph_service.py       2020/12/25   M.O
#グラフ描画関連データ処理ファイル
from flask import make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from analyze_me.services import analyzer_service, views_service

#全データ抽出
def ex_all_data(ex_id):
    #テスト結果取得
    results = views_service.find_all(ex_id)
    created_at = [ "", "", "", "", "", "", "", "", "", ""]
    a_sum = [ "", "", "", "", "", "", "", "", "", ""]
    i = 0
    for result in results:
        if i >= 10:
            break
        created_at.insert(0, '{0:%Y-%m-%d}'.format(result.created_at))
        created_at.pop()
        a_sum.insert(0, result.a_sum)
        a_sum.pop
        i += 1

    print("ex_id: {}, i: {}".format(ex_id, i))
    return created_at, a_sum

#グラフ描画
def draw_three_graphs():
    #描画データ設定、プロット
    cx, cy = ex_all_data('ces')     #ces-d
    fx, fy = ex_all_data('fu')      #fu
    qx, qy = ex_all_data('eq')      #eq

    #グラフ設定
    fig = plt.figure(figsize=[6,4])

    #ces_dグラフ
    ax1 = fig.add_subplot(311)
    ax1.set_ylim(0, 50)
    ax1.grid(which='both')
    ax1.plot(cx, cy)

    #fuグラフ
    ax2 = fig.add_subplot(312)
    ax2.set_ylim(0, 50)
    ax2.grid(which='both')
    ax2.plot(fx, fy)

    #eqグラフ
    ax3 = fig.add_subplot(313)
    ax3.set_ylim(0, 50)
    ax3.grid(which='both')
    ax3.plot(qx, qy)

    fig.tight_layout()

    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)

    return response


#個別データ抽出（POMS, TEG）
def ex_one_data(ex_id, result_id):
    #テスト結果取得
    g_fac = analyzer_service.setting_analyzer(ex_id).fac
    g_sum0 = views_service.find_one(ex_id, result_id).a_sum
    g_sum = []

    if ex_id == "teg":
        g_fac.pop()
        i = 0
        for i in range(0, 5):
            g_sum.append(g_sum0[i] * 100 / 25)
            i += 1

    return g_fac, g_sum

#グラフ描画
def draw_graph(ex_id, result_id):
    #描画データ設定、プロット
    x, y = ex_one_data(ex_id, result_id)

    #グラフ設定
    fig = plt.figure(figsize=[4.5,3])

    #グラフ
    ax = fig.add_subplot(111)
    #ax.grid(which='both')
    #ax.set_title('Graph')
    ax.bar(x, y)
    ax.set_ylabel("Parsentile(%)")              #ラベル
    ax.set_ylim(0, 100)                         #表示範囲
    ax.set_yticks([0, 25, 50, 75, 100])         #表示メモリ

    fig.tight_layout()

    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)

    return response