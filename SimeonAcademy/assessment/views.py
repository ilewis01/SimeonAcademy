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
import json
import json as simplejson
from xhtml2pdf import pisa
from django.core import serializers

from assessment.models import State, RefReason, Client, MaritalStatus, \
LivingSituation, AngerManagement, EducationLevel, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, UseTable, \
FamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_AngerHistory2, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHFamily, MHEducation, \
MHRelationship, MHActivity, MHStressor, MHLegalHistory, ClientSession, SType, \
Invoice, AM_AngerHistory3

from assessment.view_functions import convert_datepicker, generateClientID,\
getStateID, getReasonRefID, clientExist, getClientByName, getClientByDOB, \
getClientByID, getClientBySS, getEducationID, getLivingID, getMaritalID, \
amDemographicExist, findClientAM, clientAmExist, continueToAmSection, \
mhDemographicExist, clientMhExist, getClientMhList, findClientMH, \
continueToMhSection, getActiveClients, getDischargedClients, utExist, \
getUtsByDate, deleteOldUTS, getTimes, clientSAPExist, findClientSAP,\
getClientSAPList, continueToSAPSection, SAPDemographicExist, getAM_byDemographic, \
getAmDHData, amDhExist, getAMDemoFields, convert_phone, newAM, deleteAM, startAM, \
startSession, refreshAM, getAMFields, onTrue_offFalse, amSidebarImages, \
grabAmCompletedSections, grabAmClassesCSS, grabAmSideBarString, convertToPythonBool, \
resolveBlankRadio, convertRadioToBoolean, truePythonBool, blankMustDie, phone_to_integer, \
grabProperNextSection, saveCompletedAmSection, grabSapImages

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
			new_session = request.POST.get('new_session', '')
			goToNext = request.POST.get('goToNext', '')					
			client = Client.objects.get(id=clID)
			start = datetime.now()
			phone = convert_phone(client.phone)

			session = None
			session_type = None

			if new_session == 'false':
				session_id = request.POST.get('session_id', '')
				session = ClientSession.objects.get(id=session_id)
				session_type = session.s_type.session_type

			else:
				session_type = request.POST.get('session-type', '')
				session_type = SType.objects.get(id=session_type)
				session = startSession(client, session_type)


			# session = ClientSession(client=client, start=start, s_type=session_type)
			# session.save()

			content['title'] = "Client Options | Simeon Academy"
			content['goToNext'] = goToNext
			content['phone'] = phone
			content['client'] = client
			content['session_type'] = session_type
			content['start'] = start
			content['session_id'] = session.id
			content['session'] = session
			content['back'] = 'false'
			return render_to_response('counselor/client/client_options.html', content)

## ANGER MANAGEMENT VIEWS-----------------------------------------------------
@login_required(login_url='/index')
def exit_am(request):
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
			am_id = request.POST.get('am_id', '')
			session_id = request.POST.get('session_id', '')
			exit_type = request.POST.get('exit_type_sub', '')

			am = AngerManagement.objects.get(id=am_id)
			session = ClientSession.objects.get(id=session_id)

			header_phrase = None
			sub1_phrase = None
			status = None
			trigger_btn = None

			if exit_type == 'Delete':
				header_phrase = 'Delete Anger Management Form'
				sub1_phrase = 'Are you sure you want to delete the following form?'
			elif exit_type == 'Save':
				header_phrase = "Save Current Anger Management Form"
				sub1_phrase = 'Are you sure you want to save the following form?'

			if am != None:
				if am.AMComplete == True:
					status = 'Complete'
				else:
					status = 'Incomplete'

			content['AM'] = am
			content['exit_type'] = exit_type
			content['session'] = session
			content['trigger_btn'] = exit_type
			content['status'] = status
			content['header_phrase'] = header_phrase
			content['sub1_phrase'] = sub1_phrase
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/forms/AngerManagement/confirm_exit.html', content)

