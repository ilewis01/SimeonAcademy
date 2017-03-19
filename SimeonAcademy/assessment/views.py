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
from django.http import FileResponse, Http404

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
SolidState, TrackApp, WorkSchedule, Note, Roommate, Application, RoommateEvaluation, \
Attachment, Couple, TreatmentResource, Crafft

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
fetchStatusDisplay, setGlobalClientID, getGlobalClientID, getStates, getOrderedStateIndex, \
getRefReasons, getOrderedRefIndex, updateClientAccount, snagYearIndex, decodeDate, \
fetchClientUpdatedFields, fetchCalendarData, decodeCalendarData, newWorkSchedule, \
get_JSON_workSchedule, processAMC, truePythonBool, create_note, isExistingCouple, \
fetchExisitingCouples, superDuperFetchClientID_track, getStates, trueClientInitialize, \
wowClientMatch, processWowSearchData, breakToPages, fixCurrentClients, wowClientMatchFname, \
superCoupleStarter, wowPhoneNumberDisplayConverter, wowSSNumberDisplayConverter, \
wowSSNumberDisplayConverterHidden, getCoupleNotesWowBuilder, fetchExistingClientUpdates, \
changeAndUpdateExistingClient, executeClientUpdate, setNewRefReason, coupleDocumentFetch, \
documentSerializer, noteSerializer, sortResourceColumns, fetchAllResourceIds, \
fetchRawIdNumberResources, saveDischarge, crafft_fetchResults, superCrafftSaver, \
crafft_fetchResponses, getAllClientCraffts, serializeResources


## LOGIN VIEWS---------------------------------------------------------------------------------
def index(request):
	content = {}
	content.update(csrf(request))

	mhr = serializeResources()
	json_data = json.dumps(mhr)

	content['refs'] = RefReason.objects.all().order_by('reason')
	content['json_data'] = json_data
	return render_to_response('global/index.html', content)

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
	content = {}
	content.update(csrf(request))
	mhr = serializeResources()
	json_data = json.dumps(mhr)

	content['json_data'] = json_data
	return render_to_response('global/index.html', content)

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
def errorLegend(request):
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
			content['title'] = "New Client | Simeon Academy"
			return render_to_response('counselor/client/errorLegend.html', content)

@login_required(login_url='/index')
def clientCreatedBaseless(request):
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
			fname 	= request.POST.get('fname')
			lname 	= request.POST.get('lname')
			mm 		= int(request.POST.get('month'))
			dd 		= int(request.POST.get('day'))
			yy 		= int(request.POST.get('year'))
			ss_num 	= request.POST.get('ss_num')
			dob = datetime(yy, mm, dd)
			dob = dob.date()
			new_c 	= trueClientInitialize(fname, lname, dob, ss_num)
			content['title'] = "New Client | Simeon Academy"
			content['client'] = new_c['client']
			
			if new_c['new'] == True:
				new_c['client'].middleInit 			= request.POST.get('mi')
				new_c['client'].street_no 			= request.POST.get('street_no')
				new_c['client'].street_name 		= request.POST.get('street_name')
				new_c['client'].apartment_no 		= request.POST.get('apartment_no')
				new_c['client'].city 				= request.POST.get('city')
				new_c['client'].state 				= State.objects.get(id=(request.POST.get('state')))
				new_c['client'].zip_code 			= request.POST.get('zip_code')
				new_c['client'].phone 				= request.POST.get('phone')
				new_c['client'].emer_phone 			= request.POST.get('emer_phone')
				new_c['client'].work_phone 			= request.POST.get('work_phone')
				new_c['client'].probation_phone 	= request.POST.get('probation_phone')
				new_c['client'].email 				= request.POST.get('email')
				new_c['client'].probationOfficer 	= request.POST.get('probationOfficer')
				new_c['client'].emer_contact_name 	= request.POST.get('emer_contact_name')
				new_c['client'].isMale 				= truePythonBool(request.POST.get('isMale'))
				new_c['client'].reason_ref 			= RefReason.objects.get(id=(request.POST.get('reason_ref')))
				new_c['client'].isPending 			= False

				hasImage = truePythonBool(request.POST.get('hasImage'))

				if hasImage == True:
					photo = request.FILES['photo']
					new_c['client'].photo = photo

				new_c['client'].save()

				if new_c['client'].isMale == True:
					content['gender'] = "Male"
				else:
					content['gender'] = "Female"

				if new_c['client'].work_phone == None or new_c['client'].work_phone == "":
					content['work'] = "N/A"
				else:
					content['work'] = new_c['client'].work_phone

				if new_c['client'].probationOfficer==None or new_c['client'].probationOfficer=="" or new_c['client'].probation_phone==None or new_c['client'].probation_phone=="":
					content['probation'] = "N/A"
				else:
					content['probation'] = str(new_c['client'].probationOfficer) + " " + str(new_c['client'].probation_phone)

				track.c2_id = new_c['client'].id
				track.save()
				content['processed_em_phone'] = wowPhoneNumberDisplayConverter(new_c['client'].emer_phone)

				return render_to_response('counselor/client/clientCreatedBaseless.html', content)				
			else:
				track.c2_id = new_c['client'].id
				track.save()
				content['street_no'] 			= request.POST.get('street_no')
				content['street_name'] 			= request.POST.get('street_name')
				content['apartment_no'] 		= request.POST.get('apartment_no')
				content['city'] 				= request.POST.get('city')				
				content['zip_code'] 			= request.POST.get('zip_code')
				content['phone'] 				= request.POST.get('phone')
				content['emer_phone'] 			= request.POST.get('emer_phone')
				content['work_phone'] 			= request.POST.get('work_phone')
				content['probation_phone'] 		= request.POST.get('probation_phone')
				content['email'] 				= request.POST.get('email')
				content['probationOfficer']		= request.POST.get('probationOfficer')
				content['emer_contact_name'] 	= request.POST.get('emer_contact_name')
				content['state'] 				= State.objects.get(id=(request.POST.get('state')))
				content['reason_ref'] 			= RefReason.objects.get(id=(request.POST.get('reason_ref')))
				content['displayPhone'] 		= wowPhoneNumberDisplayConverter(request.POST.get('phone'))

				return render_to_response('counselor/client/existingResolveNewClient.html', content)

@login_required(login_url='/index')
def updateExistingBaseless(request):
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
			data 						= {}
			data['street_no' ]			= request.POST.get('street_no')
			data['street_name']			= request.POST.get('street_name')
			data['apartment_no'] 		= request.POST.get('apartment_no')
			data['city']				= request.POST.get('city')				
			data['zip_code'] 			= request.POST.get('zip_code')
			data['phone']				= request.POST.get('phone')
			data['emer_phone']			= request.POST.get('emer_phone')
			data['work_phone']			= request.POST.get('work_phone')
			data['probation_phone'] 	= request.POST.get('probation_phone')
			data['email']				= request.POST.get('email')
			data['probationOfficer']	= request.POST.get('probationOfficer')
			data['emer_contact_name'] 	= request.POST.get('emer_contact_name')
			data['state'] 				= State.objects.get(id=(request.POST.get('state')))
			data['reason_ref'] 			= RefReason.objects.get(id=(request.POST.get('reason_ref')))
			client 		 				= Client.objects.get(id=(request.POST.get('client_id')))
			updates 					= fetchExistingClientUpdates(data, client)

			content['street_no'] 			= data['street_no']
			content['street_name'] 			= data['street_name']
			content['apartment_no'] 		= data['apartment_no']
			content['city'] 				= data['city']
			content['zip_code'] 			= data['zip_code']
			content['phone'] 				= data['phone']
			content['emer_phone'] 			= data['emer_phone']
			content['work_phone'] 			= data['work_phone']
			content['probation_phone']	 	= data['probation_phone']
			content['email'] 				= data['email']
			content['probationOfficer'] 	= data['probationOfficer']
			content['emer_contact_name'] 	= data['emer_contact_name']
			content['state'] 				= data['state']
			content['reason_ref'] 			= data['reason_ref']
			content['stateList'] 			= State.objects.all().order_by('state')
			content['updates'] 				= updates
			content['client'] 				= client
			content['title'] 				= "Client Search | Simeon Academy"
			return render_to_response('counselor/client/updateExistingBaseless.html', content)

