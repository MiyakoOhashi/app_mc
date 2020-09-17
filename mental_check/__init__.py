#mental_check/__init__.py       2020/9/17   M.O
from flask import Flask

app = Flask(__name__)
app.config.from_object('mental_check.config')

import mental_check.views