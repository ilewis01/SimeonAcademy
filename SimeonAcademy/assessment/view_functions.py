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

from assessment.models import State, RefReason, Client, MaritalStatus, \
LivingSituation, AngerManagement, EducationLevel, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, UseTable, \
FamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_AngerHistory2, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHFamily, MHEducation, \
MHRelationship, MHActivity, MHStressor, MHLegalHistory, ClientSession, \
Invoice, SType, AM_AngerHistory3

def onTrue_offFalse(data):
	if data == 'on':
		data = True
	else:
		data = False
	return data

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

def forceNextSection(am):
	result = None
	print "INSIDE FUNCTION COMPLETE: " + str()

	demographicComplete = am.demographicComplete
	drugHistoryComplete = am.drugHistoryComplete
	childhoodComplete = am.childhoodComplete
	angerHistoryComplete = am.angerHistoryComplete
	angerHistoryComplete2 = am.angerHistoryComplete2
	angerHistoryComplete3 = am.angerHistoryComplete3
	connectionsComplete = am.connectionsComplete
	worstComplete = am.worstComplete
	angerTargetComplete = am.angerTargetComplete
	familyOriginComplete = am.familyOriginComplete
	currentProblemsComplete = am.currentProblemsComplete
	controlComplete = am.controlComplete
	finalComplete = am.finalComplete

	if demographicComplete == False:
		result = '/am_demographic/'
			
	elif drugHistoryComplete == False:
		result = '/am_drugHistory/'
			
	elif childhoodComplete == False:
		result = '/am_childhood/'
			
	elif angerHistoryComplete == False:
		result = '/am_angerHistory/'
			
	elif angerHistoryComplete2 == False:
		result = '/am_angerHistory2/'
			
	elif angerHistoryComplete3 == False:
		result = '/am_angerHistory3/'
			
	elif connectionsComplete == False:
		result = '/am_connections/'
			
	elif worstComplete == False:
		result = '/am_worst/'
			
	elif angerTargetComplete == False:
		result = '/am_angerTarget/'
			
	elif familyOriginComplete == False:
		result = '/am_familyOrigin/'

	elif currentProblemsComplete == False:
		result = '/am_problems/'
			
	elif controlComplete == False:
		result = '/am_control/'
			
	elif finalComplete == False:
		result = '/am_final/'			
	else:
		result = '/am_viewForm/'

	return result

