#analyze_me/services/graph_service.py       2020/12/25   M.O
#グラフ描画関連データ処理ファイル
from flask import make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from flask_login import current_user
from analyze_me.services import analyzer_service, views_service

#全データ抽出
def ex_all_data(ex_id):
    #テスト結果取得
    results = views_service.find_all(ex_id)
    created_at = [ "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp"]
    a_sum = [ "", "", "", "", "", "", "", "", "", ""]
    i = 0
    for result in results:
        if i >= 10:
            break
        created_at.insert(0, '{0:%Y-%m-%d}'.format(result.created_at))
        created_at.pop()
        a_sum.insert(0, result.a_sum)
        a_sum.pop()
        i += 1

    return created_at, a_sum

#グラフ描画(matplotlib_ver)
"""
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
"""

#データ換算
def conv_data(ex_id, g_sum0, g_sum):
    #TEG_male グラフ用換算値
    teg_m = [
        #CP_male[0]
            [0, 1.5, 2, 2.5, 5, 7, 10, 11, 19, 21, 30, 35, 48, 55, 65, 70, 81, 89, 95, 98.5, 100],
        #NP_male[1]
            [0, 1, 2, 2.5, 4, 4.5, 5.2, 6, 10, 11.5, 19, 26, 38, 45, 51, 61, 71, 79.5, 89.5, 94.5, 100],
        #A_male[2]
           [0, 1, 3, 3.5, 6, 7, 10.5, 15, 19, 22, 31, 29, 48, 53, 62, 69, 79, 82, 92, 95, 100],
        #FC_male[3]
           [0, 1, 1.5, 3, 5, 6, 10.5, 12, 21, 26, 31, 40.5, 50, 54, 63, 69.5, 79, 82, 92, 95, 100],
        #AC_male[4]
           [0, 5, 6, 10, 11, 18, 20.5, 22, 30, 39, 47, 50, 59, 62, 70, 78, 82, 88, 93, 95, 100]
    ]
    # TEG_female グラフ用換算値（未使用）
    teg_f = [
        #CP_female[0]
        [0, 0.8, 1.5, 2, 4, 5.5, 9, 10.5, 18, 22, 30.5, 40, 50, 59.5, 69.5, 78, 81, 90, 95, 98.5, 100],
        #NP_female[1]
        [0, 1.3, 1.5, 1.8, 2, 4.5, 6, 7, 8.5, 10.5, 20, 23, 30, 37, 42, 51, 61, 72, 82, 94, 100],
        #A_female[2]
        [0, 1.3, 3, 5.2, 9.5, 11, 20, 23, 34, 40, 50, 51, 60, 68, 78, 81, 87, 91, 95, 98, 100],
        #FC_female[3]
        [0, 0.1, 0.7, 1.3, 2, 3, 6, 9, 11.5, 20.5, 24, 30.5, 40, 50, 58, 62, 72, 80, 90, 97, 100],
        #AC_female[4]
        [0, 4, 5.5, 6, 10, 11, 18, 20.5, 24, 31, 39, 42, 52, 60, 69.5, 71, 79, 83, 94, 95.5, 100]
    ]

    #POMS_male グラフ用換算値
    pom_m = [
        # T-A_male[0]
        [31, 33, 34, 36, 37, 39, 40, 42, 44, 45, 47, 48, 50, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 71, 72, 74,
         75, 77, 79, 80, 82, 83, 85],
        # D_male[1]
        [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
         68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85],
        # A-H_male[2]
        [37, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 67, 69, 70,
         71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85],
        # V_male[3]
        [27, 28, 30, 32, 33, 35, 37, 38, 40, 41, 43, 45, 46, 48, 50, 51, 53, 55, 56, 58, 60, 61, 63, 64, 66, 68, 69, 71,
         73, 74, 76, 78, 79],
        # F_male[4]
        [35, 37, 38, 40, 41, 43, 45, 46, 48, 50, 51, 53, 54, 56, 58, 59, 61, 62, 64, 66, 67, 69, 70, 72, 74, 75, 77, 79,
         80],
        # C_male[5]
        [32, 34, 36, 38, 40, 42, 44, 47, 49, 51, 53, 55, 57, 59, 61, 64, 66, 68, 70, 72, 74, 76, 79, 81, 83, 85]
    ]
    # POMS_female グラフ用換算値（未使用）
    pom_f = [
        #T - A_female
        [33, 34, 36, 37, 39, 40, 41, 43, 44, 46, 47, 48, 50, 51, 53, 54, 55, 57, 58, 60, 61, 63, 64, 65, 67, 68, 70, 71, 72, 74, 75, 77, 78, 79, 81, 82, 84],
        #D_female   43(3, 4), 60(21, 22), 77(39, 40)
        [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
         64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85],
        #A - H_female
        [38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68,
         69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85],
        #V_female
        [29, 30, 32, 33, 35, 37, 38, 40, 41, 43, 45, 46, 48, 50, 51, 53, 54, 56, 58, 59, 61, 62, 64, 66, 67, 69, 70, 72, 74, 75, 77, 79, 80],
        #F_female
        [35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 77],
        #C_female
        [32, 34, 36, 38, 40, 42, 44, 46, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 74, 76, 78, 80, 82, 84, 85]
    ]
    #TEGグラフ用数値換算
    if ex_id == "teg":
        #男性用グラフ
        if current_user.gender == "male":
            for i in range(0, 5):
                for j in range(0, len(teg_m[i])):
                    if g_sum0[i] >= len(teg_m[i]):
                        g_sum.append(teg_m[i][len(teg_m[i])-1])
                        break
                    elif g_sum0[i] == j:
                        g_sum.append(teg_m[i][j])
                        break
        #女性用グラフ
        elif current_user.gender == "female":
            for i in range(0, 5):
                if i is 1:
                    for j in range(0, len(teg_f[i])):
                        if g_sum0[i] - 3 >= len(teg_f[i]):
                            g_sum.append(teg_f[i][len(teg_f[i]) - 1])
                            break
                        elif g_sum0[i] <= 3:
                            if g_sum0[i] == j:
                                g_sum.append(teg_f[i][j])
                                break
                        elif g_sum0[i] <= 21:
                            if g_sum0[i] - 1 == j:
                                g_sum.append(teg_f[i][j])
                                break
                        elif g_sum0[i] <= 39:
                            if g_sum0[i] - 2 == j:
                                g_sum.append(teg_f[i][j])
                                break
                        else:
                            if g_sum0[i] - 3 == j:
                                g_sum.append(teg_f[i][j])
                                break
                else:
                    for j in range(0, len(teg_f[i])):
                        if g_sum0[i] >= len(teg_f[i]):
                            g_sum.append(teg_f[i][len(teg_f[i])-1])
                            break
                        elif g_sum0[i] == j:
                            g_sum.append(teg_f[i][j])
                            break

    #POMSグラフ用数値換算
    elif ex_id == "pom":
        if current_user.gender == "male:":
            for i in range(0, 6):
                for j in range(0, len(pom_m[i])):
                    if g_sum0[i] >= len(pom_m[i]):
                        g_sum.append(pom_m[i][len(pom_m[i])-1])
                        break
                    elif g_sum0[i] == j:
                        g_sum.append(pom_m[i][j])
                        break
        elif current_user.gender == "female":
            for i in range(0, 6):
                for j in range(0, len(pom_f[i])):
                    if g_sum0[i] >= len(pom_f[i]):
                        g_sum.append(pom_f[i][len(pom_f[i])-1])
                        break
                    elif g_sum0[i] == j:
                        g_sum.append(pom_f[i][j])
                        break


#個別データ抽出及びデータ換算（POMS, TEG）
def ex_one_data(ex_id, result_id):
    #テスト結果取得
    g_fac = analyzer_service.setting_analyzer(ex_id).fac
    g_sum0 = views_service.find_one(ex_id, result_id).a_sum
    g_sum = []

    #データ換算
    if ex_id == "teg":
        g_fac.pop()
        conv_data(ex_id, g_sum0, g_sum)
    elif ex_id == "pom":
        conv_data(ex_id, g_sum0, g_sum)

    return g_fac, g_sum


#グラフ描画(teg, poms)(matplotlib_ver)
"""
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
"""
