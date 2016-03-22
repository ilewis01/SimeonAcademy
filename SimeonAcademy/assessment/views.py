from django.shortcuts import render_to_response, redirect
from django.template.loader import get_template
from django.conf import settings
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader, Context
from datetime import datetime
from datetime import date
import json as simplejson
from xhtml2pdf import pisa
from django.core import serializers

from assessment.models import State, RefReason, Client, MaritalStatus, \
LivingSituation, AngerManagement, EducationLevel, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, UseTable, \
FamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHFamily, MHEducation, \
MHRelationship, MHActivity, MHStressor, MHLegalHistory

from assessment.view_functions import convert_datepicker, generateClientID,\
getStateID, getReasonRefID, clientExist, getClientByName, getClientByDOB, \
getClientByID, getClientBySS, getEducationID, getLivingID, getMaritalID, \
amDemographicExist, findClientAM, clientAmExist, continueToAmSection

## LOGIN VIEWS---------------------------------------------------------------------------------
def index(request):
	return render_to_response('global/index.html')

def login(request):
	content = {}
	content.update(csrf(request))
	return render_to_response('global/login.html', content)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        if user.account.is_counselor == True:
        	return HttpResponseRedirect('/adminHome/')
        else:
        	return HttpResponseRedirect('/clientHome')

    else:
        return HttpResponseRedirect('/global/invalid_login')

def invalid_login(request):
	return render_to_response('global/invalid_login.html')

def newProfile(request):
	return render_to_response('global/new_user.html')

@login_required(login_url='/index')
def logout(request):
	auth.logout(request)
	return render_to_response('global/logout.html')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## CLIENT VIEWS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='/index')
