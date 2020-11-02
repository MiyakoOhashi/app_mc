#analyze_me/analyzer/fu_check.py       2020/10/08   M.O

class FU:                           #フュージョンチェックメインプログラム
    def __init__(self):
        #テストID
        self.id = "fu"
        #テスト名
        self.name = "FUチェック"
        #説明
        self.desc = "準備中"
        #質問リスト
        self.queries = ["自分の思考が、苦悩や心の痛みの原因になっている                                           ",
                        "考えていることに囚われすぎて、自分が一番したいことをすることができない                        ",
                        "自分に役に立たない位にまで、状況の分析をしすぎてしまう                                     ",
                        "自分自身の考えと苦闘する                                                             ",
                        "特定のことを考えてしまうことで、自分に動揺する                                           ",
                        "自分の考えにかなり巻き込まれがちだ                                                     ",
                        "動揺するような考えに執着しないほうが自分の役に立つと分かっていても、そうすることにとても苦労する   "
                        ]
        self.q_len = len(self.queries)
        self.que = 0
        #回答選択肢リスト
        self.options = ["全く当てはまらない",
                        "極稀に当てはまる",
                        "稀に当てはまる",
                        "時に当てはまる",
                        "かなり当てはまる",
                        "ほとんどいつも当てはまる",
                        "いつも当てはまる"
                        ]
        self.o_len = range(len(self.options))
        #回答格納リスト
        self.answers = []
        #回答合計値
        self.a_sum = 0

    def cal(self, ans):
        self.answers.append(ans)
        self.a_sum += ans
        self.que += 1
        print("回答：{}".format(self.answers))
        print("合計値：{}".format(self.a_sum))
        print("ただいまの質問：{}".format(self.que))

    def judge(self, a_sum):     #テスト結果判定（フュージョン傾向）
        if a_sum > 27:
            self.judge0 = "思考と現実を混同し、考え込みやすい傾向があります"
        elif a_sum == 27:
            self.judge0 = "一般平均値です"
        else:
            self.judge0 = "思考と現実を混同しやすい傾向は薄いです"

"""
        print("\nフュージョン尺度チェックを開始します。\n各項目に対し、当てはまる内容を番号で回答して下さい。\n")
        for i in range(len(self.query)):
            print("問{}. {}".format(i + 1, self.query[i]))
            self.en.opt.print_opt()
            while True:             #エラー時再入力処理
                self.res0 = input("回答: ")
                try:
                    self.res = int(self.res0)
                    self.rs.cal(self.res, self.en.opt.option[self.res - 1])
                    break
                except (IndexError, ValueError):
                    print("!!１〜７で回答して下さい!!")
            print("\n")
"""



