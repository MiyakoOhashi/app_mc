#analyze_me/models/analyzer.py       2020/12/04   M.O
from analyze_me import db
from datetime import datetime
from sqlalchemy.dialects import postgresql as pg
from analyze_me.analyzer.fu_check import FU
from analyze_me.analyzer.eq_check import EQ
from analyze_me.analyzer.ces_d import CES_D
from analyze_me.analyzer.poms import POMS
from analyze_me.analyzer.teg import TEG

class Analyzer(db.Model):                    #フュージョンチェックメインプログラム
    __tablename__ = 'analyzer'
    id = db.Column(db.Integer, primary_key=True)
    ex_id = db.Column(db.String(10))
    name = db.Column(db.String(30))
    sub = db.Column(db.String(100))
    desc = db.Column(db.String(1000))
    queries = db.Column(pg.ARRAY(db.String, dimensions=1), nullable=True)
    options = db.Column(pg.ARRAY(db.String, dimensions=1), nullable=True)
    #que = db.Column(db.Integer)
    #created_at = db.Column(db.DateTime)
    user_id = db.Column(db.String(50))

    @classmethod
    def from_args(cls, ex_id:str, user_id:str):
        if ex_id == "fu":
            examin = FU()
        elif ex_id == "eq":
            examin = EQ()
        elif ex_id == "ces":
            examin = CES_D()
        elif ex_id == 'pom':
            examin = POMS()
        elif ex_id == "teg":
            examin = TEG()

        instance = cls()
        instance.ex_id = examin.id
        instance.name= examin.name
        instance.sub = examin.sub
        instance.desc = examin.desc
        instance.queries = examin.queries
        instance.options = examin.options
        #instance.que = 0
        instance.user_id = user_id
        print(instance)
        return instance

    def cal(self, ans):         #判定結果計算
        self.answers.append(self.options[ans])
        self.a_sum += ans
        self.que += 1
        #print("ただいまの質問：{}".format(self.que))
        #print("回答：{}".format(self.answers))
        #print("合計値：{}".format(self.a_sum))

    def judge(self, a_sum):     #テスト結果判定（フュージョン傾向）
        if a_sum > 27:
            self.judge0 = "思考と現実を混同し、考え込みやすい傾向があります"
        elif a_sum == 27:
            self.judge0 = "一般平均値です"
        else:
            self.judge0 = "思考と現実を混同しやすい傾向は薄いです"
        #print("判定：{}".format(self.judge0))