@login_required(login_url='/index')
def am_deleted(request):
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
			session = request.POST.get('session_id', '')
			am = request.POST.get('am_id', '')
			exit_type = request.POST.get('exit_type_sub')

			session = ClientSession.objects.get(id=session)
			am = AngerManagement.objects.get(id=am)
			client = session.client

			if am == None:
				content['exit_sub_phrase'] = exit_sub_phrase
				content['title'] = "Session Options | Error"
				return render_to_response('counselor/forms/AngerManagement/am_doesNotExist.html', content)
			
			else:
				content['client'] = client
				content['session'] = session
				content['client_id'] = client.id
				content['session_id'] = session.id
				content['back'] = 'false'
				content['save_section'] = '/am_demographic/'
				content['goToNext'] = 'false'

				exit_sub_phrase = None

				if str(exit_type) == 'Delete':
					deleteAM(am)
					exit_sub_phrase = 'Deleted'

					content['exit_sub_phrase'] = exit_sub_phrase
					content['title'] = "Session Options | Simeon Academy"
					return render_to_response('counselor/forms/AngerManagement/am_deleted.html', content)
					
				elif str(exit_type) == 'Save':
					#First save current AM then return to client options page
					exit_sub_phrase = 'Saved'
					
					content['exit_sub_phrase'] = exit_sub_phrase
					content['title'] = "Session Options | Simeon Academy"
					return render_to_response('counselor/client/am_deleted.html', content)		

			
@login_required(login_url='/index')
def am_preliminary(request):
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
			return render_to_response('counselor/forms/AngerManagement/am_doesNotExist.html', content)


@login_required(login_url='/index')
def am_previouslyDeleted(request):
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)			

			if str(back) == 'false':
				saveCompletedAmSection(request, save_section, am)
			
			fields = getAMFields(am, 'counselor/forms/AngerManagement/angerHistory.html')
			json_data = json.dumps(fields)
			next_section = grabProperNextSection(am, '/am_angerHistory/')
			image = amSidebarImages(am, 'ah1')
			classes = grabAmClassesCSS(am, 'ah1')

			content['next_section'] = next_section
			content['json_data'] = json_data
			content['fields'] = fields
			content['AM'] = am
			content['session'] = session
			content['back'] = back
			content['class'] = classes
			content['image'] = image
			content['title'] = "Anger Management Assessment | Simeon Academy"
			return render_to_response('counselor/forms/AngerManagement/angerHistory.html', content)


