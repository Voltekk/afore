from flask import Flask, render_template, request, url_for, redirect, flash
from flask.ext.wtf import Form

from gw_edisc import app
from gw_edisc import db
from gw_edisc.forms import CaseForm, RequestForm
from gw_edisc.models import Case, Request

# Views
@app.route('/login')
#@login-required
def signon():
    return render_template("login.html")

'''View to list all cases (active or closed)'''    
@app.route('/cases/')
def case_list(): 
	cases = Case.objects.order_by('-created_at')
	return render_template('list_cases.html',
		cases = cases)

'''View to list details of selected case (active or closed)''' 	
@app.route('/cases/<int:case_id>/')
def case_detail():
	return 'Detail of case #{}.'. format(case_id)

'''Form to create a new case'''	
@app.route('/cases/create/', methods=['GET','POST'])
def case_create():
	case = Case()
	form = CaseForm(obj=case)
	form.case_type.choices = [('criminal','Criminal'),('civil','Civil')]
	
	if request.method == 'POST' and form.validate_on_submit():
		form.populate_obj(case)
		case.save()
		return redirect('/cases')
	elif request.method == 'GET':
		return render_template('create_case.html',
			form = form)
	
'''Form to edit an existing case'''		
@app.route('/cases/<int:case_id>/edit/', methods=['GET','POST'])
def case_edit():
	return 'Form to edit a case.'

'''View to list all requests (active or closed)'''	
@app.route('/requests/')
def request_list(): 
	requests = Request.objects.order_by('-created_at')
		
	return render_template('list_requests.html',
		requests = requests)

'''Form to create a new request'''	
@app.route('/requests/create/', methods=['GET','POST'])
def req_create():
	case = Case()
	req = Request()
	form = RequestForm(obj=req)
	
	case_ids = Case.objects.all().only('case_id')
	ids = []
	for id in case_ids:
		ids.append((str(id.case_id).lower(),str(id.case_id)))
		
	form.request_caseid.choices = ids 
	form.request_type.choices = [('collection','Collection'),('production','Production'),('conversion','Conversion')]
	
	if request.method == 'POST' and form.validate_on_submit():
		form.populate_obj(req)
		req.save()
		return redirect('/requests')
	elif request.method == 'GET':
		return render_template('create_request.html',
			form = form)
			
#@app.route('/test/')
#def show_test():
#		
#	return render_template('test.html',
#		tup = tup)
			
'''Gracefully shut down the Flask server'''
@app.route('/shutdown')
def shutdown():	
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Server is shutting down!"

#@app.route('/test/')
