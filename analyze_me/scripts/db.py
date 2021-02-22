#analyze_me/scripts/db.py       2020/9/30   M.O
from flask_script import Command
from analyze_me import db

class InitDB(Command):
    "create database"
    def run(self):
        db.create_all()

class DropDB(Command):
    "drop database"
    def run(self):
        db.drop_all()