@login_required(login_url='/index')
def am_angerHistory2(request):
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			next_section = request.POST.get('next_section', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/angerHistory2.html')
			json_data = json.dumps(fields)
			next_section = grabProperNextSection(am, '/am_angerHistory2/')
			image = amSidebarImages(am, 'ah2')
			classes = grabAmClassesCSS(am, 'ah2')

			content['next_section'] = next_section
			content['fields'] = fields
			content['json_data'] = json_data
			content['AM'] = am
			content['session'] = session
			content['title'] = "Anger Management Assessment | Simeon Academy"
			content['back'] = back
			content['class'] = classes
			content['image'] = image
			return render_to_response('counselor/forms/AngerManagement/angerHistory2.html', content)

@login_required(login_url='/index')
def am_angerHistory3(request):
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/angerHistory3.html')
			json_data = json.dumps(fields)			
			image = amSidebarImages(am, 'ah3')
			classes = grabAmClassesCSS(am, 'ah3')
			next_section = grabProperNextSection(am, '/am_angerHistory3/')

			content['next_section'] = next_section
			content['session'] = session
			content['AM'] = am
			content['fields'] = fields
			content['json_data'] = json_data
			content['back'] = back
			content['class'] = classes
			content['image'] = image
			content['title'] = "Anger Management Assessment | Simeon Academy"
			return render_to_response('counselor/forms/AngerManagement/angerHistory3.html', content)

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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/AngerTarget.html')
			json_data = json.dumps(fields)
			image = amSidebarImages(am, 'target')
			classes = grabAmClassesCSS(am, 'target')
			next_section = grabProperNextSection(am, '/am_angerTarget/')

			print "Next section: " + str(next_section)

			content['next_section'] = next_section
			content['class'] = classes
			content['image'] = image
			content['fields'] = fields
			content['json_data'] = json_data
			content['AM'] = am
			content['client'] = am.client
			content['session'] = session
			content['back'] = back
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
			back = request.POST.get('back_btn', '')
			am_id = request.POST.get('am_id', '')
			session_id = request.POST.get('session_id', '')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			session = ClientSession.objects.get(id=session_id)
			am = AngerManagement.objects.get(id=am_id)

			if back == 'false':	
				saveCompletedAmSection(request, save_section, am)	

			image = amSidebarImages(am, 'child')
			classes = grabAmClassesCSS(am, 'child')
			fields = getAMFields(am, 'counselor/forms/AngerManagement/childhoodHistory.html')
			json_data = json.dumps(fields)
			next_section = grabProperNextSection(am, '/am_childhood/')

			content['next_section'] = next_section
			content['fields'] = fields
			content['json_data'] = json_data
			content['back'] = back
			content['AM'] = am
			content['session'] = session
			content['image'] = image
			content['class'] = classes
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)
			fields = getAMFields(am, 'counselor/forms/AngerManagement/connections.html')
			json_data = json.dumps(fields)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			image = amSidebarImages(am, 'connect')
			classes = grabAmClassesCSS(am, 'connect')
			next_section = grabProperNextSection(am, '/am_connections/')

			print "Next section: " + str(next_section)

			content['next_section'] = next_section
			content['AM'] = am
			content['session'] = session
			content['back'] = back
			content['fields'] = fields
			content['json_data'] = json_data
			content['class'] = classes
			content['image'] = image
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			next_section = request.POST.get('next_section', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/control.html')
			json_data = json.dumps(fields)
			image = amSidebarImages(am, 'control')
			classes = grabAmClassesCSS(am, 'control')
			next_section = grabProperNextSection(am, '/am_control/')

			content['next_section'] = next_section
			content['class'] = classes
			content['image'] = image
			content['json_data'] = json_data
			content['fields'] = fields
			content['AM'] = am
			content['session'] = session
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
			session_id = request.POST.get('session_id', '')
			session = ClientSession.objects.get(id=session_id)
			client = session.client
			content['client'] = session.client
			phone = convert_phone(client.phone)
			content['phone'] = phone
			content['client'] = client
			content['session'] = session
			content['AM'] = am

			if str(action) == 'finish-old':
				##go to the next section to be completed in the form
				back = 'false'
				content['back'] = back
				goToLocation = continueToAmSection(am)

				if goToLocation == 'counselor/forms/AngerManagement/demographic.html':
					marital = MaritalStatus.objects.all().order_by('status')
					living = LivingSituation.objects.all().order_by('situation')
					education = EducationLevel.objects.all().order_by('level')
					content['education'] = education
					content['marital'] = marital
					content['living'] = living

				m_page = grabAmSideBarString(goToLocation)
				image = amSidebarImages(am, m_page)
				classes = grabAmClassesCSS(am, m_page)
				fields = getAMFields(am, goToLocation)
				json_data = json.dumps(fields)	

				content['class'] = classes
				content['image'] = image
				content['json_data'] = json_data
				content['fields'] = fields
				content['title'] = "Counselor Home Page | Simeon Academy"
				return render_to_response(goToLocation, content)
			elif str(action) == 'start-new':
				##delete the current form and start at beginning of the am form
				new_am = refreshAM(am)
				back = 'false'
				content['back'] = back

				fields = getAMDemoFields('false', am)
				json_data = json.dumps(fields)

				marital = MaritalStatus.objects.all().order_by('status')
				living = LivingSituation.objects.all().order_by('situation')
				education = EducationLevel.objects.all().order_by('level')
				content['AM'] = new_am
				content['json_data'] = json_data
				content['fields'] = fields
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)
			fields = getAMFields(am, 'counselor/forms/AngerManagement/currentProblems.html')
			json_data = json.dumps(fields)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)
			
			image = amSidebarImages(am, 'current')
			classes = grabAmClassesCSS(am, 'current')
			next_section = grabProperNextSection(am, '/am_problems/')

			content['next_section'] = next_section
			content['save_section'] = save_section
			content['goToNext'] = goToNext
			content['class'] = classes
			content['image'] = image
			content['json_data'] = json_data
			content['fields'] = fields
			content['AM'] = am
			content['session'] = session
			content['title'] = "Anger Management Assessment | Simeon Academy"
			return render_to_response('counselor/forms/AngerManagement/currentProblems.html', content)

