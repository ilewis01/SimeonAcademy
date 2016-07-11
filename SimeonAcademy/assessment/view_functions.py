from datetime import datetime
from datetime import date, timedelta
from django.shortcuts import render_to_response
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
import random
import string
import json
import json as simplejson

from assessment.models import State, RefReason, Client, \
AngerManagement, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, MHUseTable, \
MHFamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_AngerHistory2, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHBackground, MHEducation, \
MHStressor, MHLegalHistory, ClientSession, Invoice, SType, AM_AngerHistory3, \
Global_ID, AIS_Admin, AIS_General, AIS_Medical, AIS_Employment, AIS_Drug1, \
AIS_Legal, AIS_Family, AIS_Social1, AIS_Social2, AIS_Psych, ASI

def clientEqual(c1, c2):
	isEqual = False
	if str(c1.fname) == str(c2.fname) and str(c1.lname) == str(c2.lname) and str(c1.id) == str(c2.id) and str(c1.clientID) == str(c2.clientID):
		isEqual = True
	return isEqual

def onTrue_offFalse(data):
	if data == 'on':
		data = True
	else:
		data = False
	return data

def getOrderedStateIndex(the_state):
	index = 0

	states = State.objects.all().order_by('state')
	s_list = []

	for s in states:
		s_list.append(s.state)

	for i in range(len(s_list)):
		if str(the_state) == str(s_list[i]):
			index = i
			break

	if str(the_state) == None or str(the_state) == 'None Selected' or str(the_state) == '':
		index = 0
	else:
		index = index + 1

	return index

def convertRadioToBoolean(data):
	result = True

	if data == 'no':
		result = False

	return result

def convert_phone(phone):
	result = '('
	result += phone[0]
	result += phone[1]
	result += phone[2]
	result += ') '

	result += phone[3]
	result += phone[4]
	result += phone[5]
	result += '-'

	result += phone[6]
	result += phone[7]
	result += phone[8]
	result += phone[9]
	return result

def phone_to_integer(phone):
	result = ''

	for p in phone:
		if p=='0' or p=='1' or p=='2' or p=='3' or p=='4' or p=='5' or p=='6' or p=='7' or p=='8' or p=='9':
			result += p

	return result

##_____________________________SEARCH CLIENT FORMS_____________________________________________________

def grabClientAMForms(client):
	ams = AngerManagement.objects.all()
	search = True
	results = []

	if len(ams) == 0:
		search = False

	if search == True:
		for a in ams:
			if (str(client.id) == str(a.client.id)) and (str(client.clientID) == str(a.client.clientID)):
				results.append(a)
	return results

def grabClientSAPForms(client):
	saps = SAP.objects.all()
	search = True
	results = []

	if len(saps) == 0:
		search = False

	if search == True:
		for s in saps:
			if (str(client.id) == str(s.client.id)) and (str(client.clientID) == str(s.client.clientID)):
				results.append(s)
	return results

def grabClientMHForms(client):
	mhs = MentalHealth.objects.all()
	search = True
	results = []

	if len(mhs) == 0:
		search = False

	if search == True:
		for m in mhs:
			if (str(client.id) == str(m.client.id)) and (str(client.clientID) == str(m.client.clientID)):
				results.append(m)
	return results

def grabClientASIForms(client):
	asis = ASI.objects.all()
	search = True
	results = []

	if len(asis) == 0:
		search = False

	if search == True:
		for a in asis:
			if (str(client.id) == str(a.client.id)) and (str(client.clientID) == str(a.client.clientID)):
				results.append(a)
	return results


########################################################################################################

def resolveBlankRadio(radio, defaultValue):
	result = None

	if radio == None or radio == '':
		result = defaultValue
	else:
		result = radio
	return result

def convert_datepicker(the_date):
	month = ''
	day = ''
	year = ''
	results = {}
	month += the_date[0]
	month += the_date[1]
	day += the_date[3]
	day += the_date[4]
	year += the_date[6]
	year += the_date[7]
	year += the_date[8]
	year += the_date[9]

	month = int(month)
	day = int(day)
	year = int(year)
	results['month'] = month
	results['day'] = day
	results['year'] = year
	date = datetime(year, month, day)
	results['date'] = date.date()
	return results

def generateClientID(lname):
	results = str(lname)

	for i in range(5):
		rand = str(random.randint(0,9))
		results += rand

	results += '-'

	for s in range(3):
		alp = random.choice(string.ascii_uppercase)
		results += alp

	return results

def getStateID(state):
	states = State.objects.all()
	result = None

	for s in states:
		if str(state) == str(s.state):
			result = s.id 
			break

	return result

def getReasonRefID(reason):
	reasons = RefReason.objects.all()
	result = None

	for r in reasons:
		if str(r.reason) == str(reason):
			result = r.id
			break

	return result

def clientExist(client):
	clients = Client.objects.all()
	result = False

	for c in clients:
		if str(client.fname) == str(c.fname) and str(client.lname) == str(c.lname) and str(client.ss_num) == str(c.ss_num):
			result = True
			break

	return result

def filterSS(ss_num):
	result = ''

	for s in ss_num:
		if s=='0' or s=='1' or s=='2' or s=='3' or s=='4' or s=='5' or s=='6' or s=='7' or s=='8' or s=='9':
			result += s
	return result

def getClientBySS(ss_num):
	results = []
	clients = Client.objects.all()
	ss_num = filterSS(ss_num)

	for c in clients:
		sNum = filterSS(c.ss_num)
		if str(ss_num) == str(sNum):
			results.append(c)

	return results

def getClientByID(clientID):
	results = []
	clients = Client.objects.all()
	clientID = clientID.lower()

	for c in clients:
		compare = str(c.clientID).lower()
		if str(clientID) == str(compare):
			results.append(c)

	return results

def getClientByDOB(dob):
	results = []
	clients = Client.objects.all()

	for c in clients:
		if str(dob) == str(c.dob):
			results.append(c)

	return results

def getClientByName(fname, lname):
	results = []
	clients = Client.objects.all()

	fname = fname.lower()
	lname = lname.lower()

	for c in clients:
		compF = str(c.fname).lower()
		compL = str(c.lname).lower()
		if str(fname) == str(compF) and str(lname) == str(compL):
			results.append(c)
		elif str(lname) == None or str(lname) == '':
			if str(fname) == str(compF):
				results.append(c)
		elif str(fname) == None or str(fname) == '':
			if str(lname) == str(compL):
				results.append(c)

	return results

def startSession(client, session_type):
	sessionList = ClientSession.objects.all()
	check_sessions = True
	createNewSession = True
	session = None

	if len(sessionList) == 0:
		check_sessions = False

	if check_sessions == True:
		for s in sessionList:
			if (str(s.client.clientID) == str(client.clientID)) and (s.isComplete == False):
				session = s
				createNewSession = False
				break

	if createNewSession == True:
		startTime = datetime.now()
		session = ClientSession(client=client, start=startTime, s_type=session_type)
		session.save()

	return session


def getMaritalID(marital):
	m_id = None
	maritals = MaritalStatus.objects.all()

	for m in maritals:
		if str(marital) == str(m.status):
			m_id = m.id
			break
	return m_id

def getLivingID(living):
	l_id = None
	livings = LivingSituation.objects.all()

	for l in livings:
		if str(living) == str(l.situation):
			l_id = l.id
			break
	return l_id

def getEducationID(education):
	e_id = None
	educations = EducationLevel.objects.all()

	for e in educations:
		if str(education) == str(e.level):
			e_id = e.id
			break
	return e_id

def amDemographicExist(demo):
	demographics = AM_Demographic.objects.all()
	secondTest = True
	results = {}
	results['exist'] = False
	results['am_demo'] = None

	if len(demographics) == 0:
		secondTest = False

	if secondTest == True:
		for d in demographics:
			if str(d.client_id) == str(demo.client_id) and str(d.date_of_assessment) == str(demo.date_of_assessment):
				results['exist'] = True
				results['am_demo'] = d
				break
	return results

def getAM_byDemographic(demo):
	result = None
	ams = AngerManagement.objects.all()

	for a in ams:
		if str(a.demographic.client.clientID) == str(demo.client.clientID) and str(a.demographic.date_of_assessment) == str(demo.date_of_assessment):
			result = a

	return result

def mhDemographicExist(demo):
	demographics = MHDemographic.objects.all()
	results = {}
	results['exist'] = False
	results['mh_demo'] = None

	for d in demographics:
		if str(d.client.id) == str(demo.client.id) and str(d.birthplace) == str(demo.birthplace):
			results['exist'] = True
			results['mh_demo'] = d
			break
	return results

def SAPDemographicExist(demo):
	demographics = SapDemographics.objects.all()
	results = {}
	results['exist'] = False
	results['sap_demo'] = None

	for d in demographics:
		if str(d.client.id) == str(demo.client.id) and str(d.date1) == str(demo.date1) and str(d.client.clientID) == str(demo.client.clientID):
			results['exist'] = True
			results['sap_demo'] = d
			break
	return results

def clientAmExist(client):
	ams = AngerManagement.objects.all()
	exist = False
	filter_clients = True

	if len(ams) == 0:
		filter_clients = False

	if filter_clients == True:
		for a in ams:
			if a.demographic != None:
				if str(a.demographic.client_id) == str(client.clientID) and str(a.client.id) == str(client.id):
					exist = True
					break
	return exist

def clientMhExist(client):
	mhs = MentalHealth.objects.all()
	exist = False

	for m in mhs:
		if str(m.demographics.client.fname) == str(client.fname) and str(m.demographics.client.lname) == str(client.lname) and str(m.demographics.client.id) == str(client.id) and str(m.demographics.client.clientID) == str(client.clientID):
			exist = True
			break
	return exist

def clientSAPExist(client):
	saps = SAP.objects.all()
	exist = False

	for s in saps:
		if str(s.demographics.client.fname) == str(client.fname) and str(s.demographics.client.lname) == str(client.lname) and str(s.demographics.client.id) == str(client.id) and str(s.demographics.client.clientID) == str(client.clientID):
			exist = True
			break
	return exist

def getClientAmList(client):
	results = []
	ams = AngerManagement.objects.all()

	if clientAmExist(client) == True:
		for a in ams:
			if str(a.demographic.client_id) == str(client.clientID) and str(a.client.id) == str(client.id):
				results.append(a)
	return results

def getClientMhList(client):
	results = []
	mhs = MentalHealth.objects.all()

	if clientAmExist(client) == True:
		for m in mhs:
			if str(m.demographics.client.fname) == str(client.fname) and str(m.demographics.client.lname) == str(client.lname) and str(m.demographics.client.id) == str(client.id) and str(m.demographics.client.clientID) == str(client.clientID):
				results.append(m)
	return results

def getClientSAPList(client):
	results = []
	saps = SAP.objects.all()

	if clientSAPExist(client) == True:
		for s in saps:
			if str(s.demographics.client.fname) == str(client.fname) and str(s.demographics.client.lname) == str(client.lname) and str(s.demographics.client.id) == str(client.id) and str(s.demographics.client.clientID) == str(client.clientID):
				results.append(s)
	return results
	
def findClientAM(client):
	result = {}
	result['incomplete'] = False
	result['am'] = None
	am_list = getClientAmList(client)

	for a in am_list:
		if a.AMComplete == False:
			result['incomplete'] = True
			result['am'] = a
			break
	return result

def findClientMH(client):
	result = {}
	result['incomplete'] = False
	result['mh'] = None
	mh_list = getClientMhList(client)

	for m in mh_list:
		if m.MHComplete == False:
			result['incomplete'] = True
			result['mh'] = m
			break
	return result

def findClientSAP(client):
	result = {}
	result['incomplete'] = False
	result['sap'] = None
	sap_list = getClientSAPList(client)

	for s in sap_list:
		if s.SapComplete == False:
			result['incomplete'] = True
			result['sap'] = s
			break
	return result

def saveCompletedAmSection(request, section, am):
	if section == '/am_childhood/':
		momAlive = request.POST.get('momAlive', '')
		dadAlive = request.POST.get('dadAlive', '')
		childTrama = request.POST.get('childTrama', '')
		siblingsClose = request.POST.get('siblingsClose', '')
		dadClose = request.POST.get('dadClose', '')
		momClose = request.POST.get('momClose', '')
		wasAbused = request.POST.get('wasAbused', '')
		childAnger = request.POST.get('childAnger', '')
		otherChild = request.POST.get('otherChild', '')
		parentViolence = request.POST.get('parentViolence', '')

		#BOOLEAN FIELDS
		momAlive = truePythonBool(momAlive)
		dadAlive = truePythonBool(dadAlive)
		childTrama = truePythonBool(childTrama)
		siblingsClose = truePythonBool(siblingsClose)
		dadClose = truePythonBool(dadClose)
		momClose = truePythonBool(momClose)
		wasAbused = truePythonBool(wasAbused)
		childAnger = truePythonBool(childAnger)
		otherChild = truePythonBool(otherChild)
		parentViolence = truePythonBool(parentViolence)

		#DYNAMIC FIELDS
		traumaExplain = request.POST.get('m_traumaExplain', '')
		howLeftHome = request.POST.get('m_howLeftHome', '')
		abusedBy = request.POST.get('m_abusedBy', '')
		abuseImpact = request.POST.get('m_abuseImpact', '')
		childAngerExplain = request.POST.get('m_childAngerExplain', '')
		otherChildExplain = request.POST.get('m_otherChildExplain', '')
		parentViolenceExplain = request.POST.get('m_parentViolenceExplain', '')
		parentViolenceImpact = request.POST.get('m_parentViolenceImpact', '')

		#NORMAL FIELDS
		raisedBy = request.POST.get('raisedBy', '')
		howLeftHome = request.POST.get('howLeftHome', '')
		num_siblings = request.POST.get('num_siblings', '')
		siblingsRelationshipExplain = request.POST.get('siblingsRelationshipExplain', '')
		dadCloseExplain = request.POST.get('dadCloseExplain', '')
		momCloseExplain = request.POST.get('momCloseExplain', '')

		raisedBy = blankMustDie(raisedBy)
		howLeftHome = blankMustDie(howLeftHome)
		siblingsRelationshipExplain = blankMustDie(siblingsRelationshipExplain)
		dadCloseExplain = blankMustDie(dadCloseExplain)
		momCloseExplain = blankMustDie(momCloseExplain)

		childhood = am.childhood
		date = datetime.now()
		date = date.date()

		childhood.date_of_assessment = date
		childhood.raisedBy = raisedBy
		childhood.momAlive = momAlive
		childhood.dadAlive = dadAlive
		childhood.childTrama = childTrama
		childhood.traumaExplain = traumaExplain
		childhood.howLeftHome = howLeftHome
		childhood.num_siblings = num_siblings
		childhood.siblingsClose = siblingsClose
		childhood.siblingsRelationshipExplain = siblingsRelationshipExplain
		childhood.dadClose = dadClose
		childhood.dadCloseExplain = dadCloseExplain
		childhood.momClose = momClose
		childhood.momCloseExplain = momCloseExplain
		childhood.wasAbused = wasAbused
		childhood.abusedBy = abusedBy
		childhood.abuseImpact = abuseImpact
		childhood.childAnger = childAnger
		childhood.childAngerExplain = childAngerExplain
		childhood.otherChild = otherChild
		childhood.otherChildExplain = otherChildExplain
		childhood.parentViolence = parentViolence
		childhood.parentViolenceExplain = parentViolenceExplain
		childhood.parentViolenceImpact = parentViolenceImpact

		childhood.save()
		am.childhood = childhood
		am.save()

	elif section == '/am_angerHistory/':
		ah1 = am.angerHistory

		#DYNAMIC FIELDS
		physicalRecentV = request.POST.get('m_physicalRecentV', '')
		verbalRecentV = request.POST.get('m_verbalRecentV', '')
		threatsRecentV = request.POST.get('m_threatsRecentV', '')
		propertyRecentV = request.POST.get('m_propertyRecentV', '')
		otherRecentV = request.POST.get('m_otherRecentV', '')
		otherExplainRecentV = request.POST.get('m_otherExplainRecentV', '')
		wasTense = request.POST.get('m_wasTense', '')
		hadRush = request.POST.get('m_hadRush', '')
		feltStrong = request.POST.get('m_feltStrong', '')
		psychoRecentV = request.POST.get('m_psychoRecentV', '')
		psychoWhyRecentV = request.POST.get('m_psychoWhyRecentV', '')
		longAgoTreatRecentVmos = request.POST.get('m_longAgoTreatRecentVmos', '')
		longAgoTreatRecentVyrs = request.POST.get('m_longAgoTreatRecentVyrs', '')
		didCompleteTreatRecentV = request.POST.get('m_didCompleteTreatRecentV', '')
		reasonNotCompleteRecentV = request.POST.get('m_reasonNotCompleteRecentV', '')

		#NORMAL FIELDS
		recentIncidentV = request.POST.get('recentIncidentV', '')
		recentVDate = request.POST.get('recentVDate', '')
		recentVlocation = request.POST.get('recentVlocation', '')
		withWhomRecentV = request.POST.get('withWhomRecentV', '')
		happenedRecentV = request.POST.get('happenedRecentV', '')
		typeWordsRecentV = request.POST.get('typeWordsRecentV', '')

		physicalRecentV = truePythonBool(physicalRecentV)
		verbalRecentV = truePythonBool(verbalRecentV)
		threatsRecentV = truePythonBool(threatsRecentV)
		propertyRecentV = truePythonBool(propertyRecentV)
		otherRecentV = truePythonBool(otherRecentV)
		wasTense = truePythonBool(wasTense)
		hadRush = truePythonBool(hadRush)
		feltStrong = truePythonBool(feltStrong)
		psychoRecentV = truePythonBool(psychoRecentV)
		didCompleteTreatRecentV = truePythonBool(didCompleteTreatRecentV)

		date = datetime.now()
		date = date.date()

		ah1.date_of_assessment = date
		ah1.recentIncidentV = recentIncidentV				
		ah1.recentVDate = recentVDate
		ah1.recentVlocation = recentVlocation
		ah1.withWhomRecentV = withWhomRecentV
		ah1.happenedRecentV = happenedRecentV
		ah1.physicalRecentV = physicalRecentV
		ah1.verbalRecentV = verbalRecentV
		ah1.threatsRecentV = threatsRecentV
		ah1.propertyRecentV = propertyRecentV
		ah1.otherRecentV = otherRecentV
		ah1.otherExplainRecentV = otherExplainRecentV
		ah1.typeWordsRecentV = typeWordsRecentV
		ah1.wasTense = wasTense
		ah1.hadRush = hadRush
		ah1.feltStrong = feltStrong
		ah1.psychoRecentV = psychoRecentV
		ah1.psychoWhyRecentV = psychoWhyRecentV
		ah1.longAgoTreatRecentVmos = longAgoTreatRecentVmos
		ah1.longAgoTreatRecentVyrs = longAgoTreatRecentVyrs
		ah1.didCompleteTreatRecentV = didCompleteTreatRecentV
		ah1.reasonNotCompleteRecentV = reasonNotCompleteRecentV
		ah1.save()
		ah1 = am.angerHistory
		am.save()

	elif section == '/am_angerHistory2/':
		depress30RecentV = request.POST.get('m_depress30RecentV', '')
		depress30ExplainRecentV = request.POST.get('m_depress30ExplainRecentV', '')
		anxietyRecentV = request.POST.get('m_anxietyRecentV', '')
		anxietyExplainRecentV = request.POST.get('m_anxietyExplainRecentV', '')
		hallucinationRecentV = request.POST.get('m_hallucinationRecentV', '')
		hallucinationLastV = request.POST.get('m_hallucinationLastV', '')
		understandingRecentV = request.POST.get('m_understandingRecentV', '')
		understandingExplainRecentV = request.POST.get('m_understandingExplainRecentV', '')
		troubleControlRecentV = request.POST.get('m_troubleControlRecentV', '')
		lastTimeTroubleControl = request.POST.get('m_lastTimeTroubleControl', '')
		controlTrigger = request.POST.get('m_controlTrigger', '')
		suicide30RecentV = request.POST.get('m_suicide30RecentV', '')
		suicide30ExplainRecentV = request.POST.get('m_suicide30ExplainRecentV', '')
		suicideTodayRecentV = request.POST.get('m_suicideTodayRecentV', '')
		suicideTodayPlanRecentV = request.POST.get('m_suicideTodayPlanRecentV', '')
		suicideTodayExplainRecentV = request.POST.get('m_suicideTodayExplainRecentV', '')
		hasAttemptedSuicide = request.POST.get('m_hasAttemptedSuicide', '')
		hasAttemptedExplainRecentV = request.POST.get('m_hasAttemptedExplainRecentV', '')

		#CONVERT THE BOOLEAN FIELDS
		depress30RecentV = truePythonBool(depress30RecentV)
		anxietyRecentV = truePythonBool(anxietyRecentV)
		hallucinationRecentV = truePythonBool(hallucinationRecentV)
		understandingRecentV = truePythonBool(understandingRecentV)
		troubleControlRecentV = truePythonBool(troubleControlRecentV)
		suicide30RecentV = truePythonBool(suicide30RecentV)
		suicideTodayRecentV = truePythonBool(suicideTodayRecentV)
		suicideTodayPlanRecentV = truePythonBool(suicideTodayPlanRecentV)
		hasAttemptedSuicide = truePythonBool(hasAttemptedSuicide)

		#UPDATE ANGER HISTORY 2...
		date = datetime.now()
		date = date.date()

		ah2 = am.angerHistory2
		ah2.date_of_assessment = date

		ah2.depress30RecentV = depress30RecentV
		ah2.depress30ExplainRecentV = depress30ExplainRecentV
		ah2.anxietyRecentV = anxietyRecentV
		ah2.anxietyExplainRecentV = anxietyExplainRecentV
		ah2.hallucinationRecentV = hallucinationRecentV
		ah2.hallucinationLastV = hallucinationLastV
		ah2.understandingRecentV = understandingRecentV
		ah2.understandingExplainRecentV = understandingExplainRecentV
		ah2.troubleControlRecentV = troubleControlRecentV
		ah2.lastTimeTroubleControl = lastTimeTroubleControl
		ah2.controlTrigger = controlTrigger
		ah2.suicide30RecentV = suicide30RecentV
		ah2.suicide30ExplainRecentV = suicide30ExplainRecentV
		ah2.suicideTodayRecentV = suicideTodayRecentV
		ah2.suicideTodayPlanRecentV = suicideTodayPlanRecentV
		ah2.suicideTodayExplainRecentV = suicideTodayExplainRecentV
		ah2.hasAttemptedSuicide = hasAttemptedSuicide
		ah2.hasAttemptedExplainRecentV = hasAttemptedExplainRecentV

		ah2.save()
		am.save()

	elif section == '/am_worst/':
		useWorst = request.POST.get('m_useWorst', '')
		whoDidItFight = request.POST.get('m_whoDidItFight', '')
		physicalWorst = request.POST.get('m_physicalWorst', '')
		verbalWorst = request.POST.get('m_verbalWorst', '')
		threatsWorst = request.POST.get('m_threatsWorst', '')
		propertyWorst = request.POST.get('m_propertyWorst', '')
		otherWorst = request.POST.get('m_otherWorst', '')
		otherWorstDescription = request.POST.get('m_otherWorstDescription', '')

		#GET NORMAL TEXT FIELDS
		whoWorst = request.POST.get('whoWorst', '')
		happenedWorst = request.POST.get('happenedWorst', '')
		wordThoughtWorst = request.POST.get('wordThoughtWorst', '')
		howStartWorst = request.POST.get('howStartWorst', '')
		howEndWorst = request.POST.get('howEndWorst', '')

		#PROCESS THE CHECKBOXES AND RADIO BUTTONS
		useWorst = truePythonBool(useWorst)
		physicalWorst = truePythonBool(physicalWorst)
		verbalWorst = truePythonBool(verbalWorst)
		threatsWorst = truePythonBool(threatsWorst)
		propertyWorst = truePythonBool(propertyWorst)
		otherWorst = truePythonBool(otherWorst)				

		date = datetime.now()
		date = date.date()

		am.worstEpisode.date_of_assessment = date
		am.worstEpisode.whoWorst = whoWorst
		am.worstEpisode.happenedWorst = happenedWorst
		am.worstEpisode.wordThoughtWorst = wordThoughtWorst
		am.worstEpisode.howStartWorst = howStartWorst
		am.worstEpisode.howEndWorst = howEndWorst
		am.worstEpisode.useWorst = useWorst
		am.worstEpisode.whoDidItFight = whoDidItFight
		am.worstEpisode.physicalWorst = physicalWorst
		am.worstEpisode.verbalWorst = verbalWorst
		am.worstEpisode.threatsWorst = threatsWorst
		am.worstEpisode.propertyWorst = propertyWorst
		am.worstEpisode.otherWorst = otherWorst
		am.worstEpisode.otherWorstDescription = otherWorstDescription

		am.worstEpisode.save()
		am.save()

	elif section == '/am_drugHistory/':
		#PROCESS THE BOOLEAN FIELDS
		curUse = request.POST.get('use_drugs', '')
		everDrank = request.POST.get('ever_used', '')
		DUI = request.POST.get('has_dui', '')
		drugTreatment = request.POST.get('treatment', '')
		finishedTreatment = request.POST.get('completed_treatment', '')
		isClean = request.POST.get('still_abstinent', '')
		drinkLastEpisode = request.POST.get('drinking_last', '')
		drinkRelationshipProblem = request.POST.get('relationship_alc', '')
		needHelpDrugs = request.POST.get('need_help', '')

		everDrank = resolveBlankRadio(everDrank, 'False')
		DUI = resolveBlankRadio(DUI, 'False')
		finishedTreatment = resolveBlankRadio(finishedTreatment, 'True')
		isClean = resolveBlankRadio(isClean, 'True')

		curUse = truePythonBool(curUse)
		everDrank = truePythonBool(everDrank)
		DUI = truePythonBool(DUI)
		drugTreatment = truePythonBool(drugTreatment)
		finishedTreatment = truePythonBool(finishedTreatment)
		isClean = truePythonBool(isClean)
		drinkLastEpisode = truePythonBool(drinkLastEpisode)
		drinkRelationshipProblem = truePythonBool(drinkRelationshipProblem)
		needHelpDrugs = truePythonBool(needHelpDrugs)

		#PROCESS THE TEXT AND INTEGER FIELDS
		firstDrinkAge = request.POST.get('first_drink', '')
		firstDrinkType = request.POST.get('first_use_type', '')
		useType = request.POST.get('m_useType', '')
		amtPerWeek = request.POST.get('m_amtPerWeek', '')
		useAmt = request.POST.get('m_useAmt', '')
		monthsQuit = request.POST.get('m_monthsQuit', '')
		yearsQuit = request.POST.get('m_yearsQuit', '')
		reasonQuit = request.POST.get('m_reasonQuit', '')
		numDUI = request.POST.get('m_numDUI', '')
		BALevel = request.POST.get('m_BALevel', '')
		treatmentPlace = request.POST.get('m_treatmentPlace', '')
		dateTreated = request.POST.get('m_dateTreated', '')
		reasonNotFinishedTreatment = request.POST.get('m_reasonNotFinishedTreatment', '')
		relapseTrigger = request.POST.get('m_relapseTrigger', '')

		if curUse == True:
			everDrank = True

		date = datetime.now()
		date = date.date()

		#UPDATE DRUG HISTORY FORM
		demo = am.drugHistory
		demo.date_of_assessment = date
		demo.firstDrinkAge = firstDrinkAge
		demo.firstDrinkType = firstDrinkType
		demo.curUse = curUse
		demo.useType = useType
		demo.amtPerWeek = amtPerWeek
		demo.useAmt = useAmt
		demo.everDrank = everDrank
		demo.monthsQuit = monthsQuit
		demo.yearsQuit = yearsQuit
		demo.reasonQuit = reasonQuit
		demo.DUI = DUI
		demo.numDUI = numDUI
		demo.BALevel = BALevel
		demo.drugTreatment = drugTreatment
		demo.finishedTreatment = finishedTreatment
		demo.reasonNotFinishedTreatment = reasonNotFinishedTreatment
		demo.isClean = isClean
		demo.relapseTrigger = relapseTrigger
		demo.drinkLastEpisode = drinkLastEpisode
		demo.drinkRelationshipProblem = drinkRelationshipProblem
		demo.needHelpDrugs = needHelpDrugs
		demo.treatmentPlace = treatmentPlace
		demo.dateTreated = dateTreated

		demo.save()
		am.save()

	elif section == '/am_angerHistory3/':
		homicidal = request.POST.get('m_homicidal', '')
		homicidalExplain = request.POST.get('m_homicidalExplain', '')
		medRecentV = request.POST.get('m_medRecentV', '')
		medRecentVExplain = request.POST.get('m_medRecentVExplain', '')
		medSuccessRecentV = request.POST.get('m_medSuccessRecentV', '')
		medSuccessExplainRecentV = request.POST.get('m_medSuccessExplainRecentV', '')
		durationRecentV = request.POST.get('durationRecentV', '')
		intensityRecentV = request.POST.get('intensityRecentV')
		howOften = request.POST.get('howOften')

		homicidal = truePythonBool(homicidal)
		medRecentV = truePythonBool(medRecentV)
		medSuccessRecentV = truePythonBool(medSuccessRecentV)

		date = datetime.now()
		date = date.date()

		ah3 = am.angerHistory3
		ah3.date_of_assessment = date

		ah3.homicidal = homicidal
		ah3.homicidalExplain = homicidalExplain
		ah3.medRecentV = medRecentV
		ah3.medRecentVExplain = medRecentVExplain
		ah3.medSuccessRecentV = medSuccessRecentV
		ah3.medSuccessExplainRecentV = medSuccessExplainRecentV
		ah3.durationRecentV = durationRecentV
		ah3.intensityRecentV = intensityRecentV
		ah3.howOften = howOften

		ah3.save()
		am.save()

	elif section == '/am_problems/':
		date = datetime.now()
		date = date.date()

		brainInjury = request.POST.get('m_brainInjury', '')
		stroke = request.POST.get('m_stroke', '')
		epilepsy = request.POST.get('m_epilepsy', '')
		attentionDD = request.POST.get('m_attentionDD', '')
		pms = request.POST.get('m_pms', '')
		depression = request.POST.get('m_depression', '')
		ptsd = request.POST.get('m_ptsd', '')
		otherSeriousIllness = request.POST.get('m_otherSeriousIllness', '')
		currentlyOnMeds = request.POST.get('m_currentlyOnMeds', '')
		whichMeds = request.POST.get('m_whichMeds', '')
		describeIssue = request.POST.get('m_describeIssue', '')	

		brainInjury = truePythonBool(brainInjury)
		stroke = truePythonBool(stroke)
		epilepsy = truePythonBool(epilepsy)
		attentionDD = truePythonBool(attentionDD)
		depression = truePythonBool(depression)
		pms = truePythonBool(pms)
		ptsd = truePythonBool(ptsd)
		otherSeriousIllness = truePythonBool(otherSeriousIllness)
		currentlyOnMeds = truePythonBool(currentlyOnMeds)		

		#UPDATE CURRENT PROBLEMS DATABASE
		current = am.currentProblems
		current.date_of_assessment = date
		current.brainInjury = brainInjury
		current.stroke = stroke
		current.epilepsy = epilepsy
		current.attentionDD = attentionDD
		current.pms = pms
		current.depression = depression
		current.ptsd = ptsd
		current.otherSeriousIllness = otherSeriousIllness
		current.currentlyOnMeds = currentlyOnMeds
		current.whichMeds = whichMeds
		current.describeIssue = describeIssue

		am.currentProblems.save()
		am.save()

	elif section == '/am_familyOrigin/':
		date = datetime.now()
		date = date.date()

		kidMomAnger = request.POST.get('kidMomAnger', '')
		kidDadAnger = request.POST.get('kidDadAnger', '')
		kidSiblingAnger = request.POST.get('kidSiblingAnger', '')
		kidOtherAnger = request.POST.get('kidOtherAnger', '')
		learnFamilyAnger = request.POST.get('learnFamilyAnger', '')
		suicideHistory = request.POST.get('m_suicideHistory', '')
		hasLovingMother = request.POST.get('m_hasLovingMother', '')
		hasLovingSiblings = request.POST.get('m_hasLovingSiblings', '')

		suicideHistory = truePythonBool(suicideHistory)
		hasLovingMother = truePythonBool(hasLovingMother)
		hasLovingSiblings = truePythonBool(hasLovingSiblings)

		#UPDATE FAMILY OF ORGIN DATA
		family = am.familyOrigin

		family.date_of_assessment = date
		family.kidMomAnger = kidMomAnger
		family.kidDadAnger = kidDadAnger
		family.kidSiblingAnger = kidSiblingAnger
		family.kidOtherAnger = kidOtherAnger
		family.learnFamilyAnger = learnFamilyAnger
		family.suicideHistory = suicideHistory
		family.hasLovingMother = hasLovingMother
		family.hasLovingSiblings = hasLovingSiblings

		am.familyOrigin.save()
		am.save()

	elif section == '/am_demographic/':
		demo = am.demographic
		dateTime = datetime.now()
		date = dateTime.date()	

		#NORMAL FIELDS
		maritalStatus = request.POST.get('maritalStatus', '')
		livingSituation = request.POST.get('livingSituation', '')
		education = request.POST.get('education', '')

		months_res = request.POST.get('months_res', '')
		years_res = request.POST.get('years_res', '')
		num_children = request.POST.get('num_children', '')
		other_dependants = request.POST.get('other_dependants', '')
		job_title = request.POST.get('job_title', '')
		employee = request.POST.get('employee', '')
		emp_address = request.POST.get('emp_address', '')
		employer_phone = request.POST.get('employer_phone', '')
		employed_months = request.POST.get('employed_months', '')
		employed_years = request.POST.get('employed_years', '')

		#DYNAMIC FIELDS
		own = request.POST.get('m_own', '')
		drop_out = request.POST.get('m_drop_out', '')
		health_problem = request.POST.get('m_health_problem', '')
		medication = request.POST.get('m_medication', '')
		resasonDO = request.POST.get('m_resasonDO', '')
		health_exp = request.POST.get('m_health_exp', '')
		whatMedicine = request.POST.get('m_whatMedicine', '')

		employer_phone = phone_to_integer(employer_phone)

		#PROCESS THE RADIO BUTTONS
		own = truePythonBool(own)
		drop_out = truePythonBool(drop_out)
		health_problem = truePythonBool(health_problem)
		medication = truePythonBool(medication)

		demo.date_of_assessment 	= date
		demo.maritalStatus 			= maritalStatus
		demo.livingSituation 		= livingSituation
		demo.own 					= own
		demo.months_res 			= months_res
		demo.years_res 				= years_res
		demo.num_children 			= num_children
		demo.other_dependants 		= other_dependants
		demo.education 				= education
		demo.drop_out 				= drop_out
		demo.resasonDO 				= resasonDO
		demo.employee 				= employee
		demo.job_title 				= job_title
		demo.emp_address 			= emp_address
		demo.employed_months 		= employed_months
		demo.employed_years 		= employed_years
		demo.employer_phone 		= employer_phone
		demo.health_problem 		= health_problem
		demo.medication 			= medication
		demo.whatMedicine 			= whatMedicine
		demo.health_exp 			= health_exp

		demo.save()
		am.save()

	elif section == '/am_angerTarget/':
		angryPartner = request.POST.get('m_angryPartner', '')
		angryParents = request.POST.get('m_angryParents', '')
		angryChildren = request.POST.get('m_angryChildren', '')
		angryRelatives = request.POST.get('m_angryRelatives', '')
		angryEmployer = request.POST.get('m_angryEmployer', '')
		angryFriends = request.POST.get('m_angryFriends', '')
		angryOther = request.POST.get('m_angryOther', '')
		otherWhom = request.POST.get('m_otherWhom', '')
		angryAbout = request.POST.get('angryAbout', '')
		seldomUpset = request.POST.get('m_seldomUpset', '')

		angryPartner = truePythonBool(angryPartner)
		angryParents = truePythonBool(angryParents)
		angryChildren = truePythonBool(angryChildren)
		angryRelatives = truePythonBool(angryRelatives)
		angryEmployer = truePythonBool(angryEmployer)
		angryFriends = truePythonBool(angryFriends)
		angryOther = truePythonBool(angryOther)
		seldomUpset = truePythonBool(seldomUpset)

		date = datetime.now()
		date = date.date()

		target = am.angerTarget

		target.date_of_assessment = date
		target.angryPartner = angryPartner
		target.angryParents = angryParents
		target.angryChildren = angryChildren
		target.angryRelatives = angryRelatives
		target.angryEmployer = angryEmployer
		target.angryFriends = angryFriends
		target.angryOther = angryOther
		target.otherWhom = otherWhom
		target.angryAbout = angryAbout
		target.seldomUpset = seldomUpset

		target.save()
		am.save()

	elif section == '/am_control/':
		date = datetime.now()
		date = date.date()

		neverAttemptedControl 	= request.POST.get('m_neverAttemptedControl', '')
		talkToMyself 			= request.POST.get('m_talkToMyself', '')
		whatSayYou 				= request.POST.get('m_whatSayYou', '')
		leaveScene 				= request.POST.get('m_leaveScene', '')
		howLongLeaveScene 		= request.POST.get('m_howLongLeaveScene', '')
		whatDoLeave 			= request.POST.get('m_whatDoLeave', '')
		relax 					= request.POST.get('m_relax', '')
		howRelax 				= request.POST.get('m_howRelax', '')
		selfHelpGroup 			= request.POST.get('m_selfHelpGroup', '')
		otherControlAnger 		= request.POST.get('m_otherControlAnger', '')
		doWhatOtherControl 		= request.POST.get('m_doWhatOtherControl', '')

		neverAttemptedControl 	= truePythonBool(neverAttemptedControl)
		talkToMyself 			= truePythonBool(talkToMyself)
		leaveScene 				= truePythonBool(leaveScene)
		relax 					= truePythonBool(relax)
		selfHelpGroup 			= truePythonBool(selfHelpGroup)
		otherControlAnger 		= truePythonBool(otherControlAnger)

		control = am.control
		control.neverAttemptedControl = neverAttemptedControl
		control.talkToMyself = talkToMyself
		control.whatSayYou = whatSayYou
		control.leaveScene = leaveScene
		control.howLongLeaveScene = howLongLeaveScene
		control.whatDoLeave = whatDoLeave
		control.relax = relax
		control.howRelax = howRelax
		control.selfHelpGroup = selfHelpGroup
		control.otherControlAnger = otherControlAnger
		control.doWhatOtherControl = doWhatOtherControl
		control.date_of_assessment = date

		control.save()
		am.save()

	elif section == '/am_connections/':
		angerWorse = request.POST.get('m_angerWorse', '')
		troubleWhenUsing = request.POST.get('m_troubleWhenUsing', '')
		lessAngry = request.POST.get('m_lessAngry', '')
		othersTellMe = request.POST.get('m_othersTellMe', '')
		noConnection = request.POST.get('m_noConnection', '')
		otherConnectionsUsing = request.POST.get('m_otherConnectionsUsing', '')
		connectionExplain = request.POST.get('m_connectionExplain', '')

		angerWorse = truePythonBool(angerWorse)
		troubleWhenUsing = truePythonBool(troubleWhenUsing)
		lessAngry = truePythonBool(lessAngry)
		othersTellMe = truePythonBool(othersTellMe)
		noConnection = truePythonBool(noConnection)
		otherConnectionsUsing = truePythonBool(otherConnectionsUsing)

		date = datetime.now()
		date = date.date()

		am.connections.date_of_assessment = date
		am.connections.angerWorse = angerWorse
		am.connections.troubleWhenUsing = troubleWhenUsing
		am.connections.lessAngry = lessAngry
		am.connections.othersTellMe = othersTellMe
		am.connections.noConnection = noConnection
		am.connections.otherConnectionsUsing = otherConnectionsUsing
		am.connections.connectionExplain = connectionExplain

		am.connections.save()
		am.save()

	elif section == '/am_final/':
		anythingelse = request.POST.get('anythingelse', '')
		changeLearn1 = request.POST.get('changeLearn1', '')
		changeLearn2 = request.POST.get('changeLearn2', '')
		changeLearn3 = request.POST.get('changeLearn3', '')
		whoLivesWithClient = request.POST.get('whoLivesWithClient', '')

		date = datetime.now()
		date = date.date()

		final = am.final
		demo = am.demographic

		demo.whoLivesWithClient = whoLivesWithClient
		demo.save()

		final.date_of_assessment = date
		final.anythingelse = anythingelse
		final.changeLearn1 = changeLearn1
		final.changeLearn2 = changeLearn2
		final.changeLearn3 = changeLearn3

		final.save()
		am.save()



