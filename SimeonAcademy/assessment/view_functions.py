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
from calendar import monthrange

from assessment.models import State, RefReason, Client, \
AngerManagement, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, MHUseTable, \
MHFamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_AngerHistory2, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHBackground, MHEducation, \
MHStressor, MHLegalHistory, ClientSession, Invoice, SType, AM_AngerHistory3, \
TrackApp, AIS_Admin, AIS_General, AIS_Medical, AIS_Employment, AIS_Drug1, \
AIS_Legal, AIS_Family, AIS_Social1, AIS_Social2, AIS_Psych, ASI, UtPaid, \
SolidState, PrintableForms, WorkSchedule, Note

def isCompleteWeek(day):
	complete = False
	if day == 7:
		complete = True
	return complete

def getExtraPrevDays(year, month):
	result = []
	firstDay = date(year, month, 1).weekday()

	if month == 1:
		month = 12
		year = year - 1
	else:
		month = month - 1

	extraDays = firstDay + 1
	lastDay = monthrange(year, month)[1]
	start = lastDay - extraDays

	for i in range(start, lastDay):
		data = {}
		day = i + 1
		data['day'] 	= day
		data['class'] 	= 'prevMonth'
		data['id']		= str(year) + '-' + str(month) + '-' + str(day)
		result.append(data)
	return result

def getExtraNextDays(year, month):
	result = []
	lastDayMonth = monthrange(year, month)[1]
	lastWeekday = date(year, month, lastDayMonth).weekday()

	if month == 12:
		month = 1
		year += 1
	else:
		month += 1

	extraDays = lastWeekday + 1

	for i in range(extraDays):
		data = {}
		day = i + 1
		data['day'] = day
		data['class'] = 'extraMonth'
		data['id'] = str(year) + '-' + str(month) + '-' + str(day)
		result.append(data)
	return result

def fetchNumWeeks(year, month):
	week = 1
	firstDay = (date(year, month, 1).weekday()) + 1
	numDays = monthrange(year, month)[1]

	for i in range(numDays):
		firstDay += 1

		if firstDay == 7:
			week += 1
			firstDay = 0
	return week

def fetchCalendarData(year, month):
	result = []
	day = 0
	extraPrevious 	= None
	extraNext 		= None
	now = datetime.now().date()
	now = decodeDate(now)	

	dayRange 	= monthrange(year, month)[1]
	firstDay 	= date(year, month, 1).weekday()
	lastDay 	= date(year, month, dayRange).weekday()

	if isCompleteWeek(firstDay) == False:
		extraPrevious = getExtraPrevDays(year, month)
		for p in extraPrevious:
			result.append(p)

	for i in range(dayRange):
		data = {}
		day = i + 1
		data['day'] = day
		data['id'] = str(year) + '-' + str(month) + '-' + str(day)

		if now['year'] == year and now['month'] == month and now['day'] == day:
			data['class'] = 'thisDay'
		elif now['day'] > day:
			data['class'] = 'prevMonth'
		else:
			data['class'] = 'thisMonth'

		result.append(data)

	if isCompleteWeek(lastDay) == False:
		extraNext = getExtraNextDays(year, month)
		for n in extraNext:
			result.append(n)

	for j in range(len(result)):
		if j % 7 == 0:
			result[j]['newWeek'] = True
		else:
			result[j]['newWeek'] = False

	fetchNumWeeks(year, month)
	return result

def decodeCalDate(obj):
	result = {}
	dd = ''
	mm = ''
	yy = ''
	index1 = 0
	temp = ''
	temp2 = ''

	for i in range(len(obj)):
		if obj[i] == '/':
			index = i 
			break

	for k in range(index):
		mm += obj[k]

	for j in range((index + 1), len(obj)):
		temp += obj[j]

	for n in range(3):
		if temp[n] == '/':
			index = n
			break
		else:
			dd += temp[n]

	for p in range((index + 1), len(temp)):
		temp2 += temp[p]

	for l in range(len(temp2)):
		if temp2[l] == '/':
			break
		else:
			yy += temp2[l]

	dd = int(dd)
	mm = int(mm)
	yy = int(yy)
	result['day'] = dd
	result['month'] = mm
	result['year'] = yy
	return result


def seperateCalendarTime(val):
	result = {}
	index = 0
	temp = ''
	temp2 = ''
	start = ''
	end = ''
	val = str(val)

	for i in range(len(val)):
		if val[i] == '@':
			index = i + 1
			break

	for j in range(index, len(val)):
		temp += val[j]

	temp = cleanWhiteSpace(temp)

	for k in range(len(temp)):
		if temp[k] == '-':
			index = k + 1
			break
		else:
			start += temp[k]

	for p in range(index, len(temp)):
		end += temp[p]

	result['start'] = start
	result['end'] = end
	return result

def decodeCalendarTime(val):
	result = {}
	temp = ''
	temp2 = ''
	hh = ''
	mm = ''
	am = False
	index = 0

	for i in range(len(val)):
		if val[i] == ':':
			index = i + 1
			break
		else:
			hh += val[i]

	for j in range(index, len(val)):
		if val[j] == 'a' or val[j] == 'p':
			index = j 
			break
		else:
			mm += val[j]

	if val[index] == 'a':
		am = True

	hh = int(hh)
	mm = int(mm)

	result['am'] = am
	result['hour'] = hh
	result['minute'] = mm
	result = decodeToMillitary(result)
	return result

def decodeToMillitary(time):
	if time['am'] == False:
		time['hour'] += 12
	if time['hour'] == 24:
		time['hour'] = 0

	return time

def decodeCalendarData(obj):
	result = {}
	date = decodeCalDate(obj)
	time = seperateCalendarTime(obj)
	start = decodeCalendarTime(time['start'])
	end = decodeCalendarTime(time['end'])
	result['day'] = date['day']
	result['month'] = date['month']
	result['year'] = date['year']
	result['s_hour'] = start['hour']
	result['s_min'] = start['minute']
	result['s_am'] = start['am']
	result['e_hour'] = end['hour']
	result['e_min'] = end['minute']
	result['e_am'] = end['am']
	return result

def wsEqual(w1, w2):
	isEqual = False

	if str(w1.date) == str(w2.date) and str(w1.counselor) == str(w2.counselor) and str(w1.counselor_id) == str(w2.counselor_id):
		isEqual = True
	return isEqual

def updateWorkSchedule(o, n):
	o.startHr = n.startHr
	o.startMin = n.startMin
	o.endHr = n.endHr
	o.endMin = n.endMin
	o.save()

def saveWorkSchedule(ws):
	saveThis = False
	ws_list = WorkSchedule.objects.all()

	if len(ws_list) == 0:
		ws.save()
	else:
		for w in ws_list:
			if wsEqual(w, ws) == False:
				ws.save()
			else:
				updateWorkSchedule(w, ws)

def newWorkSchedule(encode, request):
	date = datetime(encode['year'], encode['month'], encode['day'])
	date = date.date()
	user = request.user

	counselor 	= str(user.first_name) + ' ' + str(user.last_name)
	ws 			= WorkSchedule(counselor=counselor, counselor_id=user.id)
	ws.date 	= date
	ws.startHr 	= encode['s_hour']
	ws.endHr 	= encode['e_hour']
	ws.startMin = encode['s_min']
	ws.endMin 	= encode['e_min']

	saveWorkSchedule(ws)

def getUserWorkSchedules(user):
	result = []
	wss = WorkSchedule.objects.all().order_by('date') 

	for w in wss:
		if str(user.id) == str(w.counselor_id):
			result.append(w)
	return result

def decodeCalMillitary(hour, minute):
	ampm = 'am'
	hour = int(hour)

	if hour > 12:
		hour = hour - 12
		ampm = 'pm'

	elif hour == 12:
		ampm = 'pm'

	elif hour == 0:
		hour = 12

	result = str(hour) + ':' + str(minute) + ' ' + ampm
	return result


def get_JSON_workSchedule(user):
	content = []
	schedules = getUserWorkSchedules(user)

	for s in schedules:
		data = {}
		date = str(s.date)
		day = ''
		month = ''
		year = ''
		day += date[8]
		day += date[9]
		month += date[5]
		month += date[6]
		year += date[0]
		year += date[1]
		year += date[2]
		year += date[3]
		num = int(day) + 1
		start_val = decodeCalMillitary(str(s.startHr), str(s.startMin))
		end_val = decodeCalMillitary(str(s.endHr), str(s.endMin))
		start_id = 'startDiv' + str(num)
		end_id = 'endDiv' + str(num)
		data['start_val'] = start_val
		data['start_id'] = start_id
		data['end_val'] = end_val
		data['end_id'] = end_id
		data['month'] = month
		data['year'] = year
		content.append(data)
	return content

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

def getRefReasons():
	result = []
	refs = RefReason.objects.all().order_by('reason')
	for r in refs:
		result.append(r)
	return result

def getOrderedRefIndex(refReason):
	index = 1
	ref_list = RefReason.objects.all().order_by('reason')
	r = str(refReason)

	for r in ref_list:
		if refReason == str(r.reason):
			break
		else:
			index += 1

	return index

def fetchRefReasonID(refReason):
	result = None
	refReason = str(refReason)
	refReasons = RefReason.objects.all()

	for r in refReasons:
		if str(r.reason) == refReason:
			result = r.id
			break
	return result

def getStates():
	results = []
	states = State.objects.all().order_by('state')
	for s in states:
		results.append(s)
	return results

def fetchStateID(state):
	result = None
	state = str(state)
	states = State.objects.all()
	for s in states:
		if state == str(s.state):
			result = s.id
			break
	return result

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

def snagSelectDate(request):
	m = request.POST.get('c_mob')
	d = request.POST.get('c_dob')
	y = request.POST.get('c_yob')

	m = int(m)
	d = int(d)
	y = int(y)

	date = datetime(y, m, d)
	return date.date()

def decodeDate(date):
	result = {}
	date = str(date)
	y = ''
	m = ''
	d = ''

	y += date[0]
	y += date[1]
	y += date[2]
	y += date[3]

	m += date[5]
	m += date[6]

	d += date[8]
	d += date[9]

	m = int(m)
	d = int(d)
	y = int(y)

	result['month'] = m
	result['day'] 	= d
	result['year'] 	= y
	return result


def snagYearIndex(select):
	select = str(select)
	date = datetime.now()
	temp = []
	index = 0
	year = date.year
	year = int(year)
	firstYear = year - 80
	lastYear = year - 5

	for y in range(firstYear, lastYear):
		temp.append(y)

	count = len(temp) - 1

	for i in range(count):	
		count -= 1

		if str(temp[count]) == select:
			index = i + 2
			break

	return index

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

	if phone != None and len(phone) >= 10:
		if phone != '' and  phone != ' ':
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



##################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------#
#******************************************************** CLIENT FUNTIONS *******************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#
##################################################################################################################################

#--------------------------------------------------------------------------------------------------------------------------------#
#*************************************************** CLIENT SEARCH ALGORITHM ****************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#


def cleanWhiteSpace(text):
	text = str(text)
	result = ''
	for t in text:
		if t != ' ':
			result += t
	return result

def fieldIsEmpty(text):
	text = str(text)
	proceed = True
	isEmpty = False

	if text == None or text == '' or text == ' ':
		isEmpty = True
		proceed = False

	if proceed == True:
		text = cleanWhiteSpace(text)
		if len(text) == 0:
			isEmpty = True
	return isEmpty

def grabSearchField(text):
	result = ''
	text = str(text)
	text = cleanWhiteSpace(text)
	for t in text:
		t = t.lower()
		result += t
	return result

def grabSearchParameters(request):
	result 		= {}

	fname 		= request.POST.get('fname')
	mi 			= request.POST.get('mi')
	lname 		= request.POST.get('lname')
	phone 		= request.POST.get('phone')
	ssn 		= request.POST.get('ssn')
	clientID 	= request.POST.get('clientID')
	yob 		= request.POST.get('c_yob')

	yob = str(yob)

	result['fname'] 	= False
	result['mi'] 		= False
	result['lname'] 	= False
	result['phone'] 	= False
	result['ssn'] 		= False
	result['clientID'] 	= False
	result['dob'] 		= False

	if fieldIsEmpty(fname) == False:
		result['fname'] = True

	if fieldIsEmpty(mi) == False:
		result['mi'] = True

	if fieldIsEmpty(lname) == False:
		result['lname'] = True

	if fieldIsEmpty(phone) == False:
		result['phone'] = True

	if fieldIsEmpty(ssn) == False:
		result['ssn'] = True

	if fieldIsEmpty(clientID) == False:
		result['clientID'] = True

	if yob != '0':
		result['dob'] = True
	return result

def prepareNumbersearch(ssn):
	result = ''
	ssn = str(ssn)
	ssn = cleanWhiteSpace(ssn)

	for s in ssn:
		if s=='0' or s=='1' or s=='2' or s=='3' or s=='4' or s=='5' or s=='6' or s=='7' or s=='8' or s=='9':
			result += s
	return result

def hasCorrectChars(numberChars, text):
	has3 = False
	if numberChars <= len(text):
		has3 = True
	return has3

def newWordCut(index, text):
	result = ''
	for i in range(index, len(text)):
		result += text[i]
	return result

def grabChars(index, text1, text2):
	result = {}
	numChars = len(text1)
	word = newWordCut(index, text2)
	text = ''
	proceed = hasCorrectChars(numChars, word)

	if proceed == True:
		for i in range(numChars):
			text += word[i]
		result['text'] = text
	result['proceed'] = proceed
	return result

def prepareSearchField(fType, text):
	result = None
	fType = str(fType)
	if fType == 'number':
		result = prepareNumbersearch(text)
	elif fType == 'text':
		result = grabSearchField(text)
	return result

def fieldMatch(fType, index, text1, text2):
	isMatch = False
	text1 = prepareSearchField(fType, text1)
	text2 = prepareSearchField(fType, text2)
	data = grabChars(index, text1, text2)

	if data['proceed'] == True:
		if data['text'] == text1:
			isMatch = True
	return isMatch

def processDataMatch(fType, text1, text2):
	isMatch = False

	for i in range(len(text2)):
		if fieldMatch(fType, i, text1, text2) == True:
			isMatch = True
			break
	return isMatch

def snagSearchPhone(phone):
	result = None
	if fieldIsEmpty(phone) == False:
		phone = prepareNumbersearch(phone)
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

def snagSearchSSN(ssn):
	result = None
	if fieldIsEmpty(ssn) == False:
		ssn = prepareNumbersearch(ssn)
		result = ''
		result += ssn[0]
		result += ssn[1]
		result += ssn[2]
		result += '-'
		result += ssn[3]
		result += ssn[4]
		result += '-'
		result += ssn[5]
		result += ssn[6]
		result += ssn[7]
		result += ssn[8]
	return result

def selectToDateObject(request):
	m = request.POST.get('c_mob')
	d = request.POST.get('c_dob')
	y = request.POST.get('c_yob')
	m = int(m)
	d = int(d)
	y = int(y)
	date = datetime(y, m, d)
	date = date.date()
	return date

def universal_client_match(request, client):
	isMatch = False
	fm 		= True
	lm 		= True
	mm		= True
	pm 		= True
	sm 		= True
	cm 		= True
	dm 		= True
	search 		= grabSearchParameters(request)

	if search['fname'] == True:
		fname = request.POST.get('fname')
		cfn = str(client.fname)
		if processDataMatch('text', fname, cfn) == False:
			fm = False

	if search['lname'] == True:
		lname = request.POST.get('lname')
		cln = str(client.lname)
		if processDataMatch('text', lname, cln) == False:
			lm = False

	if search['mi'] == True:
		mi = request.POST.get('mi')
		cmi = str(client.middleInit)
		if processDataMatch('text', mi, cmi) == False:
			mm = False

	if search['phone'] == True:
		phone = request.POST.get('phone')
		cph = str(client.phone)
		if processDataMatch('number', phone, cph) == False:
			pm = False

	if search['ssn'] == True:
		ssn = request.POST.get('ssn')
		csn = str(client.ss_num)
		if processDataMatch('number', ssn, csn) == False:
			sm = False

	if search['clientID'] == True:
		clientID = request.POST.get('clientID')
		cci = str(client.clientID)
		if processDataMatch('text', cci, clientID) == False:
			cm = False

	if search['dob'] == True:
		dob = selectToDateObject(request)
		cdob = client.dob
		dob = str(dob)
		cdob = str(cdob)
		if processDataMatch('number', dob, cdob) == False:
			dm = False

	if fm==True and lm==True and mm==True and pm==True and sm==True and cm==True and dm==True:
		isMatch = True
	return isMatch

def clientSort(includeDischarge, sortBy):
	result = []

	if includeDischarge == None:
		includeDischarge = False
	else:
		includeDischarge = True

	if sortBy == 'az':
		az = Client.objects.all().order_by('lname')
		if includeDischarge == True:
			result = az
		else:
			for c1 in az:
				if c1.isDischarged == False:
					result.append(c1)

	elif sortBy == 'za':
		za = Client.objects.all().order_by('-lname')
		if includeDischarge == True:
			result = za
		else:
			for c2 in za:
				if c2.isDischarged == False:
					result.append(c2)
	return result

def fetchNumSearchPages(numMatches, numPerPage):
	numPages = 0
	mod = numMatches % numPerPage

	if mod != 0:
		numPages = 1

	remain = numMatches - mod
	remain /= numPerPage
	numPages += remain
	return numPages

def grabSearchPageResults(page, history, numPerPage):
	result = []
	page = int(page)
	numPerPage = int(numPerPage)
	startIndex = (page * numPerPage) - numPerPage
	endIndex = startIndex + numPerPage
	numMatches = len(history)

	numPages = fetchNumSearchPages(numMatches, numPerPage)
	if page == int(numPages):
		endIndex = numMatches % numPerPage

	for i in range(startIndex, endIndex):
		result.append(history[i])
	return result

def snagSearchPages(history, numPerPage, page):
	result = {}
	numMatches = len(history)
	numPages = fetchNumSearchPages(numMatches, numPerPage)
	result['numPages'] = numPages
	result['entries'] = grabSearchPageResults(page, history, numPerPage) 
	return result

def snagSearchDate(date):
	date = str(date)
	m = ''
	d = ''
	y = ''

	y += date[0]
	y += date[1]
	y += date[2]
	y += date[3]

	d += date[8]
	d += date[9]

	m += date[5]
	m += date[6]

	if m == '01':
		m = 'January'
	elif m == '02':
		m = 'February'
	elif m == '03':
		m = 'March'
	elif m == '04':
		m = 'April'
	elif m == '05':
		m = 'May'
	elif m == '06':
		m = 'June'
	elif m == '07':
		m = 'July'
	elif m == '08':
		m = 'August'
	elif m == '09':
		m = 'September'
	elif m == '10':
		m = 'October'
	elif m == '11':
		m = 'November'
	elif m == '12':
		m = 'December'
	result = m + ' ' + d + ', ' + y
	return result


def superPageSelector(numEntries, matches):
	result = {}
	numPages = 0
	count = 0
	slot = 1
	pageData = []
	numMatches = len(matches)
	remainder = numMatches % numEntries

	if remainder != 0:
		numPages = 1

	otherPages = (numMatches - remainder) / numEntries
	numPages += otherPages

	for n in range(numPages):
		newArray = []
		pageData.append(newArray)

	for i in range(numPages):
		for j in range(numEntries):
			content 	= {}
			fname 		= str(matches[count].fname)
			lname 		= str(matches[count].lname)
			mi 			= str(matches[count].middleInit)
			name 		= lname + ', ' + fname + ', ' + mi
			dob 		= snagSearchDate(matches[count].dob)
			ssn 		= snagSearchSSN(matches[count].ss_num)
			phone 		= snagSearchPhone(matches[count].phone)
			photo 		= str(matches[count].photo)
			clientID 	= str(matches[count].clientID)
			cli_id 		= int(matches[count].id)

			hasUnfinished = hasUnfinishedSession(matches[count])
			if hasUnfinished == True:
				session_id = fetchUnfinishedSession(matches[count]).id
				content['session_id'] = session_id
			else:
				content['session_id'] = 'NULL'

			content['c_name'] 		= name
			content['c_dob'] 		= dob
			content['c_ssn'] 		= ssn
			content['c_phone'] 		= phone
			content['c_photo'] 		= photo
			content['c_clientID'] 	= clientID
			content['c_id'] 		= cli_id
			content['c_number']		= str(slot) + str('.')
			content['hasSession']	= hasUnfinished

			pageData[i].append(content)
			count += 1
			slot += 1

			if count == numMatches:
				break

	for p in range(numPages):
		inde = p + 1
		a_name = 'page' + str(inde)
		result[a_name] = pageData[p]
	result['numMatches'] = numMatches
	result['numPages'] = numPages

	return result

def snagSlots(numSlots):
	slots = []
	for n in range(numSlots):
		data = {}
		num = n + 1
		data['input'] = num
		data['number'] = 'c_number' + str(num)
		data['name'] = 'c_name' + str(num)
		data['ssn'] = 'c_ssn' + str(num)
		data['dob'] = 'c_dob' + str(num)
		data['photo'] = 'c_photo' + str(num)
		data['phone'] = 'c_phone' + str(num)
		data['clientID'] = 'c_clientID' + str(num)
		data['id'] = 'c_id' + str(num)
		data['hasSession'] = 'hasSession' + str(num)
		data['session_id'] = 'session_id' + str(num)
		slots.append(data)
	return slots

def fetchResultTags(numResults, numPerPage):
	slots = []

	if numResults < numPerPage:
		mod = numResults % numPerPage
		slots = snagSlots(mod)
	else:
		slots = snagSlots(numPerPage)
	return slots

def completeClientSearch(request, sortBy):
	initData = []
	count = 1
	includeDischarge 	= request.POST.get('incD')

	clients = clientSort(includeDischarge, sortBy)

	for c in clients:
		if universal_client_match(request, c) == True:
			initData.append(c)

	superSearch = superPageSelector(4, initData)

	return superSearch

