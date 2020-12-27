#analyze_me/services/graph_service.py       2020/12/25   M.O
#グラフ描画関連データ処理ファイル
from flask import make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from analyze_me.services import analyzer_service, views_service

#グラフ描画
def draw_graph(ex_id):
    #テスト結果取得
    results = views_service.find_all(ex_id)
    created_at = []
    a_sum = []
    for result in results:
        created_at.append(result.created_at)
        a_sum.append(result.a_sum)

    fig = plt.figure()
    ax = fig.add_subplot()
    plt.cla()
    #描画データ設定、プロット
    x = '{0:%Y-%m-%d}'.format(created_at)
    y = a_sum
    plt.plot(x, y)
    #グラフ軸
    plt.xlabel('実施日')
    plt.ylabel('合計点')

    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)

    return response