@login_required(login_url='/index')
def baselessUpdated(request):
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
			client = Client.objects.get(id=(request.POST.get('client_id')))
			executeClientUpdate(request, client)
			setNewRefReason('Couple Counseling', client)
			content['title'] 	= "Client Search | Simeon Academy"
			return render_to_response('counselor/client/baselessUpdated.html', content)

@login_required(login_url='/index')
def newClientAborted(request):
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
			client = Client.objects.get(id=(track.c2_id))
			client.delete()
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/newClientAborted.html', content)

@login_required(login_url='/index')
def wowSearch(request):
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
			yy = date.year
			backwards = []
			years = []

			for i in range((yy - 90), (yy)):
				backwards.append(i)
				years.append('')

			reverse = len(backwards)
			index = reverse - 1

			for j in range(reverse):
				years[j] = backwards[index]
				index -= 1

			ref_list = RefReason.objects.all().order_by('reason')

			content['years'] 	= years
			content['refs'] 	= ref_list
			content['title'] 	= "Client Search | Simeon Academy"
			return render_to_response('counselor/client/wowSearch.html', content)

@login_required(login_url='/index')
def wowSearchResults(request):
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
		phrase1 = None

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html')

		else:
			searches = str(request.POST.get('searches'))
			s_list = []
			data = []
			c = ''

			for s in searches:
				if s != '~':
					c += s
				else:
					s_list.append(c)
					c = ''

			num = len(s_list)

			for m in s_list:
				if m == 'fname':
					d = {}
					d['modelName'] = 'fname'
					d['searchField'] = processWowSearchData(request.POST.get('fname'), False)
					d['type']  = 'text'
					d['isNumber'] = False
					data.append(d)
				elif m == 'lname':
					d = {}
					d['modelName'] = 'lname'
					d['searchField'] = processWowSearchData(request.POST.get('lname'), False)
					d['type']  = 'text'
					d['isNumber'] = False
					data.append(d)
				elif m == 'ssn':
					d = {}
					d['modelName'] = 'ss_num'
					d['searchField'] = processWowSearchData(request.POST.get('ss_num'), True)
					d['type']  = 'text'
					d['isNumber'] = True
					data.append(d)
				elif m == 'phone':
					d = {}
					d['modelName'] = 'phone'
					d['searchField'] = processWowSearchData(request.POST.get('phone'), True)
					d['type']  = 'text'
					d['isNumber'] = True
					data.append(d)
				elif m == 'email':
					d = {}
					d['modelName'] = 'email'
					d['searchField'] = processWowSearchData(request.POST.get('email'), False)
					d['type']  = 'text'
					d['isNumber'] = False
					data.append(d)
				elif m == 'probationOfficer':
					d = {}
					d['modelName'] = 'probationOfficer'
					d['searchField'] = processWowSearchData(request.POST.get('probationOfficer'), False)
					d['type']  = 'text'
					d['isNumber'] = False
					data.append(d)

				elif m == 'month':
					d = {}
					d['modelName'] = 'month'
					d['searchField'] = request.POST.get('month')
					d['type']  = 'date'
					d['isNumber'] = True
					data.append(d)
				elif m == 'day':
					d = {}
					d['modelName'] = 'day'
					d['searchField'] = request.POST.get('day')
					d['type']  = 'date'
					d['isNumber'] = True
					data.append(d)
				elif m == 'year':
					d = {}
					d['modelName'] = 'year'
					d['searchField'] = request.POST.get('year')
					d['type']  = 'date'
					d['isNumber'] = True
					data.append(d)
				elif m == 'ref':
					d = {}
					d['searchField'] = request.POST.get('ref')
					d['modelName'] = 'reason_ref'
					d['type']  = 'id'
					d['isNumber'] = True					
					data.append(d)

			searchType = request.POST.get('search_type')
			discharged = truePythonBool(request.POST.get('m_discharged'))
			pending = truePythonBool(request.POST.get('m_pending'))
			getFullDOB = truePythonBool(request.POST.get('fullDOB'))

			print "SEARCH TYPE: " + str(searchType)

			if searchType == 'start_session' or searchType == 'general':
				l_NameList = wowClientMatch(data, discharged, pending, getFullDOB, None)
			elif searchType == 'couple_search':
				session = ClientSession.objects.get(id=(getSessionID(user)))
				l_NameList = wowClientMatch(data, discharged, pending, getFullDOB, session)


			# f_NameList = wowClientMatchFname(data, discharged, pending, getFullDOB, session)

			pages = breakToPages(l_NameList, 8)
			# pagesFname = breakToPages(matchFname, 8)
			json_data = json.dumps(pages)
			# json_fname = json.dumps(pagesFname)
			numMatches = len(l_NameList)

			if numMatches == 1:
				phrase1 = 'Result'
			else:
				phrase1 = 'Results'

			content['search_type'] = searchType
			content['phrase1'] = phrase1
			content['json_data'] = json_data
			# content['json_fname'] = json_fname
			content['numPages'] = len(pages)
			content['numMatches'] = numMatches
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/wowSearchResults.html', content)

@login_required(login_url='/index')
def documentLoader(request):
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
			session = ClientSession.objects.get(id=(track.s_id))
			c1_clientID = session.client.clientID
			c2_clientID = Client.objects.get(id=(track.c2_id)).clientID
			docs = coupleDocumentFetch(c1_clientID, c2_clientID)
			serializedDocuments = documentSerializer(docs)
			json_data = json.dumps(serializedDocuments)

			content['json_data'] 	= json_data
			content['numDocs'] 		= len(docs)
			content['docList'] 		= docs
			content['title'] 		= "Uploads | Simeon Academy"
			return render_to_response('counselor/client/documentLoader.html', content)

@login_required(login_url='/index')
def confirmDocumentDeletion(request):
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
			content['title'] = "Upload Documents | Simeon Academy"
			return render_to_response('counselor/client/confirmDocumentDeletion.html', content)

@login_required(login_url='/index')
def m_errors(request):
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
			content['title'] = "Upload Documents | Simeon Academy"
			return render_to_response('global/m_errors.html', content)

@login_required(login_url='/index')
def coupleUpload(request):
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
			content['title'] = "Upload Documents | Simeon Academy"
			return render_to_response('counselor/client/coupleUpload.html', content)

@login_required(login_url='/index')
def docActionTaken(request):
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
			action = str(request.POST.get('documentAction'))
			session 	= ClientSession.objects.get(id=(track.s_id))
			c1_clientID = session.client.clientID
			c2_clientID = Client.objects.get(id=(track.c2_id)).clientID

			if action == 'delete':
				doc_er = request.POST.get('selectedDocId')
				delDoc = Attachment.objects.get(id=doc_er)
				delDoc.delete()

			docs = coupleDocumentFetch(c1_clientID, c2_clientID)
			serializedDocuments = documentSerializer(docs)
			json_data = json.dumps(serializedDocuments)

			content['json_data'] 	= json_data
			content['numDocs'] 		= len(docs)
			content['docList'] 		= docs
			content['title'] 		= "Uploads | Simeon Academy"
			return render_to_response('counselor/client/docActionTaken.html', content)

