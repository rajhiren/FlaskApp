#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Manage for flaskapp."""

import os

from flaskapp import create_app, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASKAPP_ENV') or 'dev')
manager = Manager(app)


migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