@login_required(login_url='/index')
def am_demographic(request):
	#IF USER IS NOT AUTHENTICATED RETURN TO LOGIN PAGE
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		#USER HAS BEEN AUTHENTICATED
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			#RESTRICTED ACCESS FOR NON COUNSELOR USERS
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			#AUTHENTICATED AS A COUNSELOR
			client_id = request.POST.get('client_id', '')
			session_id = request.POST.get('session_id', '')
			back = request.POST.get('back_btn', '')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			client = Client.objects.get(id=client_id)			
			session = ClientSession.objects.get(id=session_id)

			if back == '' or back == None:
				back = 'false'			

			proceed = startAM(client)		
			am = proceed['am']

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			content['am'] = am
			content['back'] = back
			content['session'] = session
			content['client'] = client
			content['title'] = "Anger Management Assessment | Simeon Academy"

			print "isNew: " + str(proceed['isNew'])
			print "back: " + str(back)
			print "goToNext: " + str(goToNext)

			if proceed['isNew'] == False and proceed['back'] == 'true' and str(goToNext) == 'false':
				#CLIENT CURRENTLY HAS EXISTING INCOMPLETE AM FILE USER MUST CHOOSE WHAT TO DO WITH PRE-EXISTING											
				return render_to_response('counselor/forms/AngerManagement/getClient.html', content)

			else:
				marital = MaritalStatus.objects.all().order_by('status')
				living = LivingSituation.objects.all().order_by('situation')
				education = EducationLevel.objects.all().order_by('level')

				#JSON OBJECTS WILL DYNAMICALLY FILL IN THE HTML FORM FIELDS IN REAL TIME FROM THE SERVER
				# fields = None
				# json_data = None
				fields = getAMDemoFields(am)
				json_data = json.dumps(fields)
				image = amSidebarImages(am, 'demo')
				classes = grabAmClassesCSS(am, 'demo')
				next_section = grabProperNextSection(am, '/am_demographic/')

				#CONTEXT
				content['next_section'] = next_section
				content['class'] = classes
				content['image'] = image
				content['education'] = education
				content['marital'] = marital
				content['living'] = living
				content['AM'] = am
				content['json_data'] = json_data
				content['fields'] = fields
				content['back'] = back

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
			back = request.POST.get('back_btn', '')
			am_id = request.POST.get('am_id', '')			
			session_id = request.POST.get('session_id', '')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			session = ClientSession.objects.get(id=session_id)
			am = AngerManagement.objects.get(id=am_id)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)
				
			fields = getAMFields(am, 'counselor/forms/AngerManagement/drugHistory.html')
			json_data = json.dumps(fields)
			image = amSidebarImages(am, 'dh')
			classes = grabAmClassesCSS(am, 'dh')
			next_section = grabProperNextSection(am, '/am_drugHistory/')

			content['next_section'] = next_section
			content['back'] = back
			content['AM'] = am
			content['session'] = session
			content['fields'] = fields
			content['json_data'] = json_data
			content['class'] = classes
			content['image'] = image
			content['title'] = "Anger Management Assessment | Simeon Academy"

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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)		

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/familyOrigin.html')
			json_data = json.dumps(fields)
			image = amSidebarImages(am, 'family')
			classes = grabAmClassesCSS(am, 'family')
			next_section = grabProperNextSection(am, '/am_familyOrigin/')

			content['json_data'] = json_data
			content['fields'] = fields
			content['AM'] = am
			content['session'] = session
			content['back'] = back
			content['next_section'] = next_section
			content['class'] = classes
			content['image'] = image
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/final.html')
			json_data = json.dumps(fields)
			image = amSidebarImages(am, 'final')
			classes = grabAmClassesCSS(am, 'final')
			next_section = grabProperNextSection(am, '/am_final/')

			content['next_section'] = next_section
			content['back'] 		= back
			content['class'] 		= classes
			content['image'] 		= image
			content['fields'] 		= fields
			content['json_data'] 	= json_data
			content['AM'] 			= am
			content['session'] 		= session
			content['title'] 		= "Anger Management Assessment | Simeon Academy"
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if am.demographic.own == False:
				content['own'] = 'Rent'
			else:
				content['own'] = 'Own'

			if str(am.demographic.employer_phone) == 'NA':
				content['employer_phone'] = 'NA'
			else:
				content['employer_phone'] = convert_phone(am.demographic.employer_phone)

			if str(am.demographic.health_problem) == 'True':
				content['health'] = 'Yes'
			else:
				content['health'] = 'No'

			if str(am.demographic.medication) == 'True':
				content['medical'] = 'Yes'
			else:
				content['medical'] = 'No'

			if am.drugHistory.curUse == True:
				content['curUse'] = 'Yes'
			else:
				content['curUse'] = 'No'

			if am.drugHistory.everDrank == True:
				content['everDrank'] = 'Yes'
			else:
				content['everDrank'] = 'No'

			if am.drugHistory.DUI == True:
				content['DUI'] = 'Yes'
			else:
				content['DUI'] = 'No'

			if am.drugHistory.drugTreatment == True:
				content['drugTreatment'] = 'Yes'
			else:
				content['drugTreatment'] = 'No'

			if am.drugHistory.finishedTreatment == True:
				content['finishedTreatment'] = 'Yes'
			else:
				content['finishedTreatment'] = 'No'

			if am.drugHistory.isClean == True:
				content['isClean'] = 'Yes'
			else:
				content['isClean'] = 'No'

			if am.drugHistory.drinkLastEpisode == True:
				content['drinkLastEpisode'] = 'Yes'
			else:
				content['drinkLastEpisode'] = 'No'

			if am.drugHistory.needHelpDrugs == True:
				content['needHelpDrugs'] = 'Yes'
			else:
				content['needHelpDrugs'] = 'No'

			if am.drugHistory.drinkRelationshipProblem == True:
				content['drinkRelationshipProblem'] = 'Yes'
			else:
				content['drinkRelationshipProblem'] = 'No'


			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			image = amSidebarImages(am, 'viewForm')
			classes = grabAmClassesCSS(am, 'viewForm')

			content['class'] 		= classes
			content['image'] 		= image
			content['AM'] = am			
			content['session'] = session			
			content['title'] = "Anger Management Assessment | Simeon Academy"
			return render_to_response('counselor/forms/AngerManagement/viewForm.html', content)

