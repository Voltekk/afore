from flask import Flask
from flask.ext.mongoengine import MongoEngine

# Create eDisc
app = Flask(__name__)

app.config['SECRET_KEY'] = 'super-secret'

# MongoDB Config
app.config['MONGODB_DB'] = 'gw_edisc'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

#Create mongo database connection object
db = MongoEngine(app)

from gw_edisc import views

if __name__ == '__main__':
	app.run()