#analyze_me/config.py       2020/9/17   M.O

#データベースの設定
SQLALCHEMY_DATABASE_URI = 'sqlite:///analyze_me.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#SESSION情報暗号化（ランダム値設定推奨）
SECRET_KEY = 'secret_key'

#デバッグ設定
DEBUG = True
#USERID = 'john'
#USERNAME = 'john'
#PASSWORD = 'due123'