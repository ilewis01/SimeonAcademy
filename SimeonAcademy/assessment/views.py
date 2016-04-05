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
MHRelationship, MHActivity, MHStressor, MHLegalHistory, ClientSession, SType, \
Invoice

from assessment.view_functions import convert_datepicker, generateClientID,\
getStateID, getReasonRefID, clientExist, getClientByName, getClientByDOB, \
getClientByID, getClientBySS, getEducationID, getLivingID, getMaritalID, \
amDemographicExist, findClientAM, clientAmExist, continueToAmSection, \
mhDemographicExist, clientMhExist, getClientMhList, findClientMH, \
continueToMhSection, getActiveClients, getDischargedClients, utExist, \
getUtsByDate, deleteOldUTS, getTimes, clientSAPExist, findClientSAP,\
getClientSAPList, continueToSAPSection, SAPDemographicExist, getAM_byDemographic

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

@login_required(login_url='/index')
def all_active_clients(request):
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
			clients = getActiveClients()
			content["clients"] = clients
			content['title'] = "Simeon Academy | All Active Clients"
			return render_to_response('counselor/client/active.html', content)

@login_required(login_url='/index')
def all_discharged_clients(request):
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
			clients = getDischargedClients()
			content["clients"] = clients
			content['title'] = "Simeon Academy | All Active Clients"
			return render_to_response('counselor/client/discharged.html', content)

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
			content['title'] = "Simeon Academy"
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
			content['title'] = "New Client | Simeon Academy"
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

			content['title'] = "New Client | Simeon Academy"
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
				content['title'] = "New Client | Simeon Academy"
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
			types = SType.objects.all()
			content['session_types'] = types
			content['title'] = "Client Search | Simeon Academy"
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
			search_type = request.POST.get('s-type', '')
			session_type = request.POST.get('stype', '')

			s_results = None
			phrase = None
			searched = None

			if search_type == "ss_num":
				getThis = request.POST.get('ss_num', '')
				search_type = "social security number"
				s_results = getClientBySS(getThis)
				searched = getThis
			elif search_type == "name":
				getFirst = request.POST.get('fname', '')
				getLast = request.POST.get('lname', '')
				search_type = "name"
				s_results = getClientByName(getFirst, getLast)
				searched = str(getFirst) + " " + str(getLast)
			elif search_type == "dob":
				getThis = request.POST.get('dob', '')
				search_type = "birthdate"
				s_results = getClientByDOB(getThis)
				searched = getThis
			elif search_type == "id":
				getThis = request.POST.get('client_ID', '')
				search_type = "client ID"
				s_results = getClientByID(getThis)
				searched = getThis

			matches = len(s_results)
			if matches == 1:
				phrase = 'result'
			else:
				phrase = 'results'

			content['title'] = "Client Search | Simeon Academy"
			content['matches'] = matches
			content['results'] = s_results
			content['phrase'] = phrase
			content['type'] = search_type
			content['session'] = session_type
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
			session_type = request.POST.get('session-type', '')
			session_type = SType.objects.get(id=session_type)
			client = Client.objects.get(id=clID)
			start = datetime.now()

			session = ClientSession(client=client, start=start, s_type=session_type)
			session.save()

			content['title'] = "Client Options | Simeon Academy"
			content['client'] = client
			content['session_type'] = session_type
			content['start'] = start
			content['session_id'] = session.id
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			first_drink = request.POST.get('first_drink', '')
			first_use_type = request.POST.get('first_use_type', '')
			ever_used_drugs = request.POST.get('ever_used', '')
			quitMos = request.POST.get('quitMos', '')
			quitYrs = request.POST.get('quitYrs', '')
			reason_quit = request.POST.get('reason_quit', '')
			currently_use_drugs = request.POST.get('use_drugs', '')
			what_you_use = request.POST.get('what-you-use', '')
			how_often_you_use = request.POST.get('how-often-you-use', '')
			how_much_you_use = request.POST.get('how-much-you-use', '')
			has_dui = request.POST.get('has_dui', '')
			dui_amount = request.POST.get('dui_amount', '')
			BAL = request.POST.get('BAL', '')
			need_help = request.POST.get('need_help', '')
			had_treatment = request.POST.get('treatment', '')
			when_treated = request.POST.get('when_treated', '')
			where_treated = request.POST.get('where_treated', '')
			completed_treatment = request.POST.get('completed_treatment', '')
			no_treat_explain = request.POST.get('no_treat_explain', '')
			still_abstinent = request.POST.get('still_abstinent', '')
			relapse_explain = request.POST.get('relapse_explain', '')
			drinking_last = request.POST.get('drinking_last', '')
			relationship_alc = request.POST.get('relationship_alc', '')

			session_id = request.POST.get('session_id', '')
			am_id = request.POST.get('am_id', '')

			session = ClientSession.objects.get(id=session_id)
			am = AngerManagement.objects.get(id=am_id)
			drug_history = AM_DrugHistory(client_id=session.client.clientID)

			if currently_use_drugs == 'yes':
				currently_use_drugs = True
			else:
				currently_use_drugs = False
			if ever_used_drugs == 'yes':
				ever_used_drugs = True
			else:
				ever_used_drugs = False
			if has_dui == 'yes':
				has_dui = True
			else:
				has_dui = False
			if had_treatment == 'yes':
				had_treatment = True
			else:
				had_treatment = False
			if completed_treatment == 'yes':
				completed_treatment = True
			else:
				completed_treatment = False
			if still_abstinent == 'yes':
				still_abstinent = True
			else:
				still_abstinent = False
			if drinking_last == 'yes':
				drinking_last = True
			else:
				drinking_last = False
			if need_help == 'yes':
				need_help = True
			else:
				need_help = False

			drug_history.firstDrinkAge = first_drink
			drug_history.firstDrinkType = first_use_type
			drug_history.curUse = currently_use_drugs
			drug_history.useType = what_you_use
			drug_history.amtPerWeek = how_often_you_use
			drug_history.useAmt = how_much_you_use
			drug_history.everDrank = ever_used_drugs
			drug_history.monthsQuit = quitMos
			drug_history.yearsQuit = quitYrs
			drug_history.reasonQuit = reason_quit
			drug_history.DUI = has_dui
			drug_history.numDUI = dui_amount
			drug_history.BALevel = BAL
			drug_history.drugTreatment = had_treatment
			drug_history.treatmentPlace = where_treated
			drug_history.dateTreated = when_treated
			drug_history.finishedTreatment = completed_treatment
			drug_history.reasonNotFinishedTreatment = no_treat_explain
			drug_history.isClean = still_abstinent
			drug_history.relapseTrigger = relapse_explain
			drug_history.drinkLastEpisode = drinking_last
			drug_history.drinkRelationshipProblem = relationship_alc
			drug_history.needHelpDrugs = need_help

			drug_history.save()
			am.drugHistory = drug_history
			am.drugHistoryComplete = True
			am.save()

			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
				content['title'] = "Counselor Home Page | Simeon Academy"
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
				content['title'] = "Anger Management Assessment | Simeon Academy"
				return render_to_response('counselor/forms/AngerManagement/demographic.html', content)
			elif str(action) == 'cancel':
				## return to the client options page
				content['title'] = "Client Options | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			client_id = request.POST.get('client_id', '')
			session_id = request.POST.get('session_id', '')

			client = Client.objects.get(id=client_id)			
			session = ClientSession.objects.get(id=session_id)

			proceed = findClientAM(client)
			am = proceed['am']

			if proceed['incomplete'] == True:
				content['am'] = am
				content['client'] = client
				content['title'] = "Anger Management Assessment | Simeon Academy"
				return render_to_response('counselor/forms/AngerManagement/getClient.html', content)
			else:
				marital = MaritalStatus.objects.all().order_by('status')
				living = LivingSituation.objects.all().order_by('situation')
				education = EducationLevel.objects.all().order_by('level')
				content['title'] = "Anger Management Assessment | Simeon Academy"
				content['client'] = client
				content['education'] = education
				content['marital'] = marital
				content['living'] = living
				content['session'] = session
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
			res_year = request.POST.get('res-yrs', '')
			rent_own  = request.POST.get('rentRAD', '')
			dep_children = request.POST.get('dep_children', '')
			dep_other = request.POST.get('dep_other', '')
			education = request.POST.get('edu', '')
			dropout = request.POST.get('dip', '')
			occupation = request.POST.get('occ', '')
			employer = request.POST.get('employer', '')
			employer_address = request.POST.get('em_add', '')
			employer_phone = request.POST.get('em_phone', '')
			mosJob = request.POST.get('mosJob', '')
			yrsJob = request.POST.get('yrsJob', '')
			healthy = request.POST.get('healRad', '')
			medicine = request.POST.get('medRad', '')
			health_explain = request.POST.get('explain', '')
			session_id = request.POST.get('session_id', '')
			am_id = request.POST.get('am_id', '')

			session = ClientSession.objects.get(id=session_id)

			reasonDo = "This is the reason for dropout"

			marital = MaritalStatus.objects.get(id=marital)
			living = LivingSituation.objects.get(id=living)
			education = EducationLevel.objects.get(id=education)

			if rent_own == "rent":
				rent_own = False
			else:
				rent_own = True

			if dropout == 'dropout':
				dropout = True
			else:
				dropout = False

			if healthy == 'not_healthy':
				healthy = True
			else:
				healthy = False

			if medicine == 'medication':
				medicine = True
			else:
				medicine = False

			demographic = AM_Demographic(client=session.client, date_of_assessment=date, maritalStatus=marital,\
				livingSituation=living, own=rent_own, months_res=res_month, years_res=res_year,\
				num_children=dep_children, other_dependants=dep_other, education=education, \
				drop_out=dropout, resasonDO=reasonDo, employee=employer, job_title=occupation, \
				emp_address=employer_address, employed_months=mosJob, employed_years=yrsJob, \
				employer_phone=employer_phone, health_problem=healthy, medication=medicine, health_exp=health_explain)

			moveForward = amDemographicExist(demographic)

			if moveForward['exist'] == False:
				demographic.save()
			else:
				demographic = moveForward['am_demo']

			angerManagement = AngerManagement(demographic=demographic, demographicComplete=True, AMComplete=False)
			checkAM = clientAmExist(session.client)

			if checkAM == False:
				angerManagement.save()
			else:
				angerManagement = getAM_byDemographic(demographic)['am']

			content['title'] = "Anger Management Assessment | Simeon Academy"
			content['AM'] = angerManagement
			content['session'] = session
			content['client'] = session.client
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
			content['title'] = "Anger Management Assessment | Simeon Academy"
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
def mh_location(request):
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
			action = request.POST.get('mh-choice', '')
			mh = request.POST.get('mh_id')
			mh = MentalHealth.objects.get(id=mh)
			client = mh.demographics.client
			content['client'] = mh.demographics.client

			if str(action) == 'finish-old':
				##go to the next section to be completed in the form
				content['mh'] = mh
				goToLocation = continueToMhSection(mh)
				content['title'] = "Simeon Academy | Counselor Home Page"
				return render_to_response(goToLocation, content)
			elif str(action) == 'start-new':
				##delete the current form and start at beginning of the am form
				mh.delete()
				content['title'] = "Simeon Academy | Anger Management Assessment"
				return render_to_response('counselor/forms/MentalHealth/demographic.html', content)
			elif str(action) == 'cancel':
				## return to the client options page
				content['title'] = "Simeon Academy | Client Options"
				return render_to_response('counselor/client/client_options.html', content)

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
			client_id = request.POST.get('client_ID', '')
			client = Client.objects.get(id=client_id)
			content['client'] = client
			proceed = findClientMH(client)

			if proceed['incomplete'] == True:
				content['mh'] = proceed['mh']
				return render_to_response('counselor/forms/MentalHealth/getClient.html', content)
			else:
				##remember to incluse all valid content for this form
				return render_to_response('counselor/forms/MentalHealth/demographic.html', content)

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

			moveForward = mhDemographicExist(demographic)

			if moveForward['exist'] == False:
				demographic.save()
			else:
				demographic = moveForward['mh_demo']

			mentalHealth = MentalHealth(demographics=demographic, demographicsComplete=True, MHComplete=False)

			checkMH = clientMhExist(client)

			if checkMH == False:
				mentalHealth.save()

			content['mh_id'] = mentalHealth.id
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
def sap_location(request):
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
			action = request.POST.get('sap-choice', '')
			sap = request.POST.get('sap_id')
			sap = SAP.objects.get(id=sap)
			client = sap.demographics.client
			content['client'] = sap.demographics.client

			if str(action) == 'finish-old':
				##go to the next section to be completed in the form
				content['sap'] = sap
				goToLocation = continueToSAPSection(sap)
				content['title'] = "Simeon Academy | SAP"
				return render_to_response(goToLocation, content)
			elif str(action) == 'start-new':
				##delete the current form and start at beginning of the am form
				times = getTimes()
				content['times'] = times
				if sap.demographics != None:
					sap.demographics.delete()
				if sap.psychoactive != None:
					sap.psychoactive.delete()
				sap.delete()
				content['title'] = "Simeon Academy | SAP"
				return render_to_response('counselor/forms/SAP/demographic.html', content)
			elif str(action) == 'cancel':
				## return to the client options page
				content['title'] = "Simeon Academy | Client Options"
				return render_to_response('counselor/client/client_options.html', content)

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
			client = request.POST.get('client_ID', '')
			client = Client.objects.get(id=client)
			times = getTimes()
			proceed = findClientSAP(client)

			content['client'] = client
			content['times'] = times
			content['title'] = "Simeon Academy | Urine Test Analysis"

			if proceed['incomplete'] == True:
				content['sap'] = proceed['sap']
				return render_to_response('counselor/forms/SAP/getClient.html', content)
			else:
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
			client_id = request.POST.get('client_id', '')
			date = request.POST.get('datepicker', '')
			start_time = request.POST.get('start-time', '')
			problem = request.POST.get('problem', '')
			health = request.POST.get('health', '')
			family = request.POST.get('family', '')

			client = Client.objects.get(id=client_id)
			date = convert_datepicker(date)
			date = date['date']

			demographic = SapDemographics(client=client, date1=date, startTime1=start_time,\
				problem=problem, health=health, family=family)

			moveForward = SAPDemographicExist(demographic)

			if moveForward['exist'] == False:
				demographic.save()
			else:
				demographic = moveForward['sap_demo']

			sap = SAP(demographics=demographic, demoComplet=True, SapComplete=False)

			checkSAP = clientSAPExist(client)

			if checkSAP == False:
				sap.save()

			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/SAP/psychoactive.html', content)

