#analyze_me/analyzer/fu_check.py       2020/10/08   M.O

class FU:                           #フュージョンチェックメインプログラム
    def __init__(self):
        #テストID
        self.id = "fu"
        #テスト名
        self.name = "FU-Check"
        #サブ名
        self.sub = "フュージョン傾向チェック"
        #説明
        self.desc = "準備中"
        #質問リスト
        self.queries = ["自分の思考が、苦悩や心の痛みの原因になっている",
                        "考えていることに囚われすぎて、自分が一番したいことをすることができない",
                        "自分に役に立たない位にまで、状況の分析をしすぎてしまう",
                        "自分自身の考えと苦闘する",
                        "特定のことを考えてしまうことで、自分に動揺する",
                        "自分の考えにかなり巻き込まれがちだ",
                        "動揺するような考えに執着しないほうが自分の役に立つと分かっていても、そうすることにとても苦労する"
                        ]
        #回答選択肢リスト
        self.options = ["全く当てはまらない",
                        "極稀に当てはまる",
                        "稀に当てはまる",
                        "時に当てはまる",
                        "かなり当てはまる",
                        "ほとんどいつも当てはまる",
                        "いつも当てはまる"
                        ]

    def cal(self, ans, ses):         #判定結果計算
        #回答追加
        ses['answers'].append(self.options[ans])
        #回答加算
        ses['a_sum'] += ans

        print("ただいまの質問：{}".format(ses['que']))
        print("ANSWER：{}".format(ses['answers']))
        print("A_SUM: {}".format(ses['a_sum']))

    def judge(self, a_sum):     #テスト結果判定（フュージョン傾向）
        if a_sum > 27:
            return "思考と現実を混同し、考え込みやすい傾向があります"
        elif a_sum == 27:
            return "一般平均値です"
        else:
            return "思考と現実を混同しやすい傾向は薄いです"





