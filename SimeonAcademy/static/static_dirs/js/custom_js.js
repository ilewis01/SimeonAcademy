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

function processDynamicTextPostValue(trigger, element, m_element) {
	if (trigger.checked === true) {
		m_element.value = element.value;
	}
	else {
		m_element.value = 'N/A';
	}
}

function isBlankField(element) {
	var isBlank = false;
	if (element.value === '') {
		if (element.value === null) {
			isBlank = true;
		}
	}
	return isBlank;
}

function handleBlankElement(element) {
	if (isBlank(element) === true) {
		element.value = 'N/A';
	}
}

function handleBlankTextArea(element) {
	if (isBlank(element) === true) {
		element.innerHTML = 'N/A';
	}
}

function postCheckboxValue(box, target) {
	if (box.checked === true) {
		target.value = 'True';
	}
	else {
		target.value = 'False';
	}
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

function processRadioJavascript(radioButton, postElement) {
	if (radioButton.checked === true) {
		postElement.value = 'true';
	}
	else {
		postElement.value = 'fause';
	}
}

function processRadioByValue(radioValue, yesRadio, m_element) {
	if (String(radioValue) === String(yesRadio.value)) {
		m_element.value = true;
	}
	else {
		m_element = false;
	}
}


function copyElementToInput(element_name) {
	copiedElementName = 'm_';
	copiedElementName += element_name;

	var element_orig = document.getElementById(element_name);
	var element_copy = document.getElementById(copiedElementName);

	element_copy.value = element_orig.value;
}

function postDynamicFields(trigger, field, m_target) {
	if (trigger.checked === true) {
		if (field.value === null || field.value === '') {
			m_target.value = 'N/A';
		}
		else {
			m_target.value = field.value;
		}
	}
	else {
		m_target.value = 'N/A';
	}
}

function postDynamicRadioButtons(radio, target) {
	if (radio.checked === true) {
		target.value = 'True';
	}
	else {
		target.value = 'False';
	}
}

function pureCopy(source, target) {
	target.value = source.value;
}

function processDisabledTextFields(element, m_target) {
	if (element.disabled === true) {
		m_target.value = 'N/A';
	}
	else {
		m_target.value = element.value;
	}
}

function processDisabledNumberFields(element, m_target) {
	if ((element.disabled === true)) {
		m_target.value = '0';
	}
	else {
		m_target.value = element.value;
	}
}

function processNumberZero(element) {
	if ((element.disabled === true) || (Number.isInteger(element.value) === false)) {
		element.value = '0';
	}
}

function sideDemo() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_demographic/';
	form.submit();
}

function sideDH() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_drugHistory/';
	form.submit();
}

function sideChild() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_childhood/';
	form.submit();
}

function sideAh1() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_angerHistory/';
	form.submit();
}

function sideAh2() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_angerHistory2/';
	form.submit();
}

function sideAh3() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_angerHistory3/';
	form.submit();
}

function sideConnect() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_connections/';
	form.submit();
}

function sideWorst() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_worst/';
	form.submit();
}

function sideTarget() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_angerTarget/';
	form.submit();
}

function sideFamily() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_familyOrigin/';
	form.submit();
}

function sideCurrent() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_problems/';
	form.submit();
}

function sideControl() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_control/';
	form.submit();
}

