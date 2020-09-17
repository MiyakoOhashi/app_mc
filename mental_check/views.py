#mental_check/views.py       2020/9/17   M.O
from flask import request, redirect, url_for, \
    render_template, flash, session
from mental_check import app


@app.route('/')
def show_entries():
    return render_template('entries/index.html')