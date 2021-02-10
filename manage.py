#manage.py      2020/09/30  M.O
from flask_script import Manager
from analyze_me import creat_app
from analyze_me.scripts.db import InitDB

if __name__ == '__main__':
    manager = Manager(creat_app)
    manager.add_command('init_db', InitDB())
    manager.run()