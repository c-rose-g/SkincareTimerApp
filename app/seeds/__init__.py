from flask.cli import AppGroup
from .users import seed_users, undo_users
from app.models.db import db, environment, SCHEMA
# from .purchase_histories import seed_purchase_histories, undo_purchase_histories

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        # order: from most connected to least connected model

        undo_users()
    # Add other seed functions here
    # from least connected to most connected model
    seed_users()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
  # order: from most connected to least connected model
    # Add other undo functions here

    undo_users()
