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
AM_AngerHistory, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHFamily, MHEducation, \
MHRelationship, MHActivity, MHStressor, MHLegalHistory

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

def getClientBySS(ss_num):
	results = []
	clients = Client.objects.all()

	for c in clients:
		if str(ss_num) == str(c.ss_num):
			results.append(c)

	return results

def getClientByID(clientID):
	results = []
	clients = Client.objects.all()

	for c in clients:
		if str(clientID) == str(c.clientID):
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

	for c in clients:
		if str(fname) == str(c.fname) and str(lname) == str(c.lname):
			results.append(c)

	return results

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
	results = {}
	results['exist'] = False
	results['am_demo'] = None

	for d in demographics:
		if str(d.client.id) == str(demo.client.id) and str(d.date_of_assessment) == str(demo.date_of_assessment):
			results['exist'] = True
			results['am_demo'] = d
			break
	return results

def clientAmExist(client):
	ams = AngerManagement.objects.all()
	exist = False

	for a in ams:
		if str(a.demographic.client.fname) == str(client.fname) and str(a.demographic.client.lname) == str(client.lname) and str(a.demographic.client.id) == str(client.id) and str(a.demographic.client.clientID) == str(client.clientID):
			exist = True
			break
	return exist

def getClientAmList(client):
	results = []
	ams = AngerManagement.objects.all()

	if clientAmExist(client) == True:
		for a in ams:
			if str(a.demographic.client.fname) == str(client.fname) and str(a.demographic.client.lname) == str(client.lname) and str(a.demographic.client.id) == str(client.id) and str(a.demographic.client.clientID) == str(client.clientID):
				results.append(a)
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

def continueToAmSection(am):
	location = None

	if am.drugHistoryComplete == False:
		location = 'counselor/forms/AngerManagement/drugHistory.html'
	elif am.childhoodComplete == False:
		location = 'counselor/forms/AngerManagement/childhoodHistroy.html'
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

	return location



	
