@login_required(login_url='/index')
def sap_psychoactive2(request):
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
			return render_to_response('counselor/forms/SAP/psychoactive2.html', content)

@login_required(login_url='/index')
def sap_special(request):
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
			return render_to_response('counselor/forms/SAP/special.html', content)

@login_required(login_url='/index')
def sap_preFinal(request):
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
			return render_to_response('counselor/forms/SAP/pre_final.html', content)

@login_required(login_url='/index')
def sap_final(request):
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
			times = getTimes()
			content['times'] = times
			content['title'] = "Simeon Academy | Urine Test Analysis"
			return render_to_response('counselor/forms/SAP/final.html', content)

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
			drugs = Drug.objects.all()
			client = request.POST.get('client_ID', '')
			client = Client.objects.get(id=client)
			content['client'] = client
			content['drugs'] = drugs
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
			drugs = Drug.objects.all()
			client_id = request.POST.get('client_id', '')
			client = Client.objects.get(id=client_id)
			date = request.POST.get('datepicker', '')
			date = convert_datepicker(date)
			date = date['date']
			ut = UrineResults(client=client, testDate=date)
			results = []

			for d in drugs:
				result = request.POST.get(d.drug, '')
				if str(result) == "Positive":
					results.append(d.drug)

			amount = len(results)
			phrase = None
			phrase2 = None

			if amount == 1:
				phrase = 'match'
				phrase2 = 'was'
			else:
				phrase = 'matches'
				phrase2 = 'were'

			if amount > 0:
				for i in range(amount):
					if i == 0:
						ut.drug1=results[i]
					elif i == 1:
						ut.drug2=results[i]
					elif i == 2:
						ut.drug3=results[i]
					elif i == 3:
						ut.drug4=results[i]
					elif i == 4:
						ut.drug5=results[i]
					elif i == 5:
						ut.drug6=results[i]
					elif i == 6:
						ut.drug7=results[i]
					elif i == 7:
						ut.drug8=results[i]
					elif i == 8:
						ut.drug9=results[i]
					elif i == 9:
						ut.drug10=results[i]
					elif i == 10:
						ut.drug11=results[i]
					elif i == 11:
						ut.drug12=results[i]

			if utExist(ut) == False:
				ut.save()
				content['ut'] = ut
				content['matches'] = amount
				content['results'] = results
				content['phrase'] = phrase
				content['phrase2'] = phrase2
				content['title'] = "Simeon Academy | Urine Test Results"
				return render_to_response('counselor/forms/UrineTest/viewForm.html', content)
			else:
				ut.save()
				uts = getUtsByDate(ut)
				formMatches = len(uts)
				content['matches'] = formMatches
				content['ut'] = ut
				content['uts'] = uts
				content['title'] = "ERROR"
				return render_to_response('counselor/forms/UrineTest/getClient.html', content)

