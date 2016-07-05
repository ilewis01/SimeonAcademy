from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
	user = models.OneToOneField(User)
	is_counselor = models.NullBooleanField(default=None)
	is_validated = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return self.user.username

class Global_ID(models.Model):
	name = models.CharField(max_length=20, default=None, blank=True, null=True)
	global_id = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.global_id)

class State(models.Model):
	state = models.CharField(max_length=2, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.state

class RefReason(models.Model):
	reason = models.CharField(max_length=50, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.reason

class TermReason(models.Model):
	reason = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.reason

class MaritalStatus(models.Model):
	status = models.CharField(max_length=9, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.status

class LivingSituation(models.Model):
	situation = models.CharField(max_length=20, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.situation

class EducationLevel(models.Model):
	level = models.CharField(max_length=35, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.level

class Drug(models.Model):
	drug = models.CharField(max_length=35, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.drug

class Client(models.Model):
	fname = models.CharField(max_length=20, default=None, blank=True, null=True)
	middleInit = models.CharField(max_length=1, default=None, blank=True, null=True)
	lname = models.CharField(max_length=20, default=None, blank=True, null=True)
	isMale = models.BooleanField(default=True, blank=True)
	street_no = models.CharField(max_length=10, default=None, blank=True, null=True)
	street_name = models.CharField(max_length=20, default=None, blank=True, null=True)
	apartment_no = models.CharField(max_length=5, default=None, blank=True, null=True)
	city = models.CharField(max_length=15, default=None, blank=True, null=True)
	state = models.ForeignKey(State, null=True, blank=True, default=None)
	zip_code = models.IntegerField(default=0)
	ss_num = models.CharField(max_length=11, default=None, blank=True, null=True)
	dob = models.DateField(default=None, blank=True, null=True)
	intake_date = models.DateField(default=None, blank=True, null=True)
	emer_contact_name = models.CharField(max_length=50, default=None, blank=True, null=True)
	reason_ref = models.ForeignKey(RefReason, null=True, blank=True, default=None)
	phone = models.CharField(max_length=14, default=None, blank=True, null=True)
	emer_phone = models.CharField(max_length=14, default=None, blank=True, null=True)
	email = models.EmailField(default=None, blank=True, null=True)
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)
	isDischarged = models.BooleanField(default=False, blank=True)
	probationOfficer = models.CharField(max_length=60, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.lname) + ", " + str(self.fname) + " " + str(self.dob)

class Discharge(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	discharge_date = models.DateField(default=None, blank=True, null=True)
	termReason = models.ForeignKey(TermReason, default=None, blank=True, null=True)
	diagnosis = models.CharField(max_length=100, default=None, blank=True, null=True)
	recommendations = models.CharField(max_length=250, default=None, blank=True, null=True)
	treatmentNotes = models.CharField(max_length=250, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Discharge: " + str(self.client)

class UrineResults(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	testDate = models.DateField(default=None, blank=True, null=True)
	drug1 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug2 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug3 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug4 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug5 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug6 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug7 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug8 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug9 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug10 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug11 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug12 = models.CharField(max_length=20, default=None, blank=True, null=True)

	isOpen = models.BooleanField(default=False, blank=True)
	isComplete = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "Urine Results: " + str(self.client)

##DEMOGRAPHIC SECTION OF THE SAP FORM------------------------------------------------------
class SapDemographics(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	date1 = models.DateField(default=None, blank=True, null=True)
	date2 = models.DateField(default=None, blank=True, null=True)
	date3 = models.DateField(default=None, blank=True, null=True)

	startTime1 = models.CharField(max_length=8, default=None, blank=True, null=True)
	startTime2 = models.CharField(max_length=8, default=None, blank=True, null=True)
	startTime3 = models.CharField(max_length=8, default=None, blank=True, null=True)

	problem = models.CharField(max_length=500, default=None, blank=True, null=True)
	health = models.CharField(max_length=500, default=None, blank=True, null=True)
	family = models.CharField(max_length=500, default=None, blank=True, null=True)
	psychoactive = models.CharField(max_length=500, default=None, blank=True, null=True)
	special = models.CharField(max_length=500, default=None, blank=True, null=True)
	psychological = models.CharField(max_length=250, default=None, blank=True, null=True)
	gambling = models.CharField(max_length=250, default=None, blank=True, null=True)
	abilities = models.CharField(max_length=250, default=None, blank=True, null=True)
	other = models.CharField(max_length=250, default=None, blank=True, null=True)
	source1 = models.CharField(max_length=50, default=None, blank=True, null=True)
	relationship1 = models.CharField(max_length=25, default=None, blank=True, null=True)
	source2 = models.CharField(max_length=50, default=None, blank=True, null=True)
	relationship2 = models.CharField(max_length=25, default=None, blank=True, null=True)

	#Checkboxes
	isChild = models.BooleanField(default=False, blank=True)
	isSenior = models.BooleanField(default=False, blank=True)
	isDual = models.BooleanField(default=False, blank=True)
	isOther = models.BooleanField(default=False, blank=True)
	isNone = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return str(self.clientID)

##PSYCHOACTIVE HISTORY OF SAP FORM---------------------------------------------------------
class SapPsychoactive(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)
	
	alcoholAge = models.IntegerField(default=0)
	alcoholFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	alcoholQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	alcoholLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	alcoholHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	amphAge = models.IntegerField(default=0)
	amphFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	amphQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	amphLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	amphHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	caffineAge = models.IntegerField(default=0)
	caffineFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	caffineQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	caffineLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	caffineHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	weedAge = models.IntegerField(default=0)
	weedFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	weedQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	weedLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	weedHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	cokeAge = models.IntegerField(default=0)
	cokeFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	cokeQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	cokeLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	cokeHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	hallAge = models.IntegerField(default=0)
	hallFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	hallQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	hallLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	hallHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	inhaleAge = models.IntegerField(default=0)
	inhaleFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	inhaleQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	inhaleLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	inhaleHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	smokeAge = models.IntegerField(default=0)
	smokeFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	smokeQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	smokeLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	smokeHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	opAge = models.IntegerField(default=0)
	opFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	opQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	opLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	opHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	pcpAge = models.IntegerField(default=0)
	pcpFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	pcpQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	pcpLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	pcpHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	sedAge = models.IntegerField(default=0)
	sedFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	sedQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	sedLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	sedHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	otherAge = models.IntegerField(default=0)
	otherFrequency = models.CharField(max_length=25, default=None, blank=True, null=True)
	otherQuantity = models.CharField(max_length=25, default=None, blank=True, null=True)
	otherLast = models.CharField(max_length=25, default=None, blank=True, null=True)
	otherHow = models.CharField(max_length=25, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

##COMPLETE IMPLEMENTATION OF THE SAP FORM-----------------------------------------------
class SAP(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	demographics = models.ForeignKey(SapDemographics, default=None, blank=True, null=True)
	psychoactive = models.ForeignKey(SapPsychoactive, default=None, blank=True, null=True)

	clinicalComplete = models.BooleanField(blank=True, default=False)
	socialComplete = models.BooleanField(blank=True, default=False)
	psychoComplete = models.BooleanField(blank=True, default=False)
	psycho2Complete = models.BooleanField(blank=True, default=False)
	specialComplete = models.BooleanField(blank=True, default=False)
	otherComplete = models.BooleanField(blank=True, default=False)
	sourcesComplete = models.BooleanField(blank=True, default=False)

	clinicPriority = models.BooleanField(blank=True, default=False)
	socialPriority = models.BooleanField(blank=True, default=False)
	psycho1Priority = models.BooleanField(blank=True, default=False)
	psycho2Priority = models.BooleanField(blank=True, default=False)
	spacialPriority = models.BooleanField(blank=True, default=False)
	otherPriority = models.BooleanField(blank=True, default=False)
	sourcesPriority = models.BooleanField(blank=True, default=False)

	isOpen = models.BooleanField(blank=True, default=False)
	SapComplete = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return "SAP: " + str(self.client.clientID)

##ANGER MANAGEMENT DEMOGRAPHIC------------------------------------------------------------
class AM_Demographic(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)
	
	maritalStatus = models.ForeignKey(MaritalStatus, default=None, blank=True, null=True)
	livingSituation = models.ForeignKey(LivingSituation, default=None, blank=True, null=True)
	own = models.BooleanField(default=False, blank=True)
	months_res = models.IntegerField(default=0)
	years_res = models.IntegerField(default=0)
	whoLivesWithClient = models.CharField(max_length=500, default=None, blank=True, null=True)
	
	num_children = models.IntegerField(default=0)
	other_dependants = models.IntegerField(default=0)
	
	education = models.ForeignKey(EducationLevel, default=None, blank=True, null=True)
	drop_out = models.BooleanField(default=False, blank=True)
	resasonDO = models.CharField(max_length=250, default=None, blank=True, null=True)
	
	employee = models.CharField(max_length=50, default=None, blank=True, null=True)
	job_title = models.CharField(max_length=25, default=None, blank=True, null=True)
	emp_address = models.CharField(max_length=100, default=None, blank=True, null=True)
	employed_months = models.IntegerField(default=0)
	employed_years = models.IntegerField(default=0)
	employer_phone = models.CharField(max_length=15, default=None, blank=True, null=True)
	
	health_problem = models.BooleanField(default=False, blank=True)
	medication = models.BooleanField(default=False, blank=True)
	whatMedicine = models.CharField(max_length=100, default=None, blank=True, null=True)
	health_exp = models.CharField(max_length=250, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Anger Management: " + str(self.client_id) + " Date: " + str(self.date_of_assessment)
		# return "Anger Management/Demographics: " + str(self.client)

##ANGER MANAGEMENT ALCOHOL AND DRUG HISTORY---------------------------------------------------------
class AM_DrugHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	firstDrinkAge = models.IntegerField(default=0)
	firstDrinkType = models.CharField(default=None, max_length=50, blank=True, null=True)	
	curUse = models.BooleanField(default=False, blank=True)
	useType = models.CharField(max_length=50, default=None, blank=True, null=True)
	amtPerWeek =  models.CharField(max_length=50, default=None, blank=True, null=True)
	useAmt = models.CharField(max_length=50, default=None, blank=True, null=True)
	everDrank = models.BooleanField(default=False, blank=True)
	monthsQuit = models.IntegerField(default=0)
	yearsQuit = models.IntegerField(default=0)
	reasonQuit = models.CharField(max_length=100, default=None, blank=True, null=True)
	DUI = models.BooleanField(blank=True, default=False)
	numDUI = models.IntegerField(default=0)
	BALevel = models.CharField(max_length=20, default=None, blank=True, null=True)
	drugTreatment = models.BooleanField(default=False, blank=True)
	treatmentPlace = models.CharField(max_length=50, default=None, blank=True, null=True)
	dateTreated = models.CharField(max_length=10, default=None, blank=True, null=True)
	finishedTreatment = models.BooleanField(default=False, blank=True)
	reasonNotFinishedTreatment = models.CharField(max_length=100, blank=True, null=True, default=None)
	isClean = models.BooleanField(default=True, blank=True)
	relapseTrigger = models.CharField(max_length=250, default=None, blank=True, null=True)
	drinkLastEpisode = models.BooleanField(default=False, blank=True)
	drinkRelationshipProblem = models.BooleanField(default=False, blank=True)
	needHelpDrugs = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT CHILDHOOD HISTORY----------------------------------------------------------------
class AM_ChildhoodHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	raisedBy = models.CharField(max_length=20, default=None, blank=True, null=True)
	momAlive = models.BooleanField(default=False, blank=True)
	dadAlive = models.BooleanField(default=False, blank=True)
	childTrama = models.BooleanField(default=False, blank=True)
	traumaExplain = models.CharField(max_length=100, default=None, blank=True, null=True)
	howLeftHome = models.CharField(max_length=100, default=None, blank=True, null=True)
	num_siblings = models.IntegerField(default=0)
	siblingsClose = models.BooleanField(default=False, blank=True)
	siblingsRelationshipExplain = models.CharField(max_length=250, default=None, blank=True, null=True)
	dadClose = models.BooleanField(default=False, blank=True)
	dadCloseExplain = models.CharField(max_length=250, default=None, blank=True, null=True)
	momClose = models.BooleanField(default=False, blank=True)
	momCloseExplain = models.CharField(max_length=250, default=None, blank=True, null=True)
	wasAbused = models.BooleanField(default=False, blank=True)
	abusedBy = models.CharField(max_length=20, default=None, blank=True, null=True)
	abuseImpact = models.CharField(max_length=250, default=None, blank=True, null=True)
	childAnger = models.BooleanField(default=False, blank=True)
	childAngerExplain = models.CharField(max_length=250, default=None, blank=True, null=True)
	otherChild = models.BooleanField(default=False, blank=True)
	otherChildExplain = models.CharField(max_length=250, default=None, blank=True, null=True)
	parentViolence = models.BooleanField(default=False, blank=True)
	parentViolenceExplain = models.CharField(max_length=250, default=None, blank=True, null=True)
	parentViolenceImpact = models.CharField(max_length=250, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT ANGER/VIOLENCE HISTORY----------------------------------------------------------------
class AM_AngerHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	recentIncidentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	recentVDate = models.CharField(blank=True, null=True, default=None, max_length=100)
	recentVlocation = models.CharField(max_length=50, default=None, blank=True, null=True)
	withWhomRecentV = models.CharField(max_length=50, default=None, blank=True, null=True)
	happenedRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	physicalRecentV = models.BooleanField(default=False, blank=True)
	verbalRecentV = models.BooleanField(default=False, blank=True)
	threatsRecentV = models.BooleanField(default=False, blank=True)
	propertyRecentV = models.BooleanField(default=False, blank=True)
	otherRecentV = models.BooleanField(default=False, blank=True)
	otherExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	typeWordsRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	wasTense = models.BooleanField(default=False, blank=True)
	hadRush = models.BooleanField(default=False, blank=True)
	feltStrong = models.BooleanField(default=False, blank=True)
	psychoRecentV = models.BooleanField(default=False, blank=True)
	psychoWhyRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	longAgoTreatRecentVmos = models.IntegerField(default=0)
	longAgoTreatRecentVyrs = models.IntegerField(default=0)
	didCompleteTreatRecentV = models.BooleanField(default=False, blank=True)
	reasonNotCompleteRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT ANGER/VIOLENCE HISTORY PART 2----------------------------------------------------------------
class AM_AngerHistory2(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	depress30RecentV = models.BooleanField(default=False, blank=True)
	depress30ExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	anxietyRecentV = models.BooleanField(default=False, blank=True)
	anxietyExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	hallucinationRecentV = models.BooleanField(default=False, blank=True)
	hallucinationLastV = models.CharField(max_length=100, default=None, blank=True, null=True)
	understandingRecentV = models.BooleanField(default=False, blank=True)
	understandingExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	troubleControlRecentV = models.BooleanField(default=False, blank=True)
	lastTimeTroubleControl = models.CharField(max_length=100, default=None, blank=True, null=True)
	controlTrigger = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicide30RecentV = models.BooleanField(default=False, blank=True)
	suicide30ExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicideTodayRecentV = models.BooleanField(default=False, blank=True)
	suicideTodayPlanRecentV = models.BooleanField(default=False, blank=True)
	suicideTodayExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	hasAttemptedSuicide = models.BooleanField(default=False, blank=True)
	hasAttemptedExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	
	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT ANGER/VIOLENCE HISTORY PART 3----------------------------------------------------------------
class AM_AngerHistory3(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	homicidal = models.BooleanField(default=False, blank=True)
	homicidalExplain = models.CharField(max_length=100, default=None, blank=True, null=True)
	medRecentV = models.BooleanField(default=False, blank=True)
	medRecentVExplain = models.CharField(max_length=100, default=None, blank=True, null=True)
	medSuccessRecentV = models.BooleanField(default=False, blank=True)
	medSuccessExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	durationRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	intensityRecentV = models.IntegerField(default=0)
	howOften = models.CharField(max_length=25, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT CONNECTIONS OF USE AND ANGER----------------------------------------------------------
class AM_Connections(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	angerWorse = models.BooleanField(default=False, blank=True)
	troubleWhenUsing = models.BooleanField(default=False, blank=True)
	lessAngry = models.BooleanField(default=False, blank=True)
	othersTellMe = models.BooleanField(default=False, blank=True)
	noConnection = models.BooleanField(default=False, blank=True)
	otherConnectionsUsing = models.BooleanField(default=False, blank=True)
	connectionExplain = models.CharField(max_length=250, blank=True, null=True, default=None)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT WORST EPISODE--------------------------------------------------------------------------
class AM_WorstEpisode(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	whoWorst = models.CharField(max_length=50, default=None, blank=True, null=True)
	happenedWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	wordThoughtWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	howStartWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	howEndWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	useWorst = models.BooleanField(default=False, blank=True)
	iUsedWorst = models.BooleanField(default=False, blank=True)
	whoDidItFight = models.CharField(max_length=50, default=None, blank=True, null=True)
	theyUsedWorst = models.BooleanField(default=False, blank=True)
	physicalWorst = models.BooleanField(default=False, blank=True)
	verbalWorst = models.BooleanField(default=False, blank=True)
	threatsWorst = models.BooleanField(default=False, blank=True)
	propertyWorst = models.BooleanField(default=False, blank=True)
	otherWorst = models.BooleanField(default=False, blank=True)
	otherWorstDescription = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT WITH WHOM YOU GET ANGRY----------------------------------------------------------------
class AM_AngerTarget(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	angryPartner = models.BooleanField(blank=True, default=False)
	angryParents = models.BooleanField(blank=True, default=False)
	angryChildren = models.BooleanField(blank=True, default=False)
	angryRelatives = models.BooleanField(blank=True, default=False)
	angryEmployer = models.BooleanField(blank=True, default=False)
	angryFriends = models.BooleanField(blank=True, default=False)
	angryOther = models.BooleanField(blank=True, default=False)
	otherWhom = models.CharField(max_length=25, default=None, blank=True, null=True)
	angryAbout = models.CharField(max_length=100, default=None, blank=True, null=True)
	seldomUpset = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT FAMILY OF ORIGIN-----------------------------------------------------------------------
class AM_FamilyOrigin(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	kidMomAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidDadAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidSiblingAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidOtherAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	learnFamilyAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicideHistory = models.BooleanField(blank=True, default=False)
	hasLovingMother = models.BooleanField(blank=True, default=False)
	hasLovingSiblings = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT ANY CURRENT PROBLEMS HISTORY OF--------------------------------------------------------
class AM_CurrentProblem(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	brainInjury = models.BooleanField(blank=True, default=False)
	stroke = models.BooleanField(blank=True, default=False)
	epilepsy = models.BooleanField(blank=True, default=False)
	attentionDD = models.BooleanField(blank=True, default=False)
	pms = models.BooleanField(blank=True, default=False)
	depression = models.BooleanField(blank=True, default=False)
	ptsd = models.BooleanField(blank=True, default=False)
	otherSeriousIllness = models.BooleanField(blank=True, default=False)
	currentlyOnMeds = models.BooleanField(blank=True, default=False)
	whichMeds = models.CharField(max_length=100, default=None, blank=True, null=True)
	describeIssue = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT CONTROL--------------------------------------------------------------------------------
class AM_Control(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	neverAttemptedControl = models.BooleanField(blank=True, default=False)
	talkToMyself = models.BooleanField(blank=True, default=False)
	whatSayYou = models.CharField(max_length=50, default=None, blank=True, null=True)
	leaveScene = models.BooleanField(blank=True, default=False)
	howLongLeaveScene = models.CharField(max_length=50, default=None, blank=True, null=True)
	whatDoLeave = models.CharField(max_length=100, default=None, blank=True, null=True)
	relax = models.BooleanField(blank=True, default=False)
	howRelax = models.CharField(max_length=200, default=None, blank=True, null=True)
	selfHelpGroup = models.BooleanField(blank=True, default=False)
	otherControlAnger = models.BooleanField(blank=True, default=False)
	doWhatOtherControl = models.CharField(max_length=50, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT OTHER THINGS---------------------------------------------------------------------------
class AM_Final(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	anythingelse = models.CharField(max_length=250, default=None, blank=True, null=True)
	changeLearn1 = models.CharField(max_length=100, default=None, blank=True, null=True)
	changeLearn2 = models.CharField(max_length=100, default=None, blank=True, null=True)
	changeLearn3 = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.client_id)

##ANGER MANAGEMENT FULL IMPLEMENTATION OF ASSESSMENT FILE-------------------------------------------------------------
class AngerManagement(models.Model):
	client = models.ForeignKey(Client, blank=True, null=True, default=None)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	demographic = models.ForeignKey(AM_Demographic, blank=True, null=True, default=None)
	drugHistory = models.ForeignKey(AM_DrugHistory, blank=True, null=True, default=None)
	childhood = models.ForeignKey(AM_ChildhoodHistory, blank=True, null=True, default=None)
	angerHistory = models.ForeignKey(AM_AngerHistory, blank=True, null=True, default=None)
	angerHistory2 = models.ForeignKey(AM_AngerHistory2, blank=True, null=True, default=None)
	angerHistory3 = models.ForeignKey(AM_AngerHistory3, blank=True, null=True, default=None)
	connections = models.ForeignKey(AM_Connections, blank=True, null=True, default=None)
	worstEpisode = models.ForeignKey(AM_WorstEpisode, blank=True, null=True, default=None)
	angerTarget = models.ForeignKey(AM_AngerTarget, blank=True, null=True, default=None)
	familyOrigin = models.ForeignKey(AM_FamilyOrigin, blank=True, null=True, default=None)
	currentProblems = models.ForeignKey(AM_CurrentProblem, blank=True, null=True, default=None)
	control = models.ForeignKey(AM_Control, blank=True, null=True, default=None)
	final = models.ForeignKey(AM_Final, blank=True, null=True, default=None)

	start_time = models.DateTimeField(default=None, blank=True, null=True)
	end_time = models.DateTimeField(default=None, blank=True, null=True)

	demographicComplete = models.BooleanField(blank= True, default = False)
	drugHistoryComplete = models.BooleanField(blank= True, default = False)
	childhoodComplete = models.BooleanField(blank= True, default = False)
	angerHistoryComplete = models.BooleanField(blank= True, default = False)
	angerHistoryComplete2 = models.BooleanField(blank= True, default = False)
	angerHistoryComplete3 = models.BooleanField(blank= True, default = False)
	connectionsComplete = models.BooleanField(blank= True, default = False)
	worstComplete = models.BooleanField(blank= True, default = False)
	angerTargetComplete = models.BooleanField(blank= True, default = False)
	familyOriginComplete = models.BooleanField(blank= True, default = False)
	currentProblemsComplete = models.BooleanField(blank= True, default = False)
	controlComplete = models.BooleanField(blank= True, default = False)
	finalComplete = models.BooleanField(blank= True, default = False)

	demoPriority = models.BooleanField(blank= True, default = False)
	dhPriority = models.BooleanField(blank= True, default = False)
	childPriority = models.BooleanField(blank= True, default = False)
	ah1Priority = models.BooleanField(blank= True, default = False)
	ah2Priority = models.BooleanField(blank= True, default = False)
	ah3Priority = models.BooleanField(blank= True, default = False)
	connectPriority = models.BooleanField(blank= True, default = False)
	worstPriority = models.BooleanField(blank= True, default = False)
	targetPriority = models.BooleanField(blank= True, default = False)
	familyPriority = models.BooleanField(blank= True, default = False)
	currentPriority = models.BooleanField(blank= True, default = False)
	controlPriority = models.BooleanField(blank= True, default = False)
	finalPriority = models.BooleanField(blank= True, default = False)

	isOpen = models.BooleanField(blank=True, default=False)
	AMComplete = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return str(self.client.fname) + ' ' + str(self.client.lname) + " " + str(self.start_time)

class MHDemographic(models.Model):
	#HISTORY I
	clientID = models.CharField(max_length=25, default=None, blank=True, null=True)

	birthplace = models.CharField(max_length=25, default=None, blank=True, null=True)
	raised = models.CharField(max_length=20, default=None, blank=True, null=True)
	maritalStatus = models.CharField(max_length=30, default=None, blank=True, null=True)
	numMarriages = models.IntegerField(default=0)
	occupation = models.CharField(max_length=30, default=None, blank=True, null=True)
	employer = models.CharField(max_length=30, default=None, blank=True, null=True)
	employedMo = models.IntegerField(default=0)
	employedYrs = models.IntegerField(default=0)
	pastJobs = models.CharField(max_length=1000, default=None, blank=True, null=True)
	recentMove = models.CharField(max_length=100, default=None, blank=True, null=True)
	spouseAge = models.IntegerField(default=0)
	spouseOccupation = models.CharField(max_length=30, default=None, blank=True, null=True)
	spouseEmployer = models.CharField(max_length=35, default=None, blank=True, null=True)
	spouseWorkMos = models.IntegerField(default=0)
	spouseWorkYrs = models.IntegerField(default=0)

	childrenMale = models.CharField(max_length=1000, default=None, blank=True, null=True)
	childrenFemale = models.CharField(max_length=1000, default=None, blank=True, null=True)
	bothers = models.CharField(max_length=1000, default=None, blank=True, null=True)
	sisters = models.CharField(max_length=1000, default=None, blank=True, null=True)

	motherOccupation = models.CharField(max_length=35, default=None, blank=True, null=True)
	motherCity = models.CharField(max_length=35, default=None, blank=True, null=True)
	motherState = models.CharField(max_length=35, default=None, blank=True, null=True)
	motherLiving = models.BooleanField(blank= True, default = True)
	motherAge = models.IntegerField(default=0)
	motherAgeDeath = models.IntegerField(default=0)

	fatherOccupation = models.CharField(max_length=35, default=None, blank=True, null=True)
	fatherCity = models.CharField(max_length=35, default=None, blank=True, null=True)
	fatherState = models.CharField(max_length=35, default=None, blank=True, null=True)
	fatherLiving = models.BooleanField(blank= True, default = True)
	fatherAge = models.IntegerField(default=0)
	fatherAgeDeath = models.IntegerField(default=0)

	numChildren = models.IntegerField(default=0)
	numSisters = models.IntegerField(default=0)
	numBrothers = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.clientID)

##MENTAL HEALTH EDUCATION-------------------------------------------------------------------------------
class MHEducation(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	GradesKto6 = models.CharField(max_length=1, default=None, blank=True, null=True)
	BehaviorProblemsKto6 = models.BooleanField(default=False, blank=True)
	AcademicProblemsKto6 = models.BooleanField(default=False, blank=True)
	FriendshipsKto6 = models.IntegerField(default=0)
	Grades7to9 = models.CharField(max_length=1, default=None, blank=True, null=True)
	BehaviorProblems7to9 = models.BooleanField(default=False, blank=True)
	AcademicProblems7to9 = models.BooleanField(default=False, blank=True)
	Friendships7to9 = models.IntegerField(default=0)
	Grades10to12 = models.CharField(max_length=1, default=None, blank=True, null=True)
	BehaviorProblems10to12 = models.BooleanField(default=False, blank=True)
	AcademicProblems10to12 = models.BooleanField(default=False, blank=True)
	Friendships10to12 = models.IntegerField(default=0)
	collegeYears = models.IntegerField(default=0)
	collegeDegree = models.BooleanField(default=False, blank=True)
	collegeMajor = models.CharField(max_length=25, blank=True, null=True, default=None)
	advanceDegree = models.BooleanField(blank=True, default=False)
	tradeSch = models.BooleanField(blank=True, default=False)
	tradeSchool = models.CharField(max_length=25, blank=True, null=True, default=None)
	tradeAreaStudy = models.CharField(max_length=25, blank=True, null=True, default=None)
	military = models.BooleanField(blank=True, default=False)
	militaryBranch = models.CharField(max_length=20, default=None, blank=True, null=True)
	militaryYears = models.IntegerField(default=0)
	militaryRank = models.CharField(max_length=25, default=None, blank=True, null=True)
	honorableDischarge = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return str(self.clientID)

##MENTAL HEALTH FAMILY----------------------------------------------------------------------------------
class MHBackground(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	residence = models.CharField(max_length=20, default=None, blank=True, null=True)
	income = models.CharField(max_length=10, default=None, blank=True, null=True)
	debt = models.CharField(max_length=10, default=None, blank=True, null=True)
	credit = models.CharField(max_length=20, default=None, blank=True, null=True)
	healthCare = models.CharField(max_length=35, default=None, blank=True, null=True)
	otherIncome = models.CharField(max_length=50, default=None, blank=True, null=True)

	spouseRelationship = models.CharField(max_length=10, default=None, blank=True, null=True)
	brothersRelationship = models.CharField(max_length=10, default=None, blank=True, null=True)
	childrenRelationship = models.CharField(max_length=10, default=None, blank=True, null=True)
	parentsRelationship = models.CharField(max_length=10, default=None, blank=True, null=True)
	sistersRelationship = models.CharField(max_length=10, default=None, blank=True, null=True)
	exRelationship = models.CharField(max_length=10, default=None, blank=True, null=True)

	closeFriendVisit = models.CharField(max_length=10, default=None, blank=True, null=True)
	closeFriendNumber = models.IntegerField(default=0)
	acqVisit = models.CharField(max_length=10, default=None, blank=True, null=True)
	acqNumber = models.IntegerField(default=0)

	interest = models.CharField(max_length=50, default=None, blank=True, null=True)
	interestWeek = models.IntegerField(default=0)
	interestMonth = models.IntegerField(default=0)
	friendAct = models.CharField(max_length=50, default=None, blank=True, null=True)
	friendActWeek = models.IntegerField(default=0)
	friendActMonth = models.IntegerField(default=0)
	workAct = models.CharField(max_length=50, default=None, blank=True, null=True)
	workActWeek = models.IntegerField(default=0)
	workActMonth = models.IntegerField(default=0)
	churchAffiliation = models.CharField(max_length=50, default=None, blank=True, null=True)
	churchWeek = models.IntegerField(default=0)
	churchMonth = models.IntegerField(default=0)
	churchYear = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.clientID)

##MENTAL HEALTH ENVIRONMENTAL STRESSORS-----------------------------------------------------------------
class MHStressor(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	deathStress = models.BooleanField(default=False, blank=True)
	deathStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	divorceStress = models.BooleanField(default=False, blank=True)
	divorceStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	moveStress = models.BooleanField(default=False, blank=True)
	moveStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	medicalStress = models.BooleanField(default=False, blank=True)
	medicalStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	familyHealthStress = models.BooleanField(default=False, blank=True)
	familyHealthStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	financialStress = models.BooleanField(default=False, blank=True)
	financialStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	abuseStress = models.BooleanField(default=False, blank=True)
	abuseStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	addictionFamilyStress = models.BooleanField(default=False, blank=True)
	addictionFamilyStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	violenceFamilyStress = models.BooleanField(default=False, blank=True)
	violenceFamilyStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)
	otherStress = models.BooleanField(default=False, blank=True)
	otherStressExp = models.CharField(max_length=500, default=None, blank=True, null=True)

	##PAST PSYCHIATRIC HISTORY----------------------------------------------------------------
	psychiatricHistory = models.CharField(max_length=500, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

##MENTAL HEALTH FAMILY HISTORY--------------------------------------------------------------------------
class MHFamilyHistory(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	isdepressed = models.BooleanField(default=False, blank=True)
	depressed = models.CharField(max_length=35, default=None, blank=True, null=True)
	isadd = models.BooleanField(default=False, blank=True)
	add = models.CharField(max_length=35, default=None, blank=True, null=True)
	isbedWetting = models.BooleanField(default=False, blank=True)
	bedWetting = models.CharField(max_length=35, default=None, blank=True, null=True)
	isbipolar = models.BooleanField(default=False, blank=True)
	bipolar = models.CharField(max_length=35, default=None, blank=True, null=True)
	issuicideAttempt = models.BooleanField(default=False, blank=True)
	suicideAttempt = models.CharField(max_length=35, default=None, blank=True, null=True)
	isphysicalAbuse = models.BooleanField(default=False, blank=True)
	physicalAbuse = models.CharField(max_length=35, default=None, blank=True, null=True)
	islaw = models.BooleanField(default=False, blank=True)
	law = models.CharField(max_length=35, default=None, blank=True, null=True)
	isld = models.BooleanField(default=False, blank=True)
	ld = models.CharField(max_length=35, default=None, blank=True, null=True)
	istic = models.BooleanField(default=False, blank=True)
	tic = models.CharField(max_length=35, default=None, blank=True, null=True)
	isthyroid = models.BooleanField(default=False, blank=True)
	thyroid = models.CharField(max_length=35, default=None, blank=True, null=True)
	isheart = models.BooleanField(default=False, blank=True)
	heart = models.CharField(max_length=35, default=None, blank=True, null=True)
	isoverweight = models.BooleanField(default=False, blank=True)
	overweight = models.CharField(max_length=35, default=None, blank=True, null=True)
	ismood = models.BooleanField(default=False, blank=True)
	mood = models.CharField(max_length=35, default=None, blank=True, null=True)
	isalcohol = models.BooleanField(default=False, blank=True)
	alcohol = models.CharField(max_length=35, default=None, blank=True, null=True)
	isdrugs = models.BooleanField(default=False, blank=True)
	drugs = models.CharField(max_length=35, default=None, blank=True, null=True)
	isschizo = models.BooleanField(default=False, blank=True)
	schizo = models.CharField(max_length=35, default=None, blank=True, null=True)
	isseizures = models.BooleanField(default=False, blank=True)
	seizures = models.CharField(max_length=35, default=None, blank=True, null=True)
	iscompletedSuicide = models.BooleanField(default=False, blank=True)
	completedSuicide = models.CharField(max_length=35, default=None, blank=True, null=True)
	issexAbuse = models.BooleanField(default=False, blank=True)
	sexAbuse = models.CharField(max_length=35, default=None, blank=True, null=True)
	ispanic = models.BooleanField(default=False, blank=True)
	panic = models.CharField(max_length=35, default=None, blank=True, null=True)
	isanxiety = models.BooleanField(default=False, blank=True)
	anxiety = models.CharField(max_length=35, default=None, blank=True, null=True)
	isOCD = models.BooleanField(default=False, blank=True)
	OCD = models.CharField(max_length=35, default=None, blank=True, null=True)
	isdiabetes = models.BooleanField(default=False, blank=True)
	diabetes = models.CharField(max_length=35, default=None, blank=True, null=True)
	iscancer = models.BooleanField(default=False, blank=True)
	cancer = models.CharField(max_length=35, default=None, blank=True, null=True)
	ishighBloodPressure = models.BooleanField(default=False, blank=True)
	highBloodPressure = models.CharField(max_length=35, default=None, blank=True, null=True)
	isanger = models.BooleanField(default=False, blank=True)
	anger = models.CharField(max_length=35, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

##MENTAL HEALTH LEGAL HISTORY---------------------------------------------------------------------------
class MHLegalHistory(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	num_arrest = models.IntegerField(default=0)
	arrestCharges = models.CharField(max_length=100, default=None, blank=True, null=True)
	num_convictions = models.IntegerField(default=0)
	convictionCharges = models.CharField(max_length=100, default=None, blank=True, null=True)
	num_DUI_charges = models.IntegerField(default=0)
	num_DUI_convictions = models.IntegerField(default=0)
	probationPresent = models.BooleanField(default=False, blank=True)
	probationPast = models.BooleanField(default=False, blank=True)
	probationOfficer = models.CharField(max_length=35, blank=True, null=True, default=None)
	probationOffense = models.CharField(max_length=35, blank=True, null=True, default=None)
	suspendedDrivePresent = models.BooleanField(default=False, blank=True)
	num_suspended = models.IntegerField(default=0)
	hasLawsuit = models.BooleanField(default=False, blank=True)
	lawsuitStress = models.BooleanField(default=False, blank=True)
	inDivorce = models.BooleanField(default=False, blank=True)
	childCustody = models.BooleanField(default=False, blank=True)
	hasBankrupcy = models.BooleanField(default=False, blank=True)
	dateBenkrupcy = models.CharField(max_length=25, default=None, blank=True, null=True)
	explainPositiveAnswers = models.CharField(max_length=250, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)




##MENTAL HEALTH DRUG AND ALCOHOL USE--------------------------------------------------------------------
class MHUseTable(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	howMuch1 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften1 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong1 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld1 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime1 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch2 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften2 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong2 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld2 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime2 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch3 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften3 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong3 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld3 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime3 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch4 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften4 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong4 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld4 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime4 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch5 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften5 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong5 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld5 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime5 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch6 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften6 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong6 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld6 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime6 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch7 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften7 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong7 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld7 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime7 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch8 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften8 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong8 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld8 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime8 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch9 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften9 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong9 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld9 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime9 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch10 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften10 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong10 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld10 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime10 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch11 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften11 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong11 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld11 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime11 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch12 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften12 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong12 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld12 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime12 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch13 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften13 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong13 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld13 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime13 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch14 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften14 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong14 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld14 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime14 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch15 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften15 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong15 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld15 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime15 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch16 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften16 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong16 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld16 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime16 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch17 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften17 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong17 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld17 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime17 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch18 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften18 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong18 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld18 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime18 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch19 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften19 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong19 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld19 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime19 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch20 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften20 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong20 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld20 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime20 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howMuch21 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOften21 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howLong21 = models.CharField(max_length=15, default=None, blank=True, null=True)
	howOld21 = models.CharField(max_length=15, default=None, blank=True, null=True)
	lastTime21 = models.CharField(max_length=15, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class MentalHealth(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)

	demographics = models.ForeignKey(MHDemographic, default=None, blank=True, null=True)
	education = models.ForeignKey(MHEducation, default=None, blank=True, null=True)
	background = models.ForeignKey(MHBackground, default=None, blank=True, null=True)
	stressors = models.ForeignKey(MHStressor, default=None, blank=True, null=True)
	familyHistory = models.ForeignKey(MHFamilyHistory, default=None, blank=True, null=True)
	legalHistory = models.ForeignKey(MHLegalHistory, default=None, blank=True, null=True)
	useTable = models.ForeignKey(MHUseTable, default=None, blank=True, null=True)

	demographicsComplete = models.BooleanField(default=False, blank=True)
	educationComplete = models.BooleanField(default=False, blank=True)
	backgroundComplete = models.BooleanField(default=False, blank=True)
	stressorComplete = models.BooleanField(default=False, blank=True)
	familyComplete = models.BooleanField(default=False, blank=True)
	legalComplete = models.BooleanField(default=False, blank=True)
	psychComplete = models.BooleanField(default=False, blank=True)
	useComplete = models.BooleanField(default=False, blank=True)

	demoPriority = models.BooleanField(default=False, blank=True)
	educationPriority = models.BooleanField(default=False, blank=True)
	backgroundPriority = models.BooleanField(default=False, blank=True)
	stressPriority = models.BooleanField(default=False, blank=True)
	familyPriority = models.BooleanField(default=False, blank=True)
	legalPriority = models.BooleanField(default=False, blank=True)
	psychPriority = models.BooleanField(default=False, blank=True)
	usePriority = models.BooleanField(default=False, blank=True)

	isOpen = models.BooleanField(default=False, blank=True)
	MHComplete = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "Mental Health Form: " + str(self.client)

################################################################################################################################
#******************************************************************************************************************************#
#------------------------------------------------------------- ASI ------------------------------------------------------------#
#******************************************************************************************************************************#
################################################################################################################################

class AIS_Admin(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)
	g1 = models.CharField(max_length=4, default=None, blank=True, null=True)
	g2 = models.CharField(max_length=4, default=None, blank=True, null=True)
	g3 = models.CharField(max_length=4, default=None, blank=True, null=True)
	g4 = models.DateField(blank=True, null=True, default=None)
	g8 = models.IntegerField(default=0)
	g9 = models.IntegerField(default=0)
	g10 = models.IntegerField(default=0)
	g11 = models.CharField(max_length=2, default=None, blank=True, null=True)
	g12 = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.clientID)

class AIS_General(models.Model):
	clientID 	= models.CharField(max_length=30, default=None, blank=True, null=True)
	g13 		= models.CharField(max_length=3, default=None, blank=True, null=True)
	g14yrs 		= models.CharField(max_length=2, default=None, blank=True, null=True)
	g14mos 		= models.CharField(max_length=2, default=None, blank=True, null=True)
	g15 		= models.BooleanField(default=False, blank=True)
	g16mth 		= models.CharField(max_length=2, default=None, blank=True, null=True)
	g16day 		= models.CharField(max_length=2, default=None, blank=True, null=True)
	g16year 	= models.CharField(max_length=2, default=None, blank=True, null=True)
	g17 		= models.CharField(max_length=1, default=None, blank=True, null=True)
	g18 		= models.CharField(max_length=1, default=None, blank=True, null=True)
	g19 		= models.CharField(max_length=1, default=None, blank=True, null=True)
	g20 		= models.CharField(max_length=2, default=None, blank=True, null=True)

	#______________________ADDITIONAL TEST REULTS__________________________________#
	g21 = models.CharField(max_length=3, default=None, blank=True, null=True)
	g22 = models.CharField(max_length=3, default=None, blank=True, null=True)
	g23 = models.CharField(max_length=2, default=None, blank=True, null=True)
	g24 = models.CharField(max_length=3, default=None, blank=True, null=True)
	g25 = models.CharField(max_length=2, default=None, blank=True, null=True)
	g26 = models.CharField(max_length=3, default=None, blank=True, null=True)
	g27 = models.CharField(max_length=3, default=None, blank=True, null=True)
	g28 = models.CharField(max_length=3, default=None, blank=True, null=True)

	#_____________________________SEVERITY RATING__________________________________#
	medical = models.CharField(max_length=1, default=None, blank=True, null=True)
	employ 	= models.CharField(max_length=1, default=None, blank=True, null=True)
	alcohol = models.CharField(max_length=1, default=None, blank=True, null=True)
	drug 	= models.CharField(max_length=1, default=None, blank=True, null=True)
	legal 	= models.CharField(max_length=1, default=None, blank=True, null=True)
	family 	= models.CharField(max_length=1, default=None, blank=True, null=True)
	psych 	= models.CharField(max_length=1, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Medical(models.Model):
	clientID 	= models.CharField(max_length=30, default=None, blank=True, null=True)

	m1 = models.CharField(max_length=2, default=None, blank=True, null=True)
	m2yrs = models.CharField(max_length=2, default=None, blank=True, null=True)
	m2mth = models.CharField(max_length=2, default=None, blank=True, null=True)
	m3 = models.BooleanField(default=False, blank=True)
	m4 = models.BooleanField(default=False, blank=True)
	m5 = models.BooleanField(default=False, blank=True)
	m5Exp = models.CharField(max_length=100, default=None, blank=True, null=True)
	m6 = models.CharField(max_length=2, default=None, blank=True, null=True)
	m7 = models.CharField(max_length=1, default=None, blank=True, null=True)
	m8 = models.CharField(max_length=1, default=None, blank=True, null=True)
	m9 = models.CharField(max_length=1, default=None, blank=True, null=True)
	m10 = models.BooleanField(default=False, blank=True)
	m11 = models.BooleanField(default=False, blank=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Employment(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	e1yrs = models.CharField(max_length=2, default=None, blank=True, null=True)
	e1mth = models.CharField(max_length=2, default=None, blank=True, null=True)
	e2 = models.CharField(max_length=2, default=None, blank=True, null=True)
	e3 = models.BooleanField(default=False, blank=True)
	e3Exp = models.CharField(max_length=50, default=None, blank=True, null=True)
	e4 = models.BooleanField(default=False, blank=True)
	e5 = models.BooleanField(default=False, blank=True)
	e5Exp = models.BooleanField(default=False, blank=True)
	e6yrs = models.CharField(max_length=2, default=None, blank=True, null=True)
	e6mth = models.CharField(max_length=2, default=None, blank=True, null=True)
	e7 = models.BooleanField(default=False, blank=True)
	e7Exp = models.CharField(max_length=50, default=None, blank=True, null=True)
	e8 = models.BooleanField(default=False, blank=True)
	e9 = models.BooleanField(default=False, blank=True)
	e10 = models.CharField(max_length=1, default=None, blank=True, null=True)
	e11 = models.CharField(max_length=2, default=None, blank=True, null=True)
	e12 = models.CharField(max_length=4, default=None, blank=True, null=True)
	e13 = models.CharField(max_length=4, default=None, blank=True, null=True)
	e14 = models.CharField(max_length=4, default=None, blank=True, null=True)
	e15 = models.CharField(max_length=4, default=None, blank=True, null=True)
	e16 = models.CharField(max_length=4, default=None, blank=True, null=True)
	e17 = models.CharField(max_length=4, default=None, blank=True, null=True)
	e18 = models.CharField(max_length=1, default=None, blank=True, null=True)
	e19 = models.CharField(max_length=1, default=None, blank=True, null=True)
	e20 = models.CharField(max_length=1, default=None, blank=True, null=True)
	e21 = models.CharField(max_length=1, default=None, blank=True, null=True)
	e22 = models.CharField(max_length=1, default=None, blank=True, null=True)
	e23 = models.BooleanField(default=False, blank=True)
	e24 = models.BooleanField(default=False, blank=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Drug1(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	d1Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d1Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d1Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d2Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d2Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d2Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d3Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d3Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d3Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d4Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d4Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d4Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d5Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d5Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d5Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d6Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d6Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d6Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d7Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d7Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d7Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d8Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d8Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d8Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d9Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d9Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d9Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d10Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d10Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d10Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d11Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d11Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d11Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d12Day = models.CharField(max_length=2, default=None, blank=True, null=True)
	d12Year = models.CharField(max_length=2, default=None, blank=True, null=True)
	d12Route = models.CharField(max_length=1, default=None, blank=True, null=True)
	d13 = models.CharField(max_length=1, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Drug2(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	d14 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d15 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d16 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d17 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d18 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d19 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d20 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d21 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d22 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d23 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d24 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d25 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d26 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d27 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d28 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d29 = models.CharField(max_length=2, default=None, blank=True, null=True)
	d30 = models.CharField(max_length=1, default=None, blank=True, null=True)
	d31 = models.CharField(max_length=1, default=None, blank=True, null=True)
	d32 = models.CharField(max_length=1, default=None, blank=True, null=True)
	d33 = models.CharField(max_length=1, default=None, blank=True, null=True)
	d34 = models.BooleanField(default=False, blank=True)
	d35 = models.BooleanField(default=False, blank=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Legal(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	l1 = models.BooleanField(default=False, blank=True)
	l2 = models.BooleanField(default=False, blank=True)
	l3 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l4 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l5 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l6 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l7 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l8 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l9 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l10 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l11 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l12 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l13 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l14 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l15 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l16 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l17 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l18 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l19 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l20 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l21 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l22 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l23 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l24 = models.BooleanField(default=False, blank=True)
	l25 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l26 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l27 = models.CharField(max_length=2, default=None, blank=True, null=True)
	l28 = models.CharField(max_length=1, default=None, blank=True, null=True)
	l29 = models.CharField(max_length=1, default=None, blank=True, null=True)
	l30 = models.CharField(max_length=1, default=None, blank=True, null=True)
	l31 = models.BooleanField(default=False, blank=True)
	l32 = models.BooleanField(default=False, blank=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Family(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	h1a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h1d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h1p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h2a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h2d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h2p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h3a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h3d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h3p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h4a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h4d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h4p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h5a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h5d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h5p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h6a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h6d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h6p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h7a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h7d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h7p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h8a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h8d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h8p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h9a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h9d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h9p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h10a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h10d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h10p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h11a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h11d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h11p = models.CharField(max_length=1, default=None, blank=True, null=True)
	h12a = models.CharField(max_length=1, default=None, blank=True, null=True)
	h12d = models.CharField(max_length=1, default=None, blank=True, null=True)
	h12p = models.CharField(max_length=1, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Social1(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	f1 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f2yrs = models.CharField(max_length=2, default=None, blank=True, null=True)
	f2mth = models.CharField(max_length=2, default=None, blank=True, null=True)
	f3 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f4 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f5yrs = models.CharField(max_length=2, default=None, blank=True, null=True)
	f5mth = models.CharField(max_length=2, default=None, blank=True, null=True)
	f6 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f7 = models.BooleanField(default=False, blank=True)
	f8 = models.BooleanField(default=False, blank=True)
	f9 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f10 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f11 = models.CharField(max_length=1, default=None, blank=True, null=True)

	f30 = models.CharField(max_length=2, default=None, blank=True, null=True)
	f31 = models.CharField(max_length=2, default=None, blank=True, null=True)
	f32 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f33 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f34 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f35 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f36 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f37 = models.BooleanField(default=False, blank=True)
	f38 = models.BooleanField(default=False, blank=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Social2(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	f12 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f13 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f14 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f16 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f17 = models.CharField(max_length=1, default=None, blank=True, null=True)
	f18d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f18y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f19d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f19y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f20d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f20y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f21d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f21y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f22d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f22y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f23d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f23y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f24d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f24y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f25d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f25y = models.CharField(max_length=1, default=None, blank=True, null=True)
	f26d = models.CharField(max_length=1, default=None, blank=True, null=True)
	f26y = models.CharField(max_length=1, default=None, blank=True, null=True)

	fa18 = models.BooleanField(default=False, blank=True)
	fa19 = models.BooleanField(default=False, blank=True)
	fa20 = models.BooleanField(default=False, blank=True)
	fa21 = models.BooleanField(default=False, blank=True)
	fa22 = models.BooleanField(default=False, blank=True)
	fa23 = models.BooleanField(default=False, blank=True)
	fa24 = models.BooleanField(default=False, blank=True)
	fa25 = models.BooleanField(default=False, blank=True)
	fa26 = models.BooleanField(default=False, blank=True)

	f18dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f18yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f19dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f19yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f20dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f20yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f21dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f21yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f22dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f22yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f23dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f23yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f24dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f24yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f25dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f25yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f26dayBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	f26yearBad = models.CharField(max_length=1, default=None, blank=True, null=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class AIS_Psych(models.Model):
	clientID = models.CharField(max_length=30, default=None, blank=True, null=True)

	p1 = models.CharField(max_length=2, default=None, blank=True, null=True)
	p2 = models.CharField(max_length=2, default=None, blank=True, null=True)
	p3 = models.BooleanField(default=False, blank=True)

	p4d = models.BooleanField(default=False, blank=True)
	p4y = models.BooleanField(default=False, blank=True)
	p5d = models.BooleanField(default=False, blank=True)
	p5y = models.BooleanField(default=False, blank=True)
	p6d = models.BooleanField(default=False, blank=True)
	p6y = models.BooleanField(default=False, blank=True)
	p7d = models.BooleanField(default=False, blank=True)
	p7y = models.BooleanField(default=False, blank=True)
	p8d = models.BooleanField(default=False, blank=True)
	p8y = models.BooleanField(default=False, blank=True)
	p9d = models.BooleanField(default=False, blank=True)
	p9y = models.BooleanField(default=False, blank=True)
	p10d = models.BooleanField(default=False, blank=True)
	p10y = models.BooleanField(default=False, blank=True)
	p11d = models.BooleanField(default=False, blank=True)
	p11y = models.BooleanField(default=False, blank=True)

	p12 = models.CharField(max_length=2, default=None, blank=True, null=True)
	p13 = models.CharField(max_length=1, default=None, blank=True, null=True)
	p14 = models.CharField(max_length=1, default=None, blank=True, null=True)

	p15 = models.BooleanField(default=False, blank=True)
	p16 = models.BooleanField(default=False, blank=True)
	p17 = models.BooleanField(default=False, blank=True)
	p18 = models.BooleanField(default=False, blank=True)
	p19 = models.BooleanField(default=False, blank=True)
	p20 = models.BooleanField(default=False, blank=True)

	p21 = models.CharField(max_length=1, default=None, blank=True, null=True)
	p22 = models.BooleanField(default=False, blank=True)
	p23 = models.BooleanField(default=False, blank=True)
	comments = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.clientID)

class ASI(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)
	startTime = models.CharField(max_length=4, default=None, blank=True, null=True)
	endTime = models.CharField(max_length=4, default=None, blank=True, null=True)

	admin = models.ForeignKey(AIS_Admin, default=None, blank=True, null=True)
	general = models.ForeignKey(AIS_General, default=None, blank=True, null=True)
	medical = models.ForeignKey(AIS_Medical, default=None, blank=True, null=True)
	employment = models.ForeignKey(AIS_Employment, default=None, blank=True, null=True)
	drug1 = models.ForeignKey(AIS_Drug1, default=None, blank=True, null=True)
	drug2 = models.ForeignKey(AIS_Drug2, default=None, blank=True, null=True)
	legal = models.ForeignKey(AIS_Legal, default=None, blank=True, null=True)
	family = models.ForeignKey(AIS_Family, default=None, blank=True, null=True)
	social1 = models.ForeignKey(AIS_Social1, default=None, blank=True, null=True)
	social2 = models.ForeignKey(AIS_Social2, default=None, blank=True, null=True)
	psych = models.ForeignKey(AIS_Psych, default=None, blank=True, null=True)

	adminComplete = models.BooleanField(default=False, blank=True)
	generalComplete = models.BooleanField(default=False, blank=True)
	medicalComplete = models.BooleanField(default=False, blank=True)
	employmentComplete = models.BooleanField(default=False, blank=True)
	drug1Complete = models.BooleanField(default=False, blank=True)
	drug2Complete = models.BooleanField(default=False, blank=True)
	legalComplete = models.BooleanField(default=False, blank=True)
	familyComplete = models.BooleanField(default=False, blank=True)
	social1Complete = models.BooleanField(default=False, blank=True)
	social2Complete = models.BooleanField(default=False, blank=True)
	psychComplete = models.BooleanField(default=False, blank=True)

	adminPriority = models.BooleanField(default=False, blank=True)
	generalPriority = models.BooleanField(default=False, blank=True)
	medicalPriority = models.BooleanField(default=False, blank=True)
	employmentPriority = models.BooleanField(default=False, blank=True)
	drug1Priority = models.BooleanField(default=False, blank=True)
	drug2Priority = models.BooleanField(default=False, blank=True)
	legalPriority = models.BooleanField(default=False, blank=True)
	familyPriority = models.BooleanField(default=False, blank=True)
	social1Priority = models.BooleanField(default=False, blank=True)
	social2Priority = models.BooleanField(default=False, blank=True)
	psychPriority = models.BooleanField(default=False, blank=True)

	isOpen = models.BooleanField(default=False, blank=True)
	AIS_Complete = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "AIS Date: " + str(self.date_of_assessment) + ' | ' + str(self.client.clientID)


################################################################################################################################
################################################################################################################################

## SESSION TYPE----------------------------------------------------------------------------------------
class SType(models.Model):
	session_type = models.CharField(max_length=50, default=None, blank=True, null=True)
	duration = models.IntegerField(default=0)
	fee = models.IntegerField(default=0)
	notes = models.CharField(max_length=50, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.session_type

## APPIONTMENTS----------------------------------------------------------------------------------------
class A_Time(models.Model):
	time = models.CharField(max_length=12, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.time

class Appointment(models.Model):
	date = models.DateField(blank=True, null=True, default=None)
	time = models.ForeignKey(A_Time, default=None, blank=True, null=True)
	client = models.ForeignKey(Client, blank=True, null=True, default=None)
	sessionType = models.ForeignKey(SType, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.date) + " " + str(self.time) + " " + str(self.time)

## SESSIONS--------------------------------------------------------------------------------------------
class Invoice(models.Model):
	billed_to = models.CharField(max_length=50, default=None, blank=True, null=True)
	date = models.DateTimeField(default=None, blank=True, null=True)
	service1 = models.CharField(max_length=50, default=None, blank=True, null=True)
	service2 = models.CharField(max_length=50, default=None, blank=True, null=True)
	service3 = models.CharField(max_length=50, default=None, blank=True, null=True)
	service4 = models.CharField(max_length=50, default=None, blank=True, null=True)
	service5 = models.CharField(max_length=50, default=None, blank=True, null=True)
	service6 = models.CharField(max_length=50, default=None, blank=True, null=True)
	amount = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.billed_to) + ' ' + str(self.date) + ' $' + str(self.amount)

class ClientSession(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	s_type = models.ForeignKey(SType, default=None, blank=True, null=True)
	invoice = models.ForeignKey(Invoice, default=None, blank=True, null=True)
	start = models.DateTimeField(default=None, blank=True, null=True)
	end = models.DateTimeField(default=None, blank=True, null=True)
	isComplete = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return str(self.client) + ' ' + str(self.start)


## This is a phony session but cannot be deleted due to the many to many field
class Session(models.Model):
	appointment = models.ForeignKey(Appointment, default=None, blank=True, null=True)
	start = models.DateTimeField(default=None, blank=True, null=True)
	end = models.DateTimeField(default=None, blank=True, null=True)

	#The type of visit being billed for...
	s_type = models.ManyToManyField(SType, default=None, blank=True, null=True)
	bill = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.appointment.client) + ' ' + str(self.appointment.date) + ' ' + str(self.bill)










