def grabProperNextSection(am, current):
	result = None

	demographicComplete = am.demographicComplete
	drugHistoryComplete = am.drugHistoryComplete
	childhoodComplete = am.childhoodComplete
	angerHistoryComplete = am.angerHistoryComplete
	angerHistoryComplete2 = am.angerHistoryComplete2
	angerHistoryComplete3 = am.angerHistoryComplete3
	connectionsComplete = am.connectionsComplete
	worstComplete = am.worstComplete
	angerTargetComplete = am.angerTargetComplete
	familyOriginComplete = am.familyOriginComplete
	currentProblemsComplete = am.currentProblemsComplete
	controlComplete = am.controlComplete
	finalComplete = am.finalComplete

	if demographicComplete == False:
		result = '/am_demographic/'

		if str(current) == str(result):
			am.demographicComplete = True
			am.save()
			result = forceNextSection(am)

			am.demographicComplete = False
			am.save()
			
	elif drugHistoryComplete == False:
		result = '/am_drugHistory/'

		if str(current) == str(result):
			am.drugHistoryComplete = True
			am.save()
			result = forceNextSection(am)

			am.drugHistoryComplete = False
			am.save()
			
	elif childhoodComplete == False:
		result = '/am_childhood/'

		if str(current) == str(result):
			am.childhoodComplete = True
			am.save()
			result = forceNextSection(am)

			am.childhoodComplete = False
			am.save()
			
	elif angerHistoryComplete == False:
		result = '/am_angerHistory/'

		if str(current) == str(result):
			am.angerHistoryComplete = True
			am.save()
			result = forceNextSection(am)

			am.angerHistoryComplete = False
			am.save()
			
	elif angerHistoryComplete2 == False:
		result = '/am_angerHistory2/'

		if str(current) == str(result):
			am.angerHistoryComplete2 = True
			am.save()
			result = forceNextSection(am)

			am.angerHistoryComplete2 = False
			am.save()
			
	elif angerHistoryComplete3 == False:
		result = '/am_angerHistory3/'

		if str(current) == str(result):
			am.angerHistoryComplete3 = True
			am.save()
			result = forceNextSection(am)

			am.angerHistoryComplete3 = False
			am.save()
			
	elif connectionsComplete == False:
		result = '/am_connections/'

		if str(current) == str(result):
			am.connectionsComplete = True
			am.save()
			result = forceNextSection(am)

			am.connectionsComplete = False
			am.save()
			
	elif worstComplete == False:
		result = '/am_worst/'

		if str(current) == str(result):
			am.worstComplete = True
			am.save()
			result = forceNextSection(am)

			am.worstComplete = False
			am.save()
			
	elif angerTargetComplete == False:
		result = '/am_angerTarget/'

		if str(current) == str(result):
			am.angerTargetComplete = True
			am.save()
			result = forceNextSection(am)

			am.angerTargetComplete = False
			am.save()
			
	elif familyOriginComplete == False:
		result = '/am_familyOrigin/'

		if str(current) == str(result):
			am.familyOriginComplete = True
			am.save()
			result = forceNextSection(am)

			am.familyOriginComplete = False
			am.save()
			
	elif currentProblemsComplete == False:
		result = '/am_problems/'

		if str(current) == str(result):
			am.currentProblemsComplete = True
			am.save()
			result = forceNextSection(am)

			am.currentProblemsComplete = False
			am.save()
			
	elif controlComplete == False:
		result = '/am_control/'

		if str(current) == str(result):
			am.controlComplete = True
			am.save()
			result = forceNextSection(am)

			am.controlComplete = False
			am.save()
			
	elif finalComplete == False:
		result = '/am_final/'

		if str(current) == str(result):
			am.finalComplete = True
			am.save()
			result = forceNextSection(am)

			am.finalComplete = False
			am.save()			
	else:
		result = '/am_viewForm/'

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
		am.childhoodComplete = True
		am.save()

	elif section == '/am_angerHistory/':
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

		ah1 = am.angerHistory

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
		am.angerHistoryComplete = True
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
		am.angerHistoryComplete2 = True
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
		am.worstComplete = True
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
		am.drugHistoryComplete = True
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
		am.angerHistoryComplete3 = True
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
		am.currentProblemsComplete = True
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
		am.familyOriginComplete = True
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

		#SET DROP DOWN MENU VALUES
		maritalStatus = MaritalStatus.objects.get(id=maritalStatus)
		livingSituation = LivingSituation.objects.get(id=livingSituation)
		education = EducationLevel.objects.get(id=education)

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
		am.demographicComplete = True
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
		am.angerTargetComplete = True
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
		am.controlComplete = True
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

		am.connectionsComplete = True
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

		am.finalComplete = True
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

	classes['demo'] = processCompletedClass(am['demographicComplete'], 'demo', m_page, green, current, normal)
	classes['dh'] = processCompletedClass(am['drugHistoryComplete'], 'dh', m_page, green, current, normal)
	classes['child'] = processCompletedClass(am['childhoodComplete'], 'child', m_page, green, current, normal)
	classes['ah1'] = processCompletedClass(am['angerHistoryComplete'], 'ah1', m_page, green, current, normal)
	classes['ah2'] = processCompletedClass(am['angerHistoryComplete2'], 'ah2', m_page, green, current, normal)
	classes['ah3'] = processCompletedClass(am['angerHistoryComplete3'], 'ah3', m_page, green, current, normal)
	classes['connect'] = processCompletedClass(am['connectionsComplete'], 'connect', m_page, green, current, normal)
	classes['worst'] = processCompletedClass(am['worstComplete'], 'worst', m_page, green, current, normal)
	classes['target'] = processCompletedClass(am['angerTargetComplete'], 'target', m_page, green, current, normal)
	classes['family'] = processCompletedClass(am['familyOriginComplete'], 'family', m_page, green, current, normal)
	classes['current'] = processCompletedClass(am['currentProblemsComplete'], 'current', m_page, green, current, normal)
	classes['control'] = processCompletedClass(am['controlComplete'], 'control', m_page, green, current, normal)
	classes['final'] = processCompletedClass(am['finalComplete'], 'final', m_page, green, current, normal)

	return classes