function sideFinal() {
	back = document.getElementById('back_btn');
	back.value = 'true';
	form = document.getElementById('am_demo');
	form.action = '/am_final/';
	form.submit();
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

function twoElementRadioSetup(yesRadio, label, field) {
	if (yesRadio.checked === true) {
		label.disabled = false;
		label.style.opacity = '1.0';
		field.style.opacity = '1.0';
	}

	else {
		label.style.opacity = '0.3';
		field.style.opacity = '0.3';
		field.value = '';
		field.disabled;
	}
}

function opacityLow(element) {
	element.style.opacity = '0.3';
}

function opacityHigh(element) {
	element.style.opacity = '1.0';
}

function fourElementRadioSetup(yesTrigger, label1, label2, label3, label4, label5, field1, field2, field3, field4) {
	if (yesTrigger.checked === true) {
		field1.disabled = false;
		field2.disabled = false;
		field3.disabled = false;
		field4.disabled = false;

		opacityHigh(field1);
		opacityHigh(field2);
		opacityHigh(field3);
		opacityHigh(field4);

		opacityHigh(label1);
		opacityHigh(label2);
		opacityHigh(label3);
		opacityHigh(label4);
		opacityHigh(label5);
	}
	else {
		opacityLow(field1);
		opacityLow(field2);
		opacityLow(field3);
		opacityLow(field4);

		opacityLow(label1);
		opacityLow(label2);
		opacityLow(label3);
		opacityLow(label4);
		opacityLow(label5);

		field1.disabled = true;
		field2.disabled = true;
		field3.disabled = true;
		field4.disabled = true;
	}
}

function threeElementRadioProcess(trigger, label1, label2, label3, element1, element2, element3) {
	if (trigger.checked === true) {
		element1.disabled = false;
		element2.disabled = false;
		element3.disabled = false;

		opacityHigh(element1);
		opacityHigh(element2);
		opacityHigh(element3);
		opacityHigh(label1);
		opacityHigh(label2);
		opacityHigh(label3);
	}
	else {
		opacityLow(element1);
		opacityLow(element2);
		opacityLow(element3);
		opacityLow(label1);
		opacityLow(label2);
		opacityLow(label3);

		element1.value = '';
		element2.value = '';
		element3.value = '';

		element1.disabled = true;
		element2.disabled = true;
		element3.disabled = true;
	}
}

function secondaryTrigger(trigger, label1, label2, label3, element1, element2) {
	if (trigger === false) {
		opacityLow(label1);
		opacityLow(label2);
		opacityLow(label3);
		opacityLow(element1);
		opacityLow(element2);
	}
	else {
		element1.disabled = false;
		element2.disabled = false;
		opacityHigh(element1);
		opacityHigh(element2);
		opacityHigh(label1);
		opacityHigh(label2);
		opacityHigh(label3);
	}
}

// AM ANGER/VIOLENCE HISTORY FUNCTIONS
function continue_to_am_connections() {
	document.getElementById('am_demo').submit();
}

function insertProcessedText(text) {
	if (String(text) === 'NA') {
		text = '';
	}
	return text;
}


// AM DEMOGRAPHIC FUNCTIONS
function dropOutRadio() {
	var hs_drop = document.getElementById('hs_drop');
	var resasonDO = document.getElementById('resasonDO');
	var resasonDO_label = document.getElementById('resasonDO_label');

	if (hs_drop.checked === true) {
		resasonDO.disabled = false;
		resasonDO.style.opacity = '1.0';
		resasonDO_label.style.opacity = '1.0';
	}

	else {
		resasonDO.style.opacity = '0.3';
		resasonDO_label.style.opacity = '0.3';
		resasonDO.value = '';
		resasonDO.disabled = true;
	}
}

function healthRadioBtn() {
	var not_healthy = document.getElementById('not_healthy');
	var health_exp = document.getElementById('health_exp');
	var health_exp_label = document.getElementById('health_exp_label');

	if (not_healthy.checked === true) {
		health_exp.disabled = false;
		health_exp.style.opacity = '1.0';
		health_exp_label.style.opacity = '1.0';
	}

	else {
		health_exp.style.opacity = '0.3';
		health_exp_label.style.opacity = '0.3';
		health_exp.value = '';
		health_exp.disabled = true;
	}
}

function medsRadioBtn() {
	var on_meds = document.getElementById('on_meds');
	var explain_label_health = document.getElementById('explain_label_health');
	var whatMedicine = document.getElementById('whatMedicine');

	if (on_meds.checked === true) {
		whatMedicine.disabled = false;
		whatMedicine.style.opacity = '1.0';
		explain_label_health.style.opacity = '1.0';
	}

	else {
		whatMedicine.style.opacity = '0.3';
		explain_label_health.style.opacity = '0.3';
		whatMedicine.value = '';
		whatMedicine.disabled = true;
	}
}

function initialize_am_demo(json_data, back) {
	var marital = document.getElementById('marital');
	var living = document.getElementById('living');
	var rent_radio = document.getElementById('rent_radio');
	var own_radio = document.getElementById('own_radio');
	var res_mos = document.getElementById('res-mos');
	var res_yrs = document.getElementById('res-yrs');
	var children = document.getElementById('dep_children');
	var others = document.getElementById('dep_other');
	var edu = document.getElementById('edu');
	var hs_grad = document.getElementById('hs_grad');
	var hs_drop = document.getElementById('hs_drop');
	var resasonDO = document.getElementById('resasonDO');
	var occ = document.getElementById('occ');
	var employer = document.getElementById('employer');
	var emp_add = document.getElementById('em_add');
	var em_phone = document.getElementById('em_phone');
	var mosJob = document.getElementById('mosJob');
	var yrsJob = document.getElementById('yrsJob');
	var healthy = document.getElementById('healthy');
	var not_healthy = document.getElementById('not_healthy');
	var no_med = document.getElementById('no_med');
	var on_meds = document.getElementById('on_meds');
	var health_exp = document.getElementById('health_exp');
	var whatMedicine = document.getElementById('whatMedicine');

	marital.selectedIndex = json_data.maritalStatus
	living.selectedIndex = json_data.livingSituation
	edu.selectedIndex = json_data.education

	res_mos.value = json_data.months_res
	res_yrs.value = json_data.years_res
	children.value = json_data.num_children
	mosJob.value = json_data.employed_months
	yrsJob.value = json_data.employed_years

	resasonDO.value = insertProcessedText(json_data.resasonDO);
	occ.value = insertProcessedText(json_data.job_title);
	employer.value = insertProcessedText(json_data.employee);
	emp_add.value = insertProcessedText(json_data.emp_address);
	em_phone.value = insertProcessedText(json_data.employer_phone);
	health_exp.value = insertProcessedText(json_data.health_exp);
	whatMedicine.value = insertProcessedText(json_data.whatMedicine);	

	if (String(json_data.own) === 'true') {
		own_radio.checked = true;
	}
	else {
		rent_radio.checked = true;
	}

	if (String(json_data.drop_out) === 'true') {
		hs_drop.checked = true;
	}
	else {
		hs_grad.checked = true;
	}

	if (String(json_data.health_problem) === 'true') {
		not_healthy.checked = true;
	}
	else {
		healthy.checked = true;
	}

	if (String(json_data.medication) === 'true') {
		on_meds.checked = true;
	}
	else {
		no_med.checked = true;
	}

	dropOutRadio();
	healthRadioBtn();
	medsRadioBtn();
}


function continue_am() {
	var proceed = true;
	var back = document.getElementById('back_btn');

	back.value = 'false';	

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

function setRadioElement(trigger, yesRadio, noRadio) {
	if (String(trigger) === 'true') {
		yesRadio.checked = true;
	}
	else {
		noRadio.checked = true;
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

function dh_no_dui() {
	var dui_amount_label = document.getElementById('dui_amount_label');
	var bal_label = document.getElementById('bal_label');
	var bal_label2 = document.getElementById('bal_label2');
	var dui_amount = document.getElementById('dui_amount');
	var bal = document.getElementById('BAL');

	dui_amount_label.style.opacity = '0.3';
	bal_label.style.opacity = '0.3';
	bal_label2.style.opacity = '0.3';

	dui_amount.disabled = true;
	dui_amount.value = '0';
	bal.disabled = true;
	bal.value = '';
}

function dh_has_dui() {
	var dui_amount_label = document.getElementById('dui_amount_label');
	var bal_label = document.getElementById('bal_label');
	var bal_label2 = document.getElementById('bal_label2');
	var dui_amount = document.getElementById('dui_amount');
	var bal = document.getElementById('BAL');

	dui_amount_label.style.opacity = '1.0';
	bal_label.style.opacity = '1.0';
	bal_label2.style.opacity = '1.0';

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

	did_complete.checked = true;
	is_abstinent.checked = true;

	when_treated.disabled = false;
	where_treated.disabled = false;
	did_complete.disabled = false;
	not_completed.disabled = false;
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

	when_treated.value = '';
	where_treated.value = '';
	did_complete.checked = true;

	when_treated.disabled = true;
	where_treated.disabled = true;
	did_complete.disabled = true;
	not_completed.disabled = true;	

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

	no_treat_explain.value = '';
	is_abstinent.checked = true;

	no_treat_explain.disabled = true;
	is_abstinent.disabled = true;
	not_abstinent.disabled = true;

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

	dhRadio3();
	dhRadio2();
}


function goToCorrectAMForm() {
	document.getElementById('chooseAMform').submit();
}

function go_to_am_instruction() {
	document.getElementById('to_am_form').submit();
}

function exit_am(e_type) {
	var exit_type_sub = document.getElementById('exit_type_sub');
	exit_type_sub.value = String(e_type);
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

//DRUG HISTORY FUNCTIONS
function dhRadio3() { //CUURENTLY DRINK OR USE ALCOHOL
	var dui = document.getElementById('dui');

	var dui_amount_label = document.getElementById('dui_amount_label');
	var bal_label = document.getElementById('bal_label');
	var bal_label2 = document.getElementById('bal_label2');

	var BAL = document.getElementById('BAL');
	var dui_amount = document.getElementById('dui_amount');

	if (dui.checked == true) {
		BAL.disabled = false;
		dui_amount.disabled = false;

		BAL.style.opacity = '1.0';
		dui_amount.style.opacity = '1.0';
		dui_amount_label.style.opacity = '1.0';
		bal_label.style.opacity = '1.0';
		bal_label2.style.opacity = '1.0';
	}

	else {
		BAL.style.opacity = '0.3';
		dui_amount.style.opacity = '0.3';
		dui_amount_label.style.opacity = '0.3';
		bal_label.style.opacity = '0.3';
		bal_label2.style.opacity = '0.3';

		BAL.value = '';
		dui_amount.value = '0';

		BAL.disabled = true;
		dui_amount.disabled = true;
	}
}

function dhRadio2() {
	var has_used = document.getElementById('has_used');

	var quit_label = document.getElementById('quit-label');
	var moLabel1 = document.getElementById('moLabel1');
	var yrLabel1 = document.getElementById('yrLabel1');
	var reason_quit_label = document.getElementById('reason-quit-label');
	var got_dui_label = document.getElementById('got_dui_label');
	var hasADui_label = document.getElementById('hasADui_label');
	var no_dui_label = document.getElementById('no_dui_label');

	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');
	var reason_quit = document.getElementById('reason_quit');
	var no_dui = document.getElementById('no_dui');
	var dui = document.getElementById('dui');

	if (has_used.checked === true) {
		quitMos.disabled = false;
		quitYrs.disabled = false;
		reason_quit.disabled = false;
		no_dui.disabled = false;
		dui.disabled = false;

		quitMos.style.opacity = '1.0';
		quitYrs.style.opacity = '1.0';
		reason_quit.style.opacity = '1.0';
		no_dui.style.opacity = '1.0';
		dui.style.opacity = '1.0';
		quit_label.style.opacity = '1.0';
		moLabel1.style.opacity = '1.0';
		yrLabel1.style.opacity = '1.0';
		reason_quit_label.style.opacity = '1.0';
		got_dui_label.style.opacity = '1.0';
		hasADui_label.style.opacity = '1.0';
		no_dui_label.style.opacity = '1.0';
	}

	else {
		quitMos.style.opacity = '0.3';
		quitYrs.style.opacity = '0.3';
		reason_quit.style.opacity = '0.3';
		no_dui.style.opacity = '0.3';
		dui.style.opacity = '0.3';
		quit_label.style.opacity = '0.3';
		moLabel1.style.opacity = '0.3';
		yrLabel1.style.opacity = '0.3';
		reason_quit_label.style.opacity = '0.3';
		got_dui_label.style.opacity = '0.3';
		hasADui_label.style.opacity = '0.3';
		no_dui_label.style.opacity = '0.3';

		no_dui.checked = true;

		quitMos.value = '0';
		quitYrs.value = '0';
		reason_quit.value = '';

		quitMos.disabled = true;
		quitYrs.disabled = true;
		reason_quit.disabled = true;

		dhRadio3();
	}
}

function dhLeftRadio3() {
	var not_abstinent = document.getElementById('not_abstinent');
	var is_abstinent = document.getElementById('is_abstinent');
	var trigger_label = document.getElementById('trigger_label');
	var relapse_explain = document.getElementById('relapse_explain');
	// twoElementRadioSetup(not_abstinent, trigger_label, relapse_explain);
	if (is_abstinent.checked === true) {
		opacityLow(trigger_label);
		opacityLow(relapse_explain);
		relapse_explain.disabled = true;
	}
	else if (not_abstinent.checked === true) {
		relapse_explain.disabled = false;
		opacityHigh(trigger_label);
		opacityHigh(relapse_explain);
	}
}

function dhLeftRadio2() {
	var not_completed = document.getElementById('not_completed');
	var no_complete_explain_label = document.getElementById('no_complete_explain_label');
	var no_treat_explain = document.getElementById('no_treat_explain');

	twoElementRadioSetup(not_completed, no_complete_explain_label, no_treat_explain);

	var still_abstinent_label = document.getElementById('still_abstinent_label');
	var is_abstinent_label = document.getElementById('is_abstinent_label');
	var not_abstinent_label = document.getElementById('not_abstinent_label');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');

	if (not_completed.checked === false) {
		is_abstinent.checked = true;
		dhLeftRadio3();
		// is_abstinent.disabled = true;
		// not_abstinent.disabled = true;
	}

	else {
		is_abstinent.disabled = false;
		not_abstinent.disabled = false;		
		dhRadio3();
	}
}

function dhLeftRadio1() {
	var had_treatment = document.getElementById('had_treatment');

	var when_treated_label = document.getElementById('when_treated_label');
	var where_treated_label = document.getElementById('where_treated_label');
	var completed_treatment_label = document.getElementById('completed_treatment_label');
	var did_complete_label = document.getElementById('did_complete_label');
	var not_completed_label = document.getElementById('not_completed_label');

	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');
	var did_complete = document.getElementById('did_complete');
	var not_completed = document.getElementById('not_completed');

	var still_abstinent_label = document.getElementById('still_abstinent_label');
	var is_abstinent_label = document.getElementById('is_abstinent_label');
	var not_abstinent_label = document.getElementById('not_abstinent_label');
	var is_abstinent = document.getElementById('is_abstinent');
	var not_abstinent = document.getElementById('not_abstinent');

	if (had_treatment.checked === false) {
		did_complete.checked = true;
		opacityLow(still_abstinent_label);
		opacityLow(is_abstinent_label);
		opacityLow(not_abstinent_label);
		opacityLow(is_abstinent);
		opacityLow(not_abstinent);
		is_abstinent.disabled = true;
		not_abstinent.disabled = true;
		when_treated.value = '';
		where_treated.value = '';
	}
	else {
		is_abstinent.disabled = false;
		not_abstinent.disabled = false;
		opacityHigh(still_abstinent_label);
		opacityHigh(is_abstinent_label);
		opacityHigh(not_abstinent_label);
		opacityHigh(is_abstinent);
		opacityHigh(not_abstinent);
	}

	fourElementRadioSetup(had_treatment, when_treated_label, where_treated_label, completed_treatment_label, did_complete_label, not_completed_label, when_treated, where_treated, did_complete, not_completed);
	dhLeftRadio2();
}

function topLevelDH() {
	var current_use = document.getElementById('current_use');

	var what_use_label = document.getElementById('what_use_label');
	var how_often_label = document.getElementById('how_often_label');
	var how_much_use_label = document.getElementById('how_much_use_label');

	var what_you_use = document.getElementById('what-you-use');
	var how_often_you_use = document.getElementById('how-often-you-use');
	var how_much_you_use = document.getElementById('how-much-you-use');

	var never_used = document.getElementById('never_used');
	var has_used = document.getElementById('has_used');

	var have_you_ever_label = document.getElementById('have_you_ever_label');
	var never_used_label = document.getElementById('never_used_label');
	var has_used_label = document.getElementById('has_used_label');

	var no_dui = document.getElementById('no_dui');
	var dui = document.getElementById('dui');
	var got_dui_label = document.getElementById('got_dui_label');
	var no_dui_label = document.getElementById('no_dui_label');
	var hasADui_label = document.getElementById('hasADui_label');

	threeElementRadioProcess(current_use, what_use_label, how_often_label, how_much_use_label, what_you_use, how_often_you_use, how_much_you_use);

	if (current_use.checked === false) {
		never_used.disabled = false;
		has_used.disabled = false;
		opacityHigh(have_you_ever_label);
		opacityHigh(never_used_label);
		opacityHigh(has_used_label);
		opacityHigh(never_used);
		opacityHigh(has_used);

		dhRadio2();
	}
	else {
		never_used.checked = true;
		dhRadio2();

		opacityLow(have_you_ever_label);
		opacityLow(never_used_label);
		opacityLow(has_used_label);
		opacityLow(never_used);
		opacityLow(has_used);

		never_used.disabled = true;
		has_used.disabled = true;

		opacityHigh(got_dui_label);
		opacityHigh(no_dui_label);
		opacityHigh(hasADui_label);
		opacityHigh(no_dui);
		opacityHigh(dui);
		no_dui.disabled = false;
		dui.disabled = false;
	}
}

function radioRightNoLower() {
	var current_use = document.getElementById('current_use');

	var what_use_label = document.getElementById('what_use_label');
	var how_often_label = document.getElementById('how_often_label');
	var how_much_use_label = document.getElementById('how_much_use_label');

	var what_you_use = document.getElementById('what-you-use');
	var how_often_you_use = document.getElementById('how-often-you-use');
	var how_much_you_use = document.getElementById('how-much-you-use');

	var never_used = document.getElementById('never_used');
	var has_used = document.getElementById('has_used');

	var have_you_ever_label = document.getElementById('have_you_ever_label');
	var never_used_label = document.getElementById('never_used_label');
	var has_used_label = document.getElementById('has_used_label');

	var no_dui = document.getElementById('no_dui');
	var dui = document.getElementById('dui');
	var got_dui_label = document.getElementById('got_dui_label');
	var no_dui_label = document.getElementById('no_dui_label');
	var hasADui_label = document.getElementById('hasADui_label');

	threeElementRadioProcess(current_use, what_use_label, how_often_label, how_much_use_label, what_you_use, how_often_you_use, how_much_you_use);

	if (current_use.checked === false) {
		never_used.disabled = false;
		has_used.disabled = false;
		opacityHigh(have_you_ever_label);
		opacityHigh(never_used_label);
		opacityHigh(has_used_label);
		opacityHigh(never_used);
		opacityHigh(has_used);

		dhRadio2();

		opacityHigh(got_dui_label);
		opacityHigh(no_dui_label);
		opacityHigh(hasADui_label);
		opacityHigh(no_dui);
		opacityHigh(dui);
		no_dui.disabled = false;
		dui.disabled = false;
	}
	else {
		never_used.checked = true;
		dhRadio2();

		opacityLow(have_you_ever_label);
		opacityLow(never_used_label);
		opacityLow(has_used_label);
		opacityLow(never_used);
		opacityLow(has_used);

		never_used.disabled = true;
		has_used.disabled = true;

		opacityHigh(got_dui_label);
		opacityHigh(no_dui_label);
		opacityHigh(hasADui_label);
		opacityHigh(no_dui);
		opacityHigh(dui);
		no_dui.disabled = false;
		dui.disabled = false;
	}
}

function initialize_am_drug_history(json_data) {
	//INITIALIZE RADIO BUTTONS
	var current_use = document.getElementById('current_use');
	var no_current_use = document.getElementById('no_current_use');
	var has_used = document.getElementById('has_used');
	var never_used = document.getElementById('never_used');
	var dui = document.getElementById('dui');
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

	setRadioElement(json_data.curUse, current_use, no_current_use);

	if (current_use.checked === true) {
		never_used.checked = true;
	}

	setRadioElement(json_data.everDrank, has_used, never_used);	
	setRadioElement(json_data.drugTreatment, had_treatment, no_treatment);
	setRadioElement(json_data.finishedTreatment, did_complete, not_completed);
	setRadioElement(json_data.isClean, is_abstinent, not_abstinent);
	setRadioElement(json_data.drinkLastEpisode, was_drinking, not_drinking);
	setRadioElement(json_data.drinkRelationshipProblem, is_problem, no_problem);
	setRadioElement(json_data.needHelpDrugs, give_me_help, no_help);

	//TURN ON DYNAMIC RADIO BUTTONS
	radioRightNoLower();
	setRadioElement(json_data.DUI, dui, no_dui);
	dhRadio3();
	dhLeftRadio1();

	if (dui.checked === true) {
		document.getElementById('dui_amount').value = json_data.numDUI;
		document.getElementById('BAL').value = json_data.BALevel;
	}

	if (had_treatment.checked === true) {
		document.getElementById('when_treated').value = json_data.dateTreated;
		document.getElementById('where_treated').value = json_data.treatmentPlace;
	}

	if (not_completed.checked === true) {
		document.getElementById('no_treat_explain').value = json_data.reasonNotFinishedTreatment;
	}

	if (not_abstinent.checked === true) {
		document.getElementById('relapse_explain').value = json_data.relapseTrigger;
	}

	if (has_used.checked === true) {
		document.getElementById('quitMos').value = json_data.monthsQuit;
		document.getElementById('quitYrs').value = json_data.yearsQuit;
		document.getElementById('reason_quit').value = json_data.reasonQuit;
	}

	if (is_abstinent.checked === true) {
		opacityLow(document.getElementById('relapse_explain'));
		opacityLow(document.getElementById('trigger_label'));
		document.getElementById('relapse_explain').disabled = true;
	}
	// if (document.getElementById('not_abstinent').checked === true) {
	// 	document.getElementById('relapse_explain').disabled = false;
	// 	opacityHigh(document.getElementById('relapse_explain'));
	// 	opacityHigh(document.getElementById('trigger_label'));		
	// }
}

function continue_am_dh() {
	var proceed = true;

	//HIDDEN FIELDS
	var m_useType = document.getElementById('m_useType');
	var m_amtPerWeek = document.getElementById('m_amtPerWeek');
	var m_useAmt = document.getElementById('m_useAmt');
	var m_monthsQuit = document.getElementById('m_monthsQuit');
	var m_yearsQuit = document.getElementById('m_yearsQuit');
	var m_reasonQuit = document.getElementById('m_reasonQuit');
	var m_numDUI = document.getElementById('m_numDUI');
	var m_BALevel = document.getElementById('m_BALevel');
	var m_treatmentPlace = document.getElementById('m_treatmentPlace');
	var m_dateTreated = document.getElementById('m_dateTreated');
	var m_reasonNotFinishedTreatment = document.getElementById('m_reasonNotFinishedTreatment');
	var m_relapseTrigger = document.getElementById('m_relapseTrigger');

	//TEXT FIELDS	
	var what_you_use = document.getElementById('what-you-use');
	var how_often_you_use = document.getElementById('how-often-you-use');
	var how_much_you_use = document.getElementById('how-much-you-use');
	var quitMos = document.getElementById('quitMos');
	var quitYrs = document.getElementById('quitYrs');
	var reason_quit = document.getElementById('reason_quit');
	var dui_amount = document.getElementById('dui_amount');
	var BAL = document.getElementById('BAL');
	var when_treated = document.getElementById('when_treated');
	var where_treated = document.getElementById('where_treated');
	var no_treat_explain = document.getElementById('no_treat_explain');
	var relapse_explain = document.getElementById('relapse_explain');

	//DYNAMIC DATA TRIGGERS
	var current_use = document.getElementById('current_use');
	var has_used = document.getElementById('has_used');
	var dui = document.getElementById('dui');
	var had_treatment = document.getElementById('had_treatment');
	var not_completed = document.getElementById('not_completed');
	var not_abstinent = document.getElementById('not_abstinent');

	//PROCESS AND POST DYNAMIC FIELD VALUES
	postDynamicFields(current_use, what_you_use, m_useType);
	postDynamicFields(current_use, how_often_you_use, m_amtPerWeek);
	postDynamicFields(current_use, how_much_you_use, m_useAmt);
	postDynamicFields(has_used, reason_quit, m_reasonQuit);
	postDynamicFields(dui, dui_amount, m_numDUI);
	postDynamicFields(dui, BAL, m_BALevel);
	postDynamicFields(had_treatment, when_treated, m_dateTreated);
	postDynamicFields(had_treatment, where_treated, m_treatmentPlace);
	postDynamicFields(not_completed, no_treat_explain, m_reasonNotFinishedTreatment);
	postDynamicFields(not_abstinent, relapse_explain, m_relapseTrigger);

	//PROCESS DYNAMIC NUMBER FIELDS
	processDisabledNumberFields(quitMos, m_monthsQuit);
	processDisabledNumberFields(quitYrs, m_yearsQuit);



	document.getElementById('back_btn').value = 'false';
	
	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}


// AM CHILDHOOD FUNCTIONS
function childTraumaRadio() {
	var hadTramua = document.getElementById('hadTramua');
	var traumaExplain_label = document.getElementById('traumaExplain_label');
	var traumaExplain = document.getElementById('traumaExplain');

	twoElementRadioSetup(hadTramua, traumaExplain_label, traumaExplain);
}

function childAbusedRadio() {
	var childAbused = document.getElementById('childAbused');
	var abusedBy_label = document.getElementById('abusedBy_label');
	var abusedBy = document.getElementById('abusedBy');
	var abuseImpact_label = document.getElementById('abuseImpact_label');
	var abuseImpact = document.getElementById('abuseImpact');

	twoElementRadioSetup(childAbused, abusedBy_label, abusedBy);
	twoElementRadioSetup(childAbused, abuseImpact_label, abuseImpact);
}

function hadChildAngerRadio() {
	var hadAngerChild = document.getElementById('hadAngerChild');
	var childAngerExplain_label = document.getElementById('childAngerExplain_label');
	var childAngerExplain = document.getElementById('childAngerExplain');

	twoElementRadioSetup(hadAngerChild, childAngerExplain_label, childAngerExplain);
}

function otherEventsHelpRadio() {
	var haveOtherEvents = document.getElementById('haveOtherEvents');
	var otherChildExplain_label = document.getElementById('otherChildExplain_label');
	var otherChildExplain = document.getElementById('otherChildExplain');

	twoElementRadioSetup(haveOtherEvents, otherChildExplain_label, otherChildExplain);
}

function parentsFoughtRadio() {
	var sawViolence = document.getElementById('sawViolence');
	var parentViolenceExplain_label = document.getElementById('parentViolenceExplain_label');
	var parentViolenceExplain = document.getElementById('parentViolenceExplain');
	var parentViolenceImpact_label = document.getElementById('parentViolenceImpact_label');
	var parentViolenceImpact = document.getElementById('parentViolenceImpact');

	twoElementRadioSetup(sawViolence, parentViolenceExplain_label, parentViolenceExplain);
	twoElementRadioSetup(sawViolence, parentViolenceImpact_label, parentViolenceImpact);
}

function initialize_am_childhood(json_data) {
	//text fields
	var raisedBy = document.getElementById('raisedBy');
	var traumaExplain = document.getElementById('traumaExplain');
	var howLeftHome = document.getElementById('howLeftHome');
	var dadCloseExplain = document.getElementById('dadCloseExplain');
	var momCloseExplain = document.getElementById('momCloseExplain');
	var abusedBy = document.getElementById('abusedBy');
	var abuseImpact = document.getElementById('abuseImpact');
	var childAngerExplain = document.getElementById('childAngerExplain');
	var otherChildExplain = document.getElementById('otherChildExplain');
	var parentViolenceExplain = document.getElementById('parentViolenceExplain');
	var parentViolenceImpact = document.getElementById('parentViolenceImpact');
	var siblingsRelationshipExplain = document.getElementById('siblingsRelationshipExplain');

	//boolean fields
	var momAlive = document.getElementById('momAlive');
	var dadAlive = document.getElementById('dadAlive');
	var childTrama = document.getElementById('childTrama');
	var siblingsClose = document.getElementById('siblingsClose');
	var dadClose = document.getElementById('dadClose');
	var momClose = document.getElementById('momClose');
	var wasAbused = document.getElementById('wasAbused');
	var childAnger = document.getElementById('childAnger');
	var otherChild = document.getElementById('otherChild');
	var parentViolence = document.getElementById('parentViolence');

	//sub radio button declarations
	var motherLiving = document.getElementById('motherLiving');
	var motherNotLiving = document.getElementById('motherNotLiving');
	var fatherLiving = document.getElementById('fatherLiving');
	var fatherNotLiving = document.getElementById('fatherNotLiving');
	var hadTramua = document.getElementById('hadTramua');
	var noTrauma = document.getElementById('noTrauma');
	var sibsClose = document.getElementById('sibsClose');
	var sibsNotClose = document.getElementById('sibsNotClose');
	var dadIsClose = document.getElementById('dadIsClose');
	var dadNotClose = document.getElementById('dadNotClose');
	var childAbused = document.getElementById('childAbused');
	var childNotAbused = document.getElementById('childNotAbused');
	var meMomClose = document.getElementById('meMomClose');
	var meMomNotClose = document.getElementById('meMomNotClose');
	var hadAngerChild = document.getElementById('hadAngerChild');
	var noAngerChild = document.getElementById('noAngerChild');
	var haveOtherEvents = document.getElementById('haveOtherEvents');
	var noOtherEvents = document.getElementById('noOtherEvents');
	var sawViolence = document.getElementById('sawViolence');
	var didntSeeViolence = document.getElementById('didntSeeViolence');
	var hadAngerChild = document.getElementById('hadAngerChild');
	var noAngerChild = document.getElementById('noAngerChild');

	//PROCESS THE DROPDOWN MENU
	raisedBy.selectedIndex = json_data.raisedBy;

	//PROCESS RADIO BUTTONS
	setRadioElement(json_data.momAlive, motherLiving, motherNotLiving);
	setRadioElement(json_data.dadAlive, fatherLiving, fatherNotLiving);
	setRadioElement(json_data.childTrama, hadTramua, noTrauma);
	setRadioElement(json_data.siblingsClose, sibsClose, sibsNotClose);
	setRadioElement(json_data.dadClose, dadIsClose, dadNotClose);
	setRadioElement(json_data.momClose, meMomClose, meMomNotClose);
	setRadioElement(json_data.wasAbused, childAbused, childNotAbused);
	setRadioElement(json_data.childAnger, hadAngerChild, noAngerChild);
	setRadioElement(json_data.otherChild, haveOtherEvents, noOtherEvents);
	setRadioElement(json_data.parentViolence, sawViolence, didntSeeViolence);	

	back = document.getElementById('back_btn');

	childTraumaRadio();
	childAbusedRadio();
	hadChildAngerRadio();
	otherEventsHelpRadio();
	parentsFoughtRadio();
}

function continue_am_history1() {
	var proceed = true;

	//DYNAMIC TRIGGERS
	var hadTramua = document.getElementById('hadTramua');
	var childAbused = document.getElementById('childAbused');
	var hadAngerChild = document.getElementById('hadAngerChild');
	var haveOtherEvents = document.getElementById('haveOtherEvents');
	var sawViolence = document.getElementById('sawViolence');

	//DYNAMIC FIELDS
	var traumaExplain = document.getElementById('traumaExplain');
	var abusedBy = document.getElementById('abusedBy');
	var abuseImpact = document.getElementById('abuseImpact');
	var otherChildExplain = document.getElementById('otherChildExplain');
	var childAngerExplain = document.getElementById('childAngerExplain');
	var parentViolenceExplain = document.getElementById('parentViolenceExplain');
	var parentViolenceImpact = document.getElementById('parentViolenceImpact');

	//POST FIELDS
	var m_traumaExplain = document.getElementById('m_traumaExplain');
	var m_howLeftHome = document.getElementById('m_howLeftHome');
	var m_abusedBy = document.getElementById('m_abusedBy');
	var m_abuseImpact = document.getElementById('m_abuseImpact');
	var m_childAngerExplain = document.getElementById('m_childAngerExplain');
	var m_otherChildExplain = document.getElementById('m_otherChildExplain');
	var m_parentViolenceExplain = document.getElementById('m_parentViolenceExplain');
	var m_parentViolenceImpact = document.getElementById('m_parentViolenceImpact');


	// //PROCESS DYNAMIC FIELDS
	postDynamicFields(hadTramua, traumaExplain, m_traumaExplain);
	postDynamicFields(childAbused, abusedBy, m_abusedBy);
	postDynamicFields(childAbused, abuseImpact, m_abuseImpact);
	postDynamicFields(hadAngerChild, childAngerExplain, m_childAngerExplain);
	postDynamicFields(haveOtherEvents, otherChildExplain, m_otherChildExplain);
	postDynamicFields(sawViolence, parentViolenceExplain, m_parentViolenceExplain);
	postDynamicFields(sawViolence, parentViolenceImpact, m_parentViolenceImpact);

	document.getElementById('back_btn').value = 'false';

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

//CONTROL FUNCTIONS
function talkMyself() {
	var whatSayYou_label = document.getElementById('whatSayYou_label');
	var whatSayYou = document.getElementById('whatSayYou');

	if (document.getElementById('talkToMyself').checked === true) {
		whatSayYou_label.style.opacity = '1.0';
		whatSayYou.disabled = false;
		whatSayYou.style.opacity = '1.0';
	}
	else {
		whatSayYou_label.style.opacity = '0.3';
		whatSayYou.style.opacity = '0.3';
		whatSayYou.disabled = true;
	}
}

function leaveSceneCheckbox() {
	var leaveScene = document.getElementById('leaveScene');
	var howLongLeaveScene = document.getElementById('howLongLeaveScene');
	var whatDoLeave = document.getElementById('whatDoLeave');
	var howLongLeaveScene_label = document.getElementById('howLongLeaveScene_label');
	var whatDoLeave_label = document.getElementById('whatDoLeave_label');

	if (leaveScene.checked === true) {
		howLongLeaveScene.disabled = false;
		whatDoLeave.disabled = false;
		howLongLeaveScene_label.style.opacity = '1.0';
		whatDoLeave_label.style.opacity = '1.0';
		whatDoLeave.style.opacity = '1.0';
		howLongLeaveScene.style.opacity = '1.0';
	}
	else {
		whatDoLeave.style.opacity = '0.3';
		howLongLeaveScene.style.opacity = '0.3';
		howLongLeaveScene.disabled = true;
		whatDoLeave.disabled = true;
		howLongLeaveScene_label.style.opacity = '0.3';
		whatDoLeave_label.style.opacity = '0.3';
	}
}

function howRelaxCheckbox() {
	var relax = document.getElementById('relax');
	var howRelax_label = document.getElementById('howRelax_label');
	var howRelax = document.getElementById('howRelax');

	if (relax.checked === true) {
		howRelax_label.style.opacity = '1.0';
		howRelax.disabled = false;
		howRelax.style.opacity = '1.0';
	}
	else {
		howRelax_label.style.opacity = '0.3';
		howRelax.style.opacity = '0.3';
		howRelax.disabled = true;
	}
}

function otherControlCheckbox() {
	var otherControlAnger = document.getElementById('otherControlAnger');
	var doWhatOtherControl_label = document.getElementById('doWhatOtherControl_label');
	var doWhatOtherControl = document.getElementById('doWhatOtherControl');

	if (otherControlAnger.checked === true) {
		doWhatOtherControl_label.style.opacity = '1.0';
		doWhatOtherControl.disabled = false;
		doWhatOtherControl.style.opacity = '1.0';
	}
	else {
		doWhatOtherControl_label.style.opacity = '0.3';
		doWhatOtherControl.style.opacity = '0.3';
		doWhatOtherControl.disabled = true;
	}
}

function initalize_am_control(json_data) {
	talkMyself();
	leaveSceneCheckbox();
	howRelaxCheckbox();
	otherControlCheckbox();
}

function continue_to_am_final() {
	var proceed = true;

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

function continue_to_amViewForm() {
	var proceed = true;

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

function initializeAllCheckBoxes(trigger, box) {
	if (String(trigger) === 'true') {
		box.checked = true;
	}
	else {
		box.checked = false;
	}
}

//ANGER HISTORY FUNCTIONS
function turnOnAH1() {
	var otherRecentV = document.getElementById('otherRecentV');
	var explain_Label = document.getElementById('explain_Label');
	var otherExplainRecentV = document.getElementById('otherExplainRecentV');

	if (otherRecentV.checked === true) {
		otherExplainRecentV.disabled = false;
		otherExplainRecentV.style.opacity = '1.0';
		explain_Label.style.opacity = '1.0';
	}
	else {
		otherExplainRecentV.value = '';
		otherExplainRecentV.style.opacity = '0.3';
		explain_Label.style.opacity = '0.3';
		otherExplainRecentV.disabled = true;
	}
}

function AHcompletedRadioActivate() {
	var notCompleted = document.getElementById('notCompleted');
	var reasonNotCompleteRecentV_label = document.getElementById('reasonNotCompleteRecentV_label');
	var reasonNotCompleteRecentV = document.getElementById('reasonNotCompleteRecentV');

	if (notCompleted.checked === true) {
		reasonNotCompleteRecentV.disabled = false;
		reasonNotCompleteRecentV.style.opacity = '1.0';
		reasonNotCompleteRecentV_label.style.opacity = '1.0';
	}

	else {
		reasonNotCompleteRecentV.value = '';
		reasonNotCompleteRecentV.style.opacity = '0.3';
		reasonNotCompleteRecentV_label.style.opacity = '0.3';		
		reasonNotCompleteRecentV.disabled = true;
	}
}

function psychoClick() {
	var wasTreated = document.getElementById('wasTreated');

	var psychoWhyRecentV_label = document.getElementById('psychoWhyRecentV_label');
	var longAgoTreatment_label = document.getElementById('longAgoTreatment_label');
	var longAgoTreatRecentVmos_label = document.getElementById('longAgoTreatRecentVmos_label');
	var longAgoTreatRecentVyrs_label = document.getElementById('longAgoTreatRecentVyrs_label');
	var didCompleteTreatRecentV_label = document.getElementById('didCompleteTreatRecentV_label');
	var notCompleted_label = document.getElementById('notCompleted_label2');
	var Completed_label = document.getElementById('Completed_label');

	var didComplete = document.getElementById('didComplete');
	var notCompleted = document.getElementById('notCompleted');

	var psychoWhyRecentV = document.getElementById('psychoWhyRecentV');
	var longAgoTreatRecentVmos = document.getElementById('longAgoTreatRecentVmos');
	var longAgoTreatRecentVyrs = document.getElementById('longAgoTreatRecentVyrs');


	if (wasTreated.checked === true) {
		psychoWhyRecentV.disabled = false;
		longAgoTreatRecentVmos.disabled = false;
		longAgoTreatRecentVyrs.disabled = false;

		didComplete.disabled = false;
		notCompleted.disabled = false;

		psychoWhyRecentV_label.style.opacity = '1.0';
		longAgoTreatment_label.style.opacity = '1.0';
		longAgoTreatRecentVmos_label.style.opacity = '1.0';
		longAgoTreatRecentVyrs_label.style.opacity = '1.0';
		didCompleteTreatRecentV_label.style.opacity = '1.0';
		notCompleted_label.style.opacity = '1.0';
		Completed_label.style.opacity = '1.0';

		psychoWhyRecentV.style.opacity = '1.0';	
		longAgoTreatRecentVmos.style.opacity = '1.0';	
		longAgoTreatRecentVyrs.style.opacity = '1.0';	

		AHcompletedRadioActivate();
	}

	else {
		psychoWhyRecentV.value = '';
		longAgoTreatRecentVmos.value = '0';
		longAgoTreatRecentVyrs.value = '0';

		didComplete.checked = true;		
		
		opacityLow(psychoWhyRecentV_label);
		opacityLow(longAgoTreatment_label);
		opacityLow(longAgoTreatRecentVmos_label);
		opacityLow(longAgoTreatRecentVyrs_label);
		opacityLow(didCompleteTreatRecentV_label);
		opacityLow(notCompleted_label);
		opacityLow(Completed_label);

		opacityLow(psychoWhyRecentV);
		opacityLow(longAgoTreatRecentVmos);
		opacityLow(longAgoTreatRecentVyrs);

		AHcompletedRadioActivate();

		psychoWhyRecentV.disabled = true;
		longAgoTreatRecentVmos.disabled = true;
		longAgoTreatRecentVyrs.disabled = true;
		didComplete.disabled = true;
		notCompleted.disabled = true;
	}	
}

function initialize_am_angerHistory(json_data) {
	//CHECKE BOXES
	var physicalRecentV = document.getElementById('physicalRecentV');
	var verbalRecentV = document.getElementById('verbalRecentV');
	var threatsRecentV = document.getElementById('threatsRecentV');
	var propertyRecentV = document.getElementById('propertyRecentV');
	var otherRecentV = document.getElementById('otherRecentV');
	var wasTense = document.getElementById('wasTense');
	var hadRush = document.getElementById('hadRush');
	var feltStrong = document.getElementById('feltStrong');

	//RADIO BUTTONS
	var wasTreated = document.getElementById('wasTreated');
	var notTreated = document.getElementById('notTreated');
	var didComplete = document.getElementById('didComplete');
	var notCompleted = document.getElementById('notCompleted');

	setRadioElement(json_data.psychoRecentV, wasTreated, notTreated);
	setRadioElement(json_data.didCompleteTreatRecentV, didComplete, notCompleted);

	initializeAllCheckBoxes(json_data.physicalRecentV, physicalRecentV);
	initializeAllCheckBoxes(json_data.verbalRecentV, verbalRecentV);
	initializeAllCheckBoxes(json_data.threatsRecentV, threatsRecentV);
	initializeAllCheckBoxes(json_data.propertyRecentV, propertyRecentV);
	initializeAllCheckBoxes(json_data.otherRecentV, otherRecentV);
	initializeAllCheckBoxes(json_data.wasTense, wasTense);
	initializeAllCheckBoxes(json_data.hadRush, hadRush);
	initializeAllCheckBoxes(json_data.feltStrong, feltStrong);

	// AHcompletedRadioActivate();
	turnOnAH1();
	psychoClick();
}

function continue_to_am_AH2() {
	var proceed = true;
	var back = document.getElementById('back_btn');

	//DYNAMIC POSTING FIELDS
	var m_physicalRecentV = document.getElementById('m_physicalRecentV');
	var m_verbalRecentV = document.getElementById('m_verbalRecentV');
	var m_threatsRecentV = document.getElementById('m_threatsRecentV');
	var m_propertyRecentV = document.getElementById('m_propertyRecentV');
	var m_otherRecentV = document.getElementById('m_otherRecentV');
	var m_otherExplainRecentV = document.getElementById('m_otherExplainRecentV');
	var m_wasTense = document.getElementById('m_wasTense');
	var m_hadRush = document.getElementById('m_hadRush');
	var m_feltStrong = document.getElementById('m_feltStrong');
	var m_psychoRecentV = document.getElementById('m_psychoRecentV');
	var m_psychoWhyRecentV = document.getElementById('m_psychoWhyRecentV');
	var m_longAgoTreatRecentVmos = document.getElementById('m_longAgoTreatRecentVmos');
	var m_longAgoTreatRecentVyrs = document.getElementById('m_longAgoTreatRecentVyrs');
	var m_didCompleteTreatRecentV = document.getElementById('m_didCompleteTreatRecentV');
	var m_reasonNotCompleteRecentV = document.getElementById('m_reasonNotCompleteRecentV');

	//CHECKBOXES
	var physicalRecentV = document.getElementById('physicalRecentV');
	var verbalRecentV = document.getElementById('verbalRecentV');
	var threatsRecentV = document.getElementById('threatsRecentV');
	var propertyRecentV = document.getElementById('propertyRecentV');
	var otherRecentV = document.getElementById('otherRecentV');
	var wasTense = document.getElementById('wasTense');
	var hadRush = document.getElementById('hadRush');
	var feltStrong = document.getElementById('feltStrong');

	//TEXT FIELDS
	var otherExplainRecentV = document.getElementById('otherExplainRecentV');
	var psychoWhyRecentV = document.getElementById('psychoWhyRecentV');
	var longAgoTreatRecentVmos = document.getElementById('longAgoTreatRecentVmos');
	var longAgoTreatRecentVyrs = document.getElementById('longAgoTreatRecentVyrs');
	var reasonNotCompleteRecentV = document.getElementById('reasonNotCompleteRecentV');

	//DYNAMIC RADIOS
	var didComplete = document.getElementById('didComplete');

	//TRIGGERS
	var wasTreated = document.getElementById('wasTreated');

	//GET CHECKBOX VALUES AND SEND TO POST FIELDS
	postCheckboxValue(physicalRecentV, m_physicalRecentV);
	postCheckboxValue(verbalRecentV, m_verbalRecentV);
	postCheckboxValue(threatsRecentV, m_threatsRecentV);
	postCheckboxValue(propertyRecentV, m_propertyRecentV);
	postCheckboxValue(otherRecentV, m_otherRecentV);
	postCheckboxValue(wasTense, m_wasTense);
	postCheckboxValue(hadRush, m_hadRush);
	postCheckboxValue(feltStrong, m_feltStrong);

	//PROCESS DYNAMIC RADIO FIELDS
	if (otherRecentV.checked === true) {
		m_otherExplainRecentV.value = otherExplainRecentV.value;
	}
	else {
		m_otherExplainRecentV.value = 'N/A';
	}


	if (wasTreated.checked === true) {
		m_psychoRecentV.value = 'True';
		m_psychoWhyRecentV.value = psychoWhyRecentV.value;
		m_longAgoTreatRecentVmos.value = longAgoTreatRecentVmos.value;
		m_longAgoTreatRecentVyrs.value = longAgoTreatRecentVyrs.value;

		if (didComplete.checked === true) {
			m_didCompleteTreatRecentV.value = 'True';
			m_reasonNotCompleteRecentV.value = 'N/A';
		}
		else {
			m_didCompleteTreatRecentV.value = 'False';
			m_reasonNotCompleteRecentV.value = reasonNotCompleteRecentV.value;
		}
	}
	else {
		m_psychoRecentV.value = 'False';
		m_didCompleteTreatRecentV.value = 'False';
		m_reasonNotCompleteRecentV.value = 'N/A';
		m_psychoWhyRecentV.value = 'N/A';
		m_longAgoTreatRecentVmos.value = '0';
		m_longAgoTreatRecentVyrs.value = '0';
	}

	back.value = 'false';

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

//AM ANGER HISTORY SECTION II FUNCTIONS
function explainDep() {
	var hasExperience = document.getElementById('hasExperience');
	var depress30ExplainRecentV = document.getElementById('depress30ExplainRecentV');
	var depress30ExplainRecentV_label = document.getElementById('depress30ExplainRecentV_label');

	if (hasExperience.checked === true) {
		depress30ExplainRecentV.disabled = false;
		depress30ExplainRecentV.style.opacity = '1.0';
		depress30ExplainRecentV_label.style.opacity = '1.0';
	}
	else {
		depress30ExplainRecentV_label.style.opacity = '0.3';
		depress30ExplainRecentV.value = ''
		depress30ExplainRecentV.style.opacity = '0.3';
		depress30ExplainRecentV.disabled = true;
	}
}

function tensionRadio() {
	var hasTension = document.getElementById('hasTension');
	var anxietyExplainRecentV = document.getElementById('anxietyExplainRecentV');
	var anxietyExplainRecentV_label = document.getElementById('anxietyExplainRecentV_label');

	if (hasTension.checked === true) {
		anxietyExplainRecentV.disabled = false;
		anxietyExplainRecentV.style.opacity = '1.0';
		anxietyExplainRecentV_label.style.opacity = '1.0';
	}
	else {
		anxietyExplainRecentV_label.style.opacity = '0.3';
		anxietyExplainRecentV.value = ''
		anxietyExplainRecentV.style.opacity = '0.3';
		anxietyExplainRecentV.disabled = true;
	}
}

function halluRadio() {
	var hasHallu = document.getElementById('hasHallu');
	var hallucinationLastV = document.getElementById('hallucinationLastV');
	var hallucinationLastV_label = document.getElementById('hallucinationLastV_label');

	if (hasHallu.checked === true) {
		hallucinationLastV.disabled = false;
		hallucinationLastV.style.opacity = '1.0';
		hallucinationLastV.style.opacity = '1.0';
	}
	else {
		hallucinationLastV_label.style.opacity = '0.3';
		hallucinationLastV.value = ''
		hallucinationLastV.style.opacity = '0.3';
		hallucinationLastV.disabled = true;
	}
}

function troubleRadioAH2() {
	var hasTroubleAH2 = document.getElementById('hasTroubleAH2');
	var understandingExplainRecentV_label = document.getElementById('understandingExplainRecentV_label');
	var understandingExplainRecentV = document.getElementById('understandingExplainRecentV');

	if (hasTroubleAH2.checked === true) {
		understandingExplainRecentV.disabled = false;
		understandingExplainRecentV.style.opacity = '1.0';
		understandingExplainRecentV_label.style.opacity = '1.0';
	}
	else {
		understandingExplainRecentV.value = '';
		understandingExplainRecentV_label.style.opacity = '0.3'
		understandingExplainRecentV.style.opacity = '0.3';
		understandingExplainRecentV.disabled = true;
	}
}

function troubleControlAH2() {
	var canControl = document.getElementById('canControl');
	var lastTimeTroubleControl_label = document.getElementById('lastTimeTroubleControl_label');
	var controlTrigger_label = document.getElementById('controlTrigger_label');
	var lastTimeTroubleControl = document.getElementById('lastTimeTroubleControl');
	var controlTrigger = document.getElementById('controlTrigger');

	if (canControl.checked === true) {
		lastTimeTroubleControl.disabled = false;
		controlTrigger.disabled = false;

		lastTimeTroubleControl_label.style.opacity = '1.0';
		controlTrigger_label.style.opacity = '1.0';
		lastTimeTroubleControl.style.opacity = '1.0';
		controlTrigger.style.opacity = '1.0';
	}

	else {
		lastTimeTroubleControl_label.style.opacity = '0.3';
		controlTrigger_label.style.opacity = '0.3';
		lastTimeTroubleControl.style.opacity = '0.3';
		controlTrigger.style.opacity = '0.3';

		lastTimeTroubleControl.value = '';
		controlTrigger.value = '';

		lastTimeTroubleControl.disabled = true;
		controlTrigger.disabled = true;
	}
}


function activateAH2SubSuicide() { //lowest level radio button
	var haveAttempted = document.getElementById('haveAttempted')
	var hasAttemptedExplainRecentV = document.getElementById('hasAttemptedExplainRecentV');
	var hasAttemptedExplainRecentV_label = document.getElementById('hasAttemptedExplainRecentV_label');

	if (haveAttempted.checked === true) {
		hasAttemptedExplainRecentV.disabled = false;
		hasAttemptedExplainRecentV.style.opacity = '1.0';
		hasAttemptedExplainRecentV_label.style.opacity = '1.0';
	}

	else {
		hasAttemptedExplainRecentV.style.opacity = '0.3';
		hasAttemptedExplainRecentV_label.style.opacity = '0.3';
		hasAttemptedExplainRecentV.value = '';
		hasAttemptedExplainRecentV.disabled = true;
	}
}

function planRadioAH2() { 
	//labels
	var suicideTodayExplainRecentV_label = document.getElementById('suicideTodayExplainRecentV_label');
	var haveAttempted_label = document.getElementById('haveAttempted_label');
	var haveNotAttempted_label = document.getElementById('haveNotAttempted_label');
	var hasAttemptedSuicide_label = document.getElementById('hasAttemptedSuicide_label');

	//fields
	var suicideTodayExplainRecentV = document.getElementById('suicideTodayExplainRecentV');
	var haveAttempted = document.getElementById('haveAttempted');
	var haveNotAttempted = document.getElementById('haveNotAttempted');

	if (doesHavePlan.checked === true) {
		suicideTodayExplainRecentV_label.style.opacity = '1.0';
		suicideTodayExplainRecentV.disabled = false;
		suicideTodayExplainRecentV.style.opacity = '1.0';
	}

	else {
		suicideTodayExplainRecentV_label.style.opacity = '0.3';
		suicideTodayExplainRecentV.style.opacity = '0.3';
		suicideTodayExplainRecentV.value = '';
		suicideTodayExplainRecentV.disabled = true;
	}

}

function midLevelSubAH2() {
	var isSuicidalToday = document.getElementById('isSuicidalToday');
	//labels
	var suicideTodayPlanRecentV_label = document.getElementById('suicideTodayPlanRecentV_label');
	var doesHavePlan_label = document.getElementById('doesHavePlan_label');
	var doesNotHavePlan_label = document.getElementById('doesNotHavePlan_label');

	//fields
	var doesHavePlan = document.getElementById('doesHavePlan');
	var doesNotHavePlan = document.getElementById('doesNotHavePlan');

	if (isSuicidalToday.checked === true) {
		doesHavePlan.disabled = false;
		doesNotHavePlan.disabled = false;

		suicideTodayPlanRecentV_label.style.opacity = '1.0';
		doesHavePlan_label.style.opacity = '1.0';
		doesNotHavePlan_label.style.opacity = '1.0';

		doesHavePlan.style.opacity = '1.0';
		doesNotHavePlan.style.opacity = '1.0';
	}

	else {
		doesNotHavePlan.checked = true;
		planRadioAH2();

		suicideTodayPlanRecentV_label.style.opacity = '0.3';
		doesHavePlan_label.style.opacity = '0.3';
		doesNotHavePlan_label.style.opacity = '0.3';

		doesHavePlan.style.opacity = '0.3';
		doesNotHavePlan.style.opacity = '0.3';

		doesHavePlan.disabled = true;
		doesNotHavePlan.disabled = true;
	}
}

function suicide30recent() { //top level radio button
	var suicideThoughts = document.getElementById('suicideThoughts');

	//labels
	var suicide30ExplainRecentV_label = document.getElementById('suicide30ExplainRecentV_label');
	var suicideTodayRecentV_label = document.getElementById('suicideTodayRecentV_label');
	var isSuicidalToday_label = document.getElementById('isSuicidalToday_label');
	var isNotSuicidalToday_label = document.getElementById('isNotSuicidalToday_label');

	//fields
	var suicide30ExplainRecentV = document.getElementById('suicide30ExplainRecentV');
	var isSuicidalToday = document.getElementById('isSuicidalToday');
	var isNotSuicidalToday = document.getElementById('isNotSuicidalToday');

	var hasAttemptedSuicide_label = document.getElementById('hasAttemptedSuicide_label');
	var haveAttempted_label = document.getElementById('haveAttempted_label');
	var haveNotAttempted_label = document.getElementById('haveNotAttempted_label');
	var haveAttempted = document.getElementById('haveAttempted');
	var haveNotAttempted = document.getElementById('haveNotAttempted');


	if (suicideThoughts.checked === true) {
		suicide30ExplainRecentV.disabled = false;
		isSuicidalToday.disabled = false;
		isNotSuicidalToday.disabled = false;
		haveAttempted.disabled = false;
		haveNotAttempted.disabled = false;

		suicide30ExplainRecentV_label.style.opacity = '1.0';
		suicideTodayRecentV_label.style.opacity = '1.0';
		isSuicidalToday_label.style.opacity = '1.0';
		isNotSuicidalToday_label.style.opacity = '1.0';

		suicide30ExplainRecentV.style.opacity = '1.0';
		isSuicidalToday.style.opacity = '1.0';
		isNotSuicidalToday.style.opacity = '1.0';

		opacityHigh(hasAttemptedSuicide_label);
		opacityHigh(haveAttempted_label);
		opacityHigh(haveNotAttempted_label);
		opacityHigh(haveAttempted);
		opacityHigh(haveNotAttempted);
	}

	else {
		isNotSuicidalToday.checked = true;
		haveNotAttempted.checked = true;
		midLevelSubAH2();
		activateAH2SubSuicide();

		opacityLow(hasAttemptedSuicide_label);
		opacityLow(haveAttempted_label);
		opacityLow(haveNotAttempted_label);
		opacityLow(haveAttempted);
		opacityLow(haveNotAttempted);

		haveAttempted.disabled = true;
		haveNotAttempted.disabled = true;

		suicide30ExplainRecentV_label.style.opacity = '0.3';
		suicideTodayRecentV_label.style.opacity = '0.3';
		isSuicidalToday_label.style.opacity = '0.3';
		isNotSuicidalToday_label.style.opacity = '0.3';

		suicide30ExplainRecentV.style.opacity = '0.3';
		isSuicidalToday.style.opacity = '0.3';
		isNotSuicidalToday.style.opacity = '0.3';

		suicide30ExplainRecentV.value = '';

		suicide30ExplainRecentV.disabled = true;
		isSuicidalToday.disabled = true;
		isNotSuicidalToday.disabled = true;
	}

	activateAH2SubSuicide();
}

function initialize_am_angerHistory2(json_data) {
	//RADIO BUTTONS
	var hasExperience = document.getElementById('hasExperience');
	var noExperience = document.getElementById('noExperience');
	var hasTension = document.getElementById('hasTension');
	var noTension = document.getElementById('noTension');
	var hasHallu = document.getElementById('hasHallu');
	var noHallu = document.getElementById('noHallu');
	var hasTroubleAH2 = document.getElementById('hasTroubleAH2');
	var noTroubleAH2 = document.getElementById('noTroubleAH2');	
	var canControl = document.getElementById('canControl');
	var canNotControl = document.getElementById('canNotControl');
	var suicideThoughts = document.getElementById('suicideThoughts');
	var noSuicideThoughts = document.getElementById('noSuicideThoughts');
	var isSuicidalToday = document.getElementById('isSuicidalToday');
	var isNotSuicidalToday = document.getElementById('isNotSuicidalToday');
	var doesHavePlan = document.getElementById('doesHavePlan');
	var doesNotHavePlan = document.getElementById('doesNotHavePlan');
	var haveAttempted = document.getElementById('haveAttempted');
	var haveNotAttempted = document.getElementById('haveNotAttempted');

	setRadioElement(json_data.depress30RecentV, hasExperience, noExperience);
	setRadioElement(json_data.anxietyRecentV, hasTension, noTension);
	setRadioElement(json_data.hallucinationRecentV, hasHallu, noHallu);
	setRadioElement(json_data.understandingRecentV, hasTroubleAH2, noTroubleAH2);
	setRadioElement(json_data.troubleControlRecentV, canControl, canNotControl);
	setRadioElement(json_data.suicide30RecentV, suicideThoughts, noSuicideThoughts);
	setRadioElement(json_data.suicideTodayRecentV, isSuicidalToday, isNotSuicidalToday);
	setRadioElement(json_data.suicideTodayPlanRecentV, doesHavePlan, doesNotHavePlan);
	setRadioElement(json_data.hasAttemptedSuicide, haveAttempted, haveNotAttempted);


	explainDep();
	tensionRadio();
	halluRadio();
	troubleRadioAH2();
	troubleControlAH2();
	suicide30recent();
}

function proceed_to_section3() {
	var proceed = true;
	var back = document.getElementById('back_btn');

	//M_ELEMENTS
	var m_depress30RecentV = document.getElementById('m_depress30RecentV');
	var m_depress30ExplainRecentV = document.getElementById('m_depress30ExplainRecentV');
	var m_anxietyRecentV = document.getElementById('m_anxietyRecentV');
	var m_anxietyExplainRecentV = document.getElementById('m_anxietyExplainRecentV');
	var m_hallucinationRecentV = document.getElementById('m_hallucinationRecentV');
	var m_hallucinationLastV = document.getElementById('m_hallucinationLastV');
	var m_understandingRecentV = document.getElementById('m_understandingRecentV');
	var m_understandingExplainRecentV = document.getElementById('m_understandingExplainRecentV');
	var m_troubleControlRecentV = document.getElementById('m_troubleControlRecentV');
	var m_lastTimeTroubleControl = document.getElementById('m_lastTimeTroubleControl');
	var m_controlTrigger = document.getElementById('m_controlTrigger');
	var m_suicide30ExplainRecentV = document.getElementById('m_suicide30ExplainRecentV');
	var m_suicideTodayRecentV = document.getElementById('m_suicideTodayRecentV');
	var m_suicideTodayPlanRecentV = document.getElementById('m_suicideTodayPlanRecentV');
	var m_suicideTodayExplainRecentV = document.getElementById('m_suicideTodayExplainRecentV');
	var m_hasAttemptedSuicide = document.getElementById('m_hasAttemptedSuicide');
	var m_hasAttemptedExplainRecentV = document.getElementById('m_hasAttemptedExplainRecentV');

	//TRIGGERS
	var hasExperience = document.getElementById('hasExperience');
	var hasTension = document.getElementById('hasTension');
	var hasHallu = document.getElementById('hasHallu');
	var hasTroubleAH2 = document.getElementById('hasTroubleAH2');
	var canControl = document.getElementById('canControl');
	var suicideThoughts = document.getElementById('suicideThoughts');

	//SUB TRIGGERS
	var isSuicidalToday = document.getElementById('isSuicidalToday');
	var doesHavePlan = document.getElementById('doesHavePlan');
	var haveAttempted = document.getElementById('haveAttempted');

	//NORMAL DYNAMIC TEXT FIELDS
	var depress30ExplainRecentV = document.getElementById('depress30ExplainRecentV');
	var anxietyExplainRecentV = document.getElementById('anxietyExplainRecentV');
	var hallucinationLastV = document.getElementById('hallucinationLastV');
	var understandingExplainRecentV = document.getElementById('understandingExplainRecentV');
	var lastTimeTroubleControl = document.getElementById('lastTimeTroubleControl');
	var controlTrigger = document.getElementById('controlTrigger');
	var suicide30ExplainRecentV = document.getElementById('suicide30ExplainRecentV');

	processDynamicTextPostValue(hasExperience, depress30ExplainRecentV, m_depress30ExplainRecentV);
	processDynamicTextPostValue(hasTension, anxietyExplainRecentV, m_anxietyExplainRecentV);
	processDynamicTextPostValue(hasHallu, hallucinationLastV, m_hallucinationLastV);
	processDynamicTextPostValue(hasTroubleAH2, understandingExplainRecentV, m_understandingExplainRecentV);
	processDynamicTextPostValue(canControl, lastTimeTroubleControl, m_lastTimeTroubleControl);
	processDynamicTextPostValue(canControl, controlTrigger, m_controlTrigger);
	processDynamicTextPostValue(suicideThoughts, suicide30ExplainRecentV, m_suicide30ExplainRecentV);

	postDynamicRadioButtons(hasExperience, m_depress30RecentV);
	postDynamicRadioButtons(hasTension, m_anxietyRecentV);
	postDynamicRadioButtons(hasHallu, m_hallucinationRecentV);
	postDynamicRadioButtons(hasTroubleAH2, m_understandingRecentV);
	postDynamicRadioButtons(canControl, m_troubleControlRecentV);
	postDynamicRadioButtons(suicideThoughts, m_suicide30RecentV);

	if (suicideThoughts.checked === true) {
		postDynamicRadioButtons(isSuicidalToday, m_suicideTodayRecentV);
		postDynamicRadioButtons(haveAttempted, m_hasAttemptedSuicide);
		m_suicide30ExplainRecentV.value = suicide30ExplainRecentV.value;

		if (isSuicidalToday.checked === true) {
			postDynamicRadioButtons(doesHavePlan, m_suicideTodayPlanRecentV);
			m_suicideTodayExplainRecentV.value = suicideTodayExplainRecentV.value;
		}
		else {
			m_suicideTodayPlanRecentV.value = 'False';
			m_suicideTodayExplainRecentV.value = 'N/A';
		}

		if (doesHavePlan.checked === true) {
			m_suicideTodayExplainRecentV.value = suicideTodayExplainRecentV.value;
		}
		else {
			m_suicideTodayExplainRecentV.value = 'N/A';
		}

		if (haveAttempted.checked === true) {
			m_hasAttemptedExplainRecentV.value = hasAttemptedExplainRecentV.value;
		}
		else {
			m_hasAttemptedExplainRecentV.value = 'N/A';
		}
	}

	else {
		m_suicide30ExplainRecentV.value = 'N/A';
		m_suicideTodayExplainRecentV.value = 'N/A';
		m_hasAttemptedExplainRecentV.value = 'N/A';

		m_suicideTodayRecentV.value = 'False';
		m_suicideTodayPlanRecentV.value = 'False';
		m_hasAttemptedSuicide.value = 'False';
	}

	back.value = 'false';

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

function proceed_to_connections() {
	var proceed = true;
	var back = document.getElementById('back_btn');

	back.value = 'false';

	if (proceed === true) {
		document.getElementById('am_demo').submit();
	}
}

//AM ANGER HISTORY SECTION III FUNCTIONS


//DELETE THE ANGER MANAGEMENT FORM
function AmDeleted() {
	document.getElementById('exit_return_form').submit();
}





























