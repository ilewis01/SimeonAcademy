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
AIS_Admin, AIS_General, AIS_Medical, AIS_Employment, AIS_Drug1, AIS_Drug2, \
AIS_Legal, AIS_Family, AIS_Social1, AIS_Social2, AIS_Psych, ASI

from assessment.view_functions import convert_datepicker, generateClientID, \
getStateID, getReasonRefID, clientExist, getClientByName, getClientByDOB, \
getClientByID, getClientBySS, getEducationID, getLivingID, getMaritalID, \
getActiveClients, getDischargedClients, getTimes, convert_phone, phone_to_integer, \
grabClientOpenForm, grabGenericForm, deleteGenericForm, getOrderedStateIndex, \
getGlobalID, decodeCharfield, force_URL_priority, startForm, fetchUrl, \
fetchContent, saveForm, deleteForm, refreshForm, saveAndFinish, startSession

# from assessment.view_functions import convert_datepicker, generateClientID,\
# getStateID, getReasonRefID, clientExist, getClientByName, getClientByDOB, \
# getClientByID, getClientBySS, getEducationID, getLivingID, getMaritalID, \
# amDemographicExist, findClientAM, clientAmExist, continueToAmSection, \
# mhDemographicExist, clientMhExist, getClientMhList, findClientMH, \
# continueToMhSection, getActiveClients, getDischargedClients, utExist, \
# getUtsByDate, deleteOldUTS, getTimes, convert_phone, phone_to_integer, \
# saveIncompleteSapForm, grabClientOpenForm, grabGenericForm, deleteGenericForm, \
# getOrderedStateIndex, getGlobalID, decodeCharfield, force_URL_priority, \
# startForm, fetchUrl, fetchContent, saveForm,  deleteForm, refreshForm, saveAndFinish, \

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
			client_id = request.POST.get('client_id', '')
			new_session = request.POST.get('new_session', '')
			goToNext = request.POST.get('goToNext', '')

			client = Client.objects.get(id=client_id)
			start = datetime.now()
			phone = convert_phone(client.phone)

			session = None
			session_type = None

			if new_session == 'false':
				session_id = request.POST.get('session_id', '')
				session = ClientSession.objects.get(id=session_id)
				session_type = session.s_type.session_type

			else:
				session_type = request.POST.get('session_type', '')
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

@login_required(login_url='/index')
def comfirmSessionEnd(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			session_id = request.POST.get('session_id', '')
			session = ClientSession.objects.get(id=session_id)

			content['session'] = session
			content['title'] = "Simeon Academy | Confirm Billing Details"
			return render_to_response('global/comfirmSessionEnd.html', content)

###########################################################################################################################################
################################################################ END CLIENT ###############################################################
###########################################################################################################################################


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
				prioritySapSection(last_section, form)
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

			form = grabGenericForm(form_type, form_id)
			deleteGenericForm(form_type, form)

			content['form_type'] = form_type
			content['form_id'] = form_id
			content['title'] = "Simeon Academy"
			return render_to_response('global/genericFormDeleted.html', content)



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
			mh_id = getGlobalID()
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
			client_id = request.POST.get('client_id', '')
			session_id = request.POST.get('session_id', '')

			client = Client.objects.get(id=client_id)
			session = ClientSession.objects.get(id=session_id)

			action = startForm('asi', client)
			asi = action['asi']
			setGlobalID(asi.id)

			content['asi'] = asi
			content['session'] = session

			if action['isNew'] == False:
				next_section = fetchUrl('asi', None, asi)

				content['form'] = asi
				content['form_type'] = 'asi'
				content['type_header'] = 'A.S.I'
				content['next_section'] = next_section
				content['save_section'] = next_section
				content['title'] = "Simeon Academy | AngerManagement"
				return render_to_response('global/resolve_form.html', content)

			else:
				content['title'] = "Simeon Academy | Addiction Severity Index"
				return render_to_response('counselor/forms/ASI/instructions.html', content)

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
def asi_drug2(request):
	user = request.user
	if not user.is_authenticated():
		render_to_response('global/index.html')

	else:
		content = {}
		content.update(csrf(request))
		content['user'] = user
		if user.account.is_counselor == False:
			content['title'] = 'Restricted Access'
			return render_to_response('global/restricted.html', content)

		else:
			content = fetchContent(request, 'asi', '/asi_drug2/')
			return render_to_response('counselor/forms/ASI/drug2.html', content, context_instance=RequestContext(request))

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
			content = universalContent(request, 'asi', '/asi_admin/')
			return render_to_response('counselor/forms/ASI/viewForm.html', content, context_instance=RequestContext(request))

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


###########################################################################################################################################
################################################################ END UT ###################################################################
###########################################################################################################################################


###########################################################################################################################################
###########################################################################################################################################
#-------------------------------------------------------------- DISCHARGE ----------------------------------------------------------------#
###########################################################################################################################################
###########################################################################################################################################


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








