def refreshAM(am):
	if am.demographicComplete == True:
		date = datetime.now()
		date = date.date()
		am.demographic.delete()
		demo = AM_Demographic(client_id=am.client.clientID, date_of_assessment=date)
		demo.save()
		am.demographic = demo
		am.demographicComplete = False
		am.save()

	if am.drugHistoryComplete == True:
		am.drugHistory.delete()
		drugHistory = AM_DrugHistory(client_id=am.client.clientID, finishedTreatment=True)
		drugHistory.save()
		am.drugHistory = drugHistory
		am.drugHistoryComplete = False
		am.save()

	if am.childhoodComplete == True:
		am.childhood.delete()
		childhood = AM_ChildhoodHistory(client_id=am.client.clientID)
		childhood.save()
		am.childhood = childhood
		am.childhoodComplete = False
		am.save()

	if am.angerHistoryComplete == True:
		am.angerHistory.delete()
		angerHistory = AM_AngerHistory(client_id=am.client.clientID)
		angerHistory.save()
		am.angerHistory = angerHistory
		am.angerHistoryComplete = False
		am.save()

	if am.angerHistoryComplete2 == True:
		am.angerHistory2.delete()
		angerHistory2 = AM_AngerHistory2(client_id=am.client.clientID)
		angerHistory2.save()
		am.angerHistory2 = angerHistory2
		am.angerHistoryComplete2 = False
		am.save()

	if am.angerHistoryComplete3 == True:
		am.angerHistory3.delete()
		angerHistory3 = AM_AngerHistory3(client_id=am.client.clientID)
		angerHistory3.save()
		am.angerHistory3 = angerHistory3
		am.angerHistoryComplete3 = False
		am.save()

	if am.connectionsComplete == True:
		am.connections.delete()
		connections = AM_Connections(client_id=am.client.clientID)
		connections.save()
		am.connections = connections
		am.connectionsComplete = False
		am.save()

	if am.worstComplete == True:
		am.worstEpisode.delete()
		worstEpisode = AM_WorstEpisode(client_id=am.client.clientID)
		worstEpisode.save()
		am.worstEpisode = worstEpisode
		am.worstComplete = False
		am.save()

	if am.angerTargetComplete == True:
		am.angerTarget.delete()
		angerTarget = AM_AngerTarget(client_id=am.client.clientID)
		angerTarget.save()
		am.angerTarget = angerTarget
		am.angerTargetComplete = False
		am.save()

	if am.familyOriginComplete == True:
		am.familyOrigin.delete()
		familyOrigin = AM_FamilyOrigin(client_id=am.client.clientID)
		familyOrigin.save()
		am.familyOrigin = familyOrigin
		am.familyOriginComplete = False
		am.save()

	if am.currentProblemsComplete == True:
		am.currentProblems.delete()
		currentProblems = AM_CurrentProblem(client_id=am.client.clientID)
		currentProblems.save()
		am.currentProblems = currentProblems
		am.currentProblemsComplete = False
		am.save()

	if am.controlComplete == True:
		am.control.delete()
		control = AM_Control(client_id=am.client.clientID)
		control.save()
		am.control = control
		am.controlComplete = False
		am.save()

	if am.finalComplete == True:
		am.final.delete()
		final = AM_Final(client_id=am.client.clientID)
		final.save()
		am.final = final
		am.finalComplete = False
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

	if am.demographic.maritalStatus == None:
		data['maritalStatus'] = 0
	else:
		data['maritalStatus'] = convertMaritalToIndex(am.demographic.maritalStatus.status)

	if am.demographic.livingSituation == None:
		data['livingSituation'] = 0
	else:
		data['livingSituation'] = convertLivingToIndex(am.demographic.livingSituation.situation)

	if am.demographic.education == None:
		data['education'] = 0
	else:
		data['education'] = convertEducationToIndex(am.demographic.education.level)

	if am.demographic.employer_phone == None:
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
	fields = None

	if location == 'counselor/forms/AngerManagement/demographic.html':
		fields = getAMDemoFields(am)
	elif location == 'counselor/forms/AngerManagement/drugHistory.html':
		fields = grabAmDhFields(am)
	elif location == 'counselor/forms/AngerManagement/childhoodHistory.html':
		fields = grabAmChildhood(am)
	elif location == 'counselor/forms/AngerManagement/angerHistory.html':
		fields = grabAmAngerHistory1(am)
	elif location == 'counselor/forms/AngerManagement/angerHistory2.html':
		fields = grabAmAngerHistory2(am)
	elif location == 'counselor/forms/AngerManagement/angerHistory3.html':
		fields = grabAmAngerHistory3(am)
	elif location == 'counselor/forms/AngerManagement/AngerTarget.html':
		fields = grabAmTarget(am)
	elif location == 'counselor/forms/AngerManagement/connections.html':
		fields = grabAmConnections(am)
	elif location == 'counselor/forms/AngerManagement/control.html':
		fields = grabAmControl(am)
	elif location == 'counselor/forms/AngerManagement/currentProblems.html':
		fields = grabAmCurrentProblems(am)
	elif location == 'counselor/forms/AngerManagement/familyOrigin.html':
		fields = grabAmFamilyOrigin(am)
	elif location == 'counselor/forms/AngerManagement/worstEpisodes.html':
		fields = grabAmWorstEpisodes(am)
	elif location == 'counselor/forms/AngerManagement/final.html':
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


def startAM(client):
	results = {}
	back = "false"
	create_new = True
	am = None

	if hasAM(client) == True:
		amList = AngerManagement.objects.all()

		for a in amList:
			if (a.AMComplete == False) and (str(a.client.clientID) == str(client.clientID)):
				create_new = False
				back = "true"
				am = a
				break

	if create_new == True:
		am = newAM(client)

	results['back'] = back
	results['am'] = am
	results['isNew'] = create_new

	return results

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

