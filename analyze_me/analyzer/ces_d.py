#analyze_me/analyzer/ces_d.py       2020/11/03   M.O
from flask import session

class CES_D:                           #CES-Dメインプログラム
    def __init__(self):
        #テストID
        self.id = "ces"
        #テスト名
        self.name = "CES-D"
        #サブ名
        self.sub = "現在のうつ傾向チェック"
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
        #回答選択肢リスト
        self.options = ["ない",
                        "１ー２日",
                        "３ー４日",
                        "５日以上"
                        ]

    def cal(self, ans):         #判定結果計算
        #回答追加
        session['answers'].append(self.options[ans])
        # 加算方法イレギュラーのもの（No.3, No.7, No.15）
        if session['que'] == 3 or session['que'] == 7 or session['que'] == 15:
            ans = 3 - ans
        #回答加算
        session['a_sum'] += ans

    def judge(self):     #テスト結果判定（うつ度）
        if session['a_sum'] >= 26:
            return "重度抑うつ"
        elif session['a_sum'] >= 21:
            return "中度抑うつ"
        elif session['a_sum'] >= 17:
            return "軽度抑うつ"
        else:
            return "正常"
