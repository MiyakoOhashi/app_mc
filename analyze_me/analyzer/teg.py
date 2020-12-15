#analyze_me/analyzer/teg.py       2020/11/09   M.O

class TEG:                           #フュージョンチェックメインプログラム
    def __init__(self):
        #テストID
        self.id = "teg"
        #テスト名
        self.name = "TEG-Egogram"
        # サブ名
        self.sub = "性格傾向チェック"
        #説明
        self.desc = "準備中"
        #質問リスト
        self.queries = ["他人の言うことに左右されやすい",
                        "納得のいかないことに抗議する",
                        "ユーモアのセンスがある",
                        "他人の評価が気になる",
                        "寛大である",
                        "他人の話を聞くときに根拠を求める",
                        "他人の目を気にして行動することが多い",
                        "心が広い",
                        "一度決めたことがよくぐらつく",
                        "いつも楽しいことを探している",
                        "物事には常に原因があるから結果があると考える",
                        "理屈っぽい",
                        "人の気持ちがよくわかる",
                        "良いと思うことは貫く",
                        "議論を好む",
                        "何かを始める前には情報を集める",
                        "新しいことをやってみることが多い",
                        "のびのびと振る舞うことができる",
                        "他人に指図されることが多い",
                        "夜更かしをすることがまったくない",
                        "何気ない気配りをする",
                        "人見知りをしない",
                        "自分に厳しい",
                        "一度決めたことはやりとおす",
                        "人の気持ちがなごむように話をする",
                        "責任感が強い",
                        "夢を見たことがない",
                        "しばしば人から言われた通りに行動してしまう",
                        "他人に指図されるより指図する方が多い",
                        "人を笑わせることが得意である",
                        "人の顔色をうかがってしまう",
                        "人助けをすることに喜びを感じる",
                        "物事を言葉できちんと説明できる",
                        "人の言うことが気になる",
                        "親身になって行動する",
                        "優柔不断である",
                        "常にその場を楽しむことができる",
                        "事実の確認を行う",
                        "予測して行動する",
                        "人に優しい言葉をかける",
                        "良くないことは指摘する",
                        "論理的である",
                        "筋道立てて考える",
                        "みんなとにぎやかに騒ぐのが好きだ",
                        "明るい",
                        "決断することが苦手である",
                        "風邪を引いたことがまったくない",
                        "人には温かく接している",
                        "よく笑う",
                        "言うべきことは言う",
                        "ついリーダーシップをとってしまう",
                        "人の役に立つように行動する",
                        "常に向上心を持つ"
                        ]
        #self.q_len = len(self.queries)
        #self.q_range = range(self.q_len)
        #self.que = 0
        #回答選択肢リスト
        self.options = ["いいえ",
                        "どちらでもない",
                        "はい"
                        ]
        #self.o_range = range(len(self.options))
        #回答格納リスト
        #self.answers = []
        #回答合計値
        #self.a_sum = [ 0, 0, 0, 0, 0, 0 ]
        #self.f_range = range(len(self.a_sum))
        #self.a_sum = {"cp":0, "np":0, "a":0, "fc":0, "ac":0, "l":0}
        #因子設定
        self.fac = ["cp", "np", "a", "fc", "ac", "l"]

    def cal(self, ans, ses):         #判定結果計算
        # 各因子に関する項目
        cp = [2, 14, 23, 24, 26, 29, 41, 50, 51, 53]
        np = [5, 8, 13, 21, 25, 32, 35, 40, 48, 52]
        a = [6, 11, 12, 15, 16, 33, 38, 39, 42, 43]
        fc = [3, 10, 17, 18, 22, 30, 37, 44, 45, 49]
        ac = [1, 4, 7, 9, 19, 28, 31, 34, 46, 46]
        l = [20, 27, 47]

        #self.answers.append(self.options[ans])
        ses['answers'].append(self.options[ans])

        que = ses['que']
        if que+1 in cp:
            #self.a_sum[0] += ans
            ses['a_sum'][0] += ans
        elif que+1 in np:
            #self.a_sum[1] += ans
            ses['a_sum'][1] += ans
        elif que+1 in a:
            #self.a_sum[2] += ans
            ses['a_sum'][2] += ans
        elif que+1 in fc:
            #self.a_sum[3] += ans
            ses['a_sum'][3] += ans
        elif que+1 in ac:
            #self.a_sum[4] += ans
            ses['a_sum'][4] += ans
        elif que+1 in l:
            #self.a_sum[5] += ans
            ses['a_sum'][5] += ans

        #self.que += 1
        print("ただいまの質問：{}".format(que))
        #print("回答：{}".format(self.answers))
        #print("合計値：{}".format(self.a_sum))
        print("ANSWER：{}".format(ses['answers']))
        print("A_SUM: {}".format(ses['a_sum']))
        #print("因子数{}".format(self.f_range))

    def judge(self, ses):     #テスト結果判定（フュージョン傾向）
        pass
        #print("判定：{}".format(self.judge0))