@login_required(login_url='/index')
def ut_form_saved(request):
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
			ut_id = request.POST.get('ut_id', '')
			ut = UrineResults.objects.get(id=ut_id)
			content['ut'] = ut
			content['title'] = "Simeon Academy | Urine Test Results"
			return render_to_response('counselor/forms/UrineTest/form_created.html', content)

@login_required(login_url='/index')
def ut_form_saved2(request):
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
			choice = request.POST.get('ut_op', '')
			ut_id = request.POST.get('ut_id', '')
			ut = UrineResults.objects.get(id=ut_id)
			content['ut'] = ut
			content['title'] = "Simeon Academy | Urine Test Results"

			if str(choice) == 'keep':				
				return render_to_response('counselor/forms/UrineTest/form_created.html', content)
			elif str(choice) == 'delete':
				keepThis = ut
				deleteOldUTS(ut.testDate)
				ut.save()
				return render_to_response('counselor/forms/UrineTest/form_created.html', content)

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
			client = request.POST.get('client_ID', '')
			client = Client.objects.get(id=client)
			term = TermReason.objects.all()
			content['client'] = client
			content['term'] = term
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

## ADDICTION SEVERITY INDEX-----------------------------------------------------------
@login_required(login_url='/index')
def asi_demographic(request):
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
			client = request.POST.get('client_ID', '')
			content['client'] = client
			content['title'] = "Addiction Severity Index | Simeon Academy"
			return render_to_response('counselor/forms/ASI/asi_demographic.html', content)



































