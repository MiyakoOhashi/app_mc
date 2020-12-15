#analyze_me/models/results.py       2020/12/10   M.O
from analyze_me import db
from datetime import datetime
from sqlalchemy.dialects import postgresql as pg

class FU_result(db.Model):                    #フュージョンチェックメインプログラム
    __tablename__ = 'fu_result'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    answers = db.Column(pg.ARRAY(db.String, dimensions=1), nullable=True)
    a_sum = db.Column(db.Integer)
    jadge = db.Column(db.String(200))
    created_at = db.Column(db.DateTime)

    @classmethod
    def from_args(cls, user_id:str, answers:[], a_sum:int, jadge:str):
        instance = cls()
        instance.user_id = user_id
        instance.answers = answers
        instance.a_sum = a_sum
        instance.jadge = jadge
        instance.created_at = datetime.utcnow()
        print(instance)
        return instance

    def __repr__(self):
        return '<ID:{} answers:{} jadge:{}>'.format(self.id, self.answers, self.jadge)
