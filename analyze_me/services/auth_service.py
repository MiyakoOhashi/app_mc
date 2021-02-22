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
        username = data.get('username')
        password = data.get('password')
        gender = data.get('gender')
        #print("ID: {}, NAME: {}, PASS: {}, Gender: {}".format(user_id, username, password, gender))
        if not user_id or not username or not password or not gender:
            user = 'empty'
            new_user = None
            return user, new_user
        #ユーザ登録の有無を確認
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            new_user = None
            return user, new_user
        #ユーザ無の場合新規作成
        new_user = User.from_args(user_id, username, password, gender)
        #データベース登録
        db.session.add(new_user)
        db.session.commit()
        return user, new_user
    except SQLAlchemyError:
        raise SQLAlchemyError

#ログインサービス
def login(data: {}) -> User:
    try:
        user_id = data.get('user_id')
        password = data.get('password')
        remember = True if data.get('remember') else False
        print("ID: {}, PASS: {}, REM: {}".format(user_id, password, remember))
        if not user_id or not password:
            user = 'empty'
            return user
        user = User.query.filter_by(user_id=user_id).first()
        # ユーザ確認、パスワード確認
        if not user or not user.check_password(password):
            return
        #ユーザとパスワード確認
        #if not user and not user.check_password(user.password, password):
        #    raise SQLAlchemyError

        #ログイン維持
        login_user(user, remember=remember)
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError

#ログアウトサービス
def logout():
    logout_user()
    return True
