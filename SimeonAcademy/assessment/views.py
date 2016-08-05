from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
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

from assessment.models import State, RefReason, Client, \
AngerManagement, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, MHUseTable, \
MHFamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_AngerHistory2, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHBackground, MHEducation, \
MHStressor, MHLegalHistory, ClientSession, SType, Invoice, AM_AngerHistory3, \
AIS_Admin, AIS_General, AIS_Medical, AIS_Employment, AIS_Drug1, \
AIS_Legal, AIS_Family, AIS_Social1, AIS_Social2, AIS_Psych, ASI, UtPaid, \
SolidState, TrackApp

from assessment.view_functions import convert_datepicker, generateClientID, \
getStateID, getReasonRefID, clientExist, getClientByName, getClientByDOB, \
getClientByID, getClientBySS, getEducationID, getLivingID, getMaritalID, \
getActiveClients, getDischargedClients, getTimes, convert_phone, phone_to_integer, \
grabClientOpenForm, fetchForm, deleteForm, getOrderedStateIndex, \
getGlobalID, force_URL_priority, startForm, fetchUrl, grabMhViewImages, \
fetchContent, saveForm, deleteForm, refreshForm, saveAndFinish, beginSession, \
processClientHistory, getDischarge, getSessionID, endSession, deleteCurrentSession, \
truePythonBool, shouldDeleteSession, getExistingSessionForms, refreshCurrentSession, \
setAppTrack, getAppTrack, getTrack, quickTrack, setGlobalSession, fetchCurrentFile, \
fetchPrintFields, processInvoice, fetchBillableItems, fetchAllClientHistory, fetchUtPositive, \
getUtViewImages, getUtPaid, deprioritizeURL, setClientHistory5, fetchClientSSDisplay, \
fetchClientPhoneDisplay, calculateHistoryPages, fetchASIViewItems, completeClientSearch, \
fetchResultTags, fetchClientSSDisplay, fetchClientPhoneDisplay, fetchGenderDisplay, \
fetchStatusDisplay


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
        	track = getTrack(user)
        	quickTrack('General', track)
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
		return render_to_response('global/printAM.html', content)

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
## HOME PAGE VIEWS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@login_required(login_url='/index')
def searchClientMain(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/searchClient.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def searchFormMain(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/searchForm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def appointmentMain(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/appointments.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def billingMain(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/billing.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def AdministrativeMain(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/admin.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def emailMain(request):
	user = request.user

	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content['user'] = user
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/email.html', content, context_instance=RequestContext(request))

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
		track = getTrack(user)
		quickTrack('General', track)
		content['tracking'] = track.state.state

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			searchExistingSessions = request.POST.get('search_clientSession')
			client = None

			if searchExistingSessions == 'True':
				client = Client.objects.get(id=(request.POST.get(client_id)))
				content['client'] = client


			content['title'] = "Simeon Academy"
			return render_to_response('counselor/home.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def newClient(request):
	user = request.user
	
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		quickTrack('Admin', track)
		content['tracking'] = track.state.state
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
		track = getTrack(user)
		content['tracking'] = track.state.state
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
def uniFormSearch(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		quickTrack('Search', track)
		content['tracking'] = track.state.state
		content['user'] = user
		track = getTrack(user)
		quickTrack('Search', track)

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html')

		else:
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/main/searchForm.html', content)

@login_required(login_url='/index')
def clientCreated(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		content['tracking'] = track.state.state
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
		track = getTrack(user)
		quickTrack('Search', track)
		content['tracking'] = track.state.state
		content['user'] = user
		track = getTrack(user)
		quickTrack('Search', track)

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html')

		else:
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/search_clients.html', content)


@login_required(login_url='/index')
def updateStatus(request):
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
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/client/updateStatus.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def updateSuccess(request):
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
			client = Client.objects.get(id=(request.POST.get('client_id')))
			newStatus = request.POST.get('newStatus')
			client.isPending = False

			if newStatus == 'ACTIVE':
				client.isDischarged = False
			elif newStatus == 'DISCHARGED':
				client.isDischarged = True
			client.save()

			content['newStatus'] = newStatus
			content['client'] = client
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/client/updateSuccess.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def uniClientSearch(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		quickTrack('Search', track)
		content['tracking'] = track.state.state
		content['user'] = user
		track = getTrack(user)
		quickTrack('Search', track)

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html')

		else:
			date = datetime.now()
			temp = []
			years = []
			year = date.year
			year = int(year)
			firstYear = year - 80
			lastYear = year - 5

			for y in range(firstYear, lastYear):
				temp.append(y)

			count = len(temp) - 1
			for i in range(count):
				years.append(temp[count])
				count -= 1

			content['years'] = years
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/searchClient.html', content)

@login_required(login_url='/index')
def clientSearchResults(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		content['tracking'] = track.state.state
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			sortBy = request.POST.get('sortBy')
			page = request.POST.get('page')
			matches = completeClientSearch(request, sortBy)
			slots = fetchResultTags(matches['numMatches'], 4)
			json_data = json.dumps(matches)

			if matches['numMatches'] < 4:
				content['pageOne'] = matches['numMatches'] % 4
			else:
				content['pageOne'] = 4

			if matches['numMatches'] == 1:
				content['matchWord'] = 'Result'
			else:
				content['matchWord'] = 'Results'

			content['json_data'] 	= json_data
			content['slots']		= slots
			content['image'] 		= request.POST.get('image')
			content['sType'] 		= request.POST.get('cSearch')
			content['header'] 		= request.POST.get('header')
			content['matches'] 		= matches
			content['numMatches'] 	= matches['numMatches']
			content['numPages'] 	= matches['numPages']
			return render_to_response('counselor/client/clientSearchResults.html', content)

@login_required(login_url='/index')
def editClientInfo(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		quickTrack('Admin', user)
		content['tracking'] = track.state.state
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			return render_to_response('counselor/client/editClientInfo.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def clientHistory(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		quickTrack('Admin', user)
		content['tracking'] = track.state.state
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content = processClientHistory(request)
			return render_to_response('counselor/client/clientHistory.html', content, context_instance=RequestContext(request))

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
			page = 1
			content = beginSession(request)
			session = ClientSession.objects.get(id=(getSessionID(user)))
			initLoad = request.POST.get('initLoad')

			if initLoad == 'false':
				page = request.POST.get('histPage')

			if session.client.isMale == True:
				content['gender'] = 'Male'
			else:
				content['gender'] = 'Female'

			allHistory = fetchAllClientHistory(session)
			history = setClientHistory5(page, allHistory, user)

			matches = len(allHistory)
			pages = calculateHistoryPages(matches)

			content['phone'] = fetchClientPhoneDisplay(session.client.phone)
			content['ssn'] =fetchClientSSDisplay(session.client.ss_num)
			content['history'] = history
			content['pages'] = pages
			content['numPages'] = len(pages)
			return render_to_response('counselor/client/client_options.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def clientProfile(request):
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
			updateClass = None
			client = Client.objects.get(id=(request.POST.get('client_id')))
			session_id = request.POST.get('session_id')
			hasExisting = request.POST.get('hasExisting')

			status = fetchStatusDisplay(client.isDischarged)
			activeClass = 'clientIsActive'
			activeButton = 'Discharge Client'

			if status == 'DISCHARGED':
				activeClass = 'clientNotActive'
				activeButton = 'Reinstate Client'

			if client.isPending == True:
				status = 'PENDING'
				activeClass = 'clientIsPending'

			if status == 'PENDING' or status == 'DISCHARGED':
				updateClass = 'clientIsActive'
			else:
				updateClass = 'clientNotActive'

			content['updateClass']	= updateClass
			content['session_id']	= session_id
			content['hasExisting']	= hasExisting
			content['client'] 		= client
			content['activeClass'] 	= activeClass
			content['activeButton'] = activeButton
			content['Emphone'] 		= fetchClientPhoneDisplay(client.emer_phone)
			content['workPhone'] 	= fetchClientPhoneDisplay(client.work_phone)
			content['probationPhone'] = fetchClientPhoneDisplay(client.probation_phone)
			content['phone'] 		= fetchClientPhoneDisplay(client.phone)
			content['f_ssn'] 		= fetchClientSSDisplay(client.ss_num)
			content['gender'] 		= fetchGenderDisplay(client.isMale)
			content['status'] 		= status
			content['title'] 		= 'Simeon Academy'
			return render_to_response('counselor/client/clientProfile.html', content, context_instance=RequestContext(request))

##################################################################################################################################
##################################################################################################################################
##################################################### END CLIENT VIEWS ###########################################################
##################################################################################################################################
##################################################################################################################################

@login_required(login_url='/index')
def hasExistingSession(request):
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
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/existingSession.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def existingResolve(request):
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
			s_head = request.POST.get('s_option')
			session = ClientSession.objects.get(id=(request.POST.get('session_id')))
			setGlobalSession(session.id, user)
			content['s_head'] = s_head
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/existingResolve.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def sessionResolveSuccess(request):
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
			exit_type = request.POST.get('exit_type')
			exit_type = str(exit_type)
			s_head = ''
			session = ClientSession.objects.get(id=(getSessionID(user)))


			if exit_type == 'refresh':
				refreshCurrentSession(session)
				s_head = 'reset'
				url = '/clientOptions/'
			elif exit_type == 'delete':
				deleteCurrentSession(session)
				s_head = 'deleted'
				url ='/adminHome/'

			content['s_head'] = s_head
			content['url'] = url
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/successResolve.html', content, context_instance=RequestContext(request))




###########################################################################################################################################
###########################################################################################################################################
#------------------------------------------------------------ GENERIC VIEWS --------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################

@login_required(login_url='/index')
def uni_generic_exit(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		track = getTrack(user)
		content['tracking'] = track.state.state
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			last_section = request.POST.get('save_section', '')
			form_type = request.POST.get('exit_type')
			session_id = request.POST.get('session_id', '')

			form = None
			type_header = None

			session = ClientSession.objects.get(id=session_id)

			if str(form_type) == 'am':
				am_id = request.POST.get('am_id', '')
				form = AngerManagement.objects.get(id=am_id)
				type_header = 'Anger Management'

			elif str(form_type) == 'sap':
				sap_id = request.POST.get('sap_id', '')
				form = SAP.objects.get(id=sap_id)
				type_header = "S.A.P"

			elif str(form_type) == 'mh':
				mh_id = request.POST.get('mh_id', '')
				form = MentalHealth.objects.get(id=mh_id)
				type_header = 'Mental Health'

			elif str(form_type) == 'asi':
				asi_id = request.POST.get('asi_id', '')
				form = ASI.objects.get(id=asi_id)
				type_header = 'A.S.I'

			elif str(form_type) == 'ut':
				ut_id = request.POST.get('ut_id', '')
				form = UrineResults.objects.get(id=ut_id)
				type_header = 'Urine Test'

			saveForm(request, form_type, last_section, form)
			force_URL_priority(form_type, last_section, form)

			content['form'] = form
			content['type_header'] = type_header
			content['session'] = session
			content['form_type'] = form_type
			content['last_section'] = last_section
			content['title'] = "Simeon Academy | " + str(type_header)
			return render_to_response('global/exit.html', content)

@login_required(login_url='/index')
def generic_exit(request):
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
			last_section = request.POST.get('save_section', '')
			form_type = request.POST.get('exit_type')
			session_id = request.POST.get('session_id', '')

			form = None
			type_header = None

			session = ClientSession.objects.get(id=session_id)

			if str(form_type) == 'am':
				am_id = request.POST.get('am_id', '')
				form = AngerManagement.objects.get(id=am_id)
				type_header = 'Anger Management'

			elif str(form_type) == 'sap':
				sap_id = request.POST.get('sap_id', '')
				form = SAP.objects.get(id=sap_id)
				type_header = "S.A.P"

			elif str(form_type) == 'mh':
				mh_id = request.POST.get('mh_id', '')
				form = MentalHealth.objects.get(id=mh_id)
				type_header = 'Mental Health'

			elif str(form_type) == 'asi':
				asi_id = request.POST.get('asi_id', '')
				form = ASI.objects.get(id=asi_id)
				type_header = 'A.S.I'

			elif str(form_type) == 'ut':
				ut_id = request.POST.get(id=ut_id)
				form = UrineResults.objects.get(id=ut_id)
				type_header = 'Urine Test'

			saveForm(request, form_type, last_section, form)
			force_URL_priority(form_type, last_section, form)			

			content['form'] = form
			content['type_header'] = type_header
			content['session'] = session
			content['form_type'] = form_type
			content['last_section'] = last_section
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('global/exit.html', content)

@login_required(login_url='/index')
def genericDelete(request):
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
			content['title'] = "Simeon Academy"
			return render_to_response('global/genericDelete.html', content)

@login_required(login_url='/index')
def genericRefreshForm(request):
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
			content['title'] = "Simeon Academy"
			return render_to_response('global/genericRefreshForm.html', content)

@login_required(login_url='/index')
def genericFormRefreshed(request):
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
			form_id = request.POST.get('child_form_id', '')
			form_type = request.POST.get('child_form_type', '')
			session_id = request.POST.get('child_session_id', '')

			session = ClientSession.objects.get(id=session_id)

			type_header = None
			form = None

			if str(form_type) == 'am':
				type_header = 'Anger Management'
				form = AngerManagement.objects.get(id=form_id)
			elif str(form_type) == 'sap':
				type_header = 'S.A.P'
				form = SAP.objects.get(id=form_id)
			elif str(form_type) == 'mh':
				type_header = 'Mental Health'
				form = MentalHealth.objects.get(id=form_id)
			elif str(form_type) == 'ut':
				type_header = 'Urine Test'
				form = UrineResults.objects.get(id=form_id)
			elif str(form_type) == 'asi':
				type_header = 'Addiction Severity'
				form = ASI.objects.get(id=form_id)
			elif str(form_type) == 'discharge':
				type_header = 'Discharge Client'
				form = Discharge.objects.get(id=form_id)

			refreshForm(form_type, form)
			location = fetchUrl(form_type, None ,form)

			content['save_section'] = location
			content['form_type'] = form_type
			content['form'] = form
			content['type_header'] = type_header
			content['session'] = session
			content['title'] = "Simeon Academy"
			return render_to_response('global/genericFormRefreshed.html', content)

@login_required(login_url='/index')
def genericFormDeleted(request):
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
			form_type = request.POST.get('parent_form_type', '')
			form_id = request.POST.get('parent_form_id', '')

			form = fetchForm(form_type, form_id)
			deleteForm(form_type, form)

			content['form_type'] = form_type
			content['form_id'] = form_id
			content['title'] = "Simeon Academy"
			return render_to_response('global/genericFormDeleted.html', content)

@login_required(login_url='/index')
def closeSession(request):
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
			track = getTrack(user)
			session = ClientSession.objects.get(id=(track.s_id))
			shouldDelete = shouldDeleteSession(session)
			content['shouldDelete'] = shouldDelete
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/closeSession.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def deleteSession(request):
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
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/deleteSession.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def refreshSession(request):
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
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/refreshSession.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def uni_exit_session(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			exit_type = request.POST.get('exit_type')
			multiNav = request.POST.get('multiNav')
			exit_type = str(exit_type)

			if exit_type == 'close':				
				if shouldDeleteSession(session) == False:
					content['title'] = 'Simeon Academy'
					content['multiNav'] = multiNav
					return render_to_response('counselor/session/closeType.html', content, context_instance=RequestContext(request))
				else:
					deleteCurrentSession(session)
					content['multiNav'] = multiNav
					content['exit_type'] = 'closed.'

			elif exit_type == 'delete':
				deleteCurrentSession(session)
				content['exit_type'] = 'deleted.'
				content['multiNav'] = multiNav

			elif exit_type == 'refresh':
				refreshSession(session)
				content['exit_type'] = 'reset.'
				content['multiNav'] = multiNav

			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/uniExitSession.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def invoice(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			if session.hasInvoice == True:
				content['items'] = fetchBillableItems(session)
			return render_to_response('counselor/session/invoice.html', content, context_instance=RequestContext(request))



@login_required(login_url='/index')
def sessionClosed(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))

			if session.hasInvoice == True:
				fetchBillableItems(session)
				return render_to_response('counselor/session/invoice.html', content, context_instance=RequestContext(request))
			else:
				deleteCurrentSession(session)
				multiNav = request.POST.get('multiNav')
				content['multiNav'] = multiNav
				content['title'] = 'Simeon Academy'
				return render_to_response('counselor/session/sessionClosed.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def sessionClosedAlt(request):
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
			eType = request.POST.get('exit_type')
			session = ClientSession.objects.get(id=(getSessionID(user)))
			session.isOpen = False;
			session.save()
			multiNav = request.POST.get('multiNav')
			content['multiNav'] = multiNav
			content['exit_type'] = eType
			content['title'] = 'Simeon Academy'
			return render_to_response('counselor/session/uniExitSession.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def session_open_error(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			shouldDelete = shouldDeleteSession(session)
			content['title'] = 'Simeon Academy'
			content['shouldDelete'] = shouldDelete
			return render_to_response('counselor/session/sessionOpenError.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def form_complete(request):
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
			return render_to_response('counselor/session/form_complete.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def form_saved(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			form_type = request.POST.get('exit_type')

			if form_type == 'mh':
				form = session.mh
			elif form_type == 'am':
				form = session.am
			elif form_type == 'sap':
				form = session.sap
			elif form_type == 'asi':
				form = session.asi

			deprioritizeURL(form_type, form)
			form.isOpen = False
			form.isComplete = True
			form.save()

			content['session'] = session
			content['title'] = 'Simeon Academy | S.A.P'
			return render_to_response('counselor/session/form_saved.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def form_existing(request):
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
			return render_to_response('counselor/session/form_existing.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def printLoaded(request):
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
			return render_to_response('counselor/session/printLoaded.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def printForm(request):
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
			session_id = request.POST.get('session_id')
			form_type = request.POST.get('form_type')
			session = ClientSession.objects.get(id=session_id)
			url = None

			if form_type == 'am':
				url = 'counselor/forms/AngerManagement/printAM.html'
			elif form_type == 'mh':
				content['date'] = session.mh.date_of_assessment
				content['images'] = grabMhViewImages(session.mh)
				url = 'counselor/forms/MentalHealth/printMH.html'
			elif form_type == 'ut':
				date = datetime.now()
				content['date'] = date.date()
				content['images'] = getUtViewImages(session.ut)
				url = 'counselor/forms/UrineTest/printUT.html'
			elif form_type == 'sap':
				content = fetchPrintFields('sap' ,session.sap)
				content['date'] = session.sap.date_of_assessment
				url = 'counselor/forms/SAP/print_sap.html'
			elif form_type == 'asi':
				url = 'counselor/forms/ASI/printASI.html'

			content['session'] = session
			return render_to_response(url, content, context_instance=RequestContext(request))



###########################################################################################################################################
################################################################ END GENERIC ##############################################################
###########################################################################################################################################


###########################################################################################################################################
###########################################################################################################################################
#----------------------------------------------------------------- AM VIEWS --------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################
		

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
			content = startForm(request, 'am')

			if content['isNew'] == False:
				return render_to_response('global/resolve_form.html', content, context_instance=RequestContext(request))

			else:
				return render_to_response('counselor/forms/AngerManagement/instructions.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_demographic/')
			return render_to_response('counselor/forms/AngerManagement/demographic.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_drugHistory/')
			return render_to_response('counselor/forms/AngerManagement/drugHistory.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_childhood/')
			return render_to_response('counselor/forms/AngerManagement/childhoodHistory.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_angerHistory/')
			return render_to_response('counselor/forms/AngerManagement/angerHistory.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_angerHistory2/')
			return render_to_response('counselor/forms/AngerManagement/angerHistory2.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_angerHistory3/')
			return render_to_response('counselor/forms/AngerManagement/angerHistory3.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_connections/')
			return render_to_response('counselor/forms/AngerManagement/connections.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_worst/')
			return render_to_response('counselor/forms/AngerManagement/worstEpisodes.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_angerTarget/')
			return render_to_response('counselor/forms/AngerManagement/AngerTarget.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_familyOrigin/')
			return render_to_response('counselor/forms/AngerManagement/familyOrigin.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_problems/')
			return render_to_response('counselor/forms/AngerManagement/currentProblems.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def am_control(request):
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
			content = fetchContent(request, 'am', '/am_control/')
			return render_to_response('counselor/forms/AngerManagement/control.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_final/')
			return render_to_response('counselor/forms/AngerManagement/final.html', content, context_instance=RequestContext(request))

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


###########################################################################################################################################
################################################################## END AM #################################################################
###########################################################################################################################################


###########################################################################################################################################
###########################################################################################################################################
#----------------------------------------------------------------- MH VIEWS --------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################


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
			content = startForm(request, 'mh')

			if content['isNew'] == False:
				return render_to_response('global/resolve_form.html', content, context_instance=RequestContext(request))

			else:
				return render_to_response('counselor/forms/MentalHealth/instructions.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'mh', '/mh_demographic/')
			return render_to_response('counselor/forms/MentalHealth/demographic.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'mh', '/mh_education/')
			return render_to_response('counselor/forms/MentalHealth/education.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def mh_background(request):
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
			content = fetchContent(request, 'mh', '/mh_background/')
			return render_to_response('counselor/forms/MentalHealth/background.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'mh', '/mh_stress/')
			return render_to_response('counselor/forms/MentalHealth/stressors.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'mh', '/mh_familyHistory/')
			return render_to_response('counselor/forms/MentalHealth/familyHistory.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'mh', '/mh_legal/')
			return render_to_response('counselor/forms/MentalHealth/legal.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def mh_psych(request):
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
			content = fetchContent(request, 'mh', '/mh_psych/')
			return render_to_response('counselor/forms/MentalHealth/psych.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'mh', '/mh_useTable/')
			return render_to_response('counselor/forms/MentalHealth/useTable.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'mh', '/mh_viewForm/')
			content['images'] = grabMhViewImages(content['session'].mh)
			return render_to_response('counselor/forms/MentalHealth/viewForm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def mhDemoOpPage(request):
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
			mh_id = getGlobalID(user)
			mh = MentalHealth.objects.get(id=mh_id)
			states = State.objects.all().order_by('state')

			children = (mh.demographics.numChildren)
			sisters = (mh.demographics.numSisters)
			brothers = (mh.demographics.numBrothers)

			content['no_child'] = children
			content['no_sister'] = sisters
			content['no_brother'] = brothers

			the_class = None
			cols = 0

			if children > 0:
				content['childHead'] = 'Children'
				cols = cols + 1

				children_list = []
				for c in range(children):
					f = {}
					age = 'c_age'
					gender = 'c_gender'
					male = 'male'
					female = 'female'
					city = 'c_city'
					state = 'c_state'
					f['ageID'] = age + str(c + 1)
					f['genderName'] = gender + str(c + 1)
					f['maleID'] = male + str(c + 1)
					f['femaleID'] = female + str(c + 1)
					f['cityID'] = city + str(c + 1)
					f['stateID'] = state + str(c + 1)
					children_list.append(f)
				content['children']  = children_list

			if sisters > 0:
				content['sisterHead'] = 'Sisters'
				cols = cols + 1

				sister_list = []
				for s in range(sisters):
					f2 = {}
					age = 's_age'
					city = 's_city'
					state = 's_state'
					f2['age'] = age + str(s + 1)
					f2['city'] = city + str(s + 1)
					f2['state'] = state + str(s + 1)
					sister_list.append(f2)
				content['sisters']  = sister_list

			if brothers > 0:
				content['brotherHead'] = 'Brothers'
				cols = cols + 1

				brother_list = []
				for b in range(brothers):
					f3 = {}
					age = 'b_age'
					city = 'b_city'
					state = 'b_state'
					f3['age'] = age + str(b + 1)
					f3['city'] = city + str(b + 1)
					f3['state'] = state + str(b + 1)
					brother_list.append(f3)
				content['brothers']  = brother_list

			if cols == 1:
				the_class = 'mh_op_table1'
			elif cols == 2:
				the_class = 'mh_op_table2'
			elif cols == 3:
				the_class = 'mh_op_table3'

			content['mh'] = mh		
			content['col_class'] = the_class
			content['states'] = states
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/mhDemoOpPage.html', content)

@login_required(login_url='/index')
def verify_mhOp(request):
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
			mh_id = request.POST.get('mh_id', '')
			numChildren = int(request.POST.get('numChildren', ''))
			numSisters = int(request.POST.get('numSisters', ''))
			numBrothers = int(request.POST.get('numBrothers', ''))

			mh = MentalHealth.objects.get(id=mh_id)

			male = ''
			female = ''
			sister = ''
			brother = ''

			maleList = []
			femaleList = []
			sisterList = []
			brotherList = []

			for c in range(numChildren):
				age = 'c_age' + str(c + 1)
				gender = 'c_gender' + str(c + 1)
				city = 'c_city' + str(c + 1)
				state = 'c_state' + str(c + 1)

				age = request.POST.get(age)
				gender = request.POST.get(gender, '')
				city = request.POST.get(city, '')
				state = request.POST.get(state, '')

				if str(gender) == 'male':
					male2 = ''
					male2 += age
					male2 += '/'
					male2 += city
					male2 += ', '
					male2 += state
					maleList.append(male2)

				else:
					female2 = ''
					female2 += age
					female2 += '/'
					female2 += city
					female2 += ', '
					female2 += state
					femaleList.append(female2)

			for s in range(numSisters):
				age = 's_age' + str(s + 1)
				city = 's_city' + str(s + 1)
				state = 's_state' + str(s + 1)

				age = request.POST.get(age)
				gender = request.POST.get(gender)
				city = request.POST.get(city)
				state = request.POST.get(state)

				sister2 = ''
				sister2 += age
				sister2 += '/'
				sister2 += city
				sister2 += ', '
				sister2 += state
				sisterList.append(sister2)

			for b in range(numBrothers):
				age = 'b_age' + str(b + 1)
				city = 'b_city' + str(b + 1)
				state = 'b_state' + str(b + 1)

				age = request.POST.get(age)
				gender = request.POST.get(gender)
				city = request.POST.get(city)
				state = request.POST.get(state)

				brother2 = ''
				brother2 += age
				brother2 += '/'
				brother2 += city
				brother2 += ', '
				brother2 += state
				brotherList.append(brother2)

			flag = '~'
			for m in maleList:
				male += m
				male += flag

			for f in femaleList:
				female += f
				female += flag

			for s in sisterList:
				sister += s
				sister += flag

			for b in brotherList:
				brother += b
				brother += flag

			demo = mh.demographics
			demo.childrenMale = male
			demo.childrenFemale = female
			demo.bothers = brother
			demo.sisters = sister
			demo.save()

			mh.demographicsComplete = True
			mh.save()

			content['maleList'] = maleList
			content['femaleList'] = femaleList
			content['sisterList'] = sisterList
			content['brotherList'] = brotherList
			content['mh'] = mh
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/verify_mhOp.html', content)

@login_required(login_url='/index')
def printMH(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			# content = fetchPrintFields('mh' ,session.sap)
			content['date'] = session.mh.date_of_assessment
			content['images'] = grabMhViewImages(session.mh)
			content['session'] = session
			return render_to_response('counselor/forms/MentalHealth/printMH.html', content, context_instance=RequestContext(request))



###########################################################################################################################################
################################################################## END MH #################################################################
###########################################################################################################################################


###########################################################################################################################################
#*****************************************************************************************************************************************#
#---------------------------------------------------------------- ASI VIEWS --------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


@login_required(login_url='/index')
def asi_preliminary(request):
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
			content = startForm(request, 'asi')

			if content['isNew'] == False:
				return render_to_response('global/resolve_form.html', content, context_instance=RequestContext(request))

			else:
				return render_to_response('counselor/forms/ASI/instructions.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def asi_admin(request):
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
			content = fetchContent(request, 'asi', '/asi_admin/')
			return render_to_response('counselor/forms/ASI/admin.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_general(request):
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
			content = fetchContent(request, 'asi', '/asi_general/')
			return render_to_response('counselor/forms/ASI/general.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_medical(request):
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
			content = fetchContent(request, 'asi', '/asi_medical/')
			return render_to_response('counselor/forms/ASI/medical.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_employment(request):
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
			content = fetchContent(request, 'asi', '/asi_employment/')
			return render_to_response('counselor/forms/ASI/employment.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_drug1(request):
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
			content = fetchContent(request, 'asi', '/asi_drug1/')
			return render_to_response('counselor/forms/ASI/drug1.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def asi_legal(request):
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
			content = fetchContent(request, 'asi', '/asi_legal/')
			return render_to_response('counselor/forms/ASI/legal.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_family(request):
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
			content = fetchContent(request, 'asi', '/asi_family/')
			return render_to_response('counselor/forms/ASI/family.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_social1(request):
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
			content = fetchContent(request, 'asi', '/asi_social1/')
			return render_to_response('counselor/forms/ASI/social1.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_social2(request):
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
			content = fetchContent(request, 'asi', '/asi_social2/')
			return render_to_response('counselor/forms/ASI/social2.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_psych(request):
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
			content = fetchContent(request, 'asi', '/asi_psych/')
			return render_to_response('counselor/forms/ASI/psych.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def asi_viewForm(request):
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
			time = date.time()
			time = str(time)
			t = ''
			t += time[0]
			t += time[1]
			t += time[2]
			t += time[3]
			t += time[4]

			content = fetchContent(request, 'asi', '/asi_viewForm/')

			content['session'].asi.endTime = t
			content['session'].asi.save()

			content['data'] = fetchASIViewItems(content['session'].asi)
			return render_to_response('counselor/forms/ASI/viewForm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def printASI(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			content['data'] = fetchASIViewItems(session.asi)
			content['session'] = session
			return render_to_response('counselor/forms/ASI/printASI.html', content, context_instance=RequestContext(request))

###########################################################################################################################################
################################################################# END ASI #################################################################
###########################################################################################################################################


###########################################################################################################################################
###########################################################################################################################################
#---------------------------------------------------------------- SAP VIEWS --------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################

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
			content = startForm(request, 'sap')

			if content['isNew'] == False:
				return render_to_response('global/resolve_form.html', content, context_instance=RequestContext(request))

			else:
				return render_to_response('counselor/forms/SAP/instructions.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_demographic/')
			return render_to_response('counselor/forms/SAP/demographic.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_psychoactive/')
			return render_to_response('counselor/forms/SAP/psychoactive.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_psychoactive2/')
			return render_to_response('counselor/forms/SAP/psychoactive2.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_special/')
			return render_to_response('counselor/forms/SAP/special.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_social/')
			return render_to_response('counselor/forms/SAP/pre_final.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_other/')
			return render_to_response('counselor/forms/SAP/final.html', content, context_instance=RequestContext(request))


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
			content = fetchContent(request, 'sap', '/sap_sources/')
			return render_to_response('counselor/forms/SAP/sap_sources.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'sap', '/sap_viewForm/')
			return render_to_response('counselor/forms/SAP/viewForm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def print_sap(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			content = fetchPrintFields('sap' ,session.sap)
			content['date'] = session.sap.date_of_assessment
			content['session'] = session
			return render_to_response('counselor/forms/SAP/print_sap.html', content, context_instance=RequestContext(request))



###########################################################################################################################################
################################################################ END SAP ##################################################################
###########################################################################################################################################


###########################################################################################################################################
###########################################################################################################################################
#------------------------------------------------------------- URINE TEST ----------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################


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
			content = startForm(request, 'ut')
			return render_to_response(content['url'], content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def existingUT(request):
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
			return render_to_response('counselor/forms/UrineTest/existingUT.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def ut_pay(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			paid = getUtPaid(session.client)
			content['p_id'] = paid.id
			return render_to_response('counselor/forms/UrineTest/invoice.html', content)

@login_required(login_url='/index')
def ut_paid(request):
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
			proceed = UtPaid.objects.get(id=(request.POST.get('p_id')))
			proceed.isPaid = True
			proceed.save()
			return render_to_response('counselor/forms/UrineTest/invoice_paid.html', content)
			

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
			content = fetchContent(request, 'ut', None)
			return render_to_response('counselor/forms/UrineTest/results.html', content, context_instance=RequestContext(request))

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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			content = fetchContent(request, 'ut', None)
			content['testResults'] = fetchUtPositive(session)
			return render_to_response('counselor/forms/UrineTest/viewForm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def UT_complete(request):
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
			session = ClientSession.objects.get(id=(getSessionID(user)))
			session.ut.isComplete = True
			session.ut.isOpen = False
			session.ut.save()
			paid = getUtPaid(session.client)
			paid.delete()
			content['session'] = session
			return render_to_response('counselor/forms/UrineTest/utComplete.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def printUT(request):
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
			content['date'] = date.date()
			session = ClientSession.objects.get(id=(getSessionID(user)))
			content['images'] = getUtViewImages(session.ut)
			content['session'] = session
			return render_to_response('counselor/forms/UrineTest/printUT.html', content, context_instance=RequestContext(request))


###########################################################################################################################################
################################################################ END UT ###################################################################
###########################################################################################################################################


###########################################################################################################################################
###########################################################################################################################################
#-------------------------------------------------------------- DISCHARGE ----------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################


@login_required(login_url='/index')
def discharge_success(request):
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
			return render_to_response('counselor/forms/Discharge/verified.html', content, context_instance=RequestContext(request))


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
			content = startForm(request, 'discharge')
			return render_to_response('counselor/forms/Discharge/discharge.html', content, context_instance=RequestContext(request))

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
			session_id = getGlobalID()
			session = ClientSession.objects.get(id=session_id)
			discharge = getDischarge(session.client)
			content['session'] = session
			content['discharge'] = discharge
			content['title'] = 'Simeon Academy | Client Discharge'
			return render_to_response('counselor/forms/Discharge/viewForm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def process_discharge(request):
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
			fetchContent(request, 'discharge', None)
			return render_to_response('counselor/home.html', content, context_instance=RequestContext(request))










































