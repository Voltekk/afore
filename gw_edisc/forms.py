from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, BooleanField, validators

class CaseForm(Form):
	case_id = StringField('ID', [validators.Required()])
	case_classify = StringField('Classification', [validators.Required()])
	case_type = SelectField('Type')
	case_synopsis = TextAreaField('Synopsis')
	
class RequestForm(Form):
	request_caseid = SelectField('Case')
	request_id = StringField('ID', [validators.Required()])
	request_type = SelectField('Type')
	institution = StringField('Institution', [validators.Required()])
	requesters = StringField('Requesters', [validators.Required()])
	auth_contacts = StringField('Authorized Contacts')
	req_notes = TextAreaField('Notes')
	
class LoginForm(Form):
	user_name = StringField('Username', [validators.Required()])
	user_password = StringField('Password', [validators.Required()])
	user_remember = BooleanField('Remember Me')