def continueToAmSection(am):
	location = None

	if am.demographicComplete == False:
		location = 'counselor/forms/AngerManagement/demographic.html'
	elif am.drugHistoryComplete == False:
		location = 'counselor/forms/AngerManagement/drugHistory.html'
	elif am.childhoodComplete == False:
		location = 'counselor/forms/AngerManagement/childhoodHistory.html'
	elif am.connectionsComplete == False:
		location = 'counselor/forms/AngerManagement/connections.html'
	elif am.worstComplete == False:
		location = 'counselor/forms/AngerManagement/worstEpisodes.html'
	elif am.angerTargetComplete == False:
		location = 'counselor/forms/AngerManagement/AngerTarget.html'
	elif am.familyOriginComplete == False:
		location = 'counselor/forms/AngerManagement/familyOrigin.html'
	elif am.currentProblemsComplete == False:
		location = 'counselor/forms/AngerManagement/currentProblems.html'
	elif am.controlComplete == False:
		location = 'counselor/forms/AngerManagement/control.html'
	elif am.finalComplete == False:
		location = 'counselor/forms/AngerManagement/final.html'
	elif am.finalComplete == False:
		location = 'counselor/forms/AngerManagement/angerHistory.html'
	elif am.finalComplete == False:
		location = 'counselor/forms/AngerManagement/angerHistory2.html'
	elif am.finalComplete == False:
		location = 'counselor/forms/AngerManagement/angerHistory3.html'

	return location

def continueToMhSection(mh):
	location = None

	if mh.demographicsComplete == False:
		location = 'counselor/forms/MentalHealth/demographic.html'
	elif mh.familyComplete == False:
		location = 'counselor/forms/MentalHealth/familyBackground.html'
	elif mh.educationComplete == False:
		location = 'counselor/forms/MentalHealth/education.html'
	elif mh.relationshipsComplete == False:
		location = 'counselor/forms/MentalHealth/relationships.html'
	elif mh.activitiesComplete == False:
		location = 'counselor/forms/MentalHealth/activity.html'
	elif mh.stressorsComplete == False:
		location = 'counselor/forms/MentalHealth/stressors.html'
	elif mh.familyHistoryComplete == False:
		location = 'counselor/forms/MentalHealth/familyHistory.html'
	elif mh.legalHistoryComplete == False:
		location = 'counselor/forms/MentalHealth/legal.html'
	elif mh.useTableComplete == False:
		location = 'counselor/forms/MentalHealth/useTable.html'

	return location

def continueToSAPSection(sap):
	location = None

	if sap.demoComplet == False:
		location = 'counselor/forms/SAP/demographic.html'
	elif sap.psychoactiveComplet == False:
		location = 'counselor/forms/SAP/psychoactive.html'
	elif sap.specialComplete == False:
		location = 'counselor/forms/SAP/psychoactive2.html'
	elif sap.preFinalComplete == False:
		location = 'counselor/forms/SAP/pre_final.html'
	elif sap.finalComplete == False:
		location = 'counselor/forms/SAP/final.html'

	return location

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


#SAP FUNCTIONS_________________________________________________________________________________
def grabSapImages(sap, page):
	images = {}
	check = "/static/images/green_check.png"
	x = "/static/images/red_x.png"
	progress = "/static/images/yellow_progress.png"

	if sap.demoComplete == True and page != 'demo':
		images['demo_image'] = check
	elif page == 'viewForm':
		images['demo_image'] = check
	elif page == 'demo':
		images['demo_img'] = progress
	else:
		images['demo_img'] = x

	if sap.socialComplete == True and page != 'social':
		images['social_image'] = check
	elif page == 'viewForm':
		images['social_image'] = check
	elif page == 'social':
		images['social_image'] = progress
	else:
		images['social_image'] = x

	if sap.psycho1Complete == True and page != 'psycho1':
		images['psycho1_image'] = check
	elif page == 'viewForm':
		images['psycho1_image'] = check
	elif page == 'psycho1':
		images['psycho1_image'] = progress
	else:
		images['psycho1_image'] = x

	if sap.psycho2Complete == True and page != 'psycho2':
		images['psycho2_image'] = check
	elif page == 'viewForm':
		images['psycho2_image'] = check
	elif page == 'psycho2':
		images['psycho2_image'] = progress
	else:
		images['psycho2_image'] = x

	if sap.specialComplete == True and page != 'special':
		images['special_image'] = check
	elif page == 'viewForm':
		images['special_image'] = check
	elif page == 'special':
		images['special_image'] = progress
	else:
		images['special_image'] = x

	if sap.otherComplete == True and page != 'other':
		images['other_image'] = check
	elif page == 'viewForm':
		images['other_image'] = check
	elif page == 'other':
		images['other_image'] = progress
	else:
		images['other_image'] = x





	
























