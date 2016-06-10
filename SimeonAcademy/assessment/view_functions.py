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
	elif page == 'demo':
		images['demo_img'] = progress
	else:
		images['demo_img'] = x

	if am.drugHistoryComplete == True and page != 'dh':
		images['dh_img'] = check
	elif page == 'dh':
		images['dh_img'] = progress
	else:
		images['dh_img'] = x

	if am.childhoodComplete == True and page != 'child':
		images['child_img'] = check
	elif page == 'child':
		images['child_img'] = progress
	else:
		images['child_img'] = x

	if am.angerHistoryComplete == True and page != 'ah1':
		images['ah1_img'] = check
	elif page == 'ah1':
		images['ah1_img'] = progress
	else:
		images['ah1_img'] = x

	if am.angerHistoryComplete2 == True and page != 'ah2':
		images['ah2_img'] = check
	elif page == 'ah2':
		images['ah2_img'] = progress
	else:
		images['ah2_img'] = x

	if am.angerHistoryComplete3 == True and page != 'ah3':
		images['ah3_img'] = check
	elif page == 'ah3':
		images['ah3_img'] = progress
	else:
		images['ah3_img'] = x

	if am.connectionsComplete == True and page != 'connect':
		images['connect_img'] = check
	elif page == 'connect':
		images['connect_img'] = progress
	else:
		images['connect_img'] = x

	if am.worstComplete == True and page != 'worst':
		images['worst_img'] = check
	elif page == 'worst':
		images['worst_img'] = progress
	else:
		images['worst_img'] = x

	if am.angerTargetComplete == True and page != 'target':
		images['target_img'] = check
	elif page == 'target':
		images['target_img'] = progress
	else:
		images['target_img'] = x

	if am.familyOriginComplete == True and page != 'family':
		images['family_img'] = check
	elif page == 'family':
		images['family_img'] = progress
	else:
		images['family_img'] = x

	if am.currentProblemsComplete == True and page != 'current':
		images['current_img'] = check
	elif page == 'current':
		images['current_img'] = progress
	else:
		images['current_img'] = x

	if am.controlComplete == True and page != 'control':
		images['control_img'] = check
	elif page == 'control':
		images['control_img'] = progress
	else:
		images['control_img'] = x

	if am.finalComplete == True and page != 'final':
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
	return result

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
	fields['whoWorst'] = am.worstEpisode.whoWorst
	fields['happenedWorst'] = am.worstEpisode.happenedWorst
	fields['wordThoughtWorst'] = am.worstEpisode.wordThoughtWorst
	fields['howStartWorst'] = am.worstEpisode.howStartWorst
	fields['howEndWorst'] = am.worstEpisode.howEndWorst
	fields['useWorst'] = am.worstEpisode.useWorst
	fields['whoDidItFight'] = am.worstEpisode.whoDidItFight
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
	data['employer_phone'] = convertNullTextFields(am.demographic.employer_phone)
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
		fields = None

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





	
























