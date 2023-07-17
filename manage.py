

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from seeders import seed
from app import flask_app
from app.plugins import db


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)

seeder = FlaskSeeder()
seeder.init_app(flask_app, db)

@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])

@manager.command('seed', with_appcontext=True)
def seed():
    return seeder(seed)

if __name__ == '__main__':
    manager()