def clientHome(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		content['title'] = "Simeon Academy | Client Home Page"
		return render_to_response('client/home.html', content)

@login_required(login_url='/index')
def client_appointment(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		content['title'] = "Simeon Academy | Schedule Appointment"
		return render_to_response('client/new_appointment.html', content)

@login_required(login_url='/index')
def client_documents(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		content['title'] = "Simeon Academy | My Documents"
		return render_to_response('client/view_documents.html', content)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## COUNSELOR VIEWS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@login_required(login_url='/index')
def adminHome(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Administrative Home Page"
			return render_to_response('counselor/home.html', content)

@login_required(login_url='/index')
def newClient(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			states = State.objects.all().order_by('state')
			refs = RefReason.objects.all().order_by('reason')
			content['states'] = states
			content['refs'] = refs
			content['title'] = "Simeon Academy | New Client"
			return render_to_response('counselor/client/new_client.html', content)

@login_required(login_url='/index')
def confirmNewClient(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content.update(csrf(request))
			fname = request.POST.get('fname', '')
			lname = request.POST.get('lname', '')
			mi = request.POST.get('mi', '')
			street_no = request.POST.get('street-no', '')
			street_name = request.POST.get('street-name', '')
			apt = request.POST.get('apt', '')
			city = request.POST.get('city', '')
			state = request.POST.get('state', '')
			zip_code = request.POST.get('zip', '')
			ss_num = request.POST.get('ss_num', '')
			dob = request.POST.get('dob', '')
			intake_date = request.POST.get('datepicker', '')
			em_contact = request.POST.get('ec', '')
			reason = request.POST.get('reasonRef', '')
			phone = request.POST.get('phone', '')
			em_phone = request.POST.get('ep', '')
			email = request.POST.get('email', '')
			gender = request.POST.get('gender', '')

			state = State.objects.get(id=state)
			reason = RefReason.objects.get(id=reason)

			content['fname'] = fname
			content['lname'] = lname
			content['mi'] = mi
			content['street_no'] = street_no
			content['street_name'] = street_name
			content['apt'] = apt
			content['city'] = city
			content['state'] = state
			content['zip'] = zip_code
			content['ss_num'] = ss_num
			content['dob'] = dob
			content['intake_date'] = intake_date
			content['ec'] = em_contact
			content['reason'] = reason
			content['phone'] = phone
			content['ep'] = em_phone
			content['email'] = email
			content['gender'] = gender

			content['title'] = "Simeon Academy | New Client"
			return render_to_response('counselor/client/verify_client.html', content)

@login_required(login_url='/index')
def clientCreated(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content.update(csrf(request))
			fname = request.POST.get('fname', '')
			lname = request.POST.get('lname', '')
			mi = request.POST.get('mi', '')
			street_no = request.POST.get('street_no', '')
			street_name = request.POST.get('street_name', '')
			apt = request.POST.get('apt', '')
			city = request.POST.get('city', '')
			state = request.POST.get('state', '')
			zip_code = int(request.POST.get('zip', ''))
			ss_num = request.POST.get('ss_num', '')
			dob = request.POST.get('dob', '')
			intake_date = request.POST.get('intake_date', '')
			em_contact = request.POST.get('ec', '')
			reason = request.POST.get('reason', '')
			phone = request.POST.get('phone', '')
			em_phone = request.POST.get('ep', '')
			email = request.POST.get('email', '')
			gender = request.POST.get('gender', '')

			dob = convert_datepicker(dob)
			dob = dob['date']
			intake_date = convert_datepicker(intake_date)
			intake_date = intake_date['date']

			client_id = generateClientID(lname)
			state = getStateID(state)
			reason = getReasonRefID(reason)

			if gender == 'Male':
				gender = True
			else:
				gender = False

			client = Client(fname=fname, middleInit=mi, lname=lname, isMale=gender, \
				street_no=street_no, street_name=street_name, apartment_no=apt, \
				city=city, state=State.objects.get(id=state), zip_code=zip_code, ss_num=ss_num, dob=dob,\
				intake_date=intake_date, emer_contact_name=em_contact, \
				reason_ref=RefReason.objects.get(id=reason), phone=phone, emer_phone=em_phone, email=email, \
				isDischarged=False, clientID=client_id)
			commit = clientExist(client)
			content['client'] = client

			print "Intake Date: " + str(client.intake_date)
			print "DOB: " + str(client.dob)
			print "Reason: " + str(client.reason_ref)
			print "Exist?: " + str(commit)
			print "State: " + str(client.state)

			if commit == False:
				client.save()
				content['title'] = "Simeon Academy | New Client"
				return render_to_response('counselor/client/client_created.html', content)
			else:
				content['title'] = 'ERROR: CLIENT EXIST'
				return render_to_response('counselor/client/client_exist.html', content)

@login_required(login_url='/index')
def searchClients(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html')

		else:
			content['title'] = "Simeon Academy | Client Search"
			return render_to_response('counselor/client/search_clients.html', content)

@login_required(login_url='/index')
def clientSearchResults(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			search_type = request.POST.get('search-radio', '')
			s_results = None
			phrase = None
			searched = None

			if search_type == "ssNumSearch":
				getThis = request.POST.get('ss_num', '')
				search_type = "Social Security Number"
				s_results = getClientBySS(getThis)
				searched = getThis
			elif search_type == "nameSearch":
				getFirst = request.POST.get('fname', '')
				getLast = request.POST.get('lname', '')
				search_type = "Name"
				s_results = getClientByName(getFirst, getLast)
				searched = str(getFirst) + " " + str(getLast)
			elif search_type == "dobSearch":
				getThis = request.POST.get('dob', '')
				search_type = "Birthdate"
				s_results = getClientByDOB(getThis)
				searched = getThis
			elif search_type == "clientIDSearch":
				getThis = request.POST.get('client_ID', '')
				search_type = "Client ID"
				s_results = getClientByID(getThis)
				searched = getThis

			matches = len(s_results)
			if matches == 1:
				phrase = 'result'
			else:
				phrase = 'results'

			content['title'] = "Simeon Academy | Client Search"
			content['matches'] = matches
			content['results'] = s_results
			content['phrase'] = phrase
			content['type'] = search_type
			content['searched'] = searched
			return render_to_response('counselor/client/client_search_results.html', content)

@login_required(login_url='/index')
def clientOptions(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			clID = request.POST.get('cli-id', '')
			client = Client.objects.get(id=clID)
			content['title'] = "Simeon Academy | Client Options"
			content['client'] = client
			return render_to_response('counselor/client/client_options.html', content)

## ANGER MANAGEMENT VIEWS-----------------------------------------------------
@login_required(login_url='/index')
def am_preliminary(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/getClient.html', content)

@login_required(login_url='/index')
def am_angerHistory(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/angerHistory.html', content)

@login_required(login_url='/index')
def am_angerTarget(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/AngerTarget.html', content)

@login_required(login_url='/index')
def am_childhood(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/childhoodHistory.html', content)

@login_required(login_url='/index')
def am_connections(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/connections.html', content)

@login_required(login_url='/index')
def am_control(request):
	user = request.user
	if not user.is_authenticated():
		content.update(csrf(request))
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/control.html', content)

@login_required(login_url='/index')
def am_location(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			action = request.POST.get('am-choice', '')
			am = request.POST.get('am_id')
			am = AngerManagement.objects.get(id=am)
			client = am.demographic.client
			content['client'] = am.demographic.client

			if str(action) == 'finish-old':
				##go to the next section to be completed in the form
				content['am'] = am
				goToLocation = continueToAmSection(am)
				content['title'] = "Simeon Academy | Counselor Home Page"
				return render_to_response(goToLocation, content)
			elif str(action) == 'start-new':
				##delete the current form and start at beginning of the am form
				am.delete()
				marital = MaritalStatus.objects.all().order_by('status')
				living = LivingSituation.objects.all().order_by('situation')
				education = EducationLevel.objects.all().order_by('level')
				content['education'] = education
				content['marital'] = marital
				content['living'] = living
				content['title'] = "Simeon Academy | Anger Management Assessment"
				return render_to_response('counselor/forms/AngerManagement/demographic.html', content)
			elif str(action) == 'cancel':
				## return to the client options page
				content['title'] = "Simeon Academy | Client Options"
				return render_to_response('counselor/client/client_options.html', content)

@login_required(login_url='/index')
def am_problems(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/currentProblems.html', content)

@login_required(login_url='/index')
def am_demographic(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			client = Client.objects.get(id=(request.GET['client_ID']))
			proceed = findClientAM(client)
			am = proceed['am']

			if proceed['incomplete'] == True:
				content['am'] = am
				content['client'] = client
				content['title'] = "Simeon Academy | Anger Management Assessment"
				return render_to_response('counselor/forms/AngerManagement/getClient.html', content)
			else:
				marital = MaritalStatus.objects.all().order_by('status')
				living = LivingSituation.objects.all().order_by('situation')
				education = EducationLevel.objects.all().order_by('level')
				content['title'] = "Simeon Academy | Anger Management Assessment"
				content['client'] = client
				content['education'] = education
				content['marital'] = marital
				content['living'] = living
				return render_to_response('counselor/forms/AngerManagement/demographic.html', content)
			
@login_required(login_url='/index')
def am_drugHistory(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			date = datetime.now()
			date = date.date()
			marital = request.POST.get('marital', '')
			living = request.POST.get('living', '')
			res_month = request.POST.get('res-mo', '')
			res_year = request.POST.get('res-yr', '')
			res_type = request.POST.get('rentRAD', '')
			dep_children = request.POST.get('dep_children', '')
			dep_other = request.POST.get('dep_other', '')
			education = request.POST.get('edu', '')
			graduate = request.POST.get('dip', '')
			occupation = request.POST.get('occ', '')
			employer = request.POST.get('employer', '')
			employer_address = request.POST.get('em_add', '')
			employer_phone = request.POST.get('em_phone', '')
			mosJob = request.POST.get('mosJob', '')
			yrsJob = request.POST.get('yrsJob', '')
			heal = request.POST.get('heal', '')
			med = request.POST.get('med', '')
			health_explain = request.POST.get('explain', '')
			client_id = request.POST.get('client_id', '')
			client = Client.objects.get(id=client_id)

			reasonDo = 'Rememebr to change this shit'

			marital = getMaritalID(marital)
			living = getLivingID(living)
			education = getEducationID(education)

			marital = MaritalStatus.objects.get(id=marital)
			living = LivingSituation.objects.get(id=living)
			education = EducationLevel.objects.get(id=education)

			if res_type == "Own":
				res_type = True
			else:
				res_type = False

			if graduate == 'Dropout':
				graduate = True
			else:
				graduate = False

			if heal == 'Healthy':
				heal = False
			else:
				heal = True

			if med == 'On meds':
				med = True
			else:
				med = False

			demographic = AM_Demographic(client=client, date_of_assessment=date, maritalStatus=marital,\
				livingSituation=living, own=res_type, months_res=res_month, years_res=res_year,\
				num_children=dep_children, other_dependants=dep_other, education=education, \
				drop_out=graduate, resasonDO=reasonDo, employee=employer, job_title=occupation, \
				emp_address=employer_address, employed_months=mosJob, employed_years=yrsJob, \
				employer_phone=employer_phone, health_problem=heal, medication=med, health_exp=health_explain)

			moveForward = amDemographicExist(demographic)

			if moveForward['exist'] == False:
				demographic.save()
			else:
				demographic = moveForward['am_demo']

			angerManagement = AngerManagement(demographic=demographic, demographicComplete=True, AMComplete=False)
			checkAM = clientAmExist(client)

			if checkAM == False:
				angerManagement.save()

			content['title'] = "Simeon Academy | Anger Management Assessment"
			content['AM'] = angerManagement.id
			return render_to_response('counselor/forms/AngerManagement/drugHistory.html', content)

@login_required(login_url='/index')
def am_familyOrigin(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/familyOrigin.html', content)

@login_required(login_url='/index')
def am_final(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/final.html', content)

@login_required(login_url='/index')
def am_viewForm(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/viewForm.html', content)

@login_required(login_url='/index')
def am_worst(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Anger Management Assessment"
			return render_to_response('counselor/forms/AngerManagement/worstEpisodes.html', content)

## MENTAL HEALTH VIEWS--------------------------------------------------------
@login_required(login_url='/index')
def mh_preliminary(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/getClient.html', content)

@login_required(login_url='/index')
def mh_activity(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/activity.html', content)

@login_required(login_url='/index')
def mh_demographic(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			client = Client.objects.get(id=(request.GET['client_ID']))
			content['client'] = client
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/demographic.html', content)

@login_required(login_url='/index')
def mh_education(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/education.html', content)

@login_required(login_url='/index')
def mh_familyBackground(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			client = request.POST.get('client_id', '')
			dob = request.POST.get('dob', '')
			bp = request.POST.get('bp', '')
			raised = request.POST.get('raised', '')
			occ = request.POST.get('occ', '')
			employer = request.POST.get('employer', '')
			ep_yrs = request.POST.get('ep_yrs', '')
			ep_mos = request.POST.get('ep_mos', '')
			pe = request.POST.get('pe', '')
			no_marriages = request.POST.get('no_marriages', '')
			residence = request.POST.get('residence', '')
			income = request.POST.get('income', '')
			credit = request.POST.get('credit', '')
			debt = request.POST.get('debt', '')
			hc = request.POST.get('hc', '')
			other = request.POST.get('other', '')

			client = Client.objects.get(id=client)

			demographic = MHDemographic(client=client, birthplace=bp, raised=raised, no_marriages=no_marriages,\
				occupation=occ, employer=employer, employedMo=ep_mos, employedYrs=ep_yrs, pastJobs=pe, \
				residence=residence, income=income, debt=debt, credit=credit, healthCare=hc, otherIncome=other)

			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/familyBackground.html', content)

@login_required(login_url='/index')
def mh_familyHistory(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/familyHistory.html', content)

@login_required(login_url='/index')
def mh_legal(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/legal.html', content)

@login_required(login_url='/index')
def mh_relationships(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/relationships.html', content)

@login_required(login_url='/index')
def mh_stress(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/stressors.html', content)

@login_required(login_url='/index')
def mh_useTable(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/useTable.html', content)

@login_required(login_url='/index')
def mh_viewForm(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/viewForm.html', content)

## SAP VIEWS------------------------------------------------------------------
@login_required(login_url='/index')
def sap_preliminary(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | S.A.P Form"
			return render_to_response('counselor/forms/SAP/getClient.html', content)

@login_required(login_url='/index')
def sap_demographic(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/SAP/demographic.html', content)

@login_required(login_url='/index')
def sap_psychoactive(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/SAP/psychoactive.html', content)

@login_required(login_url='/index')
def sap_viewForm(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/SAP/viewForm.html', content)

## URINE TEST VIEWS-----------------------------------------------------------
@login_required(login_url='/index')
def ut_preliminary(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/UrineTest/getClient.html', content)

@login_required(login_url='/index')
def ut_testResults(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/UrineTest/testResults.html', content)

@login_required(login_url='/index')
def ut_viewForm(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/UrineTest/viewForm.html', content)

## DISCHARGE VIEWS------------------------------------------------------------
@login_required(login_url='/index')
def discharge_preliminary(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Discharge"
			return render_to_response('counselor/forms/Discharge/getClient.html', content)

@login_required(login_url='/index')
def discharge_client(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Discharge"
			return render_to_response('counselor/forms/Discharge/clientDischarge.html', content)

@login_required(login_url='/index')
def discharge_viewForm(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy | Discharge"
			return render_to_response('counselor/forms/Discharge/viewForm.html', content)


































