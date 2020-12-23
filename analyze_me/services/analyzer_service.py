#analyze_me/services/analyzer_service.py       2020/12/10   M.O
#ログイン関連データ処理ファイル
from sqlalchemy.exc import SQLAlchemyError
from analyze_me import db
from analyze_me.models.results import FU_results, EQ_results
from analyze_me.analyzer.fu_check import FU
from analyze_me.analyzer.eq_check import EQ
from analyze_me.analyzer.ces_d import CES_D
from analyze_me.analyzer.poms import POMS
from analyze_me.analyzer.teg import TEG

#変数設定
def set_param(ex_id, ses):
    ses['ex_id'] = ex_id
    ses['que'] = 0
    #ses['judge'] = None
    ses['answers'] = []
    if ex_id == "teg" or ex_id == "pom":        #TEG, POMS
        ses['a_sum'] = [ 0, 0, 0, 0, 0, 0 ]
    else:                                       #FU, EQ, CES-D
        ses['a_sum'] = 0

#テストセッティング
def setting_analyzer(ex_id):
    if not ex_id:
        raise Exception
    elif ex_id == "fu":
        return FU()
    elif ex_id == "eq":
        return EQ()
    elif ex_id == 'ces':
        return CES_D()
    elif ex_id == 'pom':
        return POMS()
    elif ex_id == 'teg':
        return TEG()
    print("EX_ID:{}".format(ex_id))

#全データ検索
def find_all(ex_id):
    if ex_id == 'fu':
        return FU_results.query.all()
    elif ex_id == 'eq':
        return EQ_results.query.all()
    elif ex_id == 'ces':
        #return CES_results.query.all()
        pass
    elif ex_id == 'pom':
        #return POM_results.query.all()
        pass
    elif ex_id == 'teg':
        #return TEG_results.query.all()
        pass

#選択データ検索
def find_one(ex_id, result_id):
    if not result_id:
        raise Exception
    elif ex_id == "fu":
        return FU_results.query.filter_by(id=result_id).first()
    elif ex_id == "eq":
        return EQ_results.query.filter_by(id=result_id).first()
    elif ex_id == "ces":
        #return CES_results.query.filter_by(id=result_id).first()
        pass
    elif ex_id == "pom":
        #return POM_results.query.filter_by(id=result_id).first()
        pass
    elif ex_id == "teg":
        #return TEG_results.query.filter_by(id=result_id).first()
        pass

#データ格納
def save(user_id, ses) :
    try:
        if ses['ex_id'] == 'fu':
            new_res = FU_results.from_args(
                answers= ses['answers'],
                a_sum=ses['a_sum'],
                judge=ses['judge'],
                user_id=user_id
            )

        elif ses['ex_id'] == 'eq':
            new_res = EQ_results.from_args(
                answers=ses['answers'],
                a_sum=ses['a_sum'],
                judge=ses['judge'],
                user_id=user_id
            )

        """
            elif ses['ex_id'] == 'ces':
                new_res = CES_results.from_args(
                    answers=ses['answers'],
                    a_sum=ses['a_sum'],
                    judge=ses['judge'],
                    user_id=user_id
            )

        """
        #データベース追加
        db.session.add(new_res)
        #データベース登録
        db.session.commit()
        print("USER_ID: {}, ID: {}, ANSWERS: {}".format(new_res.user_id, new_res.id, new_res.answers))
        print("S_SUM: {}, JUDGE: {}, DATE: {}".format(new_res.a_sum, new_res.judge, new_res.created_at))
        return new_res.id
    except SQLAlchemyError:
        raise SQLAlchemyError

