import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_restful import Api

from app.main import create_app, db
from app.main.src.api_routes import ApiRoutes
from app.main.config import DevelopmentConfig



# Instancie l'application
app = create_app(os.getenv('APP_SETTINGS') or 'dev')
api = Api(app)
ApiRoutes(api)

# Instancie le manager et la migration des classes
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()