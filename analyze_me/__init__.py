#analyze_me/__init__.py       2020/9/17   M.O
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('analyze_me.config')
#db = SQLAlchemy(app)

from analyze_me.views.analyzes import analyzes
app.register_blueprint(analyzes, url_prefix='/analyzes')

from analyze_me.views import views