# the flask sqlalchemy module acts as an ORM mapper that reduces the need for you to really know databases 
# It is an ORM for many relational databases not just one 
# to Install it we use the floowing command 
# pip install flask-sqlalchemy
# Database migrations - this helps change the structure of your database when updates are made to the database
# the installation process is by using the command pip install flask-migrate
# The flask sql-alchemy configurations are 

# we import the os module to enable the python to identify path for the database location
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# ... this is the first configuration of sql-alchemy
    # The Flask-SQLAlchemy extension takes the location of the application's
    #  database from the SQLALCHEMY_DATABASE_URI configuration variable.

# class Config(object):
    
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    #     # this 
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # The SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False to disable a feature of Flask-SQLAlchemy that I do not need, 
    # which is to signal the application every time a change is about to be made in the database.
    ##imports 


# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# data stored in the database is represented by a collection of classes which are reffered to as database models


# THE LAST BIT INVOLVES CREATING THE MIGRATION REPOSITORY NEEDED FOR THE DATABASE
# To accomplish this seemingly difficult task, Alembic maintains a migration repository,
#  which is a directory in which it stores its migration scripts. Each time a change is made to the database schema, a migration script is added to the repository with the details of the change.
#  To apply the migrations to a database, these migration scripts are executed in the sequence they were created.

# The flask db sub-command is added by Flask-Migrate to manage everything related to database migrations.
#  So let's create the migration repository for microblog by running flask db init:

# since the repository is established we can now make migrations  using the flask db migrate -m "message" command

# The flask db migrate sub-command generates these automatic migrations
# To apply the changes to the database, the flask db upgrade command must be used.

#  you also have a flask db downgrade command, which undoes the last migration. While you will be unlikely
#  to need this option on a production system, you may find it very useful during development.

# from app import routes, models

#  Multiple changes can be accumulated in a session and once all the changes have been registered 
#  you can issue a single db.session.commit(), which writes all the changes atomically. If at any 
#  time while working on a session there is an error, a call to db.session.rollback() will abort the 
#  session and remove any changes stored in it. The important 
#  thing to remember is that changes are only written to the database when db.session.commit() is called.

# db.session.add(model object) − inserts a record into mapped table

# db.session.delete(model object) − deletes record from table

# Resources to learn flask
# 1.Flask mega tutorial by miguel grinberg
# 2.EXplore flask open source book
# 3.learn to build web applications with flask and docker building SAAS
# 4.flask for fun and profits
# 5. How to structure large flask applications
# 6.Flask Blueprint templates shows a way of structuring your __init__.py file with blueprints for expanding projects into many files and modules.
# 7.If you're not sure why DEBUG should be set to False in a production deployment, be sure to read this article on how Patreon got hacked.

# 