@login_required(login_url='/index')
def uploadSuccess2(request):
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
			session 	= ClientSession.objects.get(id=(track.s_id))
			c1_clientID = session.client.clientID
			c2_clientID = Client.objects.get(id=(track.c2_id)).clientID
			title 		= request.POST.get('title')
			doc 		= request.FILES['upload']
			newDoc = Attachment(clientID=c1_clientID, clientID2=c2_clientID, title=title, document=doc, isCouple=True)
			newDoc.save()

			content['title'] = "Upload Documents | Simeon Academy"
			return render_to_response('counselor/client/uploadSuccess2.html', content)

@login_required(login_url='/index')
def noteLoader(request):
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
			session = ClientSession.objects.get(id=(track.s_id))
			c1_clientID = session.client.clientID
			c2_clientID = Client.objects.get(id=(track.c2_id)).clientID
			notes = getCoupleNotesWowBuilder(c1_clientID, c2_clientID)
			serializedNotes = noteSerializer(notes)
			json_data = json.dumps(serializedNotes)

			content['json_data'] = json_data
			content['numNotes']  = len(notes)
			content['noteList']  = notes
			content['c1'] 		 = c1_clientID
			content['c2'] 		 = c2_clientID
			content['title'] 	 = "Couple Counseling | Simeon Academy"
			return render_to_response('counselor/client/noteLoader.html', content)

@login_required(login_url='/index')
def view_pdf(request):
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
			path = str(request.POST.get('selectedDocPath'))
			return render_to_response('counselor/client/noteLoader.html', content)





@login_required(login_url='/index')
def noteActionTaken(request):
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
			action = str(request.POST.get('noteAction'))

			if action == 'save':
				note = Note.objects.get(id=(request.POST.get('selectedNoteId')))
				note.title 	= request.POST.get('selectedNoteSubject')
				note.note 	= request.POST.get('selectedNoteBody')
				note.save()
			elif action == 'delete':
				note = Note.objects.get(id=(request.POST.get('selectedNoteId')))
				note.delete()
			elif action == 'new':
				subject 	= request.POST.get('selectedNoteSubject')
				body 		= request.POST.get('selectedNoteBody')
				c1 			= request.POST.get('c1')
				c2 			= request.POST.get('c2')
				date 		= datetime.now().date()
				newNote 	= Note(clientID=c1, clientID_2=c2, date=date, title=subject, note=body, isCouple=True)
				newNote.save()

			session = ClientSession.objects.get(id=(track.s_id))
			c1_clientID = session.client.clientID
			c2_clientID = Client.objects.get(id=(track.c2_id)).clientID
			notes = getCoupleNotesWowBuilder(c1_clientID, c2_clientID)
			serializedNotes = noteSerializer(notes)
			json_data = json.dumps(serializedNotes)

			content['json_data'] = json_data
			content['numNotes']  = len(notes)
			content['noteList']  = notes
			content['c1'] 		 = c1_clientID
			content['c2'] 		 = c2_clientID
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/noteActionTaken.html', content)

@login_required(login_url='/index')
def superNoteDisplyer(request):
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
			return render_to_response('counselor/client/superNoteDisplyer.html', content)



@login_required(login_url='/index')
def editableCoupleNote(request):
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
			return render_to_response('counselor/client/editableCoupleNote.html', content)


@login_required(login_url='/index')
def coupleNoteDual(request):
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
			return render_to_response('counselor/client/coupleNoteDual.html', content)



@login_required(login_url='/index')
def viewProfile(request):
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

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html')

		else:
			client = Client.objects.get(id=(superDuperFetchClientID_track(track)))
			gender = None
			work = None
			probation = None
			emergency = None

			if client.isMale == True:
				gender = "Male"
			else:
				gender = "Female"

			if client.work_phone == None or client.work_phone == "":
				work = "N/A"
			else:
				work = client.work_phone

			if client.probationOfficer==None or client.probationOfficer=='' or client.probation_phone==None or client.probation_phone=='':
				probation = "N/A"
			else:
				probation = str(client.probationOfficer) + " " + str(fetchClientPhoneDisplay(client.probation_phone))

			if client.emer_contact_name==None or client.emer_contact_name=='' or client.emer_phone==None or client.emer_phone=='':
				emergency = "N/A"
			else:
				emergency = str(client.emer_contact_name) + " " + str(fetchClientPhoneDisplay(client.emer_phone))

			content['emergency'] = emergency
			content['probation'] = probation
			content['phone'] = fetchClientPhoneDisplay(client.phone)
			content['ss'] =fetchClientSSDisplay(client.ss_num)
			content['work'] = fetchClientPhoneDisplay(client.work_phone)
			content['gender'] = gender
			content['client'] = client
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/viewProfile.html', content)

@login_required(login_url='/index')
def viewFullProfile_primary(request):
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
			client = Client.objects.get(id=(superDuperFetchClientID_track(track)))
			gender = None
			work = None
			probation = None
			emergency = None

			if client.isMale == True:
				gender = "Male"
			else:
				gender = "Female"

			if client.work_phone == None or client.work_phone == "":
				work = "N/A"
			else:
				work = client.work_phone

			if client.probationOfficer==None or client.probationOfficer=='' or client.probation_phone==None or client.probation_phone=='':
				probation = "N/A"
			else:
				probation = str(client.probationOfficer) + " " + str(fetchClientPhoneDisplay(client.probation_phone))

			if client.emer_contact_name==None or client.emer_contact_name=='' or client.emer_phone==None or client.emer_phone=='':
				emergency = "N/A"
			else:
				emergency = str(client.emer_contact_name) + " " + str(fetchClientPhoneDisplay(client.emer_phone))

			content['emergency'] = emergency
			content['probation'] = probation
			content['phone'] = fetchClientPhoneDisplay(client.phone)
			content['ss'] =fetchClientSSDisplay(client.ss_num)
			content['work'] = fetchClientPhoneDisplay(client.work_phone)
			content['gender'] = gender
			content['client'] = client
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/viewFullProfileMin.html', content)

@login_required(login_url='/index')
def viewFullProfile_secondary(request):
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
			client = Client.objects.get(id=(track.c2_id))
			gender = None
			work = None
			probation = None
			emergency = None

			if client.isMale == True:
				gender = "Male"
			else:
				gender = "Female"

			if client.work_phone == None or client.work_phone == "":
				work = "N/A"
			else:
				work = client.work_phone

			if client.probationOfficer==None or client.probationOfficer=='' or client.probation_phone==None or client.probation_phone=='':
				probation = "N/A"
			else:
				probation = str(client.probationOfficer) + " " + str(fetchClientPhoneDisplay(client.probation_phone))

			if client.emer_contact_name==None or client.emer_contact_name=='' or client.emer_phone==None or client.emer_phone=='':
				emergency = "N/A"
			else:
				emergency = str(client.emer_contact_name) + " " + str(fetchClientPhoneDisplay(client.emer_phone))

			content['emergency'] = emergency
			content['probation'] = probation
			content['phone'] = fetchClientPhoneDisplay(client.phone)
			content['ss'] =fetchClientSSDisplay(client.ss_num)
			content['work'] = fetchClientPhoneDisplay(client.work_phone)
			content['gender'] = gender
			content['client'] = client
			content['title'] = "Client Search | Simeon Academy"
			return render_to_response('counselor/client/viewFullProfileMin.html', content)
			