def deleteAM(am):
	am.demographic.delete()
	am.drugHistory.delete()
	am.childhood.delete()
	am.angerHistory.delete()
	am.angerHistory2.delete()
	am.angerHistory3.delete()
	am.connections.delete()
	am.worstEpisode.delete()
	am.angerTarget.delete()
	am.familyOrigin.delete()
	am.currentProblems.delete()
	am.control.delete()
	am.final.delete()
	am.delete()

	return am

def newAM(client):
	date = datetime.now()
	am = AngerManagement(client=client, AMComplete=False, start_time=date)
	date = date.date()

	demo = AM_Demographic(client_id=client.clientID, date_of_assessment=date)
	drugHistory = AM_DrugHistory(client_id=client.clientID, finishedTreatment=True)
	childhoodHistory = AM_ChildhoodHistory(client_id=client.clientID)
	angerHistory = AM_AngerHistory(client_id=client.clientID)
	angerHistory2 = AM_AngerHistory2(client_id=client.clientID)
	angerHistory3 = AM_AngerHistory3(client_id=client.clientID)
	connections = AM_Connections(client_id=client.clientID)
	worstEpisodes = AM_WorstEpisode(client_id=client.clientID)
	amTarget = AM_AngerTarget(client_id=client.clientID)
	familyOrigin = AM_FamilyOrigin(client_id=client.clientID)
	currentProblems = AM_CurrentProblem(client_id=client.clientID)
	amControl = AM_Control(client_id=client.clientID)
	amFinal = AM_Final(client_id=client.clientID)

	demo.save()
	drugHistory.save()
	childhoodHistory.save()
	angerHistory.save()
	angerHistory2.save()
	angerHistory3.save()
	connections.save()
	worstEpisodes.save()
	amTarget.save()
	familyOrigin.save()
	currentProblems.save()
	amControl.save()
	amFinal.save()

	am.demographic = demo
	am.drugHistory = drugHistory
	am.childhood = childhoodHistory
	am.angerHistory = angerHistory
	am.angerHistory2 = angerHistory2
	am.angerHistory3 = angerHistory3
	am.connections = connections
	am.worstEpisode = worstEpisodes
	am.angerTarget = amTarget
	am.familyOrigin = familyOrigin
	am.currentProblems = currentProblems
	am.control = amControl
	am.final = amFinal

	am.save()

	return am



def amSidebarImages(am, page):
	images = {}
	check = "/static/images/green_check.png"
	x = "/static/images/red_x.png"
	progress = "/static/images/yellow_progress.png"

	if am.demographicComplete == True and page != 'demo':
		images['demo_img'] = check
	elif page == 'viewForm':
		images['demo_img'] = check
	elif page == 'demo':
		images['demo_img'] = progress
	else:
		images['demo_img'] = x

	if am.drugHistoryComplete == True and page != 'dh':
		images['dh_img'] = check
	elif page == 'viewForm':
		images['dh_img'] = check
	elif page == 'dh':
		images['dh_img'] = progress
	else:
		images['dh_img'] = x

	if am.childhoodComplete == True and page != 'child':
		images['child_img'] = check
	elif page == 'viewForm':
		images['child_img'] = check
	elif page == 'child':
		images['child_img'] = progress
	else:
		images['child_img'] = x

	if am.angerHistoryComplete == True and page != 'ah1':
		images['ah1_img'] = check
	elif page == 'viewForm':
		images['ah1_img'] = check
	elif page == 'ah1':
		images['ah1_img'] = progress
	else:
		images['ah1_img'] = x

	if am.angerHistoryComplete2 == True and page != 'ah2':
		images['ah2_img'] = check
	elif page == 'viewForm':
		images['ah2_img'] = check
	elif page == 'ah2':
		images['ah2_img'] = progress
	else:
		images['ah2_img'] = x

	if am.angerHistoryComplete3 == True and page != 'ah3':
		images['ah3_img'] = check
	elif page == 'viewForm':
		images['ah3_img'] = check
	elif page == 'ah3':
		images['ah3_img'] = progress
	else:
		images['ah3_img'] = x

	if am.connectionsComplete == True and page != 'connect':
		images['connect_img'] = check
	elif page == 'viewForm':
		images['connect_img'] = check
	elif page == 'connect':
		images['connect_img'] = progress
	else:
		images['connect_img'] = x

	if am.worstComplete == True and page != 'worst':
		images['worst_img'] = check
	elif page == 'viewForm':
		images['worst_img'] = check
	elif page == 'worst':
		images['worst_img'] = progress
	else:
		images['worst_img'] = x

	if am.angerTargetComplete == True and page != 'target':
		images['target_img'] = check
	elif page == 'viewForm':
		images['target_img'] = check
	elif page == 'target':
		images['target_img'] = progress
	else:
		images['target_img'] = x

	if am.familyOriginComplete == True and page != 'family':
		images['family_img'] = check
	elif page == 'viewForm':
		images['family_img'] = check
	elif page == 'family':
		images['family_img'] = progress
	else:
		images['family_img'] = x

	if am.currentProblemsComplete == True and page != 'current':
		images['current_img'] = check
	elif page == 'viewForm':
		images['current_img'] = check
	elif page == 'current':
		images['current_img'] = progress
	else:
		images['current_img'] = x

	if am.controlComplete == True and page != 'control':
		images['control_img'] = check
	elif page == 'viewForm':
		images['control_img'] = check
	elif page == 'control':
		images['control_img'] = progress
	else:
		images['control_img'] = x

	if am.finalComplete == True and page != 'final':
		images['final_img'] = check
	elif page == 'viewForm':
		images['final_img'] = check
	elif page == 'final':
		images['final_img'] = progress
	else:
		images['final_img'] = x

	return images

def deprioritizeAM(am):
	am.demoPriority = False
	am.dhPriority = False
	am.childPriority = False
	am.ah1Priority = False
	am.ah2Priority = False
	am.ah3Priority = False
	am.connectPriority = False
	am.worstPriority = False
	am.targetPriority = False
	am.familyPriority = False
	am.currentPriority = False
	am.controlPriority = False
	am.finalPriority = False
	am.save()

def setAmPriorityURL(section, am):
	if str(section) == '/am_demographic/':
		am.demoPriority = True
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_drugHistory/':
		am.demoPriority = False
		am.dhPriority = True
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_childhood/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = True
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_angerHistory/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = True
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_angerHistory2/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = True
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_angerHistory3/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = True
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_connections/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = True
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_worst/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = True
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_angerTarget/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = True
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_familyOrigin/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = True
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_problems/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = True
		am.controlPriority = False
		am.finalPriority = False

	elif str(section) == '/am_control/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = True
		am.finalPriority = False

	elif str(section) == '/am_final/':
		am.demoPriority = False
		am.dhPriority = False
		am.childPriority = False
		am.ah1Priority = False
		am.ah2Priority = False
		am.ah3Priority = False
		am.connectPriority = False
		am.worstPriority = False
		am.targetPriority = False
		am.familyPriority = False
		am.currentPriority = False
		am.controlPriority = False
		am.finalPriority = True

def hasPriority_AM(am):
	hasPriority = False

	if am.demoPriority == True:
		hasPriority = True
	elif am.dhPriority == True:
		hasPriority = True
	elif am.childPriority == True:
		hasPriority = True
	elif am.ah1Priority == True:
		hasPriority = True
	elif am.ah2Priority == True:
		hasPriority = True
	elif am.ah3Priority == True:
		hasPriority = True
	elif am.connectPriority == True:
		hasPriority = True
	elif am.worstPriority == True:
		hasPriority = True
	elif am.targetPriority == True:
		hasPriority = True
	elif am.familyPriority == True:
		hasPriority = True
	elif am.currentPriority == True:
		hasPriority = True
	elif am.controlPriority == True:
		hasPriority = True
	elif am.finalPriority == True:
		hasPriority = True

	return hasPriority

def getAmPrioritySection(am):
	section = ''

	if am.demoPriority == True:
		section = '/am_demographic/'
	elif am.dhPriority == True:
		section = '/am_drugHistory/'
	elif am.childPriority == True:
		section = '/am_childhood/'
	elif am.ah1Priority == True:
		section = '/am_angerHistory/'
	elif am.ah2Priority == True:
		section = '/am_angerHistory2/'
	elif am.ah3Priority == True:
		section = '/am_angerHistory3/'
	elif am.connectPriority == True:
		section = '/am_connections/'
	elif am.worstPriority == True:
		section = '/am_worst/'
	elif am.targetPriority == True:
		section = '/am_angerTarget/'
	elif am.familyPriority == True:
		section = '/am_familyOrigin/'
	elif am.currentPriority == True:
		section = '/am_problems/'
	elif am.controlPriority == True:
		section = '/am_control/'
	elif am.finalPriority == True:
		section = '/am_final/'

	return section

def get_am_urls():
	result = []
	result.append('/am_demographic/')
	result.append('/am_drugHistory/')
	result.append('/am_childhood/')
	result.append('/am_angerHistory/')
	result.append('/am_angerHistory2/')
	result.append('/am_angerHistory3/')
	result.append('/am_connections/')
	result.append('/am_worst/')
	result.append('/am_angerTarget/')
	result.append('/am_familyOrigin/')
	result.append('/am_problems/')
	result.append('/am_control/')
	result.append('/am_final/')
	return result

def get_am_complete(am):
	result = []
	result.append(am.demographicComplete)
	result.append(am.drugHistoryComplete)
	result.append(am.childhoodComplete)
	result.append(am.angerHistoryComplete)
	result.append(am.angerHistoryComplete2)
	result.append(am.angerHistoryComplete3)
	result.append(am.connectionsComplete)
	result.append(am.worstComplete)
	result.append(am.angerTargetComplete)
	result.append(am.familyOriginComplete)
	result.append(am.currentProblemsComplete)
	result.append(am.controlComplete)
	result.append(am.finalComplete)
	return result

def get_am_priority(am):
	result = []
	result.append(am.demoPriority)
	result.append(am.dhPriority)
	result.append(am.childPriority)
	result.append(am.ah1Priority)
	result.append(am.ah2Priority)
	result.append(am.ah3Priority)
	result.append(am.connectPriority)
	result.append(am.worstPriority)
	result.append(am.targetPriority)
	result.append(am.familyPriority)
	result.append(am.currentPriority)
	result.append(am.controlPriority)
	result.append(am.finalPriority)
	return result

def get_am_parameters(am):
	result = []

	url = get_am_urls()
	complete = get_am_complete(am)
	priority = get_am_priority(am)

	for l in range(len(url)):
		data = {}
		data['url'] = url[l]
		data['complete'] = complete[l]
		data['priority'] = priority[l]
		result.append(data)
	return result

def forceNextAmPage(am):
	result 	= None
	flag 	= None
	am_list = get_am_parameters(am)

	for i in range(len(am_list)):
		if am_list[i]['complete'] == False:
			flag = i
			break

	for j in range(len(am_list)):
		if am_list[j]['complete'] == False and j != flag:
			result = am_list[j]['url']
			break

	return result

def nextAmPage(am, section):
	result = ''
	next_section = ''
	proceed = True
	no_result = False
	am_list = get_am_parameters(am)

	for a in am_list:
		if a['priority'] == True:
			result = a['url']
			proceed = False
			break

	if proceed == True:
		for i in range(len(am_list)):
			if am_list[i]['complete'] == False:
				next_section = am_list[i]['url']
				break

		if str(next_section) == str(section):
			result = forceNextAmPage(am)
		else:
			result = next_section

		count = 0
		for m in am_list:
			if m['complete'] == True:
				count = count + 1

		if count == len(am_list):
			result = '/am_viewForm/'

	return result

def matchAmProgressIndex(index):
	result = None

	if str(index) == '0':
		result = '/am_demographic/'
	elif str(index) == '1':
		result = '/am_drugHistory/'
	elif str(index) == '2':
		result = '/am_childhood/'
	elif str(index) == '3':
		result = '/am_angerHistory/'
	elif str(index) == '4':
		result = '/am_angerHistory2/'
	elif str(index) == '5':
		result = '/am_angerHistory3/'
	elif str(index) == '6':
		result = '/am_connections/'
	elif str(index) == '7':
		result = '/am_worst/'
	elif str(index) == '8':
		result = '/am_angerTarget/'
	elif str(index) == '9':
		result = '/am_familyOrigin/'
	elif str(index) == '10':
		result = '/am_problems/'
	elif str(index) == '11':
		result = '/am_control/'
	elif str(index) == '12':
		result = '/am_final/'
	else:
		result = '/am_viewForm/'

	return result

def grabAmCompletedSections(am):
	results = {}

	results['demographicComplete'] 		= am.demographicComplete
	results['drugHistoryComplete'] 		= am.drugHistoryComplete
	results['childhoodComplete'] 		= am.childhoodComplete
	results['angerHistoryComplete'] 	= am.angerHistoryComplete
	results['angerHistoryComplete2'] 	= am.angerHistoryComplete2
	results['angerHistoryComplete3'] 	= am.angerHistoryComplete3
	results['connectionsComplete'] 		= am.connectionsComplete
	results['worstComplete'] 			= am.worstComplete
	results['angerTargetComplete'] 		= am.angerTargetComplete
	results['familyOriginComplete'] 	= am.familyOriginComplete
	results['currentProblemsComplete'] 	= am.currentProblemsComplete
	results['controlComplete'] 			= am.controlComplete
	results['finalComplete'] 			= am.finalComplete

	return results

def sortedAmProgress(am):
	results = []
	progress = grabAmCompletedSections(am)

	results.append(progress['demographicComplete'])
	results.append(progress['drugHistoryComplete'])
	results.append(progress['childhoodComplete'])
	results.append(progress['angerHistoryComplete'])
	results.append(progress['angerHistoryComplete2'])
	results.append(progress['angerHistoryComplete3'])
	results.append(progress['connectionsComplete'])
	results.append(progress['worstComplete'])
	results.append(progress['angerTargetComplete'])
	results.append(progress['familyOriginComplete'])
	results.append(progress['currentProblemsComplete'])
	results.append(progress['controlComplete'])
	results.append(progress['finalComplete'])

	return results


def processCompletedClass(isComplete, isCompleteKeyWord, m_page, green, yellow, normal):
	result = None

	if isComplete == True and str(isCompleteKeyWord) != str(m_page):
		result = green
	elif str(isCompleteKeyWord) == str(m_page):
		result = yellow
	else:
		result = normal

	return result


def grabAmClassesCSS(am, m_page):
	classes = {}
	am = grabAmCompletedSections(am)
	normal = 'sideBarMargin'
	green = 'sideBarMarginChecked'
	current = 'sideLinkSelected'

	classes['AMdemo'] = processCompletedClass(am['demographicComplete'], '/am_demographic/', m_page, green, current, normal)
	classes['AMdh'] = processCompletedClass(am['drugHistoryComplete'], '/am_drugHistory/', m_page, green, current, normal)
	classes['AMchild'] = processCompletedClass(am['childhoodComplete'], '/am_childhood/', m_page, green, current, normal)
	classes['AMah1'] = processCompletedClass(am['angerHistoryComplete'], '/am_angerHistory/', m_page, green, current, normal)
	classes['AMah2'] = processCompletedClass(am['angerHistoryComplete2'], '/am_angerHistory2/', m_page, green, current, normal)
	classes['AMah3'] = processCompletedClass(am['angerHistoryComplete3'], '/am_angerHistory3/', m_page, green, current, normal)
	classes['AMconnect'] = processCompletedClass(am['connectionsComplete'], '/am_connections/', m_page, green, current, normal)
	classes['AMworst'] = processCompletedClass(am['worstComplete'], '/am_worst/', m_page, green, current, normal)
	classes['AMtarget'] = processCompletedClass(am['angerTargetComplete'], '/am_angerTarget/', m_page, green, current, normal)
	classes['AMfamily'] = processCompletedClass(am['familyOriginComplete'], '/am_familyOrigin/', m_page, green, current, normal)
	classes['AMcurrent'] = processCompletedClass(am['currentProblemsComplete'], '/am_problems/', m_page, green, current, normal)
	classes['AMcontrol'] = processCompletedClass(am['controlComplete'], '/am_control/', m_page, green, current, normal)
	classes['AMfinal'] = processCompletedClass(am['finalComplete'], '/am_final/', m_page, green, current, normal)

	return classes

def refreshAM(am):
	if am.demographicComplete == True:
		date = datetime.now()
		date = date.date()
		demo = AM_Demographic(client_id=am.client.clientID, date_of_assessment=date)
		demo.save()
		temp = am.demographic
		am.demographic = demo
		am.demographicComplete = False
		temp.delete()
		am.save()

	if am.drugHistoryComplete == True:
		am.drugHistory.delete()
		drugHistory = AM_DrugHistory(client_id=am.client.clientID, finishedTreatment=True)
		drugHistory.save()
		temp = am.drugHistory
		am.drugHistory = drugHistory
		am.drugHistoryComplete = False
		temp.delete()
		am.save()

	if am.childhoodComplete == True:
		am.childhood.delete()
		childhood = AM_ChildhoodHistory(client_id=am.client.clientID)
		childhood.save()
		temp = am.childhood
		am.childhood = childhood
		am.childhoodComplete = False
		temp.delete()
		am.save()

	if am.angerHistoryComplete == True:
		am.angerHistory.delete()
		angerHistory = AM_AngerHistory(client_id=am.client.clientID)
		angerHistory.save()
		temp = am.angerHistory
		am.angerHistory = angerHistory
		am.angerHistoryComplete = False
		temp.delete()
		am.save()

	if am.angerHistoryComplete2 == True:
		am.angerHistory2.delete()
		angerHistory2 = AM_AngerHistory2(client_id=am.client.clientID)
		angerHistory2.save()
		temp = am.angerHistory2
		am.angerHistory2 = angerHistory2
		am.angerHistoryComplete2 = False
		temp.delete()
		am.save()

	if am.angerHistoryComplete3 == True:
		am.angerHistory3.delete()
		angerHistory3 = AM_AngerHistory3(client_id=am.client.clientID)
		angerHistory3.save()
		temp = am.angerHistory3
		am.angerHistory3 = angerHistory3
		am.angerHistoryComplete3 = False
		temp.delete()
		am.save()

	if am.connectionsComplete == True:
		am.connections.delete()
		connections = AM_Connections(client_id=am.client.clientID)
		connections.save()
		temp = am.connections
		am.connections = connections
		am.connectionsComplete = False
		temp.delete()
		am.save()

	if am.worstComplete == True:
		am.worstEpisode.delete()
		worstEpisode = AM_WorstEpisode(client_id=am.client.clientID)
		worstEpisode.save()
		temp = am.worstEpisode
		am.worstEpisode = worstEpisode
		am.worstComplete = False
		temp.delete()
		am.save()

	if am.angerTargetComplete == True:
		am.angerTarget.delete()
		angerTarget = AM_AngerTarget(client_id=am.client.clientID)
		angerTarget.save()
		temp = am.angerTarget
		am.angerTarget = angerTarget
		am.angerTargetComplete = False
		temp.delete()
		am.save()

	if am.familyOriginComplete == True:
		am.familyOrigin.delete()
		familyOrigin = AM_FamilyOrigin(client_id=am.client.clientID)
		familyOrigin.save()
		temp = am.familyOrigin
		am.familyOrigin = familyOrigin
		am.familyOriginComplete = False
		temp.delete()
		am.save()

	if am.currentProblemsComplete == True:
		am.currentProblems.delete()
		currentProblems = AM_CurrentProblem(client_id=am.client.clientID)
		currentProblems.save()
		temp = am.currentProblems
		am.currentProblems = currentProblems
		am.currentProblemsComplete = False
		temp.delete()
		am.save()

	if am.controlComplete == True:
		am.control.delete()
		control = AM_Control(client_id=am.client.clientID)
		control.save()
		temp = am.control
		am.control = control
		am.controlComplete = False
		temp.delete()
		am.save()

	if am.finalComplete == True:
		am.final.delete()
		final = AM_Final(client_id=am.client.clientID)
		final.save()
		temp = am.final
		am.final = final
		am.finalComplete = False
		temp.delete()
		am.save()

	return am

def blankMustDie(element):
	result = None
	if element == None or element == '':
		result = 'N/A'
	else:
		result = element
	return result

def grabAmDhFields(am):
	result = {}
	result['firstDrinkAge'] = am.drugHistory.firstDrinkAge
	result['firstDrinkType'] = am.drugHistory.firstDrinkType
	result['curUse'] = am.drugHistory.curUse
	result['useType'] = am.drugHistory.useType
	result['amtPerWeek'] = am.drugHistory.amtPerWeek
	result['useAmt'] = am.drugHistory.useAmt
	result['everDrank'] = am.drugHistory.everDrank
	result['monthsQuit'] = am.drugHistory.monthsQuit
	result['yearsQuit'] = am.drugHistory.yearsQuit
	result['reasonQuit'] = am.drugHistory.reasonQuit
	result['DUI'] = am.drugHistory.DUI
	result['numDUI'] = am.drugHistory.numDUI
	result['BALevel'] = am.drugHistory.BALevel
	result['drugTreatment'] = am.drugHistory.drugTreatment
	result['treatmentPlace'] = am.drugHistory.treatmentPlace
	result['dateTreated'] = am.drugHistory.dateTreated
	result['finishedTreatment'] = am.drugHistory.finishedTreatment
	result['reasonNotFinishedTreatment'] = am.drugHistory.reasonNotFinishedTreatment
	result['isClean'] = am.drugHistory.isClean
	result['relapseTrigger'] = am.drugHistory.relapseTrigger
	result['drinkLastEpisode'] = am.drugHistory.drinkLastEpisode
	result['drinkRelationshipProblem'] = am.drugHistory.drinkRelationshipProblem
	result['needHelpDrugs'] = am.drugHistory.needHelpDrugs

	if result['curUse'] == True:
		result['everDrank'] = False

	return result

def truePythonBool(value):
	result = False

	if value == 'True':
		result = True

	return result

def processAmDhFields(fields):
	results = {}

	if fields['curUse'] == True:
		results['']

	return results

def grabAmConnections(am):
	fields = {}

	fields['angerWorse'] = am.connections.angerWorse
	fields['troubleWhenUsing'] = am.connections.troubleWhenUsing
	fields['lessAngry'] = am.connections.lessAngry
	fields['othersTellMe'] = am.connections.othersTellMe
	fields['noConnection'] = am.connections.noConnection
	fields['otherConnectionsUsing'] = am.connections.otherConnectionsUsing
	fields['connectionExplain'] = am.connections.connectionExplain
	return fields

def grabAmControl(am):
	fields = {}
	fields['neverAttemptedControl'] = am.control.neverAttemptedControl
	fields['talkToMyself'] = am.control.talkToMyself
	fields['whatSayYou'] = am.control.whatSayYou
	fields['leaveScene'] = am.control.leaveScene
	fields['howLongLeaveScene'] = am.control.howLongLeaveScene
	fields['whatDoLeave'] = am.control.whatDoLeave
	fields['relax'] = am.control.relax
	fields['howRelax'] = am.control.howRelax
	fields['selfHelpGroup'] = am.control.selfHelpGroup
	fields['otherControlAnger'] = am.control.otherControlAnger
	fields['doWhatOtherControl'] = am.control.doWhatOtherControl
	return fields

def grabAmCurrentProblems(am):
	fields = {}
	fields['brainInjury'] = am.currentProblems.brainInjury
	fields['stroke'] = am.currentProblems.stroke
	fields['epilepsy'] = am.currentProblems.epilepsy
	fields['attentionDD'] = am.currentProblems.attentionDD
	fields['pms'] = am.currentProblems.pms
	fields['depression'] = am.currentProblems.depression
	fields['ptsd'] = am.currentProblems.ptsd
	fields['otherSeriousIllness'] = am.currentProblems.otherSeriousIllness
	fields['currentlyOnMeds'] = am.currentProblems.currentlyOnMeds
	fields['whichMeds'] = am.currentProblems.whichMeds
	fields['describeIssue'] = am.currentProblems.describeIssue
	return fields

def grabAmFamilyOrigin(am):
	fields = {}
	fields['kidMomAnger'] = am.familyOrigin.kidMomAnger
	fields['kidDadAnger'] = am.familyOrigin.kidDadAnger
	fields['kidSiblingAnger'] = am.familyOrigin.kidSiblingAnger
	fields['kidOtherAnger'] = am.familyOrigin.kidOtherAnger
	fields['learnFamilyAnger'] = am.familyOrigin.learnFamilyAnger
	fields['suicideHistory'] = am.familyOrigin.suicideHistory
	fields['hasLovingMother'] = am.familyOrigin.hasLovingMother
	fields['hasLovingSiblings'] = am.familyOrigin.hasLovingSiblings
	return fields

def grabAmWorstEpisodes(am):
	fields = {}

	selectBtn = am.worstEpisode.whoDidItFight
	index = None

	if selectBtn == None:
		index = 0
	else:
		if str(selectBtn) == 'Client Used':
			index = 1
		elif str(selectBtn) == 'The Other Party Used':
			index = 2
		elif str(selectBtn) == 'Everyone Involved':
			index = 3
		else:
			index = 0

	fields['whoWorst'] = am.worstEpisode.whoWorst
	fields['happenedWorst'] = am.worstEpisode.happenedWorst
	fields['wordThoughtWorst'] = am.worstEpisode.wordThoughtWorst
	fields['howStartWorst'] = am.worstEpisode.howStartWorst
	fields['howEndWorst'] = am.worstEpisode.howEndWorst
	fields['useWorst'] = am.worstEpisode.useWorst
	fields['whoDidItFight'] = index
	fields['theyUsedWorst'] = am.worstEpisode.theyUsedWorst
	fields['physicalWorst'] = am.worstEpisode.physicalWorst
	fields['verbalWorst'] = am.worstEpisode.verbalWorst
	fields['threatsWorst'] = am.worstEpisode.threatsWorst
	fields['propertyWorst'] = am.worstEpisode.propertyWorst
	fields['otherWorst'] = am.worstEpisode.otherWorst
	fields['otherWorstDescription'] = am.worstEpisode.otherWorstDescription
	return fields

def grabAmTarget(am):
	fields = {}
	fields['angryPartner'] = am.angerTarget.angryPartner
	fields['angryParents'] = am.angerTarget.angryParents
	fields['angryChildren'] = am.angerTarget.angryChildren
	fields['angryRelatives'] = am.angerTarget.angryRelatives
	fields['angryEmployer'] = am.angerTarget.angryEmployer
	fields['angryFriends'] = am.angerTarget.angryFriends
	fields['angryOther'] = am.angerTarget.angryOther
	fields['otherWhom'] = am.angerTarget.otherWhom
	fields['angryAbout'] = am.angerTarget.angryAbout
	fields['seldomUpset'] = am.angerTarget.seldomUpset
	return fields

def getAMDemoFields(am):
	data = {}
	phone = None

	data['maritalStatus'] = convertMaritalToIndex(am.demographic.maritalStatus)
	data['livingSituation'] = convertLivingToIndex(am.demographic.livingSituation)
	data['livingSituation'] = convertLivingToIndex(am.demographic.livingSituation)

	if am.demographic.employer_phone == None or am.demographic.employer_phone == '' or am.demographic.employer_phone == 'None':
		phone = am.demographic.employer_phone
	else:
		phone = convert_phone(am.demographic.employer_phone)

	data['own'] = convertToJavascriptBool(am.demographic.own)
	data['months_res'] = am.demographic.months_res
	data['years_res'] = am.demographic.years_res
	data['num_children'] = am.demographic.num_children
	data['other_dependants'] = am.demographic.other_dependants
	data['drop_out'] = convertToJavascriptBool(am.demographic.drop_out)
	data['resasonDO'] = convertNullTextFields(am.demographic.resasonDO)
	data['employee'] = convertNullTextFields(am.demographic.employee)
	data['job_title'] = convertNullTextFields(am.demographic.job_title)
	data['emp_address'] = convertNullTextFields(am.demographic.emp_address)
	data['employed_months'] = am.demographic.employed_months
	data['employed_years'] = am.demographic.employed_years
	data['employer_phone'] = phone
	data['health_problem'] = convertToJavascriptBool(am.demographic.health_problem)
	data['medication'] = convertToJavascriptBool(am.demographic.medication)
	data['whatMedicine'] = convertNullTextFields(am.demographic.whatMedicine)
	data['health_exp'] = convertNullTextFields(am.demographic.health_exp)

	return data

def grabAmChildhood(am):
	fields = {}

	#CONVERT DROP MENU ITEM
	select = convertNullTextFields(am.childhood.raisedBy)

	if select == 'Parents':
		select = 1
	elif select == 'Grandparents':
		select = 2
	elif select == 'Relatives':
		select = 3
	elif select == 'Foster Care':
		select = 4
	else:
		select = 0

	fields['raisedBy'] = select

	#TEXT FIELDS
	fields['traumaExplain'] = convertNullTextFields(am.childhood.traumaExplain)
	fields['howLeftHome'] = convertNullTextFields(am.childhood.howLeftHome)
	fields['siblingsRelationshipExplain'] = convertNullTextFields(am.childhood.siblingsRelationshipExplain)
	fields['dadCloseExplain'] = convertNullTextFields(am.childhood.dadCloseExplain)
	fields['momCloseExplain'] = convertNullTextFields(am.childhood.momCloseExplain)
	fields['abusedBy'] = convertNullTextFields(am.childhood.abusedBy)
	fields['abuseImpact'] = convertNullTextFields(am.childhood.abuseImpact)
	fields['childAngerExplain'] = convertNullTextFields(am.childhood.childAngerExplain)
	fields['otherChildExplain'] = convertNullTextFields(am.childhood.otherChildExplain)
	fields['parentViolenceExplain'] = convertNullTextFields(am.childhood.parentViolenceExplain)
	fields['parentViolenceImpact'] = convertNullTextFields(am.childhood.parentViolenceImpact)


	#INTEGER FIELDS...NOTHING NEEDS TO BE DONE BECAUSE DEFAULT VALUES ARE SET AT ZERO
	fields['num_siblings'] = am.childhood.num_siblings

	#BOOLEAN FIELDS
	fields['momAlive'] = convertToJavascriptBool(am.childhood.momAlive)
	fields['dadAlive'] = convertToJavascriptBool(am.childhood.dadAlive)
	fields['childTrama'] = convertToJavascriptBool(am.childhood.childTrama)
	fields['siblingsClose'] = convertToJavascriptBool(am.childhood.siblingsClose)
	fields['dadClose'] = convertToJavascriptBool(am.childhood.dadClose)
	fields['momClose'] = convertToJavascriptBool(am.childhood.momClose)
	fields['wasAbused'] = convertToJavascriptBool(am.childhood.wasAbused)
	fields['childAnger'] = convertToJavascriptBool(am.childhood.childAnger)
	fields['otherChild'] = convertToJavascriptBool(am.childhood.otherChild)
	fields['parentViolence'] = convertToJavascriptBool(am.childhood.parentViolence)

	return fields

