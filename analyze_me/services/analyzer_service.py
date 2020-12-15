#analyze_me/services/analyzer_service.py       2020/12/10   M.O
#ログイン関連データ処理ファイル
from sqlalchemy.exc import SQLAlchemyError
from analyze_me import db
from analyze_me.models.results import FU_result

#データ格納サービス
def store_data(user_id, ses) :
    try:
        ex_id = ses['ex_id']
        answers = ses['answers']
        a_sum = ses['a_sum']
        judge = ses['judge']

        if ex_id == 'fu':
            new_res = FU_result.from_args(user_id, answers, a_sum, judge)
        #データベース登録
        db.session.add(new_res)
        db.session.commit()
        return new_res

    except SQLAlchemyError:
        raise SQLAlchemyError