@login_required(login_url='/index')
def newClientBaseless(request):
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
			date = datetime.now()
			yy = date.year
			backwards = []
			years = []

			for i in range((yy - 90), (yy)):
				backwards.append(i)
				years.append('')

			reverse = len(backwards)
			index = reverse - 1

			for j in range(reverse):
				years[j] = backwards[index]
				index -= 1

			ref_list = RefReason.objects.all().order_by('reason')
			refs = []
			for r in ref_list:
				refs.append(str(r.reason))

			content['refs'] 	= ref_list
			content['years'] 	= years
			content['states'] 	= State.objects.all().order_by('state')
			content['title'] 	= "New Client | Simeon Academy"
			return render_to_response('counselor/client/newClientBaseless.html', content)

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
def new_note_pad(request):
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
			content['title'] = "New Note | Simeon Academy"
			return render_to_response('counselor/client/newNotePad.html', content)

@login_required(login_url='/index')
def notePadAdded(request):
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
			client = Client.objects.get(id=superDuperFetchClientID_track(track))
			subject = request.POST.get('subject')
			body = request.POST.get('body')
			date = datetime.now().date()
			newNote = Note(date=date, title=subject, note=body, clientID=client.id, isCouple=False)
			newNote.save()

			content['client'] = client
			content['note'] = newNote
			content['title'] = "New Note | Simeon Academy"
			return render_to_response('counselor/client/notePadAdded.html', content)

@login_required(login_url='/index')
def notePadDeleted(request):
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
			note = Note.objects.get(id=(request.POST.get('note_id')))
			note.delete()
			content['title'] = "Note Deleted | Simeon Academy"
			return render_to_response('counselor/client/notePadDeleted.html', content)

@login_required(login_url='/index')
def notePadErrorPage(request):
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
			content['title'] = "Note Pad Error | Simeon Academy"
			return render_to_response('counselor/client/notePadErrorPage.html', content)

@login_required(login_url='/index')
def simpleUpload(request):
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
			content['title'] = "Upload Documents | Simeon Academy"
			return render_to_response('counselor/client/simpleUpload.html', content)


@login_required(login_url='/index')
def uploadSuccess(request):
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
			client = Client.objects.get(id=superDuperFetchClientID_track(track))
			title = request.POST.get('title')
			doc = request.FILES['upload']
			attach = Attachment(clientID=client.clientID, title=title, document=doc)
			attach.save()
			content['title'] = "Upload Documents | Simeon Academy"
			return render_to_response('counselor/client/uploadSuccess.html', content)

@login_required(login_url='/index')
def uploadError(request):
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
			content['title'] = "Upload Error | Simeon Academy"
			return render_to_response('counselor/client/uploadError.html', content)

@login_required(login_url='/index')
def startCoupleSession(request):
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
			c1 = Client.objects.get(id=(superDuperFetchClientID_track(track)))
			content['title'] = "Couple's Therapy | Simeon Academy"
			content['c1'] = c1

			if isExistingCouple(c1.clientID) == True:
				content['couples'] = fetchExisitingCouples(c1)
				return render_to_response('counselor/client/existingCouples.html', content)
			else:
				return render_to_response('counselor/client/startCoupleSession.html', content)

@login_required(login_url='/index')
def chooseNewPair(request):
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
			content['searchType'] = 'couple'
			content['title'] = "New Note | Simeon Academy"
			return render_to_response('counselor/client/startCoupleSession.html', content)


@login_required(login_url='/index')
def coupleSession(request):
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
			c2_id = None
			c2_type = str(request.POST.get('c2Type'))

			if c2_type == "existing":
				c2_id = request.POST.get('c2_id')
				track.c2_id = c2_id
				track.save()
			elif c2_type == "new":
				c2_id = track.c2_id


			c1 			= Client.objects.get(id=(superDuperFetchClientID_track(track)))
			c2 			= Client.objects.get(id=c2_id)
			build 		= superCoupleStarter(c1.clientID, c2.clientID)
			# notes 		= getCoupleNotesWowBuilder(c1.clientID, c2.clientID)
			couple 		= build['couple']
			# json_data 	= json.dumps(noteSerializer(notes))


			content['c1'] 		 = c1
			content['c2'] 		 = c2
			# content['json_data'] = json_data
			content['c1phone'] 	 = wowPhoneNumberDisplayConverter(c1.phone)
			content['c2phone'] 	 = wowPhoneNumberDisplayConverter(c2.phone)
			content['c1ss'] 	 = wowSSNumberDisplayConverterHidden(c1.ss_num)
			content['c2ss'] 	 = wowSSNumberDisplayConverterHidden(c2.ss_num)
			content['couple_id'] = couple.id
			content['session_id'] = track.s_id
			content['title'] 	 = "Couple's Therapy | Simeon Academy"
			# content['loadedNotes'] = len(notes)
			return render_to_response('counselor/client/coupleSession.html', content)

