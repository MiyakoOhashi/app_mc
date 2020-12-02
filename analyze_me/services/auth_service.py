#analyze_me/services/auth_service.py       2020/12/01   M.O
#ログイン関連データ処理ファイル
from flask_login import login_user, logout_user
from sqlalchemy.exc import SQLAlchemyError
from analyze_me import db
from analyze_me.models.user import User

#サインインサービス
def signup(data: {}) -> User:
    try:
        user_id = data.get('user_id')
        name = data.get('name')
        password = data.get('password')
        #ユーザ登録の有無を確認
        user = User.query.filter_by(user_id=user_id).first()
        print(user)
        if user:
            return user
        #ユーザ無の場合新規作成
        new_user = User.from_args(user_id, name, password)
        #データベース登録
        db.session.add(new_user)
        db.session.commit()
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError

#ログインサービス
def login(data: {}) -> User:
    try:
        print("id:{}, name:{}, rem:{}".format(data.get('user_id'), data.get('password'),data.get('remenber')))
        user_id = data.get('user_id')
        password = data.get('password')
        remenber = True if data.get('remenber') else False
        user = User.query.filter_by(user_id=user_id).first()
        #ユーザとパスワード確認
        if not user and not user.check_password(user.password, password):
            raise SQLAlchemyError

        #ログイン維持
        login_user(user, remenber=remenber)
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError

#ログアウトサービス
def logout():
    logout_user()
    return True