#--------------------------------------------------------------------------------------------------------------------------------#
#****************************************************** END SEARCH ALGORITHM ****************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#

def fetchClientUpdatedFields(client):
	fields 		= {}
	gender 		= 'Female'
	dob 		= decodeDate(client.dob)
	fname 		= str(client.fname)
	lname 		= str(client.lname)	
	street_no   = str(client.street_no)
	street_name = str(client.street_name)
	apt 		= str(client.apartment_no)
	city 		= str(client.city)
	state 		= str(client.state.state)
	zip_code	= str(client.zip_code)

	the_name 	= fname + ' ' + lname
	address1	= street_no + ' ' + street_name + ' ' + apt
	address2 	= city + ', ' + state + ' ' + zip_code

	if client.isMale == True:
		gender = 'Male'

	fields['the_name'] 		= the_name
	fields['isMale']		= client.isMale
	fields['address1']	 	= address1
	fields['address2'] 		= address2
	fields['gender'] 		= gender
	fields['ss_num']		= fetchClientSSDisplay(str(client.ss_num))
	fields['em_contact']	= client.emer_contact_name
	fields['em_phone'] 		= fetchClientPhoneDisplay(str(client.emer_phone))
	fields['probOfficer']	= client.probationOfficer
	fields['prob_phone']	= fetchClientPhoneDisplay(str(client.probation_phone))
	fields['email']			= client.email
	fields['phone'] 		= fetchClientPhoneDisplay(str(client.phone))
	fields['work']			= fetchClientPhoneDisplay(str(client.work_phone))
	fields['state_index'] 	= getOrderedStateIndex(client.state.state)
	fields['ref_index']		= getOrderedRefIndex(client.reason_ref.reason)
	fields['dob']			= snagSearchDate(client.dob)
	return fields

def updateClientAccount(client, request):
	client.fname 				= request.POST.get('fname')
	client.lname 				= request.POST.get('lname')
	client.middleInit 			= request.POST.get('mi')
	client.street_no 			= request.POST.get('street_no')
	client.street_name 			= request.POST.get('street_name')
	client.apartment_no 		= request.POST.get('apt')
	client.city 				= request.POST.get('city')
	client.zip_code 			= request.POST.get('zip')
	client.ss_num 				= request.POST.get('ssn')
	client.dob 					= snagSelectDate(request)
	client.phone 				= request.POST.get('phone')
	client.work_phone 			= request.POST.get('workPhone')
	client.email 				= request.POST.get('email')
	client.emer_contact_name 	= request.POST.get('emer_contact_name')
	client.emer_phone 			= request.POST.get('emer_phone')
	client.probationOfficer 	= request.POST.get('probationOfficer')
	client.probation_phone 		= request.POST.get('probation_phone')

	client.isMale 		= truePythonBool(request.POST.get('isMale'))
	client.state 		= State.objects.get(id=(fetchStateID(request.POST.get('state'))))
	client.reason_ref 	= RefReason.objects.get(id=(fetchRefReasonID(request.POST.get('reasonRef'))))
	client.save()

def fetchActiveClients():
	result = []
	clients = Client.objects.all()

	for c in clients:
		if c.isDischarged == False:
			result.append(c)

	return result

def removeClient(client):
	if client.hasFiles == True:
		client.isRemoved = True
	else:
		client.delete()


def setUpNumberSearch(text):
	text = str(text)
	text = cleanWhiteSpace(text)
	text = filterSS(text)
	return text

def birthDaySearchSet(dob):
	result = ''
	result += dob[4]
	result += dob[5]
	result += dob[6]
	result += dob[7]
	result += dob[0]
	result += dob[1]
	result += dob[2]
	result += dob[3]
	return result


def getClientBySS(ss_num):
	results = []
	clients = Client.objects.all()
	ss_num = filterSS(ss_num)

	for c in clients:
		sNum = filterSS(c.ss_num)
		if str(ss_num) == str(sNum):
			data = {}
			hasUnfinished = hasUnfinishedSession(c)

			if hasUnfinished == True:
				session = fetchUnfinishedSession(c)
				data['session'] = session
			else:
				data['session'] = None

			data['hasUnfinished'] = hasUnfinished
			data['client'] = c
			results.append(data)

	return results


def getClientByID(clientID):
	results = []
	clients = Client.objects.all()
	clientID = clientID.lower()

	for c in clients:
		compare = str(c.clientID).lower()
		if str(clientID) == str(compare):
			data = {}
			hasUnfinished = hasUnfinishedSession(c)

			if hasUnfinished == True:
				session = fetchUnfinishedSession(c)
				data['session'] = session
			else:
				data['session'] = None

			data['hasUnfinished'] = hasUnfinished
			data['client'] = c
			results.append(data)

	return results

def getClientByDOB(dob):
	results = []
	clients = Client.objects.all()

	dob = setUpNumberSearch(dob)
	dob = birthDaySearchSet(dob)

	for c in clients:
		temp = setUpNumberSearch(c.dob)
		if dob == temp:
			data = {}
			hasUnfinished = hasUnfinishedSession(c)

			if hasUnfinished == True:
				session = fetchUnfinishedSession(c)
				data['session'] = session
			else:
				data['session'] = None

			data['hasUnfinished'] = hasUnfinished
			data['client'] = c
			results.append(data)

	return results

def getClientByName(fname, lname):
	results = []
	clients = Client.objects.all()

	fname = cleanWhiteSpace(fname)
	lname = cleanWhiteSpace(lname)

	fname = fname.lower()
	lname = lname.lower()

	for c in clients:
		compF = str(c.fname).lower()
		compL = str(c.lname).lower()
		if c.isDischarged == False:
			if str(fname) == str(compF) and str(lname) == str(compL):
				data = {}
				hasUnfinished = hasUnfinishedSession(c)

				if hasUnfinished == True:
					session = fetchUnfinishedSession(c)
					data['session'] = session
				else:
					data['session'] = None

				data['hasUnfinished'] = hasUnfinished
				data['client'] = c
				results.append(data)
			elif str(lname) == None or str(lname) == '':
				if str(fname) == str(compF):
					data = {}
					hasUnfinished = hasUnfinishedSession(c)

					if hasUnfinished == True:
						session = fetchUnfinishedSession(c)
						data['session'] = session
					else:
						data['session'] = None

					data['hasUnfinished'] = hasUnfinished
					data['client'] = c
					results.append(data)
			elif str(fname) == None or str(fname) == '':
				if str(lname) == str(compL):
					data = {}
					hasUnfinished = hasUnfinishedSession(c)

					if hasUnfinished == True:
						session = fetchUnfinishedSession(c)
						data['session'] = session
					else:
						data['session'] = None

					data['hasUnfinished'] = hasUnfinished
					data['client'] = c
					results.append(data)

	return results


##################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------#
#****************************************************** SESSION FUNCTIONS *******************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#
##################################################################################################################################

def sessionEqual(s1, s2):
	isEqual = False
	if str(s1.id) == str(s2.id) and clientEqual(s1.client, s2.client):
		isEqual = True
	return isEqual

def fetchSessions(client):
	sessions = ClientSession.objects.all()
	result = []
	for s in sessions:
		if clientEqual(s.client, client) == True:
			result.append(s)
	return result

def newSession(the_client):
	start = datetime.now()
	session = ClientSession(client=the_client, startTime=start)
	session.save()
	return session

def openSession(session):
	sss = fetchSessions(session.client)
	for s in sss:
		if sessionEqual(session, s) == True:
			s.isOpen = True
			s.save()
		else:
			s.isOpen = False
			s.save()

def hasUnfinishedSession(client):
	hasUnfinished = False
	sss = fetchSessions(client)
	for s in sss:
		if clientEqual(s.client, client) == True and s.isComplete == False:
			hasUnfinished = True
			break
	return hasUnfinished

def fetchUnfinishedSession(client):
	result = None
	sss = fetchSessions(client)
	for s in sss:
		if clientEqual(client, s.client):
			result = s
			break
	return result

def addService(session, s_type):
	if session.noServices == 1:
		session.invoice.service1 = str(s_type.session_type)
		session.invoice.total1 = s_type.fee
		session.invoice.save()
	elif session.noServices == 2:
		session.invoice.service2 = str(s_type.session_type)
		session.invoice.total2 = s_type.fee
		session.invoice.save()
	elif session.noServices == 3:
		session.invoice.service3 = str(s_type.session_type)
		session.invoice.total3 = s_type.fee
		session.invoice.save()
	elif session.noServices == 4:
		session.invoice.service4 = str(s_type.session_type)
		session.invoice.total4 = s_type.fee
		session.invoice.save()
	elif session.noServices == 5:
		session.invoice.service5 = str(s_type.session_type)
		session.invoice.total5 = s_type.fee
		session.invoice.save()
	elif session.noServices == 6:
		session.invoice.service6 = str(s_type.session_type)
		session.invoice.total6 = s_type.fee
		session.invoice.save()

	temp_no = session.noServices
	temp_no = temp_no + 1
	session.noServices = temp_no
	session.save()
	session.invoice.save()

def getInvoiceTotal(session):
	total = session.invoice.total1
	total = total + session.invoice.total2
	total = total + session.invoice.total3
	total = total + session.invoice.total4
	total = total + session.invoice.total5
	total = total + session.invoice.total6
	session.invoice.grandTotal = int(total)
	session.save()


def isMultiAM():
	isMulti = False
	sessions = ClientSession.objects.all()
	ams = AngerManagement.objects.all()
	count = 0

	for s in sessions:
		if s.hasAM == True:
			for a in ams:
				if str(a.id) == str(s.am.id):
					count = count + 1
					if count > 1:
						isMulti = True
						break
	return isMulti

def isMultiMH():
	isMulti = False
	sessions = ClientSession.objects.all()
	mhs = MentalHealth.objects.all()
	count = 0

	for s in sessions:
		if s.hasMH == True:
			for m in mhs:
				if str(m.id) == str(s.mh.id):
					count = count + 1
					if count > 1:
						isMulti = True
						break
	return isMulti

def isMultiUT():
	isMulti = False
	sessions = ClientSession.objects.all()
	uts = UrineResults.objects.all()
	count = 0

	for s in sessions:
		if s.hasUT == True:
			for u in uts:
				if str(u.id) == str(s.ut.id):
					count = count + 1
					if count > 1:
						isMulti = True
						break
	return isMulti

def isMultiSAP():
	isMulti = False
	sessions = ClientSession.objects.all()
	saps = SAP.objects.all()
	count = 0

	for s in sessions:
		if s.hasSAP == True:
			for sap in saps:
				if str(sap.id) == str(s.sap.id):
					count = count + 1
					if count > 1:
						isMulti = True
						break
	return isMulti

def isMultiASI():
	isMulti = False
	sessions = ClientSession.objects.all()
	asis = ASI.objects.all()
	count = 0

	for s in sessions:
		if s.hasASI == True:
			for a in asis:
				if str(s.id) == str(s.asi.id):
					count = count + 1
					if count > 1:
						isMulti = True
						break
	return isMulti

def runMultiQuery(session):
	if session.hasAM == True:
		if isMultiAM() == False:
			deleteAM(session.am)

	if session.hasMH == True:
		if isMultiMH() == False:
			deleteMh(session.mh)

	if session.hasUT == True:
		if isMultiUT() == False:
			deleteUT(session.ut)

	if session.hasSAP == True:
		if isMultiSAP() == False:
			deleteSap(session.sap)

	if session.hasASI == True:
		if isMultiASI() == False:
			deleteASI(session.asi)

def runIncompleteQuery(session):
	if session.isComplete == True:
		if session.hasAM == True:
			if session.am.isComplete == False and isMultiAM() == False:
				deleteAM(session.am)
				session.hasAM = False

		if session.hasMH == True:
			if session.mh.isComplete == False and isMultiMH() == False:
				deleteMh(session.mh)
				session.hasMH = False

		if session.hasUT == True:
			if session.ut.isComplete == False and isMultiUT() == False:
				deleteUT(session.ut)
				session.hasUT = False

		if session.hasSAP == True:
			if session.sap.isComplete == False and isMultiSAP() == False:
				deleteSap(session.sap)
				session.hasSAP = False

		if session.hasASI == True:
			if session.asi.isComplete == False and isMultiASI() == False:
				deleteASI(session.asi)
				session.hasASI = False

		session.save()


def deleteCurrentSession(session):
	runMultiQuery(session)

	if session.hasInvoice == True:
		session.invoice.delete()

	session.delete()

def refreshCurrentSession(session):
	session.startTime = datetime.now()
	session.endTime = None
	session.counselor = ''
	session.noServices = 1

	if session.hasAM == True:
		deleteAM(session.am)
	if session.hasMH == True:
		deleteMh(session.mh)
	if session.hasUT == True:
		deleteUT(session.ut)
	if session.hasSAP == True:
		deleteSap(session.sap)
	if session.hasASI == True:
		deleteASI(session.asi)
	if session.hasInvoice == True:
		session.invoice.delete()

	session.hasAM = False
	session.hasMH = False
	session.hasUT = False
	session.hasASI = False
	session.hasSAP = False
	session.isPaid = False
	session.isComplete = False	
	session.save()

def invoiceQuery(session):
	create = False
	amCheck = False
	mhCheck = False
	utCheck = False
	sapCheck = False
	asiCheck = False

	if session.hasAM == True:
		if session.am.isComplete == True:
			amCheck = True

	if session.hasMH == True:
		if session.mh.isComplete == True:
			mhCheck = True

	if session.hasUT == True:
		if session.ut.isComplete == True:
			utCheck = True

	if session.hasSAP == True:
		if session.sap.isComplete == True:
			sapCheck = True

	if session.hasASI == True:
		if session.asi.isComplete == True:
			asiCheck = True

	if amCheck==True or mhCheck==True or utCheck==True or sapCheck==True or asiCheck==True:
		create = True

	return create


def updateInvoice(session):
	if session.hasAM == True:
		if session.am.isComplete == True:
			s_type = getStype('am')
			addService(session, s_type)
	if session.hasMH == True:
		if session.mh.isComplete == True:
			s_type = getStype('mh')
			addService(session, s_type)
	if session.hasUT == True:
		if session.ut.isComplete == True:
			s_type = getStype('ut')
			addService(session, s_type)
	if session.hasASI == True:
		if session.asi.isComplete == True:
			s_type = getStype('asi')
			addService(session, s_type)
	if session.hasSAP == True:
		if session.sap.isComplete == True:
			s_type = getStype('sap')
			addService(session, s_type)

	session.invoice.save()
	getInvoiceTotal(session)

def processInvoice(session):
	if session.hasInvoice == False and invoiceQuery(session) == True:
		date = datetime.now()
		invoice = Invoice(client=session.client, date=date)
		invoice.save()
		session.invoice = invoice
		session.hasInvoice = True
		session.save()
	updateInvoice(session)

def fetchBillableItems(session):
	result = []
	names = []
	costs = []

	names.append(session.invoice.service1)
	names.append(session.invoice.service2)
	names.append(session.invoice.service3)
	names.append(session.invoice.service4)
	names.append(session.invoice.service5)
	names.append(session.invoice.service6)

	costs.append(session.invoice.total1)
	costs.append(session.invoice.total2)
	costs.append(session.invoice.total3)
	costs.append(session.invoice.total4)
	costs.append(session.invoice.total5)
	costs.append(session.invoice.total6)

	for i in range(int(session.noServices) - 1):
		data = {}
		no = i + 1
		service = 'Service ' + str(no)
		data['service'] = service
		data['name'] = names[i]
		data['cost'] = costs[i]
		result.append(data)

	return result


def shouldDeleteSession(session):
	shouldDelete = True

	if session.hasAM==True or session.hasMH==True or session.hasUT==True or session.hasSAP==True or session.hasASI==True:
		shouldDelete = False 

	return shouldDelete

def endSession(session, isfinished):
	continueProcessing = True
	date = datetime.now()
	session.isComplete = isfinished	
	session.endTime = date
	session.save()

	if invoiceQuery(session) == True:
		invoice = Invoice(client=session.client, date=date)
		invoice.save()
		session.invoice = invoice
		session.hasInvoice = True
		session.save()
	else:
		if shouldDeleteSession(session) == True:
			deleteCurrentSession(session)
			continueProcessing = False

	if continueProcessing == True:
		if session.hasInvoice == True:
			if session.hasAM == True:
				if session.am.isComplete == True:
					s_type = getStype('am')
					addService(session, s_type)
			if session.hasMH == True:
				if session.mh.isComplete == True:
					s_type = getStype('mh')
					addService(session, s_type)
			if session.hasUT == True:
				if session.ut.isComplete == True:
					s_type = getStype('ut')
					addService(session, s_type)
			if session.hasASI == True:
				if session.asi.isComplete == True:
					s_type = getStype('asi')
					addService(session, s_type)
			if session.hasSAP == True:
				if session.sap.isComplete == True:
					s_type = getStype('sap')
					addService(session, s_type)


		runIncompleteQuery(session)
		session.isOpen = False
		session.save()

def getExistingSessionForms(session):
	result = []
	if session.hasASI == True:
		result.append('Addiction Severity Index')
	if session.hasAM == True:
		result.append('Anger Management Assessment')
	if session.hasMH == True:
		result.append('Mental Health Assessment')
	if session.hasSAP == True:
		result.append('S.A.P Profile')
	if session.hasUT == True:
		result.append('Urine Analysis')	
	return result

def getAllAmForms(session):
	result = None
	if session.hasAM == True:
		if session.am.isComplete == True:
			data = {}
			data['form_type'] = 'Anger Management Assessment'
			data['form'] = session.am
			result = data
	return result

def getAllMhForms(session):
	result = None
	if session.hasMH == True:
		if session.mh.isComplete == True:
			data = {}
			data['form_type'] = 'Mental Health Assessment'
			data['form'] = session.mh
			result = data
	return result

def getAllUtForms(session):
	result = None
	if session.hasUT == True:
		if session.ut.isComplete == True:
			data = {}
			data['form_type'] = 'Urine Analysis'
			data['form'] = session.ut
			result = data
	return result

def getAllSapForms(session):
	result = None
	if session.hasSAP == True:
		if session.sap.isComplete == True:
			data = {}
			data['form_type'] = 'S.A.P Profile'
			data['form'] = session.sap
			result = data
	return result

def getAllAsiForms(session):
	result = None
	if session.hasASI == True:
		if session.asi.isComplete == True:
			data = {}
			data['form_type'] = 'Addiction Severity Index'
			data['form'] = session.asi
			result = data
	return result

def startSession(client):
	result = {}
	if hasUnfinishedSession(client) == True:
		result['session'] = fetchUnfinishedSession(client)
		result['isNew'] = False
	else:
		result['session'] = newSession(client)
		result['isNew'] = True
	return result

def beginSession(request):
	result = {}
	client = Client.objects.get(id=(request.POST.get('client_id')))

	action = startSession(client)
	session = action['session']
	result['session'] = session
	result['isNew'] = action['isNew']
	#THINK ABOUT THE PHONE SECTION

	completeAM = False
	completeMH = False
	completeUT = False
	completeASI = False
	completeSAP = False

	if session.hasAM == True:
		if session.am.isComplete == True:
			completeAM = True

	if session.hasMH == True:
		if session.mh.isComplete == True:
			completeMH = True

	if session.hasUT == True:
		if session.ut.isComplete == True:
			completeUT = True

	if session.hasSAP == True:
		if session.sap.isComplete == True:
			completeSAP = True

	if session.hasASI == True:
		if session.asi.isComplete == True:
			completeASI = True

	result['completeAM'] = completeAM
	result['completeMH'] = completeMH
	result['completeUT'] = completeUT
	result['completeASI'] = completeASI
	result['completeSAP'] = completeSAP

	user = request.user
	counselor = ''
	counselor = str(user.first_name) + ' ' + str(user.last_name)
	session.counselor = counselor
	session.save()
	openSession(session)
	setGlobalSession(session.id, request.user)
	track = getTrack(user)
	quickTrack('Session', track)
	result['tracking'] = track.state.state

	if action['isNew'] == False:
		result['init'] = getExistingSessionForms(session)
		result['url'] = 'counselor/session/existingSession.html'
	else:
		result['url'] = 'counselor/client/client_options.html'
	return result

def processSession(form_type, session):
	form_type = str(form_type)
	currentS = int(session.noServices)

	s_type = getStype(form_type)
	addService(session, s_type)
	session.noServices = currentS + 1
	session.save()


##################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------#
#********************************************************** END SESSION *********************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#
##################################################################################################################################

##################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------#
#**************************************************************** NOTES *********************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#
##################################################################################################################################

def create_note(client, subject):
	date = datetime.now()
	date = date.date()
	subject = str(subject)
	note = Note(clientID=clientID, date=date, title=subject)
	note.save()
	return note.id

def note_is_valid(text):
	text = str(text)
	text = cleanWhiteSpace(text)
	isValid = True

	if len(text) < 1:
		isValid = False
	return isValid

def save_note(note_id, text):
	noteSaved = False
	text= str(text)
	note = Note.objects.get(id=note_id)

	if note_is_valid(text):
		note.note = text
		note.save()
		noteSaved = True
	
	return noteSaved

def client_has_notes(client):
	hasNotes = False
	notes = Note.objects.all().order_by('-date')

	for n in notes:
		if clientEqual(n.client, client):
			hasNotes = True
			break
	return hasNotes

def get_all_client_notes(client):
	results = []
	notes = Note.objects.all().order_by('-date')

	for n in notes:
		if clientEqual(n.client, client):
			results.append(n)

	return results


##################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------#
#********************************************************** END NOTES ***********************************************************#
#--------------------------------------------------------------------------------------------------------------------------------#
##################################################################################################################################


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
		if a.isComplete == False:
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
		if m.isComplete == False:
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
		if s.isComplete == False:
			result['incomplete'] = True
			result['sap'] = s
			break
	return result