@login_required(login_url='/index')
def printAM(request):
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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			date_of_form = am.start_time
			date_of_form = date_of_form.date()

			unchecked = "/static/images/unchecked_checkbox.png"
			checked = "/static/images/checked_checkbox.png"

			images = {}
			spouse = None

			if am.demographic.maritalStatus.status == 'Married':
				spouse = '1'
			else:
				spouse = '0'

			#PROCESS MARITAL STATUS CHECKBOXES
			if am.demographic.maritalStatus.status == 'Divorced':
				images['divorced'] 	= checked
				images['single'] 	= unchecked
				images['separated'] = unchecked
				images['married'] 	= unchecked
			elif am.demographic.maritalStatus.status == 'Single':
				images['divorced'] 	= unchecked
				images['single'] 	= checked
				images['separated'] = unchecked
				images['married'] 	= unchecked
			elif am.demographic.maritalStatus.status == 'Married':
				images['divorced'] 	= unchecked
				images['single'] 	= unchecked
				images['separated'] = unchecked
				images['married'] 	= checked
			elif am.demographic.maritalStatus.status == 'Separated':
				images['divorced'] 	= unchecked
				images['single'] 	= unchecked
				images['separated'] = checked
				images['married'] 	= unchecked

			#PROCESS LIVING SITUATION CHECKBOXES
			if am.demographic.livingSituation.situation == 'Live with friend':
				images['friend'] 	= checked
				images['family'] 	= unchecked
				images['alone'] 	= unchecked
				images['partner'] 	= unchecked
			elif am.demographic.livingSituation.situation == 'Live with family':
				images['friend'] 	= unchecked
				images['family'] 	= checked
				images['alone'] 	= unchecked
				images['partner'] 	= unchecked
			elif am.demographic.livingSituation.situation == 'Live alone':
				images['friend'] 	= unchecked
				images['family'] 	= unchecked
				images['alone'] 	= checked
				images['partner'] 	= unchecked
			elif am.demographic.livingSituation.situation == 'Live with partner':
				images['friend'] 	= unchecked
				images['family'] 	= unchecked
				images['alone'] 	= unchecked
				images['partner'] 	= checked

			#PROCESS HEALTH CHECKBOX IMAGES
			if am.demographic.health_problem == True:
				images['goodHealth'] = checked
				images['badHealth'] = unchecked
			else:
				images['goodHealth'] = unchecked
				images['badHealth'] = checked

			if am.demographic.medication == True:
				images['onMeds'] = checked
				images['noMeds'] = unchecked
			else:
				images['onMeds'] = unchecked
				images['noMeds'] = checked

			#PROCESS EMPLOYER PHONE NUMBER
			emp_phone = convert_phone(am.demographic.employer_phone)

			#PROCESS RENT/OWN CHECKBOXES
			if am.demographic.own == True:
				images['own'] = checked
				images['rent'] = unchecked
				
			else:
				images['own'] = unchecked
				images['rent'] = checked				

			content['emp_phone'] = emp_phone
			content['spouse'] = spouse
			content['images'] = images
			content['phone'] = convert_phone(am.client.phone)
			content['date_of_form'] = date_of_form

			content['AM'] = am
			content['client'] = am.client
			content['session'] = session
			content['phone'] = convert_phone(am.client.phone)
			content['title'] = "Anger Management Assessment | Simeon Academy"
			return render_to_response('counselor/forms/AngerManagement/printAM.html', content)

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
			am = request.POST.get('am_id')
			session = request.POST.get('session_id')
			back = request.POST.get('back_btn')
			save_section = request.POST.get('save_section', '')
			goToNext = request.POST.get('goToNext', '')

			am = AngerManagement.objects.get(id=am)
			session = ClientSession.objects.get(id=session)

			if back == 'false':
				saveCompletedAmSection(request, save_section, am)

			fields = getAMFields(am, 'counselor/forms/AngerManagement/worstEpisodes.html')
			json_data = json.dumps(fields)
			image = amSidebarImages(am, 'worst')
			classes = grabAmClassesCSS(am, 'worst')
			next_section = grabProperNextSection(am, '/am_worst/')

			content['next_section'] = next_section
			content['class'] = classes
			content['image'] = image
			content['json_data'] = json_data
			content['fields'] = fields
			content['AM'] = am
			content['client'] = am.client
			content['session'] = session
			content['back'] = back
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
			content['title'] = "Simeon Academy | Substance Abuse Professional Form"

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
			content['title'] = "Simeon Academy | SAP"
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
def sap_social(request):
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
def sap_other(request):
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
def sap_sources(request):
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
			return render_to_response('counselor/forms/SAP/sap_sources.html', content)

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



