def grabAmAngerHistory1(am):
	fields = {}

	fields['recentIncidentV'] = am.angerHistory.recentIncidentV
	fields['recentVDate'] = am.angerHistory.recentVDate
	fields['recentVlocation'] = am.angerHistory.recentVlocation
	fields['withWhomRecentV'] = am.angerHistory.withWhomRecentV
	fields['happenedRecentV'] = am.angerHistory.happenedRecentV
	fields['physicalRecentV'] = am.angerHistory.physicalRecentV
	fields['verbalRecentV'] = am.angerHistory.verbalRecentV
	fields['threatsRecentV'] = am.angerHistory.threatsRecentV
	fields['propertyRecentV'] = am.angerHistory.propertyRecentV
	fields['otherRecentV'] = am.angerHistory.otherRecentV
	fields['otherExplainRecentV'] = am.angerHistory.otherExplainRecentV
	fields['typeWordsRecentV'] = am.angerHistory.typeWordsRecentV
	fields['wasTense'] = am.angerHistory.wasTense
	fields['hadRush'] = am.angerHistory.hadRush
	fields['feltStrong'] = am.angerHistory.feltStrong
	fields['psychoRecentV'] = am.angerHistory.psychoRecentV
	fields['psychoWhyRecentV'] = am.angerHistory.psychoWhyRecentV
	fields['longAgoTreatRecentVmos'] = am.angerHistory.longAgoTreatRecentVmos
	fields['longAgoTreatRecentVyrs'] = am.angerHistory.longAgoTreatRecentVyrs
	fields['didCompleteTreatRecentV'] = am.angerHistory.didCompleteTreatRecentV
	fields['reasonNotCompleteRecentV'] = am.angerHistory.reasonNotCompleteRecentV

	return fields

def grabAmAngerHistory2(am):
	fields = {}
	fields['depress30RecentV'] = am.angerHistory2.depress30RecentV
	fields['depress30ExplainRecentV'] = am.angerHistory2.depress30ExplainRecentV
	fields['anxietyRecentV'] = am.angerHistory2.anxietyRecentV
	fields['anxietyExplainRecentV'] = am.angerHistory2.anxietyExplainRecentV
	fields['hallucinationRecentV'] = am.angerHistory2.hallucinationRecentV
	fields['hallucinationLastV'] = am.angerHistory2.hallucinationLastV
	fields['understandingRecentV'] = am.angerHistory2.understandingRecentV
	fields['understandingExplainRecentV'] = am.angerHistory2.understandingExplainRecentV
	fields['troubleControlRecentV'] = am.angerHistory2.troubleControlRecentV
	fields['lastTimeTroubleControl'] = am.angerHistory2.lastTimeTroubleControl
	fields['controlTrigger'] = am.angerHistory2.controlTrigger
	fields['suicide30RecentV'] = am.angerHistory2.suicide30RecentV
	fields['suicide30ExplainRecentV'] = am.angerHistory2.suicide30ExplainRecentV
	fields['suicideTodayRecentV'] = am.angerHistory2.suicideTodayRecentV
	fields['suicideTodayPlanRecentV'] = am.angerHistory2.suicideTodayPlanRecentV
	fields['suicideTodayExplainRecentV'] = am.angerHistory2.suicideTodayExplainRecentV
	fields['hasAttemptedSuicide'] = am.angerHistory2.hasAttemptedSuicide
	fields['hasAttemptedExplainRecentV'] = am.angerHistory2.hasAttemptedExplainRecentV
	return fields

def grabAmAngerHistory3(am):
	fields = {}

	fields['homicidal'] = am.angerHistory3.homicidal
	fields['homicidalExplain'] = am.angerHistory3.homicidalExplain
	fields['medRecentV'] = am.angerHistory3.medRecentV
	fields['medRecentVExplain'] = am.angerHistory3.medRecentVExplain
	fields['medSuccessRecentV'] = am.angerHistory3.medSuccessRecentV
	fields['medSuccessExplainRecentV'] = am.angerHistory3.medSuccessExplainRecentV
	fields['durationRecentV'] = am.angerHistory3.durationRecentV
	fields['intensityRecentV'] = am.angerHistory3.intensityRecentV
	fields['howOften'] = am.angerHistory3.howOften

	return fields

def grabAmFinal(am):
	fields = {}

	fields['anythingelse'] = am.final.anythingelse
	fields['changeLearn1'] = am.final.changeLearn1
	fields['changeLearn2'] = am.final.changeLearn2
	fields['changeLearn3'] = am.final.changeLearn3
	fields['whoLivesWithClient'] = am.demographic.whoLivesWithClient

	return fields

def getAMFields(am, location):
	location = str(location)
	fields = None

	if location == '/am_demographic/':
		fields = getAMDemoFields(am)
	elif location == '/am_drugHistory/':
		fields = grabAmDhFields(am)
	elif location == '/am_childhood/':
		fields = grabAmChildhood(am)
	elif location == '/am_angerHistory/':
		fields = grabAmAngerHistory1(am)
	elif location == '/am_angerHistory2/':
		fields = grabAmAngerHistory2(am)
	elif location == '/am_angerHistory3/':
		fields = grabAmAngerHistory3(am)
	elif location == '/am_angerTarget/':
		fields = grabAmTarget(am)
	elif location == '/am_connections/':
		fields = grabAmConnections(am)
	elif location == '/am_control/':
		fields = grabAmControl(am)
	elif location == '/am_problems/':
		fields = grabAmCurrentProblems(am)
	elif location == '/am_familyOrigin/':
		fields = grabAmFamilyOrigin(am)
	elif location == '/am_worst/':
		fields = grabAmWorstEpisodes(am)
	elif location == '/am_final/':
		fields = grabAmFinal(am)

	return fields


def getDuplicateAM(client):
	amList = AngerManagement.objects.all()
	results = []

	for a in amList:
		if str(a.client.clientID) == str(client.clientID) and a.AMComplete == False:
			results.append(a)

	return results

def cleanAmDatabase(client):
	cleaning = getDuplicateAM(client)
	deleted = []

	if len(cleaning) > 0:
		for clean in cleaning:
			deleted.append(clean)
			deleteAM(clean)

	return deleted

def hasAM(client):
	amList = AngerManagement.objects.all()
	exist = False

	for a in amList:
		if (str(client.clientID) == str(a.client.clientID)) and (str(client.fname) == str(a.client.fname)) and (str(client.dob) == str(a.client.dob)):
			exist = True
			break

	return exist


# def startAM(client):
# 	results = {}
# 	create_new = True
# 	am = None

# 	if hasAM(client) == True:
# 		amList = AngerManagement.objects.all()

# 		for a in amList:
# 			if (a.AMComplete == False) and (str(a.client.clientID) == str(client.clientID)):
# 				create_new = False
# 				am = a
# 				break

# 	if create_new == True:
# 		am = newAM(client)

# 	results['am'] = am
# 	results['isNew'] = create_new

# 	return results

def grabAmSideBarString(location):
	m_page = None

	if location == 'counselor/forms/AngerManagement/demographic.html':
		m_page = 'demo'
	elif location == 'counselor/forms/AngerManagement/drugHistory.html':
		m_page = 'dh'
	elif location == 'counselor/forms/AngerManagement/childhoodHistory.html':
		m_page = 'child'
	elif location == 'counselor/forms/AngerManagement/connections.html':
		m_page = 'connect'
	elif location == 'counselor/forms/AngerManagement/worstEpisodes.html':
		m_page = 'worst'
	elif location == 'counselor/forms/AngerManagement/AngerTarget.html':
		m_page = 'target'
	elif location == 'counselor/forms/AngerManagement/familyOrigin.html':
		m_page = 'family'
	elif location == 'counselor/forms/AngerManagement/currentProblems.html':
		m_page = 'current'
	elif location == 'counselor/forms/AngerManagement/control.html':
		m_page = 'control'
	elif location == 'counselor/forms/AngerManagement/final.html':
		m_page = 'final'
	elif location == 'counselor/forms/AngerManagement/angerHistory.html':
		m_page = 'ah1'
	elif location == 'counselor/forms/AngerManagement/angerHistory2.html':
		m_page = 'ah2'
	elif location == 'counselor/forms/AngerManagement/angerHistory3.html':
		m_page = 'ah3'

	return m_page



def getActiveClients():
	clients = Client.objects.all()
	results = []

	for c in clients:
		if c.isDischarged == False:
			results.append(c)
	return results

def getDischargedClients():
	clients = Client.objects.all()
	result = []

	for c in clients:
		if c.isDischarged == True:
			result.append(c)
	return result

def utExist(ut):
	uts = UrineResults.objects.all()
	exist = False

	for u in uts:
		if str(u.client.clientID) == str(ut.client.clientID) and str(u.client.fname) == str(ut.client.fname) and str(u.testDate) == str(ut.testDate):
			exist = True
			break
	return exist

def getUtsByDate(ut):
	uts = UrineResults.objects.all()
	results = []

	for u in uts:
		if u.client == ut.client and u.testDate == ut.testDate:
			results.append(u)
	return results

def deleteOldUTS(date):
	uts = UrineResults.objects.all()
	deleted = []
	num_test = len(uts)

	for u in uts:
		if str(u.testDate) == str(date):
			deleted.append(u)
			u.delete()
	return deleted

def getTimes():
	results = []
	real = []
	final = []
	time = 7
	count = 0

	for i in range(56):
		if time == 13:
			time = 1

		results.append(time)
		count = count + 1

		if count == 4:
			time = time + 1
			count = 0

	count = 0
	for r in results:
		if count == 0:
			real.append(str(r) + ':00')
		elif count == 1:
			real.append(str(r) + ':15')
		elif count == 2:
			real.append(str(r) + ':30')
		else:
			real.append(str(r) + ':45')

		count = count + 1			
		if count == 4:
			count = 0

	for i in range(len(real)):
		if i < 20:
			final.append(str(real[i]) + ' am')
		else:
			final.append(str(real[i]) + ' pm')

	return final

def assign_married_index():
	the_list = MaritalStatus.objects.all().order_by('status')
	results = []
	count = 1

	for t in the_list:
		data = {}
		data['index'] = count
		data['status'] = t.id
		results.append(data)
		count = count + 1
	return results

def married_index(married_value):
	indices = assign_married_index()
	result = None

	for i in indices:
		if str(i['status']) == str(married_value):
			result = i['index']
			break
	return result

def assign_living_index():
	the_list = LivingSituation.objects.all().order_by('situation')
	results = []
	count = 1

	for t in the_list:
		data = {}
		data['index'] = count
		data['status'] = t.id
		results.append(data)
		count = count + 1
	return results

def living_index(living_value):
	indices = assign_living_index()
	result = None

	for i in indices:
		if str(i['status']) == str(living_value):
			result = i['index']
			break
	return result

def assign_education_index():
	the_list = EducationLevel.objects.all().order_by('level')
	results = []
	count = 1

	for t in the_list:
		data = {}
		data['index'] = count
		data['status'] = t.id
		results.append(data)
		count = count + 1
	return results

def education_index(education_value):
	indices = assign_education_index()
	result = None

	for i in indices:
		if str(i['status']) == str(education_value):
			result = i['index']
			break
	return result

def convertToJavascriptBool(data):
	if data == True:
		data = 'true'
	elif data == False:
		data = 'false'
	return data

def convertToPythonBool(data):
	if data == 'True':
		data = True
	elif data == 'False':
		data = False
	return data

def convertNullTextFields(field):
	if field == None or field == '':
		field = 'NA'
	return field

def convertMaritalToIndex(marital):
	if marital == 'Divorced':
		marital = 1
	elif marital == 'Married':
		marital = 2
	elif marital == 'Separated':
		marital = 3
	elif marital == 'Single':
		marital = 4
	else:
		marital = 0
	return marital

def convertLivingToIndex(living):
	if living == 'Live alone':
		living = 1
	elif living == 'Live with family':
		living = 2
	elif living == 'Live with friend':
		living = 3
	elif living == 'Live with partner':
		living = 4
	else:
		living = 0
	return living

def convertEducationToIndex(education):
	if education == 'College Degree':
		education = 1
	elif education == 'Dropout':
		education = 2
	elif education == 'GED':
		education = 3
	elif education == 'HS Diploma':
		education = 4
	elif education == 'Some College':
		education = 5
	else:
		education = 0
	return education


def getAmDHData(back, am):
	data = {}

	if back == False:
		data['firstDrinkAge'] = '0'
		data['firstDrinkType'] = ''
		data['curUse'] = False
		data['useType'] = ''
		data['amtPerWeek'] = ''
		data['useAmt'] = ''
		data['everDrank'] = False
		data['monthsQuit'] = '0'
		data['yearsQuit'] = '0'
		data['reasonQuit'] = ''
		data['DUI'] = False
		data['numDUI'] = '0'
		data['BALevel'] = ''
		data['drugTreatment'] = False
		data['treatmentPlace'] = ''
		data['dateTreated'] = ''
		data['finishedTreatment'] = True
		data['reasonNotFinishedTreatment'] = ''
		data['isClean'] = True
		data['relapseTrigger'] = ''
		data['drinkLastEpisode'] = False
		data['drinkRelationshipProblem'] = False
		data['needHelpDrugs'] = False

	else:
		data['firstDrinkAge'] = am.drugHistory.firstDrinkAge
		data['firstDrinkType'] = am.drugHistory.firstDrinkType
		data['curUse'] = am.drugHistory.curUse
		data['useType'] = am.drugHistory.useType
		data['amtPerWeek'] = am.drugHistory.amtPerWeek
		data['useAmt'] = am.drugHistory.useAmt
		data['everDrank'] = am.drugHistory.everDrank
		data['monthsQuit'] = am.drugHistory.monthsQuit
		data['yearsQuit'] = am.drugHistory.yearsQuit
		data['reasonQuit'] = am.drugHistory.reasonQuit
		data['DUI'] = am.drugHistory.DUI
		data['numDUI'] = am.drugHistory.numDUI
		data['BALevel'] = am.drugHistory.BALevel
		data['drugTreatment'] = am.drugHistory.drugTreatment
		data['treatmentPlace'] = am.drugHistory.treatmentPlace
		data['dateTreated'] = am.drugHistory.dateTreated
		data['finishedTreatment'] = am.drugHistory.finishedTreatment
		data['reasonNotFinishedTreatment'] = am.drugHistory.reasonNotFinishedTreatment
		data['isClean'] = am.drugHistory.isClean
		data['relapseTrigger'] = am.drugHistory.relapseTrigger
		data['drinkLastEpisode'] = am.drugHistory.drinkLastEpisode
		data['drinkRelationshipProblem'] = am.drugHistory.drinkRelationshipProblem
		data['needHelpDrugs'] = am.drugHistory.needHelpDrugs

	return data

def amDhExist(drug_history):
	exist = False
	dhs = AM_DrugHistory.objects.all()
	testList = True

	if len(dhs) == 0:
		testList = False

	if testList == True:
		for d in dhs:
			if str(drug_history.id) == str(d.id):
				exist = True
				break
	return exist

def setAmSectionComplete(am, section):
	section = str(section)
	print "Current section to complete: " + str(section)

	if section == '/am_demographic/':
		am.demographicComplete = True
	elif section == '/am_drugHistory/':
		am.drugHistoryComplete = True
	elif section == '/am_childhood/':
		am.childhoodComplete = True
	elif section == '/am_angerHistory/':
		am.angerHistoryComplete = True
	elif section == '/am_angerHistory2/':
		am.angerHistoryComplete2 = True
	elif section == '/am_angerHistory3/':
		am.angerHistoryComplete3 = True
	elif section == '/am_connections/':
		am.connectionsComplete = True
	elif section == '/am_worst/':
		am.worstComplete = True
	elif section == '/am_angerTarget/':
		am.angerTargetComplete = True
	elif section == '/am_familyOrigin/':
		am.familyOriginComplete = True
	elif section == '/am_problems/':
		am.currentProblemsComplete = True
	elif section == '/am_control/':
		am.controlComplete = True
	elif section == '/am_final/':
		am.finalComplete = True

	am.save()

def hasIncompleteAM(client):
	exist = False
	ams = AngerManagement.objects.all()

	for a in ams:
		if a.client == client and a.AMComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientAM(client):
	ams = AngerManagement.objects.all()
	result = None

	for a in ams:
		if a.client == client and a.AMComplete == False:
			result = a
			break
	return result

def startAM(client):
	result = {}

	if hasIncompleteAM(client) == False:
		result['isNew'] = True
		result['am'] = newAM(client)

	else:
		result['isNew'] = False
		result['am'] = findIncompleteClientAM(client)

	return result


def beginAM(request):
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	client = Client.objects.get(id=client_id)
	session = ClientSession.objects.get(id=session_id)

	action = startAM(client)
	am = action['am']
	setGlobalID(am.id)

	openForm('am', am, client)

	result['AM'] = am
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | Anger Management"
	result['save_this'] = 'false'

	if action['isNew'] == False:
		next_section = nextAmPage(am, None)
		result['form'] = am
		result['form_type'] = 'am'
		result['type_header'] = 'Anger Management'
		result['next_section'] = next_section
		result['save_section'] = next_section

	return result

def processAMData(request, current_section):
	result = {}

	session_id = request.POST.get('session_id', '')
	am_id = request.POST.get('am_id', '')
	save_this = request.POST.get('save_this', '')
	section = request.POST.get('save_section', '')

	session = ClientSession.objects.get(id=session_id)
	am = AngerManagement.objects.get(id=am_id)
	deprioritizeAM(am)
	fields = getAMFields(am, current_section)
	json_data = json.dumps(fields)

	if save_this == 'true':
		saveCompletedAmSection(request, section, am)
		setAmSectionComplete(am, section)

	next_url = nextAmPage(am, current_section)
	classes = grabAmClassesCSS(am, current_section)
	image = amSidebarImages(am, current_section)

	result['class'] = classes
	result['image'] = image
	result['next_url'] = next_url
	result['session'] = session
	result['AM'] = am
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | Anger Management"

	return result

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
################################################################# END AM ##################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#




###########################################################################################################################################
#*****************************************************************************************************************************************#
#----------------------------------------------------------------  S.A.P -----------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################

def sapExist(client):
	exist = False
	filter_form = True
	saps = SAP.objects.all()

	if len(saps) == 0:
		filter_form = False

	if filter_form == True:
		for s in saps:
			if (str(s.client.clientID) == str(client.clientID)) and (str(s.client.id) == str(client.id)) and (s.SapComplete == False):
				exist = True
				break
	return exist

def grabIncompleteSap(client):
	result = None
	saps = SAP.objects.all()

	for s in saps:
		if (str(s.client.clientID) == str(client.clientID)) and (str(s.client.id) == str(client.id)) and (s.SapComplete == False):
			result = s
			break
	return result

def newSap(the_client):
	date = datetime.now()
	date = date.date()
	sap = None

	demo = SapDemographics(clientID=the_client.clientID)
	psycho = SapPsychoactive(clientID=the_client.clientID)

	demo.save()
	psycho.save()

	sap = SAP(client=the_client, date_of_assessment=date)
	sap.demographics = demo
	sap.psychoactive = psycho
	sap.save()

	return sap

def getSAP(client):
	results = {}
	saps = SAP.objects.all()
	filter_list = sapExist(client)

	if len(saps) == 0 or filter_list == False:
		results['isNew'] = True
		results['sap'] = newSap(client)

	else:
		results['isNew'] = False
		results['sap'] = grabIncompleteSap(client)

	return results


def getSapProgress(sap):
	result = {}
	completed = 0
	sap_list = getCompletedSapOrdered(sap)
	result['total'] = len(sap_list)

	for s in sap_list:
		if s == True:
			completed = completed + 1

	result['completed'] = completed
	return result

def deprioritizeSAP(sap):
	sap.clinicPriority 	= False
	sap.socialPriority 	= False
	sap.psycho1Priority = False
	sap.psycho2Priority = False
	sap.spacialPriority = False
	sap.otherPriority 	= False
	sap.sourcesPriority = False
	sap.save()

def prioritySapSection(section, sap):
	if str(section) == '/sap_demographic/':
		sap.clinicPriority 	= True
		sap.socialPriority 	= False
		sap.psycho1Priority = False
		sap.psycho2Priority = False
		sap.spacialPriority = False
		sap.otherPriority 	= False
		sap.sourcesPriority = False

	elif str(section) == '/sap_social/':
		sap.clinicPriority 	= False
		sap.socialPriority 	= True
		sap.psycho1Priority = False
		sap.psycho2Priority = False
		sap.spacialPriority = False
		sap.otherPriority 	= False
		sap.sourcesPriority = False

	elif str(section) == '/sap_psychoactive/':
		sap.clinicPriority 	= False
		sap.socialPriority 	= False
		sap.psycho1Priority = True
		sap.psycho2Priority = False
		sap.spacialPriority = False
		sap.otherPriority 	= False
		sap.sourcesPriority = False

	elif str(section) == '/sap_psychoactive2/':
		sap.clinicPriority 	= False
		sap.socialPriority 	= False
		sap.psycho1Priority = False
		sap.psycho2Priority = True
		sap.spacialPriority = False
		sap.otherPriority 	= False
		sap.sourcesPriority = False
	
	elif str(section) == '/sap_special/':
		sap.clinicPriority 	= False
		sap.socialPriority 	= False
		sap.psycho1Priority = False
		sap.psycho2Priority = False
		sap.spacialPriority = True
		sap.otherPriority 	= False
		sap.sourcesPriority = False

	elif str(section) == '/sap_other/':
		sap.clinicPriority 	= False
		sap.socialPriority 	= False
		sap.psycho1Priority = False
		sap.psycho2Priority = False
		sap.spacialPriority = False
		sap.otherPriority 	= True
		sap.sourcesPriority = False

	elif str(section) == '/sap_sources/':
		sap.clinicPriority 	= False
		sap.socialPriority 	= False
		sap.psycho1Priority = False
		sap.psycho2Priority = False
		sap.spacialPriority = False
		sap.otherPriority 	= False
		sap.sourcesPriority = True
	sap.save()

def grabSapCompletedSections(sap):
	results = {}

	results['clinicalComplete'] 	= sap.clinicalComplete
	results['socialComplete'] 		= sap.socialComplete
	results['psychoComplete'] 		= sap.psychoComplete
	results['psycho2Complete'] 		= sap.psycho2Complete
	results['specialComplete'] 		= sap.specialComplete
	results['otherComplete'] 		= sap.otherComplete
	results['sourcesComplete'] 		= sap.sourcesComplete

	return results

def getCompletedSapOrdered(sap):
	s_list = []
	sections = grabSapCompletedSections(sap)

	s_list.append(sections['clinicalComplete'])
	s_list.append(sections['socialComplete'])
	s_list.append(sections['psychoComplete'])
	s_list.append(sections['psycho2Complete'])
	s_list.append(sections['specialComplete'])
	s_list.append(sections['otherComplete'])
	s_list.append(sections['sourcesComplete'])

	return s_list

def isDuplicateSapURL(current, next):
	duplicate = False

	if str(current) == str(next):
		duplicate = True

	return duplicate

def matchSapLocationIndex(index):
	result = None

	if str(index) == '0':
		result = '/sap_demographic/'
	elif str(index) == '1':
		result = '/sap_social/'
	elif str(index) == '2':
		result = '/sap_psychoactive/'
	elif str(index) == '3':
		result = '/sap_psychoactive2/'
	elif str(index) == '4':
		result = '/sap_special/'
	elif str(index) == '5':
		result = '/sap_other/'
	elif str(index) == '6':
		result = '/sap_sources/'
	else:
		result = '/sap_viewForm/'

	return result

def forceSapLocation(sap):
	result = None
	match = None
	c_list = getCompletedSapOrdered(sap)

	for i in range(len(c_list)):
		if c_list[i] == False:
			match = i
			break

	for j in range(len(c_list)):
		if c_list[j] == False and j != match:
			result = matchSapLocationIndex(j)
			break
		else:
			result = '/sap_viewForm/'
	return result

def snatchSAPcomplete(sap):
	result = []
	result.append(sap.clinicalComplete)
	result.append(sap.socialComplete)
	result.append(sap.psychoComplete)
	result.append(sap.psycho2Complete)
	result.append(sap.specialComplete)
	result.append(sap.otherComplete)
	result.append(sap.sourcesComplete)
	result.append(sap.SapComplete)
	return result

def snatchSAPpriority(sap):
	result = []
	result.append(sap.clinicPriority)
	result.append(sap.socialPriority)
	result.append(sap.psycho1Priority)
	result.append(sap.psycho2Priority)
	result.append(sap.spacialPriority)
	result.append(sap.otherPriority)
	result.append(sap.sourcesPriority)
	result.append(False)
	return result

def snatchSAPurls():
	result = []
	result.append('/sap_demographic/')
	result.append('/sap_social/')
	result.append('/sap_psychoactive/')
	result.append('/sap_psychoactive2/')
	result.append('/sap_special/')
	result.append('/sap_other/')
	result.append('/sap_sources/')
	result.append('/sap_viewForm/')
	return result

def snatch_sap_parameters(sap):
	result = []
	complete 	= snatchSAPcomplete(sap)
	priority 	= snatchSAPpriority(sap)
	urls 		= snatchSAPurls()

	for i in range(len(urls)):
		data 				= {}
		data['complete'] 	= complete[i]
		data['priority'] 	= priority[i]
		data['url'] 		= urls[i]
		result.append(data)
	return result

def forceNextSAPpage(sap):
	result 		= None
	flag 		= None
	sap_list 	= snatch_sap_parameters(sap)

	for i in range(len(sap_list)):
		if sap_list[i]['complete'] == False:
			flag = i
			break

	for j in range(len(sap_list)):
		if sap_list[j]['complete'] == False and j != flag:
			result = sap_list[j]['url']
			break

	return result

def nextSAPage(sap, section):
	result = ''
	next_section = ''
	proceed = True
	no_result = False
	sap_list = snatch_sap_parameters(sap)

	for s in sap_list:
		if s['priority'] == True:
			result = s['url']
			proceed = False
			break

	if proceed == True:
		print 'THERE ARE NO SAP PRIORITIES...'
		for i in range(len(sap_list)):
			if sap_list[i]['complete'] == False:
				print "FOUND A FALSE VALUE AT INDEX: " + str(i)
				next_section = sap_list[i]['url']
				break

		if str(next_section) == str(section):
			result = forceNextSAPpage(sap)
		else:
			result = next_section

	return result

def hasIncompleteSAP(client):
	exist = False
	sap = SAP.objects.all()

	for s in sap:
		if s.client == client and s.SapComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientSAP(client):
	sap = SAP.objects.all()
	result = None

	for s in sap:
		if s.client == client and s.SapComplete == False:
			result = s
			break
	return result

def startSAP(client):
	result = {}

	if hasIncompleteSAP(client) == False:
		result['isNew'] = True
		result['sap'] = newSap(client)

	else:
		result['isNew'] = False
		result['sap'] = findIncompleteClientSAP(client)

	return result


def beginSAP(request):
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	client = Client.objects.get(id=client_id)
	session = ClientSession.objects.get(id=session_id)

	action = startSAP(client)
	sap = action['sap']
	setGlobalID(sap.id)

	openForm('sap', sap, client)

	result['sap'] = sap
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | S.A.P"
	result['save_this'] = 'false'

	if action['isNew'] == False:
		next_section = nextSAPage(sap, None)
		result['form'] = sap
		result['form_type'] = 'sap'
		result['type_header'] = 'S.A.P'
		result['next_section'] = next_section
		result['save_section'] = next_section

	return result


def grabSapClassesCSS(sap, m_page):
	classes = {}
	sap = grabSapCompletedSections(sap)
	normal = 'sideBarMargin'
	green = 'sideBarMarginChecked'
	current = 'sideLinkSelected'

	classes['clinic'] = processCompletedClass(sap['clinicalComplete'], '/sap_demographic/', m_page, green, current, normal)
	classes['social'] = processCompletedClass(sap['socialComplete'], '/sap_social/', m_page, green, current, normal)
	classes['psycho1'] = processCompletedClass(sap['psychoComplete'], '/sap_psychoactive/', m_page, green, current, normal)
	classes['psycho2'] = processCompletedClass(sap['psycho2Complete'], '/sap_psychoactive2/', m_page, green, current, normal)
	classes['special'] = processCompletedClass(sap['specialComplete'], '/sap_special/', m_page, green, current, normal)
	classes['other'] = processCompletedClass(sap['otherComplete'], '/sap_other/', m_page, green, current, normal)
	classes['source'] = processCompletedClass(sap['sourcesComplete'], '/sap_sources/', m_page, green, current, normal)

	return classes

def grabSapImages(sap, page):
	images = {}
	check = "/static/images/green_check.png"
	x = "/static/images/red_x.png"
	progress = "/static/images/yellow_progress.png"

	if sap.clinicalComplete == True and page != '/sap_demographic/':
		images['demo_image'] = check
	elif page == '/sap_viewForm/':
		images['demo_image'] = check
	elif page == '/sap_demographic/':
		images['demo_image'] = progress
	else:
		images['demo_image'] = x

	if sap.socialComplete == True and page != '/sap_social/':
		images['social_image'] = check
	elif page == '/sap_viewForm/':
		images['social_image'] = check
	elif page == '/sap_social/':
		images['social_image'] = progress
	else:
		images['social_image'] = x

	if sap.psychoComplete == True and page != '/sap_psychoactive/':
		images['psycho1_image'] = check
	elif page == '/sap_viewForm/':
		images['psycho1_image'] = check
	elif page == '/sap_psychoactive/':
		images['psycho1_image'] = progress
	else:
		images['psycho1_image'] = x

	if sap.psycho2Complete == True and page != '/sap_psychoactive2/':
		images['psycho2_image'] = check
	elif page == '/sap_viewForm/':
		images['psycho2_image'] = check
	elif page == '/sap_psychoactive2/':
		images['psycho2_image'] = progress
	else:
		images['psycho2_image'] = x

	if sap.specialComplete == True and page != '/sap_special/':
		images['special_image'] = check
	elif page == '/sap_viewForm/':
		images['special_image'] = check
	elif page == '/sap_special/':
		images['special_image'] = progress
	else:
		images['special_image'] = x

	if sap.otherComplete == True and page != '/sap_other/':
		images['other_image'] = check
	elif page == '/sap_viewForm/':
		images['other_image'] = check
	elif page == '/sap_other/':
		images['other_image'] = progress
	else:
		images['other_image'] = x

	if sap.sourcesComplete == True and page != '/sap_sources/':
		images['source_image'] = check
	elif page == '/sap_viewForm/':
		images['source_image'] = check
	elif page == '/sap_sources/':
		images['source_image'] = progress
	else:
		images['source_image'] = x

	return images

def getSapFields(sap, section):
	result = None
	section = str(section)

	if section == '/sap_psychoactive/':
		result = grabSapPsychoFields(sap)
	else:
		result = grabSapDemoFields(sap)

	return result

def grabSapDemoFields(sap):
	fields = {}

	fields['problem'] = sap.demographics.problem
	fields['health'] = sap.demographics.health
	fields['family'] = sap.demographics.family
	fields['psychoactive'] = sap.demographics.psychoactive
	fields['special'] = sap.demographics.special
	fields['psychological'] = sap.demographics.psychological
	fields['gambling'] = sap.demographics.gambling
	fields['abilities'] = sap.demographics.abilities
	fields['other'] = sap.demographics.other
	fields['source1'] = sap.demographics.source1
	fields['relationship1'] = sap.demographics.relationship1
	fields['source2'] = sap.demographics.source2
	fields['relationship2'] = sap.demographics.relationship2

	fields['isChild'] = sap.demographics.isChild
	fields['isSenior'] = sap.demographics.isSenior
	fields['isDual'] = sap.demographics.isDual
	fields['isOther'] = sap.demographics.isOther
	fields['isNone'] = sap.demographics.isNone

	return fields

def grabSapPsychoFields(sap):
	fields = {}

	fields['alcoholAge'] = sap.psychoactive.alcoholAge
	fields['alcoholFrequency'] = sap.psychoactive.alcoholFrequency
	fields['alcoholQuantity'] = sap.psychoactive.alcoholQuantity
	fields['alcoholLast'] = sap.psychoactive.alcoholLast
	fields['alcoholHow'] = sap.psychoactive.alcoholHow

	fields['amphAge'] = sap.psychoactive.amphAge
	fields['amphFrequency'] = sap.psychoactive.amphFrequency
	fields['amphQuantity'] = sap.psychoactive.amphQuantity
	fields['amphLast'] = sap.psychoactive.amphLast
	fields['amphHow'] = sap.psychoactive.amphHow

	fields['caffineAge'] = sap.psychoactive.caffineAge
	fields['caffineFrequency'] = sap.psychoactive.caffineFrequency
	fields['caffineQuantity'] = sap.psychoactive.caffineQuantity
	fields['caffineLast'] = sap.psychoactive.caffineLast
	fields['caffineHow'] = sap.psychoactive.caffineHow

	fields['weedAge'] = sap.psychoactive.weedAge
	fields['weedFrequency'] = sap.psychoactive.weedFrequency
	fields['weedQuantity'] = sap.psychoactive.weedQuantity
	fields['weedLast'] = sap.psychoactive.weedLast
	fields['weedHow'] = sap.psychoactive.weedHow

	fields['cokeAge'] = sap.psychoactive.cokeAge
	fields['cokeFrequency'] = sap.psychoactive.cokeFrequency
	fields['cokeQuantity'] = sap.psychoactive.cokeQuantity
	fields['cokeLast'] = sap.psychoactive.cokeLast
	fields['cokeHow'] = sap.psychoactive.cokeHow

	fields['hallAge'] = sap.psychoactive.hallAge
	fields['hallFrequency'] = sap.psychoactive.hallFrequency
	fields['hallQuantity'] = sap.psychoactive.hallQuantity
	fields['hallLast'] = sap.psychoactive.hallLast
	fields['hallHow'] = sap.psychoactive.hallHow

	fields['inhaleAge'] = sap.psychoactive.inhaleAge
	fields['inhaleFrequency'] = sap.psychoactive.inhaleFrequency
	fields['inhaleQuantity'] = sap.psychoactive.inhaleQuantity
	fields['inhaleLast'] = sap.psychoactive.inhaleLast
	fields['inhaleHow'] = sap.psychoactive.inhaleHow

	fields['smokeAge'] = sap.psychoactive.smokeAge
	fields['smokeFrequency'] = sap.psychoactive.smokeFrequency
	fields['smokeQuantity'] = sap.psychoactive.smokeQuantity
	fields['smokeLast'] = sap.psychoactive.smokeLast
	fields['smokeHow'] = sap.psychoactive.smokeHow

	fields['opAge'] = sap.psychoactive.opAge
	fields['opFrequency'] = sap.psychoactive.opFrequency
	fields['opQuantity'] = sap.psychoactive.opQuantity
	fields['opLast'] = sap.psychoactive.opLast
	fields['opHow'] = sap.psychoactive.opHow

	fields['pcpAge'] = sap.psychoactive.pcpAge
	fields['pcpFrequency'] = sap.psychoactive.pcpFrequency
	fields['pcpQuantity'] = sap.psychoactive.pcpQuantity
	fields['pcpLast'] = sap.psychoactive.pcpLast
	fields['pcpHow'] = sap.psychoactive.pcpHow

	fields['sedAge'] = sap.psychoactive.sedAge
	fields['sedFrequency'] = sap.psychoactive.sedFrequency
	fields['sedQuantity'] = sap.psychoactive.sedQuantity
	fields['sedLast'] = sap.psychoactive.sedLast
	fields['sedHow'] = sap.psychoactive.sedHow

	fields['otherAge'] = sap.psychoactive.otherAge
	fields['otherFrequency'] = sap.psychoactive.otherFrequency
	fields['otherQuantity'] = sap.psychoactive.otherQuantity
	fields['otherLast'] = sap.psychoactive.otherLast
	fields['otherHow'] = sap.psychoactive.otherHow

	return fields