def saveAMDemographic(request, am):
	date = datetime.now()
	date = date.date()
	demo = am.demographic

	demo.date_of_assessment = date
	demo.maritalStatus = request.POST.get('maritalStatus')
	demo.livingSituation = request.POST.get('livingSituation')
	demo.own = truePythonBool(request.POST.get('own'))
	demo.months_res = request.POST.get('months_res')
	demo.years_res = request.POST.get('years_res')
	demo.whoLivesWithClient = request.POST.get('whoLivesWithClient')

	demo.num_children = request.POST.get('num_children')
	demo.spouse_dep = request.POST.get('spouse_dep')
	demo.other_dependants = request.POST.get('other_dependants')

	demo.education = request.POST.get('education')
	demo.resasonDO = request.POST.get('m_resasonDO')

	demo.employee = request.POST.get('employee')
	demo.job_title = request.POST.get('job_title')
	demo.emp_address = request.POST.get('emp_address')
	demo.employed_months = request.POST.get('employed_months')
	demo.employed_years = request.POST.get('employed_years')
	demo.employer_phone = phone_to_integer(request.POST.get('employer_phone'))

	demo.health_problem = truePythonBool(request.POST.get('health_problem'))
	demo.medication = truePythonBool(request.POST.get('m_medication'))
	demo.whatMedicine = request.POST.get('m_whatMedicine')
	demo.health_exp = request.POST.get('m_health_exp')

	demo.save()
	am.save()

def saveAMDrugHistory(request, am):
	date = datetime.now()
	date = date.date()
	form = am.drugHistory
	form.date_of_assessment = date

	form.firstDrinkAge = request.POST.get('firstDrinkAge')
	form.firstDrinkType = request.POST.get('firstDrinkType')
	form.curUse = truePythonBool(request.POST.get('curUse'))
	form.amtPerWeek = request.POST.get('m_amtPerWeek')
	form.useAmt = request.POST.get('m_useAmt')

	form.everDrank = truePythonBool(request.POST.get('m_everDrank'))
	form.monthsQuit = request.POST.get('m_monthsQuit')
	form.yearsQuit = request.POST.get('m_yearsQuit')
	form.reasonQuit = request.POST.get('m_reasonQuit')

	form.DUI = truePythonBool(request.POST.get('m_DUI'))
	form.numDUI = request.POST.get('m_numDUI')
	form.BALevel = request.POST.get('m_BALevel')

	form.drugTreatment = truePythonBool(request.POST.get('drugTreatment'))
	form.treatmentPlace = request.POST.get('m_treatmentPlace')
	form.dateTreated = request.POST.get('m_dateTreated')

	form.finishedTreatment = truePythonBool(request.POST.get('m_finishedTreatment'))
	form.reasonNotFinishedTreatment = request.POST.get('m_reasonNotFinishedTreatment')
	form.isClean = truePythonBool(request.POST.get('m_isClean'))
	form.relapseTrigger = request.POST.get('m_relapseTrigger')

	form.drinkLastEpisode = truePythonBool(request.POST.get('drinkLastEpisode'))
	form.drinkRelationshipProblem = truePythonBool(request.POST.get('drinkRelationshipProblem'))
	form.needHelpDrugs = truePythonBool(request.POST.get('needHelpDrugs'))

	form.save()
	am.save()

def saveAMChildhood(request, am):
	date = datetime.now()
	date = date.date()
	form = am.childhood
	form.date_of_assessment = date

	form.raisedBy = request.POST.get('raisedBy')
	form.momAlive = truePythonBool(request.POST.get('momAlive'))
	form.dadAlive = truePythonBool(request.POST.get('dadAlive'))
	form.childTrama = truePythonBool(request.POST.get('childTrama'))
	form.traumaExplain = request.POST.get('traumaExplain')

	form.howLeftHome = request.POST.get('howLeftHome')
	form.num_siblings = request.POST.get('num_siblings')
	form.siblingsClose = truePythonBool(request.POST.get('siblingsClose'))
	form.siblingsRelationshipExplain = request.POST.get('siblingsRelationshipExplain')
	form.dadClose = truePythonBool(request.POST.get('dadClose'))
	form.dadCloseExplain = request.POST.get('dadCloseExplain')
	form.momClose = truePythonBool(request.POST.get('momClose'))
	form.momCloseExplain = request.POST.get('momCloseExplain')
	form.wasAbused = truePythonBool(request.POST.get('wasAbused'))
	form.abusedBy = request.POST.get('m_abusedBy')
	form.abuseImpact = request.POST.get('m_abuseImpact')

	form.childAnger 			= truePythonBool(request.POST.get('childAnger'))
	form.childAngerExplain 		= request.POST.get('childAngerExplain')
	form.otherChild 			= truePythonBool(request.POST.get('otherChild'))
	form.otherChildExplain 		= request.POST.get('otherChildExplain')
	form.parentViolence 		= truePythonBool(request.POST.get('parentViolence'))
	form.parentViolenceExplain 	= request.POST.get('parentViolenceExplain')
	form.parentViolenceImpact 	= request.POST.get('parentViolenceImpact')

	form.save()
	am.save()

def saveAMAngerHistroy1(request, am):
	date = datetime.now()
	date = date.date()
	form = am.angerHistory
	form.date_of_assessment = date

	form.recentIncidentV 	= request.POST.get('recentIncidentV')
	form.recentVDate 		= request.POST.get('recentVDate')
	form.recentVlocation 	= request.POST.get('recentVlocation')
	form.withWhomRecentV 	= request.POST.get('withWhomRecentV')
	form.happenedRecentV 	= request.POST.get('happenedRecentV')

	form.physicalRecentV 	= truePythonBool(request.POST.get('m_physicalRecentV'))
	form.verbalRecentV 		= truePythonBool(request.POST.get('m_verbalRecentV'))
	form.propertyRecentV 	= truePythonBool(request.POST.get('m_propertyRecentV'))
	form.otherRecentV 		= truePythonBool(request.POST.get('m_otherRecentV'))
	form.wasTense 			= truePythonBool(request.POST.get('m_wasTense'))
	form.hadRush 			= truePythonBool(request.POST.get('m_hadRush'))
	form.feltStrong 		= truePythonBool(request.POST.get('m_feltStrong'))

	form.otherExplainRecentV 	= request.POST.get('m_otherExplainRecentV')
	form.typeWordsRecentV 		= request.POST.get('typeWordsRecentV')

	form.psychoRecentV 			= truePythonBool(request.POST.get('psychoRecentV'))
	form.psychoWhyRecentV 		= request.POST.get('m_psychoWhyRecentV')
	form.longAgoTreatRecentVmos = request.POST.get('m_longAgoTreatRecentVmos')
	form.longAgoTreatRecentVyrs = request.POST.get('m_longAgoTreatRecentVyrs')

	form.didCompleteTreatRecentV = truePythonBool(request.POST.get('m_didCompleteTreatRecentV'))
	form.reasonNotCompleteRecentV = request.POST.get('m_reasonNotCompleteRecentV')

	form.save()
	am.save()


def saveAMAngerHistroy2(request, am):
	date = datetime.now()
	date = date.date()
	form = am.angerHistory2
	form.date_of_assessment = date

	form.depress30RecentV 		= truePythonBool(request.POST.get('depress30RecentV'))
	form.anxietyRecentV 		= truePythonBool(request.POST.get('anxietyRecentV'))
	form.hallucinationRecentV 	= truePythonBool(request.POST.get('hallucinationRecentV'))
	form.understandingRecentV 	= truePythonBool(request.POST.get('understandingRecentV'))
	form.troubleControlRecentV 	= truePythonBool(request.POST.get('troubleControlRecentV'))
	form.suicide30RecentV 		= truePythonBool(request.POST.get('suicide30RecentV'))

	form.depress30ExplainRecentV 		= request.POST.get('m_depress30ExplainRecentV')
	form.anxietyExplainRecentV 			= request.POST.get('m_anxietyExplainRecentV')
	form.hallucinationLastV 			= request.POST.get('m_hallucinationLastV')
	form.understandingExplainRecentV 	= request.POST.get('m_understandingExplainRecentV')
	form.lastTimeTroubleControl 		= request.POST.get('m_lastTimeTroubleControl')
	form.controlTrigger 				= request.POST.get('m_controlTrigger')
	form.suicide30ExplainRecentV 		= request.POST.get('m_suicide30ExplainRecentV')

	form.suicideTodayRecentV 		= truePythonBool(request.POST.get('suicideTodayRecentV'))
	form.suicideTodayPlanRecentV 	= truePythonBool(request.POST.get('suicideTodayPlanRecentV'))
	form.hasAttemptedSuicide 		= truePythonBool(request.POST.get('hasAttemptedSuicide'))
	form.suicideTodayExplainRecentV = request.POST.get('suicideTodayExplainRecentV')
	form.hasAttemptedExplainRecentV = request.POST.get('hasAttemptedExplainRecentV')

	form.save()
	am.save()

def saveAMAngerHistroy3(request, am):
	date 					= datetime.now()
	date 					= date.date()
	form 					= am.angerHistory3
	form.date_of_assessment = date

	form.homicidal 			= truePythonBool(request.POST.get('homicidal'))
	form.medRecentV 		= truePythonBool(request.POST.get('medRecentV'))
	form.durationRecentV 	= request.POST.get('durationRecentV')
	form.intensityRecentV 	= request.POST.get('intensityRecentV')
	form.howOften 			= request.POST.get('howOften')

	form.homicidalExplain 	= request.POST.get('m_homicidalExplain')
	form.medRecentVExplain 	= request.POST.get('m_medRecentVExplain')
	form.medSuccessRecentV 	= truePythonBool(request.POST.get('m_medSuccessRecentV'))

	form.medSuccessExplainRecentV = request.POST.get('m_medSuccessExplainRecentV')

	form.save()
	am.save()

def saveAMConnections(request, am):
	date = datetime.now()
	date = date.date()
	form = am.connections
	form.date_of_assessment = date

	form.angerWorse = truePythonBool(request.POST.get('m_angerWorse'))
	form.troubleWhenUsing = truePythonBool(request.POST.get('m_troubleWhenUsing'))
	form.lessAngry = truePythonBool(request.POST.get('m_lessAngry'))
	form.othersTellMe = truePythonBool(request.POST.get('m_othersTellMe'))
	form.noConnection = truePythonBool(request.POST.get('m_noConnection'))
	form.otherConnectionsUsing = truePythonBool(request.POST.get('m_otherConnectionsUsing'))
	form.connectionExplain = request.POST.get('m_connectionExplain')

	form.save()
	am.save()

def saveAMWorst(request, am):
	date = datetime.now()
	date = date.date()
	form = am.worstEpisode
	form.date_of_assessment = date

	form.whoWorst = request.POST.get('whoWorst')
	form.happenedWorst = request.POST.get('happenedWorst')
	form.wordThoughtWorst = request.POST.get('wordThoughtWorst')
	form.howStartWorst = request.POST.get('howStartWorst')
	form.howEndWorst = request.POST.get('howEndWorst')

	form.physicalWorst = truePythonBool(request.POST.get('m_physicalWorst'))
	form.verbalWorst = truePythonBool(request.POST.get('m_verbalWorst'))
	form.propertyWorst = truePythonBool(request.POST.get('m_propertyWorst'))
	form.otherWorst = truePythonBool(request.POST.get('m_otherWorst'))
	form.otherWorstDescription = request.POST.get('m_otherWorstDescription')

	form.useWorst = truePythonBool(request.POST.get('useWorst'))

	form.whoUsed = request.POST.get('m_whoUsed')

	form.save()
	am.save()

def saveAMTarget(request, am):
	date = datetime.now()
	date = date.date()
	form = am.angerTarget
	form.date_of_assessment = date

	form.angryPartner = truePythonBool(request.POST.get('m_angryPartner'))
	form.angryParents = truePythonBool(request.POST.get('m_angryParents'))
	form.angryChildren = truePythonBool(request.POST.get('m_angryChildren'))
	form.angryRelatives = truePythonBool(request.POST.get('m_angryRelatives'))
	form.angryEmployer = truePythonBool(request.POST.get('m_angryEmployer'))
	form.angryFriends = truePythonBool(request.POST.get('m_angryFriends'))
	form.angryOther = truePythonBool(request.POST.get('m_angryOther'))
	form.seldomUpset = truePythonBool(request.POST.get('m_seldomUpset'))
	form.otherWhom = request.POST.get('m_otherWhom')
	form.angryAbout = request.POST.get('angryAbout')

	form.save()
	am.save()

def saveAMFamily(request, am):
	date = datetime.now()
	date = date.date()
	form = am.familyOrigin
	form.date_of_assessment = date

	form.kidMomAnger = request.POST.get('kidMomAnger')
	form.kidDadAnger = request.POST.get('kidDadAnger')
	form.kidSiblingAnger = request.POST.get('kidSiblingAnger')
	form.kidOtherAnger = request.POST.get('kidOtherAnger')
	form.learnFamilyAnger = request.POST.get('learnFamilyAnger')
	form.suicideHistory = truePythonBool(request.POST.get('suicideHistory'))
	form.hasLovingMother = truePythonBool(request.POST.get('m_hasLovingMother'))
	form.hasLovingSiblings = truePythonBool(request.POST.get('m_hasLovingSiblings'))

	form.save()
	am.save()

def saveAMProblems(request, am):
	date = datetime.now()
	date = date.date()
	form = am.currentProblems
	form.date_of_assessment = date

	form.describeIssue 		= request.POST.get('describeIssue')
	form.currentlyOnMeds 	= truePythonBool(request.POST.get('currentlyOnMeds'))
	form.whichMeds 			= request.POST.get('m_whichMeds')
	form.otherWhom 			= request.POST.get('m_otherWhom')

	form.brainInjury 			= truePythonBool(request.POST.get('m_brainInjury'))
	form.stroke 				= truePythonBool(request.POST.get('m_stroke'))
	form.epilepsy 				= truePythonBool(request.POST.get('m_epilepsy'))
	form.attentionDD 			= truePythonBool(request.POST.get('m_attentionDD'))
	form.pms 					= truePythonBool(request.POST.get('m_pms'))
	form.depression 			= truePythonBool(request.POST.get('m_depression'))
	form.ptsd 					= truePythonBool(request.POST.get('m_ptsd'))
	form.otherSeriousIllness 	= truePythonBool(request.POST.get('m_otherSeriousIllness'))

	form.save()
	am.save()

def saveAMControl(request, am):
	date = datetime.now()
	date = date.date()
	form = am.control
	form.date_of_assessment = date

	form.neverAttemptedControl 	= truePythonBool(request.POST.get('m_neverAttemptedControl'));
	form.talkToMyself 			= truePythonBool(request.POST.get('m_talkToMyself'));
	form.leaveScene 			= truePythonBool(request.POST.get('m_leaveScene'));
	form.relax 					= truePythonBool(request.POST.get('m_relax'));
	form.selfHelpGroup 			= truePythonBool(request.POST.get('m_selfHelpGroup'));
	form.otherControlAnger 		= truePythonBool(request.POST.get('m_otherControlAnger'));

	form.whatSayYou 		= request.POST.get('m_whatSayYou')
	form.howLongLeaveScene 	= request.POST.get('m_howLongLeaveScene')
	form.whatDoLeave 		= request.POST.get('m_whatDoLeave')
	form.howRelax 			= request.POST.get('m_howRelax')
	form.doWhatOtherControl = request.POST.get('m_doWhatOtherControl')

	form.save()
	am.save()

def saveAMFinal(request, am):
	date = datetime.now()
	date = date.date()
	form = am.final
	form.date_of_assessment = date

	form.anythingelse = request.POST.get('anythingelse')
	form.changeLearn1 = request.POST.get('changeLearn1')
	form.changeLearn2 = request.POST.get('changeLearn2')
	form.changeLearn3 = request.POST.get('changeLearn3')

	form.save()
	am.save()

def saveCompletedAmSection(request, section, am):
	if section == '/am_demographic/':
		saveAMDemographic(request, am)
	elif section == '/am_drugHistory/':
		saveAMDrugHistory(request, am)
	elif section == '/am_childhood/':
		saveAMChildhood(request, am)
	elif section == '/am_angerHistory/':
		saveAMAngerHistroy1(request, am)
	elif section == '/am_angerHistory2/':
		saveAMAngerHistroy2(request, am)
	elif section == '/am_angerHistory3/':
		saveAMAngerHistroy3(request, am)
	elif section == '/am_connections/':
		saveAMConnections(request, am)
	elif section == '/am_worst/':
		saveAMWorst(request, am)
	elif section == '/am_angerTarget/':
		saveAMTarget(request, am)
	elif section == '/am_familyOrigin/':
		saveAMFamily(request, am)
	elif section == '/am_problems/':
		saveAMProblems(request, am)
	elif section == '/am_control/':
		saveAMControl(request, am)
	elif section == '/am_final/':
		saveAMFinal(request, am)


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

def newAM(client):
	date = datetime.now()
	am = AngerManagement(client=client, isComplete=False, start_time=date)
	date = date.date()
	am.date_of_assessment = date

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
	am.initialized = False

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
	elif am.isComplete == True:
		section = '/am_viewForm/'

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
	result.append('/am_viewForm/')
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
	result.append(False)
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
	result.append(am.isComplete)
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
	normal = 'iml-button-incomplete'
	green = 'iml-button'
	current = 'iml-button-current'

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

def refresh_am1(demo):
	date = datetime.now()
	date = date.date()
	demo.date_of_assessment = date
	demo.maritalStatus = None
	demo.livingSituation = None
	demo.own = False
	demo.months_res = 0
	demo.years_res = 0
	demo.whoLivesWithClient = None
	demo.num_children = 0
	demo.spouse_dep = 0
	demo.other_dependants = 0
	demo.education = None
	demo.resasonDO = None
	demo.employee = None
	demo.job_title = None
	demo.emp_address = None
	demo.employed_months = 0
	demo.employed_years = 0
	demo.employer_phone = None
	demo.health_problem = False
	demo.medication = False
	demo.whatMedicine = None
	demo.health_exp = None

	demo.save()

def refresh_am2(dh):
	date = datetime.now()
	date = date.date()
	dh.date_of_assessment = date
	dh.firstDrinkAge = 0
	dh.firstDrinkType = None
	dh.curUse = False
	dh.useType = None
	dh.amtPerWeek = None
	dh.useAmt = None
	dh.everDrank = False
	dh.monthsQuit = 0
	dh.yearsQuit = 0
	dh.reasonQuit = None
	dh.DUI = False
	dh.numDUI = 0
	dh.BALevel = None
	dh.drugTreatment = False
	dh.treatmentPlace = None
	dh.dateTreated = None
	dh.finishedTreatment = False
	dh.reasonNotFinishedTreatment = None
	dh.isClean = False
	dh.relapseTrigger = None
	dh.drinkLastEpisode = False
	dh.drinkRelationshipProblem = False
	dh.needHelpDrugs = False

	dh.save()

def refresh_am3(child):
	date = datetime.now()
	date = date.date()
	child.date_of_assessment = date

	child.raisedBy = None
	child.momAlive = True
	child.dadAlive = True
	child.childTrama = False
	child.traumaExplain = None
	child.howLeftHome = None
	child.num_siblings = 0
	child.siblingsClose = True
	child.siblingsRelationshipExplain = None
	child.dadClose = False
	child.dadCloseExplain = None
	child.momClose = False
	child.momCloseExplain = None
	child.wasAbused = False
	child.abusedBy = None
	child.abuseImpact = None
	child.childAnger = False
	child.childAngerExplain = None
	child.otherChild = False
	child.otherChildExplain = None
	child.parentViolence = False
	child.parentViolenceExplain = None
	child.parentViolenceImpact = None

	child.save()

def refresh_am4(ah1):
	date = datetime.now()
	date = date.date()
	ah1.date_of_assessment = date

	ah1.recentIncidentV = None
	ah1.recentVDate = None
	ah1.recentVlocation = None
	ah1.withWhomRecentV = None
	ah1.happenedRecentV = None
	ah1.physicalRecentV = False
	ah1.verbalRecentV = False
	ah1.threatsRecentV = False
	ah1.propertyRecentV = False
	ah1.otherRecentV = False
	ah1.otherExplainRecentV = None
	ah1.typeWordsRecentV = None
	ah1.wasTense = False
	ah1.hadRush = False
	ah1.feltStrong = False
	ah1.psychoRecentV = False
	ah1.psychoWhyRecentV = None
	ah1.longAgoTreatRecentVmos = 0
	ah1.longAgoTreatRecentVyrs = 0
	ah1.didCompleteTreatRecentV = False
	ah1.reasonNotCompleteRecentV = None

	ah1.save()

def refresh_am5(ah2):
	date = datetime.now()
	date = date.date()
	ah2.date_of_assessment = date

	ah2.depress30RecentV = False
	ah2.depress30ExplainRecentV = None
	ah2.anxietyRecentV = False
	ah2.anxietyExplainRecentV = None
	ah2.hallucinationRecentV = False
	ah2.hallucinationLastV = None
	ah2.understandingRecentV = False
	ah2.understandingExplainRecentV = None
	ah2.troubleControlRecentV = False
	ah2.lastTimeTroubleControl = None
	ah2.controlTrigger = None
	ah2.suicide30RecentV = False
	ah2.suicide30ExplainRecentV = None
	ah2.suicideTodayRecentV = False
	ah2.suicideTodayPlanRecentV = False
	ah2.suicideTodayExplainRecentV = None
	ah2.hasAttemptedSuicide = False
	ah2.hasAttemptedExplainRecentV = None

	ah2.save()

