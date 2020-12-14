#analyze_me/services/analyzer_service.py       2020/12/10   M.O
#ログイン関連データ処理ファイル
from sqlalchemy.exc import SQLAlchemyError
from analyze_me import db
from analyze_me.models.analyzer import Analyzer

#アナライザ生成サービス
def create_ana(ex_id, user_id) -> Analyzer:
    try:
        #ユーザ登録の有無を確認
        ana = Analyzer.query.filter_by(ex_id=ex_id, user_id=user_id).first()
        if ana:
            return ana
        #ユーザ無の場合新規作成
        new_ana = Analyzer.from_args(ex_id. user_id)
        #データベース登録
        db.session.add(new_ana)
        db.session.commit()

        ana = Analyzer.query.get()
        return ana
    except SQLAlchemyError:
        raise SQLAlchemyError