def saveSapPhycho1(request, sap):
	alcoholAge = request.POST.get('alcoholAge', '')
	alcoholFrequency = request.POST.get('alcoholFrequency', '')
	alcoholQuantity = request.POST.get('alcoholQuantity', '')
	alcoholLast = request.POST.get('alcoholLast', '')
	alcoholHow = request.POST.get('alcoholHow', '')

	amphAge = request.POST.get('amphAge', '')
	amphFrequency = request.POST.get('amphFrequency', '')
	amphQuantity = request.POST.get('amphQuantity', '')
	amphLast = request.POST.get('amphLast', '')
	amphHow = request.POST.get('amphHow', '')

	caffineAge = request.POST.get('caffineAge', '')
	caffineFrequency = request.POST.get('caffineFrequency', '')
	caffineQuantity = request.POST.get('caffineQuantity', '')
	caffineLast = request.POST.get('caffineLast', '')
	caffineHow = request.POST.get('caffineHow', '')

	weedAge = request.POST.get('weedAge', '')
	weedFrequency = request.POST.get('weedFrequency', '')
	weedQuantity = request.POST.get('weedQuantity', '')
	weedLast = request.POST.get('weedLast', '')
	weedHow = request.POST.get('weedHow', '')

	cokeAge = request.POST.get('cokeAge', '')
	cokeFrequency = request.POST.get('cokeFrequency', '')
	cokeQuantity = request.POST.get('cokeQuantity', '')
	cokeLast = request.POST.get('cokeLast', '')
	cokeHow = request.POST.get('cokeHow', '')

	hallAge = request.POST.get('hallAge', '')
	hallFrequency = request.POST.get('hallFrequency', '')
	hallQuantity = request.POST.get('hallQuantity', '')
	hallLast = request.POST.get('hallLast', '')
	hallHow = request.POST.get('hallHow', '')

	inhaleAge = request.POST.get('inhaleAge', '')
	inhaleFrequency = request.POST.get('inhaleFrequency', '')
	inhaleQuantity = request.POST.get('inhaleQuantity', '')
	inhaleLast = request.POST.get('inhaleLast', '')
	inhaleHow = request.POST.get('inhaleHow', '')

	smokeAge = request.POST.get('smokeAge', '')
	smokeFrequency = request.POST.get('smokeFrequency', '')
	smokeQuantity = request.POST.get('smokeQuantity', '')
	smokeLast = request.POST.get('smokeLast', '')
	smokeHow = request.POST.get('smokeHow', '')

	opAge = request.POST.get('opAge', '')
	opFrequency = request.POST.get('opFrequency', '')
	opQuantity = request.POST.get('opQuantity', '')
	opLast = request.POST.get('opLast', '')
	opHow = request.POST.get('opHow', '')

	pcpAge = request.POST.get('pcpAge', '')
	pcpFrequency = request.POST.get('pcpFrequency', '')
	pcpQuantity = request.POST.get('pcpQuantity', '')
	pcpLast = request.POST.get('pcpLast', '')
	pcpHow = request.POST.get('pcpHow', '')

	sedAge = request.POST.get('sedAge', '')
	sedFrequency = request.POST.get('sedFrequency', '')
	sedQuantity = request.POST.get('sedQuantity', '')
	sedLast = request.POST.get('sedLast', '')
	sedHow = request.POST.get('sedHow', '')

	otherAge = request.POST.get('otherAge', '')
	otherFrequency = request.POST.get('otherFrequency', '')
	otherQuantity = request.POST.get('otherQuantity', '')
	otherLast = request.POST.get('otherLast', '')
	otherHow = request.POST.get('otherHow', '')

	psycho = sap.psychoactive

	psycho.alcoholAge = alcoholAge
	psycho.alcoholFrequency = alcoholFrequency
	psycho.alcoholQuantity = alcoholQuantity
	psycho.alcoholLast = alcoholLast
	psycho.alcoholHow = alcoholHow

	psycho.amphAge = amphAge
	psycho.amphFrequency = amphFrequency
	psycho.amphQuantity = amphQuantity
	psycho.amphLast = amphLast
	psycho.amphHow = amphHow

	psycho.caffineAge = caffineAge
	psycho.caffineFrequency = caffineFrequency
	psycho.caffineQuantity = caffineQuantity
	psycho.caffineLast = caffineLast
	psycho.caffineHow = caffineHow

	psycho.weedAge = weedAge
	psycho.weedFrequency = weedFrequency
	psycho.weedQuantity = weedQuantity
	psycho.weedLast = weedLast
	psycho.weedHow = weedHow

	psycho.cokeAge = cokeAge
	psycho.cokeFrequency = cokeFrequency
	psycho.cokeQuantity = cokeQuantity
	psycho.cokeLast = cokeLast
	psycho.cokeHow = cokeHow

	psycho.hallAge = hallAge
	psycho.hallFrequency = hallFrequency
	psycho.hallQuantity = hallQuantity
	psycho.hallLast = hallLast
	psycho.hallHow = hallHow

	psycho.inhaleAge = inhaleAge
	psycho.inhaleFrequency = inhaleFrequency
	psycho.inhaleQuantity = inhaleQuantity
	psycho.inhaleLast = inhaleLast
	psycho.inhaleHow = inhaleHow

	psycho.smokeAge = smokeAge
	psycho.smokeFrequency = smokeFrequency
	psycho.smokeQuantity = smokeQuantity
	psycho.smokeLast = smokeLast
	psycho.smokeHow = smokeHow

	psycho.opAge = opAge
	psycho.opFrequency = opFrequency
	psycho.opQuantity = opQuantity
	psycho.opLast = opLast
	psycho.opHow = opHow

	psycho.pcpAge = pcpAge
	psycho.pcpFrequency = pcpFrequency
	psycho.pcpQuantity = pcpQuantity
	psycho.pcpLast = pcpLast
	psycho.pcpHow = pcpHow

	psycho.sedAge = sedAge
	psycho.sedFrequency = sedFrequency
	psycho.sedQuantity = sedQuantity
	psycho.sedLast = sedLast
	psycho.sedHow = sedHow

	psycho.otherAge = otherAge
	psycho.otherFrequency = otherFrequency
	psycho.otherQuantity = otherQuantity
	psycho.otherLast = otherLast
	psycho.otherHow = otherHow

	psycho.save()
	sap.psychoComplete = True
	sap.save()

def saveSapDemoSection(request, section, sap):
	demo = sap.demographics

	if str(section) == '/sap_demographic/':
		problem = request.POST.get('problem', '')
		health = request.POST.get('health', '')

		demo.problem = problem
		demo.health = health
		demo.save()
		sap.clinicalComplete = True
		sap.save()

	elif str(section) == '/sap_social/':
		family = request.POST.get('family')

		demo.family = family
		demo.save()
		sap.socialComplete = True
		sap.save()

	elif str(section) == '/sap_psychoactive/':
		saveSapPhycho1(request, sap)

	elif str(section) == '/sap_psychoactive2/':
		psychoactive = request.POST.get('psychoactive')

		demo.psychoactive = psychoactive
		demo.save()
		sap.psycho2Complete = True
		sap.save()

	elif str(section) == '/sap_special/':
		isChild = request.POST.get('m_isChild', '')
		isSenior = request.POST.get('m_isSenior', '')
		isDual = request.POST.get('m_isDual', '')
		isOther = request.POST.get('m_isOther', '')
		isNone = request.POST.get('m_isNone', '')
		special = request.POST.get('m_special', '')

		isChild = truePythonBool(isChild)
		isSenior = truePythonBool(isSenior)
		isDual = truePythonBool(isDual)
		isOther = truePythonBool(isOther)
		isNone = truePythonBool(isNone)

		demo.special = special
		demo.isChild = isChild
		demo.isSenior = isSenior
		demo.isDual = isDual
		demo.isOther = isOther
		demo.isNone = isNone

		demo.save()
		sap.specialComplete = True
		sap.save()

	elif str(section) == '/sap_other/':
		psychological = request.POST.get('psychological', '')
		gambling = request.POST.get('gambling', '')
		abilities = request.POST.get('abilities', '')
		other = request.POST.get('other', '')

		demo.psychological = psychological
		demo.gambling = gambling
		demo.abilities = abilities
		demo.other = other

		demo.save()
		sap.otherComplete = True
		sap.save()

	elif str(section) == '/sap_sources/':
		source1 = request.POST.get('source1', '')
		source2 = request.POST.get('source2', '')
		relationship1 = request.POST.get('relationship1', '')
		relationship2 = request.POST.get('relationship2', '')

		demo.source1 = source1
		demo.source2 = source2
		demo.relationship1 = relationship1
		demo.relationship2 = relationship2

		demo.save()
		sap.sourcesComplete = True
		sap.save()

def saveSap(request, section, sap):
	if str(section) == '/sap_demographic/':
		problem = request.POST.get('problem', '')
		health = request.POST.get('health', '')

		sap.demographics.problem = problem
		sap.demographics.health = health
		sap.demographics.save()

	elif str(section) == '/sap_social/':
		family = request.POST.get('family')

		sap.demographics.family = family
		sap.demographics.save()

	elif str(section) == '/sap_psychoactive/':
		saveSapPhycho1(request, sap)

	elif str(section) == '/sap_psychoactive2/':
		psychoactive = request.POST.get('psychoactive')

		sap.demographics.psychoactive = psychoactive
		sap.demographics.save()

	elif str(section) == '/sap_special/':
		isChild = request.POST.get('m_isChild', '')
		isSenior = request.POST.get('m_isSenior', '')
		isDual = request.POST.get('m_isDual', '')
		isOther = request.POST.get('m_isOther', '')
		isNone = request.POST.get('m_isNone', '')
		special = request.POST.get('m_special', '')

		isChild = truePythonBool(isChild)
		isSenior = truePythonBool(isSenior)
		isDual = truePythonBool(isDual)
		isOther = truePythonBool(isOther)
		isNone = truePythonBool(isNone)

		sap.demographics.special = special
		sap.demographics.isChild = isChild
		sap.demographics.isSenior = isSenior
		sap.demographics.isDual = isDual
		sap.demographics.isOther = isOther
		sap.demographics.isNone = isNone

		sap.demographics.save()

	elif str(section) == '/sap_other/':
		psychological = request.POST.get('psychological', '')
		gambling = request.POST.get('gambling', '')
		abilities = request.POST.get('abilities', '')
		other = request.POST.get('other', '')

		sap.demographics.psychological = psychological
		sap.demographics.gambling = gambling
		sap.demographics.abilities = abilities
		sap.demographics.other = other

		sap.demographics.save()

	elif str(section) == '/sap_sources/':
		source1 = request.POST.get('source1', '')
		source2 = request.POST.get('source2', '')
		relationship1 = request.POST.get('relationship1', '')
		relationship2 = request.POST.get('relationship2', '')

		sap.demographics.source1 = source1
		sap.demographics.source2 = source2
		sap.demographics.relationship1 = relationship1
		sap.demographics.relationship2 = relationship2

		sap.demographics.save()

def saveIncompleteSapPsycho1(request, sap):
	alcoholAge = request.POST.get('alcoholAge', '')
	alcoholFrequency = request.POST.get('alcoholFrequency', '')
	alcoholQuantity = request.POST.get('alcoholQuantity', '')
	alcoholLast = request.POST.get('alcoholLast', '')
	alcoholHow = request.POST.get('alcoholHow', '')

	amphAge = request.POST.get('amphAge', '')
	amphFrequency = request.POST.get('amphFrequency', '')
	amphQuantity = request.POST.get('amphQuantity', '')
	amphLast = request.POST.get('amphLast', '')
	amphHow = request.POST.get('amphHow', '')

	caffineAge = request.POST.get('caffineAge', '')
	caffineFrequency = request.POST.get('caffineFrequency', '')
	caffineQuantity = request.POST.get('caffineQuantity', '')
	caffineLast = request.POST.get('caffineLast', '')
	caffineHow = request.POST.get('caffineHow', '')

	weedAge = request.POST.get('weedAge', '')
	weedFrequency = request.POST.get('weedFrequency', '')
	weedQuantity = request.POST.get('weedQuantity', '')
	weedLast = request.POST.get('weedLast', '')
	weedHow = request.POST.get('weedHow', '')

	cokeAge = request.POST.get('cokeAge', '')
	cokeFrequency = request.POST.get('cokeFrequency', '')
	cokeQuantity = request.POST.get('cokeQuantity', '')
	cokeLast = request.POST.get('cokeLast', '')
	cokeHow = request.POST.get('cokeHow', '')

	hallAge = request.POST.get('hallAge', '')
	hallFrequency = request.POST.get('hallFrequency', '')
	hallQuantity = request.POST.get('hallQuantity', '')
	hallLast = request.POST.get('hallLast', '')
	hallHow = request.POST.get('hallHow', '')

	inhaleAge = request.POST.get('inhaleAge', '')
	inhaleFrequency = request.POST.get('inhaleFrequency', '')
	inhaleQuantity = request.POST.get('inhaleQuantity', '')
	inhaleLast = request.POST.get('inhaleLast', '')
	inhaleHow = request.POST.get('inhaleHow', '')

	smokeAge = request.POST.get('smokeAge', '')
	smokeFrequency = request.POST.get('smokeFrequency', '')
	smokeQuantity = request.POST.get('smokeQuantity', '')
	smokeLast = request.POST.get('smokeLast', '')
	smokeHow = request.POST.get('smokeHow', '')

	opAge = request.POST.get('opAge', '')
	opFrequency = request.POST.get('opFrequency', '')
	opQuantity = request.POST.get('opQuantity', '')
	opLast = request.POST.get('opLast', '')
	opHow = request.POST.get('opHow', '')

	pcpAge = request.POST.get('pcpAge', '')
	pcpFrequency = request.POST.get('pcpFrequency', '')
	pcpQuantity = request.POST.get('pcpQuantity', '')
	pcpLast = request.POST.get('pcpLast', '')
	pcpHow = request.POST.get('pcpHow', '')

	sedAge = request.POST.get('sedAge', '')
	sedFrequency = request.POST.get('sedFrequency', '')
	sedQuantity = request.POST.get('sedQuantity', '')
	sedLast = request.POST.get('sedLast', '')
	sedHow = request.POST.get('sedHow', '')

	otherAge = request.POST.get('otherAge', '')
	otherFrequency = request.POST.get('otherFrequency', '')
	otherQuantity = request.POST.get('otherQuantity', '')
	otherLast = request.POST.get('otherLast', '')
	otherHow = request.POST.get('otherHow', '')

	psycho = sap.psychoactive

	psycho.alcoholAge = alcoholAge
	psycho.alcoholFrequency = alcoholFrequency
	psycho.alcoholQuantity = alcoholQuantity
	psycho.alcoholLast = alcoholLast
	psycho.alcoholHow = alcoholHow

	psycho.amphAge = amphAge
	psycho.amphFrequency = amphFrequency
	psycho.amphQuantity = amphQuantity
	psycho.amphLast = amphLast
	psycho.amphHow = amphHow

	psycho.caffineAge = caffineAge
	psycho.caffineFrequency = caffineFrequency
	psycho.caffineQuantity = caffineQuantity
	psycho.caffineLast = caffineLast
	psycho.caffineHow = caffineHow

	psycho.weedAge = weedAge
	psycho.weedFrequency = weedFrequency
	psycho.weedQuantity = weedQuantity
	psycho.weedLast = weedLast
	psycho.weedHow = weedHow

	psycho.cokeAge = cokeAge
	psycho.cokeFrequency = cokeFrequency
	psycho.cokeQuantity = cokeQuantity
	psycho.cokeLast = cokeLast
	psycho.cokeHow = cokeHow

	psycho.hallAge = hallAge
	psycho.hallFrequency = hallFrequency
	psycho.hallQuantity = hallQuantity
	psycho.hallLast = hallLast
	psycho.hallHow = hallHow

	psycho.inhaleAge = inhaleAge
	psycho.inhaleFrequency = inhaleFrequency
	psycho.inhaleQuantity = inhaleQuantity
	psycho.inhaleLast = inhaleLast
	psycho.inhaleHow = inhaleHow

	psycho.smokeAge = smokeAge
	psycho.smokeFrequency = smokeFrequency
	psycho.smokeQuantity = smokeQuantity
	psycho.smokeLast = smokeLast
	psycho.smokeHow = smokeHow

	psycho.opAge = opAge
	psycho.opFrequency = opFrequency
	psycho.opQuantity = opQuantity
	psycho.opLast = opLast
	psycho.opHow = opHow

	psycho.pcpAge = pcpAge
	psycho.pcpFrequency = pcpFrequency
	psycho.pcpQuantity = pcpQuantity
	psycho.pcpLast = pcpLast
	psycho.pcpHow = pcpHow

	psycho.sedAge = sedAge
	psycho.sedFrequency = sedFrequency
	psycho.sedQuantity = sedQuantity
	psycho.sedLast = sedLast
	psycho.sedHow = sedHow

	psycho.otherAge = otherAge
	psycho.otherFrequency = otherFrequency
	psycho.otherQuantity = otherQuantity
	psycho.otherLast = otherLast
	psycho.otherHow = otherHow

	psycho.save()
	sap.psychoComplete = False
	sap.save()

def saveIncompleteSapForm(request, section, sap):
	demo = sap.demographics

	if str(section) == '/sap_demographic/':
		problem = request.POST.get('problem', '')
		health = request.POST.get('health', '')

		demo.problem = problem
		demo.health = health
		demo.save()
		sap.clinicalComplete = False
		sap.save()

	elif str(section) == '/sap_social/':
		family = request.POST.get('family')

		demo.family = family
		demo.save()
		sap.socialComplete = False
		sap.save()

	elif str(section) == '/sap_psychoactive/':
		saveIncompleteSapPsycho1(request, sap)

	elif str(section) == '/sap_psychoactive2/':
		psychoactive = request.POST.get('psychoactive')

		demo.psychoactive = psychoactive
		demo.save()
		sap.psycho2Complete = False
		sap.save()

	elif str(section) == '/sap_special/':
		isChild = request.POST.get('m_isChild', '')
		isSenior = request.POST.get('m_isSenior', '')
		isDual = request.POST.get('m_isDual', '')
		isOther = request.POST.get('m_isOther', '')
		isNone = request.POST.get('m_isNone', '')
		special = request.POST.get('m_special', '')

		isChild = truePythonBool(isChild)
		isSenior = truePythonBool(isSenior)
		isDual = truePythonBool(isDual)
		isOther = truePythonBool(isOther)
		isNone = truePythonBool(isNone)

		demo.special = special
		demo.isChild = isChild
		demo.isSenior = isSenior
		demo.isDual = isDual
		demo.isOther = isOther
		demo.isNone = isNone

		demo.save()
		sap.specialComplete = False
		sap.save()

	elif str(section) == '/sap_other/':
		psychological = request.POST.get('psychological', '')
		gambling = request.POST.get('gambling', '')
		abilities = request.POST.get('abilities', '')
		other = request.POST.get('other', '')

		demo.psychological = psychological
		demo.gambling = gambling
		demo.abilities = abilities
		demo.other = other

		demo.save()
		sap.otherComplete = False
		sap.save()

	elif str(section) == '/sap_sources/':
		source1 = request.POST.get('source1', '')
		source2 = request.POST.get('source2', '')
		relationship1 = request.POST.get('relationship1', '')
		relationship2 = request.POST.get('relationship2', '')

		demo.source1 = source1
		demo.source2 = source2
		demo.relationship1 = relationship1
		demo.relationship2 = relationship2

		demo.save()
		sap.sourcesComplete = False
		sap.save()

def deleteSap(sap):
	sap.demographics.delete()
	sap.psychoactive.delete()
	sap.delete()

def refreshSap(sap):
	demo = sap.demographics
	psy = sap.psychoactive

	demo.startTime1 = ''
	demo.startTime2 = ''
	demo.startTime3 = ''

	demo.problem = ''
	demo.health = ''
	demo.family = ''
	demo.psychoactive = ''
	demo.special = ''
	demo.psychological = ''
	demo.gambling = ''
	demo.abilities = ''
	demo.other = ''
	demo.source1 = ''
	demo.relationship1 = ''
	demo.source2 = ''
	demo.relationship2 = ''

	demo.isChild = False
	demo.isSenior = False
	demo.isDual = False
	demo.isOther = False
	demo.isNone = False

	psy.alcoholAge = 0
	psy.alcoholFrequency = ''
	psy.alcoholQuantity = ''
	psy.alcoholLast = ''
	psy.alcoholHow = ''

	psy.amphAge = 0
	psy.amphFrequency = ''
	psy.amphQuantity = ''
	psy.amphLast = ''
	psy.amphHow = ''

	psy.caffineAge = 0
	psy.caffineFrequency = ''
	psy.caffineQuantity = ''
	psy.caffineLast = ''
	psy.caffineHow = ''

	psy.weedAge = 0
	psy.weedFrequency = ''
	psy.weedQuantity = ''
	psy.weedLast = ''
	psy.weedHow = ''

	psy.cokeAge = 0
	psy.cokeFrequency = ''
	psy.cokeQuantity = ''
	psy.cokeLast = ''
	psy.cokeHow = ''

	psy.hallAge = 0
	psy.hallFrequency = ''
	psy.hallQuantity = ''
	psy.hallLast = ''
	psy.hallHow = ''

	psy.inhaleAge = 0
	psy.inhaleFrequency = ''
	psy.inhaleQuantity = ''
	psy.inhaleLast = ''
	psy.inhaleHow = ''

	psy.smokeAge = 0
	psy.smokeFrequency = ''
	psy.smokeQuantity = ''
	psy.smokeLast = ''
	psy.smokeHow = ''

	psy.opAge = 0
	psy.opFrequency = ''
	psy.opQuantity = ''
	psy.opLast = ''
	psy.opHow = ''

	psy.pcpAge = 0
	psy.pcpFrequency = ''
	psy.pcpQuantity = ''
	psy.pcpLast = ''
	psy.pcpHow = ''

	psy.sedAge = 0
	psy.sedFrequency = ''
	psy.sedQuantity = ''
	psy.sedLast = ''
	psy.sedHow = ''

	psy.otherAge = 0
	psy.otherFrequency = ''
	psy.otherQuantity = ''
	psy.otherLast = ''
	psy.otherHow = ''

	sap.clinicalComplete = False
	sap.socialComplete = False
	sap.psychoComplete = False
	sap.psycho2Complete = False
	sap.specialComplete = False
	sap.otherComplete = False
	sap.sourcesComplete = False

	sap.clinicPriority = True
	sap.socialPriority = False
	sap.psycho1Priority = False
	sap.psycho2Priority = False
	sap.spacialPriority = False
	sap.otherPriority = False
	sap.sourcesPriority = False

	demo.save()
	psy.save()

	sap.SapComplete = False
	sap.save()

def setSapSectionComplete(sap, section):
	section = str(section)

	if section == '/sap_demographic/':
		sap.clinicalComplete = True
	elif section == '/sap_social/':
		sap.socialComplete = True
	elif section == '/sap_psychoactive/':
		sap.psychoComplete = True
	elif section == '/sap_psychoactive2/':
		sap.psycho2Complete = True
	elif section == '/sap_special/':
		sap.specialComplete = True
	elif section == '/sap_other/':
		sap.otherComplete = True
	elif section == '/sap_sources/':
		sap.sourcesComplete = True
	sap.save()

def processSapData(request, current_section):
	result = {}

	session_id = request.POST.get('session_id', '')
	sap_id = request.POST.get('sap_id', '')
	save_this = request.POST.get('save_this', '')
	section = request.POST.get('save_section', '')

	session = ClientSession.objects.get(id=session_id)
	sap = SAP.objects.get(id=sap_id)
	deprioritizeSAP(sap)
	fields = getSapFields(sap, current_section)
	json_data = json.dumps(fields)

	if save_this == 'true':
		saveSap(request, section, sap)
		setSapSectionComplete(sap, section)

	next_url = nextSAPage(sap, current_section)
	image = grabSapImages(sap, current_section)
	classes = grabSapClassesCSS(sap, current_section)

	result['class'] = classes
	result['image'] = image
	result['next_url'] = next_url
	result['session'] = session
	result['sap'] = sap
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | S.A.P Assessment"

	return result

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
################################################################# END SAP #################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



###########################################################################################################################################
#*****************************************************************************************************************************************#
#-----------------------------------------------------------  MENTAL HEALTH --------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################

def getOrderedMhNames():
	result = []

	result.append('history')
	result.append('education')
	result.append('finance')
	result.append('stressors')
	result.append('family')
	result.append('legal')
	result.append('psych')
	result.append('use')

	return result

def getOrderedMhCompleteName():
	result = []

	result.append('demographicsComplete')
	result.append('educationComplete')
	result.append('backgroundComplete')
	result.append('stressorComplete')
	result.append('familyComplete')
	result.append('legalComplete')
	result.append('psychComplete')
	result.append('useComplete')

	return result

def getOrderedMhURLS():
	result = []

	result.append('/mh_demographic/')
	result.append('/mh_education/')
	result.append('/mh_background/')
	result.append('/mh_stress/')
	result.append('/mh_familyHistory/')
	result.append('/mh_legal/')
	result.append('/mh_psych/')
	result.append('/mh_useTable/')
	# result.append('/mh_viewForm/')

	return result

def getOrderedMhButtonNames():
	result = []

	result.append('mhHistory_image')
	result.append('mhEducation_image')
	result.append('mhBackground_image')
	result.append('mhStress_image')
	result.append('mhFamily_image')
	result.append('mhLegal_image')
	result.append('mhPsych_image')
	result.append('mhUse_image')

	return result

def getMhOrderedCompleteValues(mh):
	result = []

	result.append(mh.demographicsComplete)
	result.append(mh.educationComplete)
	result.append(mh.backgroundComplete)
	result.append(mh.stressorComplete)
	result.append(mh.familyComplete)
	result.append(mh.legalComplete)
	result.append(mh.psychComplete)
	result.append(mh.useComplete)

	return result

def getOrderedMhPriorityValue(mh):
	result = []

	result.append(mh.demoPriority)
	result.append(mh.educationPriority)
	result.append(mh.backgroundPriority)
	result.append(mh.stressPriority)
	result.append(mh.familyPriority)
	result.append(mh.legalPriority)
	result.append(mh.psychPriority)
	result.append(mh.psychPriority)

	return result

def grabOrderedMh(mh):
	mh_list 	= []
	name 		= getOrderedMhNames()
	url 		= getOrderedMhURLS()
	complete 	= getMhOrderedCompleteValues(mh)
	priority 	= getOrderedMhPriorityValue(mh)
	btn 		= getOrderedMhButtonNames()
	cName 		= getOrderedMhCompleteName()

	for i in range(len(name)):
		data = {}
		data['name'] 		= name[i]
		data['url'] 		= url[i]
		data['complete'] 	= complete[i]
		data['priority'] 	= priority[i]
		data['btn'] 		= btn[i]
		data['cName'] 		= cName[i]
		mh_list.append(data)

	return mh_list

def forceNextMhPage(mh):
	result 	= None
	flag 	= None
	mh_list = grabOrderedMh(mh)

	for i in range(len(mh_list)):
		if mh_list[i]['complete'] == False:
			flag = i
			break

	for j in range(len(mh_list)):
		if mh_list[j]['complete'] == False and j != flag:
			result = mh_list[j]['url']
			break

	return result

def nextMhPage(mh, section):
	result 		= None
	nextSection = None
	proceed 	= True
	mh_list 	= grabOrderedMh(mh)

	for m in mh_list:
		if m['priority'] == True:
			result = m['url']
			proceed = False
			break

	if proceed == True:
		for i in range(len(mh_list)):
			if mh_list[i]['complete'] == False:
				nextSection = mh_list[i]['url']
				break

		if str(nextSection) == str(section):
			result = forceNextMhPage(mh)
		else:
			result = nextSection

	if result == None:
		result = '/mh_viewForm/'

	return result

def hasIncompleteMh(client):
	exist = False
	mhs = MentalHealth.objects.all()

	for m in mhs:
		if m.client == client and m.MHComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientMh(client):
	mhs = MentalHealth.objects.all()
	result = None

	for m in mhs:
		if m.client == client and m.MHComplete == False:
			result = m
			break
	return result

def newMh(the_client):
	date = datetime.now()
	date = date.date()

	mh = MentalHealth(client=the_client, date_of_assessment=date)

	demo = MHDemographic(clientID=the_client.clientID)	
	education = MHEducation(clientID=the_client.clientID)
	background = MHBackground(clientID=the_client.clientID)
	stressors = MHStressor(clientID=the_client.clientID)
	familyHistory = MHFamilyHistory(clientID=the_client.clientID)
	legalHistory = MHLegalHistory(clientID=the_client.clientID)
	useTable = MHUseTable(clientID=the_client.clientID)

	demo.save()
	education.save()
	background.save()
	stressors.save()
	familyHistory.save()
	legalHistory.save()
	useTable.save()

	mh.demographics = demo
	mh.education = education
	mh.background = background
	mh.stressors = stressors
	mh.familyHistory = familyHistory
	mh.legalHistory = legalHistory
	mh.useTable = useTable

	mh.isOpen = True
	mh.MHComplete = False
	mh.save()

	return mh


def startMH(client):
	result = {}

	if hasIncompleteMh(client) == False:
		result['isNew'] = True
		result['mh'] = newMh(client)

	else:
		result['isNew'] = False
		result['mh'] = findIncompleteClientMh(client)

	return result

def beginMH(request):
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	client = Client.objects.get(id=client_id)
	session = ClientSession.objects.get(id=session_id)

	action = startMH(client)
	mh = action['mh']
	setGlobalID(mh.id)

	openForm('mh', mh, client)

	result['mh'] = mh
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | Mental Health Assessment"
	result['save_this'] = 'false'

	if action['isNew'] == False:
		next_section = nextMhPage(mh, None)
		result['form'] = mh
		result['form_type'] = 'mh'
		result['type_header'] = 'Mental Health'
		result['next_section'] = next_section
		result['save_section'] = next_section

	return result

def grabMhClassesCSS(mh, m_page):
	classes = {}
	mh = grabOrderedMh(mh)
	normal = 'sideBarMargin'
	green = 'sideBarMarginChecked'
	current = 'sideLinkSelected'

	classes['mhHistory'] = processCompletedClass(mh[0]['complete'], mh[0]['url'], m_page, green, current, normal)
	classes['mhEducation'] = processCompletedClass(mh[1]['complete'], mh[1]['url'], m_page, green, current, normal)
	classes['mhBackground'] = processCompletedClass(mh[2]['complete'], mh[2]['url'], m_page, green, current, normal)
	classes['mhStress'] = processCompletedClass(mh[3]['complete'], mh[3]['url'], m_page, green, current, normal)
	classes['mhFamily'] = processCompletedClass(mh[4]['complete'], mh[4]['url'], m_page, green, current, normal)
	classes['mhLegal'] = processCompletedClass(mh[5]['complete'], mh[5]['url'], m_page, green, current, normal)	
	classes['mhPsych'] = processCompletedClass(mh[6]['complete'], mh[6]['url'], m_page, green, current, normal)
	classes['mhUse'] = processCompletedClass(mh[7]['complete'], mh[7]['url'], m_page, green, current, normal)

	return classes

def grabMhSideImages(mh, page):
	images = {}
	check = "/static/images/green_check.png"
	x = "/static/images/red_x.png"
	progress = "/static/images/yellow_progress.png"
	mhComps = grabOrderedMh(mh)

	for m in mhComps:
		if m['complete'] == True and page != m['url']:
			images[m['btn']] = check
		elif page == '/mh_viewForm/':
			images[m['btn']] = check
		elif page == m['url']:
			images[m['btn']] = progress
		else:
			images[m['btn']] = x

	return images

def grabMhResidentIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Rent':
		result = 1
	elif selection == 'Own Home':
		result = 2
	elif selection == 'Subsidized Housing':
		result = 3
	else:
		result = 0

	return result

def grabLowMedHighIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Low':
		result = 1
	elif selection == 'Medium':
		result = 2
	elif selection == 'High':
		result = 3
	else:
		result = 0

	return result

def grabMhCreditIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Poor':
		result = 1
	elif selection == 'Fair':
		result = 2
	elif selection == 'Good':
		result = 3
	elif selection == 'Bankruptcy':
		result = 4
	else:
		result = 0

	return result

def grabMhHealthIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Company Health Benefits':
		result = 1
	elif selection == 'Private Insurance':
		result = 2
	elif selection == 'Medicaid':
		result = 3
	elif selection == 'Medicare':
		result = 4
	elif selection == 'Self-Pay':
		result = 5
	else:
		result = 0

	return result

def grabMhOtherIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Alimony':
		result = 1
	elif selection == 'Child Support':
		result = 2
	elif selection == 'Aid to Dependant Children':
		result = 3
	elif selection == 'SSI':
		result = 4
	elif selection == 'Retired':
		result = 5
	elif selection == 'Support from Relatives':
		result = 6
	else:
		result = 0

	return result

def grabWeeklyIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Weekly':
		result = 1
	elif selection == 'Monthly':
		result = 2
	elif selection == 'Yearly':
		result = 3
	else:
		result = 0

	return result

def grabMhFamilySideIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Maternal':
		result = 1
	elif selection == 'Paternal':
		result = 2
	else:
		result = 0

	return result

def grabMhFamilyMemberIndex(selection):
	result = None
	selection = str(selection)

	if selection == 'Mother':
		result = 1
	elif selection == 'Father':
		result = 2
	elif selection == 'Sister':
		result = 3
	elif selection == 'Brother':
		result = 4
	elif selection == 'Child':
		result = 5
	elif selection == 'Aunt':
		result = 6
	elif selection == 'Uncle':
		result = 7
	elif selection == 'Grandmother':
		result = 8
	elif selection == 'Grandfather':
		result = 9
	else:
		result = 0

	return result

def decodeMhFamilyText(m_value):
	## This function will convert the strings to a value that can be displayed by a html select element
 	result = {}
	m_value = str(m_value)
	side = ''
	member = ''
	flag = 0

	for i in range(len(m_value)):
		if m_value[i] == ' ':
			flag = i
			break

	for j in range(0, flag):
		side += m_value[j]

	for k in range((flag + 1), len(m_value)):
		member += m_value[k]

	result['side'] = grabMhFamilySideIndex(side)
	result['member'] = grabMhFamilyMemberIndex(member)

	return result

def getMhDemoFields(mh):
	results = {}

	results['birthplace'] = mh.demographics.birthplace
	results['raised'] = mh.demographics.raised
	results['maritalStatus'] = mh.demographics.maritalStatus
	results['numMarriages'] = mh.demographics.numMarriages
	results['occupation'] = mh.demographics.occupation
	results['employer'] = mh.demographics.employer
	results['employedMo'] = mh.demographics.employedMo
	results['employedYrs'] = mh.demographics.employedYrs
	results['pastJobs'] = mh.demographics.pastJobs
	results['recentMove'] = mh.demographics.recentMove
	results['spouseAge'] = mh.demographics.spouseAge
	results['spouseOccupation'] = mh.demographics.spouseOccupation
	results['spouseEmployer'] = mh.demographics.spouseEmployer
	results['spouseWorkMos'] = mh.demographics.spouseWorkMos
	results['spouseWorkYrs'] = mh.demographics.spouseWorkYrs

	results['motherOccupation'] = mh.demographics.motherOccupation
	results['motherCity'] = mh.demographics.motherCity
	results['motherState'] = mh.demographics.motherState
	results['motherLiving'] = mh.demographics.motherLiving
	results['motherAge'] = mh.demographics.motherAge
	results['motherAgeDeath'] = mh.demographics.motherAgeDeath

	results['fatherOccupation'] = mh.demographics.fatherOccupation
	results['fatherCity'] = mh.demographics.fatherCity
	results['fatherLiving'] = mh.demographics.fatherLiving
	results['fatherState'] = mh.demographics.fatherState
	results['fatherAge'] = mh.demographics.fatherAge
	results['fatherAgeDeath'] = mh.demographics.fatherAgeDeath

	results['numChildren'] = mh.demographics.numChildren
	results['numSisters'] = mh.demographics.numSisters
	results['numBrothers'] = mh.demographics.numBrothers

	return results

def getMhEducationFields(mh):
	result = {}

	result['GradesKto6'] = mh.education.GradesKto6
	result['BehaviorProblemsKto6'] = mh.education.BehaviorProblemsKto6
	result['AcademicProblemsKto6'] = mh.education.AcademicProblemsKto6
	result['FriendshipsKto6'] = mh.education.FriendshipsKto6
	result['Grades7to9'] = mh.education.Grades7to9
	result['BehaviorProblems7to9'] = mh.education.BehaviorProblems7to9
	result['AcademicProblems7to9'] = mh.education.AcademicProblems7to9
	result['Friendships7to9'] = mh.education.Friendships7to9
	result['Grades10to12'] = mh.education.Grades10to12
	result['BehaviorProblems10to12'] = mh.education.BehaviorProblems10to12
	result['AcademicProblems10to12'] = mh.education.AcademicProblems10to12
	result['Friendships10to12'] = mh.education.Friendships10to12
	result['collegeYears'] = mh.education.collegeYears
	result['collegeDegree'] = mh.education.collegeDegree
	result['collegeMajor'] = mh.education.collegeMajor
	result['advanceDegree'] = mh.education.advanceDegree
	result['tradeSch'] = mh.education.tradeSch
	result['tradeSchool'] = mh.education.tradeSchool
	result['tradeAreaStudy'] = mh.education.tradeAreaStudy
	result['military'] = mh.education.military
	result['militaryBranch'] = mh.education.militaryBranch
	result['militaryYears'] = mh.education.militaryYears
	result['militaryRank'] = mh.education.militaryRank
	result['honorableDischarge'] = mh.education.honorableDischarge

	return result

def getMhBackgroundFields(mh):
	results = {}
	residence = grabMhResidentIndex(mh.background.residence)
	income = grabLowMedHighIndex(mh.background.income)
	debt = grabLowMedHighIndex(mh.background.debt)
	credit = grabMhCreditIndex(mh.background.credit)
	healthCare = grabMhHealthIndex(mh.background.healthCare)
	otherIncome = grabMhOtherIndex(mh.background.otherIncome)
	closeFriendVisit = grabWeeklyIndex(mh.background.closeFriendVisit)
	acqVisit = grabWeeklyIndex(mh.background.acqVisit)

	results['residence'] = residence
	results['income'] = income
	results['debt'] = debt
	results['credit'] = credit
	results['healthCare'] = healthCare
	results['otherIncome'] = otherIncome

	results['spouseRelationship'] = mh.background.spouseRelationship
	results['brothersRelationship'] = mh.background.brothersRelationship
	results['childrenRelationship'] = mh.background.childrenRelationship
	results['parentsRelationship'] = mh.background.parentsRelationship
	results['sistersRelationship'] = mh.background.sistersRelationship
	results['exRelationship'] = mh.background.exRelationship

	results['closeFriendVisit'] = closeFriendVisit
	results['closeFriendNumber'] = mh.background.closeFriendNumber
	results['acqVisit'] = acqVisit
	results['acqNumber'] = mh.background.acqNumber

	results['interest'] = mh.background.interest
	results['interestWeek'] = mh.background.interestWeek
	results['interestMonth'] = mh.background.interestMonth
	results['friendAct'] = mh.background.friendAct
	results['friendActWeek'] = mh.background.friendActWeek
	results['friendActMonth'] = mh.background.friendActMonth
	results['workAct'] = mh.background.workAct
	results['workActWeek'] = mh.background.workActWeek
	results['workActMonth'] = mh.background.workActMonth
	results['churchAffiliation'] = mh.background.churchAffiliation
	results['churchWeek'] = mh.background.churchWeek
	results['churchMonth'] = mh.background.churchMonth
	results['churchYear'] = mh.background.churchYear

	return results

def getMhStressorFields(mh):
	result = {}

	result['deathStress'] = mh.stressors.deathStress
	result['deathStressExp'] = mh.stressors.deathStressExp
	result['divorceStress'] = mh.stressors.divorceStress
	result['divorceStressExp'] = mh.stressors.divorceStressExp
	result['moveStress'] = mh.stressors.moveStress
	result['moveStressExp'] = mh.stressors.moveStressExp
	result['medicalStress'] = mh.stressors.medicalStress
	result['medicalStressExp'] = mh.stressors.medicalStressExp
	result['familyHealthStress'] = mh.stressors.familyHealthStress
	result['familyHealthStressExp'] = mh.stressors.familyHealthStressExp
	result['financialStress'] = mh.stressors.financialStress
	result['financialStressExp'] = mh.stressors.financialStressExp
	result['abuseStress'] = mh.stressors.abuseStress
	result['abuseStressExp'] = mh.stressors.abuseStressExp
	result['addictionFamilyStress'] = mh.stressors.addictionFamilyStress
	result['addictionFamilyStressExp'] = mh.stressors.addictionFamilyStressExp
	result['violenceFamilyStress'] = mh.stressors.violenceFamilyStress
	result['violenceFamilyStressExp'] = mh.stressors.violenceFamilyStressExp
	result['otherStress'] = mh.stressors.otherStress
	result['otherStressExp'] = mh.stressors.otherStressExp

	result['psychiatricHistory'] = mh.stressors.psychiatricHistory

	return result

def getMhFamilyFields(mh):
	result = {}

	## DECODE THE STRINGS
	depressed = decodeMhFamilyText(mh.familyHistory.depressed)
	add = decodeMhFamilyText(mh.familyHistory.add)
	bedWetting = decodeMhFamilyText(mh.familyHistory.bedWetting)
	bipolar = decodeMhFamilyText(mh.familyHistory.bipolar)
	suicideAttempt = decodeMhFamilyText(mh.familyHistory.suicideAttempt)
	physicalAbuse = decodeMhFamilyText(mh.familyHistory.physicalAbuse)
	law = decodeMhFamilyText(mh.familyHistory.law)
	ld = decodeMhFamilyText(mh.familyHistory.ld)
	tic = decodeMhFamilyText(mh.familyHistory.tic)
	thyroid = decodeMhFamilyText(mh.familyHistory.thyroid)
	heart = decodeMhFamilyText(mh.familyHistory.heart)
	overweight = decodeMhFamilyText(mh.familyHistory.overweight)
	mood = decodeMhFamilyText(mh.familyHistory.mood)
	alcohol = decodeMhFamilyText(mh.familyHistory.alcohol)
	drugs = decodeMhFamilyText(mh.familyHistory.drugs)
	schizo = decodeMhFamilyText(mh.familyHistory.schizo)
	seizures = decodeMhFamilyText(mh.familyHistory.seizures)
	completedSuicide = decodeMhFamilyText(mh.familyHistory.completedSuicide)
	sexAbuse = decodeMhFamilyText(mh.familyHistory.sexAbuse)
	panic = decodeMhFamilyText(mh.familyHistory.panic)
	anxiety = decodeMhFamilyText(mh.familyHistory.anxiety)
	OCD = decodeMhFamilyText(mh.familyHistory.OCD)
	diabetes = decodeMhFamilyText(mh.familyHistory.diabetes)
	cancer = decodeMhFamilyText(mh.familyHistory.cancer)
	highBloodPressure = decodeMhFamilyText(mh.familyHistory.highBloodPressure)
	anger = decodeMhFamilyText(mh.familyHistory.anger)

	## SET THE VALUES FOR THE GET FUNCTION
	result['depressedS'] = depressed['side']
	result['depressedM'] = depressed['member']
	result['isdepressed'] = mh.familyHistory.isdepressed
	result['addS'] = add['side']
	result['addM'] = add['member']
	result['isadd'] = mh.familyHistory.isadd
	result['bedWettingS'] = bedWetting['side']
	result['bedWettingM'] = bedWetting['member']
	result['isbedWetting'] = mh.familyHistory.isbedWetting
	result['bipolarS'] = bipolar['side']
	result['bipolarM'] = bipolar['member']
	result['isbipolar'] = mh.familyHistory.isbipolar
	result['suicideAttemptS'] = suicideAttempt['side']
	result['suicideAttemptM'] = suicideAttempt['member']
	result['issuicideAttempt'] = mh.familyHistory.issuicideAttempt
	result['physicalAbuseS'] = physicalAbuse['side']
	result['physicalAbuseM'] = physicalAbuse['member']
	result['isphysicalAbuse'] = mh.familyHistory.isphysicalAbuse
	result['lawS'] = law['side']
	result['lawM'] = law['member']
	result['islaw'] = mh.familyHistory.islaw
	result['ldS'] = ld['side']
	result['ldM'] = ld['member']
	result['isld'] = mh.familyHistory.isld
	result['ticS'] = tic['side']
	result['ticM'] = tic['member']
	result['istic'] = mh.familyHistory.istic
	result['thyroidS'] = thyroid['side']
	result['thyroidM'] = thyroid['member']
	result['isthyroid'] = mh.familyHistory.isthyroid
	result['heartS'] = heart['side']
	result['heartM'] = heart['member']
	result['isheart'] = mh.familyHistory.isheart
	result['overweightS'] = overweight['side']
	result['overweightM'] = overweight['member']
	result['isoverweight'] = mh.familyHistory.isoverweight
	result['moodS'] = mood['side']
	result['moodM'] = mood['member']
	result['ismood'] = mh.familyHistory.ismood
	result['alcoholS'] = alcohol['side']
	result['alcoholM'] = alcohol['member']
	result['isalcohol'] = mh.familyHistory.isalcohol
	result['drugsS'] = drugs['side']
	result['drugsM'] = drugs['member']
	result['isdrugs'] = mh.familyHistory.isdrugs
	result['schizoS'] = schizo['side']
	result['schizoM'] = schizo['member']
	result['isschizo'] = mh.familyHistory.isschizo
	result['seizuresS'] = seizures['side']
	result['seizuresM'] = seizures['member']
	result['isseizures'] = mh.familyHistory.isseizures
	result['completedSuicideS'] = completedSuicide['side']
	result['completedSuicideM'] = completedSuicide['member']
	result['iscompletedSuicide'] = mh.familyHistory.iscompletedSuicide
	result['sexAbuseS'] = sexAbuse['side']
	result['sexAbuseM'] = sexAbuse['member']
	result['issexAbuse'] = mh.familyHistory.issexAbuse
	result['panicS'] = panic['side']
	result['panicM'] = panic['member']
	result['ispanic'] = mh.familyHistory.ispanic
	result['anxietyS'] = anxiety['side']
	result['anxietyM'] = anxiety['member']
	result['isanxiety'] = mh.familyHistory.isanxiety
	result['OCDS'] = OCD['side']
	result['OCDM'] = OCD['member']
	result['isOCD'] = mh.familyHistory.isOCD
	result['diabetesS'] = diabetes['side']
	result['diabetesM'] = diabetes['member']
	result['isdiabetes'] = mh.familyHistory.isdiabetes
	result['cancerS'] = cancer['side']
	result['cancerM'] = cancer['member']
	result['iscancer'] = mh.familyHistory.iscancer
	result['highBloodPressureS'] = highBloodPressure['side']
	result['highBloodPressureM'] = highBloodPressure['member']
	result['ishighBloodPressure'] = mh.familyHistory.ishighBloodPressure
	result['angerS'] = anger['side']
	result['angerM'] = anger['member']
	result['isanger'] = mh.familyHistory.isanger

	return result

def getMhLegalFields(mh):
	result = {}

	result['num_arrest'] = mh.legalHistory.num_arrest
	result['arrestCharges'] = mh.legalHistory.arrestCharges
	result['num_convictions'] = mh.legalHistory.num_convictions
	result['convictionCharges'] = mh.legalHistory.convictionCharges
	result['num_DUI_charges'] = mh.legalHistory.num_DUI_charges
	result['num_DUI_convictions'] = mh.legalHistory.num_DUI_convictions
	result['probationPresent'] = mh.legalHistory.probationPresent
	result['probationPast'] = mh.legalHistory.probationPast
	result['probationOfficer'] = mh.legalHistory.probationOfficer
	result['probationOffense'] = mh.legalHistory.probationOffense
	result['suspendedDrivePresent'] = mh.legalHistory.suspendedDrivePresent
	result['num_suspended'] = mh.legalHistory.num_suspended
	result['hasLawsuit'] = mh.legalHistory.hasLawsuit
	result['lawsuitStress'] = mh.legalHistory.lawsuitStress
	result['inDivorce'] = mh.legalHistory.inDivorce
	result['childCustody'] = mh.legalHistory.childCustody
	result['hasBankrupcy'] = mh.legalHistory.hasBankrupcy
	result['dateBenkrupcy'] = mh.legalHistory.dateBenkrupcy
	result['explainPositiveAnswers'] = mh.legalHistory.explainPositiveAnswers

	return result

def getMhUseFields(mh):
	result = {}

	result['howMuch1'] = mh.useTable.howMuch1
	result['howOften1'] = mh.useTable.howOften1
	result['howLong1'] = mh.useTable.howLong1
	result['howOld1'] = mh.useTable.howOld1
	result['lastTime1'] = mh.useTable.lastTime1
	result['howMuch2'] = mh.useTable.howMuch2
	result['howOften2'] = mh.useTable.howOften2
	result['howLong2'] = mh.useTable.howLong2
	result['howOld2'] = mh.useTable.howOld2
	result['lastTime2'] = mh.useTable.lastTime2
	result['howMuch3'] = mh.useTable.howMuch3
	result['howOften3'] = mh.useTable.howOften3
	result['howLong3'] = mh.useTable.howLong3
	result['howOld3'] = mh.useTable.howOld3
	result['lastTime3'] = mh.useTable.lastTime3
	result['howMuch4'] = mh.useTable.howMuch4
	result['howOften4'] = mh.useTable.howOften4
	result['howLong4'] = mh.useTable.howLong4
	result['howOld4'] = mh.useTable.howOld4
	result['lastTime4'] = mh.useTable.lastTime4
	result['howMuch5'] = mh.useTable.howMuch5
	result['howOften5'] = mh.useTable.howOften5
	result['howLong5'] = mh.useTable.howLong5
	result['howOld5'] = mh.useTable.howOld5
	result['lastTime5'] = mh.useTable.lastTime5
	result['howMuch6'] = mh.useTable.howMuch6
	result['howOften6'] = mh.useTable.howOften6
	result['howLong6'] = mh.useTable.howLong6
	result['howOld6'] = mh.useTable.howOld6
	result['lastTime6'] = mh.useTable.lastTime6
	result['howMuch7'] = mh.useTable.howMuch7
	result['howOften7'] = mh.useTable.howOften7
	result['howLong7'] = mh.useTable.howLong7
	result['howOld7'] = mh.useTable.howOld7
	result['lastTime7'] = mh.useTable.lastTime7
	result['howMuch8'] = mh.useTable.howMuch8
	result['howOften8'] = mh.useTable.howOften8
	result['howLong8'] = mh.useTable.howLong8
	result['howOld8'] = mh.useTable.howOld8
	result['lastTime8'] = mh.useTable.lastTime8
	result['howMuch9'] = mh.useTable.howMuch9
	result['howOften9'] = mh.useTable.howOften9
	result['howLong9'] = mh.useTable.howLong9
	result['howOld9'] = mh.useTable.howOld9
	result['lastTime9'] = mh.useTable.lastTime9
	result['howMuch10'] = mh.useTable.howMuch10
	result['howOften10'] = mh.useTable.howOften10
	result['howLong10'] = mh.useTable.howLong10
	result['howOld10'] = mh.useTable.howOld10
	result['lastTime10'] = mh.useTable.lastTime10
	result['howMuch11'] = mh.useTable.howMuch11
	result['howOften11'] = mh.useTable.howOften11
	result['howLong11'] = mh.useTable.howLong11
	result['howOld11'] = mh.useTable.howOld11
	result['lastTime11'] = mh.useTable.lastTime11
	result['howMuch12'] = mh.useTable.howMuch12
	result['howOften12'] = mh.useTable.howOften12
	result['howLong12'] = mh.useTable.howLong12
	result['howOld12'] = mh.useTable.howOld12
	result['lastTime12'] = mh.useTable.lastTime12
	result['howMuch13'] = mh.useTable.howMuch13
	result['howOften13'] = mh.useTable.howOften13
	result['howLong13'] = mh.useTable.howLong13
	result['howOld13'] = mh.useTable.howOld13
	result['lastTime13'] = mh.useTable.lastTime13
	result['howMuch14'] = mh.useTable.howMuch14
	result['howOften14'] = mh.useTable.howOften14
	result['howLong14'] = mh.useTable.howLong14
	result['howOld14'] = mh.useTable.howOld14
	result['lastTime14'] = mh.useTable.lastTime14
	result['howMuch15'] = mh.useTable.howMuch15
	result['howOften15'] = mh.useTable.howOften15
	result['howLong15'] = mh.useTable.howLong15
	result['howOld15'] = mh.useTable.howOld15
	result['lastTime15'] = mh.useTable.lastTime15
	result['howMuch16'] = mh.useTable.howMuch16
	result['howOften16'] = mh.useTable.howOften16
	result['howLong16'] = mh.useTable.howLong16
	result['howOld16'] = mh.useTable.howOld16
	result['lastTime16'] = mh.useTable.lastTime16
	result['howMuch17'] = mh.useTable.howMuch17
	result['howOften17'] = mh.useTable.howOften17
	result['howLong17'] = mh.useTable.howLong17
	result['howOld17'] = mh.useTable.howOld17
	result['lastTime17'] = mh.useTable.lastTime17
	result['howMuch18'] = mh.useTable.howMuch18
	result['howOften18'] = mh.useTable.howOften18
	result['howLong18'] = mh.useTable.howLong18
	result['howOld18'] = mh.useTable.howOld18
	result['lastTime18'] = mh.useTable.lastTime18
	result['howMuch19'] = mh.useTable.howMuch19
	result['howOften19'] = mh.useTable.howOften19
	result['howLong19'] = mh.useTable.howLong19
	result['howOld19'] = mh.useTable.howOld19
	result['lastTime19'] = mh.useTable.lastTime19
	result['howMuch20'] = mh.useTable.howMuch20
	result['howOften20'] = mh.useTable.howOften20
	result['howLong20'] = mh.useTable.howLong20
	result['howOld20'] = mh.useTable.howOld20
	result['lastTime20'] = mh.useTable.lastTime20
	result['howMuch21'] = mh.useTable.howMuch21
	result['howOften21'] = mh.useTable.howOften21
	result['howLong21'] = mh.useTable.howLong21
	result['howOld21'] = mh.useTable.howOld21
	result['lastTime21'] = mh.useTable.lastTime21

	return result

def getMhFields(mh, section):
	result = {}

	if str(section) == '/mh_demographic/':
		result = getMhDemoFields(mh)
	elif str(section) == '/mh_education/':
		result = getMhEducationFields(mh)
	elif str(section) == '/mh_background/':
		result = getMhBackgroundFields(mh)
	elif str(section) == '/mh_stress/':
		result = getMhStressorFields(mh)
	elif str(section) == '/mh_familyHistory/':
		result = getMhFamilyFields(mh)
	elif str(section) == '/mh_legal/':
		result = getMhLegalFields(mh)
	elif str(section) == '/mh_useTable/':
		result = getMhUseFields(mh)

	return result


def saveMhDemo(request, mh):
	momLive = request.POST.get('motherLiving', '')
	dadLive  =request.POST.get('fatherLiving', '')
	momLive = truePythonBool(momLive)
	dadLive = truePythonBool(dadLive)

	mh.demographics.birthplace 			= request.POST.get('birthplace', '')
	mh.demographics.raised 				= request.POST.get('raised', '')
	mh.demographics.maritalStatus 		= request.POST.get('maritalStatus', '')
	mh.demographics.numMarriages 		= request.POST.get('m_numMarriages', '')
	mh.demographics.occupation 			= request.POST.get('occupation', '')
	mh.demographics.employer 			= request.POST.get('employer', '')
	mh.demographics.employedMo 			= request.POST.get('employedMo', '')
	mh.demographics.employedYrs 		= request.POST.get('employedYrs', '')
	mh.demographics.pastJobs 			= request.POST.get('pastJobs', '')
	mh.demographics.recentMove 			= request.POST.get('recentMove', '')
	mh.demographics.spouseAge 			= request.POST.get('m_spouseAge', '')
	mh.demographics.spouseOccupation 	= request.POST.get('m_spouseOccupation', '')
	mh.demographics.spouseEmployer 		= request.POST.get('m_spouseEmployer', '')
	mh.demographics.spouseWorkMos 		= request.POST.get('m_spouseWorkMos', '')
	mh.demographics.spouseWorkYrs 		= request.POST.get('m_spouseWorkYrs', '')
	mh.demographics.motherOccupation 	= request.POST.get('motherOccupation', '')
	mh.demographics.motherCity 			= request.POST.get('motherCity', '')
	mh.demographics.motherState 		= request.POST.get('motherState', '')
	mh.demographics.motherLiving 		= momLive
	mh.demographics.motherAge 			= request.POST.get('m_motherAge', '')
	mh.demographics.motherAgeDeath 		= request.POST.get('m_motherAgeDeath', '')
	mh.demographics.fatherOccupation 	= request.POST.get('fatherOccupation', '')
	mh.demographics.fatherCity 			= request.POST.get('fatherCity', '')
	mh.demographics.fatherState 		= request.POST.get('fatherState', '')
	mh.demographics.fatherLiving 		= dadLive
	mh.demographics.fatherAge 			= request.POST.get('m_fatherAge', '')
	mh.demographics.fatherAgeDeath 		= request.POST.get('m_fatherAgeDeath', '')
	mh.demographics.numChildren 		= request.POST.get('m_numChildren', '')
	mh.demographics.numSisters 			= request.POST.get('m_numSisters', '')
	mh.demographics.numBrothers 		= request.POST.get('m_numBrothers', '')

	mh.demographics.save()

def saveMhEducation(request, mh):
	mh.education.GradesKto6 			= request.POST.get('GradesKto6')
	mh.education.Grades7to9 			= request.POST.get('Grades7to9')
	mh.education.Grades10to12 			= request.POST.get('Grades10to12')
	mh.education.BehaviorProblemsKto6 	= truePythonBool(request.POST.get('BehaviorProblemsKto6'))
	mh.education.AcademicProblemsKto6 	= truePythonBool(request.POST.get('AcademicProblemsKto6'))
	mh.education.BehaviorProblems7to9 	= truePythonBool(request.POST.get('BehaviorProblems7to9'))
	mh.education.AcademicProblems7to9 	= truePythonBool(request.POST.get('AcademicProblems7to9'))
	mh.education.BehaviorProblems10to12 = truePythonBool(request.POST.get('BehaviorProblems10to12'))
	mh.education.AcademicProblems10to12 = truePythonBool(request.POST.get('AcademicProblems10to12'))
	mh.education.FriendshipsKto6 		= request.POST.get('m_FriendshipsKto6')
	mh.education.Friendships7to9 		= request.POST.get('m_Friendships7to9')
	mh.education.Friendships10to12		= request.POST.get('m_Friendships10to12')
	mh.education.collegeYears 			= request.POST.get('collegeYears')
	mh.education.collegeDegree 			= truePythonBool(request.POST.get('collegeDegree'))
	mh.education.collegeMajor 			= request.POST.get('m_collegeMajor')
	mh.education.advanceDegree 			= truePythonBool(request.POST.get('m_advanceDegree'))
	mh.education.tradeSch 				= truePythonBool(request.POST.get('tradeSch'))
	mh.education.tradeSchool 			= request.POST.get('m_tradeSchool')
	mh.education.tradeAreaStudy 		= request.POST.get('m_tradeAreaStudy')
	mh.education.military 				= truePythonBool(request.POST.get('military'))	
	mh.education.militaryBranch 		= request.POST.get('m_militaryBranch')
	mh.education.militaryRank 			= request.POST.get('m_militaryRank')
	mh.education.militaryYears 			= request.POST.get('m_militaryYears')
	mh.education.honorableDischarge 	= truePythonBool(request.POST.get('m_honorableDischarge'))

	mh.education.save()

def saveMhBackground(request, mh):
	mh.background.residence 				= request.POST.get('residence')
	mh.background.income 					= request.POST.get('income')
	mh.background.debt 						= request.POST.get('debt')
	mh.background.credit 					= request.POST.get('credit')
	mh.background.healthCare 				= request.POST.get('healthCare')
	mh.background.otherIncome 				= request.POST.get('otherIncome')
	mh.background.spouseRelationship 		= request.POST.get('spouseRelationship')
	mh.background.brothersRelationship 		= request.POST.get('brothersRelationship')
	mh.background.childrenRelationship 		= request.POST.get('childrenRelationship')
	mh.background.parentsRelationship 		= request.POST.get('parentsRelationship')
	mh.background.sistersRelationship 		= request.POST.get('sistersRelationship')
	mh.background.exRelationship 			= request.POST.get('exRelationship')
	mh.background.closeFriendVisit 			= request.POST.get('closeFriendVisit')
	mh.background.closeFriendNumber 		= request.POST.get('closeFriendNumber')
	mh.background.acqVisit 					= request.POST.get('acqVisit')
	mh.background.acqNumber 				= request.POST.get('acqNumber')
	mh.background.interest 					= request.POST.get('interest')
	mh.background.interestWeek 				= request.POST.get('interestWeek')
	mh.background.interestMonth 			= request.POST.get('interestMonth')
	mh.background.friendAct 				= request.POST.get('friendAct')
	mh.background.friendActWeek 			= request.POST.get('friendActWeek')
	mh.background.friendActMonth 			= request.POST.get('friendActMonth')
	mh.background.workAct 					= request.POST.get('workAct')
	mh.background.workActWeek 				= request.POST.get('workActWeek')
	mh.background.workActMonth 				= request.POST.get('workActMonth')
	mh.background.churchAffiliation 		= request.POST.get('churchAffiliation')
	mh.background.churchWeek 				= request.POST.get('churchWeek')
	mh.background.churchMonth 				= request.POST.get('churchMonth')
	mh.background.churchYear 				= request.POST.get('churchYear')

	mh.background.save()

def saveMhStress(request, mh):
	mh.stressors.deathStress 			= truePythonBool(request.POST.get('deathStress'));
	mh.stressors.divorceStress 			= truePythonBool(request.POST.get('divorceStress'));
	mh.stressors.moveStress 			= truePythonBool(request.POST.get('moveStress'));
	mh.stressors.medicalStress 			= truePythonBool(request.POST.get('medicalStress'));
	mh.stressors.familyHealthStress 	= truePythonBool(request.POST.get('familyHealthStress'));
	mh.stressors.financialStress 		= truePythonBool(request.POST.get('financialStress'));
	mh.stressors.addictionFamilyStress 	= truePythonBool(request.POST.get('addictionFamilyStress'));
	mh.stressors.violenceFamilyStress 	= truePythonBool(request.POST.get('violenceFamilyStress'));
	mh.stressors.otherStress 			= truePythonBool(request.POST.get('otherStress'));
	mh.stressors.abuseStress 			= truePythonBool(request.POST.get('abuseStress'));

	mh.stressors.deathStressExp 			= request.POST.get('m_deathStressExp');
	mh.stressors.divorceStressExp 			= request.POST.get('m_divorceStressExp');
	mh.stressors.moveStressExp 				= request.POST.get('m_moveStressExp');
	mh.stressors.medicalStressExp 			= request.POST.get('m_medicalStressExp');
	mh.stressors.familyHealthStressExp 		= request.POST.get('m_familyHealthStressExp');
	mh.stressors.financialStressExp 		= request.POST.get('m_financialStressExp');
	mh.stressors.abuseStressExp 			= request.POST.get('m_abuseStressExp');
	mh.stressors.addictionFamilyStressExp 	= request.POST.get('m_addictionFamilyStressExp');
	mh.stressors.violenceFamilyStressExp 	= request.POST.get('m_violenceFamilyStressExp');
	mh.stressors.otherStressExp 			= request.POST.get('m_otherStressExp');

	mh.stressors.save()

def saveMhFamily(request, mh):
	mh.familyHistory.isdepressed 			= truePythonBool(request.POST.get('isdepressed'))
	mh.familyHistory.isadd 					= truePythonBool(request.POST.get('isadd'))
	mh.familyHistory.isbedWetting 			= truePythonBool(request.POST.get('isbedWetting'))
	mh.familyHistory.isbipolar 				= truePythonBool(request.POST.get('isbipolar'))
	mh.familyHistory.issuicideAttempt 		= truePythonBool(request.POST.get('issuicideAttempt'))
	mh.familyHistory.isphysicalAbuse 		= truePythonBool(request.POST.get('isphysicalAbuse'))
	mh.familyHistory.islaw 					= truePythonBool(request.POST.get('islaw'))
	mh.familyHistory.isld 					= truePythonBool(request.POST.get('isld'))
	mh.familyHistory.istic 					= truePythonBool(request.POST.get('istic'))
	mh.familyHistory.isthyroid 				= truePythonBool(request.POST.get('isthyroid'))
	mh.familyHistory.isheart 				= truePythonBool(request.POST.get('isheart'))
	mh.familyHistory.isoverweight 			= truePythonBool(request.POST.get('isoverweight'))
	mh.familyHistory.ismood 				= truePythonBool(request.POST.get('ismood'))
	mh.familyHistory.isalcohol 				= truePythonBool(request.POST.get('isalcohol'))
	mh.familyHistory.isdrugs 				= truePythonBool(request.POST.get('isdrugs'))
	mh.familyHistory.isschizo 				= truePythonBool(request.POST.get('isschizo'))
	mh.familyHistory.isseizures 			= truePythonBool(request.POST.get('isseizures'))
	mh.familyHistory.iscompletedSuicide 	= truePythonBool(request.POST.get('iscompletedSuicide'))
	mh.familyHistory.issexAbuse 			= truePythonBool(request.POST.get('issexAbuse'))
	mh.familyHistory.ispanic 				= truePythonBool(request.POST.get('ispanic'))
	mh.familyHistory.isanxiety 				= truePythonBool(request.POST.get('isanxiety'))
	mh.familyHistory.isOCD 					= truePythonBool(request.POST.get('isOCD'))
	mh.familyHistory.isdiabetes 			= truePythonBool(request.POST.get('isdiabetes'))
	mh.familyHistory.iscancer 				= truePythonBool(request.POST.get('iscancer'))
	mh.familyHistory.ishighBloodPressure 	= truePythonBool(request.POST.get('ishighBloodPressure'))
	mh.familyHistory.isanger 				= truePythonBool(request.POST.get('isanger'))

	mh.familyHistory.depressed 			= request.POST.get('depressed')
	mh.familyHistory.add 				= request.POST.get('add')
	mh.familyHistory.bedWetting 		= request.POST.get('bedWetting')
	mh.familyHistory.bipolar 			= request.POST.get('bipolar')
	mh.familyHistory.suicideAttempt 	= request.POST.get('suicideAttempt')
	mh.familyHistory.physicalAbuse 		= request.POST.get('physicalAbuse')
	mh.familyHistory.law 				= request.POST.get('law')
	mh.familyHistory.ld 				= request.POST.get('ld')
	mh.familyHistory.tic 				= request.POST.get('tic')
	mh.familyHistory.thyroid 			= request.POST.get('thyroid')
	mh.familyHistory.heart 				= request.POST.get('heart')
	mh.familyHistory.overweight 		= request.POST.get('overweight')
	mh.familyHistory.mood 				= request.POST.get('mood')
	mh.familyHistory.alcohol 			= request.POST.get('alcohol')
	mh.familyHistory.drugs 				= request.POST.get('drugs')
	mh.familyHistory.schizo 			= request.POST.get('schizo')
	mh.familyHistory.seizures 			= request.POST.get('seizures')
	mh.familyHistory.completedSuicide 	= request.POST.get('completedSuicide')
	mh.familyHistory.sexAbuse 			= request.POST.get('sexAbuse')
	mh.familyHistory.panic 				= request.POST.get('panic')
	mh.familyHistory.anxiety 			= request.POST.get('anxiety')	
	mh.familyHistory.OCD 				= request.POST.get('OCD')
	mh.familyHistory.diabetes 			= request.POST.get('diabetes')
	mh.familyHistory.cancer 			= request.POST.get('cancer')
	mh.familyHistory.highBloodPressure 	= request.POST.get('highBloodPressure')
	mh.familyHistory.anger 				= request.POST.get('anger')

	mh.familyHistory.save()