def refresh_am6(ah3):
	date = datetime.now()
	date = date.date()
	ah3.date_of_assessment = date

	ah3.homicidal = False
	ah3.homicidalExplain = None
	ah3.medRecentV = False
	ah3.medRecentVExplain = None
	ah3.medSuccessRecentV = False
	ah3.medSuccessExplainRecentV = None
	ah3.durationRecentV = None
	ah3.intensityRecentV = 0
	ah3.howOften = None

	ah3.save()

def refresh_am7(connect):
	date = datetime.now()
	date = date.date()
	connect.date_of_assessment = date

	connect.angerWorse = False
	connect.troubleWhenUsing = False
	connect.lessAngry = False
	connect.othersTellMe = False
	connect.noConnection = False
	connect.otherConnectionsUsing = False
	connect.connectionExplain = None

	connect.save()

def refresh_am8(worst):
	date = datetime.now()
	date = date.date()
	worst.date_of_assessment = date

	worst.whoWorst = None
	worst.happenedWorst = None
	worst.wordThoughtWorst = None
	worst.howStartWorst = None
	worst.howEndWorst = None
	worst.useWorst = False
	worst.whoUsed = None
	worst.physicalWorst = False
	worst.verbalWorst = False
	worst.propertyWorst = False
	worst.otherWorst = False
	worst.otherWorstDescription = None

	worst.save()

def refresh_am9(target):
	date = datetime.now()
	date = date.date()
	target.date_of_assessment = date

	target.angryPartner = False
	target.angryParents = False
	target.angryChildren = False
	target.angryRelatives = False
	target.angryEmployer = False
	target.angryFriends = False
	target.angryOther = False
	target.otherWhom = None
	target.angryAbout = None
	target.seldomUpset = False

	target.save()

def refresh_am10(family):
	date = datetime.now()
	date = date.date()
	family.date_of_assessment = date

	family.kidMomAnger = None
	family.kidDadAnger = None
	family.kidSiblingAnger = None
	family.kidOtherAnger = None
	family.learnFamilyAnger = None
	family.suicideHistory = False
	family.hasLovingMother = False
	family.hasLovingSiblings = False

	family.save()

def refresh_am11(current):
	date = datetime.now()
	date = date.date()
	current.date_of_assessment = date

	current.brainInjury = False
	current.stroke = False
	current.epilepsy = False
	current.attentionDD = False
	current.pms = False
	current.depression = False
	current.ptsd = False
	current.otherSeriousIllness = False
	current.otherWhom = None
	current.currentlyOnMeds = False
	current.whichMeds = None
	current.describeIssue = None

	current.save()

def refresh_am12(control):
	date = datetime.now()
	date = date.date()
	control.date_of_assessment = date

	control.neverAttemptedControl = False
	control.talkToMyself = False
	control.whatSayYou = None
	control.leaveScene = False
	control.howLongLeaveScene = None
	control.whatDoLeave = None
	control.relax = False
	control.howRelax = None
	control.selfHelpGroup = False
	control.otherControlAnger = False
	control.doWhatOtherControl = None

	control.save()

def refresh_am13(final):
	date = datetime.now()
	date = date.date()
	final.date_of_assessment = date

	final.anythingelse = None
	final.changeLearn1 = None
	final.changeLearn2 = None
	final.changeLearn3 = None

	final.save()

def refreshAM(am):
	date = datetime.now()
	date = date.date()

	am.date_of_assessment = date

	refresh_am1(am.demographic)
	refresh_am2(am.drugHistory)
	refresh_am3(am.childhood)
	refresh_am4(am.angerHistory)
	refresh_am5(am.angerHistory2)
	refresh_am6(am.angerHistory3)
	refresh_am7(am.connections)
	refresh_am8(am.worstEpisode)
	refresh_am9(am.angerTarget)
	refresh_am10(am.familyOrigin)
	refresh_am11(am.currentProblems)
	refresh_am12(am.control)
	refresh_am13(am.final)

	am.demographicComplete = False
	am.drugHistoryComplete = False
	am.childhoodComplete = False
	am.angerHistoryComplete = False
	am.angerHistoryComplete2 = False
	am.angerHistoryComplete3 = False
	am.connectionsComplete = False
	am.worstComplete = False
	am.angerTargetComplete = False
	am.familyOriginComplete = False
	am.currentProblemsComplete = False
	am.controlComplete = False
	am.finalComplete = False

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

	am.isComplete = False
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
	result['isComplete'] = am.drugHistoryComplete

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
	fields['isComplete'] = am.connectionsComplete
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
	fields['isComplete'] = am.controlComplete
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
	fields['otherWhom'] = am.currentProblems.otherWhom
	fields['describeIssue'] = am.currentProblems.describeIssue
	fields['isComplete'] = am.currentProblemsComplete
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
	fields['isComplete'] = am.familyOriginComplete
	return fields

def grabAmWorstEpisodes(am):
	fields = {}

	selectBtn = am.worstEpisode.whoUsed
	index = None

	if selectBtn == None:
		index = 0
	else:
		if str(selectBtn) == 'Client Used Only':
			index = 1
		elif str(selectBtn) == 'The Other Party Used Only':
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
	fields['whoUsed'] = index
	fields['physicalWorst'] = am.worstEpisode.physicalWorst
	fields['verbalWorst'] = am.worstEpisode.verbalWorst
	fields['propertyWorst'] = am.worstEpisode.propertyWorst
	fields['otherWorst'] = am.worstEpisode.otherWorst
	fields['otherWorstDescription'] = am.worstEpisode.otherWorstDescription
	fields['isComplete'] = am.worstComplete
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
	fields['isComplete'] = am.angerTargetComplete
	return fields

def getAMDemoFields(am):
	data = {}
	phone = None

	data['maritalStatus'] = convertMaritalToIndex(am.demographic.maritalStatus)
	data['livingSituation'] = convertLivingToIndex(am.demographic.livingSituation)

	if am.demographic.employer_phone == None or am.demographic.employer_phone == '' or am.demographic.employer_phone == 'None':
		phone = am.demographic.employer_phone
	else:
		phone = convert_phone(am.demographic.employer_phone)

	data['own'] 				= am.demographic.own
	data['months_res'] 			= am.demographic.months_res
	data['years_res'] 			= am.demographic.years_res
	data['num_children'] 		= am.demographic.num_children
	data['education'] 			= am.demographic.education
	data['spouse_dep'] 			= am.demographic.spouse_dep
	data['other_dependants'] 	= am.demographic.other_dependants
	data['whoLivesWithClient'] 	= am.demographic.whoLivesWithClient
	data['resasonDO'] 			= am.demographic.resasonDO
	data['employee'] 			= am.demographic.employee
	data['job_title'] 			= am.demographic.job_title
	data['emp_address'] 		= am.demographic.emp_address
	data['employed_months'] 	= am.demographic.employed_months
	data['employed_years'] 		= am.demographic.employed_years
	data['employer_phone'] 		= phone
	data['health_problem'] 		= am.demographic.health_problem
	data['medication'] 			= am.demographic.medication
	data['whatMedicine'] 		= am.demographic.whatMedicine
	data['health_exp'] 			= am.demographic.health_exp
	data['isComplete'] 			= am.demographicComplete

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
	fields['traumaExplain'] = am.childhood.traumaExplain
	fields['howLeftHome'] = am.childhood.howLeftHome
	fields['siblingsRelationshipExplain'] = am.childhood.siblingsRelationshipExplain
	fields['dadCloseExplain'] = am.childhood.dadCloseExplain
	fields['momCloseExplain'] = am.childhood.momCloseExplain
	fields['abusedBy'] = am.childhood.abusedBy
	fields['abuseImpact'] = am.childhood.abuseImpact
	fields['childAngerExplain'] = am.childhood.childAngerExplain
	fields['otherChildExplain'] = am.childhood.otherChildExplain
	fields['parentViolenceExplain'] = am.childhood.parentViolenceExplain
	fields['parentViolenceImpact'] = am.childhood.parentViolenceImpact


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
	fields['isComplete'] = am.childhoodComplete

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
	fields['isComplete'] = am.angerHistoryComplete

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
	fields['isComplete'] = am.angerHistoryComplete2
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
	fields['isComplete'] = am.angerHistoryComplete3

	return fields

def grabAmFinal(am):
	fields = {}

	fields['anythingelse'] = am.final.anythingelse
	fields['changeLearn1'] = am.final.changeLearn1
	fields['changeLearn2'] = am.final.changeLearn2
	fields['changeLearn3'] = am.final.changeLearn3
	fields['isComplete'] = am.finalComplete

	return fields

def qbool(trigger, yes, no, dictList):
	checked = '/static/images/checked_checkbox.png'
	unchecked = '/static/images/unchecked_checkbox.png'
	yes = str(yes)
	no = str(no)

	if trigger == True:
		dictList[yes] = checked
		dictList[no] = unchecked
	else:
		dictList[yes] = unchecked
		dictList[no] = checked

def qCheck(trigger, fname, dictList):
	checked = '/static/images/checked_checkbox.png'
	unchecked = '/static/images/unchecked_checkbox.png'
	fname = str(fname)

	if trigger == True:
		dictList[fname] = checked
	else:
		dictList[fname] = unchecked

def fetchAmChecks(am):
	images = {}
	checked = '/static/images/checked_checkbox.png'
	unchecked = '/static/images/unchecked_checkbox.png'

	if (am.demographic.maritalStatus == 'Divorced'):
		images['divorced'] = checked
		images['married'] = unchecked
		images['single'] = unchecked
		images['separated'] = unchecked
	elif (am.demographic.maritalStatus == 'Married'):
		images['divorced'] = unchecked
		images['married'] = checked
		images['single'] = unchecked
		images['separated'] = unchecked
	elif (am.demographic.maritalStatus == 'Separated'):
		images['divorced'] = unchecked
		images['married'] = unchecked
		images['single'] = unchecked
		images['separated'] = checked
	elif (am.demographic.maritalStatus == 'Single'):
		images['divorced'] = unchecked
		images['married'] = unchecked
		images['single'] = checked
		images['separated'] = unchecked

	if am.demographic.livingSituation == 'Live alone':
		images['partner'] = unchecked
		images['alone'] = checked
		images['family'] = unchecked
		images['friend'] = unchecked
	elif am.demographic.livingSituation == 'Live with family':
		images['partner'] = unchecked
		images['alone'] = unchecked
		images['family'] = checked
		images['friend'] = unchecked
	elif am.demographic.livingSituation == 'Live with friend':
		images['partner'] = unchecked
		images['alone'] = unchecked
		images['family'] = unchecked
		images['friend'] = checked
	elif am.demographic.livingSituation == 'Live with partner':
		images['partner'] = checked
		images['alone'] = unchecked
		images['family'] = unchecked
		images['friend'] = unchecked

	if am.demographic.own == True:
		images['rent'] = unchecked
		images['own'] = checked
	else:
		images['rent'] = checked
		images['own'] = unchecked

	if am.demographic.education == 'HS':
		images['ged'] = unchecked
		images['hs'] = checked
		images['college'] = unchecked
	elif am.demographic.education == 'GED':
		images['ged'] = checked
		images['hs'] = unchecked
		images['college'] = unchecked
	elif am.demographic.education == 'College':
		images['ged'] = unchecked
		images['hs'] = unchecked
		images['college'] = checked
	elif am.demographic.education == 'Drop out':
		images['ged'] = unchecked
		images['hs'] = unchecked
		images['college'] = unchecked

	if am.demographic.health_problem == False:
		images['goodHealth'] = unchecked
		images['badHealth'] = checked
	else:
		images['goodHealth'] = checked
		images['badHealth'] = unchecked

	if am.demographic.medication == True:
		images['onMeds'] = checked
		images['noMeds'] = unchecked
	else:
		images['onMeds'] = unchecked
		images['noMeds'] = checked

	if am.angerHistory.psychoRecentV == True:
		images['yesEmotional'] = checked
		images['noEmotional'] = unchecked
	else:
		images['yesEmotional'] = unchecked
		images['noEmotional'] = checked

	if am.angerHistory.didCompleteTreatRecentV == True:
		images['didComplete'] = checked
		images['nopeComplete'] = unchecked
	else:
		images['nopeComplete'] = checked
		images['didComplete'] = unchecked

	if am.childhood.raisedBy == 'Parents':
		images['raisedParent'] = checked
		images['raisedGrand'] = unchecked
		images['raisedRelative'] = unchecked
		images['raisedFosted'] = unchecked
	elif am.childhood.raisedBy == 'Grandparents':
		images['raisedParent'] = unchecked
		images['raisedGrand'] = checked
		images['raisedRelative'] = unchecked
		images['raisedFosted'] = unchecked
	elif am.childhood.raisedBy == 'Relatives':
		images['raisedParent'] = unchecked
		images['raisedGrand'] = unchecked
		images['raisedRelative'] = checked
		images['raisedFosted'] = unchecked
	elif am.childhood.raisedBy == 'Foster':
		images['raisedParent'] = unchecked
		images['raisedGrand'] = unchecked
		images['raisedRelative'] = unchecked
		images['raisedFosted'] = checked

	if am.angerHistory3.howOften == 'This time only':
		images['tto'] = checked
		images['tmo'] = unchecked
		images['lsm'] = unchecked
		images['tsc'] = unchecked
		images['tta'] = unchecked
		images['oaa'] = unchecked
	elif am.angerHistory3.howOften == 'This month only':
		images['tto'] = unchecked
		images['tmo'] = checked
		images['lsm'] = unchecked
		images['tsc'] = unchecked
		images['tta'] = unchecked
		images['oaa'] = unchecked
	elif am.angerHistory3.howOften == 'Last six months':
		images['tto'] = unchecked
		images['tmo'] = unchecked
		images['lsm'] = checked
		images['tsc'] = unchecked
		images['tta'] = unchecked
		images['oaa'] = unchecked
	elif am.angerHistory3.howOften == 'Since childhood':
		images['tto'] = unchecked
		images['tmo'] = unchecked
		images['lsm'] = unchecked
		images['tsc'] = checked
		images['tta'] = unchecked
		images['oaa'] = unchecked
	elif am.angerHistory3.howOften == 'Adolecent':
		images['tto'] = unchecked
		images['tmo'] = unchecked
		images['lsm'] = unchecked
		images['tsc'] = unchecked
		images['tta'] = checked
		images['oaa'] = unchecked
	elif am.angerHistory3.howOften == 'Only as an adult':
		images['tto'] = unchecked
		images['tmo'] = unchecked
		images['lsm'] = unchecked
		images['tsc'] = unchecked
		images['tta'] = unchecked
		images['oaa'] = checked

	qbool(am.angerHistory2.depress30RecentV, 'yesSD', 'noSD', images)
	qbool(am.angerHistory2.anxietyRecentV, 'yesSax', 'noSax', images)
	qbool(am.angerHistory2.hallucinationRecentV, 'yesHall', 'noHall', images)
	qbool(am.angerHistory2.understandingRecentV, 'yesTU', 'noTU', images)
	qbool(am.angerHistory2.troubleControlRecentV, 'yesVB', 'noVB', images)
	qbool(am.angerHistory2.suicide30RecentV, 'yesThSU', 'noThSU', images)
	qbool(am.angerHistory2.suicideTodayRecentV, 'yesStoday', 'noStoday', images)
	qbool(am.angerHistory2.suicideTodayPlanRecentV, 'yesPlan', 'noPlan', images)
	qbool(am.angerHistory2.hasAttemptedSuicide, 'yesAttSU', 'noAttSU', images)
	qbool(am.angerHistory3.homicidal, 'yesHomicide', 'noHomicide', images)
	qbool(am.angerHistory3.medRecentV, 'yesPrescr', 'noPrescr', images)
	qbool(am.angerHistory3.medSuccessRecentV, 'yesSuccess', 'noSuccess', images)
	qbool(am.drugHistory.curUse, 'yesCurUse', 'nocurUse', images)
	qbool(am.drugHistory.everDrank, 'yeseverDrank', 'noeverDrank', images)
	qbool(am.drugHistory.DUI, 'yesDUI', 'noDUI', images)
	qbool(am.drugHistory.drugTreatment, 'yesdrugTreatment', 'nodrugTreatment', images)
	qbool(am.drugHistory.finishedTreatment, 'yesfinishedTreatment', 'nofinishedTreatment', images)
	qbool(am.drugHistory.isClean, 'yesisClean', 'noisClean', images)
	qbool(am.drugHistory.drinkLastEpisode, 'yesdrinkLastEpisode', 'nodrinkLastEpisode', images)
	qbool(am.drugHistory.drinkRelationshipProblem, 'yesdrinkRelationshipProblem', 'nodrinkRelationshipProblem', images)
	qbool(am.drugHistory.needHelpDrugs, 'yesneedHelpDrugs', 'noneedHelpDrugs', images)
	qbool(am.childhood.momAlive, 'momAlive', 'nomomAlive', images)
	qbool(am.childhood.dadAlive, 'dadAlive', 'nodadAlive', images)
	qbool(am.childhood.childTrama, 'childTrama', 'nochildTrama', images)
	qbool(am.childhood.siblingsClose, 'siblingsClose', 'nosiblingsClose', images)
	qbool(am.childhood.dadClose, 'dadClose', 'nodadClose', images)
	qbool(am.childhood.momClose, 'momClose', 'nomomClose', images)
	qbool(am.childhood.wasAbused, 'wasAbused', 'nowasAbused', images)
	qbool(am.childhood.childAnger, 'childAnger', 'nochildAnger', images)
	qbool(am.childhood.parentViolence, 'parentViolence', 'noparentViolence', images)
	qbool(am.childhood.otherChild, 'otherChild', 'nootherChild', images)
	qbool(am.worstEpisode.useWorst, 'useWorst', 'nouseWorst', images)

	qCheck(am.angerHistory.physicalRecentV, 'physicalRecentV', images)
	qCheck(am.angerHistory.verbalRecentV, 'verbalRecentV', images)
	qCheck(am.angerHistory.propertyRecentV, 'propertyRecentV', images)
	qCheck(am.angerHistory.otherRecentV, 'otherRecentV', images)
	qCheck(am.angerHistory.wasTense, 'wasTense', images)
	qCheck(am.angerHistory.hadRush, 'hadRush', images)
	qCheck(am.angerHistory.feltStrong, 'feltStrong', images)
	qCheck(am.connections.angerWorse, 'angerWorse', images)
	qCheck(am.connections.troubleWhenUsing, 'troubleWhenUsing', images)
	qCheck(am.connections.lessAngry, 'lessAngry', images)
	qCheck(am.connections.othersTellMe, 'othersTellMe', images)
	qCheck(am.connections.noConnection, 'noConnection', images)
	qCheck(am.connections.otherConnectionsUsing, 'otherConnectionsUsing', images)
	qCheck(am.worstEpisode.physicalWorst, 'physicalWorst', images)
	qCheck(am.worstEpisode.verbalWorst, 'verbalWorst', images)
	qCheck(am.worstEpisode.propertyWorst, 'propertyWorst', images)
	qCheck(am.worstEpisode.otherWorst, 'otherWorst', images)

	qCheck(am.angerTarget.angryPartner, 'angryPartner', images)
	qCheck(am.angerTarget.angryParents, 'angryParents', images)
	qCheck(am.angerTarget.angryChildren, 'angryChildren', images)
	qCheck(am.angerTarget.angryRelatives, 'angryRelatives', images)
	qCheck(am.angerTarget.angryEmployer, 'angryEmployer', images)
	qCheck(am.angerTarget.angryFriends, 'angryFriends', images)
	qCheck(am.angerTarget.angryOther, 'angryOther', images)
	qCheck(am.angerTarget.seldomUpset, 'seldomUpset', images)
	qCheck(am.currentProblems.brainInjury, 'brainInjury', images)
	qCheck(am.currentProblems.stroke, 'stroke', images)
	qCheck(am.currentProblems.epilepsy, 'epilepsy', images)
	qCheck(am.currentProblems.attentionDD, 'attentionDD', images)
	qCheck(am.currentProblems.pms, 'pms', images)
	qCheck(am.currentProblems.ptsd, 'ptsd', images)
	qCheck(am.currentProblems.otherSeriousIllness, 'otherSeriousIllness', images)
	qCheck(am.currentProblems.depression, 'depression', images)

	qbool(am.currentProblems.currentlyOnMeds, 'currentlyOnMeds', 'nocurrentlyOnMeds', images)

	qCheck(am.control.neverAttemptedControl, 'neverAttemptedControl', images)
	qCheck(am.control.talkToMyself, 'talkToMyself', images)
	qCheck(am.control.leaveScene, 'leaveScene', images)
	qCheck(am.control.relax, 'relax', images)
	qCheck(am.control.selfHelpGroup, 'selfHelpGroup', images)
	qCheck(am.control.otherControlAnger, 'otherControlAnger', images)

	if (am.familyOrigin.suicideHistory == True):
		images['suicideHistory'] = 'Yes'
	else:
		images['suicideHistory'] = 'No'


	return images


def grabAMViewForm(am):
	fields = {}
	fields['demo'] = getAMDemoFields(am)
	fields['dh'] = grabAmDhFields(am)
	fields['child'] = grabAmChildhood(am)
	fields['ah1'] = grabAmAngerHistory1(am)
	fields['ah2'] = grabAmAngerHistory2(am)
	fields['ah3'] = grabAmAngerHistory3(am)
	fields['target'] = grabAmTarget(am)
	fields['connect'] = grabAmConnections(am)
	fields['control'] = grabAmControl(am)
	fields['current'] = grabAmCurrentProblems(am)
	fields['family'] = grabAmFamilyOrigin(am)
	fields['worst'] = grabAmWorstEpisodes(am)
	fields['final'] = grabAmFinal(am)
	fields['images'] = fetchAmChecks(am)
	fields['emp_phone'] = fetchClientPhoneDisplay(am.demographic.employer_phone)

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
	elif location == '/am_viewForm/':
		fields = grabAMViewForm(am)

	return fields


