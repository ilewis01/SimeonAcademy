from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
	user = models.OneToOneField(User)
	is_counselor = models.NullBooleanField(default=None)

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
	lname = models.CharField(max_length=20, default=None, blank=True, null=True)
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
	clientID = models.CharField(max_length=10, default=None, blank=True, null=True)

	def __unicode__(self):
		return str(self.lname) + ", " + str(self.fname) + " " + str(self.dob)

class Discharge(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	discharge_date = models.DateField(default=None, blank=True, null=True)
	termReason = models.ForeignKey(TermReason, default=None, blank=True, null=True)
	diagnosis = models.CharField(max_length=50, default=None, blank=True, null=True)
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

class SAP(models.Model):
	client = models.ForeignKey(Client, default=None, blank=True, null=True)
	date1 = models.DateField(default=None, blank=True, null=True)
	date2 = models.DateField(default=None, blank=True, null=True)
	date3 = models.DateField(default=None, blank=True, null=True)
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

	##PSYCHOACTIVE HISTORY---------------------------------------------------------
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
		return "SAP: " + str(self.client)

class AngerManagement(models.Model):
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

	##ALCOHOL AND DRUG HISTORY---------------------------------------------------------
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

	##CHILDHOOD HISTORY----------------------------------------------------------------
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

	##ANGER/VIOLENCE HISTORY----------------------------------------------------------------

	##CONNECTIONS OF USE AND ANGER----------------------------------------------------------
	angerWorse = models.BooleanField(default=False, blank=True)
	troubleWhenUsing = models.BooleanField(default=False, blank=True)
	lessAngry = models.BooleanField(default=False, blank=True)
	othersTellMe = models.BooleanField(default=False, blank=True)
	noConnection = models.BooleanField(default=False, blank=True)
	otherConnectionsUsing = models.BooleanField(default=False, blank=True)
	connectionExplain = models.CharField(max_length=250, blank=True, null=True, default=None)

	##WORST EPISODE--------------------------------------------------------------------------
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

	##WITH WHOM YOU GET ANGRY----------------------------------------------------------------
	angryPartner = models.BooleanField(blank=True, default=False)
	angryParents = models.BooleanField(blank=True, default=False)
	angryChildren = models.BooleanField(blank=True, default=False)
	angryRelatives = models.BooleanField(blank=True, default=False)
	angryEmployer = models.BooleanField(blank=True, default=False)
	angryFriends = models.BooleanField(blank=True, default=False)
	angryOther = models.BooleanField(blank=True, default=False)
	otherWhom = models.CharField(max_length=25, default=True, blank=True, null=True)
	angryAbout = models.CharField(max_length=100, default=True, blank=True, null=True)
	seldomUpset = models.BooleanField(blank=True, default=False)

	##FAMILY OF ORIGIN-----------------------------------------------------------------------
	kidMomAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidDadAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidSiblingAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	kidOtherAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	learnFamilyAnger = models.CharField(max_length=100, default=None, blank=True, null=True)
	suicideHistory = models.BooleanField(blank=True, default=False)

	##ANY CURRENT PROBLEMS HISTORY OF--------------------------------------------------------
	brainInjury = models.BooleanField(blank=True, default=False)
	stroke = models.BooleanField(blank=True, default=False)
	epilepsy = models.BooleanField(blank=True, default=False)
	attentionDD = models.BooleanField(blank=True, default=False)
	pms = models.BooleanField(blank=True, default=False)
	depression = models.BooleanField(blank=True, default=False)
	ptsd = models.BooleanField(blank=True, default=False)
	otherSeriousIllness = models.BooleanField(blank=True, default=False)
	currentlyOnMeds = models.BooleanField(blank=True, default=False)
	whichMeds = models.CharField(max_length=100, default=True, blank=True, null=True)
	describeIssue = models.CharField(max_length=100, default=True, blank=True, null=True)

	##CONTROL--------------------------------------------------------------------------------
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

	##OTHER THINGS---------------------------------------------------------------------------
	anythingelse = models.CharField(max_length=250, default=None, blank=True, null=True)
	changeLearn1 = models.CharField(max_length=100, default=None, blank=True, null=True)
	changeLearn2 = models.CharField(max_length=100, default=None, blank=True, null=True)
	changeLearn3 = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __unicode__(self):
		return "Anger Management: " + str(self.client)




































