#analyze_me/services/views_service.py       2020/12/24   M.O
#ログ表示関連データ処理ファイル
from flask import session
from flask_login import current_user
from sqlalchemy.exc import SQLAlchemyError
from analyze_me import db
from analyze_me.models.results import FU_results, EQ_results, \
    CES_results, POM_results, TEG_results

#全データ検索
def find_all(ex_id):
    if ex_id == 'fu':
        return FU_results.query.filter(FU_results.user_id == current_user.id).order_by(FU_results.id.desc()).all()
    elif ex_id == 'eq':
        return EQ_results.query.filter(EQ_results.user_id == current_user.id).order_by(EQ_results.id.desc()).all()
    elif ex_id == 'ces':
        return CES_results.query.filter(CES_results.user_id == current_user.id).order_by(CES_results.id.desc()).all()
    elif ex_id == 'pom':
        session['pom_fac'] = ["fa", "d", "ah", "v", "f", "c"]
        return POM_results.query.filter(POM_results.user_id == current_user.id).order_by(POM_results.id.desc()).all()
    elif ex_id == 'teg':
        session['teg_fac'] = ["cp", "np", "a", "fc", "ac", "l"]
        return TEG_results.query.filter(TEG_results.user_id == current_user.id).order_by(TEG_results.id.desc()).all()

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

#データ削除
def delete(ex_id, result_id):
    if not result_id:
        raise Exception
    elif ex_id =="fu":
        result = FU_results.query.filter_by(id=result_id).first()
    elif ex_id =="eq":
        result = EQ_results.query.filter_by(id=result_id).first()
    elif ex_id =="ces":
        result = CES_results.query.filter_by(id=result_id).first()
    elif ex_id =="pom":
        result = POM_results.query.filter_by(id=result_id).first()
    elif ex_id =="teg":
        result = TEG_results.query.filter_by(id=result_id).first()

    db.session.delete(result)
    db.session.commit()