def getDuplicateAM(client):
	amList = AngerManagement.objects.all()
	results = []

	for a in amList:
		if str(a.client.clientID) == str(client.clientID) and a.isComplete == False:
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
		if a.client == client and a.isComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientAM(client):
	ams = AngerManagement.objects.all()
	result = None

	for a in ams:
		if a.client == client and a.isComplete == False:
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
	session_id = request.POST.get('session_id', '')

	session = ClientSession.objects.get(id=session_id)
	client = session.client

	action = startAM(client)
	am = action['am']
	setGlobalID(am.id, request.user)

	openForm('am', am, client)
	session.hasAM = True
	session.am = am
	session.save()

	track = getTrack(request.user)

	result['AM'] = am
	result['session'] = session
	result['isNew'] = action['isNew']
	result['title'] = "Simeon Academy | Anger Management"
	result['save_this'] = 'false'
	result['tracking'] = track.state.state

	if action['isNew'] == False:
		next_section = nextAmPage(am, None)
		result['form'] = am
		result['form_type'] = 'am'
		result['type_header'] = 'Anger Management'
		result['next_section'] = next_section
		result['save_section'] = next_section

	return result

def processAMC(request):
	result = {}
	session_id = request.POST.get('session_id', '')
	am_id = request.POST.get('am_id', '')
	save_this = request.POST.get('save_this', '')
	section = request.POST.get('save_section', '')

	session = ClientSession.objects.get(id=session_id)
	am = AngerManagement.objects.get(id=am_id)
	saveAMChildhood(request, am)
	deprioritizeAM(am)
	fields = getAMFields(am, '/am_childhood/')
	json_data = json.dumps(fields)

	next_url = nextAmPage(am, '/am_childhood/')
	classes = grabAmClassesCSS(am, '/am_childhood/')
	image = amSidebarImages(am, '/am_childhood/')
	track = getTrack(request.user)

	result['tracking'] = track.state.state
	result['class'] = classes
	result['image'] = image
	result['next_url'] = next_url
	result['session'] = session
	result['AM'] = am
	result['fields'] = fields
	result['json_data'] = json_data
	result['current_section'] = '/am_childhood/'
	result['title'] = "Simeon Academy | Anger Management"

	return result

def processAMData(request, current_section):
	result = {}

	session_id = request.POST.get('session_id')
	am_id = request.POST.get('am_id')
	save_this = request.POST.get('save_this')
	section = request.POST.get('save_section')

	session = ClientSession.objects.get(id=session_id)
	am = AngerManagement.objects.get(id=(session.am.id))
	deprioritizeAM(am)
	fields = getAMFields(am, current_section)
	json_data = json.dumps(fields)

	if save_this == 'true':
		saveCompletedAmSection(request, section, am)
		setAmSectionComplete(am, section)

	next_url = nextAmPage(am, current_section)
	classes = grabAmClassesCSS(am, current_section)
	image = amSidebarImages(am, current_section)
	track = getTrack(request.user)

	result['tracking'] = track.state.state
	result['class'] = classes
	result['image'] = image
	result['next_url'] = next_url
	result['session'] = session
	result['AM'] = am
	result['fields'] = fields
	result['json_data'] = json_data
	result['current_section'] = current_section
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
			if (str(s.client.clientID) == str(client.clientID)) and (str(s.client.id) == str(client.id)) and (s.isComplete == False):
				exist = True
				break
	return exist

def grabIncompleteSap(client):
	result = None
	saps = SAP.objects.all()

	for s in saps:
		if (str(s.client.clientID) == str(client.clientID)) and (str(s.client.id) == str(client.id)) and (s.isComplete == False):
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
	result.append(sap.isComplete)
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
		for i in range(len(sap_list)):
			if sap_list[i]['complete'] == False:
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
		if s.client == client and s.isComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientSAP(client):
	sap = SAP.objects.all()
	result = None

	for s in sap:
		if s.client == client and s.isComplete == False:
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
	proceed = True
	sap = None
	action = {}
	action['isNew'] = False
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	session = ClientSession.objects.get(id=session_id)
	client = session.client

	if session.hasSAP == True:
		if session.sap.isComplete == True:
			sap = session.sap
			setGlobalID(sap.id, request.user)
			result['isNew'] = False
			proceed = False

	if proceed == True:
		action = startSAP(client)
		sap = action['sap']
		setGlobalID(sap.id, request.user)
		result['isNew'] = action['isNew']

	openForm('sap', sap, client)
	session.hasSAP = True
	session.sap = sap
	session.save()
	result['sap'] = sap
	result['session'] = session
	
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
	normal = 'iml-button-incomplete'
	green = 'iml-button'
	current = 'iml-button-current'

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
	elif section == '/sap_viewForm/':
		result = grabSapViewFields(sap)
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

	fields['clinicalComplete'] = sap.clinicalComplete
	fields['socialComplete'] = sap.socialComplete
	fields['psycho2Complete'] = sap.psycho2Complete
	fields['specialComplete'] = sap.specialComplete
	fields['otherComplete'] = sap.otherComplete
	fields['sourcesComplete'] = sap.sourcesComplete

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

	fields['psychoComplete'] = sap.psychoComplete

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
	sap.save()

def getSAPViewImages(sap):
	results = {}
	results['isChild'] = getViewFormCheckImages(sap.demographics.isChild)
	results['isSenior'] = getViewFormCheckImages(sap.demographics.isSenior)
	results['isDual'] = getViewFormCheckImages(sap.demographics.isDual)
	results['isOther'] = getViewFormCheckImages(sap.demographics.isOther)
	results['isNone'] = getViewFormCheckImages(sap.demographics.isNone)
	return results

def grabSapViewFields(sap):
	result = {}
	result['images'] 	= getSAPViewImages(sap)
	result['main'] 		= grabSapDemoFields(sap)
	result['psycho']	= grabSapPsychoFields(sap)
	# result['date']		= str(sap.date_of_assessment)
	return result

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
		special = request.POST.get('m_special')

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
	demo = sap.demographics

	if str(section) == '/sap_demographic/':
		problem = request.POST.get('problem', '')
		health = request.POST.get('health', '')

		demo.problem = problem
		demo.health = health
		demo.save()
		sap.save()

	elif str(section) == '/sap_social/':
		family = request.POST.get('family')

		demo.family = family
		demo.save()
		sap.save()

	elif str(section) == '/sap_psychoactive/':
		saveSapPhycho1(request, sap)

	elif str(section) == '/sap_psychoactive2/':
		psychoactive = request.POST.get('psychoactive')

		demo.psychoactive = psychoactive
		demo.save()
		sap.save()

	elif str(section) == '/sap_special/':
		isChild = request.POST.get('m_isChild', '')
		isSenior = request.POST.get('m_isSenior', '')
		isDual = request.POST.get('m_isDual', '')
		isOther = request.POST.get('m_isOther', '')
		isNone = request.POST.get('m_isNone', '')
		special = request.POST.get('m_special')

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
		sap.save()

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

	sap.isComplete = False
	sap.save()

def fetchAllClientSaps(client):
	result = []
	saps = SAP.objects.all()

	for s in saps:
		if clientEqual(client, s.client) == True:
			result.append(s)

	return result

def getClientOpenSap(client):
	result = None
	saps = fetchAllClientSaps(client)

	for s in saps:
		if s.isOpen == True:
			result = s
			break
	return result


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
	track = getTrack(request.user)

	if current_section == '/sap_viewForm/':
		result['s_date'] = sap.date_of_assessment

	result['tracking'] = track.state.state
	result['current_section'] = current_section
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
	result.append('viewForm')

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
	result.append('isComplete')

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
	result.append('/mh_viewForm/')

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
	result.append(' ')

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
	result.append(mh.isComplete)

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
	result.append(False)

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
	result 		= None
	flag 		= None
	mh_list 	= grabOrderedMh(mh)

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
	result = ''
	next_section = ''
	proceed = True
	no_result = False
	mh_list = grabOrderedMh(mh)

	for m in mh_list:
		if m['priority'] == True:
			result = m['url']
			proceed = False
			break

	if proceed == True:
		for i in range(len(mh_list)):
			if mh_list[i]['complete'] == False:
				next_section = mh_list[i]['url']
				break

		if str(next_section) == str(section):
			result = forceNextMhPage(mh)
		else:
			result = next_section

	return result

def hasIncompleteMh(client):
	exist = False
	mhs = MentalHealth.objects.all()

	for m in mhs:
		if m.client == client and m.isComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientMh(client):
	mhs = MentalHealth.objects.all()
	result = None

	for m in mhs:
		if m.client == client and m.isComplete == False:
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
	mh.isComplete = False
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

	session = ClientSession.objects.get(id=session_id)
	client = session.client

	action = startMH(client)
	mh = action['mh']
	setGlobalID(mh.id, request.user)

	openForm('mh', mh, client)
	session.hasMH = True
	session.mh = mh
	session.save()

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
	normal = 'iml-button-incomplete-sm'
	green = 'iml-button-sm'
	current = 'iml-button-current-sm'

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

	m_state = getOrderedStateIndex(mh.demographics.motherState)
	f_state = getOrderedStateIndex(mh.demographics.fatherState)

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
	results['motherState'] = m_state
	results['motherLiving'] = mh.demographics.motherLiving
	results['motherAge'] = mh.demographics.motherAge
	results['motherAgeDeath'] = mh.demographics.motherAgeDeath

	results['fatherOccupation'] = mh.demographics.fatherOccupation
	results['fatherCity'] = mh.demographics.fatherCity
	results['fatherLiving'] = mh.demographics.fatherLiving
	results['fatherState'] = f_state
	results['fatherAge'] = mh.demographics.fatherAge
	results['fatherAgeDeath'] = mh.demographics.fatherAgeDeath

	results['numChildren'] = mh.demographics.numChildren
	results['numSisters'] = mh.demographics.numSisters
	results['numBrothers'] = mh.demographics.numBrothers

	results['childrenMale'] = mh.demographics.childrenMale
	results['childrenFemale'] = mh.demographics.childrenFemale
	results['bothers'] = mh.demographics.bothers
	results['sisters'] = mh.demographics.sisters

	results['isComplete'] = mh.demographicsComplete

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

	result['isComplete'] = mh.educationComplete

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

	results['isComplete'] = mh.backgroundComplete

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

	result['isComplete'] = mh.stressorComplete

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

	result['isComplete'] = mh.familyComplete

	return result

def getMhPsychFields(mh):
	result = {}
	result['psychiatricHistory'] = mh.stressors.psychiatricHistory
	result['isComplete'] = mh.psychComplete
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

	result['isComplete'] = mh.legalComplete

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

	result['isComplete'] = mh.useComplete

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
	elif str(section) == '/mh_psych/':
		result = getMhPsychFields(mh)
	elif str(section) == '/mh_useTable/':
		result = getMhUseFields(mh)

	return result

def getLastWordIndex(text):
	count = len(text) 
 
	while text[count] != ' ' and count != 0:
		count = count - 1

		if count == 0:
			break;
	# count = count + 1
	return count

def getLastWord(text):
	result = ''
	start = getLastWordIndex(text)
	for i in range(start, len(text)):
		result += text[i]
	return result

def splitWords(text):
	result = []
	temp = ''

	for t in text:
		if t != ' ':
			temp += t
		else:
			temp += ' '
			result.append(temp)
			temp = ''

	result.append(temp)
	# lWord = getLastWord(text)
	# result.append(lWord)
	return result

def wordFits(lineLength, word):
	canFit = False
	if len(word) <= lineLength:
		canFit = True
	return canFit

def grabSingleLine(lineLength, text):
	word = splitWords(text)
	current = 0
	numWords = 0
	line = ''
	result = {}

	for w in word:
		lineLength = lineLength - current
		if wordFits(lineLength, w):
			line += w
			current = len(w)
			numWords += 1
		else:
			break
	result['numWords'] = numWords
	result['line'] = line
	return result

def grabLines(lineLength, text):
	word = splitWords(text)
	nLine = lineLength
	nWord = ''
	current = 0
	index = 0
	line = ''
	result = []

	for w in word:
		nLine = nLine - current
		line += nWord

		if wordFits(nLine, w):
			line += w
			current = len(w)
			index += 1
			nWord = ''
		else:
			result.append(line)
			nLine = lineLength
			current = 0
			line = ''
			nWord = w

	result.append(line)

	return result

def grabLinesInfo(numLines, lineLength, text):
	word = splitWords(text)
	nLine = lineLength
	nWord = ''
	current = 0
	c_line = 0
	index = 0
	line = ''
	lines = []
	result = {}

	for w in word:
		nLine = nLine - current
		line += nWord

		if nWord != '':
			index += 1

		if wordFits(nLine, w):
			line += w
			current = len(w)
			index += 1
			nWord = ''
		else:
			lines.append(line)
			nLine = lineLength
			current = 0
			line = ''
			nWord = w

		c_line = len(lines)
		if c_line == numLines:
			break

	lines.append(line)
	result['lines'] = lines
	result['index'] = index
	return result

def splitFormLines(numLines, lineLength, text):
	result = {}
	lines = grabLines(lineLength, text)

	for i in range(numLines):
		num = i + 1
		name = 'line' + str(num)

		if i < len(lines):
			result[name] = lines[i]
		else:
			result[name] = ' '

	return result

def splitFormLinesInfo(numLines, lineLength, text):
	result = {}
	data = grabLinesInfo(lineLength, text)
	index = data['index']
	lines = data['lines']

	for i in range(numLines):
		num = i + 1
		name = 'line' + str(num)

		if i < len(lines):
			result[name] = lines[i]
		else:
			result[name] = ' '

	result['index'] = index
	return result


def multiLineSplit(numLines, line1Length, otherLineLength, text):
	result = {}
	firstInfo = grabSingleLine(line1Length, text)
	lin1 = firstInfo['line']
	t2 = ''

	words = splitWords(text)
	for i in range(firstInfo['numWords'], len(words)):
		t2 += words[i]

	lines = grabLines(otherLineLength, t2)
	s_num = len(lines)
	s_num += 1

	for i in range(numLines):
		num = i + 1
		name = 'line' + str(num)

		if i < s_num:
			if i == 0:
				result[name] = lin1

			else:
				result[name] = lines[i - 1]
		else:
			result[name] = ' '
	return result

def superSplit(section1Length, numSec1, section2Length, numSec2, text):
	result = {}
	t2 = ''
	totalLines = numSec1 + numSec2 + 1
	start2 = numSec1 + 1

	sec1 = grabLinesInfo(numSec1, section1Length, text)
	index = sec1['index']

	words = splitWords(text)

	for i in range(index, len(words)):
		t2 += words[i]

	sec2 = grabLinesInfo(numSec2, section2Length, t2)

	sec1 = sec1['lines']
	sec2 = sec2['lines']

	sc = []

	for s1 in sec1:
		sc.append(s1)
	for s2 in sec2:
		sc.append(s2)

	for i in range(totalLines):
		num = i + 1
		name = 'line' + str(num)

		if i < len(sc):
			result[name] = sc[i]
		else:
			result[name] = ' '

	return result

def fetchClientSSDisplay(ss):
	result = None
	if ss != None:
		if fieldIsEmpty(ss) == False and len(ss) > 8:
			ss = cleanWhiteSpace(ss)
			ss = prepareNumbersearch(ss)
			result = ''
			result += ss[0]
			result += ss[1]
			result += ss[2]
			result += '-'
			result += ss[3]
			result += ss[4]
			result += '-'
			result += ss[5]
			result += ss[6]
			result += ss[7]
			result += ss[8]
	return result

def fetchClientPhoneDisplay(phone):
	result = None
	if phone != None:
		if fieldIsEmpty(phone) == False and len(phone) > 9:
			phone = cleanWhiteSpace(phone)
			phone = prepareNumbersearch(phone)
			result = ''
			result += '('
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

def fetchGenderDisplay(isMale):
	result = 'Female'
	if isMale == True:
		result = 'Male'
	return result

def fetchStatusDisplay(isDischarged):
	result = 'ACTIVE'
	if isDischarged == True:
		result = 'DISCHARGED'
	return result

