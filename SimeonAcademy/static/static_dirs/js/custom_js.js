function set_radio_buttons() {
	var ss_num = document.getElementById('ss_num');
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');
	var s_type = document.getElementById('s-type');

	s_type.value = 'name';

	ss_num.value = '';
	fname.value = '';
	lname.value = '';
	dob.value = '';
	client_ID.value = '';

	ss_num.disabled = true;
	fname.disabled = false;
	lname.disabled = false;
	dob.disabled = true;
	client_ID.disabled = true;

	ss_num.style.opacity = '0.5';
	fname.style.opacity = '1.0';
	lname.style.opacity = '1.0';
	dob.style.opacity = '0.5';
	client_ID.style.opacity = '0.5';
}

function processCheckbox(checkbox_element) {
	if (checkbox_element.checked === true) {
		checkbox_element.value = 'on';
	}
	else {
		checkbox_element.value = 'off';
	}
}

function processCheckboxPython(checkbox_element) {
	if (checkbox_element.checked === true) {
		checkbox_element.value = 'True';
	}
	else {
		checkbox_element.value = 'False';
	}
}

function processRadioYes(radioButton, postElement) {
	if (radioButton.checked === true) {
		postElement.value = 'True';
	}
	else {
		postElement.value = 'Fause';
	}
}


function copyElementToInput(element_name) {
	copiedElementName = 'm_';
	copiedElementName += element_name;

	var element_orig = document.getElementById(element_name);
	var element_copy = document.getElementById(copiedElementName);

	element_copy.value = element_orig.value;
}

function processDisabledTextFields(element, m_target) {
	if (element.disabled === true) {
		m_target.value = 'NA';
	}
	else {
		m_target.value = element.value;
	}
}

function processDisabledNumberFields(element, m_target) {
	if (element.disabled === true) {
		m_target.value = '0';
	}
	else {
		m_target.value = element.value;
	}
}

function updateSS() {
	var ss_num = document.getElementById('ss_num');
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');
	var s_type = document.getElementById('s-type');

	document.getElementById('error1').innerHTML = '';
	document.getElementById('error2').innerHTML = '';
	document.getElementById('error3').innerHTML = '';
	document.getElementById('error4').innerHTML = '';

	s_type.value = 'ss_num';

	ss_num.disabled = false;
	fname.disabled = true;
	lname.disabled = true;
	dob.disabled = true;
	client_ID.disabled = true;

	ss_num.style.opacity = '1.0';
	fname.style.opacity = '0.5';
	lname.style.opacity = '0.5';
	dob.style.opacity = '0.5';
	client_ID.style.opacity = '0.5';

	ss_num.value = '';
	fname.value = '';
	lname.value = '';
	dob.value = '';
	client_ID.value = '';
}

function updateName() {
	var ss_num = document.getElementById('ss_num');
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');
	var s_type = document.getElementById('s-type');

	document.getElementById('error1').innerHTML = '';
	document.getElementById('error2').innerHTML = '';
	document.getElementById('error3').innerHTML = '';
	document.getElementById('error4').innerHTML = '';

	s_type.value = 'name';

	ss_num.disabled = true;
	fname.disabled = false;
	lname.disabled = false;
	dob.disabled = true;
	client_ID.disabled = true;

	ss_num.style.opacity = '0.5';
	fname.style.opacity = '1.0';
	lname.style.opacity = '1.0';
	dob.style.opacity = '0.5';
	client_ID.style.opacity = '0.5';

	ss_num.value = '';
	fname.value = '';
	lname.value = '';
	dob.value = '';
	client_ID.value = '';
}

function updateDOB() {
	var ss_num = document.getElementById('ss_num')
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');
	var s_type = document.getElementById('s-type');

	document.getElementById('error1').innerHTML = '';
	document.getElementById('error2').innerHTML = '';
	document.getElementById('error3').innerHTML = '';
	document.getElementById('error4').innerHTML = '';

	s_type.value = 'dob';

	ss_num.disabled = true;
	fname.disabled = true;
	lname.disabled = true;
	dob.disabled = false;
	client_ID.disabled = true;

	ss_num.style.opacity = '0.5';
	fname.style.opacity = '0.5';
	lname.style.opacity = '0.5';
	dob.style.opacity = '1.0';
	client_ID.style.opacity = '0.5';

	ss_num.value = '';
	fname.value = '';
	lname.value = '';
	dob.value = '';
	client_ID.value = '';
}

function updateID() {
	var ss_num = document.getElementById('ss_num')
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');
	var s_type = document.getElementById('s-type');

	document.getElementById('error1').innerHTML = '';
	document.getElementById('error2').innerHTML = '';
	document.getElementById('error3').innerHTML = '';
	document.getElementById('error4').innerHTML = '';

	s_type.value = 'id';

	ss_num.disabled = true;
	fname.disabled = true;
	lname.disabled = true;
	dob.disabled = true;
	client_ID.disabled = false;

	ss_num.style.opacity = '0.5';
	fname.style.opacity = '0.5';
	lname.style.opacity = '0.5';
	dob.style.opacity = '0.5';
	client_ID.style.opacity = '1.0';

	ss_num.value = '';
	fname.value = '';
	lname.value = '';
	dob.value = '';
	client_ID.value = '';
}

function filterDOB() {
	var valid = true;
	var testString = false;	
	var dob = document.getElementById('dob').value;

	if (dob.length === 10) {
		testString = true;
	}
	else {
		valid = false;
	}

	if (testString === true) {
		for(var i = 0; i < dob.length; i++) {
			var c = dob.charAt(i);

			if (i===0 || i===1 || i===3 || i===4 || i==6 || i==7 || i==8 || i==9) {
				if (c==='0' || c==='1' || c==='2' || c==='3' || c==='4' || c==='5' || c==='6' || c==='7' || c==='8' || c==='9') {
					valid = true;
				}
				else {
					valid = false;
					break;
				}
			}
			else {
				if (c === '/') {
					valid = true;
				}
				else {
					valid = false;
					break;
				}
			}
		}
	}

	return valid;
}

function filterSS() {
	var valid = true;
	var testSS = false;
	var ss = document.getElementById('ss_num').value;

	if (ss.length === 11) {
		testSS = true;
	}
	else {
		valid = false;
	}

	if (testSS === true) {
		for (var i = 0; i < ss.length; i++) {
		var c = ss.charAt(i);

			if (i===0 || i===1 || i===2 || i===4 || i===5 || i===7 || i===8 || i===9 || i===10) {
				if (c==='0' || c==='1' || c==='2' || c==='3' || c==='4' || c==='5' || c==='6' || c==='7' || c==='8' || c==='9') {
					valid = true;
				}
				else {
					valid = false;
					break;
				}
			}
			else {
				if (c === '-') {
					valid = true;
				}
				else {
					valid = false;
					break;
				}
			}
		}
	}

	return valid;
}

function submit_session() {
	var name_radio = document.getElementById('name_radio');
	var dob_radio = document.getElementById('dob_radio');
	var id_radio = document.getElementById('id_radio');
	var ss_radio = document.getElementById('ss_radio');
	var stype = document.getElementById('stype');
	var proceed = false;

	if (name_radio.checked === true) 
	{
		var fname = document.getElementById('fname');
		var lname = document.getElementById('lname');

		if (fname.value === '' || fname.value === null || lname.value === '' || lname.value === null || fname.value === ' ' || lname.value === ' ') 
		{
			document.getElementById('error1').innerHTML = '*YOU MUST ENTER A VALID NAME';
			proceed = false;
		}
		else {proceed = true;}		
	}
	else if (dob_radio.checked === true)
	{
		var dob = document.getElementById('dob');
		var valid = filterDOB();

		if (dob.value === '' || dob.value === ' ' || dob.value === null)
		{
			document.getElementById('error2').innerHTML = '*YOU MUST ENTER A VALID BIRTHDATE';
			proceed = false;
		}
		else if (valid === false)
		{
			document.getElementById('error2').innerHTML = '*DATE MUST BE IN THE FORM MM/DD/YYYY';
			proceed = false;
		}
		else {proceed = true;}
	}
	else if (ss_radio.checked === true)
	{
		var ss_num = document.getElementById('ss_num');
		var validSS = filterSS();

		if (ss_num.value === '' || ss_num.value === ' ' || ss_num.value === null) 
		{
			document.getElementById('error3').innerHTML = '*YOU MUST ENTER A VALID SOCIAL SECURITY NUMBER';
			proceed = false;
		}
		else if (validSS === false) {
			document.getElementById('error3').innerHTML = '*SOCIAL SECURITY NUMBER MUST BE N THE FORM XXX-XX-XXXX';
			proceed = false;
		}
		else {proceed = true;}
	}
	else if (id_radio.checked === true)
	{
		var client_id = document.getElementById('client_ID');

		if (client_id.value === '' || client_id.value === ' ' || client_id.value === null)
		{
			document.getElementById('error4').innerHTML = '*YOU MUST ENTER A VALID CLIENT ID';
			proceed = false;
		}
		else {proceed = true;}
	}

	if (stype.value === 'choose') {
		document.getElementById('error5').innerHTML = '*YOU MUST CHOOSE A SESSION TYPE TO PROCEDE';
		proceed = false;
	}
	else {proceed = true;}


	if (proceed === true) {
		document.getElementById('client-search').submit();
	}
}