def saveMhLegal(request, mh):
	mh.legalHistory.num_arrest = request.POST.get('num_arrest')
	mh.legalHistory.arrestCharges = request.POST.get('arrestCharges')
	mh.legalHistory.num_convictions = request.POST.get('num_convictions')
	mh.legalHistory.convictionCharges = request.POST.get('convictionCharges')
	mh.legalHistory.probationPresent = truePythonBool(request.POST.get('probationPresent'))
	mh.legalHistory.probationPast = truePythonBool(request.POST.get('probationPast'))
	mh.legalHistory.num_DUI_charges = request.POST.get('num_DUI_charges')
	mh.legalHistory.num_DUI_convictions = request.POST.get('num_DUI_convictions')
	mh.legalHistory.suspendedDrivePresent = truePythonBool(request.POST.get('suspendedDrivePresent'))
	mh.legalHistory.num_suspended = request.POST.get('num_suspended')
	mh.legalHistory.hasLawsuit = truePythonBool(request.POST.get('hasLawsuit'))
	mh.legalHistory.inDivorce = truePythonBool(request.POST.get('inDivorce'))
	mh.legalHistory.childCustody = truePythonBool(request.POST.get('childCustody'))
	mh.legalHistory.hasBankrupcy = truePythonBool(request.POST.get('hasBankrupcy'))
	mh.legalHistory.explainPositiveAnswers = request.POST.get('explainPositiveAnswers')
	mh.legalHistory.probationOfficer = request.POST.get('m_probationOfficer')
	mh.legalHistory.probationOffense = request.POST.get('m_probationOffense')
	mh.legalHistory.lawsuitStress = request.POST.get('m_lawsuitStress')
	mh.legalHistory.dateBenkrupcy = request.POST.get('m_dateBenkrupcy')

	mh.legalHistory.save()

def saveMhPsych(request, mh):
	mh.stressors.psychiatricHistory = request.POST.get('psychiatricHistory')
	mh.stressors.save()

def saveMhUse(request, mh):
	mh.useTable.howMuch1 = request.POST.get('howMuch1')
	mh.useTable.howMuch2 = request.POST.get('howMuch2')
	mh.useTable.howMuch3 = request.POST.get('howMuch3')
	mh.useTable.howMuch4 = request.POST.get('howMuch4')
	mh.useTable.howMuch5 = request.POST.get('howMuch5')
	mh.useTable.howMuch6 = request.POST.get('howMuch6')
	mh.useTable.howMuch7 = request.POST.get('howMuch7')
	mh.useTable.howMuch8 = request.POST.get('howMuch8')
	mh.useTable.howMuch9 = request.POST.get('howMuch9')
	mh.useTable.howMuch10 = request.POST.get('howMuch10')
	mh.useTable.howMuch11 = request.POST.get('howMuch11')
	mh.useTable.howMuch12 = request.POST.get('howMuch12')
	mh.useTable.howMuch13 = request.POST.get('howMuch13')
	mh.useTable.howMuch14 = request.POST.get('howMuch14')
	mh.useTable.howMuch15 = request.POST.get('howMuch15')
	mh.useTable.howMuch16 = request.POST.get('howMuch16')
	mh.useTable.howMuch17 = request.POST.get('howMuch17')
	mh.useTable.howMuch18 = request.POST.get('howMuch18')
	mh.useTable.howMuch19 = request.POST.get('howMuch19')
	mh.useTable.howMuch20 = request.POST.get('howMuch20')
	mh.useTable.howMuch21 = request.POST.get('howMuch21')

	mh.useTable.howOften1 = request.POST.get('howOften1')
	mh.useTable.howOften2 = request.POST.get('howOften2')
	mh.useTable.howOften3 = request.POST.get('howOften3')
	mh.useTable.howOften4 = request.POST.get('howOften4')
	mh.useTable.howOften5 = request.POST.get('howOften5')
	mh.useTable.howOften6 = request.POST.get('howOften6')
	mh.useTable.howOften7 = request.POST.get('howOften7')
	mh.useTable.howOften8 = request.POST.get('howOften8')
	mh.useTable.howOften9 = request.POST.get('howOften9')
	mh.useTable.howOften10 = request.POST.get('howOften10')
	mh.useTable.howOften11 = request.POST.get('howOften11')
	mh.useTable.howOften12 = request.POST.get('howOften12')
	mh.useTable.howOften13 = request.POST.get('howOften13')
	mh.useTable.howOften14 = request.POST.get('howOften14')
	mh.useTable.howOften15 = request.POST.get('howOften15')
	mh.useTable.howOften16 = request.POST.get('howOften16')
	mh.useTable.howOften17 = request.POST.get('howOften17')
	mh.useTable.howOften18 = request.POST.get('howOften18')
	mh.useTable.howOften19 = request.POST.get('howOften19')
	mh.useTable.howOften20 = request.POST.get('howOften20')
	mh.useTable.howOften21 = request.POST.get('howOften21')

	mh.useTable.howLong1 = request.POST.get('howLong1')
	mh.useTable.howLong2 = request.POST.get('howLong2')
	mh.useTable.howLong3 = request.POST.get('howLong3')
	mh.useTable.howLong4 = request.POST.get('howLong4')
	mh.useTable.howLong5 = request.POST.get('howLong5')
	mh.useTable.howLong6 = request.POST.get('howLong6')
	mh.useTable.howLong7 = request.POST.get('howLong7')
	mh.useTable.howLong8 = request.POST.get('howLong8')
	mh.useTable.howLong9 = request.POST.get('howLong9')
	mh.useTable.howLong10 = request.POST.get('howLong10')
	mh.useTable.howLong11 = request.POST.get('howLong11')
	mh.useTable.howLong12 = request.POST.get('howLong12')
	mh.useTable.howLong13 = request.POST.get('howLong13')
	mh.useTable.howLong14 = request.POST.get('howLong14')
	mh.useTable.howLong15 = request.POST.get('howLong15')
	mh.useTable.howLong16 = request.POST.get('howLong16')
	mh.useTable.howLong17 = request.POST.get('howLong17')
	mh.useTable.howLong18 = request.POST.get('howLong18')
	mh.useTable.howLong19 = request.POST.get('howLong19')
	mh.useTable.howLong20 = request.POST.get('howLong20')
	mh.useTable.howLong21 = request.POST.get('howLong21')

	mh.useTable.howOld1 = request.POST.get('howOld1')
	mh.useTable.howOld2 = request.POST.get('howOld2')
	mh.useTable.howOld3 = request.POST.get('howOld3')
	mh.useTable.howOld4 = request.POST.get('howOld4')
	mh.useTable.howOld5 = request.POST.get('howOld5')
	mh.useTable.howOld6 = request.POST.get('howOld6')
	mh.useTable.howOld7 = request.POST.get('howOld7')
	mh.useTable.howOld8 = request.POST.get('howOld8')
	mh.useTable.howOld9 = request.POST.get('howOld9')
	mh.useTable.howOld10 = request.POST.get('howOld10')
	mh.useTable.howOld11 = request.POST.get('howOld11')
	mh.useTable.howOld12 = request.POST.get('howOld12')
	mh.useTable.howOld13 = request.POST.get('howOld13')
	mh.useTable.howOld14 = request.POST.get('howOld14')
	mh.useTable.howOld15 = request.POST.get('howOld15')
	mh.useTable.howOld16 = request.POST.get('howOld16')
	mh.useTable.howOld17 = request.POST.get('howOld17')
	mh.useTable.howOld18 = request.POST.get('howOld18')
	mh.useTable.howOld19 = request.POST.get('howOld19')
	mh.useTable.howOld20 = request.POST.get('howOld20')
	mh.useTable.howOld21 = request.POST.get('howOld21')

	mh.useTable.lastTime1 = request.POST.get('lastTime1')
	mh.useTable.lastTime2 = request.POST.get('lastTime2')
	mh.useTable.lastTime3 = request.POST.get('lastTime3')
	mh.useTable.lastTime4 = request.POST.get('lastTime4')
	mh.useTable.lastTime5 = request.POST.get('lastTime5')
	mh.useTable.lastTime6 = request.POST.get('lastTime6')
	mh.useTable.lastTime7 = request.POST.get('lastTime7')
	mh.useTable.lastTime8 = request.POST.get('lastTime8')
	mh.useTable.lastTime9 = request.POST.get('lastTime9')
	mh.useTable.lastTime10 = request.POST.get('lastTime10')
	mh.useTable.lastTime11 = request.POST.get('lastTime11')
	mh.useTable.lastTime12 = request.POST.get('lastTime12')
	mh.useTable.lastTime13 = request.POST.get('lastTime13')
	mh.useTable.lastTime14 = request.POST.get('lastTime14')
	mh.useTable.lastTime15 = request.POST.get('lastTime15')
	mh.useTable.lastTime16 = request.POST.get('lastTime16')
	mh.useTable.lastTime17 = request.POST.get('lastTime17')
	mh.useTable.lastTime18 = request.POST.get('lastTime18')
	mh.useTable.lastTime19 = request.POST.get('lastTime19')
	mh.useTable.lastTime20 = request.POST.get('lastTime20')
	mh.useTable.lastTime21 = request.POST.get('lastTime21')

	mh.useTable.save()

def saveMentalHealth(request, section, mh):
	if str(section) == '/mh_demographic/':
		saveMhDemo(request, mh)
	elif str(section) == '/mh_education/':
		saveMhEducation(request, mh)
	elif str(section) == '/mh_background/':
		saveMhBackground(request, mh)
	elif str(section) == '/mh_stress/':
		saveMhStress(request, mh)
	elif str(section) == '/mh_familyHistory/':
		saveMhFamily(request, mh)
	elif str(section) == '/mh_legal/':
		saveMhLegal(request, mh)
	elif str(section) == '/mh_psych/':
		saveMhPsych(request, mh)
	elif str(section) == '/mh_useTable/':
		saveMhUse(request, mh)

def refreshMhDemo(mh):
	mh.demographics.birthplace = None
	mh.demographics.raised = None
	mh.demographics.maritalStatus = None
	mh.demographics.numMarriages = 0
	mh.demographics.occupation = ''
	mh.demographics.employer = ''
	mh.demographics.employedMo = 0
	mh.demographics.employedYrs = 0
	mh.demographics.pastJobs = ''
	mh.demographics.recentMove = ''
	mh.demographics.spouseAge = 0
	mh.demographics.spouseOccupation = ''
	mh.demographics.spouseEmployer = ''
	mh.demographics.spouseWorkMos = 0
	mh.demographics.spouseWorkYrs = 0
	mh.demographics.childrenMale = ''
	mh.demographics.childrenFemale = ''
	mh.demographics.bothers = ''
	mh.demographics.sisters = ''
	mh.demographics.motherOccupation = ''
	mh.demographics.motherCity = ''
	mh.demographics.motherState = ''
	mh.demographics.motherLiving = False
	mh.demographics.motherAge = 0
	mh.demographics.motherAgeDeath = 0
	mh.demographics.fatherOccupation = ''
	mh.demographics.fatherCity = ''
	mh.demographics.fatherState = ''
	mh.demographics.fatherLiving = False
	mh.demographics.fatherAge = 0
	mh.demographics.fatherAgeDeath = 0
	mh.demographics.numChildren = 0
	mh.demographics.numSisters = 0
	mh.demographics.numBrothers = 0
	mh.demographics.save()

def refreshEdu(mh):
	result = mh
	mh.education.GradesKto6 = ''
	mh.education.BehaviorProblemsKto6 = False
	mh.education.AcademicProblemsKto6 = False
	mh.education.FriendshipsKto6 = 0
	mh.education.Grades7to9 = ''
	mh.education.BehaviorProblems7to9 = False
	mh.education.AcademicProblems7to9 = False
	mh.education.Friendships7to9 = 0
	mh.education.Grades10to12 = ''
	mh.education.BehaviorProblems10to12 = False
	mh.education.AcademicProblems10to12 = False
	mh.education.Friendships10to12 = 0
	mh.education.collegeYears = 0
	mh.education.collegeDegree = False
	mh.education.collegeMajor = ''
	mh.education.advanceDegree = False
	mh.education.tradeSch = ''
	mh.education.tradeSchool = False
	mh.education.tradeAreaStudy = ''
	mh.education.military = False
	mh.education.militaryBranch = ''
	mh.education.militaryYears = 0
	mh.education.militaryRank = ''
	mh.education.honorableDischarge = ''
	mh.education.save()
	return result

def refreshBack(mh):
	result = mh
	mh.background.closeFriendNumber = 0
	mh.background.acqNumber = 0
	mh.background.interestWeek = 0
	mh.background.interestMonth = 0
	mh.background.friendActWeek = 0
	mh.background.friendActMonth = 0
	mh.background.workActWeek = 0
	mh.background.workActMonth = 0
	mh.background.churchWeek = 0
	mh.background.churchMonth = 0
	mh.background.churchYear = 0	
	mh.background.residence = ''
	mh.background.income = ''
	mh.background.debt = ''
	mh.background.credit = ''
	mh.background.healthCare = ''
	mh.background.otherIncome = ''
	mh.background.spouseRelationship = ''
	mh.background.brothersRelationship = ''
	mh.background.childrenRelationship = ''
	mh.background.parentsRelationship = ''
	mh.background.sistersRelationship = ''
	mh.background.exRelationship = ''
	mh.background.closeFriendVisit = ''
	mh.background.acqVisit = ''
	mh.background.interest = ''
	mh.background.friendAct = ''
	mh.background.workAct = ''
	mh.background.churchAffiliation = ''
	mh.background.save()
	return result

def refreshMhStress(mh):
	result = mh
	mh.stressors.deathStressExp = ''
	mh.stressors.divorceStressExp = ''
	mh.stressors.moveStressExp = ''
	mh.stressors.medicalStressExp = ''
	mh.stressors.familyHealthStressExp = ''
	mh.stressors.financialStressExp = ''
	mh.stressors.abuseStressExp = ''
	mh.stressors.addictionFamilyStressExp = ''
	mh.stressors.violenceFamilyStressExp = ''
	mh.stressors.otherStressExp = ''
	mh.stressors.psychiatricHistory = ''
	mh.stressors.deathStress = False
	mh.stressors.divorceStress = False
	mh.stressors.moveStress = False
	mh.stressors.medicalStress = False
	mh.stressors.familyHealthStress = False
	mh.stressors.financialStress = False
	mh.stressors.abuseStress = False
	mh.stressors.addictionFamilyStress = False
	mh.stressors.violenceFamilyStress = False
	mh.stressors.otherStress = False
	mh.stressors.save()
	return result

def refreshMhFam(mh):
	THEclientID = mh.client.clientID
	newFam = MHFamilyHistory(clientID=THEclientID)
	oldFam = mh.familyHistory
	newFam.save()
	mh.familyHistory = newFam
	mh.save()	
	oldFam.delete()

def refreshMhLegal(mh):
	result = mh
	mh.legalHistory.num_arrest = 0
	mh.legalHistory.num_convictions = 0
	mh.legalHistory.num_DUI_charges = 0
	mh.legalHistory.num_DUI_convictions = 0
	mh.legalHistory.num_suspended = 0
	mh.legalHistory.arrestCharges = ''
	mh.legalHistory.convictionCharges = ''
	mh.legalHistory.probationOfficer = ''
	mh.legalHistory.probationOffense = ''
	mh.legalHistory.dateBenkrupcy = ''
	mh.legalHistory.explainPositiveAnswers = ''
	mh.legalHistory.probationPresent = False
	mh.legalHistory.probationPast = False
	mh.legalHistory.suspendedDrivePresent = False
	mh.legalHistory.hasLawsuit = False
	mh.legalHistory.lawsuitStress = False
	mh.legalHistory.inDivorce = False
	mh.legalHistory.childCustody = False
	mh.legalHistory.hasBankrupcy = False
	mh.legalHistory.save()
	return result

def refreshMhUse(mh):	
	THEclientID = mh.client.clientID
	newUse = MHUseTable(clientID=THEclientID)
	oldUse = mh.useTable
	newUse.save()
	mh.useTable = newUse
	mh.save()
	oldUse.delete()

def refreshMh(mh):
	refreshMhDemo(mh)
	refreshEdu(mh)
	refreshBack(mh)
	refreshMhStress(mh)
	refreshMhFam(mh)
	refreshMhLegal(mh)
	# refreshMhPsy(mh)
	refreshMhUse(mh)

	mh.demographicsComplete = False
	mh.educationComplete = False
	mh.backgroundComplete = False
	mh.stressorComplete = False
	mh.familyComplete = False
	mh.legalComplete = False
	mh.psychComplete = False
	mh.useComplete = False
	mh.demoPriority = False
	mh.educationPriority = False
	mh.backgroundPriority = False
	mh.stressPriority = False
	mh.familyPriority = False
	mh.legalPriority = False
	mh.psychPriority = False
	mh.usePriority = False
	mh.MHComplete = False
	mh.save()

def deleteMh(mh):
	result = mh
	mh.demographics.delete()
	mh.education.delete()
	mh.background.delete()
	mh.stressors.delete()
	mh.familyHistory.delete()
	mh.legalHistory.delete()
	mh.useTable.delete()
	mh.delete()
	return result

def mhDemo_priority(mh):
	mh.demoPriority 		= True
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False

def mhEdu_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= True
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False

def mhBack_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= True
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False

def mhStress_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= True
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False

def mhFamily_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= True
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False

def mhLegal_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= True
	mh.psychPriority 		= False
	mh.usePriority 			= False

def mhPsych_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= True
	mh.usePriority 			= False

def mhUse_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= True