def grabMhViewImages(mh):
	result = {}
	check = "/static/images/check_o.png"
	nope = '/static/images/nope.png'

	result['pastWork'] = multiLineSplit(2, 60, 80, str(mh.demographics.pastJobs))
	result['psychHistory'] = splitFormLines(6, 80, str(mh.stressors.psychiatricHistory))
	result['pAnsExp'] = multiLineSplit(4, 60, 80, str(mh.legalHistory.explainPositiveAnswers))
	result['m_children'] = decodeCharfield(mh.demographics.childrenMale)
	result['f_children'] = decodeCharfield(mh.demographics.childrenFemale)
	result['m_brothers'] = decodeCharfield(mh.demographics.bothers)
	result['f_sisters'] = decodeCharfield(mh.demographics.sisters)
	result['RSSN'] = fetchClientSSDisplay(mh.client.ss_num)
	result['RCPHONE'] = fetchClientPhoneDisplay(mh.client.phone)

	if mh.demographics.maritalStatus == 'Married':
		result['Married'] = check
		result['Single'] = nope
		result['Divorced'] = nope
		result['Widowed'] = nope
		result['Seperated'] = nope
	elif mh.demographics.maritalStatus == 'Single':
		result['Married'] = nope
		result['Single'] = check
		result['Divorced'] = nope
		result['Widowed'] = nope
		result['Seperated'] = nope
	elif mh.demographics.maritalStatus == 'Divorced':
		result['Married'] = nope
		result['Single'] = nope
		result['Divorced'] = check
		result['Widowed'] = nope
		result['Seperated'] = nope
	elif mh.demographics.maritalStatus == 'Widowed':
		result['Married'] = nope
		result['Single'] = nope
		result['Divorced'] = nope
		result['Widowed'] = check
		result['Seperated'] = nope
	elif mh.demographics.maritalStatus == 'Seperated':
		result['Married'] = nope
		result['Single'] = nope
		result['Divorced'] = nope
		result['Widowed'] = nope
		result['Seperated'] = check

	if mh.client.isMale == True:
		result['male'] = check
		result['female'] = nope
	else:
		result['male'] = nope
		result['female'] = check

	if mh.education.BehaviorProblemsKto6 == True:
		result['bk6'] = 'Yes'
	else:
		result['bk6'] = 'None'

	if mh.education.BehaviorProblems7to9 == True:
		result['b79'] = 'Yes'
	else:
		result['b79'] = 'None'

	if mh.education.BehaviorProblems10to12 == True:
		result['b1012'] = 'Yes'
	else:
		result['b1012'] = 'None'


	if mh.education.AcademicProblemsKto6 == True:
		result['ak6'] = 'Yes'
	else:
		result['ak6'] = 'None'

	if mh.education.AcademicProblems7to9 == True:
		result['a79'] = 'Yes'
	else:
		result['a79'] = 'None'

	if mh.education.AcademicProblems10to12 == True:
		result['a1012'] = 'Yes'
	else:
		result['a1012'] = 'None'


	if mh.education.FriendshipsKto6 < 5:
		result['fs1'] = ' '
	else:
		result['fs1'] = mh.education.FriendshipsKto6
	if mh.education.Friendships7to9 < 5:
		result['fs2'] = ' '
	else:
		result['fs2'] = mh.education.Friendships7to9
	if mh.education.Friendships10to12 < 5:
		result['fs3'] = ' '
	else:
		result['fs3'] = mh.education.Friendships10to12


	if mh.education.FriendshipsKto6 == 1:
		result['a1'] = 'junkie'
		result['a2'] = None
		result['a3'] = None
		result['a4'] = None
		result['a5'] = None
	elif mh.education.FriendshipsKto6 == 2:
		result['a1'] = None
		result['a2'] = 'junkie'
		result['a3'] = None
		result['a4'] = None
		result['a5'] = None
	elif mh.education.FriendshipsKto6 == 3:
		result['a1'] = None
		result['a2'] = None
		result['a3'] = 'junkie'
		result['a4'] = None
		result['a5'] = None
	elif mh.education.FriendshipsKto6 == 4:
		result['a1'] = None
		result['a2'] = None
		result['a3'] = None
		result['a4'] = 'junkie'
		result['a5'] = None
	elif mh.education.FriendshipsKto6 > 4:
		result['a1'] = None
		result['a2'] = None
		result['a3'] = None
		result['a4'] = None
		result['a5'] = 'junkie'

	if mh.education.Friendships7to9 == 1:
		result['b1'] = 'junkie'
		result['b2'] = None
		result['b3'] = None
		result['b4'] = None
		result['b5'] = None
	elif mh.education.Friendships7to9 == 2:
		result['b1'] = None
		result['b2'] = 'junkie'
		result['b3'] = None
		result['b4'] = None
		result['b5'] = None
	elif mh.education.Friendships7to9 == 3:
		result['b1'] = None
		result['b2'] = None
		result['b3'] = 'junkie'
		result['b4'] = None
		result['b5'] = None
	elif mh.education.Friendships7to9 == 4:
		result['b1'] = None
		result['b2'] = None
		result['b3'] = None
		result['b4'] = 'junkie'
		result['b5'] = None
	elif mh.education.Friendships7to9 > 4:
		result['b1'] = None
		result['b2'] = None
		result['b3'] = None
		result['b4'] = None
		result['b5'] = 'junkie'

	if mh.education.Friendships10to12 == 1:
		result['c1'] = 'junkie'
		result['c2'] = None
		result['c3'] = None
		result['c4'] = None
		result['c5'] = None
	elif mh.education.Friendships10to12 == 2:
		result['c1'] = None
		result['c2'] = 'junkie'
		result['c3'] = None
		result['c4'] = None
		result['c5'] = None
	elif mh.education.Friendships10to12 == 3:
		result['c1'] = None
		result['c2'] = None
		result['c3'] = 'junkie'
		result['c4'] = None
		result['c5'] = None
	elif mh.education.Friendships10to12 == 4:
		result['c1'] = None
		result['c2'] = None
		result['c3'] = None
		result['c4'] = 'junkie'
		result['c5'] = None
	elif mh.education.Friendships10to12 > 4:
		result['c1'] = None
		result['c2'] = None
		result['c3'] = None
		result['c4'] = None
		result['c5'] = 'junkie'

	if mh.education.collegeYears == 1:
		result['d1'] = 'junkie'
		result['d2'] = None
		result['d3'] = None
		result['d4'] = None
		result['d5'] = None
	elif mh.education.collegeYears == 2:
		result['d1'] = None
		result['d2'] = 'junkie'
		result['d3'] = None
		result['d4'] = None
		result['d5'] = None
	elif mh.education.collegeYears == 3:
		result['d1'] = None
		result['d2'] = None
		result['d3'] = 'junkie'
		result['d4'] = None
		result['d5'] = None
	elif mh.education.collegeYears == 4:
		result['d1'] = None
		result['d2'] = None
		result['d3'] = None
		result['d4'] = 'junkie'
		result['d5'] = None
	elif mh.education.collegeYears > 4:
		result['d1'] = None
		result['d2'] = None
		result['d3'] = None
		result['d4'] = None
		result['d5'] = 'junkie'

	if mh.education.collegeDegree == True:
		result['grad'] = 'junkie'

	if mh.education.advanceDegree == True:
		result['advDeg'] = check
	else:
		result['advDeg'] = nope

	if mh.education.honorableDischarge == True:
		result['yeshonor'] = 'junkie'
		result['nohonor'] = nope
	else:
		result['yeshonor'] = nope
		result['nohonor'] = 'junkie'

	if mh.background.residence == 'Rent':
		result['rent'] = check
		result['own'] = nope
		result['subHouse'] = nope
	elif mh.background.residence == 'Own Home':
		result['own'] = check
		result['rent'] = nope
		result['subHouse'] = nope
	elif mh.background.residence == 'Subsidized Housing':
		result['subHouse'] = check
		result['own'] = nope
		result['rent'] = nope

	if mh.background.income == 'Low':
		result['ilow'] = check
		result['imed'] = nope
		result['ihi'] = nope
	elif mh.background.income == 'Medium':
		result['imed'] = check
		result['ilow'] = nope
		result['ihi'] = nope
	elif mh.background.income == 'High':
		result['ihi'] = check
		result['ilow'] = nope
		result['imed'] = nope

	if mh.background.debt == 'Low':
		result['dlow'] = check
		result['dmed'] = nope
		result['dhi'] = nope
	elif mh.background.debt == 'Medium':
		result['dmed'] = check
		result['dlow'] = nope
		result['dhi'] = nope
	elif mh.background.debt == 'High':
		result['dhi'] = check
		result['dlow'] = nope
		result['dmed'] = nope

	if mh.background.credit == 'Poor':
		result['poor'] = check
		result['fair'] = nope
		result['good'] = nope
		result['bankrupt'] = nope
	elif mh.background.credit == 'Fair':
		result['fair'] = check
		result['poor'] = nope
		result['good'] = nope
		result['bankrupt'] = nope
	elif mh.background.credit == 'Good':
		result['good'] = check
		result['poor'] = nope
		result['bankrupt'] = nope
		result['fair'] = nope
	elif mh.background.credit == 'Bankruptcy':
		result['bankrupt'] = check
		result['poor'] = nope
		result['good'] = nope
		result['fair'] = nope

	if mh.background.healthCare == 'Company Health Benefits':
		result['hc'] = check
		result['pi'] = nope
		result['medicaid'] = nope
		result['medicare'] = nope
		result['selfpay'] = nope
	elif mh.background.healthCare == 'Private Insurance':
		result['pi'] = check
		result['hc'] = nope
		result['medicaid'] = nope
		result['medicare'] = nope
		result['selfpay'] = nope
	elif mh.background.healthCare == 'Medicaid':
		result['medicaid'] = check
		result['pi'] = nope
		result['hc'] = nope
		result['medicare'] = nope
		result['selfpay'] = nope
	elif mh.background.healthCare == 'Medicare':
		result['medicare'] = check
		result['pi'] = nope
		result['hc'] = nope
		result['medicaid'] = nope
		result['selfpay'] = nope
	elif mh.background.healthCare == 'Self-Pay':
		result['selfpay'] = check
		result['pi'] = nope
		result['hc'] = nope
		result['medicare'] = nope
		result['medicaid'] = nope

	if mh.background.otherIncome == 'Alimony':
		result['ali'] = check
		result['cs'] = nope
		result['adc'] = nope
		result['ssi'] = nope
		result['retired'] = nope
		result['sfr'] = nope
	elif mh.background.otherIncome == 'Child Support':
		result['ali'] = nope
		result['cs'] = check
		result['adc'] = nope
		result['ssi'] = nope
		result['retired'] = nope
		result['sfr'] = nope
	elif mh.background.otherIncome == 'Aid to Dependant Children':
		result['ali'] = nope
		result['cs'] = nope
		result['adc'] = check
		result['ssi'] = nope
		result['retired'] = nope
		result['sfr'] = nope
	elif mh.background.otherIncome == 'SSI':
		result['ali'] = nope
		result['cs'] = nope
		result['adc'] = nope
		result['ssi'] = check
		result['retired'] = nope
		result['sfr'] = nope
	elif mh.background.otherIncome == 'Retired':
		result['ali'] = nope
		result['cs'] = nope
		result['adc'] = nope
		result['ssi'] = nope
		result['retired'] = check
		result['sfr'] = nope
	elif mh.background.otherIncome == 'Support from Relatives':
		result['ali'] = nope
		result['cs'] = nope
		result['adc'] = nope
		result['ssi'] = nope
		result['retired'] = nope
		result['sfr'] = check

	if mh.background.spouseRelationship == 'Poor':
		result['spouseP'] = check
		result['spouseA'] = nope
		result['spouseG'] = nope
	elif mh.background.spouseRelationship == 'Average':
		result['spouseP'] = nope
		result['spouseA'] = check
		result['spouseG'] = nope
	elif mh.background.spouseRelationship == 'Good':
		result['spouseP'] = nope
		result['spouseA'] = nope
		result['spouseG'] = check

	if mh.background.brothersRelationship == 'Poor':
		result['broP'] = check
		result['broA'] = nope
		result['broG'] = nope
	elif mh.background.brothersRelationship == 'Average':
		result['broP'] = nope
		result['broA'] = check
		result['broG'] = nope
	elif mh.background.brothersRelationship == 'Good':
		result['broP'] = nope
		result['broA'] = nope
		result['broG'] = check

	if mh.background.childrenRelationship == 'Poor':
		result['childP'] = check
		result['childA'] = nope
		result['childG'] = nope
	elif mh.background.childrenRelationship == 'Average':
		result['childP'] = nope
		result['childA'] = check
		result['childG'] = nope
	elif mh.background.childrenRelationship == 'Good':
		result['childP'] = nope
		result['childA'] = nope
		result['childG'] = check

	if mh.background.parentsRelationship == 'Poor':
		result['parentP'] = check
		result['parentA'] = nope
		result['parentG'] = nope
	elif mh.background.parentsRelationship == 'Average':
		result['parentP'] = nope
		result['parentA'] = check
		result['parentG'] = nope
	elif mh.background.parentsRelationship == 'Good':
		result['parentP'] = nope
		result['parentA'] = nope
		result['parentG'] = check

	if mh.background.sistersRelationship == 'Poor':
		result['sisP'] = check
		result['sisA'] = nope
		result['sisG'] = nope
	elif mh.background.sistersRelationship == 'Average':
		result['sisP'] = nope
		result['sisA'] = check
		result['sisG'] = nope
	elif mh.background.sistersRelationship == 'Good':
		result['sisP'] = nope
		result['sisA'] = nope
		result['sisG'] = check

	if mh.background.exRelationship == 'Poor':
		result['exP'] = check
		result['exA'] = nope
		result['exG'] = nope
	elif mh.background.exRelationship == 'Average':
		result['exP'] = nope
		result['exA'] = check
		result['exG'] = nope
	elif mh.background.exRelationship == 'Good':
		result['exP'] = nope
		result['exA'] = nope
		result['exG'] = check

	if mh.background.closeFriendVisit == 'Weekly':
		result['cfw'] = check
		result['cfm'] = nope
		result['cfy'] = nope
	elif mh.background.closeFriendVisit == 'Monthly':
		result['cfw'] = nope
		result['cfm'] = check
		result['cfy'] = nope
	elif mh.background.closeFriendVisit == 'Yearly':
		result['cfw'] = nope
		result['cfm'] = nope
		result['cfy'] = check

	if mh.background.acqVisit == 'Weekly':
		result['afw'] = check
		result['afm'] = nope
		result['afy'] = nope
	elif mh.background.acqVisit == 'Monthly':
		result['afw'] = nope
		result['afm'] = check
		result['afy'] = nope
	elif mh.background.acqVisit == 'Yearly':
		result['afw'] = nope
		result['afm'] = nope
		result['afy'] = check

	if mh.legalHistory.probationPresent == True:
		result['probPresent'] = check
	else:
		result['probPresent'] = nope

	if mh.legalHistory.probationPast == True:
		result['probPast'] = check
	else:
		result['probPast'] = nope

	if mh.legalHistory.suspendedDrivePresent == True:
		result['susPre'] = check
	else:
		result['susPre'] = nope

	if mh.legalHistory.hasLawsuit == True:
		result['lawsuit'] = 'Yes'
	else:
		result['lawsuit'] = 'No'

	if mh.legalHistory.lawsuitStress == True:
		result['lawStress'] = 'Yes'
	else:
		result['lawStress'] = 'No'

	if mh.legalHistory.inDivorce == True:
		result['inDiv'] = check
		result['noIsDiv'] = nope
	else:
		result['inDiv'] = nope
		result['noIsDiv'] = check

	if mh.legalHistory.childCustody == True:
		result['inCust'] = check
		result['noCust'] = nope
	else:
		result['inCust'] = nope
		result['noCust'] = check

	if mh.legalHistory.hasBankrupcy == True:
		result['inBnkR'] = check
		result['noBnkR'] = nope
	else:
		result['inBnkR'] = nope
		result['noBnkR'] = check

	return result


def saveMhDemo(request, mh):
	mh.demographics.birthplace 			= request.POST.get('birthplace');
	mh.demographics.raised 				= request.POST.get('raised');
	mh.demographics.occupation 			= request.POST.get('occupation');
	mh.demographics.employer 			= request.POST.get('employer');
	mh.demographics.pastJobs 			= request.POST.get('pastJobs');
	mh.demographics.recentMove 			= request.POST.get('recentMove');
	mh.demographics.motherOccupation 	= request.POST.get('motherOccupation');
	mh.demographics.motherCity 			= request.POST.get('motherCity');
	mh.demographics.fatherOccupation 	= request.POST.get('fatherOccupation');
	mh.demographics.fatherCity 			= request.POST.get('fatherCity');
	mh.demographics.employedMo 			= request.POST.get('employedMo');
	mh.demographics.employedYrs 		= request.POST.get('employedYrs');
	mh.demographics.childrenMale 		= request.POST.get('childrenMale');
	mh.demographics.childrenFemale 		= request.POST.get('childrenFemale');
	mh.demographics.bothers 			= request.POST.get('m_brothersFinal');
	mh.demographics.sisters 			= request.POST.get('m_sistersFinal');
	mh.demographics.motherAge 			= request.POST.get('m_motherAge');
	mh.demographics.motherAgeDeath 		= request.POST.get('m_motherAgeDeath');
	mh.demographics.fatherAge 			= request.POST.get('m_fatherAge');
	mh.demographics.fatherAgeDeath 		= request.POST.get('m_fatherAgeDeath');
	mh.demographics.maritalStatus 		= request.POST.get('maritalStatus');
	mh.demographics.numMarriages 		= request.POST.get('m_numMarriages')
	mh.demographics.spouseAge 			= request.POST.get('m_spouseAge')
	mh.demographics.spouseOccupation 	= request.POST.get('m_spouseOccupation')
	mh.demographics.spouseEmployer 		= request.POST.get('m_spouseEmployer')
	mh.demographics.spouseWorkMos 		= request.POST.get('m_spouseWorkMos')
	mh.demographics.spouseWorkYrs 		= request.POST.get('m_spouseWorkYrs')
	mh.demographics.motherLiving 		= truePythonBool(request.POST.get('motherLiving'));
	mh.demographics.fatherLiving 		= truePythonBool(request.POST.get('fatherLiving'));
	mh.demographics.fatherState 		= request.POST.get('d_dad_state');
	mh.demographics.motherState 		= request.POST.get('d_mom_state');

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
	mh.education.collegeYears			= request.POST.get('collegeYears')
	mh.education.tradeSch 				= truePythonBool(request.POST.get('tradeSch'))
	mh.education.military 				= truePythonBool(request.POST.get('military'))
	mh.education.FriendshipsKto6 		= request.POST.get('m_FriendshipsKto6')
	mh.education.Friendships7to9 		= request.POST.get('m_Friendships7to9')
	mh.education.Friendships10to12		= request.POST.get('m_Friendships10to12')
	mh.education.tradeSchool 			= request.POST.get('m_tradeSchool')
	mh.education.tradeAreaStudy 		= request.POST.get('m_tradeAreaStudy')
	mh.education.militaryBranch 		= request.POST.get('m_militaryBranch')
	mh.education.militaryRank 			= request.POST.get('m_militaryRank')
	mh.education.militaryYears 			= request.POST.get('m_militaryYears')
	mh.education.honorableDischarge 	= truePythonBool(request.POST.get('m_honorableDischarge'))
	mh.education.collegeDegree 			= request.POST.get('m_collegeDegree')
	mh.education.collegeMajor 			= request.POST.get('m_collegeMajor')
	mh.education.advanceDegree 			= truePythonBool(request.POST.get('m_advanceDegree'))	

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
	mh.legalHistory.lawsuitStress = truePythonBool(request.POST.get('m_lawsuitStress'))
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
	mh.isComplete = False
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
	mh.save()

def mhEdu_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= True
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False
	mh.save()

def mhBack_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= True
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False
	mh.save()

def mhStress_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= True
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False
	mh.save()

def mhFamily_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= True
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False
	mh.save()

def mhLegal_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= True
	mh.psychPriority 		= False
	mh.usePriority 			= False
	mh.save()

def mhPsych_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= True
	mh.usePriority 			= False
	mh.save()

