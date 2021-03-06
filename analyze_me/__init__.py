#analyze_me/__init__.py       2020/9/17   M.O
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#sqlalchemyを通しflaskからdbへアクセスする入口
db = SQLAlchemy()

#app生成
def create_app(test_config=None):
    # Flaskアプリ生成
    app = Flask(__name__)

    #コンフィグ召喚
    app.config.from_object('analyze_me.config')

    #テストコンフィグ召喚
    if test_config:
        app.config.from_mapping(test_config)

    #アプリケーションとデータベースの紐付け
    db.init_app(app)

    # flask-loginに関する設定
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # DBインポート
    from analyze_me.models.user import User
    from analyze_me.models.results import FU_results, EQ_results, \
        CES_results, POM_results, TEG_results

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #blueprint（views）インポート
    from analyze_me.views.views import views
    app.register_blueprint(views)

    #blueprint（auth）インポート
    from analyze_me.views.auth import auth
    app.register_blueprint(auth)

    #blueprint（analyzes）インポート
    from analyze_me.views.analyzes import analyzes
    app.register_blueprint(analyzes, url_prefix='/analyzes')

    return app