function toClientOptions(form_id) {
	document.getElementById(form_id).submit();
}

function new_am() {
	document.getElementById('am').submit();
}

function new_asi() {
	document.getElementById('asi').submit();
}

function new_mh() {
	document.getElementById('mh').submit();
}

function new_sap() {
	document.getElementById('sap').submit();
}

function new_ut() {
	document.getElementById('ut').submit();
}

function discharge() {
	document.getElementById('discharge').submit();
}

function goBackPage(back_url) {
	var form = document.getElementById('am_demo');
	form.action = back_url;
	form.submit();
}

function hideToggle() {
	var btn = document.getElementById('my_toggle_btn1');

	if (btn.innerHTML === "Show Details") {
		btn.innerHTML = "Hide Details";
	}
	else if (btn.innerHTML === "Hide Details") {
		btn.innerHTML = "Show Details";
	}
}

function clearNullTextField(element) {
	if (element.value === null) {
		element.value = '';
	}
	return element.value;
}

function clearNullTextArea(element) {
	if (element.innerHTML === null) {
		element.innerHTML = '';
	}
	return element.innerHTML;
}



// AM CONNECTIONS FUNCTIONS
function connectionCheck() {
	var explain = document.getElementById('connectionExplain');
	var label = document.getElementById('explain_label');

	if (document.getElementById('otherConnectionsUsing').checked === true) {
		explain.disabled = false;
		explain.style.opacity = "1.0";
		label.style.opacity = "1.0";
	}

	else {
		explain.disabled = true;
		explain.style.opacity = "0.5";
		label.style.opacity = "0.5";
		explain.innerHTML = '';
	}
}

function initalize_am_connections(json_data) {
	var angerWorse = document.getElementById('angerWorse');
	var troubleWhenUsing = document.getElementById('troubleWhenUsing');
	var lessAngry = document.getElementById('lessAngry');
	var othersTellMe = document.getElementById('othersTellMe');
	var noConnection = document.getElementById('noConnection');
	var otherConnectionsUsing = document.getElementById('otherConnectionsUsing');
	var connectionExplain = document.getElementById('connectionExplain');

	angerWorse.checked = json_data.angerWorse;
	troubleWhenUsing.checked = json_data.troubleWhenUsing;
	lessAngry.checked = json_data.lessAngry;
	othersTellMe.checked = json_data.othersTellMe;
	noConnection.checked = json_data.noConnection;
	otherConnectionsUsing.checked = json_data.otherConnectionsUsing;

	connectionCheck();

	if (otherConnectionsUsing.checked === true) {
		connectionExplain.innerHTML = json_data.connectionExplain;
	}
}