def mhUse_priority(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= True
	mh.save()

def deprioritizeMH(mh):
	mh.demoPriority 		= False
	mh.educationPriority 	= False
	mh.backgroundPriority 	= False
	mh.stressPriority 		= False
	mh.familyPriority 		= False
	mh.legalPriority 		= False
	mh.psychPriority 		= False
	mh.usePriority 			= False
	mh.save()

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
	track = getTrack(request.user)

	result['tracking'] = track.state.state
	result['current_section'] = current_section
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
	result.append('viewForm')
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
	result.append('/asi_viewForm/')
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
	result.append(' ')
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
	result.append(asi.isComplete)
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
	result.append(asi.isComplete)
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
#Will place a priority flag on the specified URL
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
#Will set all priority booleans to False
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
#Returns a string containing the next URL to go to.
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
#Returns dictionary list of the CSS class for the specified button
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
		if a.client == client and a.isComplete == False:
			exist = True
			break
	return exist

def findIncompleteClientASI(client):
#Returns all incomplete ASI objects for the client
	asis = ASI.objects.all()
	result = None

	for a in asis:
		if a.client == client and a.isComplete == False:
			result = a
			break
	return result

def newASI(the_client):
#Creates all components of a ASI and sets default values
#Returns the new ASI object
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
#Returns a dictionary with either a new ASI or a incomplete ASI along with True bool if new and False if not
	result = {}

	if hasIncompleteASI(client) == False:
		result['isNew'] = True
		result['asi'] = newASI(client)

	else:
		result['isNew'] = False
		result['asi'] = findIncompleteClientASI(client)

	return result

def beginASI(request):
# function 1. Returns dictionary object with all the page content
# function 2. Collects all POST data and translates them
# function 3. Sets global ID and Opens A form in the session.
	result = {}
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	session = ClientSession.objects.get(id=session_id)
	client = session.client

	action = startASI(client)
	asi = action['asi']
	setGlobalID(asi.id, request.user)

	openForm('asi', asi, client)
	session.asi = asi
	session.hasASI = True
	session.save()

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

def getDrugTableIndex(m_val):
	m_val = str(m_val)
	index = 0

	if m_val != 'None' and m_val != 'Select' and m_val != '':
		if m_val=='0' or m_val=='1' or m_val=='2' or m_val=='3' or m_val=='4':
			index = int(m_val)
		elif m_val=='X':
			index = 6
		elif m_val == 'N':
			index = 7

	return index

def getASIDrugMajor(m_val):
	m_val = str(m_val)
	index = 0

	if m_val != 'None' and m_val != 'Select' and m_val != '':
		if m_val=='00' or m_val=='01'or m_val=='02'or m_val=='03'or m_val=='04'or m_val=='05'or m_val=='06'or m_val=='07'or m_val=='08'or m_val=='09':
			temp = m_val[1]
			index = int(temp) + 1
		else:
			index = int(m_val) - 1
	return index

def getLegalChargesIndex(m_val):
	m_val = str(m_val)
	index = 0

	if m_val != 'None' and m_val != 'Select' and m_val != '':
		if m_val=='18' or m_val=='19' or m_val=='20':
			index = int(m_val) - 3
		else:
			index = int(m_val) - 2

	return index

def getLegalFamilyIndex(m_val):
	m_val = str(m_val)
	index = 0

	if m_val == '1':
		index = 1
	elif m_val == '0':
		index = 2
	elif m_val == 'X':
		index = 3
	elif m_val == 'N':
		index = 4

	return index

def getASI_YNI(m_val):
	m_val = str(m_val)
	index = 0

	if m_val != 'None' and m_val != 'Select' and m_val != '':
		index = int(m_val) + 1

	return index

def decodeASIFields(numBoxes, field):
	field = str(field)
	items = []
	result = {}
	adjust = None
	pre = 'box'

	fieldLen = len(field)

	if fieldLen < numBoxes:
		adjust = numBoxes - fieldLen
		lastIndex = fieldLen - 1

		if fieldLen == 1 and str(field[lastIndex]) == 'N':
			for a in range(adjust):
				items.append('X')
		else:
			for a in range(adjust):
				items.append('0')

	for f in field:
		items.append(f)

	for i in range(numBoxes):
		num = i + 1
		name = pre + str(num)
		result[name] = items[i]

	return result

def fetchSPchecks(val):
	result = {}
	val = str(val)
	check = "/static/images/check_o.png"
	nope = '/static/images/nope.png'

	if val == '0':
		result['q0'] = check
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '1':
		result['q0'] = nope
		result['q1'] = check
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '2':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = check
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '3':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = check
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '4':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = check
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '5':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = check
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '6':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = check
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = nope
	elif val == '7':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = check
		result['q8'] = nope
		result['q9'] = nope
	elif val == '8':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = check
		result['q9'] = nope
	elif val == '9':
		result['q0'] = nope
		result['q1'] = nope
		result['q2'] = nope
		result['q3'] = nope
		result['q4'] = nope
		result['q5'] = nope
		result['q6'] = nope
		result['q7'] = nope
		result['q8'] = nope
		result['q9'] = check
	return result

def decodeASIdate(date):
	result = {}
	date = str(date)
	result['box1'] = date[5]
	result['box2'] = date[6]
	result['box3'] = date[8]
	result['box4'] = date[9]
	result['box5'] = date[2]
	result['box6'] = date[3]
	return result

def decodeASITime(time):
	time = str(time)
	result = {}
	result['box1'] = time[0]
	result['box2'] = time[1]
	result['box3'] = time[3]
	result['box4'] = time[4]
	return result

def decodeASIBool(val):
	result = 0
	if val == True:
		result = 1
	return result

def snagAsiAdmin(asi):
	result = {}
	g10 = '2'
	if asi.client.isMale == True:
		g10 = '1'

	result['g1'] 	= decodeASIFields(4, asi.admin.g1)
	result['g2'] 	= decodeASIFields(4, asi.admin.g2)
	result['g3'] 	= decodeASIFields(3, asi.admin.g3)
	result['g4'] 	= decodeASIdate(asi.admin.g4)
	result['g5'] 	= decodeASIdate(asi.date_of_assessment)
	result['g6'] 	= decodeASITime(asi.startTime)
	result['g7'] 	= decodeASITime(asi.endTime)
	result['g8'] 	= decodeASIFields(1, asi.admin.g8)
	result['g9'] 	= decodeASIFields(1, asi.admin.g9)
	result['g10'] 	= g10
	result['g11'] 	= decodeASIFields(2, asi.admin.g11)
	result['g12'] 	= decodeASIFields(1,asi.admin.g12)
	return result

def snagASIgeneral(asi):
	result 				= {}
	result['g13'] 		= decodeASIFields(3, asi.general.g13)
	result['g14yrs'] 	= decodeASIFields(2, asi.general.g14yrs)
	result['g14mos'] 	= decodeASIFields(2, asi.general.g14mos)
	result['g15'] 		= decodeASIBool(asi.general.g15)
	result['g16'] 		= decodeASIdate(asi.client.dob)
	result['g16mth'] 	= decodeASIFields(2, asi.general.g16mth)
	result['g16day'] 	= decodeASIFields(2, asi.general.g16day)
	result['g16year'] 	= decodeASIFields(2, asi.general.g16year)
	result['g20'] 		= decodeASIFields(2, asi.general.g20)

	result['g21'] 		= decodeASIFields(3, asi.general.g21)
	result['g22'] 		= decodeASIFields(3, asi.general.g22)
	result['g23'] 		= decodeASIFields(2, asi.general.g23)
	result['g24'] 		= decodeASIFields(3, asi.general.g24)
	result['g25'] 		= decodeASIFields(2, asi.general.g25)
	result['g26'] 		= decodeASIFields(3, asi.general.g26)
	result['g27'] 		= decodeASIFields(3, asi.general.g27)
	result['g28'] 		= decodeASIFields(3, asi.general.g28)

	result['medical'] 	= fetchSPchecks(asi.general.medical)
	result['employ'] 	= fetchSPchecks(asi.general.employ)
	result['alcohol'] 	= fetchSPchecks(asi.general.alcohol)
	result['drug'] 		= fetchSPchecks(asi.general.drug)
	result['legal'] 	= fetchSPchecks(asi.general.legal)
	result['family'] 	= fetchSPchecks(asi.general.family)
	result['psych'] 	= fetchSPchecks(asi.general.psych)
	return result

def snagASImedical(asi):
	result 				= {}
	result['m1'] 		= decodeASIFields(2, asi.medical.m1)
	result['m2yrs'] 	= decodeASIFields(2, asi.medical.m2yrs)
	result['m2mth'] 	= decodeASIFields(2, asi.medical.m2mth)
	result['m6'] 		= decodeASIFields(2, asi.medical.m6)
	result['comments'] 	= splitFormLines(2, 90, str(asi.medical.comments))
	return result

def snagASIemployment(asi):
	result 				= {}
	result['e1yrs'] 	= decodeASIFields(2, asi.employment.e1yrs)
	result['e1mth'] 	= decodeASIFields(2, asi.employment.e1mth)
	result['e2'] 		= decodeASIFields(2, asi.employment.e2)
	result['e6yrs'] 	= decodeASIFields(2, asi.employment.e6yrs)
	result['e6mth'] 	= decodeASIFields(2, asi.employment.e6mth)
	result['e11'] 		= decodeASIFields(2, asi.employment.e11)
	result['e12'] 		= decodeASIFields(4, asi.employment.e12)
	result['e13'] 		= decodeASIFields(4, asi.employment.e13)
	result['e14'] 		= decodeASIFields(4, asi.employment.e14)
	result['e15'] 		= decodeASIFields(4, asi.employment.e15)
	result['e16'] 		= decodeASIFields(4, asi.employment.e16)
	result['e17'] 		= decodeASIFields(4, asi.employment.e17)
	result['comments'] 	= splitFormLines(3, 90, str(asi.employment.comments))
	return result

def snagASIdrug(asi):
	result = {}
	result['d1Day'] = decodeASIFields(2, asi.drug1.d1Day)
	result['d1Year'] = decodeASIFields(2, asi.drug1.d1Year)
	result['d2Day'] = decodeASIFields(2, asi.drug1.d2Day)
	result['d2Year'] = decodeASIFields(2, asi.drug1.d2Year)
	result['d3Day'] = decodeASIFields(2, asi.drug1.d3Day)
	result['d3Year'] = decodeASIFields(2, asi.drug1.d3Year)
	result['d4Day'] = decodeASIFields(2, asi.drug1.d4Day)
	result['d4Year'] = decodeASIFields(2, asi.drug1.d4Year)
	result['d5Day'] = decodeASIFields(2, asi.drug1.d5Day)
	result['d5Year'] = decodeASIFields(2, asi.drug1.d5Year)
	result['d6Day'] = decodeASIFields(2, asi.drug1.d6Day)
	result['d6Year'] = decodeASIFields(2, asi.drug1.d6Year)
	result['d7Day'] = decodeASIFields(2, asi.drug1.d7Day)
	result['d7Year'] = decodeASIFields(2, asi.drug1.d7Year)
	result['d8Day'] = decodeASIFields(2, asi.drug1.d8Day)
	result['d8Year'] = decodeASIFields(2, asi.drug1.d8Year)
	result['d9Day'] = decodeASIFields(2, asi.drug1.d9Day)
	result['d9Year'] = decodeASIFields(2, asi.drug1.d9Year)
	result['d10Day'] = decodeASIFields(2, asi.drug1.d10Day)
	result['d10Year'] = decodeASIFields(2, asi.drug1.d10Year)
	result['d11Day'] = decodeASIFields(2, asi.drug1.d11Day)
	result['d11Year'] = decodeASIFields(2, asi.drug1.d11Year)
	result['d12Day'] = decodeASIFields(2, asi.drug1.d12Day)
	result['d12Year'] = decodeASIFields(2, asi.drug1.d12Year)
	result['d14'] = decodeASIFields(2, asi.drug1.d14)
	result['d15'] = decodeASIFields(2, asi.drug1.d15)
	result['d16'] = decodeASIFields(2, asi.drug1.d16)
	result['d17'] = decodeASIFields(2, asi.drug1.d17)
	result['d18'] = decodeASIFields(2, asi.drug1.d18)
	result['d19'] = decodeASIFields(2, asi.drug1.d19)
	result['d20'] = decodeASIFields(2, asi.drug1.d20)
	result['d21'] = decodeASIFields(2, asi.drug1.d21)
	result['d22'] = decodeASIFields(2, asi.drug1.d22)
	result['d23'] = decodeASIFields(2, asi.drug1.d23)
	result['d24'] = decodeASIFields(2, asi.drug1.d24)
	result['d25'] = decodeASIFields(2, asi.drug1.d25)
	result['d26'] = decodeASIFields(2, asi.drug1.d26)
	result['d27'] = decodeASIFields(2, asi.drug1.d27)
	result['d28'] = decodeASIFields(2, asi.drug1.d28)
	result['d29'] = decodeASIFields(2, asi.drug1.d29)
	result['comments'] 	= splitFormLines(11, 90, str(asi.drug1.comments))
	return result

def snagASIlegal(asi):
	result = {}
	result['l3'] = decodeASIFields(2, asi.legal.l3)
	result['l4'] = decodeASIFields(2, asi.legal.l4)
	result['l5'] = decodeASIFields(2, asi.legal.l5)
	result['l6'] = decodeASIFields(2, asi.legal.l6)
	result['l7'] = decodeASIFields(2, asi.legal.l7)
	result['l8'] = decodeASIFields(2, asi.legal.l8)
	result['l9'] = decodeASIFields(2, asi.legal.l9)
	result['l10'] = decodeASIFields(2, asi.legal.l10)
	result['l11'] = decodeASIFields(2, asi.legal.l11)
	result['l12'] = decodeASIFields(2, asi.legal.l12)
	result['l13'] = decodeASIFields(2, asi.legal.l13)
	result['l14'] = decodeASIFields(2, asi.legal.l14)
	result['l15'] = decodeASIFields(2, asi.legal.l15)
	result['l16'] = decodeASIFields(2, asi.legal.l16)
	result['l17'] = decodeASIFields(2, asi.legal.l17)
	result['l18'] = decodeASIFields(2, asi.legal.l18)
	result['l19'] = decodeASIFields(2, asi.legal.l19)
	result['l20'] = decodeASIFields(2, asi.legal.l20)
	result['l21'] = decodeASIFields(2, asi.legal.l21)
	result['l22'] = decodeASIFields(2, asi.legal.l22)
	result['l23'] = decodeASIFields(2, asi.legal.l23)
	result['l25'] = decodeASIFields(2, asi.legal.l25)
	result['l26'] = decodeASIFields(2, asi.legal.l26)
	result['l27'] = decodeASIFields(2, asi.legal.l27)
	result['comments'] 	= splitFormLines(5, 90, str(asi.legal.comments))
	return result

def snagASIsocial(asi):
	result = {}
	result['f2yrs'] = decodeASIFields(2, asi.social1.f2yrs)
	result['f2mth'] = decodeASIFields(2, asi.social1.f2mth)
	result['f5yrs'] = decodeASIFields(2, asi.social1.f5yrs)
	result['f5mth'] = decodeASIFields(2, asi.social1.f5mth)
	result['f30'] = decodeASIFields(2, asi.social1.f30)
	result['f31'] = decodeASIFields(2, asi.social1.f31)
	result['comments'] = superSplit(20, 11, 85, 4, str(asi.social2.comments))
	return result

def snagASIpsych(asi):
	result = {}
	result['p1'] = decodeASIFields(2, asi.psych.p1)
	result['p2'] = decodeASIFields(2, asi.psych.p2)
	result['p12'] = decodeASIFields(2, asi.psych.p12)
	result['comments'] 	= splitFormLines(12, 90, str(asi.psych.comments))
	return result

def fetchASIViewItems(asi):
	result = {}
	result['admin'] 	= snagAsiAdmin(asi)
	result['general'] 	= snagASIgeneral(asi)
	result['medical'] 	= snagASImedical(asi)
	result['employ'] 	= snagASIemployment(asi)
	result['drug'] 		= snagASIdrug(asi)
	result['legal'] 	= snagASIlegal(asi)
	result['social'] 	= snagASIsocial(asi)
	result['psych'] 	= snagASIpsych(asi)
	return result

def grabAsiAdminFields(asi):
	# Returns a dictionary List of ASI.admin fields
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
	# Returns a dictionary List of ASI.general fields
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
	# Returns a dictionary List of ASI.medical fields
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
	# Returns a dictionary List of ASI.employment fields
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
	# Returns a dictionary List of ASI.drug fields
	result = {}
	d1Route = getDrugTableIndex(asi.drug1.d1Route)
	d2Route = getDrugTableIndex(asi.drug1.d2Route)
	d3Route = getDrugTableIndex(asi.drug1.d3Route)
	d4Route = getDrugTableIndex(asi.drug1.d4Route)
	d5Route = getDrugTableIndex(asi.drug1.d5Route)
	d6Route = getDrugTableIndex(asi.drug1.d6Route)
	d7Route = getDrugTableIndex(asi.drug1.d7Route)
	d8Route = getDrugTableIndex(asi.drug1.d8Route)
	d9Route = getDrugTableIndex(asi.drug1.d9Route)
	d10Route = getDrugTableIndex(asi.drug1.d10Route)
	d11Route = getDrugTableIndex(asi.drug1.d11Route)
	d12Route = getDrugTableIndex(asi.drug1.d12Route)

	d13 = getDrugTableIndex(asi.drug1.d13)
	d14 = getASIDrugMajor(asi.drug1.d14)
	d28 = getPatientIndex(asi.drug1.d28)
	d29 = getPatientIndex(asi.drug1.d29)
	d30 = getPatientIndex(asi.drug1.d30)
	d31 = getPatientIndex(asi.drug1.d31)
	d32 = getInterviewerIndex(asi.drug1.d32)
	d33 = getInterviewerIndex(asi.drug1.d33)

	result['d1Day'] = asi.drug1.d1Day
	result['d1Year'] = asi.drug1.d1Year
	result['d1Route'] = d1Route

	result['d2Day'] = asi.drug1.d2Day
	result['d2Year'] = asi.drug1.d2Year
	result['d2Route'] = d2Route

	result['d3Day'] = asi.drug1.d3Day
	result['d3Year'] = asi.drug1.d3Year
	result['d3Route'] = d3Route

	result['d4Day'] = asi.drug1.d4Day
	result['d4Year'] = asi.drug1.d4Year
	result['d4Route'] = d4Route

	result['d5Day'] = asi.drug1.d5Day
	result['d5Year'] = asi.drug1.d5Year
	result['d5Route'] = d5Route

	result['d6Day'] = asi.drug1.d6Day
	result['d6Year'] = asi.drug1.d6Year
	result['d6Route'] = d6Route

	result['d7Day'] = asi.drug1.d7Day
	result['d7Year'] = asi.drug1.d7Year
	result['d7Route'] = d7Route

	result['d8Day'] = asi.drug1.d8Day
	result['d8Year'] = asi.drug1.d8Year
	result['d8Route'] = d8Route

	result['d9Day'] = asi.drug1.d9Day
	result['d9Year'] = asi.drug1.d9Year
	result['d9Route'] = d9Route

	result['d10Day'] = asi.drug1.d10Day
	result['d10Year'] = asi.drug1.d10Year
	result['d10Route'] = d10Route

	result['d11Day'] = asi.drug1.d11Day
	result['d11Year'] = asi.drug1.d11Year
	result['d11Route'] = d11Route

	result['d12Day'] = asi.drug1.d12Day
	result['d12Year'] = asi.drug1.d12Year
	result['d12Route'] = d12Route

	result['d13'] = d13
	result['d14'] = d14
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
	result['d28'] = d28
	result['d29'] = d29
	result['d30'] = d30
	result['d31'] = d31
	result['d32'] = d32
	result['d33'] = d33
	result['d34'] = asi.drug1.d34
	result['d35'] = asi.drug1.d35

	result['comments'] = asi.drug1.comments
	result['isComplete'] = asi.drug1Complete
	return result

def grabAsiLegalFields(asi):
	# Returns a dictionary List of ASI.legal fields
	result = {}

	l23 = getLegalChargesIndex(asi.legal.l23)
	l25 = getLegalChargesIndex(asi.legal.l25)
	l28 = getPatientIndex(asi.legal.l28)
	l29 = getPatientIndex(asi.legal.l29)
	l30 = getInterviewerIndex(asi.legal.l30)

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
	result['l23'] = l23
	result['l24'] = asi.legal.l24
	result['l25'] = l25
	result['l26'] = asi.legal.l26
	result['l27'] = asi.legal.l27
	result['l28'] = l28
	result['l29'] = l29
	result['l30'] = l30
	result['l31'] = asi.legal.l31
	result['l32'] = asi.legal.l32
	result['comments'] = asi.legal.comments
	result['isComplete'] = asi.legalComplete
	return result

def grabAsiFamilyFields(asi):
	# Returns a dictionary List of ASI.family fields
	result = {}
	result['h1a'] = getLegalFamilyIndex(asi.family.h1a)
	result['h1d'] = getLegalFamilyIndex(asi.family.h1d)
	result['h1p'] = getLegalFamilyIndex(asi.family.h1p)

	result['h2a'] = getLegalFamilyIndex(asi.family.h2a)
	result['h2d'] = getLegalFamilyIndex(asi.family.h2d)
	result['h2p'] = getLegalFamilyIndex(asi.family.h2p)

	result['h3a'] = getLegalFamilyIndex(asi.family.h3a)
	result['h3d'] = getLegalFamilyIndex(asi.family.h3d)
	result['h3p'] = getLegalFamilyIndex(asi.family.h3p)

	result['h4a'] = getLegalFamilyIndex(asi.family.h4a)
	result['h4d'] = getLegalFamilyIndex(asi.family.h4d)
	result['h4p'] = getLegalFamilyIndex(asi.family.h4p)

	result['h5a'] = getLegalFamilyIndex(asi.family.h5a)
	result['h5d'] = getLegalFamilyIndex(asi.family.h5d)
	result['h5p'] = getLegalFamilyIndex(asi.family.h5p)

	result['h6a'] = getLegalFamilyIndex(asi.family.h6a)
	result['h6d'] = getLegalFamilyIndex(asi.family.h6d)
	result['h6p'] = getLegalFamilyIndex(asi.family.h6p)

	result['h7a'] = getLegalFamilyIndex(asi.family.h7a)
	result['h7d'] = getLegalFamilyIndex(asi.family.h7d)
	result['h7p'] = getLegalFamilyIndex(asi.family.h7p)

	result['h8a'] = getLegalFamilyIndex(asi.family.h8a)
	result['h8d'] = getLegalFamilyIndex(asi.family.h8d)
	result['h8p'] = getLegalFamilyIndex(asi.family.h8p)

	result['h9a'] = getLegalFamilyIndex(asi.family.h9a)
	result['h9d'] = getLegalFamilyIndex(asi.family.h9d)
	result['h9p'] = getLegalFamilyIndex(asi.family.h9p)

	result['h10a'] = getLegalFamilyIndex(asi.family.h10a)
	result['h10d'] = getLegalFamilyIndex(asi.family.h10d)
	result['h10p'] = getLegalFamilyIndex(asi.family.h10p)

	result['h11a'] = getLegalFamilyIndex(asi.family.h11a)
	result['h11d'] = getLegalFamilyIndex(asi.family.h11d)
	result['h11p'] = getLegalFamilyIndex(asi.family.h11p)

	result['h12a'] = getLegalFamilyIndex(asi.family.h12a)
	result['h12d'] = getLegalFamilyIndex(asi.family.h12d)
	result['h12p'] = getLegalFamilyIndex(asi.family.h12p)
	result['isComplete'] = asi.familyComplete
	return result

def grabAsiSocial1Fields(asi):
	# Returns a dictionary List of ASI.social1 fields
	result = {}
	result['f1'] = asi.social1.f1
	result['f2yrs'] = asi.social1.f2yrs
	result['f2mth'] = asi.social1.f2mth
	result['f3'] = getASI_YNI(asi.social1.f3)
	result['f4'] = asi.social1.f4
	result['f5yrs'] = asi.social1.f5yrs
	result['f5mth'] = asi.social1.f5mth
	result['f6'] = getASI_YNI(asi.social1.f6)
	result['f7'] = asi.social1.f7
	result['f8'] = asi.social1.f8
	result['f9'] = asi.social1.f9
	result['f10'] = getASI_YNI(asi.social1.f10)
	result['f11'] = asi.social1.f11
	result['f30'] = asi.social1.f30
	result['f31'] = asi.social1.f31
	result['f32'] = getPatientIndex(asi.social1.f32)
	result['f33'] = getPatientIndex(asi.social1.f33)
	result['f34'] = getPatientIndex(asi.social1.f34)
	result['f35'] = getPatientIndex(asi.social1.f35)
	result['f36'] = getInterviewerIndex(asi.social1.f36)
	result['f37'] = asi.social1.f37
	result['f38'] = asi.social1.f38
	result['isComplete'] = asi.social1Complete
	return result

def grabAsiSocial2Fields(asi):
	# Returns a dictionary List of ASI.social2 fields
	result = {}
	result['f12'] = getLegalFamilyIndex(asi.social2.f12)
	result['f13'] = getLegalFamilyIndex(asi.social2.f13)
	result['f14'] = getLegalFamilyIndex(asi.social2.f14)
	result['f16'] = getLegalFamilyIndex(asi.social2.f16)
	result['f17'] = getLegalFamilyIndex(asi.social2.f17)

	result['f18d'] = getLegalFamilyIndex(asi.social2.f18d)
	result['f18y'] = getLegalFamilyIndex(asi.social2.f18y)
	result['f19d'] = getLegalFamilyIndex(asi.social2.f19d)
	result['f19y'] = getLegalFamilyIndex(asi.social2.f19y)
	result['f20d'] = getLegalFamilyIndex(asi.social2.f20d)
	result['f20y'] = getLegalFamilyIndex(asi.social2.f20y)
	result['f21d'] = getLegalFamilyIndex(asi.social2.f21d)
	result['f21y'] = getLegalFamilyIndex(asi.social2.f21y)
	result['f22d'] = getLegalFamilyIndex(asi.social2.f22d)
	result['f22y'] = getLegalFamilyIndex(asi.social2.f22y)
	result['f23d'] = getLegalFamilyIndex(asi.social2.f23d)
	result['f23y'] = getLegalFamilyIndex(asi.social2.f23y)
	result['f24d'] = getLegalFamilyIndex(asi.social2.f24d)
	result['f24y'] = getLegalFamilyIndex(asi.social2.f24y)
	result['f25d'] = getLegalFamilyIndex(asi.social2.f25d)
	result['f25y'] = getLegalFamilyIndex(asi.social2.f25y)
	result['f26d'] = getLegalFamilyIndex(asi.social2.f26d)
	result['f26y'] = getLegalFamilyIndex(asi.social2.f26y)
	
	result['f27d'] = asi.social2.f27d
	result['f27y'] = asi.social2.f27y
	result['f28d'] = asi.social2.f28d
	result['f28y'] = asi.social2.f28y
	result['f29d'] = asi.social2.f29d
	result['f29y'] = asi.social2.f29y

	result['comments'] = asi.social2.comments
	result['isComplete'] = asi.social2Complete
	return result

def grabAsiPsychFields(asi):
	# Returns a dictionary List of ASI.psych fields
	result = {}
	result['p1'] = asi.psych.p1
	result['p2'] = asi.psych.p2
	result['p3'] = asi.psych.p3

	result['p4d'] = getLegalFamilyIndex(asi.psych.p4d)
	result['p5d'] = getLegalFamilyIndex(asi.psych.p5d)
	result['p6d'] = getLegalFamilyIndex(asi.psych.p6d)
	result['p7d'] = getLegalFamilyIndex(asi.psych.p7d)
	result['p8d'] = getLegalFamilyIndex(asi.psych.p8d)
	result['p9d'] = getLegalFamilyIndex(asi.psych.p9d)
	result['p10d'] = getLegalFamilyIndex(asi.psych.p10d)
	result['p11d'] = getLegalFamilyIndex(asi.psych.p11d)

	result['p4y'] = getLegalFamilyIndex(asi.psych.p4y)
	result['p5y'] = getLegalFamilyIndex(asi.psych.p5y)
	result['p6y'] = getLegalFamilyIndex(asi.psych.p6y)
	result['p7y'] = getLegalFamilyIndex(asi.psych.p7y)
	result['p8y'] = getLegalFamilyIndex(asi.psych.p8y)
	result['p9y'] = getLegalFamilyIndex(asi.psych.p9y)
	result['p10y'] = getLegalFamilyIndex(asi.psych.p10y)
	result['p11y'] = getLegalFamilyIndex(asi.psych.p11y)

	result['p12'] = asi.psych.p12
	result['p13'] = getPatientIndex(asi.psych.p13)
	result['p14'] = getPatientIndex(asi.psych.p14)
	result['p15'] = asi.psych.p15
	result['p16'] = asi.psych.p16
	result['p17'] = asi.psych.p17
	result['p18'] = asi.psych.p18
	result['p19'] = asi.psych.p19
	result['p20'] = asi.psych.p20
	result['p21'] = getInterviewerIndex(asi.psych.p21)
	result['p22'] = asi.psych.p22
	result['p23'] = asi.psych.p23
	result['comments'] = asi.psych.comments
	result['isComplete'] = asi.psychComplete
	return result

def grabASIViewFields(asi):
	result = {}
	##Return all ASI fields and Image Locations where applicable
	admin 		= grabAsiAdminFields(asi)
	general 	= grabAsiGeneralFields(asi)
	medical 	= grabAsiGeneralFields(asi)
	employment 	= grabAsiGeneralFields(asi)
	drug 		= grabAsiGeneralFields(asi)
	legal 		= grabAsiGeneralFields(asi)
	family 		= grabAsiGeneralFields(asi)
	social1 	= grabAsiGeneralFields(asi)
	social2 	= grabAsiGeneralFields(asi)
	psych 		= grabAsiGeneralFields(asi)
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
	elif section == '/asi_viewForm/':
		result = grabASIViewFields(asi)

	return result

def processASIbool(val):
	result = False
	if str(val) == '1':
		result = True
	return result

def saveASIadmin(request, asi):
	g4 = process_jq_date(request.POST.get('g4'))
	asi.admin.g1 = request.POST.get('g1')
	asi.admin.g2 = request.POST.get('g2')
	asi.admin.g3 = request.POST.get('g3')
	asi.admin.g4 = g4
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
	asi.psych.comments = request.POST.get('comments')

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
	asi.legalPriority = False
	asi.familyPriority = False
	asi.social1Priority = False
	asi.social2Priority = False
	asi.psychPriority = False
	asi.isComplete = False
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
		if clientEqual(client, d.client) == True:
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

def getDischarge(client):
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
		result['discharge'] = getDischarge(client)
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
	discharge.isOpen 			= False
	discharge.isComplete 		= True
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

	session = ClientSession.objects.get(id=session_id)
	client = session.client

	action = startDischarge(client)
	d = action['discharge']
	setGlobalSession(session.id, request.user)

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
	session_id = request.POST.get('session_id')
	d_id = request.POST.get('d_id')
	session = ClientSession.objects.get(id=session_id)
	discharge = Discharge.objects.get(id=d_id)
	saveDischarge(request, discharge)
	session.client.isDischarged = True
	session.client.save()
	endSession(session, True)




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
		if clientEqual(client, u.client) == True:
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

def hasUtPaid(client):
	hasPaid = False
	p_list = UtPaid.objects.all()

	for p in p_list:
		if clientEqual(client, p.client) == True:
			hasPaid = True
			break
	return hasPaid

def getUtPaid(client):
	result = None
	p_list = UtPaid.objects.all()

	for p in p_list:
		if clientEqual(client, p.client) == True:
			result = p
			break
	return result

def deleteUT(ut):
	paid = getUtPaid(ut.client)
	paid.delete()
	ut.delete()

def newUT(client):
	date = datetime.now()
	date = date.date()
	ut = UrineResults(client=client, date_of_assessment=date)
	ut.save()
	return ut

def startUT(client):
	result = None

	if hasIncompleteUT(client) == True:
		result = getClientIncompleteUt(client)
	else:
		result = newUT(client)

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
	ut.date_of_assessment = process_jq_date(request.POST.get('m_date'))
	ut.drug1 = truePythonBool(request.POST.get('m_ut1'))
	ut.drug2 = truePythonBool(request.POST.get('m_ut2'))
	ut.drug3 = truePythonBool(request.POST.get('m_ut3'))
	ut.drug4 = truePythonBool(request.POST.get('m_ut4'))
	ut.drug5 = truePythonBool(request.POST.get('m_ut5'))
	ut.drug6 = truePythonBool(request.POST.get('m_ut6'))
	ut.drug7 = truePythonBool(request.POST.get('m_ut7'))
	ut.drug8 = truePythonBool(request.POST.get('m_ut8'))
	ut.drug9 = truePythonBool(request.POST.get('m_ut9'))
	ut.drug10 = truePythonBool(request.POST.get('m_ut10'))
	ut.drug11 = truePythonBool(request.POST.get('m_ut11'))
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

def getUtData(ut):
	result = []

	if ut.drug1 == True:
		result.append('Cannibus')
	if ut.drug2 == True:
		result.append('Amphetamine')
	if ut.drug3 == True:
		result.append('Cocaine')
	if ut.drug4 == True:
		result.append('Opiate')
	if ut.drug5 == True:
		result.append('Benzodiazepine')
	if ut.drug6 == True:
		result.append('Barbiturates')
	if ut.drug7 == True:
		result.append('PCP')
	if ut.drug8 == True:
		result.append('OxyContin')
	if ut.drug9 == True:
		result.append('Methamphetamine')
	if ut.drug10 == True:
		result.append('Morphine')
	if ut.drug11 == True:
		result.append('Methadone')

	return result

def getUtViewImages(ut):
	images = {}
	images['drug1'] = getViewFormCheckImages(ut.drug1)
	images['drug2'] = getViewFormCheckImages(ut.drug2)
	images['drug3'] = getViewFormCheckImages(ut.drug3)
	images['drug4'] = getViewFormCheckImages(ut.drug4)
	images['drug5'] = getViewFormCheckImages(ut.drug5)
	images['drug6'] = getViewFormCheckImages(ut.drug6)
	images['drug7'] = getViewFormCheckImages(ut.drug7)
	images['drug8'] = getViewFormCheckImages(ut.drug8)
	images['drug9'] = getViewFormCheckImages(ut.drug9)
	images['drug10'] = getViewFormCheckImages(ut.drug10)
	images['drug11'] = getViewFormCheckImages(ut.drug11)
	return images


def beginUT(request):
	result = {}
	paid = None
	client_id = request.POST.get('client_id', '')
	session_id = request.POST.get('session_id', '')

	session = ClientSession.objects.get(id=session_id)
	client = session.client

	result['session'] = session

	s_type = getStype('ut')
	result['s_type'] = s_type

	if hasUtPaid(client) == True:
		paid = getUtPaid(client)
		setGlobalID(paid.id, request.user)
		result['paid'] = paid

		if session.hasUT == True:
			result['isNew'] = False
		else:
			date = datetime.now()
			ut = UrineResults(client=client, date_of_assessment=date.date())
			ut.save()
			session.ut = ut
			session.hasUT = True
			session.save()
			result['isNew'] = True

		setGlobalID(session.ut.id, request.user)
		result['ut'] = session.ut

		if paid.isPaid == True:
			result['url'] = 'counselor/forms/UrineTest/results.html'
		else:			
			result['url'] = 'counselor/forms/UrineTest/instructions.html'

	else:
		paid = UtPaid(client=client)
		paid.save()
		setGlobalID(paid.id, request.user)
		result['url'] = 'counselor/forms/UrineTest/instructions.html'

	return result

def processUtData(request):
	result = {}

	session_id = request.POST.get('session_id', '')
	ut_id = request.POST.get('ut_id', '')
	save_this = request.POST.get('save_this', '')

	session = ClientSession.objects.get(id=session_id)
	ut = UrineResults.objects.get(id=ut_id)
	fields = getUtFields(ut)
	json_data = json.dumps(fields)
	result['date'] = ut.date_of_assessment

	if save_this == 'true':
		saveUT(request, ut)
		# finishUT(ut)

	result['session'] = session
	result['ut'] = ut
	result['fields'] = fields
	result['json_data'] = json_data
	result['title'] = "Simeon Academy | Urine Test Analysis"

	return result

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
################################################################ END URINE ################################################################
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

###########################################################################################################################################
#*****************************************************************************************************************************************#
#--------------------------------------------------------------- BILLING -----------------------------------------------------------------#
#*****************************************************************************************************************************************#
###########################################################################################################################################

def getStype(ftype):
	ftype = str(ftype)
	result = None
	if ftype == 'am':
		result = SType.objects.get(id=1)
	elif ftype == 'mh':
		result = SType.objects.get(id=2)
	elif ftype == 'ut':
		result = SType.objects.get(id=3)
	elif ftype == 'sap':
		result = SType.objects.get(id=4)
	elif ftype == 'asi':
		result = SType.objects.get(id=5)
	return result

def getInvoices(client):
	result = []
	invoices = Invoice.objects.all()
	for i in invoice:
		if clientEqual(i.client, client):
			result.append(i)
	return result

def chooseToBill(form_type, form, session):
	if form.initialized == False:
		processSession(form_type, session)
		form.initialized = True
		form.save()

def resetInvoice(invoice):
	invoice.date = ''
	invoice.service1 = ''
	invoice.service2 = ''
	invoice.service3 = ''
	invoice.service4 = ''
	invoice.service5 = ''
	invoice.service6 = ''
	invoice.total1 = 0
	invoice.total2 = 0
	invoice.total3 = 0
	invoice.total4 = 0
	invoice.total5 = 0
	invoice.total6 = 0
	invoice.grandTotal = 0
	invoice.isPaid = False
	invoice.partialPaid = False
	invoice.save()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
############################################################## END BILLING ################################################################
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


############################################################################################
	              ## CLIENT OPTION FUNCTIONS
############################################################################################

def orderedASI(order, client):
	result = []
	order = str(order)
	asi = None

	if order == 'low':
		asi = ASI.objects.all().order_by('date_of_assessment')
	elif order == 'high':
		asi = ASI.objects.all().order_by('-date_of_assessment')

	for a in asi:
		if clientEqual(client, a.client):
			data = {}
			data['form_type'] = 'asi'
			data['form'] = a
			data['name'] = 'Addiction Severity Index'
			result.append(data)

	return result

def orderedAM(order, client):
	result = []
	order = str(order)
	am = None

	if order == 'low':
		am = AngerManagement.objects.all().order_by('date_of_assessment')
	elif order == 'high':
		am = AngerManagement.objects.all().order_by('-date_of_assessment')

	for a in am:
		if clientEqual(client, a.client):
			data = {}
			data['form_type'] = 'am'
			data['form'] = a
			data['name'] = 'Anger Management'
			result.append(data)

	return result

def orderedSAP(order, client):
	result = []
	order = str(order)
	sap = None

	if order == 'low':
		sap = SAP.objects.all().order_by('date_of_assessment')
	elif order == 'high':
		sap = SAP.objects.all().order_by('-date_of_assessment')

	for s in sap:
		if clientEqual(client, s.client):
			data = {}
			data['form_type'] = 'sap'
			data['form'] = s
			data['name'] = 'S.A.P'
			result.append(data)

	return result

def orderedMH(order, client):
	result = []
	order = str(order)
	mh = None

	if order == 'low':
		mh = MentalHealth.objects.all().order_by('date_of_assessment')
	elif order == 'high':
		mh = MentalHealth.objects.all().order_by('-date_of_assessment')

	for m in mh:
		if clientEqual(client, m.client):
			data = {}
			data['form_type'] = 'mh'
			data['form'] = m
			data['name'] = 'Mental Health'
			result.append(data)

	return result

def orderedUT(order, client):
	result = []
	order = str(order)
	ut = None

	if order == 'low':
		ut = UrineResults.objects.all().order_by('date_of_assessment')
	elif order == 'high':
		ut = UrineResults.objects.all().order_by('-date_of_assessment')

	for u in ut:
		if clientEqual(client, u.client):
			data = {}
			data['form_type'] = 'ut'
			data['form'] = u
			data['name'] = 'Urine Analysis'
			result.append(data)

	return result

def formLowDateLow(client):
	result = []
	am 	= orderedAM('low', client)
	asi = orderedASI('low', client)
	mh 	= orderedMH('low', client)
	sap = orderedSAP('low', client)
	ut 	= orderedUT('low', client)
	for a in am:
		result.append(a)
	for ai in asi:
		result.append(ai)
	for m in mh:
		result.append(m)
	for s in sap:
		result.append(s)
	for u in ut:
		result.append(u)
	return result

def formLowDateHi(client):
	result = []
	am 	= orderedAM('high', client)
	asi = orderedASI('high', client)
	mh 	= orderedMH('high', client)
	sap = orderedSAP('high', client)
	ut 	= orderedUT('high', client)
	for a in am:
		result.append(a)
	for ai in asi:
		result.append(ai)
	for m in mh:
		result.append(m)
	for s in sap:
		result.append(s)
	for u in ut:
		result.append(u)
	return result

def formHiDateLow(client):
	result = []
	am 	= orderedAM('low', client)
	asi = orderedASI('low', client)
	mh 	= orderedMH('low', client)
	sap = orderedSAP('low', client)
	ut 	= orderedUT('low', client)	
	for u in ut:
		result.append(u)
	for s in sap:
		result.append(s)
	for m in mh:
		result.append(m)
	for ai in asi:
		result.append(ai)
	for a in am:
		result.append(a)
	return result

def formHiDateHi(client):
	result = []
	am 	= orderedAM('high', client)
	asi = orderedASI('high', client)
	mh 	= orderedMH('high', client)
	sap = orderedSAP('high', client)
	ut 	= orderedUT('high', client)	
	for u in ut:
		result.append(u)
	for s in sap:
		result.append(s)
	for m in mh:
		result.append(m)
	for ai in asi:
		result.append(ai)
	for a in am:
		result.append(a)
	return result

def getOrderedHistory(f_order, d_order, client):
	result = []
	f_order = str(f_order)
	d_order = str(d_order)
	
	if f_order == 'low' and d_order == 'high':
		result = formLowDateHi(client)
	elif f_order == 'high' and d_order == 'low':
		result = formHiDateLow(client)
	elif f_order == 'high' and d_order == 'high':
		result = formHiDateHi(client)
	else:
		result = formLowDateLow(client)		
	return result


def processClientHistory(request):
	result = {}
	fields = {}
	session_id = request.POST.get('session_id')
	session = ClientSession.objects.get(id=session_id)
	f_order = request.POST.get('forder')
	d_order = request.POST.get('dorder')
	client = session.client

	h_list = getOrderedHistory(f_order, d_order, client)

	fields['f_order'] = f_order
	fields['d_order'] = d_order
	json_data = json.dumps(fields)

	result['json_data'] = json_data
	result['h_list'] 	= h_list	
	result['session'] 	= session
	result['title']		= 'Simeon Academy | Client History'

 	return result




############################################################################################
	              ## END CLIENT OPTION FUNCTIONS
############################################################################################
def userHasTrack(user):
	hasTrack = False
	tracks = TrackApp.objects.all()

	for t in tracks:
		if str(t.c_id) == str(user.id):
			hasTrack = True
			break

	return hasTrack

def getUserTrack(user):
	tracking = None

	tracks = TrackApp.objects.all()

	for t in tracks:
		if str(t.c_id) == str(user.id):
			tracking = t
			break

	return tracking

def getTrack(user):
	tracking = None

	if userHasTrack(user) == True:
		tracking = getUserTrack(user)
	else:
		m_counselor = ''
		m_counselor += str(user.first_name)
		m_counselor += ' '
		m_counselor += str(user.last_name)
		m_id = str(user.id)
		tracking = TrackApp(counselor=m_counselor, c_id=m_id)
		tracking.save()

		thePrint = PrintableForms(counselor=m_counselor)
		thePrint.save()
		tracking.printable = thePrint
		tracking.save()

	return tracking

def getAppAction(m_action):
	result = None
	m_action = str(m_action)

	if m_action == 'Admin':
		result = SolidState.objects.get(id=1)
	elif m_action == 'General':
		result = SolidState.objects.get(id=2)
	elif m_action == 'Session':
		result = SolidState.objects.get(id=3)
	elif m_action == 'Search':
		result = SolidState.objects.get(id=4)

	return result


def setGlobalID(the_id, user):
	track = getUserTrack(user)
	track.f_id = the_id
	track.save()

def getGlobalID(user):
	track = getUserTrack(user)
	return track.f_id

def setGlobalClientID(the_id, user):
	track = getUserTrack(user)
	track.client_id = the_id
	track.save()

def getGlobalClientID(user):
	track = getUserTrack(user)
	return track.client_id

def setGlobalSession(the_id, user):
	track = getUserTrack(user)
	track.s_id = the_id
	track.save()

def getSessionID(user):
	track = getUserTrack(user)
	return track.s_id

def setAppTrack(m_action, user):
	track = getUserTrack(user)
	loc = getAppAction(m_action)
	track.state = loc
	track.save()

def quickTrack(m_action, track):
	loc = getAppAction(m_action)
	track.state = loc
	track.save()


def getAppTrack(user):
	track = getUserTrack(user)
	return track.state

def decodeCharfield(text):
	temp = ''
	result = []

	for t in text:
		if str(t) != '~':
			temp += t
		else:
			result.append(temp)
			temp = ''

	result.append(temp)
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

	elif form_type == 'discharge':
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

def fetchPrintFields(form_type, form):
	result = {}
	form_type = str(form_type)

	if form_type == 'am':
		result = None
	elif form_type == 'mh':
		result = None
	elif form_type == 'ut':
		result = None
	elif form_type == 'sap':
		result = grabSapViewFields(form)
	elif form_type == 'asi':
		result = None
	return result

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
		saveUT(request, form)
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
	elif form_type == 'ut':
		deleteUT(form)
	elif form_type == 'discharge':
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

def getViewFormCheckImages(torf):
	image = None
	check 	= "/static/images/checked_checkbox.png"
	uncheck = "/static/images/unchecked_checkbox.png"

	if torf == True:
		image = check
	else:
		image = uncheck
	return image

def fetchCurrentFile(form_type, client):
	result = None
	form_type = str(form_type)

	if form_type == 'am':
		result = None
	elif form_type == 'mh':
		result = None
	elif form_type == 'ut':
		result = None
	elif form_type == 'sap':
		result = getClientOpenSap(client)
	elif form_type == 'asi':
		result = None

	return result

def fetchAllClientHistory(session):
	result = []
	sessions = ClientSession.objects.all().order_by('startTime');
	counter = 100
	pre = 'hist'
	match = 0

	for s in sessions:
		if clientEqual(session.client, s.client):
			form = getAllAmForms(session)
			if form != None:
				data = {}
				data['session'] = s
				data['form_type'] = 'am'
				data['name'] = 'Anger Management Assessment'
				data['form'] = s.am
				data['id'] = pre + str(counter)
				counter += 1
				result.append(data)

		if clientEqual(session.client, s.client):
			form = getAllMhForms(session)
			if form != None:
				data = {}
				data['session'] = s
				data['form_type'] = 'mh'
				data['name'] = 'Mental Health Profile'
				data['form'] = s.mh
				data['id'] = pre + str(counter)
				counter += 1
				result.append(data)

		if clientEqual(session.client, s.client):
			form = getAllUtForms(session)
			if form != None:
				data = {}
				data['session'] = s
				data['form_type'] = 'ut'
				data['name'] = 'Urine Analysis'
				data['form'] = s.ut
				data['id'] = pre + str(counter)
				counter += 1
				result.append(data)

		if clientEqual(session.client, s.client):
			form = getAllAsiForms(session)
			if form != None:
				data = {}
				data['session'] = s
				data['form_type'] = 'asi'
				data['name'] = 'Addiction Severity Index'
				data['form'] = s.asi
				data['id'] = pre + str(counter)
				counter += 1
				result.append(data)

		if clientEqual(session.client, s.client):
			form = getAllSapForms(session)
			if form != None:
				data = {}
				data['session'] = s
				data['form_type'] = 'sap'
				data['name'] = 'S.A.P Profile'
				data['form'] = s.sap
				data['id'] = pre + str(counter)
				counter += 1
				result.append(data)

	return result

def setPrintable(index, printable, his):
	if index == 0:
		printable.p1_id = his['session'].id
		printable.p1_type = his['form_type']
	elif index == 1:
		printable.p2_id = his['session'].id
		printable.p2_type = his['form_type']
	elif index == 2:
		printable.p3_id = his['session'].id
		printable.p3_type = his['form_type']
	elif index == 3:
		printable.p4_id = his['session'].id
		printable.p4_type = his['form_type']
	elif index == 4:
		printable.p5_id = his['session'].id
		printable.p5_type = his['form_type']
	printable.save()

def setClientHistory5(page, history, user):
	index = []
	forms = []
	count = 0
	matches = len(history)

	track = getUserTrack(user)
	printable = track.printable
	startIndex = (page * 5) - 5
	endIndex = page * 5

	for j in range(startIndex, endIndex):
		if j < matches:
			index.append(j)
		else:
			break

	for i in index:
		forms.append(history[i])

	for f in forms:
		setPrintable(count, printable, f)
		count += 1

	return forms

def calculateHistoryPages(matches):
	selList = []
	np = 0
	offset = matches % 5

	if offset > 0:
		np = 1

	if matches > 5:
		matches -= offset
		otherP = matches / 5
		np += otherP

	for i in range(np):
		num = i + 1
		selList.append(num)

	return selList

def fetchClientHistory(session, numberRequested):
	result = []
	sessions = ClientSession.objects.all()
	
	for s in sessions:
		if len(result) < numberRequested:
			if clientEqual(s.client, session.client):
				data = getAllAmForms(session)
				if data != None:
					result.append(data)

		if len(result) < numberRequested:
			if clientEqual(s.client, session.client):
				data = getAllMhForms(session)
				if data != None:
					result.append(data)

		if len(result) < numberRequested:
			if clientEqual(s.client, session.client):
				data = getAllUtForms(session)
				if data != None:
					result.append(data)

		if len(result) < numberRequested:
			if clientEqual(s.client, session.client):
				data = getAllAsiForms(session)
				if data != None:
					result.append(data)

		if len(result) < numberRequested:
			if clientEqual(s.client, session.client):
				data = getAllSapForms(session)
				if data != None:
					result.append(data)
	return result

def fetchUtPositive(session):
	result = None
	if session.hasUT == True:
		result = getUtData(session.ut)
	return result

def deprioritizeURL(form_type, form):
	f = str(form_type)
	if f == 'asi':
		deprioritizeASI(form)
	elif f == 'sap':
		deprioritizeSAP(form)
	elif f == 'am':
		deprioritizeAM(form)
	elif f == 'mh':
		deprioritizeMH(form)
	form.save()
























	
























