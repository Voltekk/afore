import datetime
from flask.ext.mongoengine import MongoEngine
from flask import url_for
from gw_edisc import db

class Case(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	case_id = db.StringField(max_length=50, required=True)
	case_nickname = db.StringField(max_length=50, required=False)
	case_classify = db.StringField(max_length=50, required=False)
	case_type = db.StringField(max_length=50, required=True)
	case_synopsis = db.StringField(max_length=1000, required=False)
	case_status = db.StringField(max_length=50, required=False)

	meta = {'collection': 'cases',
			'ordering': ['-created_at']
	}
	
class Request(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	request_type =  db.StringField(max_length=50, required=True)
	institution =  db.StringField(max_length=50, required=True)
	requesters =  db.StringField(max_length=50, required=True)
	auth_contacts = db.StringField(max_length=50, required=True)
	request_id = db.StringField(max_length=50, required=True)
	notes = db.StringField(max_length=1000, required=False)
	status = db.StringField(max_length=50, required=False)

	meta = {'collection': 'requests',
			'ordering': ['-created_at']
	}