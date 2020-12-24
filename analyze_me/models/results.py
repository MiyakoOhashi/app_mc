#analyze_me/models/results.py       2020/12/10   M.O
from analyze_me import db
from datetime import datetime
#from sqlalchemy.dialects import postgresql as pg

#フュージョンチェックデータベース
class FU_results(db.Model):
    __tablename__ = 'fu_results'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    answers = db.Column(db.PickleType, nullable=True)
    #answers = db.Column(pg.ARRAY(db.String, dimensions=1), nullable=True)
    a_sum = db.Column(db.Integer, nullable=True)
    judge = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    @classmethod
    def from_args(cls, answers: [], a_sum: int, judge: str, user_id: int) -> object:
        instance = cls()
        instance.answers = answers
        instance.a_sum = a_sum
        instance.judge = judge
        instance.created_at = datetime.now()
        instance.user_id = user_id
        return instance

    def __repr__(self):
        return '<ID:{} answers:{} judge:{}>'.format(self.id, self.answers, self.judge)


#脱中心化チェックデータベース
class EQ_results(db.Model):
    __tablename__ = 'eq_results'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    answers = db.Column(db.PickleType, nullable=True)
    a_sum = db.Column(db.Integer, nullable=True)
    judge = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    @classmethod
    def from_args(cls, answers: [], a_sum: int, judge: str, user_id: int) -> object:
        instance = cls()
        instance.answers = answers
        instance.a_sum = a_sum
        instance.judge = judge
        instance.created_at = datetime.now()
        instance.user_id = user_id
        return instance

    def __repr__(self):
        return '<ID:{} answers:{} judge:{}>'.format(self.id, self.answers, self.judge)


# CES-Dデータベース
class CES_results(db.Model):
    __tablename__ = 'ces_results'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    answers = db.Column(db.PickleType, nullable=True)
    a_sum = db.Column(db.Integer, nullable=True)
    judge = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    @classmethod
    def from_args(cls, answers: [], a_sum: int, judge: str, user_id: int) -> object:
        instance = cls()
        instance.answers = answers
        instance.a_sum = a_sum
        instance.judge = judge
        instance.created_at = datetime.now()
        instance.user_id = user_id
        return instance

    def __repr__(self):
        return '<ID:{} answers:{} judge:{}>'.format(self.id, self.answers, self.judge)


#　POMSデータベース
class POM_results(db.Model):
    __tablename__ = 'pom_results'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    answers = db.Column(db.PickleType, nullable=True)
    a_sum = db.Column(db.PickleType, nullable=True)
    #judge = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    @classmethod
    def from_args(cls, answers: [], a_sum: [], user_id: int) -> object:
        instance = cls()
        instance.answers = answers
        instance.a_sum = a_sum
        #instance.judge = judge
        instance.created_at = datetime.now()
        instance.user_id = user_id
        return instance

    def __repr__(self):
        return '<ID:{} answers:{} judge:{}>'.format(self.id, self.answers, self.a_sum)


#　TEGデータベース
class TEG_results(db.Model):
    __tablename__ = 'teg_results'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    answers = db.Column(db.PickleType, nullable=True)
    a_sum = db.Column(db.PickleType, nullable=True)
    #judge = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    @classmethod
    def from_args(cls, answers: [], a_sum: [], user_id: int) -> object:
        instance = cls()
        instance.answers = answers
        instance.a_sum = a_sum
        #instance.judge = judge
        instance.created_at = datetime.now()
        instance.user_id = user_id
        return instance

    def __repr__(self):
        return '<ID:{} answers:{} judge:{}>'.format(self.id, self.answers, self.a_sum)
