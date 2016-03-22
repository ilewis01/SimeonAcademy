from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
	user = models.OneToOneField(User)
	is_counselor = models.NullBooleanField(default=None)
	is_validated = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return self.user.username

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

	def __unicode__(self):
		return "Urine Results: " + str(self.client)

##DEMOGRAPHIC SECTION OF THE SAP FORM------------------------------------------------------
class SapDemographics(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
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

	def __unicode__(self):
		return "SAP/Demographics: " + str(self.client.client_id)

##PSYCHOACTIVE HISTORY OF SAP FORM---------------------------------------------------------
class SapPsychoactive(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	drug1 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age1 = models.IntegerField(default=0)
	frequency1 = models.IntegerField(default=0)
	quantity1 = models.IntegerField(default=0)
	last1 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how1 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug2 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age2 = models.IntegerField(default=0)
	frequency2 = models.IntegerField(default=0)
	quantity2 = models.IntegerField(default=0)
	last2 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how2 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug3 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age3 = models.IntegerField(default=0)
	frequency3 = models.IntegerField(default=0)
	quantity3 = models.IntegerField(default=0)
	last3 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how3 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug4 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age4 = models.IntegerField(default=0)
	frequency4 = models.IntegerField(default=0)
	quantity4 = models.IntegerField(default=0)
	last4 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how4 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug5 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age5 = models.IntegerField(default=0)
	frequency5 = models.IntegerField(default=0)
	quantity5 = models.IntegerField(default=0)
	last5 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how5 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug6 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age6 = models.IntegerField(default=0)
	frequency6 = models.IntegerField(default=0)
	quantity6 = models.IntegerField(default=0)
	last6 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how6 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug7 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age7 = models.IntegerField(default=0)
	frequency7 = models.IntegerField(default=0)
	quantity7 = models.IntegerField(default=0)
	last7 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how7 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug8 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age8 = models.IntegerField(default=0)
	frequency8 = models.IntegerField(default=0)
	quantity8 = models.IntegerField(default=0)
	last8 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how8 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug9 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age9 = models.IntegerField(default=0)
	frequency9 = models.IntegerField(default=0)
	quantity9 = models.IntegerField(default=0)
	last9 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how9 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug10 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age10 = models.IntegerField(default=0)
	frequency10 = models.IntegerField(default=0)
	quantity10 = models.IntegerField(default=0)
	last10 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how10 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug11 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age11 = models.IntegerField(default=0)
	frequency11 = models.IntegerField(default=0)
	quantity11 = models.IntegerField(default=0)
	last11 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how11 = models.CharField(max_length=20, default=None, blank=True, null=True)
	drug12 = models.CharField(max_length=25, default=None, blank=True, null=True)
	age12 = models.IntegerField(default=0)
	frequency12 = models.IntegerField(default=0)
	quantity12 = models.IntegerField(default=0)
	last12 = models.CharField(max_length=20, default=None, blank=True, null=True)
	how12 = models.CharField(max_length=20, default=None, blank=True, null=True)

	def __unicode__(self):
		return "SAP/Psychoavtive Table: " + str(self.client_id)

##COMPLETE IMPLEMENTATION OF THE SAP FORM-----------------------------------------------
class SAP(models.Model):
	demographics = models.ForeignKey(SapDemographics, default=None, blank=True, null=True)
	psychoactive = models.ForeignKey(SapPsychoactive, default=None, blank=True, null=True)

	def __unicode__(self):
		return "SAP: " + str(self.demographics.client)

##ANGER MANAGEMENT DEMOGRAPHIC------------------------------------------------------------
class AM_Demographic(models.Model):
	client = models.ForeignKey(Client, default=None, blank=False, null=False)
	date_of_assessment = models.DateField(blank=True, default=None, null=True)
	
	maritalStatus = models.ForeignKey(MaritalStatus, default=None, blank=True, null=True)
	livingSituation = models.ForeignKey(LivingSituation, default=None, blank=True, null=True)
	own = models.BooleanField(default=False, blank=True)
	months_res = models.IntegerField(default=0)
	years_res = models.IntegerField(default=0)
	
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
	employer_phone = models.IntegerField(default=0)
	
	health_problem = models.BooleanField(default=False, blank=True)
	medication = models.BooleanField(default=False, blank=True)
	health_exp = models.CharField(max_length=250, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Anger Management/Demographics: " + str(self.client)

##ANGER MANAGEMENT ALCOHOL AND DRUG HISTORY---------------------------------------------------------
class AM_DrugHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	firstDrinkAge = models.IntegerField(default=0)
	firstDrinkType = models.CharField(default=None, max_length=50, blank=True, null=True)	
	curUse = models.BooleanField(default=False, blank=True)
	useType = models.CharField(max_length=50, default=None, blank=True, null=True)
	amtPerWeek = models.IntegerField(default=0)
	useAmt = models.IntegerField(default=0)
	everDrank = models.BooleanField(default=False, blank=True)
	timeQuit = models.IntegerField(default=0)
	monthsQuit = models.IntegerField(default=0)
	yearsQuit = models.IntegerField(default=0)
	reasonQuit = models.CharField(max_length=100, default=None, blank=True, null=True)
	DUI = models.BooleanField(blank=True, default=False)
	numDUI = models.IntegerField(default=0)
	BALevel = models.FloatField(default=0.0)
	drugTreatment = models.BooleanField(default=False, blank=True)
	treatmentPlace = models.CharField(max_length=50, default=None, blank=True, null=True)
	dateTreated = models.DateField(default=None, blank=True, null=True)
	finishedTreatment = models.BooleanField(default=False, blank=True)
	reasonNotFinishedTreatment = models.CharField(max_length=100, blank=True, null=True, default=None)
	isClean = models.BooleanField(default=False, blank=True)
	relapseTrigger = models.CharField(max_length=250, default=None, blank=True, null=True)
	drinkLastEpisode = models.BooleanField(default=False, blank=True)
	drinkRelationshipProblem = models.BooleanField(default=False, blank=True)
	needHelpDrugs = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "Anger Management/Drug History: " + str(self.client_id)

##ANGER MANAGEMENT CHILDHOOD HISTORY----------------------------------------------------------------
class AM_ChildhoodHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	raisedBy = models.CharField(max_length=20, default=None, blank=True, null=True)
	momAlive = models.BooleanField(default=False, blank=True)
	dadAlive = models.BooleanField(default=False, blank=True)
	childTrama = models.BooleanField(default=False, blank=True)
	howLeftHome = models.CharField(max_length=100, default=None, blank=True, null=True)
	num_siblings = models.IntegerField(default=0)
	siblingsRelationship = models.CharField(max_length=250, default=None, blank=True, null=True)
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
		return "Anger Management/Childhood History: " + str(self.client_id)

##ANGER MANAGEMENT ANGER/VIOLENCE HISTORY----------------------------------------------------------------
class AM_AngerHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	recentIncidentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	recentVDate = models.DateField(blank=True, null=True, default=None)
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
	howfeelRecentV = models.CharField(max_length=8, default=None, blank=True, null=True)
	psychoRecentV = models.BooleanField(default=False, blank=True)
	psychoWhyRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	longAgoTreatRecentVmos = models.IntegerField(default=0)
	longAgoTreatRecentVyrs = models.IntegerField(default=0)
	didCompleteTreatRecentV = models.BooleanField(default=False, blank=True)
	reasonNotCompleteRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	depress30RecentV = models.BooleanField(default=False, blank=True)
	depress30ExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	anxietyRecentV = models.BooleanField(default=False, blank=True)
	anxietyExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	hallucinationRecentV = models.BooleanField(default=False, blank=True)
	hallucinationRecentVmos = models.IntegerField(default=0)
	hallucinationRecentVyrs = models.IntegerField(default=0)
	understandingRecentV = models.BooleanField(default=False, blank=True)
	understandingExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	troubleControlRecentV = models.BooleanField(default=False, blank=True)
	troubleControlRecentVmos = models.IntegerField(default=0)
	troubleControlRecentVyrs = models.IntegerField(default=0)
	troubleControlExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicide30RecentV = models.BooleanField(default=False, blank=True)
	suicide30ExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicideTodayRecentV = models.BooleanField(default=False, blank=True)
	suicideTodayPlanRecentV = models.BooleanField(default=False, blank=True)
	suicideTodayExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	hasAttemptedSuicide = models.BooleanField(default=False, blank=True)
	hasAttemptedExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	homicidal = models.BooleanField(default=False, blank=True)
	homicidalExplain = models.CharField(max_length=100, default=None, blank=True, null=True)
	medRecentV = models.BooleanField(default=False, blank=True)
	medRecentVExplain = models.CharField(max_length=100, default=None, blank=True, null=True)
	medSuccessRecentV = models.BooleanField(default=False, blank=True)
	medSuccessExplainRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	episodeEndRecentV = models.CharField(max_length=100, default=None, blank=True, null=True)
	hadDrugsRecentV = models.BooleanField(default=False, blank=True)
	hadDrugsRecentVExplain = models.CharField(max_length=100, default=None, blank=True, null=True)
	typicalRecentV = models.BooleanField(default=False, blank=True)
	durationRecentV = models.CharField(max_length=25, default=None, blank=True, null=True)
	intensityRecentV = models.IntegerField(default=0)
	thisTimeOnly = models.BooleanField(default=False, blank=True)
	thisMonthOnly = models.BooleanField(default=False, blank=True)
	last6Months = models.BooleanField(default=False, blank=True)
	sinceChildhood = models.BooleanField(default=False, blank=True)
	adolescent = models.BooleanField(default=False, blank=True)
	onlyAsAdult = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "Anger Management/Anger History: " + str(self.client_id)

##ANGER MANAGEMENT CONNECTIONS OF USE AND ANGER----------------------------------------------------------
class AM_Connections(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	angerWorse = models.BooleanField(default=False, blank=True)
	troubleWhenUsing = models.BooleanField(default=False, blank=True)
	lessAngry = models.BooleanField(default=False, blank=True)
	othersTellMe = models.BooleanField(default=False, blank=True)
	noConnection = models.BooleanField(default=False, blank=True)
	otherConnectionsUsing = models.BooleanField(default=False, blank=True)
	connectionExplain = models.CharField(max_length=250, blank=True, null=True, default=None)

	def __unicode__(self):
		return "Anger Management/Connections: " + str(self.client_id)

##ANGER MANAGEMENT WORST EPISODE--------------------------------------------------------------------------
class AM_WorstEpisode(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	whoWorst = models.CharField(max_length=50, default=None, blank=True, null=True)
	happenedWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	wordThoughtWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	howStartWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	howEndWorst = models.CharField(max_length=100, default=None, blank=True, null=True)
	useWorst = models.BooleanField(default=False, blank=True)
	iUsedWorst = models.BooleanField(default=False, blank=True)
	theyUsedWorst = models.BooleanField(default=False, blank=True)
	physicalWorst = models.BooleanField(default=False, blank=True)
	verbalWorst = models.BooleanField(default=False, blank=True)
	threatsWorst = models.BooleanField(default=False, blank=True)
	propertyWorst = models.BooleanField(default=False, blank=True)
	otherWorst = models.BooleanField(default=False, blank=True)
	otherWorstDescription = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Anger Management/Worst Episode: " + str(self.client_id)

##ANGER MANAGEMENT WITH WHOM YOU GET ANGRY----------------------------------------------------------------
class AM_AngerTarget(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
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
		return "Anger Management/Anger Target: " + str(self.client_id)

##ANGER MANAGEMENT FAMILY OF ORIGIN-----------------------------------------------------------------------
class AM_FamilyOrigin(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	kidMomAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidDadAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidSiblingAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidOtherAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	learnFamilyAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicideHistory = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return "Anger Management/Family Origin: " + str(self.client_id)

##ANGER MANAGEMENT ANY CURRENT PROBLEMS HISTORY OF--------------------------------------------------------
class AM_CurrentProblem(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
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
		return "Anger Management/Current Problems: " + str(self.client_id)

##ANGER MANAGEMENT CONTROL--------------------------------------------------------------------------------
class AM_Control(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	neverAttemptedControl = models.BooleanField(blank=True, default=False)
	talkToMyself = models.BooleanField(blank=True, default=False)
	whatSayYou = models.CharField(max_length=50, default=None, blank=True, null=True)
	leaveScene = models.BooleanField(blank=True, default=False)
	howLongLeaveScene = models.IntegerField(default=0)
	whatDoLeave = models.CharField(max_length=100, default=None, blank=True, null=True)
	relax = models.BooleanField(blank=True, default=False)
	selfHelpGroup = models.BooleanField(blank=True, default=False)
	otherControlAnger = models.BooleanField(blank=True, default=False)
	doWhatOtherControl = models.CharField(max_length=50, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Anger Management/Control: " + str(self.client_id)

##ANGER MANAGEMENT OTHER THINGS---------------------------------------------------------------------------
class AM_Final(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	anythingelse = models.CharField(max_length=250, default=None, blank=True, null=True)
	changeLearn1 = models.CharField(max_length=100, default=None, blank=True, null=True)
	changeLearn2 = models.CharField(max_length=100, default=None, blank=True, null=True)
	changeLearn3 = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Anger Management/Final: " + str(self.client_id)

##ANGER MANAGEMENT FULL IMPLEMENTATION OF ASSESSMENT FILE-------------------------------------------------------------
class AngerManagement(models.Model):
	demographic = models.ForeignKey(AM_Demographic, blank=True, null=True, default=None)
	drugHistory = models.ForeignKey(AM_DrugHistory, blank=True, null=True, default=None)
	childhood = models.ForeignKey(AM_ChildhoodHistory, blank=True, null=True, default=None)
	angerHistory = models.ForeignKey(AM_AngerHistory, blank=True, null=True, default=None)
	connections = models.ForeignKey(AM_Connections, blank=True, null=True, default=None)
	worstEpisode = models.ForeignKey(AM_WorstEpisode, blank=True, null=True, default=None)
	angerTarget = models.ForeignKey(AM_AngerTarget, blank=True, null=True, default=None)
	familyOrigin = models.ForeignKey(AM_FamilyOrigin, blank=True, null=True, default=None)
	currentProblems = models.ForeignKey(AM_CurrentProblem, blank=True, null=True, default=None)
	control = models.ForeignKey(AM_Control, blank=True, null=True, default=None)
	final = models.ForeignKey(AM_Final, blank=True, null=True, default=None)

	demographicComplete = models.BooleanField(blank= True, default = False)
	drugHistoryComplete = models.BooleanField(blank= True, default = False)
	childhoodComplete = models.BooleanField(blank= True, default = False)
	angerHistoryComplete = models.BooleanField(blank= True, default = False)
	connectionsComplete = models.BooleanField(blank= True, default = False)
	worstComplete = models.BooleanField(blank= True, default = False)
	angerTargetComplete = models.BooleanField(blank= True, default = False)
	familyOriginComplete = models.BooleanField(blank= True, default = False)
	currentProblemsComplete = models.BooleanField(blank= True, default = False)
	controlComplete = models.BooleanField(blank= True, default = False)
	finalComplete = models.BooleanField(blank= True, default = False)

	AMComplete = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return str(self.demographic.client.fname) + ' ' + str(self.demographic.client.lname)

class MHDemographic(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	birthplace = models.CharField(max_length=25, default=None, blank=True, null=True)
	raised = models.CharField(max_length=20, default=None, blank=True, null=True)
	no_marriages = models.IntegerField(default=0)
	occupation = models.CharField(max_length=30, default=None, blank=True, null=True)
	employer = models.CharField(max_length=30, default=None, blank=True, null=True)
	employedMo = models.IntegerField(default=0)
	employedYrs = models.IntegerField(default=0)
	pastJobs = models.CharField(max_length=50, default=None, blank=True, null=True)
	##FINANCIAL STATUS------------------------------------------------------------------------
	residence = models.CharField(max_length=15, default=None, blank=True, null=True)
	income = models.CharField(max_length=15, default=None, blank=True, null=True)
	debt = models.CharField(max_length=15, default=None, blank=True, null=True)
	credit = models.CharField(max_length=15, default=None, blank=True, null=True)
	healthCare = models.CharField(max_length=15, default=None, blank=True, null=True)
	otherIncome = models.CharField(max_length=15, default=None, blank=True, null=True)
	##remember to check form to make sure that all fields are accounted for

	def __unicode__(self):
		return "Mental Health/Demographic: " + str(self.client)

##MENTAL HEALTH FAMILY----------------------------------------------------------------------------------
class MHFamily(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	spouseAge = models.IntegerField(default=0)
	spouseOccupation = models.CharField(max_length=35, default=None, blank=True, null=True)
	spouseEmployer = models.CharField(max_length=35, default=None, blank=True, null=True)
	spouseWorkMos = models.IntegerField(default=0)
	spouseWorkYrs = models.IntegerField(default=0)
	childrenMale = models.CharField(max_length=100, default=None, blank=True, null=True)
	childrenFemale = models.CharField(max_length=100, default=None, blank=True, null=True)
	recentMove = models.CharField(max_length=100, default=None, blank=True, null=True)
	motherOccupation = models.CharField(max_length=35, default=None, blank=True, null=True)
	motherJobCity = models.CharField(max_length=35, default=None, blank=True, null=True)
	motherJobState = models.CharField(max_length=2, default=None, blank=True, null=True)
	motherAge = models.IntegerField(default=0)
	motherAgeDeath = models.IntegerField(default=0)
	fatherOccupation = models.CharField(max_length=35, default=None, blank=True, null=True)
	fatherJobCity = models.CharField(max_length=35, default=None, blank=True, null=True)
	fatherJobState = models.CharField(max_length=2, default=None, blank=True, null=True)
	fatherAge = models.IntegerField(default=0)
	fatherAgeDeath = models.IntegerField(default=0)
	brothers = models.CharField(max_length=100, default=None, blank=True, null=True)
	sisters = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Mental Health/Family: " + str(self.client_id)

##MENTAL HEALTH EDUCATION-------------------------------------------------------------------------------
class MHEducation(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
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
	tradeSchool = models.BooleanField(blank=True, default=False)
	tradeAreaStudy = models.CharField(max_length=25, blank=True, null=True, default=None)
	wasMillitary = models.BooleanField(default=False, blank=True)
	millitaryBranch = models.CharField(max_length=20, default=None, blank=True, null=True)
	millitaryYears = models.IntegerField(default=0)
	millitaryRank = models.CharField(max_length=25, default=None, blank=True, null=True)
	honorableDischarge = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "Mental Health/Education: " + str(self.client_id)

##MENTAL HEALTH RELATIONSHIPS---------------------------------------------------------------------------
class MHRelationship(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	spouseR = models.CharField(max_length=7, default=None, blank=True, null=True)
	bothersR = models.CharField(max_length=7, default=None, blank=True, null=True)
	childrenR = models.CharField(max_length=7, default=None, blank=True, null=True)
	parentsR = models.CharField(max_length=7, default=None, blank=True, null=True)
	sistersR = models.CharField(max_length=7, default=None, blank=True, null=True)
	exR = models.CharField(max_length=7, default=None, blank=True, null=True)
	friendsCallNum = models.IntegerField(default=0)
	friendsVisitWeek = models.IntegerField(default=0)
	friendsVisitMonth = models.IntegerField(default=0)
	friendsVisitYear = models.IntegerField(default=0)
	aquaintCallNum = models.IntegerField(default=0)
	aquaintVisitWeek = models.IntegerField(default=0)
	aquaintVisitMonth = models.IntegerField(default=0)
	aquaintVisitYear = models.IntegerField(default=0)

	def __unicode__(self):
		return "Mental Health/Relationships: " + str(self.client_id)

##MENTAL HEALTH ACTIVITIES------------------------------------------------------------------------------
class MHActivity(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	interestAct = models.CharField(max_length=25, default=None, blank=True, null=True)
	interestWeek = models.IntegerField(default=0)
	interestMonth = models.IntegerField(default=0)
	friendsAct = models.CharField(max_length=25, default=None, blank=True, null=True)
	friendsWeek = models.IntegerField(default=0)
	friendsMonth = models.IntegerField(default=0)
	workAct = models.CharField(max_length=25, default=None, blank=True, null=True)
	workWeek = models.IntegerField(default=0)
	workMonth = models.IntegerField(default=0)
	churchAffiliation = models.CharField(max_length=40, default=None, blank=True, null=True)
	churchWeek = models.IntegerField(default=0)
	churchMonth = models.IntegerField(default=0)
	churchYear = models.IntegerField(default=0)

	def __unicode__(self):
		return "Mental Health/Activities: " + str(self.client_id)

##MENTAL HEALTH ENVIRONMENTAL STRESSORS-----------------------------------------------------------------
class MHStressor(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	deathStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	divorceStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	moveStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	medicalStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	familyHealthStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	financialStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	abuseStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	addictionFamilyStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	violenceFamilyStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	otherStress = models.CharField(max_length=500, default=None, blank=True, null=True)
	##PAST PSYCHIATRIC HISTORY----------------------------------------------------------------
	psychiatricHistory = models.CharField(max_length=500, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Mental Health/Stressors: " + str(self.client_id)

##MENTAL HEALTH FAMILY HISTORY--------------------------------------------------------------------------
class FamilyHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
	depression = models.CharField(max_length=35, default=None, blank=True, null=True)
	hyperactivity = models.CharField(max_length=35, default=None, blank=True, null=True)
	bedWetting = models.CharField(max_length=35, default=None, blank=True, null=True)
	bipolar = models.CharField(max_length=35, default=None, blank=True, null=True)
	suicideAttempt = models.CharField(max_length=35, default=None, blank=True, null=True)
	physicalAbuse = models.CharField(max_length=35, default=None, blank=True, null=True)
	law = models.CharField(max_length=35, default=None, blank=True, null=True)
	LD = models.CharField(max_length=35, default=None, blank=True, null=True)
	tic = models.CharField(max_length=35, default=None, blank=True, null=True)
	thyroid = models.CharField(max_length=35, default=None, blank=True, null=True)
	heart = models.CharField(max_length=35, default=None, blank=True, null=True)
	overweight = models.CharField(max_length=35, default=None, blank=True, null=True)
	mood = models.CharField(max_length=35, default=None, blank=True, null=True)
	alcohol = models.CharField(max_length=35, default=None, blank=True, null=True)
	drugs = models.CharField(max_length=35, default=None, blank=True, null=True)
	schizo = models.CharField(max_length=35, default=None, blank=True, null=True)
	seizures = models.CharField(max_length=35, default=None, blank=True, null=True)
	completedSuicide = models.CharField(max_length=35, default=None, blank=True, null=True)
	sexAbuse = models.CharField(max_length=35, default=None, blank=True, null=True)
	panic = models.CharField(max_length=35, default=None, blank=True, null=True)
	anxiety = models.CharField(max_length=35, default=None, blank=True, null=True)
	OCD = models.CharField(max_length=35, default=None, blank=True, null=True)
	diabetes = models.CharField(max_length=35, default=None, blank=True, null=True)
	cancer = models.CharField(max_length=35, default=None, blank=True, null=True)
	highBloodPressure = models.CharField(max_length=35, default=None, blank=True, null=True)
	anger = models.CharField(max_length=35, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Mental Health/Family History: " + str(self.client_id)

##MENTAL HEALTH LEGAL HISTORY---------------------------------------------------------------------------
class MHLegalHistory(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
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
		return "Mental Health/Legal History: " + str(self.client_id)

##MENTAL HEALTH DRUG AND ALCOHOL USE--------------------------------------------------------------------
class UseTable(models.Model):
	client_id = models.CharField(max_length=30, default=None, blank=True, null=True)
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
		return "Mental Health/Use Table: " + str(self.client_id)

class MentalHealth(models.Model):
	demographics = models.ForeignKey(MHDemographic, default=None, blank=True, null=True)
	family = models.ForeignKey(MHFamily, default=None, blank=True, null=True)
	education = models.ForeignKey(MHEducation, default=None, blank=True, null=True)
	relationships = models.ForeignKey(MHRelationship, default=None, blank=True, null=True)
	activities = models.ForeignKey(MHActivity, default=None, blank=True, null=True)
	stressors = models.ForeignKey(MHStressor, default=None, blank=True, null=True)
	familyHistory = models.ForeignKey(FamilyHistory, default=None, blank=True, null=True)
	legalHistory = models.ForeignKey(MHLegalHistory, default=None, blank=True, null=True)
	useTable = models.ForeignKey(UseTable, default=None, blank=True, null=True)

	demographicsComplete = models.BooleanField(default=False, blank=True)
	familyComplete = models.BooleanField(default=False, blank=True)
	educationComplete = models.BooleanField(default=False, blank=True)
	relationshipsComplete = models.BooleanField(default=False, blank=True)
	activitiesComplete = models.BooleanField(default=False, blank=True)
	stressorsComplete = models.BooleanField(default=False, blank=True)
	familyHistoryComplete = models.BooleanField(default=False, blank=True)
	legalHistoryComplete = models.BooleanField(default=False, blank=True)
	useTableComplete = models.BooleanField(default=False, blank=True)

	MHComplete = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return "Mental Health Form: " + str(self.demographics.client)







































