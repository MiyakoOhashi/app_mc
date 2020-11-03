#analyze_me/analyzer/ces_d.py       2020/11/03   M.O

class CES_D:                           #CES-Dメインプログラム
    def __init__(self):
        #テストID
        self.id = "ces"
        #テスト名
        self.name = "CES-D"
        #説明
        self.desc = "準備中"
        #質問リスト
        self.queries = ["普段は何でもないことがわずらわしい",
                        "食べなくない。食欲が落ちた",
                        "家族や友達に励ましてもらっても、気分が晴れない",
                        "他の人と同じ程度には、能力があると思う",
                        "物事に集中できない",
                        "ゆううつだ",
                        "何をするにも面倒だ",
                        "これから先のことについて積極的に考えることができる",
                        "過去のことについてくよくよ考える",
                        "何か恐ろしい気持ちがする",
                        "なかなか寝られない",
                        "生活について不満なく過ごせる",
                        "普段より口数が少ない、口が重い",
                        "一人ぼっちでさみしい",
                        "皆がよそよそしいと思う",
                        "毎日が楽しい",
                        "急に泣き出すことがある",
                        "悲しいと感じる",
                        "皆が自分を嫌っていると感じる",
                        "仕事が手に付かない"
                        ]
        self.q_len = len(self.queries)
        self.q_range = range(self.q_len)
        self.que = 0
        #回答選択肢リスト
        self.options = ["ない",
                        "１ー２日",
                        "３ー４日",
                        "５日以上"
                        ]
        self.o_range = range(len(self.options))
        #回答格納リスト
        self.answers = []
        #回答合計値
        self.a_sum = 0

    def cal(self, ans):         #判定結果計算
        self.answers.append(self.options[ans])
        if self.que == 3 or self.que == 7 or self.que == 15:
            ans = 3 - ans
        self.a_sum += ans
        self.que += 1
        print("回答：{}".format(self.answers))
        print("合計値：{}".format(self.a_sum))
        print("ただいまの質問：{}".format(self.que))
        print("質問レンジ{}".format(self.q_range))

    def judge(self, a_sum):     #テスト結果判定（脱中心化傾向）
        if a_sum >= 26:
            self.judge0 = "重度抑うつ"
        elif a_sum >= 21:
            self.judge0 = "中度抑うつ"
        elif a_sum >= 17:
            self.judge0 = "軽度抑うつ"
        else:
            self.judge0 = "正常"
        print("判定：{}".format(self.judge0))