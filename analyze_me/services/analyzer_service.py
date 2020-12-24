#analyze_me/services/analyzer_service.py       2020/12/10   M.O
#ログイン関連データ処理ファイル
from flask import session
from sqlalchemy.exc import SQLAlchemyError
from analyze_me import db
from analyze_me.models.results import FU_results, EQ_results, \
    CES_results, POM_results, TEG_results
from analyze_me.analyzer.fu_check import FU
from analyze_me.analyzer.eq_check import EQ
from analyze_me.analyzer.ces_d import CES_D
from analyze_me.analyzer.poms import POMS
from analyze_me.analyzer.teg import TEG

#変数設定
def set_param(ex_id):
    session['ex_id'] = ex_id
    session['que'] = 0
    #session['judge'] = None
    session['answers'] = []
    if ex_id == "teg" or ex_id == "pom":        #TEG, POMS
        session['a_sum'] = [ 0, 0, 0, 0, 0, 0 ]
    else:                                       #FU, EQ, CES-D
        session['a_sum'] = 0


# セッション情報削除
def delete_param():
    session.pop('ex_id', None)
    session.pop('answers', None)
    session.pop('a_sum', None)
    session.pop('judge', None)
    session.pop('que', None)


#アナライザ設定
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
        return CES_results.query.all()
    elif ex_id == 'pom':
        session['pom_fac'] = ["fa", "d", "ah", "v", "f", "c"]
        return POM_results.query.all()
    elif ex_id == 'teg':
        session['teg_fac'] = ["cp", "np", "a", "fc", "ac", "l"]
        return TEG_results.query.all()

#選択データ検索
def find_one(ex_id, result_id):
    if not result_id:
        raise Exception
    elif ex_id == "fu":
        return FU_results.query.filter_by(id=result_id).first()
    elif ex_id == "eq":
        return EQ_results.query.filter_by(id=result_id).first()
    elif ex_id == "ces":
        return CES_results.query.filter_by(id=result_id).first()
    elif ex_id == "pom":
        return POM_results.query.filter_by(id=result_id).first()
    elif ex_id == "teg":
        return TEG_results.query.filter_by(id=result_id).first()

#データ格納
def save(user_id) :
    try:
        if session['ex_id'] == 'fu':
            new_res = FU_results.from_args(
                answers= session['answers'],
                a_sum=session['a_sum'],
                judge=session['judge'],
                user_id=user_id
            )

        elif session['ex_id'] == 'eq':
            new_res = EQ_results.from_args(
                answers=session['answers'],
                a_sum=session['a_sum'],
                judge=session['judge'],
                user_id=user_id
            )

        elif session['ex_id'] == 'ces':
            new_res = CES_results.from_args(
                answers=session['answers'],
                a_sum=session['a_sum'],
                judge=session['judge'],
                user_id=user_id
            )

        elif session['ex_id'] == 'pom':
            new_res = POM_results.from_args(
                answers=session['answers'],
                a_sum=session['a_sum'],
                user_id=user_id
            )

        elif session['ex_id'] == 'teg':
            new_res = TEG_results.from_args(
                answers=session['answers'],
                a_sum=session['a_sum'],
                user_id=user_id
            )

        #データベース登録
        db.session.add(new_res)
        db.session.commit()

        # セッション情報削除
        delete_param()

        #print("USER_ID: {}, ID: {}, ANSWERS: {}".format(new_res.user_id, new_res.id, new_res.answers))
        #print("S_SUM: {}, JUDGE: {}, DATE: {}".format(new_res.a_sum, new_res.judge, new_res.created_at))

        return new_res.id
    except SQLAlchemyError:
        raise SQLAlchemyError