def deprioritizeMH(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= True

def setMhPriority(mh, section):
	section = str(section)

	if section == '/mh_demographic/':
		mhDemo_priority(mh)
	elif section == '/mh_education/':
		mhEdu_priority(mh)
	elif section == '/mh_background/':
		mhBack_priority(mh)
	elif section == '/mh_stress/':
		mhStress_priority(mh)
	elif section == '/mh_familyHistory/':
		mhFamily_priority(mh)
	elif section == '/mh_legal/':
		mhLegal_priority(mh)
	elif section == '/mh_psych/':
		mhPsych_priority(mh)
	elif section == '/mh_useTable/':
		mhUse_priority(mh)

def finishMhSection(mh, section):
	section = str(section)

	if section == '/mh_demographic/':
		mh.demographicsComplete = True
	elif section == '/mh_education/':
		mh.educationComplete = True
	elif section == '/mh_background/':
		mh.backgroundComplete = True
	elif section == '/mh_stress/':
		mh.stressorComplete = True
	elif section == '/mh_familyHistory/':
		mh.familyComplete = True
	elif section == '/mh_legal/':
		mh.legalComplete = True
	elif section == '/mh_psych/':
		mh.psychComplete = True
	elif section == '/mh_useTable/':
		mh.useComplete = True

	mh.save()

def processMhData(request, current_section):
	result = {}

	session_id = request.POST.get('session_id', '')
	mh_id = request.POST.get('mh_id', '')
	save_this = request.POST.get('save_this', '')
	section = request.POST.get('save_section', '')

	session = ClientSession.objects.get(id=session_id)
	mh = MentalHealth.objects.get(id=mh_id)
	deprioritizeMH(mh)
	fields = getMhFields(mh, current_section)
	json_data = json.dumps(fields)

	if current_section == '/mh_demographic/':
		states = State.objects.all().order_by('state')
		result['states'] = states

	if save_this == 'true':
		saveMentalHealth(request, section, mh)
		finishMhSection(mh, section)

	next_url = nextMhPage(mh, current_section)
	image = grabMhSideImages(mh, current_section)
	classes = grabMhClassesCSS(mh, current_section)

	result['class'] = classes
	result['image'] = image
	result['next_url'] = next_url
	result['session'] = session
	result['mh'] = mh
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | Mental Health Assessment"

	return result


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
################################################################# END MH ##################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



###########################################################################################################################################
#*****************************************************************************************************************************************#
#---------------------------------------------------------------- ASI VIEWS --------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


def isJQnumber(din):
	din = str(din)
	isNumber = False
	if din[0]=='1' or din[0]=='2' or din[0]=='3' or din[0]=='4' or din[0]=='5' or din[0]=='6' or din[0]=='7' or din[0]=='8' or din[0]=='9' or din[0]=='0':
		isNumber = True
	return isNumber

def process_jq_year(year):
	year = str(year)
	result = ''
	result += year[0]
	result += year[1]
	result += year[2]
	result += year[3]
	return result

def process_jq_day(day):
	day = str(day)
	result = ''

	if len(day) == 2:
		result += '0'
		result += day[0]
	else:
		result += day[0]
		result += day[1]
	return result

def break_up_jq_str_date(din):
	result = {}
	day = ''
	month =''
	year = ''
	flag1 = 0
	flag2 = 0

	for i in range(len(din)):
		if din[i] != ' ':
			month += din[i]
		else:
			flag1 = i + 1
			break

	for j in range(flag1, len(din)):
		if din[j] != ' ':
			day += din[j]
		else:
			flag2 = j + 1
			break

	for k in range(flag2, len(din)):
		year += din[k]

	result['month'] = month
	result['day'] = day
	result['year'] = year
	return result

def get_first3_jq(din):
	result = ''
	result += str(din[0])
	result += str(din[1])
	result += str(din[2])
	return result

def jq_month_to_int(din):
	result = None
	din = get_first3_jq(din)
	din = str(din)

	if din == 'Jan':
		result = '01'
	elif din == 'Feb':
		result = '02'
	elif din == 'Mar':
		result = '03'
	elif din == 'Apr':
		result = '04'
	elif din == 'May':
		result = '05'
	elif din == 'Jun':
		result = '06'
	elif din == 'Jul':
		result = '07'
	elif din == 'Aug':
		result = '08'
	elif din == 'Sep':
		result = '09'
	elif din == 'Oct':
		result = '10'
	elif din == 'Nov':
		result = '11'
	elif din == 'Dec':
		result = '12'
	return result

def from_str_date(din):
	result = ''
	comps = break_up_jq_str_date(din)
	month = jq_month_to_int(comps['month'])
	day = process_jq_day(comps['day'])
	year = process_jq_year(comps['year'])
	result += year
	result += '-'
	result += month
	result += '-'
	result += day
	return result

def convertJQdate(din):
	result = ''
	result += din[6]
	result += din[7]
	result += din[8]
	result += din[9]
	result += '-'
	result += din[0]
	result += din[1]
	result += '-'
	result += din[3]
	result += din[4]
	return result

def process_jq_date(din):
	result = None
	if isJQnumber(din) == True:
		result = convertJQdate(din)
	else:
		result = from_str_date(din)
	return result

def get_asi_names():
	result = []
	result.append('admin')
	result.append('general')
	result.append('medical')
	result.append('employment')
	result.append('drug1')
	result.append('legal')
	result.append('family')
	result.append('social1')
	result.append('social2')
	result.append('psych')
	return result

def get_asi_urls():
	result = []
	result.append('/asi_admin/')
	result.append('/asi_general/')
	result.append('/asi_medical/')
	result.append('/asi_employment/')
	result.append('/asi_drug1/')
	result.append('/asi_legal/')
	result.append('/asi_family/')
	result.append('/asi_social1/')
	result.append('/asi_social2/')
	result.append('/asi_psych/')
	return result

def get_asi_butons():
	result = []
	result.append('asi_admin_image')
	result.append('asi_general_image')
	result.append('asi_medical_image')
	result.append('asi_employment_image')
	result.append('asi_drug1_image')
	result.append('asi_legal_image')
	result.append('asi_family_image')
	result.append('asi_social1_image')
	result.append('asi_social2_image')
	result.append('asi_psych_image')
	return result

def get_asi_complete(asi):
	result = []
	result.append(asi.adminComplete)
	result.append(asi.generalComplete)
	result.append(asi.medicalComplete)
	result.append(asi.employmentComplete)
	result.append(asi.drug1Complete)
	result.append(asi.legalComplete)
	result.append(asi.familyComplete)
	result.append(asi.social1Complete)
	result.append(asi.social2Complete)
	result.append(asi.psychComplete)
	return result

def get_asi_priority(asi):
	result = []
	result.append(asi.adminPriority)
	result.append(asi.generalPriority)
	result.append(asi.medicalPriority)
	result.append(asi.employmentPriority)
	result.append(asi.drug1Priority)
	result.append(asi.legalPriority)
	result.append(asi.familyPriority)
	result.append(asi.social1Priority)
	result.append(asi.social2Priority)
	result.append(asi.psychPriority)
	return result

def get_asi_parameters(asi):
	result = []
	name = get_asi_names()
	url = get_asi_urls()
	btn = get_asi_butons()
	complete = get_asi_complete(asi)
	priority = get_asi_priority(asi)

	for l in range(len(name)):
		data = {}
		data['name'] = name[l]
		data['url'] = url[l]
		data['btn'] = btn[l]
		data['complete'] = complete[l]
		data['priority'] = priority[l]
		result.append(data)
	return result

def priority_asi_admin(asi):
	asi.adminPriority 		= True
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_general(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= True
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_medical(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= True
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_employment(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= True
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_drug1(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= True
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False


def priority_asi_legal(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= True
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_family(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= True
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_soc1(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= True
	asi.social2Priority 	= False
	asi.psychPriority 		= False

def priority_asi_soc2(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= True
	asi.psychPriority 		= False

def priority_asi_psych(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= True

def asiPriority(asi, section):
	section = str(section)

	if section == '/asi_admin/':
		result = priority_asi_admin(asi)
	elif section == '/asi_general/':
		result = priority_asi_general(asi)
	elif section == '/asi_medical/':
		result = priority_asi_medical(asi)
	elif section == '/asi_employment/':
		result = priority_asi_employment(asi)
	elif section == '/asi_drug1/':
		result = priority_asi_drug1(asi)
	elif section == '/asi_legal/':
		result = priority_asi_legal(asi)
	elif section == '/asi_family/':
		result = priority_asi_family(asi)
	elif section == '/asi_social1/':
		result = priority_asi_soc1(asi)
	elif section == '/asi_social2/':
		result = priority_asi_soc2(asi)
	elif section == '/asi_psych/':
		result = priority_asi_psych(asi)
	asi.save()

def deprioritizeASI(asi):
	asi.adminPriority 		= False
	asi.generalPriority 	= False
	asi.medicalPriority 	= False
	asi.employmentPriority 	= False
	asi.drug1Priority 		= False
	asi.legalPriority 		= False
	asi.familyPriority 		= False
	asi.social1Priority 	= False
	asi.social2Priority 	= False
	asi.psychPriority 		= False
	asi.save()

def forceNextAsiPage(asi):
	result 	= None
	flag 	= None
	asi_list = get_asi_parameters(asi)

	for i in range(len(asi_list)):
		if asi_list[i]['complete'] == False:
			flag = i
			break

	for j in range(len(asi_list)):
		if asi_list[j]['complete'] == False and j != flag:
			result = asi_list[j]['url']
			break

	return result

def nextAsiPage(asi, section):
	result 		= None
	nextSection = None
	proceed 	= True
	asi_list 	= get_asi_parameters(asi)

	for a in asi_list:
		if a['priority'] == True:
			result = a['url']
			proceed = False
			break

	if proceed == True:
		for i in range(len(asi_list)):
			if asi_list[i]['complete'] == False:
				nextSection = asi_list[i]['url']
				break

		if str(nextSection) == str(section):
			result = forceNextAsiPage(asi)
		else:
			result = nextSection

	if result == None:
		result = '/asi_viewForm/'

	return result

def grabASIClassesCSS(asi, m_page):
	classes = {}
	asi = get_asi_parameters(asi)
	normal = 'sideBarMargin'
	green = 'sideBarMarginChecked'
	current = 'sideLinkSelected'

	classes['asiAdmin'] = processCompletedClass(asi[0]['complete'], asi[0]['url'], m_page, green, current, normal)
	classes['asiGeneral'] = processCompletedClass(asi[1]['complete'], asi[1]['url'], m_page, green, current, normal)
	classes['asiMedical'] = processCompletedClass(asi[2]['complete'], asi[2]['url'], m_page, green, current, normal)
	classes['asiEmployment'] = processCompletedClass(asi[3]['complete'], asi[3]['url'], m_page, green, current, normal)
	classes['asiDrug1'] = processCompletedClass(asi[4]['complete'], asi[4]['url'], m_page, green, current, normal)	
	classes['asiLegal'] = processCompletedClass(asi[5]['complete'], asi[5]['url'], m_page, green, current, normal)
	classes['asiFamily'] = processCompletedClass(asi[6]['complete'], asi[6]['url'], m_page, green, current, normal)
	classes['asiSocial1'] = processCompletedClass(asi[7]['complete'], asi[7]['url'], m_page, green, current, normal)
	classes['asiSocial2'] = processCompletedClass(asi[8]['complete'], asi[8]['url'], m_page, green, current, normal)
	classes['asiPsych'] = processCompletedClass(asi[9]['complete'], asi[9]['url'], m_page, green, current, normal)

	return classes

def grabASISideImages(asi, page):
	images = {}
	check = "/static/images/green_check.png"
	x = "/static/images/red_x.png"
	progress = "/static/images/yellow_progress.png"
	asiComps = get_asi_parameters(asi)

	for a in asiComps:
		if a['complete'] == True and page != a['url']:
			images[a['btn']] = check
		elif page == '/asi_viewForm/':
			images[a['btn']] = check
		elif page == a['url']:
			images[a['btn']] = progress
		else:
			images[a['btn']] = x

	return images

def hasIncompleteASI(client):
	exist = False
	asis = ASI.objects.all()

	for a in asis:
		if a.client == client and a.AIS_Complete == False:
			exist = True
			break
	return exist

def findIncompleteClientASI(client):
	asis = ASI.objects.all()
	result = None

	for a in asis:
		if a.client == client and a.AIS_Complete == False:
			result = a
			break
	return result

def newASI(the_client):
	the_date = datetime.now()
	date = the_date.date()
	temp_time = str(the_date.time())
	time = ''
	time += temp_time[0]
	time += temp_time[1]
	time += temp_time[2]
	time += temp_time[3]
	time += temp_time[4]

	asi = ASI(client=the_client, date_of_assessment=date, startTime=time)

	admin 		= AIS_Admin(clientID=the_client.clientID)	
	general 	= AIS_General(clientID=the_client.clientID)
	medical 	= AIS_Medical(clientID=the_client.clientID)
	employment 	= AIS_Employment(clientID=the_client.clientID)
	drug1 		= AIS_Drug1(clientID=the_client.clientID)
	legal 		= AIS_Legal(clientID=the_client.clientID)
	family 		= AIS_Family(clientID=the_client.clientID)
	social1 	= AIS_Social1(clientID=the_client.clientID)
	social2 	= AIS_Social2(clientID=the_client.clientID)
	psych 		= AIS_Psych(clientID=the_client.clientID)

	admin.save()
	general.save()
	medical.save()
	employment.save()
	drug1.save()
	legal.save()
	family.save()
	social1.save()
	social2.save()
	psych.save()

	asi.admin 		= admin
	asi.general 	= general
	asi.medical 	= medical
	asi.employment 	= employment
	asi.drug1 		= drug1
	asi.legal 		= legal
	asi.family 		= family
	asi.social1 	= social1
	asi.social2 	= social2
	asi.psych 		= psych

	asi.isOpen = True
	asi.save()

	return asi


def startASI(client):
	result = {}

	if hasIncompleteASI(client) == False:
		result['isNew'] = True
		result['asi'] = newASI(client)

	else:
		result['isNew'] = False
		result['asi'] = findIncompleteClientASI(client)

	return result

def beginASI(request):
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	client = Client.objects.get(id=client_id)
	session = ClientSession.objects.get(id=session_id)

	action = startASI(client)
	asi = action['asi']
	setGlobalID(asi.id)

	openForm('asi', asi, client)

	result['asi'] = asi
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | Addiction Severity Index"
	result['save_this'] = 'false'

	if action['isNew'] == False:
		next_section = nextAsiPage(asi, None)
		result['form'] = asi
		result['form_type'] = 'asi'
		result['type_header'] = 'A.S.I'
		result['next_section'] = next_section
		result['save_section'] = next_section

	return result

def getInterviewerIndex(m_val):
	index = 0

	if m_val != None and m_val != 'Select' and m_val != '':
		index = int(m_val) + 1

	return index


def getPatientIndex(m_val):
	m_val = str(m_val)
	index = 0

	if m_val != 'None' and m_val != 'Select' and m_val != '':
		if m_val=='0' or m_val=='1' or m_val=='2' or m_val=='3' or m_val=='4':
			index = int(m_val) + 1
		elif m_val=='X':
			index = 6
		elif m_val == 'N':
			index = 7

	return index

def grabAsiAdminFields(asi):
	result = {}
	result['g1'] = asi.admin.g1
	result['g2'] = asi.admin.g2
	result['g3'] = asi.admin.g3
	result['g8'] = asi.admin.g8
	result['g9'] = asi.admin.g9
	result['g10'] = asi.admin.g10
	result['g11'] = asi.admin.g11
	result['g12'] = asi.admin.g12
	result['isComplete'] = asi.adminComplete
	return result

def grabAsiGeneralFields(asi):
	result = {}
	result['g13'] 		= asi.general.g13
	result['g14yrs'] 	= asi.general.g14yrs
	result['g14mos'] 	= asi.general.g14mos
	result['g15'] 		= asi.general.g15
	result['g16mth'] 	= asi.general.g16mth
	result['g16day'] 	= asi.general.g16day
	result['g16year'] 	= asi.general.g16year
	result['g17'] 		= asi.general.g17
	result['g18'] 		= asi.general.g18
	result['g19'] 		= asi.general.g19
	result['g20'] 		= asi.general.g20
	result['g21'] 		= asi.general.g21
	result['g22'] 		= asi.general.g22
	result['g23'] 		= asi.general.g23
	result['g24'] 		= asi.general.g24
	result['g25'] 		= asi.general.g25
	result['g26'] 		= asi.general.g26
	result['g27'] 		= asi.general.g27
	result['g28'] 		= asi.general.g28
	result['medical'] 	= asi.general.medical
	result['employ'] 	= asi.general.employ
	result['alcohol'] 	= asi.general.alcohol
	result['drug'] 		= asi.general.drug
	result['legal'] 	= asi.general.legal
	result['family'] 	= asi.general.family
	result['psych'] 	= asi.general.psych
	result['test1'] 	= asi.general.test1
	result['test2'] 	= asi.general.test2
	result['test3'] 	= asi.general.test3
	result['isComplete'] = asi.generalComplete
	return result

def grabAsiMedicalFields(asi):
	result = {}
	m7 = getPatientIndex(asi.medical.m7)
	m8 = getPatientIndex(asi.medical.m8)
	m9 = getInterviewerIndex(asi.medical.m9)

	result['m1'] = asi.medical.m1
	result['m2yrs'] = asi.medical.m2yrs
	result['m2mth'] = asi.medical.m2mth
	result['m3'] = asi.medical.m3
	result['m4'] = asi.medical.m4
	result['m5'] = asi.medical.m5
	result['m5Exp'] = asi.medical.m5Exp
	result['m6'] = asi.medical.m6
	result['m7'] = m7
	result['m8'] = m8
	result['m9'] = m9
	result['m10'] = asi.medical.m10
	result['m11'] = asi.medical.m11
	result['comments'] = asi.medical.comments
	result['isComplete'] = asi.medicalComplete
	return result

def grabAsiEmploymentFields(asi):
	result = {}
	e20 = getPatientIndex(asi.employment.e20)
	e21 = getPatientIndex(asi.employment.e21)
	e22 = getInterviewerIndex(asi.employment.e22)

	result['e1yrs'] = asi.employment.e1yrs
	result['e1mth'] = asi.employment.e1mth
	result['e2'] = asi.employment.e2
	result['e3'] = asi.employment.e3
	result['e3Exp'] = asi.employment.e3Exp
	result['e4'] = asi.employment.e4
	result['e5'] = asi.employment.e5
	result['e6yrs'] = asi.employment.e6yrs
	result['e6mth'] = asi.employment.e6mth
	result['e7'] = asi.employment.e7
	result['e7Exp'] = asi.employment.e7Exp
	result['e8'] = asi.employment.e8
	result['e9'] = asi.employment.e9
	result['e10'] = asi.employment.e10
	result['e11'] = asi.employment.e11
	result['e12'] = asi.employment.e12
	result['e13'] = asi.employment.e13
	result['e14'] = asi.employment.e14
	result['e15'] = asi.employment.e15
	result['e16'] = asi.employment.e16
	result['e17'] = asi.employment.e17
	result['e18'] = asi.employment.e18
	result['e19'] = asi.employment.e19
	result['e20'] = e20
	result['e21'] = e21
	result['e22'] = e22
	result['e23'] = asi.employment.e23
	result['e24'] = asi.employment.e24
	result['comments'] = asi.employment.comments
	result['isComplete'] = asi.employmentComplete
	
	return result

def grabAsiDrug1Fields(asi):
	result = {}
	result['d1Day'] = asi.drug1.d1Day
	result['d1Year'] = asi.drug1.d1Year
	result['d1Route'] = asi.drug1.d1Route

	result['d2Day'] = asi.drug1.d2Day
	result['d2Year'] = asi.drug1.d2Year
	result['d2Route'] = asi.drug1.d2Route

	result['d3Day'] = asi.drug1.d3Day
	result['d3Year'] = asi.drug1.d3Year
	result['d3Route'] = asi.drug1.d3Route

	result['d4Day'] = asi.drug1.d4Day
	result['d4Year'] = asi.drug1.d4Year
	result['d4Route'] = asi.drug1.d4Route

	result['d5Day'] = asi.drug1.d5Day
	result['d5Year'] = asi.drug1.d5Year
	result['d5Route'] = asi.drug1.d5Route

	result['d6Day'] = asi.drug1.d6Day
	result['d6Year'] = asi.drug1.d6Year
	result['d6Route'] = asi.drug1.d6Route

	result['d7Day'] = asi.drug1.d7Day
	result['d7Year'] = asi.drug1.d7Year
	result['d7Route'] = asi.drug1.d7Route

	result['d8Day'] = asi.drug1.d8Day
	result['d8Year'] = asi.drug1.d8Year
	result['d8Route'] = asi.drug1.d8Route

	result['d9Day'] = asi.drug1.d9Day
	result['d9Year'] = asi.drug1.d9Year
	result['d9Route'] = asi.drug1.d9Route

	result['d10Day'] = asi.drug1.d10Day
	result['d10Year'] = asi.drug1.d10Year
	result['d10Route'] = asi.drug1.d10Route

	result['d11Day'] = asi.drug1.d11Day
	result['d11Year'] = asi.drug1.d11Year
	result['d11Route'] = asi.drug1.d11Route

	result['d12Day'] = asi.drug1.d12Day
	result['d12Year'] = asi.drug1.d12Year
	result['d12Route'] = asi.drug1.d12Route

	result['d13'] = asi.drug1.d13
	result['isComplete'] = asi.drug1Complete

	result['d14'] = asi.drug1.d14
	result['d15'] = asi.drug1.d15
	result['d16'] = asi.drug1.d16
	result['d17'] = asi.drug1.d17
	result['d18'] = asi.drug1.d18
	result['d19'] = asi.drug1.d19
	result['d20'] = asi.drug1.d20
	result['d21'] = asi.drug1.d21
	result['d22'] = asi.drug1.d22
	result['d23'] = asi.drug1.d23
	result['d24'] = asi.drug1.d24
	result['d25'] = asi.drug1.d25
	result['d26'] = asi.drug1.d26
	result['d27'] = asi.drug1.d27
	result['d28'] = asi.drug1.d28
	result['d29'] = asi.drug1.d29
	result['d30'] = asi.drug1.d30
	result['d31'] = asi.drug1.d31
	result['d32'] = asi.drug1.d32
	result['d33'] = asi.drug1.d33
	result['d34'] = asi.drug1.d34
	result['d35'] = asi.drug1.d35
	result['comments'] = asi.drug1.comments
	return result

def grabAsiLegalFields(asi):
	result = {}
	result['l1'] = asi.legal.l1
	result['l2'] = asi.legal.l2
	result['l3'] = asi.legal.l3
	result['l4'] = asi.legal.l4
	result['l5'] = asi.legal.l5
	result['l6'] = asi.legal.l6
	result['l7'] = asi.legal.l7
	result['l8'] = asi.legal.l8
	result['l9'] = asi.legal.l9
	result['l10'] = asi.legal.l10
	result['l11'] = asi.legal.l11
	result['l12'] = asi.legal.l12
	result['l13'] = asi.legal.l13
	result['l14'] = asi.legal.l14
	result['l15'] = asi.legal.l15
	result['l16'] = asi.legal.l16
	result['l17'] = asi.legal.l17
	result['l18'] = asi.legal.l18
	result['l19'] = asi.legal.l19
	result['l20'] = asi.legal.l20
	result['l21'] = asi.legal.l21
	result['l22'] = asi.legal.l22
	result['l23'] = asi.legal.l23
	result['l24'] = asi.legal.l24
	result['l25'] = asi.legal.l25
	result['l26'] = asi.legal.l26
	result['l27'] = asi.legal.l27
	result['l28'] = asi.legal.l28
	result['l29'] = asi.legal.l29
	result['l30'] = asi.legal.l30
	result['l31'] = asi.legal.l31
	result['l32'] = asi.legal.l32
	result['comments'] = asi.legal.comments
	result['isComplete'] = asi.legalComplete
	return result

def grabAsiFamilyFields(asi):
	result = {}
	result['h1a'] = asi.family.h1a
	result['h1d'] = asi.family.h1d
	result['h1p'] = asi.family.h1p

	result['h1a'] = asi.family.h2a
	result['h1d'] = asi.family.h2d
	result['h1p'] = asi.family.h2p

	result['h1a'] = asi.family.h3a
	result['h1d'] = asi.family.h3d
	result['h1p'] = asi.family.h3p

	result['h1a'] = asi.family.h4a
	result['h1d'] = asi.family.h4d
	result['h1p'] = asi.family.h4p

	result['h1a'] = asi.family.h5a
	result['h1d'] = asi.family.h5d
	result['h1p'] = asi.family.h5p

	result['h1a'] = asi.family.h6a
	result['h1d'] = asi.family.h6d
	result['h1p'] = asi.family.h6p

	result['h1a'] = asi.family.h7a
	result['h1d'] = asi.family.h7d
	result['h1p'] = asi.family.h7p

	result['h1a'] = asi.family.h8a
	result['h1d'] = asi.family.h8d
	result['h1p'] = asi.family.h8p

	result['h1a'] = asi.family.h9a
	result['h1d'] = asi.family.h9d
	result['h1p'] = asi.family.h9p

	result['h1a'] = asi.family.h10a
	result['h1d'] = asi.family.h10d
	result['h1p'] = asi.family.h10p

	result['h1a'] = asi.family.h11a
	result['h1d'] = asi.family.h11d
	result['h1p'] = asi.family.h11p

	result['h1a'] = asi.family.h12a
	result['h1d'] = asi.family.h12d
	result['h1p'] = asi.family.h12p
	result['isComplete'] = asi.familyComplete
	return result

def grabAsiSocial1Fields(asi):
	result = {}
	result['f1'] = asi.social1.f1
	result['f2yrs'] = asi.social1.f2yrs
	result['f2mth'] = asi.social1.f2mth
	result['f3'] = asi.social1.f3
	result['f4'] = asi.social1.f4
	result['f5yrs'] = asi.social1.f5yrs
	result['f5mth'] = asi.social1.f5mth
	result['f6'] = asi.social1.f6
	result['f7'] = asi.social1.f7
	result['f8'] = asi.social1.f8
	result['f9'] = asi.social1.f9
	result['f10'] = asi.social1.f10
	result['f11'] = asi.social1.f11
	result['f30'] = asi.social1.f30
	result['f31'] = asi.social1.f31
	result['f32'] = asi.social1.f32
	result['f33'] = asi.social1.f33
	result['f34'] = asi.social1.f34
	result['f35'] = asi.social1.f35
	result['f36'] = asi.social1.f36
	result['f37'] = asi.social1.f37
	result['f38'] = asi.social1.f38
	result['comments'] = asi.social1.comments
	result['isComplete'] = asi.social1Complete
	return result

def grabAsiSocial2Fields(asi):
	result = {}
	result['f12'] = asi.social2.f12
	result['f13'] = asi.social2.f13
	result['f14'] = asi.social2.f14
	result['f16'] = asi.social2.f16
	result['f17'] = asi.social2.f17

	result['f18d'] = asi.social2.f18d
	result['f18y'] = asi.social2.f18y
	result['f19d'] = asi.social2.f19d
	result['f19y'] = asi.social2.f19y
	result['f20d'] = asi.social2.f20d
	result['f20y'] = asi.social2.f20y
	result['f21d'] = asi.social2.f21d
	result['f21y'] = asi.social2.f21y
	result['f22d'] = asi.social2.f22d
	result['f22y'] = asi.social2.f22y
	result['f23d'] = asi.social2.f23d
	result['f23y'] = asi.social2.f23y
	result['f24d'] = asi.social2.f24d
	result['f24y'] = asi.social2.f24y
	result['f25d'] = asi.social2.f25d
	result['f25y'] = asi.social2.f25y
	result['f26d'] = asi.social2.f26d
	result['f26y'] = asi.social2.f26y
	
	result['fa18'] = asi.social2.fa18
	result['fa19'] = asi.social2.fa19
	result['fa20'] = asi.social2.fa20
	result['fa21'] = asi.social2.fa21
	result['fa22'] = asi.social2.fa22
	result['fa23'] = asi.social2.fa23
	result['fa24'] = asi.social2.fa24
	result['fa25'] = asi.social2.fa25
	result['fa26'] = asi.social2.fa26

	result['f18dayBad'] = asi.social2.f18dayBad
	result['f19dayBad'] = asi.social2.f19dayBad
	result['f20dayBad'] = asi.social2.f20dayBad
	result['f21dayBad'] = asi.social2.f21dayBad
	result['f22dayBad'] = asi.social2.f22dayBad
	result['f23dayBad'] = asi.social2.f23dayBad
	result['f24dayBad'] = asi.social2.f24dayBad
	result['f25dayBad'] = asi.social2.f25dayBad
	result['f26dayBad'] = asi.social2.f26dayBad

	result['f18yearBad'] = asi.social2.f18yearBad
	result['f19yearBad'] = asi.social2.f19yearBad
	result['f20yearBad'] = asi.social2.f20yearBad
	result['f21yearBad'] = asi.social2.f21yearBad
	result['f22yearBad'] = asi.social2.f22yearBad
	result['f23yearBad'] = asi.social2.f23yearBad
	result['f24yearBad'] = asi.social2.f24yearBad
	result['f25yearBad'] = asi.social2.f25yearBad
	result['f26yearBad'] = asi.social2.f26yearBad

	result['comments'] = asi.social2.comments
	result['isComplete'] = asi.social2Complete
	return result

def grabAsiPsychFields(asi):
	result = {}
	result['p1'] = asi.psych.p1
	result['p2'] = asi.psych.p2
	result['p3'] = asi.psych.p3

	result['p4d'] = asi.psych.p4d
	result['p5d'] = asi.psych.p5d
	result['p6d'] = asi.psych.p6d
	result['p7d'] = asi.psych.p7d
	result['p8d'] = asi.psych.p8d
	result['p9d'] = asi.psych.p9d
	result['p10d'] = asi.psych.p10d
	result['p11d'] = asi.psych.p11d

	result['p4y'] = asi.psych.p4y
	result['p5y'] = asi.psych.p5y
	result['p6y'] = asi.psych.p6y
	result['p7y'] = asi.psych.p7y
	result['p8y'] = asi.psych.p8y
	result['p9y'] = asi.psych.p9y
	result['p10y'] = asi.psych.p10y
	result['p11y'] = asi.psych.p11y

	result['p12'] = asi.psych.p12
	result['p13'] = asi.psych.p13
	result['p14'] = asi.psych.p14
	result['p15'] = asi.psych.p15
	result['p16'] = asi.psych.p16
	result['p17'] = asi.psych.p17
	result['p18'] = asi.psych.p18
	result['p19'] = asi.psych.p19
	result['p20'] = asi.psych.p20
	result['p21'] = asi.psych.p21
	result['p22'] = asi.psych.p22
	result['p23'] = asi.psych.p23
	result['comments'] = asi.psych.comments
	result['isComplete'] = asi.psychComplete
	return result

def grabASIFields(asi, section):
	section = str(section)
	result = {}

	if section == '/asi_admin/':
		result = grabAsiAdminFields(asi)
	elif section == '/asi_general/':
		result = grabAsiGeneralFields(asi)
	elif section == '/asi_medical/':
		result = grabAsiMedicalFields(asi)
	elif section == '/asi_employment/':
		result = grabAsiEmploymentFields(asi)
	elif section == '/asi_drug1/':
		result = grabAsiDrug1Fields(asi)
	elif section == '/asi_legal/':
		result = grabAsiLegalFields(asi)
	elif section == '/asi_family/':
		result = grabAsiFamilyFields(asi)
	elif section == '/asi_social1/':
		result = grabAsiSocial1Fields(asi)
	elif section == '/asi_social2/':
		result = grabAsiSocial2Fields(asi)
	elif section == '/asi_psych/':
		result = grabAsiPsychFields(asi)

	return result

def processASIbool(val):
	result = False
	if str(val) == '1':
		result = True
	return result

def saveASIadmin(request, asi):
	asi.admin.g1 = request.POST.get('g1')
	asi.admin.g2 = request.POST.get('g2')
	asi.admin.g3 = request.POST.get('g3')
	asi.admin.g4 = process_jq_date(request.POST.get('g4'))
	asi.admin.g8 = request.POST.get('g8')
	asi.admin.g9 = request.POST.get('g9')
	asi.admin.g10 = request.POST.get('g10')
	asi.admin.g11 = request.POST.get('g11')
	asi.admin.g12 = request.POST.get('g12')

	asi.admin.save()

def saveASIgeneral(request, asi):
	asi.general.g13 = request.POST.get('g13')
	asi.general.g14yrs = request.POST.get('g14yrs')
	asi.general.g14mos = request.POST.get('g14mos')
	asi.general.g15 = request.POST.get('g15')
	asi.general.g16mth = request.POST.get('g16mth')
	asi.general.g16day = request.POST.get('g16day')
	asi.general.g16year = request.POST.get('g16year')
	asi.general.g17 = request.POST.get('g17')
	asi.general.g18 = request.POST.get('g18')
	asi.general.g19 = request.POST.get('g19')
	asi.general.g20 = request.POST.get('g20')

	asi.general.g21 = request.POST.get('g21')
	asi.general.g22 = request.POST.get('g22')
	asi.general.g23 = request.POST.get('g23')
	asi.general.g24 = request.POST.get('g24')
	asi.general.g25 = request.POST.get('g25')
	asi.general.g26 = request.POST.get('g26')
	asi.general.g27 = request.POST.get('g27')
	asi.general.g28 = request.POST.get('g28')

	asi.general.medical = request.POST.get('medical')
	asi.general.employ = request.POST.get('employ')
	asi.general.alcohol = request.POST.get('alcohol')
	asi.general.drug = request.POST.get('drug')
	asi.general.legal = request.POST.get('legal')
	asi.general.family = request.POST.get('family')
	asi.general.psych = request.POST.get('psych')

	asi.general.test1 = request.POST.get('test1')
	asi.general.test2 = request.POST.get('test2')
	asi.general.test3 = request.POST.get('test3')

	asi.general.save()

def saveASImedical(request, asi):
	asi.medical.m1 = request.POST.get('m1')
	asi.medical.m2yrs = request.POST.get('m2yrs')
	asi.medical.m2mth = request.POST.get('m2mth')
	asi.medical.m3 = request.POST.get('m3')
	asi.medical.m4 = request.POST.get('m4')
	asi.medical.m5 = request.POST.get('m5')
	asi.medical.m5Exp = request.POST.get('m_m5Exp')
	asi.medical.m6 = request.POST.get('m6')
	asi.medical.m7 = request.POST.get('m7')
	asi.medical.m8 = request.POST.get('m8')
	asi.medical.m9 = request.POST.get('m9')
	asi.medical.m10 = request.POST.get('m10')
	asi.medical.m11 = request.POST.get('m11')
	asi.medical.comments = request.POST.get('comments')

	asi.medical.save()

def saveASIemployment(request, asi):
	asi.employment.e1yrs = request.POST.get('e1yrs')
	asi.employment.e1mth = request.POST.get('e1mth')
	asi.employment.e2 = request.POST.get('e2')
	asi.employment.e3 = request.POST.get('e3')
	asi.employment.e3Exp = request.POST.get('m_e3Exp')
	asi.employment.e4 = request.POST.get('e4')
	asi.employment.e5 = request.POST.get('m_e5')
	asi.employment.e6yrs = request.POST.get('e6yrs')
	asi.employment.e6mth = request.POST.get('e6mth')
	asi.employment.e7 = request.POST.get('e7')
	asi.employment.e7Exp = request.POST.get('m_e7Exp')
	asi.employment.e8 = request.POST.get('e8')
	asi.employment.e9 = request.POST.get('m_e9')
	asi.employment.e10 = request.POST.get('e10')
	asi.employment.e11 = request.POST.get('e11')
	asi.employment.e12 = request.POST.get('e12')
	asi.employment.e13 = request.POST.get('e13')
	asi.employment.e14 = request.POST.get('e14')
	asi.employment.e15 = request.POST.get('e15')
	asi.employment.e16 = request.POST.get('e16')
	asi.employment.e17 = request.POST.get('e17')
	asi.employment.e18 = request.POST.get('e18')
	asi.employment.e19 = request.POST.get('e19')
	asi.employment.e20 = request.POST.get('e20')
	asi.employment.e21 = request.POST.get('e21')
	asi.employment.e22 = request.POST.get('e22')
	asi.employment.e23 = request.POST.get('e23')
	asi.employment.e24 = request.POST.get('e24')
	asi.employment.comments = request.POST.get('comments')

	asi.employment.save()

def saveASIdrug1(request, asi):
	asi.drug1.d1Day = request.POST.get('d1Day')
	asi.drug1.d1Year = request.POST.get('d1Year')
	asi.drug1.d1Route = request.POST.get('d1Route')

	asi.drug1.d2Day = request.POST.get('d2Day')
	asi.drug1.d2Year = request.POST.get('d2Year')
	asi.drug1.d2Route = request.POST.get('d2Route')

	asi.drug1.d3Day = request.POST.get('d3Day')
	asi.drug1.d3Year = request.POST.get('d3Year')
	asi.drug1.d3Route = request.POST.get('d3Route')

	asi.drug1.d4Day = request.POST.get('d4Day')
	asi.drug1.d4Year = request.POST.get('d4Year')
	asi.drug1.d4Route = request.POST.get('d4Route')

	asi.drug1.d5Day = request.POST.get('d5Day')
	asi.drug1.d5Year = request.POST.get('d5Year')
	asi.drug1.d5Route = request.POST.get('d5Route')

	asi.drug1.d6Day = request.POST.get('d6Day')
	asi.drug1.d6Year = request.POST.get('d6Year')
	asi.drug1.d6Route = request.POST.get('d6Route')

	asi.drug1.d7Day = request.POST.get('d7Day')
	asi.drug1.d7Year = request.POST.get('d7Year')
	asi.drug1.d7Route = request.POST.get('d7Route')

	asi.drug1.d8Day = request.POST.get('d8Day')
	asi.drug1.d8Year = request.POST.get('d8Year')
	asi.drug1.d8Route = request.POST.get('d8Route')

	asi.drug1.d9Day = request.POST.get('d9Day')
	asi.drug1.d9Year = request.POST.get('d9Year')
	asi.drug1.d9Route = request.POST.get('d9Route')

	asi.drug1.d10Day = request.POST.get('d10Day')
	asi.drug1.d10Year = request.POST.get('d10Year')
	asi.drug1.d10Route = request.POST.get('d10Route')

	asi.drug1.d11Day = request.POST.get('d11Day')
	asi.drug1.d11Year = request.POST.get('d11Year')
	asi.drug1.d11Route = request.POST.get('d11Route')

	asi.drug1.d12Day = request.POST.get('d12Day')
	asi.drug1.d12Year = request.POST.get('d12Year')
	asi.drug1.d12Route = request.POST.get('d12Route')

	asi.drug1.d13 = request.POST.get('d13')
	asi.drug1.d14 = request.POST.get('d14')
	asi.drug1.d15 = request.POST.get('d15')
	asi.drug1.d16 = request.POST.get('d16')

	asi.drug1.d17 = request.POST.get('d17')
	asi.drug1.d18 = request.POST.get('d18')
	asi.drug1.d19 = request.POST.get('d19')
	asi.drug1.d20 = request.POST.get('d20')
	asi.drug1.d21 = request.POST.get('d21')
	asi.drug1.d22 = request.POST.get('d22')
	asi.drug1.d23 = request.POST.get('d23')
	asi.drug1.d24 = request.POST.get('d24')
	asi.drug1.d25 = request.POST.get('d25')
	asi.drug1.d26 = request.POST.get('d26')
	asi.drug1.d27 = request.POST.get('d27')
	asi.drug1.d28 = request.POST.get('d28')
	asi.drug1.d29 = request.POST.get('d29')
	asi.drug1.d30 = request.POST.get('d30')
	asi.drug1.d31 = request.POST.get('d31')
	asi.drug1.d32 = request.POST.get('d32')
	asi.drug1.d33 = request.POST.get('d33')
	asi.drug1.d34 = request.POST.get('d34')
	asi.drug1.d35 = request.POST.get('d35')
	asi.drug1.comments = request.POST.get('comments')

	asi.drug1.save()


def saveASIlegal(request, asi):
	asi.legal.l1 = request.POST.get('l1')
	asi.legal.l2 = request.POST.get('l2')
	asi.legal.l3 = request.POST.get('l3')
	asi.legal.l4 = request.POST.get('l4')
	asi.legal.l5 = request.POST.get('l5')
	asi.legal.l6 = request.POST.get('l6')
	asi.legal.l7 = request.POST.get('l7')
	asi.legal.l8 = request.POST.get('l8')
	asi.legal.l9 = request.POST.get('l9')
	asi.legal.l10 = request.POST.get('l10')
	asi.legal.l11 = request.POST.get('l11')
	asi.legal.l12 = request.POST.get('l12')
	asi.legal.l13 = request.POST.get('l13')
	asi.legal.l14 = request.POST.get('l14')
	asi.legal.l15 = request.POST.get('l15')
	asi.legal.l16 = request.POST.get('l16')
	asi.legal.l17 = request.POST.get('l17')
	asi.legal.l18 = request.POST.get('l18')
	asi.legal.l19 = request.POST.get('l19')
	asi.legal.l20 = request.POST.get('l20')
	asi.legal.l21 = request.POST.get('l21')
	asi.legal.l22 = request.POST.get('l22')
	asi.legal.l23 = request.POST.get('l23')
	asi.legal.l24 = request.POST.get('l24')
	asi.legal.l25 = request.POST.get('l25')
	asi.legal.l26 = request.POST.get('l26')
	asi.legal.l27 = request.POST.get('l27')
	asi.legal.l28 = request.POST.get('l28')
	asi.legal.l29 = request.POST.get('l29')
	asi.legal.l30 = request.POST.get('l30')
	asi.legal.l31 = request.POST.get('l31')
	asi.legal.l32 = request.POST.get('l32')
	asi.legal.comments = request.POST.get('comments')

	asi.legal.save()

def saveASIfamily(request, asi):
	asi.family.h1a = request.POST.get('h1a')
	asi.family.h1d = request.POST.get('h1d')
	asi.family.h1p = request.POST.get('h1p')

	asi.family.h2a = request.POST.get('h2a')
	asi.family.h2d = request.POST.get('h2d')
	asi.family.h2p = request.POST.get('h2p')

	asi.family.h3a = request.POST.get('h3a')
	asi.family.h3d = request.POST.get('h3d')
	asi.family.h3p = request.POST.get('h3p')

	asi.family.h4a = request.POST.get('h4a')
	asi.family.h4d = request.POST.get('h4d')
	asi.family.h4p = request.POST.get('h4p')

	asi.family.h5a = request.POST.get('h5a')
	asi.family.h5d = request.POST.get('h5d')
	asi.family.h5p = request.POST.get('h5p')

	asi.family.h6a = request.POST.get('h6a')
	asi.family.h6d = request.POST.get('h6d')
	asi.family.h6p = request.POST.get('h6p')

	asi.family.h7a = request.POST.get('h7a')
	asi.family.h7d = request.POST.get('h7d')
	asi.family.h7p = request.POST.get('h7p')

	asi.family.h8a = request.POST.get('h8a')
	asi.family.h8d = request.POST.get('h8d')
	asi.family.h8p = request.POST.get('h8p')

	asi.family.h9a = request.POST.get('h9a')
	asi.family.h9d = request.POST.get('h9d')
	asi.family.h9p = request.POST.get('h9p')

	asi.family.h10a = request.POST.get('h10a')
	asi.family.h10d = request.POST.get('h10d')
	asi.family.h10p = request.POST.get('h10p')

	asi.family.h11a = request.POST.get('h11a')
	asi.family.h11d = request.POST.get('h11d')
	asi.family.h11p = request.POST.get('h11p')

	asi.family.h12a = request.POST.get('h12a')
	asi.family.h12d = request.POST.get('h12d')
	asi.family.h12p = request.POST.get('h12p')

	asi.family.save()

def saveASIsocial1(request, asi):
	asi.social1.f1 = request.POST.get('f1')
	asi.social1.f2yrs = request.POST.get('f2yrs')
	asi.social1.f2mth = request.POST.get('f2mth')
	asi.social1.f3 = request.POST.get('f3')
	asi.social1.f4 = request.POST.get('f4')
	asi.social1.f5yrs = request.POST.get('f5yrs')
	asi.social1.f5mth = request.POST.get('f5mth')
	asi.social1.f6 = request.POST.get('f6')
	asi.social1.f7 = request.POST.get('f7')
	asi.social1.f8 = request.POST.get('f8')
	asi.social1.f9 = request.POST.get('f9')
	asi.social1.f10 = request.POST.get('f10')
	asi.social1.f11 = request.POST.get('f11')

	asi.social1.f30 = request.POST.get('f30')
	asi.social1.f31 = request.POST.get('f31')
	asi.social1.f32 = request.POST.get('f32')
	asi.social1.f33 = request.POST.get('f33')
	asi.social1.f34 = request.POST.get('f34')
	asi.social1.f35 = request.POST.get('f35')
	asi.social1.f36 = request.POST.get('f36')
	asi.social1.f37 = request.POST.get('f37')
	asi.social1.f38 = request.POST.get('f38')
	asi.social1.comments = request.POST.get('comments')

	asi.social1.save()

def saveASIsocial2(request, asi):
	asi.social2.f12 = request.POST.get('f12')
	asi.social2.f13 = request.POST.get('f13')
	asi.social2.f14 = request.POST.get('f14')
	asi.social2.f16 = request.POST.get('f16')
	asi.social2.f17 = request.POST.get('f17')

	asi.social2.f18d = request.POST.get('f18d')
	asi.social2.f19d = request.POST.get('f19d')
	asi.social2.f20d = request.POST.get('f20d')
	asi.social2.f21d = request.POST.get('f21d')
	asi.social2.f22d = request.POST.get('f22d')
	asi.social2.f23d = request.POST.get('f23d')
	asi.social2.f24d = request.POST.get('f24d')
	asi.social2.f25d = request.POST.get('f25d')
	asi.social2.f26d = request.POST.get('f26d')

	asi.social2.f18y = request.POST.get('f18y')
	asi.social2.f19y = request.POST.get('f19y')
	asi.social2.f20y = request.POST.get('f20y')
	asi.social2.f21y = request.POST.get('f21y')
	asi.social2.f22y = request.POST.get('f22y')
	asi.social2.f23y = request.POST.get('f23y')
	asi.social2.f24y = request.POST.get('f24y')
	asi.social2.f25y = request.POST.get('f25y')
	asi.social2.f26y = request.POST.get('f26y')

	asi.social2.fa18 = request.POST.get('fa18')
	asi.social2.fa19 = request.POST.get('fa19')
	asi.social2.fa20 = request.POST.get('fa20')
	asi.social2.fa21 = request.POST.get('fa21')
	asi.social2.fa22 = request.POST.get('fa22')
	asi.social2.fa23 = request.POST.get('fa23')
	asi.social2.fa24 = request.POST.get('fa24')
	asi.social2.fa25 = request.POST.get('fa25')
	asi.social2.fa26 = request.POST.get('fa26')

	asi.social2.f18dayBad = request.POST.get('f18dayBad')
	asi.social2.f19dayBad = request.POST.get('f19dayBad')
	asi.social2.f20dayBad = request.POST.get('f20dayBad')
	asi.social2.f21dayBad = request.POST.get('f21dayBad')
	asi.social2.f22dayBad = request.POST.get('f22dayBad')
	asi.social2.f23dayBad = request.POST.get('f23dayBad')
	asi.social2.f24dayBad = request.POST.get('f24dayBad')
	asi.social2.f25dayBad = request.POST.get('f25dayBad')
	asi.social2.f26dayBad = request.POST.get('f26dayBad')

	asi.social2.f18yearBad = request.POST.get('f18yearBad')
	asi.social2.f19yearBad = request.POST.get('f19yearBad')
	asi.social2.f20yearBad = request.POST.get('f20yearBad')
	asi.social2.f21yearBad = request.POST.get('f21yearBad')
	asi.social2.f22yearBad = request.POST.get('f22yearBad')
	asi.social2.f23yearBad = request.POST.get('f23yearBad')
	asi.social2.f24yearBad = request.POST.get('f24yearBad')
	asi.social2.f25yearBad = request.POST.get('f25yearBad')
	asi.social2.f26yearBad = request.POST.get('f26yearBad')

	asi.social2.comments = request.POST.get('comments')

	asi.social2.save()

def saveASIpsych(request, asi):
	asi.psych.p1 = request.POST.get('p1')
	asi.psych.p2 = request.POST.get('p2')
	asi.psych.p3 = request.POST.get('p3')

	asi.psych.p4d = request.POST.get('p4d')
	asi.psych.p5d = request.POST.get('p5d')
	asi.psych.p6d = request.POST.get('p6d')
	asi.psych.p7d = request.POST.get('p7d')
	asi.psych.p8d = request.POST.get('p8d')
	asi.psych.p9d = request.POST.get('p9d')
	asi.psych.p10d = request.POST.get('p10d')
	asi.psych.p11d = request.POST.get('p11d')

	asi.psych.p4y = request.POST.get('p4y')
	asi.psych.p5y = request.POST.get('p5y')
	asi.psych.p6y = request.POST.get('p6y')
	asi.psych.p7y = request.POST.get('p7y')
	asi.psych.p8y = request.POST.get('p8y')
	asi.psych.p9y = request.POST.get('p9y')
	asi.psych.p10y = request.POST.get('p10y')
	asi.psych.p11y = request.POST.get('p11y')

	asi.psych.p12 = request.POST.get('p12')
	asi.psych.p13 = request.POST.get('p13')
	asi.psych.p14 = request.POST.get('p14')
	asi.psych.p15 = request.POST.get('p15')
	asi.psych.p16 = request.POST.get('p16')
	asi.psych.p17 = request.POST.get('p17')
	asi.psych.p18 = request.POST.get('p18')
	asi.psych.p19 = request.POST.get('p19')
	asi.psych.p20 = request.POST.get('p20')
	asi.psych.p21 = request.POST.get('p21')
	asi.psych.p22 = request.POST.get('p22')
	asi.psych.p23 = request.POST.get('p23')

	asi.psych.save()

def saveASI(request, section, asi):
	section = str(section)

	if section == '/asi_admin/':
		saveASIadmin(request, asi)
	elif section == '/asi_general/':
		saveASIgeneral(request, asi)
	elif section == '/asi_medical/':
		saveASImedical(request, asi)
	elif section == '/asi_employment/':
		saveASIemployment(request, asi)
	elif section == '/asi_drug1/':
		saveASIdrug1(request, asi)
	elif section == '/asi_legal/':
		saveASIlegal(request, asi)
	elif section == '/asi_family/':
		saveASIfamily(request, asi)
	elif section == '/asi_social1/':
		saveASIsocial1(request, asi)
	elif section == '/asi_social2/':
		saveASIsocial2(request, asi)
	elif section == '/asi_psych/':
		saveASIpsych(request, asi)

def setASIcomplete(asi, section):
	section = str(section)

	if section == '/asi_admin/':
		asi.adminComplete = True
	elif section == '/asi_general/':
		asi.generalComplete = True
	elif section == '/asi_medical/':
		asi.medicalComplete = True
	elif section == '/asi_employment/':
		asi.employmentComplete = True
	elif section == '/asi_drug1/':
		asi.drug1Complete = True
	elif section == '/asi_legal/':
		asi.legalComplete = True
	elif section == '/asi_family/':
		asi.familyComplete = True
	elif section == '/asi_social1/':
		asi.social1Complete = True
	elif section == '/asi_social2/':
		asi.social2Complete = True
	elif section == '/asi_psych/':
		asi.psychComplete = True

	asi.save()

def deleteASI(asi):
	asi.admin.delete()
	asi.general.delete()
	asi.medical.delete()
	asi.employment.delete()
	asi.drug1.delete()
	asi.legal.delete()
	asi.family.delete()
	asi.social1.delete()
	asi.social2.delete()
	asi.psych.delete()
	asi.delete()

def refreshASIadmin(asi):
	asi.admin.g1 = None
	asi.admin.g2 = None
	asi.admin.g3 = None
	asi.admin.g4 = None
	asi.admin.g8 = 0
	asi.admin.g9 = 0
	asi.admin.g10 = 0
	asi.admin.g11 = None
	asi.admin.g12 = 0

	asi.admin.save()

def refreshASIgeneral(asi):
	asi.general.g13 = None
	asi.general.g14yrs = None
	asi.general.g14mos = None
	asi.general.g15 = False
	asi.general.g16mth = None
	asi.general.g16day = None
	asi.general.g16year = None
	asi.general.g17 = None
	asi.general.g18 = None
	asi.general.g19 = None
	asi.general.g20 = None

	asi.general.g21 = None
	asi.general.g22 = None
	asi.general.g23 = None
	asi.general.g24 = None
	asi.general.g25 = None
	asi.general.g26 = None

	asi.general.medical = None
	asi.general.employ = None
	asi.general.alcohol = None
	asi.general.drug = None
	asi.general.legal = None
	asi.general.family = None
	asi.general.psych = None

	asi.general.save()

def refreshASImedical(asi):
	asi.medical.m1 = None
	asi.medical.m2yrs = None
	asi.medical.m2mth = None
	asi.medical.m3 = False
	asi.medical.m4 = False
	asi.medical.m5 = False
	asi.medical.m5Exp = None
	asi.medical.m6 = None
	asi.medical.m7 = None
	asi.medical.m8 = None
	asi.medical.m9 = None
	asi.medical.m10 = False
	asi.medical.m11 = False
	asi.medical.comments = None

	asi.medical.save()

def refreshASIemployment(asi):
	asi.employment.e1yrs = None
	asi.employment.e1mth = None
	asi.employment.e2 = None
	asi.employment.e3 = False
	asi.employment.e3Exp = None
	asi.employment.e4 = False
	asi.employment.e5 = False
	asi.employment.e5Exp = None
	asi.employment.e6yrs = None
	asi.employment.e6mth = None
	asi.employment.e7 = False
	asi.employment.e7Exp = None
	asi.employment.e8 = False
	asi.employment.e9 = False
	asi.employment.e10 = None
	asi.employment.e11 = None
	asi.employment.e12 = None
	asi.employment.e13 = None
	asi.employment.e14 = None
	asi.employment.e15 = None
	asi.employment.e16 = None
	asi.employment.e17 = None
	asi.employment.e18 = None
	asi.employment.e19 = None
	asi.employment.e20 = None
	asi.employment.e21 = None
	asi.employment.e22 = None
	asi.employment.e23 = False
	asi.employment.e24 = False
	asi.employment.comments = None

	asi.employment.save()

def refreshASIdrug1(asi):
	asi.drug1.d1Day = None
	asi.drug1.d1Year = None
	asi.drug1.d1Route = None
	asi.drug1.d2Day = None
	asi.drug1.d2Year = None
	asi.drug1.d2Route = None
	asi.drug1.d3Day = None
	asi.drug1.d3Year = None
	asi.drug1.d3Route = None
	asi.drug1.d4Day = None
	asi.drug1.d4Year = None
	asi.drug1.d4Route = None
	asi.drug1.d5Day = None
	asi.drug1.d5Year = None
	asi.drug1.d5Route = None
	asi.drug1.d6Day = None
	asi.drug1.d6Year = None
	asi.drug1.d6Route = None
	asi.drug1.d7Day = None
	asi.drug1.d7Year = None
	asi.drug1.d7Route = None
	asi.drug1.d8Day = None
	asi.drug1.d8Year = None
	asi.drug1.d8Route = None
	asi.drug1.d9Day = None
	asi.drug1.d9Year = None
	asi.drug1.d9Route = None
	asi.drug1.d10Day = None
	asi.drug1.d10Year = None
	asi.drug1.d10Route = None
	asi.drug1.d11Day = None
	asi.drug1.d11Year = None
	asi.drug1.d11Route = None
	asi.drug1.d12Day = None
	asi.drug1.d12Year = None
	asi.drug1.d12Route = None
	asi.drug1.d13 = None
	asi.drug1.d14 = None
	asi.drug1.d15 = None
	asi.drug1.d16 = None
	asi.drug1.d17 = None
	asi.drug1.d18 = None
	asi.drug1.d19 = None
	asi.drug1.d20 = None
	asi.drug1.d21 = None
	asi.drug1.d22 = None
	asi.drug1.d23 = None
	asi.drug1.d24 = None
	asi.drug1.d25 = None
	asi.drug1.d26 = None
	asi.drug1.d27 = None
	asi.drug1.d28 = None
	asi.drug1.d29 = None
	asi.drug1.d30 = None
	asi.drug1.d31 = None
	asi.drug1.d32 = None
	asi.drug1.d33 = None
	asi.drug1.d34 = False
	asi.drug1.d35 = False
	asi.drug1.comments = None

	asi.drug1.save()

def refreshASIlegal(asi):
	asi.legal.l1 = False
	asi.legal.l2 = False
	asi.legal.l3 = None
	asi.legal.l4 = None
	asi.legal.l5 = None
	asi.legal.l6 = None
	asi.legal.l7 = None
	asi.legal.l8 = None
	asi.legal.l9 = None
	asi.legal.l10 = None
	asi.legal.l11 = None
	asi.legal.l12 = None
	asi.legal.l13 = None
	asi.legal.l14 = None
	asi.legal.l15 = None
	asi.legal.l16 = None
	asi.legal.l17 = None
	asi.legal.l18 = None
	asi.legal.l19 = None
	asi.legal.l20 = None
	asi.legal.l21 = None
	asi.legal.l22 = None
	asi.legal.l23 = None
	asi.legal.l24 = False
	asi.legal.l25 = None
	asi.legal.l26 = None
	asi.legal.l27 = None
	asi.legal.l28 = None
	asi.legal.l29 = None
	asi.legal.l30 = None
	asi.legal.l31 = False
	asi.legal.l32 = False
	asi.legal.comments = None

	asi.legal.save()

def refreshASIfamily(asi):
	asi.family.h1a = None
	asi.family.h1d = None
	asi.family.h1p = None
	asi.family.h2a = None
	asi.family.h2d = None
	asi.family.h2p = None
	asi.family.h3a = None
	asi.family.h3d = None
	asi.family.h3p = None
	asi.family.h4a = None
	asi.family.h4d = None
	asi.family.h4p = None
	asi.family.h5a = None
	asi.family.h5d = None
	asi.family.h5p = None
	asi.family.h6a = None
	asi.family.h6d = None
	asi.family.h6p = None
	asi.family.h7a = None
	asi.family.h7d = None
	asi.family.h7p = None
	asi.family.h8a = None
	asi.family.h8d = None
	asi.family.h8p = None
	asi.family.h9a = None
	asi.family.h9d = None
	asi.family.h9p = None
	asi.family.h10a = None
	asi.family.h10d = None
	asi.family.h10p = None
	asi.family.h11a = None
	asi.family.h11d = None
	asi.family.h11p = None
	asi.family.h12a = None
	asi.family.h12d = None
	asi.family.h12p = None

	asi.family.save()

def refreshASIsocial1(asi):
	asi.social1.f1 = None
	asi.social1.f2yrs = None
	asi.social1.f2mth = None
	asi.social1.f3 = None
	asi.social1.f4 = None
	asi.social1.f5yrs = None
	asi.social1.f5mth = None
	asi.social1.f6 = None
	asi.social1.f7 = False
	asi.social1.f8 = False
	asi.social1.f9 = None
	asi.social1.f10 = None
	asi.social1.f11 = None

	asi.social1.f30 = None
	asi.social1.f31 = None
	asi.social1.f32 = None
	asi.social1.f33 = None
	asi.social1.f34 = None
	asi.social1.f35 = None
	asi.social1.f36 = None
	asi.social1.f37 = False
	asi.social1.f38 = False
	asi.social1.comments = None

	asi.social1.save()

def refreshASIsocial2(asi):
	asi.social2.f12 = None
	asi.social2.f13 = None
	asi.social2.f14 = None
	asi.social2.f16 = None
	asi.social2.f17 = None

	asi.social2.f18d = None
	asi.social2.f19d = None
	asi.social2.f20d = None
	asi.social2.f21d = None
	asi.social2.f22d = None
	asi.social2.f23d = None
	asi.social2.f24d = None
	asi.social2.f25d = None
	asi.social2.f26d = None

	asi.social2.f18y = None
	asi.social2.f19y = None
	asi.social2.f20y = None
	asi.social2.f21y = None
	asi.social2.f22y = None
	asi.social2.f23y = None
	asi.social2.f24y = None
	asi.social2.f25y = None
	asi.social2.f26y = None

	asi.social2.fa18 = False
	asi.social2.fa19 = False
	asi.social2.fa20 = False
	asi.social2.fa21 = False
	asi.social2.fa22 = False
	asi.social2.fa23 = False
	asi.social2.fa24 = False
	asi.social2.fa25 = False
	asi.social2.fa26 = False

	asi.social2.f18dayBad = None
	asi.social2.f19dayBad = None
	asi.social2.f20dayBad = None
	asi.social2.f21dayBad = None
	asi.social2.f22dayBad = None
	asi.social2.f23dayBad = None
	asi.social2.f24dayBad = None
	asi.social2.f25dayBad = None
	asi.social2.f26dayBad = None

	asi.social2.f18yearBad = None
	asi.social2.f19yearBad = None
	asi.social2.f20yearBad = None
	asi.social2.f21yearBad = None
	asi.social2.f22yearBad = None
	asi.social2.f23yearBad = None
	asi.social2.f24yearBad = None
	asi.social2.f25yearBad = None
	asi.social2.f26yearBad = None

	asi.social2.comments = None

	asi.social2.save()

def refreshASIpsych(asi):
	asi.psych.p1 = None
	asi.psych.p2 = None
	asi.psych.p3 = False

	asi.psych.p4d = False
	asi.psych.p5d = False
	asi.psych.p6d = False
	asi.psych.p7d = False
	asi.psych.p8d = False
	asi.psych.p9d = False
	asi.psych.p10d = False
	asi.psych.p11d = False

	asi.psych.p4y = False
	asi.psych.p5y = False
	asi.psych.p6y = False
	asi.psych.p7y = False
	asi.psych.p8y = False
	asi.psych.p9y = False
	asi.psych.p10y = False
	asi.psych.p11y = False

	asi.psych.p12 = None
	asi.psych.p13 = None
	asi.psych.p14 = None
	asi.psych.p15 = False
	asi.psych.p16 = False
	asi.psych.p17 = False
	asi.psych.p18 = False
	asi.psych.p19 = False
	asi.psych.p20 = False
	asi.psych.p21 = None
	asi.psych.p22 = False
	asi.psych.p23 = False
	asi.psych.comments = None

def refreshASI(asi):
	refreshASIadmin(asi)
	refreshASIgeneral(asi)
	refreshASImedical(asi)
	refreshASIemployment(asi)
	refreshASIdrug1(asi)
	refreshASIdrug2(asi)
	refreshASIlegal(asi)
	refreshASIfamily(asi)
	refreshASIsocial1(asi)
	refreshASIsocial2(asi)
	refreshASIpsych(asi)

	asi.adminComplete = False
	asi.generalComplete = False
	asi.medicalComplete = False
	asi.employmentComplete = False
	asi.drug1Complete = False
	asi.drug2Complete = False
	asi.legalComplete = False
	asi.familyComplete = False
	asi.social1Complete = False
	asi.social2Complete = False
	asi.psychComplete = False

	asi.adminPriority = False
	asi.generalPriority = False
	asi.medicalPriority = False
	asi.employmentPriority = False
	asi.drug1Priority = False
	asi.drug2Priority = False
	asi.legalPriority = False
	asi.familyPriority = False
	asi.social1Priority = False
	asi.social2Priority = False
	asi.psychPriority = False
	asi.AIS_Complete = False
	asi.save()

def processAsiData(request, current_section):
	result = {}

	session_id = request.POST.get('session_id', '')
	asi_id = request.POST.get('asi_id', '')
	save_this = request.POST.get('save_this', '')
	section = request.POST.get('save_section', '')

	session = ClientSession.objects.get(id=session_id)
	asi = ASI.objects.get(id=asi_id)
	deprioritizeASI(asi)
	fields = grabASIFields(asi, current_section)
	json_data = json.dumps(fields)

	if current_section == '/asi_admin/':
		ad_date = asi.admin.g4
		result['ad_date'] = ad_date

	if save_this == 'true':
		saveASI(request, section, asi)
		setASIcomplete(asi, section)

	next_url = nextAsiPage(asi, current_section)
	image = grabASISideImages(asi, current_section)
	classes = grabASIClassesCSS(asi, current_section)

	result['class'] = classes
	result['image'] = image
	result['next_url'] = next_url
	result['session'] = session
	result['current_section'] = current_section
	result['asi'] = asi
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | Addiction Severity Index"

	return result


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
################################################################ END ASI ##################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

###########################################################################################################################################
#*****************************************************************************************************************************************#
#-------------------------------------------------------------- DISCHARGE ----------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


def grabClientDischargeForms(client):
	results = []
	dis = Discharge.objects.all()

	for d in dis:
		if clientEqual(client, d) == True:
			results.append(d)
	return results

def hasIncompleteDischarge(client):
	hasIncomplete = False
	d_list = grabClientDischargeForms(client)
	for d in d_list:
		if d.isComplete == False:
			hasIncomplete = True
			break
	return hasIncomplete

def getClientIncompleteDischarge(client):
	result = None
	d_list = grabClientDischargeForms(client)

	for d in d_list:
		if d.isComplete == False:
			result = d
			break
	return result

def newDischarge(client):
	date = datetime.now()
	date = date.date()
	d = Discharge(client=client, date_of_assessment=date)
	d.save()
	return d

def startDischarge(client):
	result = {}

	if hasIncompleteDischarge(client) == True:
		result['discharge'] = getClientIncompleteDischarge(client)
		result['isNew'] = False
	else:
		result['discharge'] = newDischarge(client)
		result['isNew'] = True

	return result

def getDischargeFields(discharge):
	fields = {}
	fields['reasonRefered'] 	= discharge.reasonRefered
	fields['diagnosis'] 		= discharge.diagnosis
	fields['reasonTerminated'] 	= discharge.reasonTerminated
	fields['clientAttitude'] 	= discharge.clientAttitude
	fields['recommendations'] 	= discharge.recommendations
	return fields

def saveDischarge(request, discharge):
	discharge.reasonRefered 	= request.POST.get('reasonRefered')
	discharge.diagnosis 		= request.POST.get('diagnosis')
	discharge.reasonTerminated 	= request.POST.get('reasonTerminated')
	discharge.clientAttitude 	= request.POST.get('clientAttitude')
	discharge.recommendations 	= request.POST.get('recommendations')
	discharge.save()

def refreshDischarge(discharge):
	discharge.reasonRefered 	= ''
	discharge.diagnosis 		= ''
	discharge.reasonTerminated 	= ''
	discharge.clientAttitude 	= ''
	discharge.recommendations	= ''
	ut.save()

def finishDischarge(discharge):
	discharge.isComplete = True
	discharge.save()

def beginDischarge(request):
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	client = Client.objects.get(id=client_id)
	session = ClientSession.objects.get(id=session_id)

	action = startDischarge(client)
	d = action['discharge']
	setGlobalID(d.id)

	openForm('discharge', d, client)

	result['discharge'] = d
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | Client Discharge"
	result['save_this'] = 'false'

	if action['isNew'] == False:
		result['form'] = d
		result['form_type'] = 'discharge'
		result['type_header'] = 'Client Discharge'

	return result

def processDischargeData(request):
	result = {}

	session_id = request.POST.get('session_id', '')
	d_id = request.POST.get('d_id', '')
	save_this = request.POST.get('save_this', '')

	session = ClientSession.objects.get(id=session_id)
	d = Discharge.objects.get(id=d_id)
	fields = getDischargeFields(d)
	json_data = json.dumps(fields)

	if save_this == 'true':
		saveDischarge(request, d)
		finishUT(ut)

	result['session'] = session
	result['discharge'] = d
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | Client Discharge"

	return result



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
############################################################ END DISCHARGE ################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



###########################################################################################################################################
#*****************************************************************************************************************************************#
#------------------------------------------------------------- URINE TEST ----------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


def grabClientUtForms(client):
	results = []
	uts = UrineResults.objects.all()

	for u in uts:
		if clientEqual(client, u) == True:
			results.append(u)
	return results

def hasIncompleteUT(client):
	hasIncomplete = False
	ut_list = grabClientUtForms(client)
	for u in ut_list:
		if u.isComplete == False:
			hasIncomplete = True
			break
	return hasIncomplete

def getClientIncompleteUt(client):
	result = None
	ut_list = grabClientUtForms(client)

	for u in ut_list:
		if u.isComplete == False:
			result = u
			break
	return result

def newUT(client):
	date = datetime.now()
	date = date.date()
	ut = UrineResults(client=client, date_of_assessment=date)
	ut.save()
	return ut

def startUT(client):
	result = {}

	if hasIncompleteUT(client) == True:
		result['ut'] = getClientIncompleteUt(client)
		result['isNew'] = False
	else:
		result['ut'] = newUT(client)
		result['isNew'] = True

	return result

def getUtFields(ut):
	fields = {}
	fields['drug1'] = ut.drug1
	fields['drug2'] = ut.drug2
	fields['drug3'] = ut.drug3
	fields['drug4'] = ut.drug4
	fields['drug5'] = ut.drug5
	fields['drug6'] = ut.drug6
	fields['drug7'] = ut.drug7
	fields['drug8'] = ut.drug8
	fields['drug9'] = ut.drug9
	fields['drug10'] = ut.drug10
	fields['drug11'] = ut.drug11
	return fields

def saveUT(request, ut):
	ut.drug1 = truePythonBool(request.POST.get('drug1'))
	ut.drug2 = truePythonBool(request.POST.get('drug2'))
	ut.drug3 = truePythonBool(request.POST.get('drug3'))
	ut.drug4 = truePythonBool(request.POST.get('drug4'))
	ut.drug5 = truePythonBool(request.POST.get('drug5'))
	ut.drug6 = truePythonBool(request.POST.get('drug6'))
	ut.drug7 = truePythonBool(request.POST.get('drug7'))
	ut.drug8 = truePythonBool(request.POST.get('drug8'))
	ut.drug9 = truePythonBool(request.POST.get('drug9'))
	ut.drug10 = truePythonBool(request.POST.get('drug10'))
	ut.drug11 = truePythonBool(request.POST.get('drug11'))
	ut.save()

def refreshUT(ut):
	ut.drug1 = False
	ut.drug2 = False
	ut.drug3 = False
	ut.drug4 = False
	ut.drug5 = False
	ut.drug6 = False
	ut.drug7 = False
	ut.drug8 = False
	ut.drug9 = False
	ut.drug10 = False
	ut.drug11 = False
	ut.save()

def finishUT(ut):
	ut.isComplete = True
	ut.save()

def beginUT(request):
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	client = Client.objects.get(id=client_id)
	session = ClientSession.objects.get(id=session_id)

	action = startUT(client)
	ut = action['ut']
	setGlobalID(ut.id)

	openForm('ut', ut, client)

	result['ut'] = ut
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | Urine Analysis"
	result['save_this'] = 'false'

	if action['isNew'] == False:
		result['form'] = ut
		result['form_type'] = 'ut'
		result['type_header'] = 'Urine Analysis'

	return result

def processUtData(request):
	result = {}

	session_id = request.POST.get('session_id', '')
	ut_id = request.POST.get('ut_id', '')
	save_this = request.POST.get('save_this', '')

	session = ClientSession.objects.get(id=session_id)
	ut = UrineResults.objects.get(id=asi_id)
	fields = getUtFields(ut)
	json_data = json.dumps(fields)

	if save_this == 'true':
		saveUT(request, ut)
		finishUT(ut)

	result['session'] = session
	result['ut'] = ut
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | Urine Test Analysis"

	return result

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
############################################################ END DISCHARGE ################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


###########################################################################################################################################
#*****************************************************************************************************************************************#
#---------------------------------------------------------- OPEN/CLOSE FORMS -------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################

def formEqual(f1, f2):
	formEqual = False
	if str(f1.id) == str(f2.id) and str(f1.date_of_assessment) == str(f2.date_of_assessment) and clientEqual(f1.client, f2.client):
		formEqual = True
	return formEqual

def formIsOpen(form):
	opened = False
	if form.isOpen == True:
		opened = True
	return opened

def hasOpened(form_list):
	exist = False

	for f in form_list:
		if f.isOpen == True:
			exist = True
			break
	return exist

def getOpenedForm(form_list):
	form = None

	for f in form_list:
		if f.isOpen == True:
			form = f
			break
	return form


def grabClientOpenForm(client, form_type):
	result = None

	if str(form_type) == 'am':
		ams = grabClientAMForms(client)

		if hasOpened(ams) == True:
			result = getOpenedForm(ams)

	elif str(form_type) == 'sap':
		saps = grabClientSAPForms(client)

		if hasOpened(saps) == True:
			result = getOpenedForm(saps)

	elif str(form_type) == 'mh':
		mhs = grabClientMHForms(client)

		if hasOpened(mhs) == True:
			result = getOpenedForm(mhs)

	elif str(form_type) == 'asi':
		asis = grabClientAsiForms(client)

		if hasOpened(asis) == True:
			result = getOpenedForm(asis)

	elif str(form_type) == 'ut':
		uts = grabClientUtForms(client)

		if hasOpened(uts) == True:
			result = getOpenedForm(uts)

	return result


def grabOpenForm():
	result = {}
	result['type'] = None
	result['form'] = None
	match = False

	am = AngerManagement.objects.all()

	for a in am:
		if a.isOpen == True:
			result['type'] = 'am'
			result['form'] = a
			match = True
			break

	if match == False:
		sap = SAP.objects.all()

		for s in sap:
			if s.isOpen == True:
				result['type'] = 'sap'
				result['form'] = s
				match = True
				break

	if match == False:
		mh = MentalHealth.objects.all()

		for m in mh:
			if m.isOpen == True:
				result['type'] = 'mh'
				result['form'] = m
				match = True
				break

	if match == False:
		asi = ASI.objects.all()

		for ai in asi:
			if asi.isOpen == True:
				result['type'] = 'asi'
				result['form'] = ai
				match = True
				break

	if match == False:
		ut = UrineResults.objects.all()

		for u in ut:
			if u.isOpen == True:
				result['type'] = 'ut'
				result['form'] = u
				match = True
				break


	return result

def openForm(form_type, form, client):
	ams = grabClientAMForms(client)
	saps = grabClientSAPForms(client)
	mhs = grabClientMHForms(client)
	asis = grabClientASIForms(client)
	uts = grabClientUtForms(client)
	dis = grabClientDischargeForms(client)

	if str(form_type) == 'am':
		if ams != None:
			for a in ams:
				if str(form.id) == str(a.id):
					a.isOpen = True
					a.save()
				else:
					a.isOpen = False
					a.save()
			for s in saps:
				s.isOpen = False
				s.save()
			for m in  mhs:
				m.isOpen = False
				m.save()
			for u in uts:
				u.isOpen = False
				u.save()
			for ai in asis:
				ai.isOpen = False
				ai.save()
			for d in dis:
				d.isOpen = False
				d.save()

	elif str(form_type) == 'sap':
		if saps != None:
			for s in saps:
				if str(form.id) == str(s.id):
					s.isOpen = True
					s.save()
				else:
					s.isOpen = False
					s.save()
			for a in ams:
				a.isOpen = False
				a.save()
			for m in  mhs:
				m.isOpen = False
				m.save()
			for u in uts:
				u.isOpen = False
				u.save()
			for ai in asis:
				ai.isOpen = False
				ai.save()
			for d in dis:
				d.isOpen = False
				d.save()

	elif str(form_type) == 'mh':
		if mhs != None:
			for m in mhs:
				if str(form.id) == str(m.id):
					m.isOpen = True
					m.save()
				else:
					m.isOpen = False
					m.save()
			for a in ams:
				a.isOpen = False
				a.save()
			for s in  saps:
				s.isOpen = False
				s.save()
			for u in uts:
				u.isOpen = False
				u.save()
			for ai in asis:
				ai.isOpen = False
				ai.save()
			for d in dis:
				d.isOpen = False
				d.save()

	elif str(form_type) == 'asi':
		if asis != None:
			for ai in asis:
				if str(form.id) == str(ai.id):
					ai.isOpen = True
					ai.save()
				else:
					ai.isOpen = False
					ai.save()
			for a in ams:
				a.isOpen = False
				a.save()
			for s in  saps:
				s.isOpen = False
				s.save()
			for u in uts:
				u.isOpen = False
				u.save()
			for m in  mhs:
				m.isOpen = False
				m.save()
			for d in dis:
				d.isOpen = False
				d.save()

	elif str(form_type) == 'ut':
		if uts != None:
			for u in uts:
				if str(form.id) == str(u.id):
					u.isOpen = True
					u.save()
				else:
					u.isOpen = False
					u.save()
			for a in ams:
				a.isOpen = False
				a.save()
			for m in  mhs:
				m.isOpen = False
				m.save()
			for s in saps:
				s.isOpen = False
				s.save()
			for ai in asis:
				ai.isOpen = False
				ai.save()
			for d in dis:
				d.isOpen = False
				d.save()

	elif str(form_type) == 'discharge':
		if dis != None:
			for d in dis:
				if str(form.id) == str(d.id):
					d.isOpen = True
					d.save()
				else:
					d.isOpen = False
					d.save()
			for a in ams:
				a.isOpen = False
				a.save()
			for m in  mhs:
				m.isOpen = False
				m.save()
			for s in saps:
				s.isOpen = False
				s.save()
			for ai in asis:
				ai.isOpen = False
				ai.save()
			for u in uts:
				u.isOpen = False
				u.save()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
############################################################## END OPEN/CLOSE #############################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#




###########################################################################################################################################
#*****************************************************************************************************************************************#
#------------------------------------------------------- UNIVERSAL FUNCTIONS -------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


###########################################################################################################################################
#*****************************************************************************************************************************************#
#------------------------------------------------------- UNIVERSAL FUNCTIONS -------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


###########################################################################################################################################
#*****************************************************************************************************************************************#
#------------------------------------------------------- UNIVERSAL FUNCTIONS -------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################


###########################################################################################################################################
#*****************************************************************************************************************************************#
#------------------------------------------------------- UNIVERSAL FUNCTIONS -------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################

def grabGenericForm(form_type, form_id):
	form = None

	if str(form_type) == 'am':
		form = AngerManagement.objects.get(id=form_id)
	elif str(form_type) == 'sap':
		form = SAP.objects.get(id=form_id)
	elif str(form_type) == 'mh':
		form = MentalHealth.objects.get(id=form_id)
	elif str(form_type) == 'ut':
		form = UrineResults.objects.get(id=form_id)
	elif str(form_type) == 'asi':
		form = ASI.objects.get(id=form_id)
	elif str(form_type) == 'discharge':
		form = Discharge.objects.get(id=form_id)

	return form

def deleteGenericForm(form_type, form):
	if form_type == 'am':
		deleteAM(form)
	elif form_type == 'sap':
		deleteSap(form)
	elif form_type == 'mh':
		deleteMh(form)
	elif form_type == 'asi':
		deleteASI(form)

def universalLocation(form_type, form_id):
	location = None

	if str(form_type) == 'am':
		am = AngerManagement.objects.get(id=form_id)
		nextAmPage(am, None)
	elif str(form_type) == 'sap':
		sap = SAP.objects.get(id=form_id)
		location = nextSAPage(sap, None)
	elif str(form_type) == 'mh':
		mh = MentalHealth.objects.get(id=form_id)
		location = nextMhPage(mh, None)
	elif str(form_type) == 'ut':
		ut = UrineResults.objects.get(id=form_id)

	return location

def universalRefresh(form_type, form):
	if str(form_type) == 'am':
		refreshAM(form)
	elif str(form_type) == 'sap':
		refreshSap(form)
	elif str(form_type) == 'mh':
		refreshMh(form)
	elif str(form_type) == 'asi':
		refreshASI(form)

def universalSaveForm(request, form_type, section, form):
	if form_type == 'am':
		no = None
	elif form_type == 'sap':
		no = None
	elif form_type == 'mh':
		saveMentalHealth(request, section, form)
	elif form_type == 'asi':
		saveASI(request, section, form)

def universalSaveFinishForm(request, form_type, section, form):
	if form_type == 'am':
		no = None
	elif form_type == 'sap':
		no = None
	elif form_type == 'mh':
		saveMentalHealth(request, section, form)
		finishMhSection(form, section)
	elif form_type == 'asi':
		saveASI(request, section, form)
		setASIcomplete(section, form)

def universalContent(request, form_type, gField):
	## TAKES DJANGO REQUEST, THE TYPE OF FORM BEING PROCESSED AND THE SECTION FOR WHICH YOU ARE REQUESTING THE FIELDS
	## THIS FUNCTION SAVES THE FORM'S SECTION IF CONDITIONS ARE MET
	## RETURNS ALL THE CONTENT ASSOCIATED WITH THE FORM AND SECTION (INCLUDING THE FORM AND SESSION)
	result = None

	if form_type == 'am':
		no = None
	elif form_type == 'sap':
		no = None
	elif form_type == 'mh':
		result = processMhData(request, gField)

	return result

def universalGrabFields(form_type, section, form):
	form_type = str(form_type)
	section = str(section)
	result = {}

	if form_type == 'am':
		result = getAMFields(form, section)
	elif form_type == 'mh':
		result = getMhFields(form, section)
	elif form_type == 'asi':
		result = grabASIFields(form, section)
	elif form_type == 'sap':
		result = None

	return result

def universalStartForm(form_type, client):
	form_type = str(form_type)
	result = None

	if form_type == 'am':
		result = startAM(client)
	elif form_type == 'mh':
		result = startMH(client)
	elif form_type == 'sap':
		result = getSAP(client)
	elif form_type == 'asi':
		result = startASI(client)

	return result

############################################################################################
	              ##MUST WRITE DELETE METHOD FOR OTHER FORMS AS CREATED
############################################################################################

def setGlobalID(the_id):
	gloVar = Global_ID.objects.get(id=1)
	gloVar.global_id = the_id
	gloVar.save()

def getGlobalID():
	gloVar = Global_ID.objects.get(id=1)
	return gloVar.global_id

def decodeCharfield(text):
	result = []
	temp = ''

	for t in text:
		if str(t) != '~':
			temp += t
		else:
			result.append(temp)
			temp = ''

	return result

def startForm(request, form_type):
	form_type = str(form_type)
	result = None

	if form_type == 'am':
		result = beginAM(request)

	elif form_type == 'mh':
		result = beginMH(request)

	elif form_type == 'sap':
		result = beginSAP(request)

	elif form_type == 'asi':
		result = beginASI(request)

	elif form_type == 'ut':
		result = beginUT(request)

	elif form_type == 'ut':
		result = beginDischarge(request)

	return result

def fetchUrl(form_type, current_page, form):
	url = None
	form_type = str(form_type)

	if form_type == 'am':
		url = nextAmPage(form, current_page)
	elif form_type == 'sap':
		url = nextSAPage(form, current_page)
	elif form_type == 'mh':
		url = nextMhPage(form, current_page)
	elif form_type == 'asi':
		url = nextAsiPage(form, current_page)

	return url

def fetchContent(request, form_type, current_section):
	current_section = str(current_section)
	content = None

	if form_type == 'am':
		content = processAMData(request, current_section)
	elif form_type == 'sap':
		content = processSapData(request, current_section)
	elif form_type == 'mh':
		content = processMhData(request, current_section)
	elif form_type == 'asi':
		content = processAsiData(request, current_section)
	elif form_type == 'ut':
		content = processUtData(request)
	elif form_type == 'discharge':
		content = processDischargeData(request)

	return content

def saveForm(request, form_type, section, form):
	if form_type == 'am':
		saveCompletedAmSection(request, section, form)
	elif form_type == 'sap':
		saveSap(request, section, form)
	elif form_type == 'mh':
		saveMentalHealth(request, section, form)
	elif form_type == 'asi':
		saveASI(request, section, form)
	elif form_type == 'ut':
		saveUT(request, section, form)
	elif form_type == 'discharge':
		saveDischarge(request, discharge)

def saveAndFinish(request, form_type, section, form):
	if form_type == 'am':
		saveCompletedAmSection(request, section, form)
		setAmSectionComplete(form, section)
	elif form_type == 'sap':
		saveSap(request, section, form)
		setSapSectionComplete(form, section)
	elif form_type == 'mh':
		saveMentalHealth(request, section, form)
		finishMhSection(form, section)
	elif form_type == 'asi':
		saveASI(request, section, form)
		setASIcomplete(section, form)
	elif form_type == 'ut':
		saveUT(request, form)
		finishUT(form)
	elif form_type == 'discharge':
		saveDischarge(request, discharge)
		finishDischarge(form)

def fetchForm(form_type, form_id):
	form = None

	if str(form_type) == 'am':
		form = AngerManagement.objects.get(id=form_id)
	elif str(form_type) == 'sap':
		form = SAP.objects.get(id=form_id)
	elif str(form_type) == 'mh':
		form = MentalHealth.objects.get(id=form_id)
	elif str(form_type) == 'asi':
		form = ASI.objects.get(id=form_id)
	elif str(form_type) == 'ut':
		form = UrineResults.objects.get(id=form_id)
	elif str(form_type) == 'discharge':
		form = Discharge.objects.get(id=form_id)

	return form

def deleteForm(form_type, form):
	form_type = str(form_type)

	if form_type == 'am':
		deleteAM(form)
	elif form_type == 'sap':
		deleteSap(form)
	elif form_type == 'mh':
		deleteMh(form)
	elif form_type == 'asi':
		deleteASI(form)
	elif form_type == 'ut' or form_type == 'discharge':
		form.delete()

def refreshForm(form_type, form):
	if str(form_type) == 'am':
		refreshAM(form)
	elif str(form_type) == 'sap':
		refreshSap(form)
	elif str(form_type) == 'mh':
		refreshMh(form)
	elif str(form_type) == 'asi':
		refreshASI(form)
	elif str(form_type) == 'ut':
		refreshUT(form)
	elif str(form_type) == 'discharge':
		refreshDischarge(form)

def force_URL_priority(form_type, section, form):
	form_type = str(form_type)

	if form_type == 'asi':
		asiPriority(form, section)
	elif form_type == 'sap':
		prioritySapSection(section, form)
	elif form_type == 'mh':
		setMhPriority(form, section)
	elif form_type == 'am':
		setAmPriorityURL(section, form)

def milHr_toStd(hr):
	result = ''
	hr = str(hr)
	if hr == '01' or hr == '13':
		result = '1'
	elif hr == '02' or hr == '14':
		result = '2'
	elif hr == '03' or hr == '15':
		result = '3'
	elif hr == '04' or hr == '16':
		result = '4'
	elif hr == '05' or hr == '17':
		result = '5'
	elif hr == '06' or hr == '18':
		result = '6'
	elif hr == '07' or hr == '19':
		result = '7'
	elif hr == '08' or hr == '20':
		result = '8'
	elif hr == '09' or hr == '21':
		result = '9'
	elif hr == '10' or hr == '22':
		result = '10'
	elif hr == '11' or hr == '23':
		result = '11'
	elif hr == '12' or hr == '00':
		result = '12'
	return result


def millitary_to_std(time):
	result = ''
	hr = ''
	ampm = 'am'
	time = str(time)
	hr += time[0]
	hr += time[1]

	if int(hr) > 11:
		ampm = 'pm'

	hr = milHr_toStd(hr)

	result = str(hr) + str(time[2]) + str(time[3]) + str(time[4]) + ampm
	return result




















	
