@login_required(login_url='/index')
def blankOnlyErrorHighlighted(request):
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
			return render_to_response('counselor/client/blankOnlyErrorHighlighted.html', content)

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

			states 		= getStates()
			refs 		= getRefReasons()
			client 		= Client.objects.get(id=(getGlobalClientID(user)))
			selects 	= {}
			stateSel 	= getOrderedStateIndex(str(client.state))
			refSel 		= getOrderedRefIndex(str(client.reason_ref))

			dob = decodeDate(client.dob)

			selects['state']  	= stateSel
			selects['ref']	  	= refSel
			selects['gender'] 	= client.isMale
			selects['day'] 		= dob['day']
			selects['month'] 	= dob['month']
			selects['year']	  	= snagYearIndex(dob['year'])
			json_data = json.dumps(selects)

			content['client'] 			= client
			content['states'] 			= states
			content['reason']			= refs
			content['phone'] 			= fetchClientPhoneDisplay(client.phone)
			content['ssn']				= fetchClientSSDisplay(client.ss_num)
			content['work_phone']		= fetchClientPhoneDisplay(client.work_phone)
			content['prob_phone']		= fetchClientPhoneDisplay(client.probation_phone)
			content['json_data'] 		= json_data
			return render_to_response('counselor/client/editClientInfo.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def submitClientUpdate(request):
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
			client = Client.objects.get(id=(track.client_id))
			updateClientAccount(client, request)
			return render_to_response('counselor/client/editClientInfo.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def clientAccountUpdated(request):
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
			client = Client.objects.get(id=(track.client_id))
			content['client_id'] = client.id
			return render_to_response('counselor/client/updateAccountSuccess.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def updateClientPage(request):
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
			client = Client.objects.get(id=(track.client_id))
			fields = fetchClientUpdatedFields(client)
			json_data = json.dumps(fields)
			content['json_data'] = json_data
			return render_to_response('counselor/client/updatingParent.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def confirmDeleteClient(request):
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
			return render_to_response('counselor/client/confirmDelete.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def clientDeleteSucess(request):
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
			return render_to_response('counselor/client/clientRemoved.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def clientInvoiceMain(request):
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
			client = Client.objects.get(id=(track.client_id))
			content['client'] = client
			return render_to_response('counselor/client/clientInvoiceMain.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def clientFiles(request):
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
			client = Client.objects.get(id=(track.client_id))
			content['client'] = client
			return render_to_response('counselor/client/clientFiles.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def clientAppointments(request):
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
			client = Client.objects.get(id=(track.client_id))
			content['client'] = client
			return render_to_response('counselor/client/clientAppointments.html', content, context_instance=RequestContext(request))

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
			track = getTrack(user)
			quickTrack('Session', track)
			content['tracking'] = track.state.state
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

			content['phone'] = wowPhoneNumberDisplayConverter(session.client.phone)
			content['ssn'] = fetchClientSSDisplay(session.client.ss_num)
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

			setGlobalClientID(client.id, user)

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
			content['displayPhone'] = wowPhoneNumberDisplayConverter(session.client.phone)
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
			session_id = track.s_id

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

			elif str(form_type) == 'couple':
				couple_id = request.POST.get('couple_id', '')
				form = Couple.objects.get(id=couple_id)
				type_header = 'Couple Counseling'

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
			exit_to = request.POST.get('exit_to')
			exit_type = request.POST.get('exit_type')
			multiNav = request.POST.get('multiNav')
			exit_type = str(exit_type)
			content['exit_to'] = exit_to

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
			form_type = str(request.POST.get('form_type'))
			form = None

			if form_type == 'mh':
				form = session.mh
				content['formHead'] = 'Mental Health'
			elif form_type == 'am':
				form = session.am
				content['formHead'] = 'Anger Management'
			elif form_type == 'sap':
				form = session.sap
				content['formHead'] = 'S.A.P'
			elif form_type == 'asi':
				form = session.asi
				content['formHead'] = 'Addiction Severity Index'

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


@login_required(login_url='/index')
def underConstruction(request):
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
			return render_to_response('global/underConstruction.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def dataTemplate(request):
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
			return render_to_response('global/dataTemplate.html', content, context_instance=RequestContext(request))



###########################################################################################################################################
################################################################ END GENERIC ##############################################################
###########################################################################################################################################

###########################################################################################################################################
###########################################################################################################################################
#----------------------------------------------------------------- SCHEDULE --------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################


@login_required(login_url='/index')
def setSchedule(request):
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
			data = get_JSON_workSchedule(user)
			json_data = json.dumps(data)
			content['json_data'] = json_data
			return render_to_response('counselor/schedule/setSchedule.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def workDateSelector(request):
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
			return render_to_response('counselor/schedule/workDateSelector.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def calendarSaved(request):
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
			pre = 'save'
			saveThese = []
			numToSave = request.POST.get('numSaved')
			numToSave = int(numToSave)

			for i in range(numToSave):
				num = i + 1
				name = pre + str(num)
				obj = request.POST.get(name)
				saveThese.append(obj)

			for st in saveThese:
				data = decodeCalendarData(st)
				newWorkSchedule(data, request)


			content['title'] = "Simeon Academy"
			return render_to_response('counselor/main/appointments.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def viewAppointments(request):
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
			return render_to_response('counselor/schedule/viewAppointments.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def avaiableAppointments(request):
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
			return render_to_response('counselor/schedule/avaiableAppointments.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def apptHistory(request):
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
			return render_to_response('counselor/schedule/apptHistory.html', content, context_instance=RequestContext(request))


###########################################################################################################################################
################################################################ END SCHEDULE #############################################################
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
def generateErrors(request):
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
			return render_to_response('global/generateErrors.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def error_zero(request):
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
			return render_to_response('global/error_zero.html', content, context_instance=RequestContext(request))

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
def am_angerHistory2_suicide(request):
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
			data = {}
			track = getTrack(user)
			quickTrack('Session', track)
			session = ClientSession.objects.get(id=(track.s_id))

			data['isComplete'] 					= session.am.angerHistoryComplete2
			data['suicideTodayRecentV'] 		= session.am.angerHistory2.suicideTodayRecentV
			data['suicideTodayPlanRecentV'] 	= session.am.angerHistory2.suicideTodayPlanRecentV
			data['suicideTodayExplainRecentV'] 	= session.am.angerHistory2.suicideTodayExplainRecentV
			data['hasAttemptedSuicide'] 		= session.am.angerHistory2.hasAttemptedSuicide
			data['hasAttemptedExplainRecentV'] 	= session.am.angerHistory2.hasAttemptedExplainRecentV

			json_data = json.dumps(data)
			content['json_data'] = json_data
			content['fields'] = data
			return render_to_response('counselor/forms/AngerManagement/suicide.html', content, context_instance=RequestContext(request))

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
def finishChildhood(request):
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
			data = {}
			track = getTrack(user)
			quickTrack('Session', track)
			session = ClientSession.objects.get(id=(track.s_id))
			data['isComplete'] = session.am.childhoodComplete
			data['childAnger'] = session.am.childhood.childAnger
			data['otherChild'] = session.am.childhood.otherChild
			data['parentViolence'] = session.am.childhood.parentViolence
			json_data = json.dumps(data)
			content['json_data'] = json_data
			content['form'] = session.am.childhood
			return render_to_response('counselor/forms/AngerManagement/finishChildhood.html', content, context_instance=RequestContext(request))

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
			content = fetchContent(request, 'am', '/am_viewForm/')
			return render_to_response('counselor/forms/AngerManagement/viewForm.html', content, context_instance=RequestContext(request))

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
def dynamic_useTable(request):
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
			return render_to_response('counselor/forms/MentalHealth/dynamic_useTable.html', content, context_instance=RequestContext(request))


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
			state_list_init = State.objects.all().order_by('state')
			state_list = []
			data = {}

			for s in state_list_init:
				state_list.append(s.state)

			data['male'] = mh.demographics.childrenMale
			data['female'] = mh.demographics.childrenFemale
			data['brother'] = mh.demographics.bothers
			data['sister'] = mh.demographics.sisters
			json_data = json.dumps(data);

			content['mh'] = mh		
			# content['states'] = states
			content['state_list'] = state_list
			content['json_data'] = json_data
			content['title'] = "Simeon Academy | Mental Health Assessment"
			return render_to_response('counselor/forms/MentalHealth/mhDemoOpPage.html', content)

@login_required(login_url='/index')
def op_input_error(request):
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
			return render_to_response('counselor/forms/MentalHealth/op_input_error.html', content)

@login_required(login_url='/index')
def op_type_error(request):
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
			return render_to_response('counselor/forms/MentalHealth/op_type_error.html', content)

@login_required(login_url='/index')
def op_item_exist(request):
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
			return render_to_response('counselor/forms/MentalHealth/op_item_exist.html', content)

@login_required(login_url='/index')
def mh_to_op_errors(request):
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
			return render_to_response('counselor/forms/MentalHealth/mh_to_op_errors.html', content)

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
def viewASIinstruction(request):
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
			return render_to_response('counselor/forms/ASI/viewASIinstruction.html', content, context_instance=RequestContext(request))


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
def new_comment(request):
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
			return render_to_response('counselor/forms/ASI/new_comment.html', content, context_instance=RequestContext(request))

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
			content 						= startForm(request, 'discharge')
			content['m_phone'] 				= wowPhoneNumberDisplayConverter(content['session'].client.phone)
			content['m_work_phone'] 		= wowPhoneNumberDisplayConverter(content['session'].client.work_phone)
			content['m_probation_phone'] 	= wowPhoneNumberDisplayConverter(content['session'].client.probation_phone)
			content['m_emer_phone'] 		= wowPhoneNumberDisplayConverter(content['session'].client.emer_phone)
			content['m_ssn'] 				= wowSSNumberDisplayConverter(content['session'].client.ss_num)

			isMale = content['session'].client.isMale

			if isMale == True:
				content['gender'] = "Male"
			else:
				content['gender'] = "Female"

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


@login_required(login_url='/index')
def startStudentEval(request):
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

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			# hasExisting = False
			client_id = superDuperFetchClientID_track(track)
			client = Client.objects.get(id=client_id)
			# existing = getAllClientCraffts(client)
			content['client_id'] = client.id
			content['title'] = 'CRAFFT Screening | Simeon Academy'

			# if len(existing) > 0:
			# 	hasExisting = True

			# content['hasExisting'] = hasExisting
			return render_to_response('counselor/forms/Crafft/crafft_a.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def crafft_b(request):
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

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['a1'] 		 = request.POST.get('a1')
			content['a2'] 		 = request.POST.get('a2')
			content['a3'] 		 = request.POST.get('a3')
			content['b1'] 		 = request.POST.get('b1')
			content['client_id'] = request.POST.get('client_id')
			content['title'] 	 = 'CRAFFT Screening | Simeon Academy'
			return render_to_response('counselor/forms/Crafft/crafft_b.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def crafft_Results(request):
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

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			date 	= datetime.now().date()
			client 	= Client.objects.get(id=(request.POST.get('client_id')))
			crafft 	= Crafft(date_of_assessment=date, client=client, positiveScreen=False)

			crafft.a1 = truePythonBool(request.POST.get('a1'))
			crafft.a2 = truePythonBool(request.POST.get('a2'))
			crafft.a3 = truePythonBool(request.POST.get('a3'))
			crafft.b1 = truePythonBool(request.POST.get('b1'))
			crafft.b2 = truePythonBool(request.POST.get('b2'))
			crafft.b3 = truePythonBool(request.POST.get('b3'))
			crafft.b4 = truePythonBool(request.POST.get('b4'))
			crafft.b5 = truePythonBool(request.POST.get('b5'))
			crafft.b6 = truePythonBool(request.POST.get('b6'))
			crafft 	  = superCrafftSaver(crafft)

			score = crafft_fetchResults(crafft)
			responses = crafft_fetchResponses(crafft)
			content['crafft_result'] = 'NEGATIVE'
			content['phrase'] = "No additional assessment is required"

			if crafft.positiveScreen == True:
				content['crafft_result'] = 'POSITIVE'
				content['phrase'] = "Additional assessment is suggested"

			content['responses'] 	= responses
			content['score'] 		= score['score']
			content['ranking'] 		= score['ranking']
			content['image'] 		= score['image']
			content['crafft'] 		= crafft
			content['title'] 		= 'CRAFFT Screening | Simeon Academy'
			return render_to_response('counselor/forms/Crafft/crafft_Results.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def crafft_viewScoreInstruction(request):
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
		content['user'] = user

		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content['title'] = 'CRAFFT Screening | Simeon Academy'
			return render_to_response('counselor/forms/Crafft/crafft_viewScoreInstruction.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def treatmentResourcesMain(request):
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
			r_list 				= sortResourceColumns()
			right 				= r_list['right']
			left 				= r_list['left']
			numSrcs 			= len(right) + len(left)
			content['right'] 	= right
			content['left'] 	= left
			content['numSrcs'] 	= numSrcs
			content['id_data'] 	= json.dumps(fetchAllResourceIds())
			content['raw_ids'] 	= json.dumps(fetchRawIdNumberResources())
			content['title'] 	= 'Manage Treatment Resources | Simeon Academy'
			return render_to_response('counselor/main/treatmentResourcesMain.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def treatmentResourcesMain2(request):
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
			r_list 				= sortResourceColumns()
			right 				= r_list['right']
			left 				= r_list['left']
			numSrcs 			= len(right) + len(left)
			content['right'] 	= right
			content['left'] 	= left
			content['numSrcs'] 	= numSrcs
			content['id_data'] 	= json.dumps(fetchAllResourceIds())
			content['raw_ids'] 	= json.dumps(fetchRawIdNumberResources())
			content['title'] 	= 'Manage Treatment Resources | Simeon Academy'
			return render_to_response('counselor/main/treatmentResourcesMain.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def newTreatmentResource(request):
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
			content['states'] = states
			content['title'] = 'Manage Treatment Resources'
			return render_to_response('counselor/main/newTreatmentResource.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def editTreatmentResource(request):
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
			content['states'] = states
			content['title'] = 'Manage Treatment Resources'
			return render_to_response('counselor/main/editResource.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def generalMessage(request):
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
			content['title'] = 'Manage Treatment Resources'
			return render_to_response('global/generalMessage.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def generalDeleteConfirm(request):
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
			content['message'] = 'Are You Sure You Want To Delete This?'
			return render_to_response('global/generalDeleteConfirm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def generalSaveConfirm(request):
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
			return render_to_response('global/generalSaveConfirm.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def generalDeleteElement(request):
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
			form = None
			form_id = request.POST.get('form_id')
			form_type = str(request.POST.get('form_type'))

			if form_type == 'treatmentResource':
				form = TreatmentResource.objects.get(id=form_id)
			elif form_type == 'crafft':
				form = Crafft.objects.get(id=form_id)

			form.delete()

			content['title'] = 'Manage Treatment Resources'
			content['message'] = "Sucessfully Deleted"
			return render_to_response('global/generalMessage.html', content, context_instance=RequestContext(request))

def generalSaveElement(request):
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
			form_type = str(request.POST.get('form_type'))
			
			if form_type == 'discharge':
				client = Client.objects.get(id=(request.POST.get('client_id')))
				discharge = saveDischarge(request, client)

			content['message'] = " "
			return render_to_response('global/generalMessageClose.html', content, context_instance=RequestContext(request))


@login_required(login_url='/index')
def newResourceCreated(request):
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
			name 					= request.POST.get('name')
			address 				= request.POST.get('address')
			city 					= request.POST.get('city')
			state 					= request.POST.get('state')
			zip_code 				= request.POST.get('zip_code')
			director_name 			= request.POST.get('director_name')
			director_title 			= str(request.POST.get('director_title'))
			phone 					= request.POST.get('phone')
			fax 					= request.POST.get('fax')
			email 					= request.POST.get('email')
			website 				= request.POST.get('website')
			isDAS 					= truePythonBool(request.POST.get('m_isDAS'))
			isAccredited 			= truePythonBool(request.POST.get('m_isAccredited'))
			isHandiCap 				= truePythonBool(request.POST.get('m_isHandiCap'))
			type_organ 				= request.POST.get('type_organ')
			tpye_treat 				= request.POST.get('m_tpye_treat')

			resource 				= TreatmentResource(name=name)
			resource.address 		= address
			resource.city 			= city
			resource.state 			= state
			resource.zip_code 		= zip_code
			resource.director_name 	= director_name
			resource.director_title = director_title
			resource.phone 			= phone
			resource.fax 			= fax
			resource.email 			= email
			resource.website 		= website
			resource.isDAS 			= isDAS
			resource.isAccredited 	= isAccredited
			resource.isHandiCap 	= isHandiCap
			resource.type_organ 	= type_organ
			resource.tpye_treat 	= tpye_treat
			resource.save()

			content['title'] = 'Manage Treatment Resources'
			return render_to_response('counselor/main/newResourceCreated.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def resourceEdited(request):
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
			r_id 					= request.POST.get('r_id')
			name 					= request.POST.get('name')
			address 				= request.POST.get('address')
			city 					= request.POST.get('city')
			state 					= request.POST.get('state')
			zip_code 				= request.POST.get('zip_code')
			director_name 			= request.POST.get('director_name')
			director_title 			= request.POST.get('director_title')
			phone 					= request.POST.get('phone')
			fax 					= request.POST.get('fax')
			email 					= request.POST.get('email')
			website 				= request.POST.get('website')
			isDAS 					= truePythonBool(request.POST.get('m_isDAS'))
			isAccredited 			= truePythonBool(request.POST.get('m_isAccredited'))
			isHandiCap 				= truePythonBool(request.POST.get('m_isHandiCap'))
			type_organ 				= request.POST.get('type_organ')
			tpye_treat 				= request.POST.get('m_tpye_treat')

			resource 				= TreatmentResource.objects.get(id=r_id)
			resource.address 		= address
			resource.city 			= city
			resource.state 			= state
			resource.zip_code 		= zip_code
			resource.director_name 	= director_name
			resource.director_title = director_title
			resource.phone 			= phone
			resource.fax 			= fax
			resource.email 			= email
			resource.website 		= website
			resource.isDAS 			= isDAS
			resource.isAccredited 	= isAccredited
			resource.isHandiCap 	= isHandiCap
			resource.type_organ 	= type_organ
			resource.tpye_treat 	= tpye_treat
			resource.save()

			content['message'] = 'Sucessfully Updated'
			content['title'] = 'Manage Treatment Resources'
			return render_to_response('global/generalMessage.html', content, context_instance=RequestContext(request))































@login_required(login_url='/index')
def roommate_page(request):
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
			proceed = str(request.POST.get('save_this'))

			if proceed == 'new_roommate':
				name = str(request.POST.get('name'))
				phone = str(request.POST.get('phone'))
				email = str(request.POST.get('email'))
				notes = str(request.POST.get('notes'))
				date = str(request.POST.get('viewDate'))
				isMale = str(request.POST.get('isMale'))
				isCandidate = str(request.POST.get('isCandidate'))
				mm = date[0]
				mm += date[1]
				dd = date[3]
				dd += date[4]
				yy = date[6]
				yy += date[7]
				yy += date[8]
				yy += date[9]
				mm = int(mm)
				dd = int(dd)
				yy = int(yy)
				date = datetime(yy, mm, dd)
				date = date.date()
				if isMale == 'False':
					isMale = False
				elif isMale == 'True':
					isMale = True
				if isCandidate == 'False':
					isCandidate = False
				elif isCandidate == 'True':
					isCandidate = True
				candidate = Roommate(name=name, phone=phone, email=email, viewDate=date, isMale=isMale, notes=notes, isCandidate=isCandidate)
				candidate.save()

			elif proceed == 'new_application':
				firstName = str(request.POST.get('firstName'))
				lastName = str(request.POST.get('lastName'))
				phone = str(request.POST.get('phone'))
				ssn = str(request.POST.get('ssn'))
				email = str(request.POST.get('email'))
				dob = str(request.POST.get('dob'))
				employer = str(request.POST.get('employer'))
				work_phone = str(request.POST.get('work_phone'))
				occupation = str(request.POST.get('occupation'))
				emergency_contact = str(request.POST.get('emergency_contact'))
				emergency_phone = str(request.POST.get('emergency_phone'))
				ref1 = str(request.POST.get('ref1'))
				ref2 = str(request.POST.get('ref2'))
				ref3 = str(request.POST.get('ref3'))
				ref1_phone = str(request.POST.get('ref1_phone'))
				ref2_phone = str(request.POST.get('ref2_phone'))
				ref3_phone = str(request.POST.get('ref3_phone'))
				description = str(request.POST.get('description'))

				isMale = str(request.POST.get('isMale'))
				isAuthorized = str(request.POST.get('isAuthorized'))

				if isMale == 'True':
					isMale = True
				elif isMale == 'False':
					isMale = False
				if isAuthorized == 'True':
					isAuthorized = True
				elif isAuthorized == 'False':
					isAuthorized = False

				app = Application(firstName=firstName, lastName=lastName, phone=phone, ssn=ssn, email=email, dob=dob)
				app.employer = employer
				app.work_phone = work_phone
				app.occupation =occupation
				app.emergency_contact = emergency_contact
				app.emergency_phone = emergency_phone
				app.ref1 = ref1
				app.ref2 = ref2
				app.ref3 = ref3
				app.ref1_phone = ref1_phone
				app.ref2_phone = ref2_phone
				app.ref3_phone = ref3_phone
				app.isMale = isMale
				app.isAuthorized = isAuthorized
				app.description = description
				app.save()
			elif proceed == 'save_evaluation':
				eval_id = int(request.POST.get('eval_id'))
				evaluation = RoommateEvaluation.objects.get(id=eval_id)

				hasCheckstubs 	= truePythonBool(request.POST.get('hasCheckstubs'))
				hasCredit 		= truePythonBool(request.POST.get('hasCredit'))
				hasId 			= truePythonBool(request.POST.get('hasId'))
				ref1_verified 	= truePythonBool(request.POST.get('ref1_verified'))
				ref2_verified 	= truePythonBool(request.POST.get('ref2_verified'))
				ref3_verified 	= truePythonBool(request.POST.get('ref3_verified'))
				work_verified 	= truePythonBool(request.POST.get('work_verified'))
				personality 	= truePythonBool(request.POST.get('personality'))
				isCandidate 	= truePythonBool(request.POST.get('isCandidate'))
				notes 			= request.POST.get('notes')

				if hasCheckstubs == True:
					if hasCredit == True:
						if hasId == True:
							if ref1_verified == True:
								if ref2_verified == True:
									if ref3_verified == True:
										if work_verified == True:
											if personality == True:
												evaluation.application.isEvaluated = True
												evaluation.isComplete = True
												evaluation.application.save()
												evaluation.save()

				evaluation.hasCheckstubs 	= hasCheckstubs
				evaluation.hasCredit 		= hasCredit
				evaluation.hasId 			= hasId
				evaluation.ref1_verified 	= ref1_verified
				evaluation.ref2_verified 	= ref2_verified
				evaluation.ref3_verified 	= ref3_verified
				evaluation.work_verified 	= work_verified
				evaluation.personality 		= personality
				evaluation.isCandidate 		= isCandidate
				evaluation.notes 			= notes
				evaluation.save()
			elif proceed == 'rate_applicant':
				rating = str(request.POST.get('rating')) 
				isCandidate = truePythonBool(request.POST.get('isCandidate')) 
				a_id = str(request.POST.get('app_id'))
				applicant = Application.objects.get(id=a_id)

				applicant.rating = rating
				applicant.isCandidate = isCandidate
				applicant.save()

			return render_to_response('global/roommate_page.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_new(request):
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
			return render_to_response('global/roommate_new.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_ref(request):
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
			return render_to_response('global/roommate_ref.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_eval(request):
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
			proceed = str(request.POST.get('save_this'))
			app_list = Application.objects.all().order_by('firstName')
			col1 = []
			col2 = []
			eval_list = []

			if proceed == 'save_evaluation':
				eval_id = int(request.POST.get('eval_id'))
				evaluation = RoommateEvaluation.objects.get(id=eval_id)

				hasCheckstubs 	= truePythonBool(request.POST.get('hasCheckstubs'))
				hasCredit 		= truePythonBool(request.POST.get('hasCredit'))
				hasId 			= truePythonBool(request.POST.get('hasId'))
				ref1_verified 	= truePythonBool(request.POST.get('ref1_verified'))
				ref2_verified 	= truePythonBool(request.POST.get('ref2_verified'))
				ref3_verified 	= truePythonBool(request.POST.get('ref3_verified'))
				work_verified 	= truePythonBool(request.POST.get('work_verified'))
				personality 	= truePythonBool(request.POST.get('personality'))
				isCandidate 	= truePythonBool(request.POST.get('isCandidate'))
				notes 			= request.POST.get('notes')

				if hasCheckstubs == True:
					if hasCredit == True:
						if hasId == True:
							if ref1_verified == True:
								if ref2_verified == True:
									if ref3_verified == True:
										if work_verified == True:
											if personality == True:
												evaluation.application.isEvaluated = True
												evaluation.isComplete = True
												evaluation.application.save()
												evaluation.save()

				evaluation.hasCheckstubs 	= hasCheckstubs
				evaluation.hasCredit 		= hasCredit
				evaluation.hasId 			= hasId
				evaluation.ref1_verified 	= ref1_verified
				evaluation.ref2_verified 	= ref2_verified
				evaluation.ref3_verified 	= ref3_verified
				evaluation.work_verified 	= work_verified
				evaluation.personality 		= personality
				evaluation.isCandidate 		= isCandidate
				evaluation.notes 			= notes
				evaluation.save()

			for a in app_list:
				if a.isEvaluated == False:
					eval_list.append(a)

			for i in range(len(eval_list)):
				if i % 2 == 0:
					col1.append(eval_list[i])
				else:
					col2.append(eval_list[i])

			content['e_list'] = eval_list
			content['col1'] = col1
			content['col2'] = col2
			return render_to_response('global/roommate_eval.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_all(request):
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
			col1 = []
			col2 = []
			col3 = []
			col4 = []
			c_list = []
			start1 = 1
			start2 = 4
			start3 = 7
			start4 = 10
			index = 2
			candidates = Roommate.objects.all().order_by('name')

			for r in range(12):
				c_list.append(None)

			for i in range(len(candidates)):
				c_list[i] = candidates[i]

			for w in range(3):
				data1 = {}
				data2 = {}
				data3 = {}
				data4 = {}

				data1['num'] = start1
				data2['num'] = start2
				data3['num'] = start3
				data4['num'] = start4

				data1['name_id'] = 'nm_id' + str(start1)
				data2['name_id'] = 'nm_id' + str(start2)
				data3['name_id'] = 'nm_id' + str(start3)
				data4['name_id'] = 'nm_id' + str(start4)

				col1.append(data1)
				col2.append(data2)
				col3.append(data3)
				col4.append(data4)

				start1 += 1
				start2 += 1
				start3 += 1
				start4 += 1

			col1[0]['applicant'] = c_list[0]
			col1[1]['applicant'] = c_list[1]
			col1[2]['applicant'] = c_list[2]

			col2[0]['applicant'] = c_list[3]
			col2[1]['applicant'] = c_list[4]
			col2[2]['applicant'] = c_list[5]

			col3[0]['applicant'] = c_list[6]
			col3[1]['applicant'] = c_list[7]
			col3[2]['applicant'] = c_list[8]

			col4[0]['applicant'] = c_list[9]
			col4[1]['applicant'] = c_list[10]
			col4[2]['applicant'] = c_list[11]


			for i in range(3):
				if col1[index]['applicant'] == None:
					col1.pop(index)
				if col2[index]['applicant'] == None:
					col2.pop(index)
				if col3[index]['applicant'] == None:
					col3.pop(index)
				if col4[index]['applicant'] == None:
					col4.pop(index)

				index = index - 1

			content['col1'] = col1
			content['col2'] = col2
			content['col3'] = col3
			content['col4'] = col4
			return render_to_response('global/roommate_all.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_win(request):
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
			app_list = Application.objects.all().order_by('firstName')
			eval_list = []
			proceed = str(request.POST.get('save_this'))

			if proceed == 'rate_applicant':
				rating = str(request.POST.get('rating')) 
				isCandidate = truePythonBool(request.POST.get('isCandidate')) 
				a_id = str(request.POST.get('app_id'))
				applicant = Application.objects.get(id=a_id)

				applicant.rating = rating
				applicant.isCandidate = isCandidate
				applicant.isRated = True
				applicant.save()

			for a in app_list:
				if a.isEvaluated == True and a.isRated == False:
					eval_list.append(a)

			if len(eval_list) == 0:
				content['message'] = "There are no completed applications."
			else:
				content['message'] = "Select An Applicant"
				col1 = []
				col2 = []
				for i in range(len(eval_list)):
					if i % 2 == 0:
						col1.append(eval_list[i])
					else:
						col2.append(eval_list[i])
				content['col1'] = col1
				content['col2'] = col2

			content['e_list'] = eval_list
			return render_to_response('global/roommate_win.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def verify_rm_delete(request):
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
			return render_to_response('global/roommate_verify_rm_delete.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def complete_rm_removal(request):
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
			r_list = []
			i_list = []

			r_list.append(request.POST.get('re1'))
			r_list.append(request.POST.get('re2'))
			r_list.append(request.POST.get('re3'))
			r_list.append(request.POST.get('re4'))
			r_list.append(request.POST.get('re5'))
			r_list.append(request.POST.get('re6'))
			r_list.append(request.POST.get('re7'))
			r_list.append(request.POST.get('re8'))
			r_list.append(request.POST.get('re9'))
			r_list.append(request.POST.get('re10'))
			r_list.append(request.POST.get('re11'))
			r_list.append(request.POST.get('re12'))

			for r in r_list:
				if str(r) != 'empty':
					item = Roommate.objects.get(id=r)
					item.delete()

			return render_to_response('global/complete_rm_removal.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_view_application(request):
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
			current = request.POST.get('current')
			applicant = Application.objects.get(id=current)
			content['applicant'] = applicant
			content['rating'] = applicant.rating
			content['isCandidate'] = applicant.isCandidate
			return render_to_response('global/roommate_view_application.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def roommate_profile(request):
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
			evaluation = None
			match = False
			gender = None
			current = request.POST.get('current')
			applicant = Application.objects.get(id=current)

			if applicant.isMale == True:
				gender = 'Male'
			else:
				gender = 'Female'
			
			eval_list = RoommateEvaluation.objects.all()
			for e in eval_list:
				if e.application == applicant and e.application.isEvaluated == False:
					evaluation = e
					match = True
					break

			if match == False:
				evaluation = RoommateEvaluation(application=applicant)
				evaluation.save()

			content['stub'] = evaluation.hasCheckstubs
			content['credit'] = evaluation.hasCredit
			content['d_id'] = evaluation.hasId
			content['ref1'] = evaluation.ref1_verified
			content['ref2'] = evaluation.ref2_verified
			content['ref3'] = evaluation.ref3_verified
			content['work'] = evaluation.work_verified
			content['pNality'] = evaluation.personality
			content['candidate'] = evaluation.isCandidate
			content['notes'] = evaluation.notes
			content['gender'] = gender
			content['eval'] = evaluation
			return render_to_response('global/roommate_profile.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def rm_edit_app(request):
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
			return render_to_response('global/rm_edit_app.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def rm_delete_app(request):
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
			return render_to_response('global/rm_delete_app.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def rm_top_apps(request):
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
			return render_to_response('global/rm_top_apps.html', content, context_instance=RequestContext(request))

@login_required(login_url='/index')
def rm_new_lease(request):
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
			return render_to_response('global/rm_new_lease.html', content, context_instance=RequestContext(request))












































