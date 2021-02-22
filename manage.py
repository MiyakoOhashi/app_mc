#manage.py      2020/09/30  M.O
from flask_script import Manager
from analyze_me import create_app
from analyze_me.scripts.db import InitDB, DropDB

if __name__ == '__main__':
    manager = Manager(create_app)
    manager.add_command('init_db', InitDB())
    manager.add_command('drop_db', DropDB())
    manager.run()