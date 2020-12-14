#analyze_me/analyzer/eq_check.py       2020/11/03   M.O

class EQ:                           #EQ（脱中心化）チェックメインプログラム
    def __init__(self):
        #テストID
        self.id = "eq"
        #テスト名
        self.name = "EQ-Check"
        #サブ名
        self.sub = "脱中心化チェック"
        #説明
        self.desc = "準備中"
        #質問リスト
        self.queries = ["私は、自分自身をあるがままに受け入れることができる",
                        "私は、ストレスを感じている時であっても、自分の考えを落ち着かせることができる",
                        "私は、自分の考えや感情から自分自身を切り離すことができる",
                        "私は、周囲の状況に対して落ち着いて応じることができる",
                        "私は、自分自身を思いやりを持って扱うことができる",
                        "私は、不快な感情に飲み込まれることなく、その感情を観察することができる",
                        "私は、自分の周囲や自分自身の内側で起きてることに十分気づいている感覚がある",
                        "私は、自分自身が自分の思考とは別物であることを実際に認識できる",
                        "私は、自分の身体の感覚全体を意識的に感じるようにしている",
                        "私は、より広い視野で物事を捉える"
                        ]
        #self.q_len = len(self.queries)
        #self.q_range = range(self.q_len)
        #self.que = 0
        #回答選択肢リスト
        self.options = ["全く当てはまらない",
                        "いく分当てはまる",
                        "どちらでもない",
                        "かなりよく当てはまる",
                        "非常によく当てはまる"
                        ]
        #self.o_range = range(len(self.options))
        #回答格納リスト
        self.answers = []
        #回答合計値
        self.a_sum = 0

    def cal(self, ans, que):         #判定結果計算
        self.answers.append(self.options[ans])
        self.a_sum += ans
        #self.que += 1
        print("ただいまの質問：{}".format(que))
        print("回答：{}".format(self.answers))
        print("合計値：{}".format(self.a_sum))

    def judge(self, a_sum):     #テスト結果判定（脱中心化傾向）
        if a_sum >= 25:
            self.judge0 = "思考と距離を置き、思考に巻き込まれずに判断している傾向：高い"
        else:
            self.judge0 = "思考と距離を置き、思考に巻き込まれずに判断している傾向：低い"
        print("判定：{}".format(self.judge0))