function continue_to_worst() {
	var proceed = true;
	var angerWorse = document.getElementById('angerWorse');
	var troubleWhenUsing = document.getElementById('troubleWhenUsing');
	var lessAngry = document.getElementById('lessAngry');
	var othersTellMe = document.getElementById('othersTellMe');
	var noConnection = document.getElementById('noConnection');
	var otherConnectionsUsing = document.getElementById('otherConnectionsUsing');
	var connectionExplain = document.getElementById('connectionExplain');

	processCheckbox(angerWorse);
	processCheckbox(troubleWhenUsing);
	processCheckbox(lessAngry);
	processCheckbox(othersTellMe);
	processCheckbox(noConnection);
	processCheckbox(otherConnectionsUsing);

	copyElementToInput('angerWorse');
	copyElementToInput('troubleWhenUsing');
	copyElementToInput('lessAngry');
	copyElementToInput('othersTellMe');
	copyElementToInput('noConnection');
	copyElementToInput('otherConnectionsUsing');
	copyElementToInput('connectionExplain');

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

// AM WORST EPISODES FUNCTIONS
function worstCheck() {
	var description = document.getElementById('otherWorstDescription');

	if (document.getElementById('otherWorst').checked === true) {
		description.style.opacity = "1.0";
		description.disabled = false;
	}
	else {
		description.style.opacity = '0';
		description.disabled = true;
	}
}

function activateWorstRadio() {
	var selectBox = document.getElementById('whoDidItFight');
	var label = document.getElementById('whoDidItFight_label');

	if (document.getElementById('hadDrugs').checked === true) {
		label.style.opacity = '1.0';
		selectBox.style.opacity = '1.0';
		selectBox.disabled = false;
	}

	if (document.getElementById('noDrugs').checked === true) {
		label.style.opacity = '0.5';
		selectBox.style.opacity = '0.5';
		selectBox.disabled = true;
	}
}

function initalize_am_worst(json_data) {
	var whoWorst = document.getElementById('whoWorst');
	var happenedWorst = document.getElementById('happenedWorst');
	var wordThoughtWorst = document.getElementById('wordThoughtWorst');
	var howStartWorst = document.getElementById('howStartWorst');
	var howEndWorst = document.getElementById('howEndWorst');
	var whoDidItFight = document.getElementById('whoDidItFight');
	var theyUsedWorst = document.getElementById('theyUsedWorst');
	var physicalWorst = document.getElementById('physicalWorst');
	var verbalWorst = document.getElementById('verbalWorst');
	var threatsWorst = document.getElementById('threatsWorst');
	var propertyWorst = document.getElementById('propertyWorst');
	var otherWorst = document.getElementById('otherWorst');
	var otherWorstDescription = document.getElementById('otherWorstDescription');

	var hadDrugs = document.getElementById('hadDrugs');
	var noDrugs = document.getElementById('noDrugs');

	if (json_data.useWorst === true) {
		hadDrugs.checked = true;
	}
	else {
		noDrugs.checked = true;
	}

	if (String(json_data.whoDidItFight) === 'not selected' || json_data.whoDidItFight === null) {
		whoDidItFight.selectedIndex = 0;
	}
	else if (String(json_data.whoDidItFight) === 'client used only') {
		whoDidItFight.selectedIndex = 1;
	}
	else if (String(json_data.whoDidItFight) === 'other party used only') {
		whoDidItFight.selectedIndex = 2;
	}
	else {
		whoDidItFight.selectedIndex = 3;
	}

	whoWorst.innerHTML = json_data.whoWorst;
	happenedWorst.innerHTML = json_data.happenedWorst;
	wordThoughtWorst.innerHTML = json_data.wordThoughtWorst;
	howStartWorst.innerHTML = json_data.howStartWorst;
	howEndWorst.innerHTML = json_data.howEndWorst;

	physicalWorst.checked = json_data.physicalWorst;
	verbalWorst.checked = json_data.verbalWorst;
	threatsWorst.checked = json_data.threatsWorst;
	propertyWorst.checked = json_data.propertyWorst;
	otherWorst.checked = json_data.otherWorst;

	worstCheck();
	activateWorstRadio();

	if (otherWorst.checked === true) {
		otherWorstDescription.innerHTML = json_data.otherWorstDescription;
	}
}

function continue_to_target() {
	var proceed = true;
	var whoWorst = document.getElementById('whoWorst');
	var happenedWorst = document.getElementById('happenedWorst');
	var wordThoughtWorst = document.getElementById('wordThoughtWorst');
	var howStartWorst = document.getElementById('howStartWorst');
	var howEndWorst = document.getElementById('howEndWorst');
	var hadDrugs = document.getElementById('hadDrugs');
	var whoDidItFight = document.getElementById('whoDidItFight');
	var physicalWorst = document.getElementById('physicalWorst');
	var verbalWorst = document.getElementById('verbalWorst');
	var threatsWorst = document.getElementById('threatsWorst');
	var propertyWorst = document.getElementById('propertyWorst');
	var otherWorst = document.getElementById('otherWorst');
	var otherWorstDescription = document.getElementById('otherWorstDescription');

	var useWorst = document.getElementById('m_useWorst');
	var descriptOUT = document.getElementById('m_otherWorstDescription');

	processCheckbox(physicalWorst);
	processCheckbox(verbalWorst);
	processCheckbox(threatsWorst);
	processCheckbox(propertyWorst);
	processCheckbox(otherWorst);

	if (hadDrugs.checked === true) {
		useWorst.value = "True";
	}
	else {
		useWorst.value = "False";
	}

	if (otherWorst.checked === true) {
		copyElementToInput('otherWorstDescription');
	}
	else {
		descriptOUT.value = 'NA';
	}

	whoDidItFight.value = whoDidItFight.options[whoDidItFight.selectedIndex].value;

	copyElementToInput('whoWorst');
	copyElementToInput('happenedWorst');
	copyElementToInput('wordThoughtWorst');
	copyElementToInput('howStartWorst');
	copyElementToInput('howEndWorst');
	copyElementToInput('whoDidItFight');
	copyElementToInput('physicalWorst');
	copyElementToInput('verbalWorst');
	copyElementToInput('threatsWorst');
	copyElementToInput('propertyWorst');
	copyElementToInput('otherWorst');

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}


// AM TARGET FUNCTIONS
function amTargetOther() {
	otherWhom = document.getElementById('otherWhom');

	if(document.getElementById('angryOther').checked === true) {
		otherWhom.disabled = false;
		otherWhom.style.opacity = '1.0';
	}
	else {
		otherWhom.disabled = true;
		otherWhom.style.opacity = '0';
	}
}

function initalize_am_target(json_data) {
	var angryPartner = document.getElementById('angryPartner');
	var angryParents = document.getElementById('angryParents');
	var angryChildren = document.getElementById('angryChildren');
	var angryRelatives = document.getElementById('angryRelatives');
	var angryEmployer = document.getElementById('angryEmployer');
	var angryFriends = document.getElementById('angryFriends');
	var angryOther = document.getElementById('angryOther');
	var otherWhom = document.getElementById('otherWhom');
	var angryAbout = document.getElementById('angryAbout');
	var seldomUpset = document.getElementById('seldomUpset');

	angryPartner.checked = json_data.angryPartner;
	angryParents.checked = json_data.angryParents;
	angryChildren.checked = json_data.angryChildren;
	angryRelatives.checked = json_data.angryRelatives;
	angryEmployer.checked = json_data.angryEmployer;
	angryFriends.checked = json_data.angryFriends;
	angryOther.checked = json_data.angryOther;
	seldomUpset.checked = json_data.seldomUpset;

	amTargetOther();

	if (angryOther.checked === true) {
		otherWhom.value = json_data.otherWhom;
	}

	angryAbout.innerHTML = json_data.angryAbout;
}

function continue_to_am_family() {
	var proceed = true;
	var angryPartner = document.getElementById('angryPartner');
	var angryParents = document.getElementById('angryParents');
	var angryChildren = document.getElementById('angryChildren');
	var angryRelatives = document.getElementById('angryRelatives');
	var angryEmployer = document.getElementById('angryEmployer');
	var angryFriends = document.getElementById('angryFriends');
	var angryOther = document.getElementById('angryOther');
	var otherWhom = document.getElementById('otherWhom');
	var angryAbout = document.getElementById('angryAbout');
	var seldomUpset = document.getElementById('seldomUpset');

	processCheckbox(angryPartner);
	processCheckbox(angryParents);
	processCheckbox(angryChildren);
	processCheckbox(angryRelatives);
	processCheckbox(angryEmployer);
	processCheckbox(angryFriends);
	processCheckbox(angryOther);
	processCheckbox(seldomUpset);

	if (angryOther.checked === false) {
		document.getElementById('m_otherWhom').value = 'NA';
	}
	else {
		copyElementToInput('otherWhom');
	}

	//ERROR CHECKING...

	copyElementToInput('angryPartner');
	copyElementToInput('angryParents');
	copyElementToInput('angryChildren');
	copyElementToInput('angryRelatives');
	copyElementToInput('angryEmployer');
	copyElementToInput('angryFriends');
	copyElementToInput('angryOther');	
	copyElementToInput('angryAbout');
	copyElementToInput('seldomUpset');

	
	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}


// AM FAMILY OF ORIGIN FUNCTIONS
function initalize_family_origin(json_data) {
	kidMomAnger = document.getElementById('kidMomAnger');
	kidDadAnger = document.getElementById('kidDadAnger');
	kidSiblingAnger = document.getElementById('kidSiblingAnger');
	kidOtherAnger = document.getElementById('kidOtherAnger');
	learnFamilyAnger = document.getElementById('learnFamilyAnger');
	hasSuicide = document.getElementById('hasSuicide');
	noSuicide = document.getElementById('noSuicide');
	hasLovingMother = document.getElementById('hasLovingMother');
	hasLovingSiblings = document.getElementById('hasLovingSiblings');

	if (json_data.suicideHistory === true) {
		hasSuicide.checked = true;
	}
	else {
		noSuicide.checked = true;
	}


	if (json_data.kidMomAnger !== null) {
		kidMomAnger.value = json_data.kidMomAnger
	}

	if (json_data.kidDadAnger !== null) {
		kidDadAnger.value = json_data.kidDadAnger
	}

	if (json_data.kidSiblingAnger !== null) {
		kidSiblingAnger.value = json_data.kidSiblingAnger
	}

	if (json_data.kidOtherAnger !== null) {
		kidOtherAnger.value = json_data.kidOtherAnger
	}

	if (json_data.learnFamilyAnger !== null) {
		learnFamilyAnger.value = json_data.learnFamilyAnger
	}

	hasLovingMother.checked = json_data.hasLovingMother
	hasLovingSiblings.checked = json_data.hasLovingSiblings
}

function continue_to_am_problems() {
	var proceed = true;
	var kidMomAnger = document.getElementById('kidMomAnger');
	var kidDadAnger = document.getElementById('kidDadAnger');
	var kidSiblingAnger = document.getElementById('kidSiblingAnger');
	var kidOtherAnger = document.getElementById('kidOtherAnger');
	var learnFamilyAnger = document.getElementById('learnFamilyAnger');
	var hasSuicide = document.getElementById('hasSuicide');
	var hasLovingMother = document.getElementById('hasLovingMother');
	var hasLovingSiblings = document.getElementById('hasLovingSiblings');

	//PROCESS CHECKBOXES
	processCheckbox(hasLovingMother);
	processCheckbox(hasLovingSiblings);

	//PROCESS RADIO BUTTONS
	if (hasSuicide.checked === true) {
		document.getElementById('m_suicideHistory').value = 'True';
	}
	else {
		document.getElementById('m_suicideHistory').value = 'False';
	}

	//COPY OUTPUT FIELDS
	copyElementToInput('kidMomAnger');
	copyElementToInput('kidDadAnger');
	copyElementToInput('kidSiblingAnger');
	copyElementToInput('kidOtherAnger');
	copyElementToInput('learnFamilyAnger');
	copyElementToInput('hasLovingMother');
	copyElementToInput('hasLovingSiblings');
	
	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

//AM CURRENT PROBLEMS FUNCTIONS
function am_problems_check() {
	var label = document.getElementById('other_label');
	var box = document.getElementById('describeIssue');

	if (document.getElementById('otherSeriousIllness').checked === true) {
		label.style.opacity = '1.0';
		box.style.opacity = '1.0';
		box.disabled = false;
	}
	else {
		label.style.opacity = '0';
		box.style.opacity = '0';
		box.disabled = true;
	}
}

function am_problems_radio() {
	var label = document.getElementById('taking_meds_label');
	var box = document.getElementById('whichMeds');

	if (document.getElementById('onMeds').checked === true) {
		label.style.opacity = '1.0';
		box.style.opacity = '1.0';
		box.disabled = false;
	}

	if (document.getElementById('noMeds').checked === true) {
		label.style.opacity = '0.5';
		box.style.opacity = '0.5';
		box.disabled = true;
	}
}

function initalize_am_problems(json_data) {
	var brainInjury = document.getElementById('brainInjury');
	var stroke = document.getElementById('stroke');
	var epilepsy = document.getElementById('epilepsy');
	var attentionDD = document.getElementById('attentionDD');
	var pms = document.getElementById('pms');
	var depression = document.getElementById('depression');
	var ptsd = document.getElementById('ptsd');
	var otherSeriousIllness = document.getElementById('otherSeriousIllness');
	var whichMeds = document.getElementById('whichMeds');
	var describeIssue = document.getElementById('describeIssue');

	var onMeds = document.getElementById('onMeds');
	var noMeds = document.getElementById('noMeds');

	if (json_data.currentlyOnMeds === true) {
		onMeds.checked = true;
	}
	else {
		noMeds.checked = true;
	}

	brainInjury.checked = json_data.brainInjury;
	stroke.checked = json_data.stroke;
	epilepsy.checked = json_data.epilepsy;
	attentionDD.checked = json_data.attentionDD;
	pms.checked = json_data.pms;
	depression.checked = json_data.depression;
	ptsd.checked = json_data.ptsd;
	otherSeriousIllness.checked = json_data.otherSeriousIllness;

	am_problems_check();
	am_problems_radio();

	if (json_data.otherSeriousIllness === true) {
		describeIssue.innerHTML = json_data.describeIssue;
	}

	if (json_data.currentlyOnMeds === true) {
		whichMeds.innerHTML = json_data.whichMeds;
	}
}

function continue_to_am_control() {
	var proceed = true;
	var brainInjury = document.getElementById('brainInjury');
	var stroke = document.getElementById('stroke');
	var epilepsy = document.getElementById('epilepsy');
	var attentionDD = document.getElementById('attentionDD');
	var pms = document.getElementById('pms');
	var depression = document.getElementById('depression');
	var ptsd = document.getElementById('ptsd');
	var otherSeriousIllness = document.getElementById('otherSeriousIllness');
	var onMeds = document.getElementById('onMeds');
	var whichMeds = document.getElementById('whichMeds');
	var describeIssue = document.getElementById('describeIssue');

	//PROCESS RADIO BUTTONS
	if (onMeds.checked === true) {
		document.getElementById('m_currentlyOnMeds').value = 'True';
		copyElementToInput('whichMeds')
	}
	else {
		document.getElementById('m_currentlyOnMeds').value = 'False';
		document.getElementById('m_whichMeds').value = 'NA';
	}

	//PROCESS DYNAMIC FIELDS
	if (otherSeriousIllness.checked === false) {
		document.getElementById('m_describeIssue').value = 'NA';
	}
	else {
		copyElementToInput('describeIssue');
	}

	//PROCESS CHECKBOXES
	processCheckboxPython(brainInjury);
	processCheckboxPython(stroke);
	processCheckboxPython(epilepsy);
	processCheckboxPython(attentionDD);
	processCheckboxPython(pms);
	processCheckboxPython(depression);
	processCheckboxPython(ptsd);
	processCheckboxPython(otherSeriousIllness);

	//ERROR CHECKING...

	//PROCESS HIDDEN POST INPUTS
	copyElementToInput('brainInjury');
	copyElementToInput('stroke');
	copyElementToInput('epilepsy');
	copyElementToInput('attentionDD');
	copyElementToInput('pms');
	copyElementToInput('depression');
	copyElementToInput('ptsd');
	copyElementToInput('otherSeriousIllness');


	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}


// AM CHILDHOOD FUNCTIONS
function continue_am_history1() {
	document.getElementById('am_demo').submit();
}



// AM ANGER/VIOLENCE HISTORY FUNCTIONS
function continue_to_am_connections() {
	document.getElementById('am_demo').submit();
}




// AM DEMOGRAPHIC FUNCTIONS
function initialize_am_demo(json_data, back) {
	var rent_radio = document.getElementById('rent_radio');
	var own_radio = document.getElementById('own_radio');
	var hs_grad = document.getElementById('hs_grad');
	var hs_drop = document.getElementById('hs_drop');
	var healthy = document.getElementById('healthy');
	var not_healthy = document.getElementById('not_healthy');
	var no_med = document.getElementById('no_med');
	var on_meds = document.getElementById('on_meds');

	if (String(json_data.own) == 'false') {
		rent_radio.checked = true;
	}
	else {own_radio.checked = true;}

	if (String(json_data.drop_out) == 'false') {
		hs_grad.checked = true;
	}
	else {hs_drop.checked = true;}

	if (String(json_data.health_problem) == 'false') {
		healthy.checked = true;
		health_options_off();
	}
	else {
		not_healthy.checked = true;
		health_options_on();
		document.getElementById('explain').innerHTML = json_data.health_exp;
	}

	if (String(json_data.medication) == 'false') {
		no_med.checked = true;
	}
	else {
		on_meds.checked = true;
	}

	var marital = document.getElementById('marital');
	var living = document.getElementById('living');
	var edu = document.getElementById('edu');

	marital.selectedIndex = String(json_data.maritalStatus);
	living.selectedIndex = String(json_data.livingSituation);
	edu.selectedIndex = String(json_data.education);

	if (String(back) === 'false') {
		document.getElementById('occ').value = '';
		document.getElementById('employer').value = '';
		document.getElementById('em_add').value = '';
		document.getElementById('em_phone').value = '';
	}
}

function health_options_on() {
	var explain = document.getElementById('explain');
	var explain_label = document.getElementById('explain-label')
	var med_label = document.getElementById('med-label');
	var no_med_label = document.getElementById('no_med_label');
	var yes_med_label = document.getElementById('yes_med_label');
	var med_taking_label = document.getElementById('med_taking_label');
	var no_med = document.getElementById('no_med');
	var on_meds = document.getElementById('on_meds');

	explain.disabled = false;
	no_med.disabled = false;
	on_meds.disabled = false;

	explain_label.style.opacity = '1.0';
	no_med_label.style.opacity = '1.0';
	yes_med_label.style.opacity = '1.0';
	med_taking_label.style.opacity = '1.0';
}

function health_options_off() {
	var explain = document.getElementById('explain');
	var explain_label = document.getElementById('explain-label')
	var med_label = document.getElementById('med-label');
	var no_med_label = document.getElementById('no_med_label');
	var yes_med_label = document.getElementById('yes_med_label');
	var med_taking_label = document.getElementById('med_taking_label');
	var no_med = document.getElementById('no_med');
	var on_meds = document.getElementById('on_meds');

	explain.disabled = true;
	no_med.disabled = true;
	on_meds.disabled = true;

	explain_label.style.opacity = '0.3';
	no_med_label.style.opacity = '0.3';
	yes_med_label.style.opacity = '0.3';
	med_taking_label.style.opacity = '0.3';

	explain.value = '';
	no_med.checked = true;
}

function continue_am() {
	var marital = document.getElementById('marital');
	var living = document.getElementById('living');
	var res_mos = document.getElementById('res-mos');
	var res_yrs = document.getElementById('res-yrs');
	var children = document.getElementById('dep_children');
	var others = document.getElementById('dep_other');
	var edu = document.getElementById('edu');
	var occ = document.getElementById('occ');
	var employer = document.getElementById('employer');
	var emp_add = document.getElementById('em_add');
	var em_phone = document.getElementById('em_phone');
	var mosJob = document.getElementById('mosJob');
	var yrsJob = document.getElementById('yrsJob');
	var healthy = document.getElementById('healthy');
	var explain = document.getElementById('explain');
	var error_msg = document.getElementById('error_message_main');
	var proceed = true;

	if (marital.selectedIndex === 0) {
		error_msg.innerHTML = 'You must choose a marital status';
		proceed = false;
	}
	else if (living.selectedIndex === 0) {
		error_msg.innerHTML = 'You must choose a living situation';
		proceed = false;
	}
	else if (edu.selectedIndex === 0) {
		error_msg.innerHTML = 'You must choose a level of education';
		proceed = false;
	}
	else if (res_mos.value ==='' || res_mos.value === null || res_mos.value === ' ') {
		error_msg.innerHTML = 'Months at residence field cannot be blank (Enter 0 if there are zero months at residence)';
		proceed = false;
	}
	else if (res_yrs.value ==='' || res_yrs.value === null || res_yrs.value === ' ') {
		error_msg.innerHTML = 'Years at residence field cannot be blank (Enter 0 if there are zero years at residence)';
		proceed = false;
	}
	else if (children.value ==='' || children.value === null || children.value === ' ') {
		error_msg.innerHTML = '"Children" field cannot be blank (Enter 0 if there are zero months at residence)';
		proceed = false;
	}
	else if (others.value ==='' || others.value === null || others.value === ' ') {
		error_msg.innerHTML = '"Other dependents" field cannot be blank (Enter 0 if there are zero years at residence)';
		proceed = false;
	}
	else if (mosJob.value ==='' || mosJob.value === null || mosJob.value === ' ') {
		error_msg.innerHTML = 'Months at employer field cannot be blank (Enter 0 if there are zero months at residence)';
		proceed = false;
	}
	else if (yrsJob.value ==='' || yrsJob.value === null || yrsJob.value === ' ') {
		error_msg.innerHTML = 'Months at employer field cannot be blank (Enter 0 if there are zero years at residence)';
		proceed = false;
	}

	if (healthy.checked == false) {
		if (explain.value === '' || explain.value === ' ' || explain.value === null) {
			error_msg.innerHTML = 'You have indicated that this client currently has health issues. The explaination cannot be left blank';
			proceed = false;
		}
		else {proceed === true;}
	}

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

function continue_am_dh() {
	proceed = true;

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

function back(back_url) {
	var form = document.getElementById('am_demo');
	document.getElementById('back').value = true;
	form.action = back_url;
	document.getElementById('am_demo').submit();
}

function defineRadio(yesElement, NoElement, m_value) {
	if (m_value === true) {
		yesElement.checked = true;
	}
	else {
		NoElement.checked = true;
	}
}

function treatNullTextFields(element, json_value) {
	if (json_value === null) {
		element.value = '';
	}
	else {
		element.value = json_value;
	}
}

function treatNullAreaFields(element, json_value) {
	if (json_value === null) {
		element.innerHTML = '';
	}
	else {
		element.innerHTML = json_value;
	}
}

function treatNumberFields(element, json_value) {
	if (Number.isInteger(json_value) === true && json_value > 0) {
		element.value = json_value
	}
	else {
		element.value = 0;
	}
}

function toggleUseAlcoholRadio() {
	var current_use = document.getElementById('current_use');
	var no_current_use = document.getElementById('no_current_use');
	var first_use_type = document.getElementById('how-much-you-use');	
	var what_you_use = document.getElementById('what-you-use');
	var how_often_you_use = document.getElementById('how-often-you-use');
	var what_use_label = document.getElementById('what_use_label');
	var how_often_label = document.getElementById('how_often_label');
	var how_much_use_label = document.getElementById('how_much_use_label');

	if (current_use.checked === true) {
		what_you_use.disabled = false;
		how_often_you_use.disabled = false;
		first_use_type.disabled = false;

		what_use_label.style.opacity = '1.0';
		how_often_label.style.opacity = '1.0';
		how_much_use_label.style.opacity = '1.0';
	}

	else {
		what_you_use.disabled = true;
		how_often_you_use.disabled = true;
		first_use_type.disabled = true;

		what_use_label.style.opacity = '0.5';
		how_often_label.style.opacity = '0.5';
		how_much_use_label.style.opacity = '0.5';
	}
}

function initializeDUIRadio() {
	var dui = document.getElementById('dui'); //has DUI
	var BAL = document.getElementById('BAL');
	var dui_amount = document.getElementById('dui_amount');
	var dui_amount_label = document.getElementById('dui_amount_label');
	var bal_label = document.getElementById('bal_label');

	if (dui.checked === false) {
		dui_amount_label.style.opacity = '0.5';
		bal_label.style.opacity = '0.5';

		BAL.disabled = true;
		dui_amount.disabled = true;
	}

	else {
		dui_amount_label.style.opacity = '1.0';
		bal_label.style.opacity = '1.0';

		BAL.disabled = false;
		dui_amount.disabled = false;
	}
}

function toggleEverDrankRadio() {
	var has_used = document.getElementById('has_used');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');
	var reason_quit = document.getElementById('reason_quit');
	var reason_quit_label = document.getElementById('reason-quit-label');
	var moLabel1 = document.getElementById('moLabel1');
	var yrLabel1 = document.getElementById('yrLabel1');
	var label = document.getElementById('quit-label');

	if (has_used.checked === true) {
		quitMos.disabled = false;
		quitYrs.disabled = false;
		reason_quit.disabled = false;

		reason_quit_label.style.opacity = '1.0';
		moLabel1.style.opacity = '1.0';
		yrLabel1.style.opacity = '1.0';
		label.style.opacity = '1.0';
	}

	else {
		quitMos.disabled = true;
		quitYrs.disabled = true;
		reason_quit.disabled = true;

		reason_quit_label.style.opacity = '0.5';
		moLabel1.style.opacity = '0.5';
		yrLabel1.style.opacity = '0.5';
		label.style.opacity = '0.5';
	}
}

function initializeTreatmentRadio() {
	var had_treatment = document.getElementById('had_treatment');
	var no_treatment = document.getElementById('no_treatment');

	var when_treated_label = document.getElementById('when_treated_label');
	var where_treated_label = document.getElementById('where_treated_label');
	var completed_treatment_label = document.getElementById('completed_treatment_label');
	var did_complete_label = document.getElementById('did_complete_label');
	var not_completed_label = document.getElementById('not_completed_label');

	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');
	var did_complete = document.getElementById('did_complete');
	var not_completed = document.getElementById('not_completed');

	if (no_treatment.checked === true) {
		when_treated_label.style.opacity = '0.5';
		where_treated_label.style.opacity = '0.5';
		completed_treatment_label.style.opacity = '0.5';
		did_complete_label.style.opacity = '0.5';
		not_completed_label.style.opacity = '0.5';

		when_treated.disabled = true;
		where_treated.disabled = true;
		did_complete.disabled = true;
		not_completed.disabled = true;
	}

	else {
		when_treated_label.style.opacity = '1.0';
		where_treated_label.style.opacity = '1.0';
		completed_treatment_label.style.opacity = '1.0';
		did_complete_label.style.opacity = '1.0';
		not_completed_label.style.opacity = '1.0';

		when_treated.disabled = false;
		where_treated.disabled = false;
		did_complete.disabled = false;
		not_completed.disabled = false;
	}
}

function initializeRadioSub1() {
	var had_treatment = document.getElementById('did_complete');

	var not_abstinent = document.getElementById('not_abstinent');
	var is_abstinent = document.getElementById('is_abstinent');
	var no_treat_explain = document.getElementById('no_treat_explain');

	var no_complete_explain_label = document.getElementById('no_complete_explain_label');
	var still_abstinent_label = document.getElementById('still_abstinent_label');
	var is_abstinent_label = document.getElementById('is_abstinent_label');
	var not_abstinent_label = document.getElementById('not_abstinent_label');

	if (had_treatment.checked === true) {
		no_complete_explain_label.style.opacity = '0.5';
		still_abstinent_label.style.opacity = '0.5';
		is_abstinent_label.style.opacity = '0.5';
		not_abstinent_label.style.opacity = '0.5';

		not_abstinent.disabled = true;
		is_abstinent.disabled = true;
		no_treat_explain.disabled = true;
	}
}

function initializeSoberRadio() {
	var not_abstinent = document.getElementById('not_abstinent');
	var trigger_label = document.getElementById('trigger_label');
	var relapse_explain = document.getElementById('relapse_explain');

	if (not_abstinent.checked === false) {
		trigger_label.style.opacity = '0.5';
		relapse_explain.disabled = true;
	}
	else {
		trigger_label.style.opacity = '1.0';
		relapse_explain.disabled = false;
	}
}

function am_drug_history_initialize(json_data, back) {
	var no_current_use = document.getElementById('no_current_use');
	var current_use = document.getElementById('current_use');
	var never_used = document.getElementById('never_used');
	var has_used = document.getElementById('has_used');
	var no_dui = document.getElementById('no_dui');
	var dui = document.getElementById('dui');
	var give_me_help = document.getElementById('give_me_help');
	var no_help = document.getElementById('no_help');
	var had_treatment = document.getElementById('had_treatment');
	var no_treatment = document.getElementById('no_treatment');
	var did_complete = document.getElementById('did_complete');
	var not_completed = document.getElementById('not_completed');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');
	var was_drinking = document.getElementById('was_drinking');
	var not_drinking = document.getElementById('not_drinking');
	var is_problem = document.getElementById('is_problem');
	var no_problem = document.getElementById('no_problem');

	if ( String(json_data.curUse) === 'true') {
		current_use.checked = true;
		dh_drinks();
	}
	else {
		no_current_use.checked = true;
		dh_no_drink();
	}

	if ( String(json_data.everDrank) === 'true') {
		has_used.checked = true;
		dh_has_used();
	}
	else {
		never_used.checked = true;
		dh_never_used();
	}

	if ( String(json_data.DUI) === 'true') {
		dui.checked = true;
		dh_has_dui();
	}
	else {
		no_dui.checked = true;
		dh_no_dui();
	}

	if ( String(json_data.needHelpDrugs) === 'true') {
		give_me_help.checked = true;
	}
	else {
		no_help.checked = true;
	}

	if ( String(json_data.drugTreatment) === 'true') {
		had_treatment.checked = true;
		dh_had_treatment();
	}
	else {
		no_treatment.checked = true;
		dh_no_treatment();
	}

	if ( String(json_data.finishedTreatment) === 'true') {
		did_complete.checked = true;
		// dh_did_completed_sub();
	}
	else {
		not_completed.checked = true;
		// dh_not_completed_sub();
	}

	if ( String(json_data.isClean) === 'true') {
		is_abstinent.checked = true;
		// dh_is_abstinent();
	}
	else {
		not_abstinent.checked = true;
		// dh_not_abstinent();
	}

	if ( String(json_data.drinkLastEpisode) === 'true') {
		was_drinking.checked = true;
	}
	else {
		not_drinking.checked = true;
	}

	if ( String(json_data.drinkRelationshipProblem) === 'true') {
		is_problem.checked = true;
	}
	else {
		no_problem.checked = true;
	}

	if (String(back) === 'false') {
		document.getElementById('first_use_type').value = '';
		document.getElementById('what-you-use').value = '';
		document.getElementById('how-often-you-use').value = '';
		document.getElementById('how-much-you-use').value = '';
		document.getElementById('reason_quit').value = '';
		document.getElementById('BAL').value = '';
		document.getElementById('when_treated').value = '';
		document.getElementById('where_treated').value = '';
		document.getElementById('no_treat_explain').innerHTML = '';
		document.getElementById('relapse_explain').innerHTML = '';
	}
	else {
		document.getElementById('first_drink').value = json_data.firstDrinkAge;
		document.getElementById('first_use_type').value = json_data.firstDrinkType;
		document.getElementById('what-you-use').value = json_data.useType;
		document.getElementById('how-often-you-use').value = json_data.amtPerWeek;
		document.getElementById('how-much-you-use').value = json_data.useAmt;
		document.getElementById('quitMos').value = json_data.monthsQuit;
		document.getElementById('quitYrs').value = json_data.yearsQuit;
		document.getElementById('reason_quit').value = json_data.reasonQuit;
		document.getElementById('dui_amount').value = json_data.numDUI;
		document.getElementById('BAL').value = json_data.BALevel;
		document.getElementById('when_treated').value = json_data.dateTreated;
		document.getElementById('where_treated').value = json_data.treatmentPlace;
		document.getElementById('no_treat_explain').innerHTML = json_data.reasonNotFinishedTreatment;
		document.getElementById('relapse_explain').innerHTML = json_data.relapseTrigger;
	}

	document.getElementById('first_use_type').value = clearNullTextField(document.getElementById('first_use_type'));
	document.getElementById('what-you-use').value = clearNullTextField(document.getElementById('what-you-use'));
	document.getElementById('how-often-you-use').value = clearNullTextField(document.getElementById('how-often-you-use'));
	document.getElementById('how-much-you-use').value = clearNullTextField(document.getElementById('how-much-you-use'));
	document.getElementById('reason_quit').value = clearNullTextField(document.getElementById('reason_quit'));
	document.getElementById('BAL').value = clearNullTextField(document.getElementById('BAL'));
	document.getElementById('when_treated').value = clearNullTextField(document.getElementById('when_treated'));
	document.getElementById('where_treated').value = clearNullTextField(document.getElementById('where_treated'));
	document.getElementById('no_treat_explain').innerHTML = clearNullTextArea(document.getElementById('no_treat_explain'));
	document.getElementById('relapse_explain').innerHTML = clearNullTextArea(document.getElementById('relapse_explain'));
}

function dh_drinks() {
	var what_use_label = document.getElementById('what_use_label');
	var how_often_label = document.getElementById('how_often_label');
	var how_much_use_label = document.getElementById('how_much_use_label');
	var what_you_use = document.getElementById('what-you-use');	
	var how_often_you_use = document.getElementById('how-often-you-use');	
	var how_much_you_use = document.getElementById('how-much-you-use');	
	var have_you_ever_label = document.getElementById('have_you_ever_label');
	var never_used = document.getElementById('never_used');
	var has_used = document.getElementById('has_used');
	var no_treat_explain = document.getElementById('never_used_label');
	var has_used_label = document.getElementById('has_used_label');


	what_use_label.style.opacity = '1.0';
	how_often_label.style.opacity = '1.0';
	how_much_use_label.style.opacity = '1.0';
	have_you_ever_label.style.opacity = '0.3';
	never_used_label.style.opacity = '0.3';
	has_used_label.style.opacity = '0.3';

	what_you_use.disabled = false;
	how_often_you_use.disabled = false;
	how_much_you_use.disabled = false;
	never_used.disabled = true;
	has_used.disabled = true;

	never_used.checked = true;

	var quit_label = document.getElementById('quit-label');
	var reason_quit_label = document.getElementById('reason-quit-label');
	var moLabel1 = document.getElementById('moLabel1');
	var yrLabel1 = document.getElementById('yrLabel1');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');	
	var reason_quit = document.getElementById('reason_quit');
	
	quit_label.style.opacity = '0.3';
	reason_quit_label.style.opacity = '0.3';
	moLabel1.style.opacity = '0.3';
	yrLabel1.style.opacity = '0.3';

	quitYrs.disabled = true;
	quitMos.disabled = true;
	reason_quit.disabled = true;

	quitYrs.value = '0';
	quitMos.value = '0';
	reason_quit.value = '';
}

function dh_no_drink() {
	var what_use_label = document.getElementById('what_use_label');
	var how_often_label = document.getElementById('how_often_label');
	var how_much_use_label = document.getElementById('how_much_use_label');
	var what_you_use = document.getElementById('what-you-use');	
	var how_often_you_use = document.getElementById('how-often-you-use');	
	var how_much_you_use = document.getElementById('how-much-you-use');
	var have_you_ever_label = document.getElementById('have_you_ever_label');
	var never_used = document.getElementById('never_used');
	var has_used = document.getElementById('has_used');
	var never_used_label = document.getElementById('never_used_label');
	var has_used_label = document.getElementById('has_used_label');

	what_use_label.style.opacity = '0.3';
	how_often_label.style.opacity = '0.3';
	how_much_use_label.style.opacity = '0.3';
	have_you_ever_label.style.opacity = '1.0';
	never_used_label.style.opacity = '1.0';
	has_used_label.style.opacity = '1.0';

	what_you_use.disabled = true;
	how_often_you_use.disabled = true;
	how_much_you_use.disabled = true;
	never_used.disabled = false;
	has_used.disabled = false;

	what_you_use.value = '';
	how_often_you_use.value = '';
	how_much_you_use.value = '';
}

function dh_never_used() {
	var quit_label = document.getElementById('quit-label');
	var reason_quit_label = document.getElementById('reason-quit-label');
	var moLabel1 = document.getElementById('moLabel1');
	var yrLabel1 = document.getElementById('yrLabel1');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');	
	var reason_quit = document.getElementById('reason_quit');
	
	quit_label.style.opacity = '0.3';
	reason_quit_label.style.opacity = '0.3';
	moLabel1.style.opacity = '0.3';
	yrLabel1.style.opacity = '0.3';

	quitYrs.disabled = true;
	quitMos.disabled = true;
	reason_quit.disabled = true;

	quitYrs.value = '0';
	quitMos.value = '0';
	reason_quit.value = '';
}

function dh_has_used() {
	var quit_label = document.getElementById('quit-label');
	var reason_quit_label = document.getElementById('reason-quit-label');
	var moLabel1 = document.getElementById('moLabel1');
	var yrLabel1 = document.getElementById('yrLabel1');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');	
	var reason_quit = document.getElementById('reason_quit');
	
	quit_label.style.opacity = '1.0';
	reason_quit_label.style.opacity = '1.0';
	moLabel1.style.opacity = '1.0';
	yrLabel1.style.opacity = '1.0';

	quitYrs.disabled = false;
	quitMos.disabled = false;
	reason_quit.disabled = false;
}

function dh_no_dui() {
	var dui_amount_label = document.getElementById('dui_amount_label');
	var bal_label = document.getElementById('bal_label');
	var dui_amount = document.getElementById('dui_amount');
	var bal = document.getElementById('BAL');

	dui_amount_label.style.opacity = '0.3';
	bal_label.style.opacity = '0.3';

	dui_amount.disabled = true;
	dui_amount.value = '0';
	bal.disabled = true;
	bal.value = '';
}

function dh_has_dui() {
	var dui_amount_label = document.getElementById('dui_amount_label');
	var bal_label = document.getElementById('bal_label');
	var dui_amount = document.getElementById('dui_amount');
	var bal = document.getElementById('BAL');

	dui_amount_label.style.opacity = '1.0';
	bal_label.style.opacity = '1.0';

	dui_amount.disabled = false;
	bal.disabled = false;
}

function dh_had_treatment() {
	var when_treated_label = document.getElementById('when_treated_label');
	var where_treated_label = document.getElementById('where_treated_label');
	var completed_treatment_label = document.getElementById('completed_treatment_label'); 
	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');
	var did_complete = document.getElementById('did_complete');
	var not_completed = document.getElementById('not_completed');
	var did_complete_label = document.getElementById('did_complete_label');
	var not_completed_label = document.getElementById('not_completed_label');
	var is_abstinent = document.getElementById('is_abstinent');

	when_treated_label.style.opacity = '1.0';
	where_treated_label.style.opacity = '1.0';
	completed_treatment_label.style.opacity = '1.0';
	did_complete_label.style.opacity = '1.0';
	not_completed_label.style.opacity = '1.0';

	when_treated.disabled = false;
	where_treated.disabled = false;
	did_complete.disabled = false;
	not_completed.disabled = false;

	did_complete.checked = true;
	is_abstinent.checked = true;
}

function dh_no_treatment() {
	var when_treated_label = document.getElementById('when_treated_label');
	var where_treated_label = document.getElementById('where_treated_label');
	var completed_treatment_label = document.getElementById('completed_treatment_label'); 
	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');
	var did_complete = document.getElementById('did_complete');
	var not_completed = document.getElementById('not_completed');
	var did_complete_label = document.getElementById('did_complete_label');
	var not_completed_label = document.getElementById('not_completed_label');

	when_treated_label.style.opacity = '0.3';
	where_treated_label.style.opacity = '0.3';
	completed_treatment_label.style.opacity = '0.3';
	did_complete_label.style.opacity = '0.3';
	not_completed_label.style.opacity = '0.3';

	when_treated.disabled = true;
	where_treated.disabled = true;
	did_complete.disabled = true;
	not_completed.disabled = true;

	when_treated.value = '';
	where_treated.value = '';
	did_complete.checked = true;

	var no_complete_explain_label = document.getElementById('no_complete_explain_label');
	var still_abstinent_label = document.getElementById('still_abstinent_label');
	var no_treat_explain = document.getElementById('no_treat_explain');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');
	var is_abstinent_label = document.getElementById('is_abstinent_label');
	var not_abstinent_label = document.getElementById('not_abstinent_label')

	no_complete_explain_label.style.opacity = '0.3';
	still_abstinent_label.style.opacity = '0.3';
	is_abstinent_label.style.opacity = '0.3';
	not_abstinent_label.style.opacity = '0.3';

	no_treat_explain.disabled = true;
	is_abstinent.disabled = true;
	not_abstinent.disabled = true;

	no_treat_explain.value = '';
	is_abstinent.checked = true;

	var trigger_label = document.getElementById('trigger_label');
	var relapse_explain = document.getElementById('relapse_explain');

	trigger_label.style.opacity = '0.3';
	relapse_explain.disabled = true;
	relapse_explain.value = '';
}

function dh_not_completed_sub() {
	var no_complete_explain_label = document.getElementById('no_complete_explain_label');
	var still_abstinent_label = document.getElementById('still_abstinent_label');
	var no_treat_explain = document.getElementById('no_treat_explain');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');
	var is_abstinent_label = document.getElementById('is_abstinent_label');
	var not_abstinent_label = document.getElementById('not_abstinent_label')

	no_complete_explain_label.style.opacity = '1.0';
	still_abstinent_label.style.opacity = '1.0';
	is_abstinent_label.style.opacity = '1.0';
	not_abstinent_label.style.opacity = '1.0';

	no_treat_explain.disabled = false;
	is_abstinent.disabled = false;
	not_abstinent.disabled = false;
}

function dh_did_completed_sub() {
	var no_complete_explain_label = document.getElementById('no_complete_explain_label');
	var still_abstinent_label = document.getElementById('still_abstinent_label');
	var no_treat_explain = document.getElementById('no_treat_explain');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');
	var is_abstinent_label = document.getElementById('is_abstinent_label');
	var not_abstinent_label = document.getElementById('not_abstinent_label')

	no_complete_explain_label.style.opacity = '0.3';
	still_abstinent_label.style.opacity = '0.3';
	is_abstinent_label.style.opacity = '0.3';
	not_abstinent_label.style.opacity = '0.3';

	no_treat_explain.disabled = true;
	is_abstinent.disabled = true;
	not_abstinent.disabled = true;

	no_treat_explain.value = '';
	is_abstinent.checked = true;

	var trigger_label = document.getElementById('trigger_label');
	var relapse_explain = document.getElementById('relapse_explain');

	trigger_label.style.opacity = '0.3';
	relapse_explain.disabled = true;
	relapse_explain.value = '';
}

function dh_is_abstinent() {
	var trigger_label = document.getElementById('trigger_label');
	var relapse_explain = document.getElementById('relapse_explain');

	trigger_label.style.opacity = '0.3';
	relapse_explain.disabled = true;
	relapse_explain.value = '';
}

function dh_not_abstinent() {
	var trigger_label = document.getElementById('trigger_label');
	var relapse_explain = document.getElementById('relapse_explain');

	trigger_label.style.opacity = '1.0';
	relapse_explain.disabled = false;
}

function goToCorrectAMForm() {
	document.getElementById('chooseAMform').submit();
}

function go_to_am_instruction() {
	document.getElementById('to_am_form').submit();
}

function exit_am(e_type) {
	document.getElementById('exit_type').value = e_type
	document.getElementById('exit_form').submit();
}

function exit_am2(e_type) {
	var form = document.getElementById('am_demo');
	document.getElementById('exit_type').value = e_type;
	form.action = '/exit_am/';
	form.submit();
}

function is_blank(data) {
	isBlank = false;

	if (String(data.value) === '' || String(data.value) === ' ' || String(data.value) === null) {
		isBlank = true;
	}

	return isBlank;
}

function set_blank_error_msg(field) {
	var error_field = document.getElementById('error_msg_field');
	var message = "The highlighted field " + String(field) + " cannot be blank";
	error_field.innerHTML = message;
}

function clear_error_field() {
	document.getElementById('error_msg_field').innerHTML = '';
}

function evaluate_checked_true(choice_yes, field, hidden, error_msg) {
	var proceed = true;

	if (choice_yes.checked === true) {
		proceed = evaluate_field(field, hidden, error_msg)
	}

	return proceed;
}

function evaluate_checked_false(choice_yes, field, hidden, error_msg) {
	var proceed = true;

	if (choice_yes.checked === false) {
		proceed = evaluate_field(field, hidden, error_msg)
	}

	return proceed;
}

function evaluate_field(field, hidden, error_msg) {
	var proceed = true;

	if (is_blank(field) === true) {
		set_blank_error_msg(error_msg);
		proceed = false;
	}
	else {
		hidden.value = field.value;
		clear_error_field();
	}

	return proceed;
}

function initialize_am_drug_history(json_data) {
	//TEXT FIELDS	
	var first_use_type = document.getElementById('first_use_type');	
	var what_you_use = document.getElementById('what-you-use');
	var how_often_you_use = document.getElementById('how-often-you-use');
	var how_much_you_use = document.getElementById('how-much-you-use');
	var reason_quit = document.getElementById('reason_quit');
	var BAL = document.getElementById('BAL');
	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');

	//TEXTAREA FIELDS
	var no_treat_explain = document.getElementById('no_treat_explain');
	var relapse_explain = document.getElementById('relapse_explain');
	
	//NUMBER FIELDS
	var first_drink = document.getElementById('first_drink');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');
	var dui_amount = document.getElementById('dui_amount');

	//RADIO ELEMENTS
	var current_use = document.getElementById('current_use');
	var no_current_use = document.getElementById('no_current_use');
	var has_used = document.getElementById('has_used');
	var never_used = document.getElementById('never_used');
	var dui = document.getElementById('dui'); //has DUI
	var no_dui = document.getElementById('no_dui');
	var give_me_help = document.getElementById('give_me_help');
	var no_help = document.getElementById('no_help');
	var had_treatment = document.getElementById('had_treatment');
	var no_treatment = document.getElementById('no_treatment');
	var did_complete = document.getElementById('did_complete');
	var not_completed = document.getElementById('not_completed');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');
	var was_drinking = document.getElementById('was_drinking');
	var not_drinking = document.getElementById('not_drinking');
	var is_problem = document.getElementById('is_problem');
	var no_problem = document.getElementById('no_problem');

	//DEFINE THE RADIO FIELDS
	defineRadio(current_use, no_current_use, json_data.curUse);
	defineRadio(has_used, never_used, json_data.everDrank);
	defineRadio(dui, no_dui, json_data.DUI);
	defineRadio(give_me_help, no_help, json_data.needHelpDrugs);
	defineRadio(had_treatment, no_treatment, json_data.drugTreatment);
	defineRadio(did_complete, not_completed, json_data.finishedTreatment);
	defineRadio(is_abstinent, not_abstinent, json_data.isClean);
	defineRadio(was_drinking, not_drinking, json_data.drinkLastEpisode);
	defineRadio(is_problem, no_problem, json_data.drinkRelationshipProblem);

	//CHECK FOR NULL VALUES IN TEXT AREAS
	treatNullAreaFields(no_treat_explain, json_data.reasonNotFinishedTreatment);
	treatNullAreaFields(relapse_explain, json_data.relapseTrigger);

	//CHECK FOR NULL VALUES IN TEXT FIELDS
	treatNullTextFields(first_use_type, json_data.firstDrinkType);
	treatNullTextFields(what_you_use, json_data.useType);
	treatNullTextFields(how_often_you_use, json_data.amtPerWeek);
	treatNullTextFields(how_much_you_use, json_data.useAmt);
	treatNullTextFields(reason_quit, json_data.reasonQuit);
	treatNullTextFields(BAL, json_data.BALevel);
	treatNullTextFields(when_treated, json_data.dateTreated);
	treatNullTextFields(where_treated, json_data.treatmentPlace);

	//PROCESS NUMBER FIELDS
	treatNumberFields(first_drink, json_data.firstDrinkAge);
	treatNumberFields(quitMos, json_data.monthsQuit);
	treatNumberFields(quitYrs, json_data.yearsQuit);
	treatNumberFields(dui_amount, json_data.numDUI);

	//INITIALIZE AND DISABLE/ENABLE FIELDS
	toggleUseAlcoholRadio();
	toggleEverDrankRadio();
	initializeDUIRadio();
	initializeTreatmentRadio();
	initializeRadioSub1();
	initializeSoberRadio();

	// clearNullTextField(first_use_type);
	// clearNullTextField(what_you_use);
	// clearNullTextField(how_often_you_use);
	// clearNullTextField(how_much_you_use);
	// clearNullTextField(reason_quit);
	// clearNullTextField(BAL);
	// clearNullTextField(when_treated);
	// clearNullTextField(where_treated);
}

function continue_am_dh() {
	var proceed = true;
	var first_drink = document.getElementById('first_drink');
	var first_use_type = document.getElementById('first_use_type');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');
	var reason_quit = document.getElementById('reason_quit');
	var what_you_use = document.getElementById('what-you-use');
	var how_often_you_use = document.getElementById('how-often-you-use');
	var how_much_you_use = document.getElementById('how-much-you-use');
	var dui_amount = document.getElementById('dui_amount');
	var BAL = document.getElementById('BAL');
	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');
	var no_treat_explain = document.getElementById('no_treat_explain');
	var relapse_explain = document.getElementById('relapse_explain');

	//TRUE RADIO BUTTONS
	var current_use = document.getElementById('current_use');
	var has_used = document.getElementById('current_use');
	var has_dui = document.getElementById('dui');
	var give_me_help = document.getElementById('give_me_help');
	var had_treatment = document.getElementById('had_treatment');
	var did_complete = document.getElementById('did_complete');
	var is_abstinent =document.getElementById('is_abstinent');
	var was_drinking =document.getElementById('was_drinking');
	var is_problem =document.getElementById('is_problem');

	//PROCESS RADIO BUTTONS
	processRadioYes(current_use, document.getElementById('m_curr_use'));
	processRadioYes(has_used, document.getElementById('m_everDrank'));
	processRadioYes(has_dui, document.getElementById('m_DUI'));
	processRadioYes(give_me_help, document.getElementById('m_needHelpDrugs'));
	processRadioYes(had_treatment, document.getElementById('m_drugTreatment'));
	processRadioYes(did_complete, document.getElementById('m_finishedTreatment'));
	processRadioYes(is_abstinent, document.getElementById('m_isClean'));
	processRadioYes(was_drinking, document.getElementById('m_drinkLastEpisode'));
	processRadioYes(is_problem, document.getElementById('m_drinkRelationshipProblem'));

	//PROCESS DYNAMICALLY DISABLED FIELDS
	processDisabledTextFields(first_use_type, m_first_use_type);
	processDisabledTextFields(what_you_use, document.getElementById('m-what-you-use'));
	processDisabledTextFields(how_often_you_use, document.getElementById('m-how-often-you-use'));
	processDisabledTextFields(how_much_you_use, document.getElementById('m-how-much-you-use'));
	processDisabledTextFields(reason_quit, document.getElementById('m_reason_quit'));
	processDisabledTextFields(BAL, document.getElementById('m_BAL'));
	processDisabledTextFields(when_treated, document.getElementById('m_when_treated'));
	processDisabledTextFields(where_treated, document.getElementById('m_where_treated'));

	// if (no_treat_explain.disabled === true) {
	// 	document.getElementById('m_no_treat_explain').value = 'Kiss my ass';
	// }
	processDisabledTextFields(no_treat_explain, document.getElementById('m_no_treat_explain'));
	processDisabledTextFields(relapse_explain, document.getElementById('m_relapse_explain'));

	//PROCESS DYNAMICALLY DISABLED NUMBER FIELDS
	processDisabledNumberFields(quitMos, document.getElementById('m_quitMos'));
	processDisabledNumberFields(quitYrs, document.getElementById('m_quitYrs'));
	processDisabledNumberFields(dui_amount, document.getElementById('m_dui_amount'));

	//COPY THE REMAINING FEILDS TO POST
	copyElementToInput('first_drink');
	copyElementToInput('first_use_type');
	
	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}











