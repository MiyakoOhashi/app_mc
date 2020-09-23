#analyze_me/__init__.py       2020/9/17   M.O
from flask import Flask

app = Flask(__name__)
app.config.from_object('analyze_me.config')

import analyze_me.views