from multiprocessing import Manager
from app import create_app,db
from app.models import User,Comments,Blogs
import app
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
app = create_app('test')


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Blogs = Blogs,Comments = Comments)
if __name__ == '__main__':
    manager.run()