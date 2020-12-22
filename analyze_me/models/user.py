#analyze_me/models/user.py       2020/11/30   M.O
from analyze_me import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

#個人情報エントリ
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime)

    fu_results = relationship('FU_results')

    @classmethod
    def from_args(cls, user_id:str, name:str, password:str):
        instance = cls()
        instance.user_id = user_id
        instance.name= name
        if password is not None:
            instance.hash_password(password)
        instance.created_at = datetime.utcnow()
        return instance

    def hash_password(self, clean_password):
        self.password = generate_password_hash(str(clean_password), method='sha256')

    def check_password(self, clean_password):
        return check_password_hash(self.password, clean_password)

    def __repr__(self):
        return '<Entry id:{} name:{} user_id:{}>'.format(self.id, self.name, self.user_id)



