#analyze_me/analyzer/poms.py       2020/11/06   M.O

class POMS:                           #フュージョンチェックメインプログラム
    def __init__(self):
        #テストID
        self.id = "pom"
        #テスト名
        self.name = "POMS"
        #サブ名
        self.sub = "現在のうつ傾向チェック"
        #説明
        self.desc = "準備中"
        #質問リスト
        self.queries = ["人付き合いが楽しい",
                        "希望が持てない",
                        "心の中でふんがいする",
                        "陽気な気持ち",
                        "考えがまとまらない",
                        "頭がすっきりする",
                        "がっかりしてやる気をなくす",
                        "迷惑をかけられて困る",
                        "疲れた",
                        "集中できない",
                        "いじわるしたい",
                        "自分はほめられるに値しないと感じる",
                        "他人を思いやれる",
                        "うろたえる",
                        "精力がみなぎる",
                        "ゆううつだ",
                        "ふきげんだ",
                        "神経がたかぶる",
                        "積極的な気持ちだ",
                        "悲しい",
                        "いらいらする",
                        "物事に気のりがしない",
                        "落ち着かない",
                        "あれこれ後悔する",
                        "頭が混乱する",
                        "生き生きする",
                        "ぐったりする",
                        "怒る",
                        "自分は不幸だ",
                        "他人の役に立つ気がする",
                        "同情する",
                        "どうも忘れっぽい",
                        "気がはりつめる",
                        "ヘトヘトだ",
                        "他人を信頼する",
                        "気持ちがくつろぐ",
                        "孤独でさびしい",
                        "すぐけんかしたくなる",
                        "頭がさえわたる",
                        "とほうに暮れる",
                        "内心ひどく腹立たしい",
                        "自分はみじめだ",
                        "他人にあたたかくできる",
                        "だるい",
                        "物事がてきぱきできる気がする",
                        "反抗したい",
                        "気持ちが沈んで暗い",
                        "もう何の望みもない",
                        "不安だ",
                        "元気がいっぱいだ",
                        "自分では何もできない",
                        "他人に裏切られた気がする",
                        "気がかりでそわそわする",
                        "心配事がなくていい気分だ",
                        "自分は価値がない人間だ",
                        "激しい怒りを感じる",
                        "うんざりだ",
                        "緊張する",
                        "何かにおびえる",
                        "物事に確信が持てない",
                        "活気がわいてくる",
                        "ひどくくたびれた",
                        "すぐかっとなる",
                        "罪悪感がある",
                        "あれこれ心配だ"
                        ]
        self.q_len = len(self.queries)
        self.q_range = range(self.q_len)
        self.que = 0
        #回答選択肢リスト
        self.options = ["まったくなかった",
                        "少しあった",
                        "まあまああった",
                        "かなりあった",
                        "非常に多くあった"
                        ]
        self.o_range = range(len(self.options))
        #回答格納リスト
        self.answers = []
        #回答合計値
        self.a_sum = [ 0, 0, 0, 0, 0, 0 ]
        self.f_range = range(len(self.a_sum))
        #self.a_sum = {"fa":0, "d":0, "ah":0, "v":0, "f":0, "c":0}
        #因子設定
        self.fac = ["fa", "d", "ah", "v", "f", "c"]

    def cal(self, ans):         #判定結果計算
        #各因子に関する項目
        fa = [14, 18, 23, 33, 36, 49, 53, 58, 65]
        d = [2, 7, 12, 16, 20, 24, 29, 37, 42, 47, 48, 51, 55, 59, 64]
        ah = [3, 8, 11, 17, 21, 28, 38, 41, 46, 52, 56, 63]
        v = [4, 15, 19, 26, 39, 50, 54, 61]
        f = [9, 22, 27, 34, 44, 57, 62]
        c = [5, 10, 25, 32, 40, 45, 60]

        self.answers.append(self.options[ans])

        if self.que+1 == 36 or self.que+1 == 45:
            ans = 4 - ans

        if self.que+1 in fa:
            self.a_sum[0] += ans
        elif self.que+1 in d:
            self.a_sum[1] += ans
        elif self.que+1 in ah:
            self.a_sum[2] += ans
        elif self.que+1 in v:
            self.a_sum[3] += ans
        elif self.que+1 in f:
            self.a_sum[4] += ans
        elif self.que+1 in c:
            self.a_sum[5] += ans

        self.que += 1
        print("ただいまの質問：{}".format(self.que))
        print("回答：{}".format(self.answers))
        print("合計値：{}".format(self.a_sum))

    def judge(self, a_sum):     #テスト結果判定（フュージョン傾向）
        pass
        #print("判定：{}".format(self.judge0))