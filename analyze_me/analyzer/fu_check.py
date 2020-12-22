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
        #self.q_len = len(self.queries)
        #self.q_range = range(self.q_len)
        #self.que = 0
        #回答選択肢リスト
        self.options = ["全く当てはまらない",
                        "極稀に当てはまる",
                        "稀に当てはまる",
                        "時に当てはまる",
                        "かなり当てはまる",
                        "ほとんどいつも当てはまる",
                        "いつも当てはまる"
                        ]
        #self.o_range = range(len(self.options))
        #回答格納リスト
        #self.answers = []
        #回答合計値
        #self.a_sum = 0

    def cal(self, ans, ses):         #判定結果計算
        #self.answers.append(self.options[ans])
        #self.a_sum += ans
        ses['answers'].append(self.options[ans])
        ses['a_sum'] += ans
        #self.que += 1
        print("ただいまの質問：{}".format(ses['que']))
        #print("回答：{}".format(self.answers))
        #print("合計値：{}".format(self.a_sum))
        print("ANSWER：{}".format(ses['answers']))
        print("A_SUM: {}".format(ses['a_sum']))

    def judge(self, a_sum):     #テスト結果判定（フュージョン傾向）
        if a_sum > 27:
            return "思考と現実を混同し、考え込みやすい傾向があります"
        elif a_sum == 27:
            return "一般平均値です"
        else:
            return "思考と現実を混同しやすい傾向は薄いです"
        #print("判定：{}".format(ses['judge']))





