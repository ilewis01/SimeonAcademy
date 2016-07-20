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

function nullTextMustDie(element) {
	if (String(element.value) === '' || String(element.value) === 'NA' || String(element.value) === 'None' || String(element.value) === 'N/A') {
		element.value = '';
	}
}

function nullTextMustDie2(element) {
	if (String(element.value) === '' || String(element.value) === 'None') {
		element.value = '';
	}
}

function nullTextMustDie3(element) {
	if (String(element.value) === '' || String(element.value) === 'NA') {
		element.value = '';
	}
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

function postTextNA(field) {
	if (field.value === '' || field.value === null) {
		field.value = 'N/A';
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

function searchRadio() {
	if (grab('name_radio').checked == true) {
		grab('fname').disabled = false;
		grab('lname').disabled = false;
		opacityHigh(grab('fname'));
		opacityHigh(grab('lname'));

		opacityLow(grab('dob'));
		opacityLow(grab('ss_num'));
		opacityLow(grab('client_ID'));
		grab('dob').disabled = true;
		grab('ss_num').disabled = true;
		grab('client_ID').disabled = true;
	}
	if (grab('dob_radio').checked === true) {
		grab('dob').disabled = false;
		opacityHigh(grab('dob'));

		opacityLow(grab('fname'));
		opacityLow(grab('lname'));
		opacityLow(grab('ss_num'));
		opacityLow(grab('client_ID'));
		grab('fname').disabled = true;
		grab('lname').disabled = true;
		grab('ss_num').disabled = true;
		grab('client_ID').disabled = true;
	}
	if (grab('ss_radio').checked === true) {
		grab('ss_num').disabled = false;
		opacityHigh(grab('ss_num'));

		opacityLow(grab('fname'));
		opacityLow(grab('lname'));
		opacityLow(grab('dob'));
		opacityLow(grab('client_ID'));
		grab('fname').disabled = true;
		grab('lname').disabled = true;
		grab('dob').disabled = true;
		grab('client_ID').disabled = true;
	}
	if (grab('id_radio').checked === true) {
		grab('client_ID').disabled = false;
		opacityHigh(grab('client_ID'));

		opacityLow(grab('fname'));
		opacityLow(grab('lname'));
		opacityLow(grab('dob'));
		opacityLow(grab('ss_num'));
		grab('fname').disabled = true;
		grab('lname').disabled = true;
		grab('dob').disabled = true;
		grab('ss_num').disabled = true;
	}
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
	var proceed = true;
	var m_search_type = grab('m_search_type');

	if (grab('name_radio').checked === true) {
		m_search_type.value = 'name';
	}
	else if (grab('dob_radio').checked === true) {
		m_search_type.value = 'dob';
	}
	else if (grab('ss_radio').checked === true) {
		m_search_type.value = 'ss_num';
	}
	else if (grab('id_radio').checked === true) {
		m_search_type.value = 'ID';
	}

	if (proceed === true) {
		grab('c_search').submit();
	}
}

function toClientOptions(form_id, hasUnfinished) {
	hasUnfinished = String(hasUnfinished);

	if (hasUnfinished == 'True') {
		grab('form_name').value = String(form_id);
		grab('se_id').value = grab('session_id').value;
		var w = 600, h = 500;
		openPopUp('auto', '/hasExistingSession/',w, h);
	}

	else {
		document.getElementById(form_id).submit();
	}
}

function set_session_option() {
	grab('session_id').value = getPopParent('se_id').value;

	if (grab('continue').checked === true) {
		grab('s_option').value = 'continue';
	}
	else if (grab('refresh').checked === true) {
		grab('s_option').value = 'refresh';
	}
	else if (grab('delete').checked === true) {
		grab('s_option').value = 'delete';
	}
}

function processExistingSession() {
	var form 		= null;
	var s_option 	= grab('s_option').value;
	s_option 		= String(s_option);

	if (s_option === 'continue') {
		var f_id = getPopParent('form_name').value;
		f_id = String(f_id);
		form = getPopParent(f_id);
		form.submit();
		window.close();
	}
	else {
		grab('s_form').submit();
	}
}

function finializeSessionResolve() {	
	var eType = grab('exit_type').value;
	eType = String(eType);
	grab('s_form').submit();

	if (eType === 'refresh') {
		var f_id = getPopParent('form_name').value;
		f_id = String(f_id);
		var form = getPopParent(f_id);
		form.submit();
	}

	else if (eType === 'delete') {
		getPopParent('result_form').submit();
	}
}

function new_am() {
	grab('c_form').action = '/am_preliminary/';
	grab('c_form').submit();
}

function new_asi() {
	grab('c_form').action = '/asi_preliminary/';
	grab('c_form').submit();
}

function new_mh() {
	grab('c_form').action = '/mh_preliminary/';
	grab('c_form').submit();
}

function new_sap() {
	grab('c_form').action = '/sap_preliminary/';
	grab('c_form').submit();
}

function new_ut() {
	grab('c_form').action = '/ut_preliminary/';
	grab('c_form').submit();
}

function new_discharge() {
	grab('c_form').action = '/discharge_client/';
	grab('c_form').submit();
}

function get_client_history() {
	grab('c_form').action = '/clientHistory/';
	grab('c_form').submit();
}

function close_session() {
	var w = 500, h = 250;
	openPopUp('auto', '/closeSession/', w, h);
}

function delete_session() {
	var w = 500, h = 250;
	openPopUp('auto', '/deleteSession/', w, h);
}

function return_to_options2() {
	form = document.getElementById('mh_instructions');
	form.action = '/clientOptions/';
	form.submit();
}

function return_to_options3() {
	form = document.getElementById('asi_instructions');
	form.action = '/clientOptions/';
	form.submit();
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

//#####################################################################################################################//
//#####################################################################################################################//
//-------------------------------------------------- DISCHARGE FUNCTIONS ----------------------------------------------//
//#####################################################################################################################//
//#####################################################################################################################//

function init_discharge() {
	grab('reasonRefered').value = '';
	grab('clientAttitude').value = '';
	grab('recommendations').value = '';
}

function exit_discharge() {
	grab('d_form').action = '/clientOptions/';
	grab('d_form').submit();
}

function continue_discharge() {
	var w = 425, h = 325;
	var lefts = Number((screen.width/2) - (w/2));
	var tops = Number((screen.height/2) - (h/2));
	var opWin = window.open('/discharge_viewForm/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
}

function discharge_proceed() {
	grab('d_form').submit();
	getPopParent('d_form').submit();
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//**************************************************** END DISCHARGE **************************************************//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//

//#####################################################################################################################//
//#####################################################################################################################//
//----------------------------------------------------- AM FUNCTIONS --------------------------------------------------//
//#####################################################################################################################//
//#####################################################################################################################//

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
		explain.value = '';
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

	initializeAllCheckBoxes(json_data.angerWorse, angerWorse);
	initializeAllCheckBoxes(json_data.troubleWhenUsing, troubleWhenUsing);
	initializeAllCheckBoxes(json_data.lessAngry, lessAngry);
	initializeAllCheckBoxes(json_data.othersTellMe, othersTellMe);
	initializeAllCheckBoxes(json_data.noConnection, noConnection);
	initializeAllCheckBoxes(json_data.otherConnectionsUsing, otherConnectionsUsing);

	connectionCheck();
}

function post_dynamic_am_connections() {
	var angerWorse = document.getElementById('angerWorse');
	var troubleWhenUsing = document.getElementById('troubleWhenUsing');
	var lessAngry = document.getElementById('lessAngry');
	var othersTellMe = document.getElementById('othersTellMe');
	var noConnection = document.getElementById('noConnection');
	var otherConnectionsUsing = document.getElementById('otherConnectionsUsing');
	var connectionExplain = document.getElementById('connectionExplain');

	postCheckboxValue(angerWorse, m_angerWorse);
	postCheckboxValue(troubleWhenUsing, m_troubleWhenUsing);
	postCheckboxValue(lessAngry, m_lessAngry);
	postCheckboxValue(othersTellMe, m_othersTellMe);
	postCheckboxValue(noConnection, m_noConnection);
	postCheckboxValue(otherConnectionsUsing, m_otherConnectionsUsing);

	if (otherConnectionsUsing.checked === true) {
		m_connectionExplain.value = connectionExplain.value;
	}
	else {
		m_connectionExplain.value = 'N/A';
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
		description.value = '';
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
		selectBox.selectedIndex = 0;
		label.style.opacity = '0.5';
		selectBox.style.opacity = '0.5';
		selectBox.disabled = true;
	}
}

function initalize_am_worst(json_data) {
	var back = document.getElementById('back_btn');

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

	setRadioElement(json_data.useWorst, hadDrugs, noDrugs);
	whoDidItFight.selectedIndex = json_data.whoDidItFight;

	initializeAllCheckBoxes(json_data.physicalWorst, physicalWorst);
	initializeAllCheckBoxes(json_data.verbalWorst, verbalWorst);
	initializeAllCheckBoxes(json_data.threatsWorst, threatsWorst);
	initializeAllCheckBoxes(json_data.propertyWorst, propertyWorst);
	initializeAllCheckBoxes(json_data.otherWorst, otherWorst);

	worstCheck();
	activateWorstRadio();

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('whoWorst'));
		nullTextMustDie(document.getElementById('happenedWorst'));
		nullTextMustDie(document.getElementById('wordThoughtWorst'));
		nullTextMustDie(document.getElementById('howStartWorst'));
		nullTextMustDie(document.getElementById('howEndWorst'));
	}
	else {
		nullTextMustDie2(document.getElementById('whoWorst'));
		nullTextMustDie2(document.getElementById('happenedWorst'));
		nullTextMustDie2(document.getElementById('wordThoughtWorst'));
		nullTextMustDie2(document.getElementById('howStartWorst'));
		nullTextMustDie2(document.getElementById('howEndWorst'));
	}
}

function post_dynamic_am_worst() {
	//M_VALUE ELEMENTS
	var m_useWorst = document.getElementById('m_useWorst');
	var m_whoDidItFight = document.getElementById('m_whoDidItFight');
	var m_physicalWorst = document.getElementById('m_physicalWorst');
	var m_verbalWorst = document.getElementById('m_verbalWorst');
	var m_threatsWorst = document.getElementById('m_threatsWorst');
	var m_propertyWorst = document.getElementById('m_propertyWorst');
	var m_otherWorst = document.getElementById('m_otherWorst');
	var m_otherWorstDescription = document.getElementById('m_otherWorstDescription');

	//TRIGGERS
	var hadDrugs = document.getElementById('hadDrugs');

	// CHECKBOXES
	var physicalWorst = document.getElementById('physicalWorst');
	var verbalWorst = document.getElementById('verbalWorst');
	var threatsWorst = document.getElementById('threatsWorst');
	var propertyWorst = document.getElementById('propertyWorst');
	var otherWorst = document.getElementById('otherWorst');

	// DYNAMIC TEXT FIELDS
	var whoDidItFight = document.getElementById('whoDidItFight');

	postDynamicRadioButtons(hadDrugs, m_useWorst);
	processDynamicTextPostValue(hadDrugs, whoDidItFight, m_whoDidItFight);

	postCheckboxValue(physicalWorst, m_physicalWorst);
	postCheckboxValue(verbalWorst, m_verbalWorst);
	postCheckboxValue(threatsWorst, m_threatsWorst);
	postCheckboxValue(propertyWorst, m_propertyWorst);
	postCheckboxValue(otherWorst, m_otherWorst);

	if (otherWorst.checked === true) {
		m_otherWorstDescription.value = document.getElementById('otherWorstDescription').value;
	}
	else {
		m_otherWorstDescription.value = 'N/A';
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
		otherWhom.value = '';
		otherWhom.style.opacity = '0';
		otherWhom.disabled = true;
	}
}

function initalize_am_target(json_data) {
	var back = document.getElementById('back_btn');

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

	initializeAllCheckBoxes(json_data.angryPartner, angryPartner);
	initializeAllCheckBoxes(json_data.angryParents, angryParents);
	initializeAllCheckBoxes(json_data.angryChildren, angryChildren);
	initializeAllCheckBoxes(json_data.angryPartner, angryPartner);
	initializeAllCheckBoxes(json_data.angryRelatives, angryRelatives);
	initializeAllCheckBoxes(json_data.angryEmployer, angryEmployer);
	initializeAllCheckBoxes(json_data.angryFriends, angryFriends);
	initializeAllCheckBoxes(json_data.angryOther, angryOther);
	initializeAllCheckBoxes(json_data.seldomUpset, seldomUpset);

	amTargetOther();

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('angryAbout'));
	}
	else {
		nullTextMustDie2(document.getElementById('angryAbout'));
	}
}

function post_dynamic_am_target() {
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

	postCheckboxValue(angryPartner, document.getElementById('m_angryPartner'));
	postCheckboxValue(angryParents, document.getElementById('m_angryParents'));
	postCheckboxValue(angryChildren, document.getElementById('m_angryChildren'));
	postCheckboxValue(angryRelatives, document.getElementById('m_angryRelatives'));
	postCheckboxValue(angryEmployer, document.getElementById('m_angryEmployer'));
	postCheckboxValue(angryFriends, document.getElementById('m_angryFriends'));
	postCheckboxValue(angryOther, document.getElementById('m_angryOther'));
	postCheckboxValue(seldomUpset, document.getElementById('m_seldomUpset'));

	if (angryOther.checked === false) {
		document.getElementById('m_otherWhom').value = 'N/A';
	}
	else {
		document.getElementById('m_otherWhom').value = otherWhom.value;
	}

	if (angryAbout.value === '') {
		angryAbout.value = 'N/A';
	}
}

// AM FAMILY OF ORIGIN FUNCTIONS
function initalize_family_origin(json_data) {
	var back = document.getElementById('back_btn');

	var hasLovingMother = document.getElementById('hasLovingMother');
	var hasLovingSiblings = document.getElementById('hasLovingSiblings');
	var hasSuicide = document.getElementById('hasSuicide');
	var noSuicide = document.getElementById('noSuicide');

	initializeAllCheckBoxes(json_data.hasLovingMother, hasLovingMother);
	initializeAllCheckBoxes(json_data.hasLovingSiblings, hasLovingSiblings);
	setRadioElement(json_data.suicideHistory, hasSuicide, noSuicide);

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('kidDadAnger'));
		nullTextMustDie(document.getElementById('kidMomAnger'));
		nullTextMustDie(document.getElementById('kidSiblingAnger'));
		nullTextMustDie(document.getElementById('kidOtherAnger'));
		nullTextMustDie(document.getElementById('learnFamilyAnger'));
	}
	else {
		nullTextMustDie2(document.getElementById('kidDadAnger'));
		nullTextMustDie2(document.getElementById('kidMomAnger'));
		nullTextMustDie2(document.getElementById('kidSiblingAnger'));
		nullTextMustDie2(document.getElementById('kidOtherAnger'));
		nullTextMustDie2(document.getElementById('learnFamilyAnger'));
	}
}

function post_dynamic_am_family() {
	var m_hasLovingMother = document.getElementById('m_hasLovingMother');
	var m_hasLovingSiblings = document.getElementById('m_hasLovingSiblings');
	var m_suicideHistory = document.getElementById('m_suicideHistory');

	var hasLovingMother = document.getElementById('hasLovingMother');
	var hasLovingSiblings = document.getElementById('hasLovingSiblings');
	var hasSuicide = document.getElementById('hasSuicide');

	var hasSuicide = document.getElementById('hasSuicide');

	postCheckboxValue(hasLovingMother, m_hasLovingMother);
	postCheckboxValue(hasLovingSiblings, m_hasLovingSiblings);
	postDynamicRadioButtons(hasSuicide, m_suicideHistory);
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
		box.value = '';
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
		box.value = '';
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

	var onMeds = document.getElementById('onMeds');
	var noMeds = document.getElementById('noMeds');

	initializeAllCheckBoxes(json_data.brainInjury, brainInjury);
	initializeAllCheckBoxes(json_data.stroke, stroke);
	initializeAllCheckBoxes(json_data.epilepsy, epilepsy);
	initializeAllCheckBoxes(json_data.attentionDD, attentionDD);
	initializeAllCheckBoxes(json_data.pms, pms);
	initializeAllCheckBoxes(json_data.depression, depression);
	initializeAllCheckBoxes(json_data.ptsd, ptsd);
	initializeAllCheckBoxes(json_data.otherSeriousIllness, otherSeriousIllness);

	setRadioElement(json_data.currentlyOnMeds, onMeds, noMeds);

	am_problems_check();
	am_problems_radio();
}

function post_dynamic_am_current() {
	//M_VALUES
	var m_brainInjury = document.getElementById('m_brainInjury');
	var m_stroke = document.getElementById('m_stroke');
	var m_epilepsy = document.getElementById('m_epilepsy');
	var m_attentionDD = document.getElementById('m_attentionDD');
	var m_pms = document.getElementById('m_pms');
	var m_depression = document.getElementById('m_depression');
	var m_ptsd = document.getElementById('m_ptsd');
	var m_otherSeriousIllness = document.getElementById('m_otherSeriousIllness');
	var m_describeIssue = document.getElementById('m_describeIssue');
	var m_currentlyOnMeds = document.getElementById('m_currentlyOnMeds');
	var m_whichMeds = document.getElementById('m_whichMeds');

	//ALL ELEMENTS
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

	postCheckboxValue(brainInjury, m_brainInjury);
	postCheckboxValue(depression, m_depression);
	postCheckboxValue(stroke, m_stroke);
	postCheckboxValue(epilepsy, m_epilepsy);
	postCheckboxValue(attentionDD, m_attentionDD);
	postCheckboxValue(pms, m_pms);
	postCheckboxValue(ptsd, m_ptsd);
	postCheckboxValue(otherSeriousIllness, m_otherSeriousIllness);

	postDynamicRadioButtons(onMeds, m_currentlyOnMeds);
	processDynamicTextPostValue(otherSeriousIllness, describeIssue, m_describeIssue);
	processDynamicTextPostValue(onMeds, whichMeds, m_whichMeds);
}

function universal_am_dynamic_post(section) {
	section = String(section);

	if (section === '/am_demographic/') {
		processAMDemoData();
	}
	else if (section === '/am_drugHistory/') {
		processAM_DH_data();
	}
	else if (section === '/am_childhood/') {
		process_am_child_data();
	}
	else if (section === '/am_angerHistory/') {
		process_am_ah1_data();
	}
	else if (section === '/am_angerHistory2/') {
		post_am_dynamic2();
	}
	else if (section === '/am_angerHistory3/') {
		post_dynamic_am_ah3();
	}
	else if (section === '/am_connections/') {
		post_dynamic_am_connections();
	}
	else if (section === '/am_worst/') {
		post_dynamic_am_worst();
	}
	else if (section === '/am_angerTarget/') {
		post_dynamic_am_target();
	}
	else if (section === '/am_familyOrigin/') {
		post_dynamic_am_family();
	}
	else if (section === '/am_problems/') {
		post_dynamic_am_current();
	}
	else if (section === '/am_final/') {
		post_dynamic_am_control();
	}
}

function continue_am_form(section) {
	var proceed = true;
	var next_url = document.getElementById('next_url');
	var form = document.getElementById('am_demo');

	universal_am_dynamic_post(section);

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = next_url.value;
		form.submit();
	}
}

function twoElementRadioSetup(trigger, label, field) {
	if (trigger.checked === true) {
		field.disabled = false;
		opacityHigh(label);
		opacityHigh(field);
	}

	else {
		opacityLow(label);
		opacityLow(field);
		field.value = '';
		field.disabled = true;
	}
}

function twoElementRadioSetupNumber(trigger, label, field) {
	if (trigger.checked === true) {
		field.disabled = false;
		opacityHigh(label);
		opacityHigh(field);
	}

	else {
		opacityLow(label);
		opacityLow(field);
		field.value = 0;
		field.disabled = true;
	}
}

function threeElementRadioSetup(trigger, label1, label2, label3, radio1, defaultRadio) {
	if (trigger.checked === true) {
		radio1.disabled = false;
		defaultRadio.disabled = false;

		opacityHigh(label1);
		opacityHigh(label2);
		opacityHigh(label3);
		opacityHigh(radio1);
		opacityHigh(defaultRadio);
	}

	else {
		opacityLow(label1);
		opacityLow(label2);
		opacityLow(label3);
		opacityLow(radio1);
		opacityLow(defaultRadio);

		defaultRadio.checked = true;

		radio1.disabled = true;
		defaultRadio.disabled = true;
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

	twoElementRadioSetup(hs_drop, resasonDO_label, resasonDO);
}

function healthRadioBtn() {
	//TRIGGER
	var healthy = document.getElementById('healthy');

	//LABELS
	var health_exp_label = document.getElementById('health_exp_label');
	var med_taking_label = document.getElementById('med_taking_label');
	var no_med_label = document.getElementById('no_med_label');
	var yes_med_label = document.getElementById('yes_med_label');
	var explain_label_health = document.getElementById('explain_label_health');

	//ELEMENTS
	var health_exp = document.getElementById('health_exp');
	var no_med = document.getElementById('no_med');
	var on_meds = document.getElementById('on_meds');

	if (healthy.checked == true) {
		health_exp.disabled = false;
		no_med.disabled = false;
		on_meds.disabled = false;

		opacityHigh(health_exp);
		opacityHigh(no_med);
		opacityHigh(on_meds);

		opacityHigh(health_exp_label);
		opacityHigh(med_taking_label);
		opacityHigh(no_med_label);
		opacityHigh(yes_med_label);
		opacityHigh(explain_label_health);
	}

	else {
		no_med.checked = true;
		medsRadioBtn();

		opacityLow(health_exp_label);
		opacityLow(med_taking_label);
		opacityLow(no_med_label);
		opacityLow(yes_med_label);
		opacityLow(explain_label_health);

		health_exp.value = '';
		health_exp.disabled = true;
		no_med.disabled = true;
		on_meds.disabled = true;
	}
}

function medsRadioBtn() {
	var on_meds = document.getElementById('on_meds');
	var explain_label_health = document.getElementById('explain_label_health');
	var whatMedicine = document.getElementById('whatMedicine');

	twoElementRadioSetup(on_meds, explain_label_health, whatMedicine);
}

function initialize_am_demo(json_data) {

	//DROP DOWN MENUS
	var maritalStatus = document.getElementById('maritalStatus');
	var livingSituation = document.getElementById('livingSituation');
	var education = document.getElementById('education');

	//RADIO BUTTONS
	var doesRent = document.getElementById('doesRent');
	var doesOwn = document.getElementById('doesOwn');
	var hs_grad = document.getElementById('hs_grad');
	var hs_drop = document.getElementById('hs_drop');
	var healthy = document.getElementById('healthy');
	var not_healthy = document.getElementById('not_healthy');
	var on_meds = document.getElementById('on_meds');
	var no_med = document.getElementById('no_med');

	//PROCESS DROP DOWN MENUS
	maritalStatus.selectedIndex = json_data.maritalStatus;
	livingSituation.selectedIndex = json_data.livingSituation;
	education.selectedIndex = json_data.education;

	//PROCESS RADIO BUTTONS
	setRadioElement(json_data.own, doesOwn, doesRent);
	setRadioElement(json_data.drop_out, hs_drop, hs_grad);
	setRadioElement(json_data.health_problem, healthy, not_healthy);
	setRadioElement(json_data.medication, on_meds, no_med);

	dropOutRadio();
	healthRadioBtn();

	if (back.value === 'false') {
		nullTextMustDie(document.getElementById('job_title'));
		nullTextMustDie(document.getElementById('employer'));
		nullTextMustDie(document.getElementById('emp_address'));
		nullTextMustDie(document.getElementById('employer_phone'));
	}
}

function start_am_form() {
	var form = document.getElementById('am_instructions');
	form.action = '/am_demographic/';
	form.submit();
}

function processAMDemoData() {
	//M_VALUES
	var m_own = document.getElementById('m_own');
	var m_drop_out = document.getElementById('m_drop_out');
	var m_health_problem = document.getElementById('m_health_problem');
	var m_medication = document.getElementById('m_medication');
	var m_resasonDO = document.getElementById('m_resasonDO');
	var m_health_exp = document.getElementById('m_health_exp');
	var m_whatMedicine = document.getElementById('m_whatMedicine');

	//TRIGGERS AND RADIOS
	var doesOwn = document.getElementById('doesOwn');
	var hs_drop = document.getElementById('hs_drop');
	var not_healthy = document.getElementById('healthy');
	var on_meds = document.getElementById('on_meds');

	//DYNAMIC FIELDS
	var resasonDO = document.getElementById('resasonDO');
	var health_exp = document.getElementById('health_exp');
	var whatMedicine = document.getElementById('whatMedicine');

	postDynamicRadioButtons(doesOwn, m_own);
	postDynamicRadioButtons(hs_drop, m_drop_out);
	postDynamicRadioButtons(not_healthy, m_health_problem);

	processDynamicTextPostValue(hs_drop, resasonDO, m_resasonDO);
	processDynamicTextPostValue(not_healthy, health_exp, m_health_exp);

	if (not_healthy.checked == true) {
		postDynamicRadioButtons(on_meds, m_medication);
		processDynamicTextPostValue(on_meds, whatMedicine, m_whatMedicine);
	}
	else {
		m_medication.value = 'False';
		m_whatMedicine.value = 'N/A';
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
	var form = document.getElementById('am_demo');
	var exit_type_sub = document.getElementById('exit_type_sub');

	exit_type_sub.value = String(e_type);
	form.action = '/exit_am/';
	form.submit();
}

function exit_am2(e_type) {
	var form = document.getElementById('exit_return_form');
	var exit_type_sub = document.getElementById('exit_type_sub');

	exit_type_sub.value = String(e_type);
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
	
	if (String(back.value) == 'false') {
		nullTextMustDie(document.getElementById('first_use_type'));
	}
	else {
		nullTextMustDie2(document.getElementById('first_use_type'));
	}
}

function processAM_DH_data() {
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
	var back = document.getElementById('back_btn');

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

	childTraumaRadio();
	childAbusedRadio();
	hadChildAngerRadio();
	otherEventsHelpRadio();
	parentsFoughtRadio();

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('howLeftHome'));
		nullTextMustDie(document.getElementById('siblingsRelationshipExplain'));
		nullTextMustDie(document.getElementById('dadCloseExplain'));
		nullTextMustDie(document.getElementById('momCloseExplain'));
	}
	else {
		nullTextMustDie3(document.getElementById('howLeftHome'));
		nullTextMustDie3(document.getElementById('siblingsRelationshipExplain'));
		nullTextMustDie3(document.getElementById('dadCloseExplain'));
		nullTextMustDie3(document.getElementById('momCloseExplain'));
	}
}

function process_am_child_data() {
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
}

function continue_am_history1() {
	var proceed = true;
	var form = document.getElementById('am_demo');
	process_am_child_data();

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
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
		whatSayYou.value = '';
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
		howLongLeaveScene.value = '';
		whatDoLeave.value = '';
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
		howRelax.value = '';
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
		doWhatOtherControl.value = '';
		doWhatOtherControl.disabled = true;
	}
}

function initalize_am_control(json_data) {
	var neverAttemptedControl = document.getElementById('neverAttemptedControl');
	var talkToMyself = document.getElementById('talkToMyself');
	var leaveScene = document.getElementById('leaveScene');
	var selfHelpGroup = document.getElementById('selfHelpGroup');
	var relax = document.getElementById('relax');
	var otherControlAnger = document.getElementById('otherControlAnger');

	initializeAllCheckBoxes(json_data.neverAttemptedControl, neverAttemptedControl);
	initializeAllCheckBoxes(json_data.talkToMyself, talkToMyself);
	initializeAllCheckBoxes(json_data.leaveScene, leaveScene);
	initializeAllCheckBoxes(json_data.selfHelpGroup, selfHelpGroup);
	initializeAllCheckBoxes(json_data.relax, relax);
	initializeAllCheckBoxes(json_data.otherControlAnger, otherControlAnger);

	talkMyself();
	leaveSceneCheckbox();
	howRelaxCheckbox();
	otherControlCheckbox();
}

function post_dynamic_am_control() {
	//M_VALUES
	var m_neverAttemptedControl = document.getElementById('m_neverAttemptedControl');
	var m_talkToMyself = document.getElementById('m_talkToMyself');
	var m_whatSayYou = document.getElementById('m_whatSayYou');
	var m_leaveScene = document.getElementById('m_leaveScene');
	var m_howLongLeaveScene = document.getElementById('m_howLongLeaveScene');
	var m_whatDoLeave = document.getElementById('m_whatDoLeave');
	var m_relax = document.getElementById('m_relax');
	var m_howRelax = document.getElementById('m_howRelax');
	var m_selfHelpGroup = document.getElementById('m_selfHelpGroup');
	var m_otherControlAnger = document.getElementById('m_otherControlAnger');
	var m_doWhatOtherControl = document.getElementById('m_doWhatOtherControl');

	//CHECKBOXES
	var neverAttemptedControl = document.getElementById('neverAttemptedControl');
	var talkToMyself = document.getElementById('talkToMyself');
	var leaveScene = document.getElementById('leaveScene');
	var selfHelpGroup = document.getElementById('selfHelpGroup');
	var relax = document.getElementById('relax');
	var otherControlAnger = document.getElementById('otherControlAnger');

	//DYNAMIC FIELDS
	var whatSayYou = document.getElementById('whatSayYou');
	var howLongLeaveScene = document.getElementById('howLongLeaveScene');
	var whatDoLeave = document.getElementById('whatDoLeave');
	var howRelax = document.getElementById('howRelax');
	var doWhatOtherControl = document.getElementById('doWhatOtherControl');

	postCheckboxValue(neverAttemptedControl, m_neverAttemptedControl);
	postCheckboxValue(talkToMyself, m_talkToMyself);
	postCheckboxValue(leaveScene, m_leaveScene);
	postCheckboxValue(selfHelpGroup, m_selfHelpGroup);
	postCheckboxValue(relax, m_relax);
	postCheckboxValue(otherControlAnger, m_otherControlAnger);

	processDynamicTextPostValue(talkToMyself, whatSayYou, m_whatSayYou);
	processDynamicTextPostValue(leaveScene, howLongLeaveScene, m_howLongLeaveScene);
	processDynamicTextPostValue(leaveScene, whatDoLeave, m_whatDoLeave);
	processDynamicTextPostValue(relax, howRelax, m_howRelax);
	processDynamicTextPostValue(otherControlAnger, doWhatOtherControl, m_doWhatOtherControl);
}

function initalize_am_final() {
	var back = document.getElementById('back_btn');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('whoLivesWithClient'));
		nullTextMustDie(document.getElementById('anythingelse'));
		nullTextMustDie(document.getElementById('changeLearn1'));
		nullTextMustDie(document.getElementById('changeLearn2'));
		nullTextMustDie(document.getElementById('changeLearn3'));
	}

	else {
		nullTextMustDie2(document.getElementById('whoLivesWithClient'));
		nullTextMustDie2(document.getElementById('anythingelse'));
		nullTextMustDie2(document.getElementById('changeLearn1'));
		nullTextMustDie2(document.getElementById('changeLearn2'));
		nullTextMustDie2(document.getElementById('changeLearn3'));
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
	back = document.getElementById('back_btn');

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

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('recentIncidentV'));
		nullTextMustDie(document.getElementById('happenedRecentV'));
		nullTextMustDie(document.getElementById('typeWordsRecentV'));
		nullTextMustDie(document.getElementById('recentVDate'));
		nullTextMustDie(document.getElementById('recentVlocation'));
		nullTextMustDie(document.getElementById('withWhomRecentV'));
	}
	else {
		nullTextMustDie2(document.getElementById('recentIncidentV'));
		nullTextMustDie2(document.getElementById('happenedRecentV'));
		nullTextMustDie2(document.getElementById('typeWordsRecentV'));
		nullTextMustDie2(document.getElementById('recentVDate'));
		nullTextMustDie2(document.getElementById('recentVlocation'));
		nullTextMustDie2(document.getElementById('withWhomRecentV'));
	}
}

function process_am_ah1_data() {
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
	var back = document.getElementById('back_btn');

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

function post_am_dynamic2() {
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
}


//AM ANGER HISTORY SECTION III FUNCTIONS
function homicidalRadio() {
	var isHomicidal = document.getElementById('isHomicidal');
	var homicidalExplain_label = document.getElementById('homicidalExplain_label');
	var homicidalExplain = document.getElementById('homicidalExplain');

	twoElementRadioSetup(isHomicidal, homicidalExplain_label, homicidalExplain);
}

function ah3number2() {
	var hasMedRecent = document.getElementById('hasMedRecent');

	//LABELS
	var medRecentVExplain_label = document.getElementById('medRecentVExplain_label');
	var medSuccessRecentV_label = document.getElementById('medSuccessRecentV_label');
	var treatmentSuccess_label = document.getElementById('treatmentSuccess_label');
	var noTreatmentSuccess_label = document.getElementById('noTreatmentSuccess_label');
	var medSuccessExplainRecentV_label = document.getElementById('medSuccessExplainRecentV_label');

	//FIELDS
	var medRecentVExplain = document.getElementById('medRecentVExplain');
	var medSuccessExplainRecentV = document.getElementById('medSuccessExplainRecentV');
	var treatmentSuccess = document.getElementById('treatmentSuccess');
	var noTreatmentSuccess = document.getElementById('noTreatmentSuccess');

	if (hasMedRecent.checked === true) {
		medRecentVExplain.disabled = false;
		medSuccessExplainRecentV.disabled = false;
		treatmentSuccess.disabled = false;
		noTreatmentSuccess.disabled = false;

		opacityHigh(medRecentVExplain);
		opacityHigh(medSuccessExplainRecentV);

		opacityHigh(medRecentVExplain_label);
		opacityHigh(medSuccessRecentV_label);
		opacityHigh(treatmentSuccess_label);
		opacityHigh(noTreatmentSuccess_label);
		opacityHigh(medSuccessExplainRecentV_label);
	}

	else {
		medRecentVExplain.value = '';
		medSuccessExplainRecentV.value = '';

		opacityLow(medRecentVExplain_label);
		opacityLow(medSuccessRecentV_label);
		opacityLow(treatmentSuccess_label);
		opacityLow(noTreatmentSuccess_label);
		opacityLow(medSuccessExplainRecentV_label);

		opacityLow(medRecentVExplain);
		opacityLow(medSuccessExplainRecentV);

		treatmentSuccess.disabled = true;
		noTreatmentSuccess.disabled = true;
		medRecentVExplain.disabled = true;
		medSuccessExplainRecentV.disabled = true;
	}
}

function initialize_am_angerHistory3(json_data) {
	var back = document.getElementById('back_btn');

	//RADIO BUTTONS
	var isHomicidal = document.getElementById('isHomicidal');
	var notHomicidal = document.getElementById('notHomicidal');
	var hasMedRecent = document.getElementById('hasMedRecent');
	var noMedRecent = document.getElementById('noMedRecent');
	var treatmentSuccess = document.getElementById('treatmentSuccess');
	var noTreatmentSuccess = document.getElementById('noTreatmentSuccess');

	var intensityRecentV = document.getElementById('intensityRecentV');

	setRadioElement(json_data.homicidal, isHomicidal, notHomicidal);
	setRadioElement(json_data.medRecentV, hasMedRecent, noMedRecent);
	setRadioElement(json_data.medSuccessRecentV, treatmentSuccess, noTreatmentSuccess);

	if (String(json_data.intensityRecentV) === '1') {
		document.getElementById('one').checked = true;
	}
	if (String(json_data.intensityRecentV) === '2') {
		document.getElementById('two').checked = true;
	}
	if (String(json_data.intensityRecentV) === '3') {
		document.getElementById('three').checked = true;
	}
	if (String(json_data.intensityRecentV) === '4') {
		document.getElementById('four').checked = true;
	}
	if (String(json_data.intensityRecentV) === '5') {
		document.getElementById('five').checked = true;
	}
	if (String(json_data.intensityRecentV) === '6') {
		document.getElementById('six').checked = true;
	}
	if (String(json_data.intensityRecentV) === '7') {
		document.getElementById('seven').checked = true;
	}
	if (String(json_data.intensityRecentV) === '8') {
		document.getElementById('eight').checked = true;
	}
	if (String(json_data.intensityRecentV) === '9') {
		document.getElementById('nine').checked = true;
	}
	if (String(json_data.intensityRecentV) === '10') {
		document.getElementById('ten').checked = true;
	}



	if (String(json_data.howOften) === 'This time only') {
		document.getElementById('thisTimeOnly').checked = true;
	}
	if (String(json_data.howOften) === 'Since childhood') {
		document.getElementById('sinceChildhood').checked = true;
	}
	if (String(json_data.howOften) === 'This month only') {
		document.getElementById('ThisMonthOnly').checked = true;
	}
	if (String(json_data.howOften) === 'Adolescent') {
		document.getElementById('adolescent').checked = true;
	}
	if (String(json_data.howOften) === 'Last six months') {
		document.getElementById('lastSixMonth').checked = true;
	}
	if (String(json_data.howOften) === 'Only as an adult') {
		document.getElementById('onlyAdult').checked = true;
	}

	homicidalRadio();
	ah3number2();

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('durationRecentV'));
	}
	else {
		nullTextMustDie2(document.getElementById('durationRecentV'));
	}
}

function post_dynamic_am_ah3() {
	//M_VALUE ELEMENTS
	var m_homicidal = document.getElementById('m_homicidal');
	var m_homicidalExplain = document.getElementById('m_homicidalExplain');
	var m_medRecentV = document.getElementById('m_medRecentV');
	var m_medRecentVExplain = document.getElementById('m_medRecentVExplain');
	var m_medSuccessRecentV = document.getElementById('m_medSuccessRecentV');
	var m_medSuccessExplainRecentV = document.getElementById('m_medSuccessExplainRecentV');

	//TRIGGERS
	var isHomicidal = document.getElementById('isHomicidal');
	var hasMedRecent = document.getElementById('hasMedRecent');

	//DYNAMIC TEXT FIELDS
	var homicidalExplain = document.getElementById('homicidalExplain');
	var medRecentVExplain = document.getElementById('medRecentVExplain');
	var medSuccessExplainRecentV = document.getElementById('medSuccessExplainRecentV');

	//PROCESS RADIO BUTTONS AND ASSOCIATED TEXT FIELDS
	postDynamicRadioButtons(isHomicidal, m_homicidal);
	postDynamicRadioButtons(hasMedRecent, m_medRecentV);

	processDynamicTextPostValue(isHomicidal, homicidalExplain, m_homicidalExplain);
	processDynamicTextPostValue(hasMedRecent, medRecentVExplain, m_medRecentVExplain);
	processDynamicTextPostValue(hasMedRecent, medSuccessExplainRecentV, m_medSuccessExplainRecentV);

	if (hasMedRecent.checked === true) {
		postDynamicRadioButtons(document.getElementById('treatmentSuccess'), m_medSuccessRecentV);
	}
	else {
		m_medSuccessRecentV.value = 'False';
	}
}


//DELETE THE ANGER MANAGEMENT FORM
function AmDeleted() {
	document.getElementById('exit_return_form').submit();
}

function continue_AM_session() {
	form = document.getElementById('exit_return_form');
	form.action = '/clientOptions/';
	form.submit();
}


//SAP FUNCTIONS

function continue_to_sap_form(next_page) {
	var proceed = true;
	var form = document.getElementById('sap_instructions');

	if (proceed === true) {
		if (String(next_page) === 'options') {
			form.action = '/clientOptions/';
		}

		else {
			form.action = '/sap_demographic/';
		}

		form.submit();
	}
}

function initialize_sap_clinic() {
	var back = document.getElementById('back');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('problem'));
		nullTextMustDie(document.getElementById('health'));
	}

	else {
		nullTextMustDie2(document.getElementById('problem'));
		nullTextMustDie2(document.getElementById('health'));
	}
}

function initialize_sap_social() {
	var back = document.getElementById('back');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('family'));
	}

	else {
		nullTextMustDie2(document.getElementById('family'));
	}
}

function initialize_sap_psycho1() {
	var back = document.getElementById('back');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('alcoholFrequency'));
		nullTextMustDie(document.getElementById('alcoholQuantity'));
		nullTextMustDie(document.getElementById('alcoholLast'));
		nullTextMustDie(document.getElementById('alcoholHow'));

		nullTextMustDie(document.getElementById('amphFrequency'));
		nullTextMustDie(document.getElementById('amphQuantity'));
		nullTextMustDie(document.getElementById('amphLast'));
		nullTextMustDie(document.getElementById('amphHow'));

		nullTextMustDie(document.getElementById('caffineFrequency'));
		nullTextMustDie(document.getElementById('caffineQuantity'));
		nullTextMustDie(document.getElementById('caffineLast'));
		nullTextMustDie(document.getElementById('caffineHow'));

		nullTextMustDie(document.getElementById('weedFrequency'));
		nullTextMustDie(document.getElementById('weedQuantity'));
		nullTextMustDie(document.getElementById('weedLast'));
		nullTextMustDie(document.getElementById('weedHow'));

		nullTextMustDie(document.getElementById('cokeFrequency'));
		nullTextMustDie(document.getElementById('cokeQuantity'));
		nullTextMustDie(document.getElementById('cokeLast'));
		nullTextMustDie(document.getElementById('cokeHow'));

		nullTextMustDie(document.getElementById('hallFrequency'));
		nullTextMustDie(document.getElementById('hallQuantity'));
		nullTextMustDie(document.getElementById('hallLast'));
		nullTextMustDie(document.getElementById('hallHow'));

		nullTextMustDie(document.getElementById('inhaleFrequency'));
		nullTextMustDie(document.getElementById('inhaleQuantity'));
		nullTextMustDie(document.getElementById('inhaleLast'));
		nullTextMustDie(document.getElementById('inhaleHow'));

		nullTextMustDie(document.getElementById('smokeFrequency'));
		nullTextMustDie(document.getElementById('smokeQuantity'));
		nullTextMustDie(document.getElementById('smokeLast'));
		nullTextMustDie(document.getElementById('smokeHow'));

		nullTextMustDie(document.getElementById('opFrequency'));
		nullTextMustDie(document.getElementById('opQuantity'));
		nullTextMustDie(document.getElementById('opLast'));
		nullTextMustDie(document.getElementById('opHow'));

		nullTextMustDie(document.getElementById('pcpFrequency'));
		nullTextMustDie(document.getElementById('pcpQuantity'));
		nullTextMustDie(document.getElementById('pcpLast'));
		nullTextMustDie(document.getElementById('pcpHow'));

		nullTextMustDie(document.getElementById('sedFrequency'));
		nullTextMustDie(document.getElementById('sedQuantity'));
		nullTextMustDie(document.getElementById('sedLast'));
		nullTextMustDie(document.getElementById('sedHow'));

		nullTextMustDie(document.getElementById('otherFrequency'));
		nullTextMustDie(document.getElementById('otherQuantity'));
		nullTextMustDie(document.getElementById('otherLast'));
		nullTextMustDie(document.getElementById('otherHow'));
	}

	else {
		nullTextMustDie2(document.getElementById('alcoholFrequency'));
		nullTextMustDie2(document.getElementById('alcoholQuantity'));
		nullTextMustDie2(document.getElementById('alcoholLast'));
		nullTextMustDie2(document.getElementById('alcoholHow'));

		nullTextMustDie2(document.getElementById('amphFrequency'));
		nullTextMustDie2(document.getElementById('amphQuantity'));
		nullTextMustDie2(document.getElementById('amphLast'));
		nullTextMustDie2(document.getElementById('amphHow'));

		nullTextMustDie2(document.getElementById('caffineFrequency'));
		nullTextMustDie2(document.getElementById('caffineQuantity'));
		nullTextMustDie2(document.getElementById('caffineLast'));
		nullTextMustDie2(document.getElementById('caffineHow'));

		nullTextMustDie2(document.getElementById('weedFrequency'));
		nullTextMustDie2(document.getElementById('weedQuantity'));
		nullTextMustDie2(document.getElementById('weedLast'));
		nullTextMustDie2(document.getElementById('weedHow'));

		nullTextMustDie2(document.getElementById('cokeFrequency'));
		nullTextMustDie2(document.getElementById('cokeQuantity'));
		nullTextMustDie2(document.getElementById('cokeLast'));
		nullTextMustDie2(document.getElementById('cokeHow'));

		nullTextMustDie2(document.getElementById('hallFrequency'));
		nullTextMustDie2(document.getElementById('hallQuantity'));
		nullTextMustDie2(document.getElementById('hallLast'));
		nullTextMustDie2(document.getElementById('hallHow'));

		nullTextMustDie2(document.getElementById('inhaleFrequency'));
		nullTextMustDie2(document.getElementById('inhaleQuantity'));
		nullTextMustDie2(document.getElementById('inhaleLast'));
		nullTextMustDie2(document.getElementById('inhaleHow'));

		nullTextMustDie2(document.getElementById('smokeFrequency'));
		nullTextMustDie2(document.getElementById('smokeQuantity'));
		nullTextMustDie2(document.getElementById('smokeLast'));
		nullTextMustDie2(document.getElementById('smokeHow'));

		nullTextMustDie2(document.getElementById('opFrequency'));
		nullTextMustDie2(document.getElementById('opQuantity'));
		nullTextMustDie2(document.getElementById('opLast'));
		nullTextMustDie2(document.getElementById('opHow'));

		nullTextMustDie2(document.getElementById('pcpFrequency'));
		nullTextMustDie2(document.getElementById('pcpQuantity'));
		nullTextMustDie2(document.getElementById('pcpLast'));
		nullTextMustDie2(document.getElementById('pcpHow'));

		nullTextMustDie2(document.getElementById('sedFrequency'));
		nullTextMustDie2(document.getElementById('sedQuantity'));
		nullTextMustDie2(document.getElementById('sedLast'));
		nullTextMustDie2(document.getElementById('sedHow'));

		nullTextMustDie2(document.getElementById('otherFrequency'));
		nullTextMustDie2(document.getElementById('otherQuantity'));
		nullTextMustDie2(document.getElementById('otherLast'));
		nullTextMustDie2(document.getElementById('otherHow'));
	}
}

function initialize_sap_psycho2() {
	var back = document.getElementById('back');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('psychoactive'));
	}

	else {
		nullTextMustDie2(document.getElementById('psychoactive'));
	}
}

function initialize_sap_other() {
	var back = document.getElementById('back');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('psychological'));
		nullTextMustDie(document.getElementById('gambling'));
		nullTextMustDie(document.getElementById('abilities'));
		nullTextMustDie(document.getElementById('other'));
	}

	else {
		nullTextMustDie2(document.getElementById('psychological'));
		nullTextMustDie2(document.getElementById('gambling'));
		nullTextMustDie2(document.getElementById('abilities'));
		nullTextMustDie2(document.getElementById('other'));
	}
}

function initialize_sap_sources() {
	var back = document.getElementById('back');

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('source1'));
		nullTextMustDie(document.getElementById('source2'));
		nullTextMustDie(document.getElementById('relationship1'));
		nullTextMustDie(document.getElementById('relationship2'));
	}

	else {
		nullTextMustDie2(document.getElementById('source1'));
		nullTextMustDie2(document.getElementById('source2'));
		nullTextMustDie2(document.getElementById('relationship1'));
		nullTextMustDie2(document.getElementById('relationship2'));
	}
}

function post_dynamic_sap_sources() {
	//NULL TEXT
	var source1 = document.getElementById('source1');
	var source2 = document.getElementById('source2');
	var relationship1 = document.getElementById('relationship1');
	var relationship2 = document.getElementById('relationship2');

	postTextNA(source1);
	postTextNA(source2);
	postTextNA(relationship1);
	postTextNA(relationship2);
}

function post_dynamic_sap_other() {
	//TEXT
	var psychological = document.getElementById('psychological');
	var gambling = document.getElementById('gambling');
	var abilities = document.getElementById('abilities');
	var other = document.getElementById('other');

	postTextNA(psychological);
	postTextNA(gambling);
	postTextNA(abilities);
	postTextNA(other);
}

function post_dynamic_sap_special() {
	//M_VALUE ELEMENTS
	var m_isChild = document.getElementById('m_isChild');
	var m_isSenior = document.getElementById('m_isSenior');
	var m_isDual = document.getElementById('m_isDual');
	var m_isOther = document.getElementById('m_isOther');
	var m_isNone = document.getElementById('m_isNone');
	var m_special = document.getElementById('m_special');

	//CHECKBOXES
	var isChild = document.getElementById('isChild');
	var isSenior = document.getElementById('isSenior');
	var isDual = document.getElementById('isDual');
	var isOther = document.getElementById('isOther');
	var isNone = document.getElementById('isNone');

	var special = document.getElementById('special');

	if (special.value === '' || special.value === null) {
		m_special.value = 'N/A';
	}

	postCheckboxValue(isChild, m_isChild);
	postCheckboxValue(isSenior, m_isSenior);
	postCheckboxValue(isDual, m_isDual);
	postCheckboxValue(isOther, m_isOther);
	postCheckboxValue(isNone, m_isNone);

	if (String(special.value) === '' || String(special.value) === null) {
		m_special.value = 'N/A';
	}
	else {
		m_special.value = special.value;
	}
}

function post_dynamic_sap_psycho2() {
	//TEXT PROCESSING
	var psychoactive = document.getElementById('psychoactive');
	postTextNA(psychoactive);
}

function post_dynamic_sap_psycho1() {
	postTextNA(document.getElementById('alcoholFrequency'));
	postTextNA(document.getElementById('alcoholQuantity'));
	postTextNA(document.getElementById('alcoholLast'));
	postTextNA(document.getElementById('alcoholHow'));

	postTextNA(document.getElementById('amphFrequency'));
	postTextNA(document.getElementById('amphQuantity'));
	postTextNA(document.getElementById('amphLast'));
	postTextNA(document.getElementById('amphHow'));

	postTextNA(document.getElementById('caffineFrequency'));
	postTextNA(document.getElementById('caffineQuantity'));
	postTextNA(document.getElementById('caffineLast'));
	postTextNA(document.getElementById('caffineHow'));

	postTextNA(document.getElementById('weedFrequency'));
	postTextNA(document.getElementById('weedQuantity'));
	postTextNA(document.getElementById('weedLast'));
	postTextNA(document.getElementById('weedHow'));

	postTextNA(document.getElementById('cokeFrequency'));
	postTextNA(document.getElementById('cokeQuantity'));
	postTextNA(document.getElementById('cokeLast'));
	postTextNA(document.getElementById('cokeHow'));

	postTextNA(document.getElementById('hallFrequency'));
	postTextNA(document.getElementById('hallQuantity'));
	postTextNA(document.getElementById('hallLast'));
	postTextNA(document.getElementById('hallHow'));

	postTextNA(document.getElementById('inhaleFrequency'));
	postTextNA(document.getElementById('inhaleQuantity'));
	postTextNA(document.getElementById('inhaleLast'));
	postTextNA(document.getElementById('inhaleHow'));

	postTextNA(document.getElementById('smokeFrequency'));
	postTextNA(document.getElementById('smokeQuantity'));
	postTextNA(document.getElementById('smokeLast'));
	postTextNA(document.getElementById('smokeHow'));

	postTextNA(document.getElementById('opFrequency'));
	postTextNA(document.getElementById('opQuantity'));
	postTextNA(document.getElementById('opLast'));
	postTextNA(document.getElementById('opHow'));

	postTextNA(document.getElementById('pcpFrequency'));
	postTextNA(document.getElementById('pcpQuantity'));
	postTextNA(document.getElementById('pcpLast'));
	postTextNA(document.getElementById('pcpHow'));

	postTextNA(document.getElementById('sedFrequency'));
	postTextNA(document.getElementById('sedQuantity'));
	postTextNA(document.getElementById('sedLast'));
	postTextNA(document.getElementById('sedHow'));

	postTextNA(document.getElementById('otherFrequency'));
	postTextNA(document.getElementById('otherQuantity'));
	postTextNA(document.getElementById('otherLast'));
	postTextNA(document.getElementById('otherHow'));
}

function post_dynamic_sap_social() {
	var family = document.getElementById('family');
	postTextNA(family);
}

function post_dynamic_sap_demo() {
	//TEXT FIELDS
	var problem = document.getElementById('problem');
	var health = document.getElementById('health');

	postTextNA(problem);
	postTextNA(health);
}

function post_dynamic_sap_fields(section) {
	section = String(section);

	if (section === '/sap_demographic/') {
		post_dynamic_sap_demo();
	}
	else if (section === '/sap_social/') {
		post_dynamic_sap_social();
	}
	else if (section === '/sap_psychoactive/') {
		post_dynamic_sap_psycho1();
	}
	else if (section === '/sap_psychoactive2/') {
		post_dynamic_sap_psycho2();
	}
	else if (section === '/sap_special/') {
		post_dynamic_sap_special();
	}
	else if (section === '/sap_other/') {
		post_dynamic_sap_other();
	}
	else if (section === '/sap_sources/') {
		post_dynamic_sap_sources();
	}
}

function continue_sap_form(section) {
	var proceed = true;
	var form = document.getElementById('sap_form');
	var next_url = document.getElementById('next_url');

	post_dynamic_sap_fields(section);

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = next_url.value;
		form.submit();
	}
}

function disable_sap_special() {
	//TRIGGER
	var isNone = document.getElementById('isNone');

	//LABELS
	var other_label = document.getElementById('other_label');
	var dual_label = document.getElementById('dual_label');
	var senior_label = document.getElementById('senior_label');
	var child_label = document.getElementById('child_label');
	var text_label = document.getElementById('text_label');

	//FIELDS
	var isChild = document.getElementById('isChild');
	var isSenior = document.getElementById('isSenior');
	var isDual = document.getElementById('isDual');
	var isOther = document.getElementById('isOther');
	var special = document.getElementById('special');

	if (isNone.checked === true) {
		opacityLow(other_label);
		opacityLow(dual_label);
		opacityLow(senior_label);
		opacityLow(child_label);
		opacityLow(text_label);

		opacityLow(isChild);
		opacityLow(isSenior);
		opacityLow(isDual);
		opacityLow(isOther);
		opacityLow(special);

		special.value = '';

		isChild.checked = false;
		isSenior.checked = false;
		isDual.checked = false;
		isOther.checked = false;

		isChild.disabled = true;
		isSenior.disabled = true;
		isDual.disabled = true;
		isOther.disabled = true;
		special.disabled = true;
	}

	else {
		isChild.disabled = false;
		isSenior.disabled = false;
		isDual.disabled = false;
		isOther.disabled = false;
		special.disabled = false;

		opacityHigh(other_label);
		opacityHigh(dual_label);
		opacityHigh(senior_label);
		opacityHigh(child_label);
		opacityHigh(text_label);

		opacityHigh(isChild);
		opacityHigh(isSenior);
		opacityHigh(isDual);
		opacityHigh(isOther);
		opacityHigh(special);
	}
}

function initialize_sap_special(json_data) {
	var isChild = document.getElementById('isChild');
	var isSenior = document.getElementById('isSenior');
	var isDual = document.getElementById('isDual');
	var isOther = document.getElementById('isOther');
	var isNone = document.getElementById('isNone');
	var back = document.getElementById('back');

	initializeAllCheckBoxes(json_data.isChild, isChild);
	initializeAllCheckBoxes(json_data.isSenior, isSenior);
	initializeAllCheckBoxes(json_data.isDual, isDual);
	initializeAllCheckBoxes(json_data.isOther, isOther);
	initializeAllCheckBoxes(json_data.isNone, isNone);

	if (String(back.value) === 'false') {
		nullTextMustDie(document.getElementById('special'));
	}
	else {
		nullTextMustDie2(document.getElementById('special'));
	}

	disable_sap_special();
}

//#####################################################################################################################//
//*********************************************************************************************************************//
//-------------------------------------------------- MH FUNCTIONS -----------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//

function mhSpouse() {
	//TRIGGERS
	var divorced = document.getElementById('divorced');
	var married = document.getElementById('married');
	var widowed = document.getElementById('widowed');
	var seperated = document.getElementById('seperated');

	//LABELS
	var spouseAge_label = document.getElementById('spouseAge_label');
	var spouseOccupation_label = document.getElementById('spouseOccupation_label');
	var spouseEmployer_label = document.getElementById('spouseEmployer_label');
	var spouseWorkMos_label = document.getElementById('spouseWorkMos_label');
	var numMarriages_label = document.getElementById('numMarriages_label')
	var syears_label = document.getElementById('syears_label');
	var smonths = document.getElementById('smonths');
	var syears = document.getElementById('syears');

	//FIELDS
	var spouseAge = document.getElementById('spouseAge');
	var spouseOccupation = document.getElementById('spouseOccupation');
	var spouseEmployer = document.getElementById('spouseEmployer');
	var spouseWorkMos = document.getElementById('spouseWorkMos');
	var spouseWorkYrs = document.getElementById('spouseWorkYrs');
	var numMarriages = document.getElementById('numMarriages');

	if (divorced.checked == true || married.checked == true || widowed.checked == true || seperated.checked == true) {
		spouseAge.disabled = false;
		spouseOccupation.disabled = false;
		spouseEmployer.disabled = false;
		spouseWorkMos.disabled = false;
		spouseWorkYrs.disabled = false;
		numMarriages.disabled = false;

		opacityHigh(spouseAge_label);
		opacityHigh(spouseOccupation_label);
		opacityHigh(spouseEmployer_label);
		opacityHigh(spouseWorkMos_label);
		opacityHigh(syears_label);
		opacityHigh(smonths);
		opacityHigh(syears);
		opacityHigh(numMarriages_label);

		opacityHigh(spouseAge);
		opacityHigh(spouseOccupation);
		opacityHigh(spouseEmployer);
		opacityHigh(spouseWorkMos);
		opacityHigh(spouseWorkYrs);
		opacityHigh(numMarriages);
	}

	else {
		opacityLow(spouseAge_label);
		opacityLow(spouseOccupation_label);
		opacityLow(spouseEmployer_label);
		opacityLow(spouseWorkMos_label);
		opacityLow(syears_label);
		opacityLow(smonths);
		opacityLow(syears);
		opacityLow(numMarriages_label);

		opacityLow(spouseAge);
		opacityLow(spouseOccupation);
		opacityLow(spouseEmployer);
		opacityLow(spouseWorkMos);
		opacityLow(spouseWorkYrs);
		opacityLow(numMarriages);

		spouseAge.value = '0';
		spouseOccupation.value = '';
		spouseEmployer.value = '';
		spouseWorkMos.value = '0';
		spouseWorkYrs.value = '0';
		numMarriages.value = '0';

		spouseAge.disabled = true;
		spouseOccupation.disabled = true;
		spouseEmployer.disabled = true;
		spouseWorkMos.disabled = true;
		spouseWorkYrs.disabled = true;
		numMarriages.disabled = true;
	}
}

function mhChildren() {
	var yesChild = document.getElementById('yesChild');
	var numChildren_label = document.getElementById('numChildren_label');
	var numChildren = document.getElementById('numChildren');

	twoElementRadioSetupNumber(yesChild, numChildren_label, numChildren);
}

function mhSister() {
	var yesSister = document.getElementById('yesSister');
	var numSisters_label = document.getElementById('numSisters_label');
	var numSisters = document.getElementById('numSisters');

	twoElementRadioSetupNumber(yesSister, numSisters_label, numSisters);
}

function mhBrother() {
	var yesBrother = document.getElementById('yesBrother');
	var numBrothers_label = document.getElementById('numBrothers_label');
	var numBrothers = document.getElementById('numBrothers');

	twoElementRadioSetupNumber(yesBrother, numBrothers_label, numBrothers);
}

function motherShift() {
	//TRIGGER
	var momIsLiving = document.getElementById('momIsLiving');

	//LABELS
	var motherAge_label = document.getElementById('motherAge_label');
	var motherAgeDeath_label = document.getElementById('motherAgeDeath_label'); 

	//FIELDS
	var motherAge = document.getElementById('motherAge');
	var motherAgeDeath = document.getElementById('motherAgeDeath');

	if (momIsLiving.checked === true) {
		motherAge.disabled = false;
		opacityHigh(motherAge);
		opacityHigh(motherAge_label);

		motherAgeDeath.value = '0';
		opacityLow(motherAgeDeath);
		opacityLow(motherAgeDeath_label);
		motherAgeDeath.disabled = true;
	}

	else {
		motherAgeDeath.disabled = false;
		opacityHigh(motherAgeDeath);
		opacityHigh(motherAgeDeath_label);

		motherAge.value = '0';
		opacityLow(motherAge);
		opacityLow(motherAge_label);
		motherAge.disabled = true;
	}
}

function fatherShift() {
	//TRIGGER
	var dadIsLiving = document.getElementById('dadIsLiving');

	//LABELS
	var fatherAge_label = document.getElementById('fatherAge_label');
	var fatherAgeDeath_label = document.getElementById('fatherAgeDeath_label'); 

	//FIELDS
	var fatherAge = document.getElementById('fatherAge');
	var fatherAgeDeath = document.getElementById('fatherAgeDeath');

	if (dadIsLiving.checked === true) {
		fatherAge.disabled = false;
		opacityHigh(fatherAge);
		opacityHigh(fatherAge_label);

		fatherAgeDeath.value = '0';
		opacityLow(fatherAgeDeath);
		opacityLow(fatherAgeDeath_label);
		fatherAgeDeath.disabled = true;
	}

	else {
		fatherAgeDeath.disabled = false;
		opacityHigh(fatherAgeDeath);
		opacityHigh(fatherAgeDeath_label);

		fatherAge.value = '0';
		opacityLow(fatherAge);
		opacityLow(fatherAge_label);
		fatherAge.disabled = true;
	}
}

function initialize_mh_demo(json_data) {
	var married = document.getElementById('married');
	var single = document.getElementById('single');
	var divorced = document.getElementById('divorced');
	var widowed = document.getElementById('widowed');
	var seperated = document.getElementById('seperated');
	var maritalStatus = String(json_data.maritalStatus);

	var d_mom_state = document.getElementById('d_mom_state').value;
	var d_dad_state = document.getElementById('d_dad_state').value;
	var motherState = document.getElementById('motherState');
	var fatherState = document.getElementById('fatherState');

	motherState.selectedIndex = d_mom_state;
	fatherState.selectedIndex = d_dad_state;

	if (maritalStatus === 'Married') {
		married.checked = true;
	}
	else if (maritalStatus === 'Single') {
		single.checked = true;
	}
	else if (maritalStatus === 'Divorced') {
		divorced.checked = true;
	}
	else if (maritalStatus === 'Widowed') {
		widowed.checked = true;
	}
	else if (maritalStatus === 'Seperated') {
		seperated.checked = true;
	}


	if (String(json_data.numChildren) !== '0') {
		document.getElementById('yesChild').checked = true;
	}
	else {
		document.getElementById('numChildren').value = '0';
		document.getElementById('noChild').checked = true;
	}
	if (String(json_data.numSisters) !== '0') {
		document.getElementById('yesSister').checked = true;
	}
	else {
		document.getElementById('noSister').checked = true;
	}
	if (String(json_data.numBrothers) !== '0') {
		document.getElementById('yesBrother').checked = true;
	}
	else {
		document.getElementById('noBrother').checked = true;
	}

	setRadioElement(json_data.motherLiving, document.getElementById('momIsLiving'), document.getElementById('momNotLiving'));
	setRadioElement(json_data.fatherLiving, document.getElementById('dadIsLiving'), document.getElementById('dadNotLiving'));

	mhSpouse();
	motherShift();
	fatherShift();
	mhChildren();
	mhSister();
	mhBrother();
}

function postMhFamily(trigger, element, m_element) {
	if (trigger.checked === true) {
		m_element.value = element.value;
	}
	else {
		m_element.value = '0';
	}
}

function postMhParents(trigger, elementOn, elementOff, m_elementOn, m_elementOff) {
	if (trigger.checked === true) {
		m_elementOn.value = elementOn.value;
		m_elementOff.value = '0';
	}
	else {
		m_elementOn.value = '0';
		m_elementOff.value = elementOff.value;
	}
}

function postMhNoMarriages(trigger, element, m_element) {
	if (trigger.checked === true) {
		m_element.value = '0';
	}
	else {
		m_element.value = element.value;
	}
}

function postMhSpouse(noTrigger, num1, num2, num3, t1, t2, m_num1, m_num2, m_num3, m_text1, m_text2) {
	if (noTrigger.checked === true) {
		m_num1.value = '0';
		m_num2.value = '0';
		m_num3.value = '0';

		m_text1.value = 'N/A';
		m_text2.value = 'N/A';
	}
	else {
		m_num1.value = num1.value;
		m_num2.value = num2.value;
		m_num3.value = num3.value;

		m_text1.value = t1.value;
		m_text2.value = t2.value;
	}
}

function postMhEducationFriendNumber(f1, f2, f3, f4, moreTrigger, moreElement, m_data) {
	if (f1.checked === true) {
		m_data.value = '1';
	}
	else if (f2.checked == true) {
		m_data.value = '2';
	}
	else if (f3.checked == true) {
		m_data.value = '3';
	}
	else if (f4.checked == true) {
		m_data.value = '4';
	}
	else if (moreTrigger.checked == true) {
		m_data.value = moreElement.value;
	}
}

function verify_mh_op() {
	document.getElementById('mhOpForm').submit();
}

function proceed_opWin() {
	var form = window.opener.document.getElementById('mh_form');
	// form.submit();
	window.close();
}

function edit_mhOpResults() {
	document.getElementById('back_edit').submit();
}

function continue_to_mh_form() {
	var form = document.getElementById('mh_instructions');
	form.action = '/mh_demographic/';
	form.submit();
}

function moreFriends(trigger_id, label_id, field_id) {
	var trigger = document.getElementById(trigger_id);
	var label = document.getElementById(label_id);
	var field = document.getElementById(field_id);

	twoElementRadioSetupNumber(trigger, label, field)
}

function mhCollegeRadio() {
	//TRIGGER
	var yesGrad = document.getElementById('yesGrad');

	//LABELS
	var collegeMajor_label = document.getElementById('collegeMajor_label');
	var advanceDegree_label = document.getElementById('advanceDegree_label');
	var hasAdvanced_label = document.getElementById('hasAdvanced_label');
	var noAdvanced_label = document.getElementById('noAdvanced_label');

	// //ELEMENTS
	var collegeMajor = document.getElementById('collegeMajor');
	var hasAdvanced = document.getElementById('hasAdvanced');
	var noAdvanced = document.getElementById('noAdvanced');
	
	twoElementRadioSetup(yesGrad, collegeMajor_label, collegeMajor);
	threeElementRadioSetup(yesGrad, advanceDegree_label, hasAdvanced_label, noAdvanced_label, hasAdvanced, noAdvanced);
}

function mhTrade() {
	//TRIGGER
	var yesTrade = document.getElementById('yesTrade');

	//LABELS
	var tradeSchool_label = document.getElementById('tradeSchool_label');
	var tradeAreaStudy_label = document.getElementById('tradeAreaStudy_label');

	//ELEMENTS
	var tradeSchool = document.getElementById('tradeSchool');
	var tradeAreaStudy = document.getElementById('tradeAreaStudy');

	twoElementRadioSetup(yesTrade, tradeSchool_label, tradeSchool);
	twoElementRadioSetup(yesTrade, tradeAreaStudy_label, tradeAreaStudy);
}

function mhMilitary() {
	//TRIGGER
	var isMilitary = document.getElementById('isMilitary');

	//LABELS
	var militaryBranch_label = document.getElementById('militaryBranch_label');
	var militaryYears_label = document.getElementById('militaryYears_label');
	var militaryRank_label = document.getElementById('militaryRank_label');
	var honorableDischarge_label = document.getElementById('honorableDischarge_label');
	var isHonor_label = document.getElementById('isHonor_label');
	var notHonor_label = document.getElementById('notHonor_label');

	//FIELDS
	var militaryBranch = document.getElementById('militaryBranch');
	var militaryYears = document.getElementById('militaryYears');
	var militaryRank = document.getElementById('militaryRank');
	var isHonor = document.getElementById('isHonor');
	var notHonor = document.getElementById('notHonor');

	twoElementRadioSetup(isMilitary, militaryBranch_label, militaryBranch);
	twoElementRadioSetup(isMilitary, militaryRank_label, militaryRank);
	twoElementRadioSetupNumber(isMilitary, militaryYears_label, militaryYears);
	threeElementRadioSetup(isMilitary, honorableDischarge_label, isHonor_label, notHonor_label, isHonor, notHonor);
}

function grabGradeRadio(grade, r1, r2, r3, r4, r5, r6) {
	grade = String(grade);

	if (grade === 'A') {
		r1.checked = true;
	}
	else if (grade === 'B') {
		r2.checked = true;
	}
	else if (grade === 'C') {
		r3.checked = true;
	}
	else if (grade === 'D') {
		r4.checked = true;
	}
	else if (grade === 'E') {
		r5.checked = true;
	}
	else {
		r6.checked = true;
	}
}

function grabFriendRadio(num, r1, r2, r3, r4, r5) {
	num = String(num);

	if (num === '1') {
		r1.checked = true;
	}
	else if (num === '2') {
		r2.checked = true;
	}
	else if (num === '3') {
		r3.checked = true;
	}
	else if (num === '4') {
		r4.checked = true;
	}
	else {
		r5.checked = true;
	}

	if (num === '0') {
		r1.checked = true;
	}
}

function grabMhRelationshipRadios(rating, r1, r2, r3) {
	rating = String(rating);

	if (rating === 'Poor') {
		r1.checked = true;
	}
	else if (rating === 'Average') {
		r2.checked = true;
	}
	if (rating === 'Good') {
		r3.checked = true;
	}
}

function initialize_mh_education(json_data) {
	//AVERAGE GRADES
	var a = document.getElementById('k6a');
	var b = document.getElementById('k6b');
	var c = document.getElementById('k6c');
	var d = document.getElementById('k6d');
	var e = document.getElementById('k6e');
	var f = document.getElementById('k6f');
	var g7a = document.getElementById('g7_9a');
	var g7b = document.getElementById('g7_9b');
	var g7c = document.getElementById('g7_9c');
	var g7d = document.getElementById('g7_9d');
	var g7e = document.getElementById('g7_9e');
	var g7f = document.getElementById('g7_9f');
	var g10a = document.getElementById('g10_12a');
	var g10b = document.getElementById('g10_12b');
	var g10c = document.getElementById('g10_12c');
	var g10d = document.getElementById('g10_12d');
	var g10e = document.getElementById('g10_12e');
	var g10f = document.getElementById('g10_12f');

	//RADIO ELEMENTS
	var behaved 		= document.getElementById('behaved');
	var notBehaved 		= document.getElementById('notBehaved');
	var yesAcademic 	= document.getElementById('yesAcademic');
	var noAcademic 		= document.getElementById('noAcademic');
	var behaved2 		= document.getElementById('behaved2');
	var notBehaved2 	= document.getElementById('notBehaved2');
	var yesAcademic2 	= document.getElementById('yesAcademic2');
	var noAcademic2 	= document.getElementById('noAcademic2');
	var behaved3 		= document.getElementById('behaved3');
	var notBehaved3 	= document.getElementById('notBehaved3');
	var yesAcademic3 	= document.getElementById('yesAcademic3');
	var noAcademic3 	= document.getElementById('noAcademic3');

	var yesGrad 		= document.getElementById('yesGrad');
	var noGrad 			= document.getElementById('noGrad');
	var hasAdvanced 	= document.getElementById('hasAdvanced');
	var noAdvanced 		= document.getElementById('noAdvanced');
	var yesTrade 		= document.getElementById('yesTrade');
	var noTrade 		= document.getElementById('noTrade');
	var isMilitary 		= document.getElementById('isMilitary');
	var notMilitary 	= document.getElementById('notMilitary');
	var isHonor 		= document.getElementById('isHonor');
	var notHonor 		= document.getElementById('notHonor');

	//FRIENDSHIP RADIOS
	var kf1 = document.getElementById('friend1');
	var kf2 = document.getElementById('friend2');
	var kf3 = document.getElementById('friend3');
	var kf4 = document.getElementById('friend4');
	var kfm = document.getElementById('friendMore');
	var g7f1 = document.getElementById('friend1g7');
	var g7f2 = document.getElementById('friend2g7');
	var g7f3 = document.getElementById('friend3g7');
	var g7f4 = document.getElementById('friend4g7');
	var g7fm = document.getElementById('friendMoreg7');
	var g10f1 = document.getElementById('friend1g10');
	var g10f2 = document.getElementById('friend2g10');
	var g10f3 = document.getElementById('friend3g10');
	var g10f4 = document.getElementById('friend4g10');
	var g10fm = document.getElementById('friendMoreg10');

	//SET THE GRADE RADIO FIELDS
	grabGradeRadio(json_data.GradesKto6, a, b, c, d, e, f);
	grabGradeRadio(json_data.Grades7to9, g7a, g7b, g7c, g7d, g7e, g7f);
	grabGradeRadio(json_data.Grades10to12, g10a, g10b, g10c, g10d, g10e, g10f);

	//INITIALIZE THE RADIO BUTTONS
	setRadioElement(json_data.BehaviorProblemsKto6, behaved, notBehaved);
	setRadioElement(json_data.AcademicProblemsKto6, yesAcademic, noAcademic);
	setRadioElement(json_data.BehaviorProblems7to9, behaved2, notBehaved2);
	setRadioElement(json_data.AcademicProblems7to9, yesAcademic2, noAcademic2);
	setRadioElement(json_data.BehaviorProblems10to12, behaved3, notBehaved3);
	setRadioElement(json_data.AcademicProblems10to12, yesAcademic3, noAcademic3);
	setRadioElement(json_data.collegeDegree, yesGrad, noGrad);
	setRadioElement(json_data.advanceDegree, hasAdvanced, noAdvanced);
	setRadioElement(json_data.tradeSch, yesTrade, noTrade);
	setRadioElement(json_data.military, isMilitary, notMilitary);
	setRadioElement(json_data.honorableDischarge, isHonor, notHonor);

	//SET THE NUMBER OF FRIENDSHIP RADIOS AND NUMBER FIELDS
	grabFriendRadio(json_data.FriendshipsKto6, kf1, kf2, kf3, kf4, kfm);
	grabFriendRadio(json_data.Friendships7to9, g7f1, g7f2, g7f3, g7f4, g7fm);
	grabFriendRadio(json_data.Friendships10to12, g10f1, g10f2, g10f3, g10f4, g10fm);

	//SET THE NUMBER OF COLLEGE YEARS RADIO RUTTONS
	if (String(json_data.collegeYears) === '1') {
		document.getElementById('college1').checked = true;
	}
	else if (String(json_data.collegeYears) === '2') {
		document.getElementById('college2').checked = true;
	}
	else if (String(json_data.collegeYears) === '3') {
		document.getElementById('college3').checked = true;
	}
	else {
		document.getElementById('college4').checked = true;
	}

	//SET DYNAMIC FIELD RADIO BUTTONS
	moreFriends('friendMore', 'numMore_label', 'numMore');
	moreFriends('friendMoreg7', 'numMore_labelg7', 'numMoreg7');
	moreFriends('friendMoreg10', 'numMore_labelg10', 'numMoreg10');
	mhCollegeRadio();
	mhTrade();
	mhMilitary();
}

function initialize_mh_background(json_data) {
	//RELATIONSHIP RADIOS
	var isPoorSpouse = document.getElementById('isPoorSpouse');
	var isAvgSpouse = document.getElementById('isAvgSpouse');
	var isGoodSpouse = document.getElementById('isGoodSpouse');
	var isPoorParents = document.getElementById('isPoorParents');
	var isAvgParents = document.getElementById('isAvgParents');
	var isGoodParents = document.getElementById('isGoodParents');
	var isPoorBro = document.getElementById('isPoorBro');
	var isAvgBro = document.getElementById('isAvgBro');
	var isGoodBro = document.getElementById('isGoodBro');
	var isPoorSis = document.getElementById('isPoorSis');
	var isAvgSis = document.getElementById('isAvgSis');
	var isGoodSis = document.getElementById('isGoodSis');
	var isPoorKids = document.getElementById('isPoorKids');
	var isAvgKids = document.getElementById('isAvgKids');
	var isGoodKids = document.getElementById('isGoodKids');
	var isPoorEx = document.getElementById('isPoorEx');
	var isAvgEx = document.getElementById('isAvgEx');
	var isGoodEx = document.getElementById('isGoodEx');

	document.getElementById('residence').selectedIndex = json_data.residence;
	document.getElementById('income').selectedIndex = json_data.income;
	document.getElementById('debt').selectedIndex = json_data.debt;
	document.getElementById('credit').selectedIndex = json_data.credit;
	document.getElementById('healthCare').selectedIndex = json_data.healthCare;
	document.getElementById('otherIncome').selectedIndex = json_data.otherIncome;
	document.getElementById('closeFriendVisit').selectedIndex = json_data.closeFriendVisit;
	document.getElementById('acqVisit').selectedIndex = json_data.acqVisit;

	grabMhRelationshipRadios(json_data.spouseRelationship, isPoorSpouse, isAvgSpouse, isGoodSpouse);
	grabMhRelationshipRadios(json_data.brothersRelationship, isPoorBro, isAvgBro, isGoodBro);
	grabMhRelationshipRadios(json_data.childrenRelationship, isPoorKids, isAvgKids, isGoodKids);
	grabMhRelationshipRadios(json_data.parentsRelationship, isPoorParents, isAvgParents, isGoodParents);
	grabMhRelationshipRadios(json_data.sistersRelationship, isPoorSis, isAvgSis, isGoodSis);
	grabMhRelationshipRadios(json_data.exRelationship, isPoorEx, isAvgEx, isGoodEx);
}

function initialize_mh_stress(json_data) {
	//RADIO ELEMENTS
	var yesDeath = document.getElementById('yesDeath');
	var noDeath = document.getElementById('noDeath');
	var yesDivorce = document.getElementById('yesDivorce');
	var noDivorce = document.getElementById('noDivorce');
	var yesMove = document.getElementById('yesMove');
	var noMove = document.getElementById('noMove');
	var yesMedical = document.getElementById('yesMedical');
	var noMedical = document.getElementById('noMedical');
	var yesFamily = document.getElementById('yesFamily');
	var noFamily = document.getElementById('noFamily');
	var yesMoney = document.getElementById('yesMoney');
	var noMoney = document.getElementById('noMoney');
	var yesAbuse = document.getElementById('yesAbuse');
	var noAbuse = document.getElementById('noAbuse');
	var yesAddiction = document.getElementById('yesAddiction');
	var noAddiction = document.getElementById('noAddiction');
	var yesViolence = document.getElementById('yesViolence');
	var noViolence = document.getElementById('noViolence');
	var yesOther = document.getElementById('yesOther');
	var noOther = document.getElementById('noOther');

	setRadioElement(json_data.deathStress, yesDeath, noDeath);
	setRadioElement(json_data.divorceStress, yesDivorce, noDivorce);
	setRadioElement(json_data.moveStress, yesMove, noMove);
	setRadioElement(json_data.medicalStress, yesMedical, noMedical);
	setRadioElement(json_data.familyHealthStress, yesFamily, noFamily);
	setRadioElement(json_data.financialStress, yesMoney, noMoney);
	setRadioElement(json_data.abuseStress, yesAbuse, noAbuse);
	setRadioElement(json_data.addictionFamilyStress, yesAddiction, noAddiction);
	setRadioElement(json_data.violenceFamilyStress, yesViolence, noViolence);
	setRadioElement(json_data.otherStress, yesOther, noOther);

	mhStressRadio('yesDeath', 'deathStressExp_lab', 'deathStressExp');
	mhStressRadio('yesDivorce', 'divorceStressExp_lab', 'divorceStressExp');
	mhStressRadio('yesMove', 'moveStressExp_lab', 'moveStressExp');
	mhStressRadio('yesMedical', 'medicalStressExp_lab', 'medicalStressExp');
	mhStressRadio('yesFamily', 'familyHealthStressExp_lab', 'familyHealthStressExp');
	mhStressRadio('yesMoney', 'financialStressExp_lab', 'financialStressExp');
	mhStressRadio('yesAbuse', 'abuseStressExp_lab', 'abuseStressExp');
	mhStressRadio('yesAddiction', 'addictionFamilyStressExp_lab', 'addictionFamilyStressExp');
	mhStressRadio('yesViolence', 'violenceFamilyStressExp_lab', 'violenceFamilyStressExp');
	mhStressRadio('yesOther', 'otherStressExp_lab', 'otherStressExp');
}

function initialize_mh_family(json_data) {
	//CONFIGURE THE RADIO BUTTONS
	var yesDepress = document.getElementById('yesDepress');
	var noDepress = document.getElementById('noDepress');
	var yesADD = document.getElementById('yesADD');
	var noADD = document.getElementById('noADD');
	var yesBed = document.getElementById('yesBed');
	var noBed = document.getElementById('noBed');
	var yesBi = document.getElementById('yesBi');
	var noBi = document.getElementById('noBi');
	var yesATT = document.getElementById('yesATT');
	var noATT = document.getElementById('noATT');
	var yesPA = document.getElementById('yesPA');
	var noPA = document.getElementById('noPA');
	var yesLaw = document.getElementById('yesLaw');
	var noLaw = document.getElementById('noLaw');
	var yesLD = document.getElementById('yesLD');
	var noLD = document.getElementById('noLD');
	var yesTic = document.getElementById('yesTic');
	var noTic = document.getElementById('noTic');
	var yesThy = document.getElementById('yesThy');
	var noThy = document.getElementById('noThy');
	var yesHeart = document.getElementById('yesHeart');
	var noHeart = document.getElementById('noHeart');
	var yesOW = document.getElementById('yesOW');
	var noOW = document.getElementById('noOW');
	var yesMood = document.getElementById('yesMood');
	var noMood = document.getElementById('noMood');
	var yesAlc = document.getElementById('yesAlc');
	var noAlc = document.getElementById('noAlc');
	var yesDrug = document.getElementById('yesDrug');
	var noDrug = document.getElementById('noDrug');
	var yesSch = document.getElementById('yesSch');
	var noSch = document.getElementById('noSch');
	var YesSe = document.getElementById('YesSe');
	var noSe = document.getElementById('noSe');
	var yesCS = document.getElementById('yesCS');
	var noCS = document.getElementById('noCS');
	var yesSex = document.getElementById('yesSex');
	var noSex = document.getElementById('noSex');
	var yesPanick = document.getElementById('yesPanick');
	var noPanick = document.getElementById('noPanick');
	var yesAnx = document.getElementById('yesAnx');
	var noAnx = document.getElementById('noAnx');
	var yesOCD = document.getElementById('yesOCD');
	var noOCD = document.getElementById('noOCD');
	var yesSugar = document.getElementById('yesSugar');
	var noSudar = document.getElementById('noSudar');

	var yesCancer = document.getElementById('yesCancer');
	var noCancer = document.getElementById('noCancer');

	var yesCancer = document.getElementById('yesCancer');
	var noCancer = document.getElementById('noCancer');
	var yesBlood = document.getElementById('yesBlood');
	var noBlood = document.getElementById('noBlood');
	var yesAngry = document.getElementById('yesAngry');
	var noAngry = document.getElementById('noAngry');

	setRadioElement(json_data.isdepressed, yesDepress, noDepress);
	setRadioElement(json_data.isadd, yesADD, noADD);
	setRadioElement(json_data.isbedWetting, yesBed, noBed);
	setRadioElement(json_data.isbipolar, yesBi, noBi);
	setRadioElement(json_data.issuicideAttempt, yesATT, noATT);
	setRadioElement(json_data.isphysicalAbuse, yesPA, noPA);
	setRadioElement(json_data.islaw, yesLaw, noLaw);
	setRadioElement(json_data.isld, yesLD, noLD);
	setRadioElement(json_data.istic, yesTic, noTic);
	setRadioElement(json_data.isthyroid, yesThy, noThy);
	setRadioElement(json_data.isheart, yesHeart, noHeart);
	setRadioElement(json_data.isoverweight, yesOW, noOW);
	setRadioElement(json_data.ismood, yesMood, noMood);
	setRadioElement(json_data.isalcohol, yesAlc, noAlc);
	setRadioElement(json_data.isdrugs, yesDrug, noDrug);
	setRadioElement(json_data.isschizo, yesSch, noSch);	
	setRadioElement(json_data.isseizures, YesSe, noCS);
	setRadioElement(json_data.iscompletedSuicide, yesCS, noCS);
	setRadioElement(json_data.issexAbuse, yesSex, noSex);
	setRadioElement(json_data.ispanic, yesPanick, noPanick);
	setRadioElement(json_data.isanxiety, yesAnx, noAnx);
	setRadioElement(json_data.isOCD, yesSugar, noSudar);
	setRadioElement(json_data.iscancer, yesCancer, noCancer);
	setRadioElement(json_data.ishighBloodPressure, yesBlood, noBlood);
	setRadioElement(json_data.isanger, yesAngry, noAngry);

	//FAMILY SIDE SELECT OPTIONS
	document.getElementById('depressSide').selectedIndex 	= json_data.depressedS
	document.getElementById('sideADD').selectedIndex 		= json_data.addS

	document.getElementById('sideBed').selectedIndex		= json_data.bedWettingS
	document.getElementById('sideBi').selectedIndex 		= json_data.bipolarS
	document.getElementById('sideATT').selectedIndex 		= json_data.suicideAttemptS
	document.getElementById('sidePA').selectedIndex 		= json_data.physicalAbuseS

	document.getElementById('sideLaw').selectedIndex 		= json_data.lawS
	document.getElementById('sideLD').selectedIndex 		= json_data.ldS
	document.getElementById('sideTic').selectedIndex 		= json_data.ticS
	document.getElementById('sideThy').selectedIndex 		= json_data.thyroidS
	document.getElementById('sideHeart').selectedIndex 		= json_data.heartS
	document.getElementById('sideOW').selectedIndex 		= json_data.overweightS
	document.getElementById('sideMood').selectedIndex 		= json_data.moodS
	document.getElementById('sideAlc').selectedIndex 		= json_data.alcoholS
	document.getElementById('sideDrug').selectedIndex 		= json_data.drugsS
	document.getElementById('sideSch').selectedIndex 		= json_data.schizoS
	document.getElementById('sideSe').selectedIndex 		= json_data.seizuresS
	document.getElementById('sideCS').selectedIndex 		= json_data.completedSuicideS
	document.getElementById('sideSex').selectedIndex 		= json_data.sexAbuseS
	document.getElementById('sidePanick').selectedIndex 	= json_data.panicS
	document.getElementById('sideAnx').selectedIndex 		= json_data.anxietyS
	document.getElementById('sideOCD').selectedIndex 		= json_data.OCDS
	document.getElementById('sideSugar').selectedIndex 		= json_data.diabetesS
	document.getElementById('sideCancer').selectedIndex 	= json_data.cancerS
	document.getElementById('sideBlood').selectedIndex 		= json_data.highBloodPressureS
	document.getElementById('sideAngry').selectedIndex 		= json_data.angerS

	//FAMILY MEMBER SELECT OPTIONS
	document.getElementById('depressMember').selectedIndex 	= json_data.depressedM
	document.getElementById('memADD').selectedIndex 		= json_data.addM
	document.getElementById('memBed').selectedIndex			= json_data.bedWettingM
	document.getElementById('memBi').selectedIndex 			= json_data.bipolarM
	document.getElementById('memATT').selectedIndex 		= json_data.suicideAttemptM
	document.getElementById('memPA').selectedIndex 			= json_data.physicalAbuseM
	document.getElementById('memLaw').selectedIndex 		= json_data.lawM
	document.getElementById('memLD').selectedIndex 			= json_data.ldM
	document.getElementById('memTic').selectedIndex 		= json_data.ticM
	document.getElementById('memThy').selectedIndex 		= json_data.thyroidM
	document.getElementById('memHeart').selectedIndex 		= json_data.heartM
	document.getElementById('memOW').selectedIndex 			= json_data.overweightM
	document.getElementById('memMood').selectedIndex 		= json_data.moodM
	document.getElementById('memAlc').selectedIndex 		= json_data.alcoholM
	document.getElementById('memDrug').selectedIndex 		= json_data.drugsM
	document.getElementById('memSch').selectedIndex 		= json_data.schizoM
	document.getElementById('memSe').selectedIndex 			= json_data.seizuresM
	document.getElementById('memCS').selectedIndex 			= json_data.completedSuicideM
	document.getElementById('memSex').selectedIndex 		= json_data.sexAbuseM
	document.getElementById('memPanick').selectedIndex 		= json_data.panicM
	document.getElementById('memAnx').selectedIndex 		= json_data.anxietyM
	document.getElementById('memOCD').selectedIndex 		= json_data.OCDM
	document.getElementById('memSugar').selectedIndex 		= json_data.diabetesM
	document.getElementById('memCancer').selectedIndex 		= json_data.cancerM
	document.getElementById('memBlood').selectedIndex 		= json_data.highBloodPressureM
	document.getElementById('memAngry').selectedIndex 		= json_data.angerM

	mhFamilyRadio('yesDepress', 'depSide', 'depMem', 'depressSide', 'depressMember');
	mhFamilyRadio('yesADD', 'sideADD_lab', 'memADD_lab', 'sideADD', 'memADD');
	mhFamilyRadio('yesBed', 'sideBedLab', 'memBedLab', 'sideBed', 'memBed');
	mhFamilyRadio('yesBi', 'sideBiLab', 'memBiLab', 'sideBi', 'memBi');
	mhFamilyRadio('yesATT', 'sideATTLab', 'memATTLab', 'sideATT', 'memATT');
	mhFamilyRadio('yesPA', 'sidePALab', 'memPALab', 'sidePA', 'memPA');
	mhFamilyRadio('yesLaw', 'sideLawLab', 'memLawLab', 'sideLaw', 'memLaw');
	mhFamilyRadio('yesLD', 'sideLDLab', 'memLDLab', 'sideLD', 'memLD');
	mhFamilyRadio('yesTic', 'sideTicLab', 'memTicLab', 'sideTic', 'memTic');
	mhFamilyRadio('yesThy', 'sideThyLab', 'memThyLab', 'sideThy', 'memThy');
	mhFamilyRadio('yesHeart', 'sideHeartLab', 'memHeartLab', 'sideHeart', 'memHeart');
	mhFamilyRadio('yesOW', 'sideOWLab', 'memOWLab', 'sideOW', 'memOW');
	mhFamilyRadio('yesMood', 'sideMoodLab', 'memMoodLab', 'sideMood', 'memMood');
	mhFamilyRadio('yesAlc', 'sideAlcLab', 'memAlcLab', 'sideAlc', 'memAlc');
	mhFamilyRadio('yesDrug', 'sideDrugLab', 'memDrugLab', 'sideDrug', 'memDrug');
	mhFamilyRadio('yesSch', 'sideSchLab', 'memSchLab', 'sideSch', 'memSch');
	mhFamilyRadio('YesSe', 'sideSeLab', 'memSeLab', 'sideSe', 'memSe');
	mhFamilyRadio('yesCS', 'sideCSLab', 'memCSLab', 'sideCS', 'memCS');
	mhFamilyRadio('yesSex', 'sideSexLab', 'memSexLab', 'sideSex', 'memSex');
	mhFamilyRadio('yesPanick', 'sidePanickLab', 'memPanickLab', 'sidePanick', 'memPanick');
	mhFamilyRadio('yesAnx', 'sideAnxLab', 'memAnxLab', 'sideAnx', 'memAnx');
	mhFamilyRadio('yesOCD', 'sideOCDLab', 'memOCDLab', 'sideOCD', 'memOCD');
	mhFamilyRadio('yesSugar', 'sideSugarLab', 'memSugarLab', 'sideSugar', 'memSugar');
	mhFamilyRadio('yesCancer', 'sideCancerLab', 'memCancerLab', 'sideCancer', 'memCancer');
	mhFamilyRadio('yesBlood', 'sideBloodLab', 'memBloodLab', 'sideBlood', 'memBlood');
	mhFamilyRadio('yesAngry', 'sideAngryLab', 'memAngryLab', 'sideAngry', 'memAngry');
}

function initialize_mh_legal(json_data) {
	//RADIO VARIABLES
	var yesPresent = document.getElementById('yesPresent');
	var noPresent = document.getElementById('noPresent');
	var yesPast = document.getElementById('yesPast');
	var noPast = document.getElementById('noPast');
	var isSuspended = document.getElementById('isSuspended');
	var notSuspended = document.getElementById('notSuspended');
	var yesSuit = document.getElementById('yesSuit');
	var noSuit = document.getElementById('noSuit');
	var yesStress = document.getElementById('yesStress');
	var noStress = document.getElementById('noStress');
	var yesDivPro = document.getElementById('yesDivPro');
	var noDivPro = document.getElementById('noDivPro');
	var yesChildDis = document.getElementById('yesChildDis');
	var noChildDis = document.getElementById('noChildDis');
	var yesBank = document.getElementById('yesBank');
	var noBank = document.getElementById('noBank');

	setRadioElement(json_data.probationPresent, yesPresent, noPresent);
	setRadioElement(json_data.probationPast, yesPast, noPast);
	setRadioElement(json_data.suspendedDrivePresent, isSuspended, notSuspended);
	setRadioElement(json_data.hasLawsuit, yesSuit, noSuit);
	setRadioElement(json_data.lawsuitStress, yesStress, noStress);
	setRadioElement(json_data.inDivorce, yesDivPro, noDivPro);
	setRadioElement(json_data.childCustody, yesChildDis, noChildDis);
	setRadioElement(json_data.hasBankrupcy, yesBank, noBank);

	mhProbation();
	mhLawsuits();
	mhBank();
}

function initialize_mh_use(json_data) {

}

function processDynamicMhHistory() {
	//TRIGGERS
	var yesChild = document.getElementById('yesChild');
	var yesSister = document.getElementById('yesSister');
	var yesBrother = document.getElementById('yesBrother');
	var momIsLiving = document.getElementById('momIsLiving');	
	var dadIsLiving = document.getElementById('dadIsLiving');
	var single = document.getElementById('single');

	//M DATA
	var m_motherAge = document.getElementById('m_motherAge');
	var m_motherAgeDeath = document.getElementById('m_motherAgeDeath');
	var m_fatherAge = document.getElementById('m_fatherAge');
	var m_fatherAgeDeath = document.getElementById('m_fatherAgeDeath');
	var m_numChildren = document.getElementById('m_numChildren');
	var m_numSisters = document.getElementById('m_numSisters');
	var m_numBrothers = document.getElementById('m_numBrothers');
	var m_numMarriages = document.getElementById('m_numMarriages');
	var m_spouseOccupation = document.getElementById('m_spouseOccupation');
	var m_spouseEmployer = document.getElementById('m_spouseEmployer');
	var m_spouseAge = document.getElementById('m_spouseAge');
	var m_spouseWorkMos = document.getElementById('m_spouseWorkMos');
	var m_spouseWorkYrs = document.getElementById('m_spouseWorkYrs');

	//DYNAMIC FIELDS
	var motherAge = document.getElementById('motherAge');
	var motherAgeDeath = document.getElementById('motherAgeDeath');
	var fatherAge = document.getElementById('fatherAge');
	var fatherAgeDeath = document.getElementById('fatherAgeDeath');
	var numChildren = document.getElementById('numChildren');
	var numSisters = document.getElementById('numSisters');
	var numBrothers = document.getElementById('numBrothers');
	var numMarriages = document.getElementById('numMarriages');
	var spouseOccupation = document.getElementById('spouseOccupation');
	var spouseEmployer = document.getElementById('spouseEmployer');
	var spouseAge = document.getElementById('spouseAge');
	var spouseWorkMos = document.getElementById('spouseWorkMos');
	var spouseWorkYrs = document.getElementById('spouseWorkYrs');

	postMhFamily(yesChild, numChildren, m_numChildren);
	postMhFamily(yesSister, numSisters, m_numSisters);
	postMhFamily(yesBrother, numBrothers, m_numBrothers);

	postMhParents(momIsLiving, motherAge, motherAgeDeath, m_motherAge, m_motherAgeDeath);
	postMhParents(dadIsLiving, fatherAge, fatherAgeDeath, m_fatherAge, m_fatherAgeDeath);

	postMhNoMarriages(single, numMarriages, m_numMarriages);
	postMhSpouse(single, spouseAge, spouseWorkMos, spouseWorkYrs, spouseOccupation, spouseEmployer, m_spouseAge, m_spouseWorkMos, m_spouseWorkYrs, m_spouseOccupation, m_spouseEmployer);
}

function mh_continue_demographic() {
	var proceed = true;
	var yesChild = document.getElementById('yesChild');
	var yesSister = document.getElementById('yesSister');
	var yesBrother = document.getElementById('yesBrother');
	var form = document.getElementById('mh_form');

	processDynamicMhHistory();	

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();

		if (yesChild.checked === true || yesSister.checked === true || yesBrother.checked === true) {
			var w = 750, h = 600;
			var lefts = Number((screen.width/2) - (w/2));
			var tops = Number((screen.height/2) - (h/2));
			var opWin = window.open('/mhDemoOpPage/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
		}	
	}
}

function postUniversalRadioText(trigger, textField, m_post) {
	if (trigger.checked === true) {
		m_post.value = textField.value;
	}
	else {
		m_post.value = 'N/A';
	}
}

function postUniversalRadioText_asi(trigger, textField, m_post) {
	if (trigger.checked === true) {
		m_post.value = textField.value;
	}
	else {
		m_post.value = 'N';
	}
}

function postUniversalRadioNumber(trigger, numberField, m_post) {
	if (trigger.checked === true) {
		m_post.value = numberField.value;
	}
	else {
		m_post.value = '0';
	}
}

function postUniversalRadioRadio(trigger, yesRadio, m_post) {
	if (trigger.checked === true) {
		postDynamicRadioButtons(yesRadio, m_post);
	}
	else {
		m_post.value = 'False';
	}
}


function processDynamicMhEducation() {
	//DYNAMIC RADIO FRIEND NUMBER TRIGGERS
	var fk1 = document.getElementById('friend1');
	var fk2 = document.getElementById('friend2');
	var fk3 = document.getElementById('friend3');
	var fk4 = document.getElementById('friend4');
	var fkm = document.getElementById('friendMore');
	var numMore = document.getElementById('numMore');
	var m_FriendshipsKto6 = document.getElementById('m_FriendshipsKto6');
	var f7g1 = document.getElementById('friend1g7');
	var f7g2 = document.getElementById('friend2g7');
	var f7g3 = document.getElementById('friend3g7');
	var f7g4 = document.getElementById('friend4g7');
	var f7gm = document.getElementById('friendMoreg7');
	var numMoreg7 = document.getElementById('numMoreg7');
	var m_Friendships7to9 = document.getElementById('m_Friendships7to9');
	var f10g1 = document.getElementById('friend1g10');
	var f10g2 = document.getElementById('friend2g10');
	var f10g3 = document.getElementById('friend3g10');
	var f10g4 = document.getElementById('friend4g10');
	var f10gm = document.getElementById('friendMoreg10');
	var numMoreg10 = document.getElementById('numMoreg10');
	var Friendships10to12 = document.getElementById('m_Friendships10to12');	
	var yesGrad = document.getElementById('yesGrad');
	var collegeMajor = document.getElementById('collegeMajor');	
	var m_collegeMajor = document.getElementById('m_collegeMajor');
	var hasAdvanced = document.getElementById('hasAdvanced');
	var m_advanceDegree = document.getElementById('m_advanceDegree');

	var yesTrade = document.getElementById('yesTrade');
	var tradeSchool = document.getElementById('tradeSchool');
	var tradeAreaStudy = document.getElementById('tradeAreaStudy');
	var m_tradeSchool = document.getElementById('m_tradeSchool');
	var m_tradeAreaStudy = document.getElementById('m_tradeAreaStudy');

	var isMilitary = document.getElementById('isMilitary');
	var militaryBranch = document.getElementById('militaryBranch');
	var militaryRank = document.getElementById('militaryRank');
	var militaryYears = document.getElementById('militaryYears');
	var isHonor = document.getElementById('isHonor');
	var m_militaryBranch = document.getElementById('m_militaryBranch');
	var m_militaryRank = document.getElementById('m_militaryRank');
	var m_militaryYears = document.getElementById('m_militaryYears');
	var m_honorableDischarge = document.getElementById('m_honorableDischarge');

	postMhEducationFriendNumber(fk1, fk2, fk3, fk4, fkm, numMore, m_FriendshipsKto6);
	postMhEducationFriendNumber(f7g1, f7g2, f7g3, f7g4, f7gm, numMoreg7, m_Friendships7to9);
	postMhEducationFriendNumber(f10g1, f10g2, f10g3, f10g4, f10gm, numMoreg10, Friendships10to12);

	postUniversalRadioText(yesGrad, collegeMajor, m_collegeMajor);	
	postUniversalRadioText(yesTrade, tradeSchool, m_tradeSchool);
	postUniversalRadioText(yesTrade, tradeAreaStudy, m_tradeAreaStudy);
	postUniversalRadioText(isMilitary, militaryBranch, m_militaryBranch);
	postUniversalRadioText(isMilitary, militaryRank, m_militaryRank);

	postUniversalRadioNumber(isMilitary, militaryYears, m_militaryYears);

	postUniversalRadioRadio(yesGrad, hasAdvanced, m_advanceDegree);
	postUniversalRadioRadio(isMilitary, isHonor, m_honorableDischarge);
}

function proceed_mh_education() {
	var proceed = true;
	form = document.getElementById('mh_form');
	processDynamicMhEducation();	

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function proceed_mh_background() {
	var proceed = true;
	form = document.getElementById('mh_form');

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function processDynamicMhStress() {
	//TRIGGERS
	var yesDeath 		= document.getElementById('yesDeath');
	var yesDivorce 		= document.getElementById('yesDivorce');
	var yesMove 		= document.getElementById('yesMove');
	var yesMedical 		= document.getElementById('yesMedical');
	var yesFamily 		= document.getElementById('yesFamily');
	var yesMoney 		= document.getElementById('yesMoney');
	var yesAbuse 		= document.getElementById('yesAbuse');
	var yesAddiction 	= document.getElementById('yesAddiction');
	var yesViolence 	= document.getElementById('yesViolence');
	var yesOther 		= document.getElementById('yesOther');

	//FIELDS
	var deathStressExp 				= document.getElementById('deathStressExp');
	var divorceStressExp 			= document.getElementById('divorceStressExp');
	var moveStressExp 				= document.getElementById('moveStressExp');
	var medicalStressExp 			= document.getElementById('medicalStressExp');
	var familyHealthStressExp 		= document.getElementById('familyHealthStressExp');
	var financialStressExp 			= document.getElementById('financialStressExp');
	var abuseStressExp 				= document.getElementById('abuseStressExp');
	var addictionFamilyStressExp 	= document.getElementById('addictionFamilyStressExp');
	var violenceFamilyStressExp 	= document.getElementById('violenceFamilyStressExp');
	var otherStressExp 				= document.getElementById('otherStressExp');

	postUniversalRadioText(yesDeath, deathStressExp, m_deathStressExp);
	postUniversalRadioText(yesDivorce, divorceStressExp, m_divorceStressExp);
	postUniversalRadioText(yesMove, moveStressExp, m_moveStressExp);
	postUniversalRadioText(yesMedical, medicalStressExp, m_medicalStressExp);
	postUniversalRadioText(yesFamily, familyHealthStressExp, m_familyHealthStressExp);
	postUniversalRadioText(yesMoney, financialStressExp, m_financialStressExp);
	postUniversalRadioText(yesAbuse, abuseStressExp, m_abuseStressExp);
	postUniversalRadioText(yesAddiction, addictionFamilyStressExp, m_addictionFamilyStressExp);
	postUniversalRadioText(yesViolence, violenceFamilyStressExp, m_violenceFamilyStressExp);
	postUniversalRadioText(yesOther, otherStressExp, m_otherStressExp);
}

function proceed_mh_stress() {
	var proceed = true;
	form = document.getElementById('mh_form');
	processDynamicMhStress();

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function combineFamilyValues(trigger, fSide, fMem, m_post) {
	if (trigger.checked === true) {
		temp = String(fSide.value) + ' ' + String(fMem.value);
		m_post.value = temp;
	}

	else {
		m_post.value = 'N/A';
	}
}

function processDynamicMhFamily() {
	combineFamilyValues(document.getElementById('yesDepress'), document.getElementById('depressSide'), document.getElementById('depressMember'), document.getElementById('depressed'));
	combineFamilyValues(document.getElementById('yesADD'), document.getElementById('sideADD'), document.getElementById('memADD'), document.getElementById('add'));
	combineFamilyValues(document.getElementById('yesBed'), document.getElementById('sideBed'), document.getElementById('memBed'), document.getElementById('bedWetting'));
	combineFamilyValues(document.getElementById('yesBi'), document.getElementById('sideBi'), document.getElementById('memBi'), document.getElementById('bipolar'));
	combineFamilyValues(document.getElementById('yesATT'), document.getElementById('sideATT'), document.getElementById('memATT'), document.getElementById('suicideAttempt'));
	combineFamilyValues(document.getElementById('yesPA'), document.getElementById('sidePA'), document.getElementById('memPA'), document.getElementById('physicalAbuse'));
	combineFamilyValues(document.getElementById('yesLaw'), document.getElementById('sideLaw'), document.getElementById('memLaw'), document.getElementById('law'));
	combineFamilyValues(document.getElementById('yesLD'), document.getElementById('sideLD'), document.getElementById('memLD'), document.getElementById('ld'));
	combineFamilyValues(document.getElementById('yesTic'), document.getElementById('sideTic'), document.getElementById('memTic'), document.getElementById('tic'));
	combineFamilyValues(document.getElementById('yesThy'), document.getElementById('sideThy'), document.getElementById('memThy'), document.getElementById('thyroid'));
	combineFamilyValues(document.getElementById('yesHeart'), document.getElementById('sideHeart'), document.getElementById('memHeart'), document.getElementById('heart'));
	combineFamilyValues(document.getElementById('yesOW'), document.getElementById('sideOW'), document.getElementById('memOW'), document.getElementById('overweight'));
	combineFamilyValues(document.getElementById('yesMood'), document.getElementById('sideMood'), document.getElementById('memMood'), document.getElementById('mood'));
	combineFamilyValues(document.getElementById('yesAlc'), document.getElementById('sideAlc'), document.getElementById('memAlc'), document.getElementById('alcohol'));

	combineFamilyValues(document.getElementById('yesDrug'), document.getElementById('sideDrug'), document.getElementById('memDrug'), document.getElementById('drugs'));
	combineFamilyValues(document.getElementById('yesSch'), document.getElementById('sideSch'), document.getElementById('memSch'), document.getElementById('schizo'));
	combineFamilyValues(document.getElementById('YesSe'), document.getElementById('sideSe'), document.getElementById('memSe'), document.getElementById('seizures'));
	combineFamilyValues(document.getElementById('yesCS'), document.getElementById('sideCS'), document.getElementById('memCS'), document.getElementById('completedSuicide'));
	combineFamilyValues(document.getElementById('yesSex'), document.getElementById('sideSex'), document.getElementById('memSex'), document.getElementById('sexAbuse'));
	combineFamilyValues(document.getElementById('yesPanick'), document.getElementById('sidePanick'), document.getElementById('memPanick'), document.getElementById('panic'));
	combineFamilyValues(document.getElementById('yesAnx'), document.getElementById('sideAnx'), document.getElementById('memAnx'), document.getElementById('anxiety'));

	combineFamilyValues(document.getElementById('yesOCD'), document.getElementById('sideOCD'), document.getElementById('memOCD'), document.getElementById('OCD'));
	combineFamilyValues(document.getElementById('yesSugar'), document.getElementById('sideSugar'), document.getElementById('memSugar'), document.getElementById('diabetes'));
	combineFamilyValues(document.getElementById('yesCancer'), document.getElementById('sideCancer'), document.getElementById('memCancer'), document.getElementById('cancer'));
	combineFamilyValues(document.getElementById('yesBlood'), document.getElementById('sideBlood'), document.getElementById('memBlood'), document.getElementById('highBloodPressure'));
	combineFamilyValues(document.getElementById('yesAngry'), document.getElementById('sideAngry'), document.getElementById('memAngry'), document.getElementById('anger'));

}

function proceed_mh_familyHistory() {
	var proceed = true;
	form = document.getElementById('mh_form');
	processDynamicMhFamily();	

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function processDynamicMhLegal() {
	//TRIGGERS
	var yesPresent = document.getElementById('yesPresent');
	var yesPast = document.getElementById('yesPast');
	var yesSuit = document.getElementById('yesSuit');
	var yesBank = document.getElementById('yesBank');

	//DYNAMIC FIELDS
	var probationOfficer = document.getElementById('probationOfficer');
	var probationOffense = document.getElementById('probationOffense');
	var yesStress = document.getElementById('yesStress'); //ALSO A TRIGGER FOR RADIO RADIO
	var dateBenkrupcy = document.getElementById('dateBenkrupcy');

	//POST FIELDS (M_DATA)
	var m_probationOfficer = document.getElementById('m_probationOfficer');
	var m_probationOffense = document.getElementById('m_probationOffense');
	var m_lawsuitStress = document.getElementById('m_lawsuitStress');
	var m_dateBenkrupcy = document.getElementById('m_dateBenkrupcy');

	if (yesPresent.checked === true || yesPast.checked === true) {
		m_probationOfficer.value = probationOfficer.value;
		m_probationOffense.value = probationOffense.value;
	}
	else if (yesPresent.checked === false && yesPast.checked == false) {
		m_probationOfficer.value = 'N/A';
		m_probationOffense.value = 'N/A';
	}

	postUniversalRadioRadio(yesSuit, yesStress, m_lawsuitStress);
	postUniversalRadioNumber(yesBank, dateBenkrupcy, m_dateBenkrupcy);
}

function proceed_mh_legalHistory() {
	var proceed = true;
	processDynamicMhLegal();
	form = document.getElementById('mh_form');

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function proceed_mh_psychHistory() {
	var proceed = true;
	form = document.getElementById('mh_form');

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function proceed_mh_useTable() {
	var proceed = true;
	form = document.getElementById('mh_form');

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = document.getElementById('next_url').value;
		form.submit();
	}
}

function mhStressRadio(trigger_id, label_id, element_id) {
	var trigger = document.getElementById(trigger_id);
	var label = document.getElementById(label_id);
	var element = document.getElementById(element_id);

	twoElementRadioSetup(trigger, label, element);
}

function mhFamilyRadio(trigger_id, label1_id, label2_id, sel1_id, sel2_id) {
	var trigger = document.getElementById(trigger_id);
	var lab1 = document.getElementById(label1_id);
	var lab2 = document.getElementById(label2_id);
	var sel1 = document.getElementById(sel1_id);
	var sel2 = document.getElementById(sel2_id);

	if (trigger.checked === true) {
		sel1.disabled = false;
		sel2.disabled = false;
		opacityHigh(lab1);
		opacityHigh(lab2);
		opacityHigh(sel1);
		opacityHigh(sel2);
	}

	else {
		opacityLow(sel1);
		opacityLow(sel2);
		opacityLow(lab1);
		opacityLow(lab2);
		sel1.selectedIndex = 0;
		sel2.selectedIndex = 0;
		sel1.disabled = true;
		sel2.disabled = true;
	}
}

function mhProbation() {
	//TRIGGERS
	var yesPresent = document.getElementById('yesPresent');
	var yesPast = document.getElementById('yesPast');

	//LABELS
	var probLab = document.getElementById('probLab');
	var probOffLab = document.getElementById('probOffLab');

	//ELEMENTS
	var probationOfficer = document.getElementById('probationOfficer');
	var probationOffense = document.getElementById('probationOffense');

	if (yesPresent.checked === true || yesPast.checked === true) {
		probationOfficer.disabled = false;
		probationOffense.disabled = false;
		opacityHigh(probLab);
		opacityHigh(probOffLab);
		opacityHigh(probationOfficer);
		opacityHigh(probationOffense);
	}

	else if (yesPresent.checked === false || yesPast.checked === false) {
		opacityLow(probLab);
		opacityLow(probOffLab);
		opacityLow(probationOfficer);
		opacityLow(probationOffense);
		probationOfficer.value = '';
		probationOffense.value = '';
		probationOfficer.disabled = true;
		probationOffense.disabled = true;
	}
}

function mhLawsuits() {
	//TRIGGER
	var yesSuit = document.getElementById('yesSuit');

	//LABELS
	var mhFamStressLab = document.getElementById('mhFamStressLab');
	var yesStressLab = document.getElementById('yesStressLab');
	var noStressLab = document.getElementById('noStressLab');

	//ELEMENTS
	var yesStress = document.getElementById('yesStress');
	var noStress = document.getElementById('noStress');

	if (yesSuit.checked === true) {
		yesStress.disabled = false;
		noStress.disabled = false;
		opacityHigh(mhFamStressLab);
		opacityHigh(yesStressLab);
		opacityHigh(noStressLab);
		opacityHigh(yesStress);
		opacityHigh(noStress);
	}

	else {
		opacityLow(mhFamStressLab);
		opacityLow(yesStressLab);
		opacityLow(noStressLab);
		opacityLow(yesStress);
		opacityLow(noStress);
		yesStress.checked = true;
		yesStress.disabled = true;
		noStress.disabled = true;
	}
}

function mhBank() {
	var yesBank = document.getElementById('yesBank');
	var bankLab = document.getElementById('bankLab');
	var dateBenkrupcy = document.getElementById('dateBenkrupcy');

	twoElementRadioSetup(yesBank, bankLab, dateBenkrupcy);
}

//=====================================================================================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//=====================================================================================================================//



//#####################################################################################################################//
//*********************************************************************************************************************//
//------------------------------------------------- ASI FUNCTIONS -----------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//


//*********************************************** ASI INITIALIZATIONS *************************************************//

function initialize_asi(section, json_data) {
	section = String(section);

	if (section === '/asi_admin/') {
		init_asi_admin(json_data);
	}
	else if (section === '/asi_general/') {
		init_asi_general(json_data);
	}
	else if (section === '/asi_medical/') {
		init_asi_medical(json_data);
	}
	else if (section === '/asi_employment/') {
		init_asi_employmentl(json_data);
	}
	else if (section === '/asi_drug1/') {
		init_asi_drug1(json_data);
	}
	else if (section === '/asi_legal/') {
		init_asi_legal(json_data);
	}
	else if (section === '/asi_family/') {
		init_asi_family(json_data);
	}
	else if (section === '/asi_social1/') {
		init_asi_soc1(json_data);
	}
	else if (section === '/asi_social2/') {
		init_asi_soc2(json_data);
	}
	else if (section === '/asi_psych/') {
		init_asi_psych(json_data);
	}
}

function init_asi_admin(json_data) {
	blank_init_asi(json_data.isComplete, document.getElementById('g1'));
	blank_init_asi(json_data.isComplete, document.getElementById('g2'));
	blank_init_asi(json_data.isComplete, document.getElementById('g3'));
	blank_init_asi(json_data.isComplete, document.getElementById('popupDatepicker'));
	blank_init_asi(json_data.isComplete, document.getElementById('g11'));

	document.getElementById('g8').selectedIndex = json_data.g8;
	document.getElementById('g9').selectedIndex = json_data.g9;
	document.getElementById('g12').selectedIndex = json_data.g12;
	asi_radioBtn_select(json_data.g10, document.getElementById('isMale'), document.getElementById('isFemale'));
}

function init_asi_general(json_data) {
	blank_init_asi(json_data.isComplete, document.getElementById('g13'));
	blank_init_asi(json_data.isComplete, document.getElementById('g21'));
	blank_init_asi(json_data.isComplete, document.getElementById('g22'));
	blank_init_asi(json_data.isComplete, document.getElementById('g23'));
	blank_init_asi(json_data.isComplete, document.getElementById('g24'));
	blank_init_asi(json_data.isComplete, document.getElementById('g25'));
	blank_init_asi(json_data.isComplete, document.getElementById('g26'));
	blank_init_asi(json_data.isComplete, document.getElementById('g27'));
	blank_init_asi(json_data.isComplete, document.getElementById('g28'));
	blank_init_asi(json_data.isComplete, document.getElementById('test1'));
	blank_init_asi(json_data.isComplete, document.getElementById('test2'));
	blank_init_asi(json_data.isComplete, document.getElementById('test3'));

	number_init(json_data.isComplete, document.getElementById('g14yrs'));
	number_init(json_data.isComplete, document.getElementById('g14mos'));
	number_init(json_data.isComplete, document.getElementById('g20'));

	//SEVERITY RADIO ENTRIES
	var m0 = document.getElementById('m0');
	var m1 = document.getElementById('m1');
	var m2 = document.getElementById('m2');
	var m3 = document.getElementById('m3');
	var m4 = document.getElementById('m4');
	var m5 = document.getElementById('m5');
	var m6 = document.getElementById('m6');
	var m7 = document.getElementById('m7');
	var m8 = document.getElementById('m8');
	var m9 = document.getElementById('m9');

	var e0 = document.getElementById('e0');
	var e1 = document.getElementById('e1');
	var e2 = document.getElementById('e2');
	var e3 = document.getElementById('e3');
	var e4 = document.getElementById('e4');
	var e5 = document.getElementById('e5');
	var e6 = document.getElementById('e6');
	var e7 = document.getElementById('e7');
	var e8 = document.getElementById('e8');
	var e9 = document.getElementById('e9');

	var a0 = document.getElementById('a0');
	var a1 = document.getElementById('a1');
	var a2 = document.getElementById('a2');
	var a3 = document.getElementById('a3');
	var a4 = document.getElementById('a4');
	var a5 = document.getElementById('a5');
	var a6 = document.getElementById('a6');
	var a7 = document.getElementById('a7');
	var a8 = document.getElementById('a8');
	var a9 = document.getElementById('a9');

	var d0 = document.getElementById('d0');
	var d1 = document.getElementById('d1');
	var d2 = document.getElementById('d2');
	var d3 = document.getElementById('d3');
	var d4 = document.getElementById('d4');
	var d5 = document.getElementById('d5');
	var d6 = document.getElementById('d6');
	var d7 = document.getElementById('d7');
	var d8 = document.getElementById('d8');
	var d9 = document.getElementById('d9');

	var l0 = document.getElementById('l0');
	var l1 = document.getElementById('l1');
	var l2 = document.getElementById('l2');
	var l3 = document.getElementById('l3');
	var l4 = document.getElementById('l4');
	var l5 = document.getElementById('l5');
	var l6 = document.getElementById('l6');
	var l7 = document.getElementById('l7');
	var l8 = document.getElementById('l8');
	var l9 = document.getElementById('l9');

	var f0 = document.getElementById('f0');
	var f1 = document.getElementById('f1');
	var f2 = document.getElementById('f2');
	var f3 = document.getElementById('f3');
	var f4 = document.getElementById('f4');
	var f5 = document.getElementById('f5');
	var f6 = document.getElementById('f6');
	var f7 = document.getElementById('f7');
	var f8 = document.getElementById('f8');
	var f9 = document.getElementById('f9');

	var p0 = document.getElementById('p0');
	var p1 = document.getElementById('p1');
	var p2 = document.getElementById('p2');
	var p3 = document.getElementById('p3');
	var p4 = document.getElementById('p4');
	var p5 = document.getElementById('p5');
	var p6 = document.getElementById('p6');
	var p7 = document.getElementById('p7');
	var p8 = document.getElementById('p8');
	var p9 = document.getElementById('p9');

	assign_radio1_9(json_data.medical, m0, m1, m2, m3, m4, m5, m6, m7, m8, m9);
	assign_radio1_9(json_data.employ, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9);
	assign_radio1_9(json_data.alcohol, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9);
	assign_radio1_9(json_data.drug, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9);
	assign_radio1_9(json_data.legal, l0, l1, l2, l3, l4, l5, l6, l7, l8, l9);
	assign_radio1_9(json_data.family, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9);
	assign_radio1_9(json_data.psych, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9);

	document.getElementById('g17').selectedIndex = json_data.g17;
	document.getElementById('g18').selectedIndex = json_data.g18;
	document.getElementById('g19').selectedIndex = json_data.g19;
}

function init_asi_medical(json_data) {
	number_init(json_data.isComplete, document.getElementById('m2yrs'));
	number_init(json_data.isComplete, document.getElementById('m2mth'));
	number_init(json_data.isComplete, document.getElementById('m1'));
	number_init(json_data.isComplete, document.getElementById('m6'));

	blank_init_asi(json_data.isComplete, document.getElementById('m5Exp'));
	blank_init_asi(json_data.isComplete, document.getElementById('comments'));

	document.getElementById('m7').selectedIndex = Number(json_data.m7);
	document.getElementById('m8').selectedIndex = Number(json_data.m8);
	document.getElementById('m9').selectedIndex = Number(json_data.m9);
	
	asi_radioBtn_select(json_data.m3, document.getElementById('m3yes'), document.getElementById('m3no'));
	asi_radioBtn_select(json_data.m4, document.getElementById('m4yes'), document.getElementById('m4no'));
	asi_radioBtn_select(json_data.m5, document.getElementById('m5yes'), document.getElementById('m5no'));
	asi_radioBtn_select(json_data.m10, document.getElementById('m10yes'), document.getElementById('m10no'));
	asi_radioBtn_select(json_data.m11, document.getElementById('m11yes'), document.getElementById('m11no'));

	m5Radio();
}

function init_asi_employmentl(json_data) {
	number_init(json_data.isComplete, document.getElementById('e1yrs'));
	number_init(json_data.isComplete, document.getElementById('e1mth'));
	number_init(json_data.isComplete, document.getElementById('e2'));
	number_init(json_data.isComplete, document.getElementById('e6yrs'));
	number_init(json_data.isComplete, document.getElementById('e6mth'));
	number_init(json_data.isComplete, document.getElementById('e11'));
	number_init(json_data.isComplete, document.getElementById('e12'));
	number_init(json_data.isComplete, document.getElementById('e13'));
	number_init(json_data.isComplete, document.getElementById('e14'));
	number_init(json_data.isComplete, document.getElementById('e15'));
	number_init(json_data.isComplete, document.getElementById('e16'));
	number_init(json_data.isComplete, document.getElementById('e17'));
	number_init(json_data.isComplete, document.getElementById('e18'));
	number_init(json_data.isComplete, document.getElementById('e19'));

	blank_init_asi(json_data.isComplete, document.getElementById('e3Exp'));
	blank_init_asi(json_data.isComplete, document.getElementById('e7Exp'));
	blank_init_asi(json_data.isComplete, document.getElementById('comments'));

	document.getElementById('e10').selectedIndex = json_data.e10;
	document.getElementById('e20').selectedIndex = json_data.e20;
	document.getElementById('e21').selectedIndex = json_data.e21;
	document.getElementById('e22').selectedIndex = json_data.e22;

	asi_radioBtn_select(json_data.e3, document.getElementById('e3yes'), document.getElementById('e3no'));
	asi_radioBtn_select(json_data.e4, document.getElementById('e4yes'), document.getElementById('e4no'));
	asi_radioBtn_select(json_data.e5, document.getElementById('e5yes'), document.getElementById('e5no'));
	asi_radioBtn_select(json_data.e7, document.getElementById('e7yes'), document.getElementById('e7no'));
	asi_radioBtn_select(json_data.e8, document.getElementById('e8yes'), document.getElementById('e8no'));
	asi_radioBtn_select(json_data.e9, document.getElementById('e9yes'), document.getElementById('e9no'));
	asi_radioBtn_select(json_data.e23, document.getElementById('e23yes'), document.getElementById('e23no'));
	asi_radioBtn_select(json_data.e24, document.getElementById('e24yes'), document.getElementById('e24no'));

	e3Radio();
	e4Radio();
	e7Radio();
	e8Radio();
}

function init_asi_drug1(json_data) {
	blank_init_asi(json_data.isComplete, document.getElementById('comments'));

	number_init(json_data.isComplete, document.getElementById('d1Day'));
	number_init(json_data.isComplete, document.getElementById('d2Day'));
	number_init(json_data.isComplete, document.getElementById('d3Day'));
	number_init(json_data.isComplete, document.getElementById('d4Day'));
	number_init(json_data.isComplete, document.getElementById('d5Day'));
	number_init(json_data.isComplete, document.getElementById('d6Day'));
	number_init(json_data.isComplete, document.getElementById('d7Day'));
	number_init(json_data.isComplete, document.getElementById('d8Day'));
	number_init(json_data.isComplete, document.getElementById('d9Day'));
	number_init(json_data.isComplete, document.getElementById('d10Day'));
	number_init(json_data.isComplete, document.getElementById('d11Day'));
	number_init(json_data.isComplete, document.getElementById('d12Day'));

	number_init(json_data.isComplete, document.getElementById('d1Year'));
	number_init(json_data.isComplete, document.getElementById('d2Year'));
	number_init(json_data.isComplete, document.getElementById('d3Year'));
	number_init(json_data.isComplete, document.getElementById('d4Year'));
	number_init(json_data.isComplete, document.getElementById('d5Year'));
	number_init(json_data.isComplete, document.getElementById('d6Year'));
	number_init(json_data.isComplete, document.getElementById('d7Year'));
	number_init(json_data.isComplete, document.getElementById('d8Year'));
	number_init(json_data.isComplete, document.getElementById('d9Year'));
	number_init(json_data.isComplete, document.getElementById('d10Year'));
	number_init(json_data.isComplete, document.getElementById('d11Year'));
	number_init(json_data.isComplete, document.getElementById('d12Year'));

	number_init(json_data.isComplete, document.getElementById('d15'));
	number_init(json_data.isComplete, document.getElementById('d16'));
	number_init(json_data.isComplete, document.getElementById('d17'));
	number_init(json_data.isComplete, document.getElementById('d18'));
	number_init(json_data.isComplete, document.getElementById('d19'));
	number_init(json_data.isComplete, document.getElementById('d20'));
	number_init(json_data.isComplete, document.getElementById('d21'));
	number_init(json_data.isComplete, document.getElementById('d22'));
	number_init(json_data.isComplete, document.getElementById('d23'));
	number_init(json_data.isComplete, document.getElementById('d24'));
	number_init(json_data.isComplete, document.getElementById('d25'));
	number_init(json_data.isComplete, document.getElementById('d26'));
	number_init(json_data.isComplete, document.getElementById('d27'));

	document.getElementById('d1Route').selectedIndex = json_data.d1Route;
	document.getElementById('d2Route').selectedIndex = json_data.d2Route;
	document.getElementById('d3Route').selectedIndex = json_data.d3Route;
	document.getElementById('d4Route').selectedIndex = json_data.d4Route;
	document.getElementById('d5Route').selectedIndex = json_data.d5Route;
	document.getElementById('d6Route').selectedIndex = json_data.d6Route;
	document.getElementById('d7Route').selectedIndex = json_data.d7Route;
	document.getElementById('d8Route').selectedIndex = json_data.d8Route;
	document.getElementById('d9Route').selectedIndex = json_data.d9Route;
	document.getElementById('d10Route').selectedIndex = json_data.d10Route;
	document.getElementById('d11Route').selectedIndex = json_data.d11Route;
	document.getElementById('d12Route').selectedIndex = json_data.d12Route;

	document.getElementById('d13').selectedIndex = json_data.d13;
	document.getElementById('d14').selectedIndex = json_data.d14;
	document.getElementById('d28').selectedIndex = json_data.d28;
	document.getElementById('d29').selectedIndex = json_data.d29;
	document.getElementById('d30').selectedIndex = json_data.d30;
	document.getElementById('d31').selectedIndex = json_data.d31;
	document.getElementById('d32').selectedIndex = json_data.d32;
	document.getElementById('d33').selectedIndex = json_data.d33;

	asi_radioBtn_select(json_data.d34, document.getElementById('d34yes'), document.getElementById('d34no'));
	asi_radioBtn_select(json_data.d35, document.getElementById('d35yes'), document.getElementById('d35no'));
}

function init_asi_legal(json_data) {
	number_init(json_data.isComplete, document.getElementById('l3'));
	number_init(json_data.isComplete, document.getElementById('l4'));
	number_init(json_data.isComplete, document.getElementById('l5'));
	number_init(json_data.isComplete, document.getElementById('l6'));
	number_init(json_data.isComplete, document.getElementById('l7'));
	number_init(json_data.isComplete, document.getElementById('l8'));
	number_init(json_data.isComplete, document.getElementById('l9'));
	number_init(json_data.isComplete, document.getElementById('l10'));
	number_init(json_data.isComplete, document.getElementById('l11'));
	number_init(json_data.isComplete, document.getElementById('l12'));
	number_init(json_data.isComplete, document.getElementById('l13'));
	number_init(json_data.isComplete, document.getElementById('l14'));
	number_init(json_data.isComplete, document.getElementById('l15'));
	number_init(json_data.isComplete, document.getElementById('l16'));
	number_init(json_data.isComplete, document.getElementById('l17'));
	number_init(json_data.isComplete, document.getElementById('l18'));
	number_init(json_data.isComplete, document.getElementById('l19'));
	number_init(json_data.isComplete, document.getElementById('l20'));
	number_init(json_data.isComplete, document.getElementById('l21'));
	number_init(json_data.isComplete, document.getElementById('l22'));
	number_init(json_data.isComplete, document.getElementById('l26'));
	number_init(json_data.isComplete, document.getElementById('l27'));

	blank_init_asi(json_data.isComplete, document.getElementById('comments'));

	asi_radioBtn_select(json_data.l1, document.getElementById('l1yes'), document.getElementById('l1no'));
	asi_radioBtn_select(json_data.l2, document.getElementById('l2yes'), document.getElementById('l2no'));
	asi_radioBtn_select(json_data.l24, document.getElementById('l24yes'), document.getElementById('l24no'));
	asi_radioBtn_select(json_data.l31, document.getElementById('l31yes'), document.getElementById('l31no'));
	asi_radioBtn_select(json_data.l32, document.getElementById('l32yes'), document.getElementById('l32no'));

	document.getElementById('l23').selectedIndex = json_data.l23;
	document.getElementById('l25').selectedIndex = json_data.l25;
	document.getElementById('l28').selectedIndex = json_data.l28;
	document.getElementById('l29').selectedIndex = json_data.l29;
	document.getElementById('l30').selectedIndex = json_data.l30;
}

function init_asi_family(json_data) {
	document.getElementById('h1a').selectedIndex = json_data.h1a;
	document.getElementById('h2a').selectedIndex = json_data.h2a;
	document.getElementById('h3a').selectedIndex = json_data.h3a;
	document.getElementById('h4a').selectedIndex = json_data.h4a;
	document.getElementById('h5a').selectedIndex = json_data.h5a;
	document.getElementById('h6a').selectedIndex = json_data.h6a;
	document.getElementById('h7a').selectedIndex = json_data.h7a;
	document.getElementById('h8a').selectedIndex = json_data.h8a;
	document.getElementById('h9a').selectedIndex = json_data.h9a;
	document.getElementById('h10a').selectedIndex = json_data.h10a;
	document.getElementById('h11a').selectedIndex = json_data.h11a;
	document.getElementById('h12a').selectedIndex = json_data.h12a;

	document.getElementById('h1d').selectedIndex = json_data.h1d;
	document.getElementById('h2d').selectedIndex = json_data.h2d;
	document.getElementById('h3d').selectedIndex = json_data.h3d;
	document.getElementById('h4d').selectedIndex = json_data.h4d;
	document.getElementById('h5d').selectedIndex = json_data.h5d;
	document.getElementById('h6d').selectedIndex = json_data.h6d;
	document.getElementById('h7d').selectedIndex = json_data.h7d;
	document.getElementById('h8d').selectedIndex = json_data.h8d;
	document.getElementById('h9d').selectedIndex = json_data.h9d;
	document.getElementById('h10d').selectedIndex = json_data.h10d;
	document.getElementById('h11d').selectedIndex = json_data.h11d;
	document.getElementById('h12d').selectedIndex = json_data.h12d;

	document.getElementById('h1p').selectedIndex = json_data.h1p;
	document.getElementById('h2p').selectedIndex = json_data.h2p;
	document.getElementById('h3p').selectedIndex = json_data.h3p;
	document.getElementById('h4p').selectedIndex = json_data.h4p;
	document.getElementById('h5p').selectedIndex = json_data.h5p;
	document.getElementById('h6p').selectedIndex = json_data.h6p;
	document.getElementById('h7p').selectedIndex = json_data.h7p;
	document.getElementById('h8p').selectedIndex = json_data.h8p;
	document.getElementById('h9p').selectedIndex = json_data.h9p;
	document.getElementById('h10p').selectedIndex = json_data.h10p;
	document.getElementById('h11p').selectedIndex = json_data.h11p;
	document.getElementById('h12p').selectedIndex = json_data.h12p;
}

function init_asi_soc1(json_data) {
	number_init(json_data.isComplete, document.getElementById('f2'));
	number_init(json_data.isComplete, document.getElementById('f5'));
	number_init(json_data.isComplete, document.getElementById('f11'));
	number_init(json_data.isComplete, document.getElementById('f30'));
	number_init(json_data.isComplete, document.getElementById('f31'));

	document.getElementById('f1').selectedIndex = json_data.f1;
	document.getElementById('f3').selectedIndex = json_data.f3;
	document.getElementById('f4').selectedIndex = json_data.f4;
	document.getElementById('f6').selectedIndex = json_data.f6;
	document.getElementById('f9').selectedIndex = json_data.f9;
	document.getElementById('f10').selectedIndex = json_data.f10;
	document.getElementById('f32').selectedIndex = json_data.f32;
	document.getElementById('f33').selectedIndex = json_data.f33;
	document.getElementById('f34').selectedIndex = json_data.f34;
	document.getElementById('f35').selectedIndex = json_data.f35;
	document.getElementById('f36').selectedIndex = json_data.f36;

	asi_radioBtn_select(json_data.f7, document.getElementById('f7yes'), document.getElementById('f7no'));
	asi_radioBtn_select(json_data.f8, document.getElementById('f8yes'), document.getElementById('f8no'));
	asi_radioBtn_select(json_data.f37, document.getElementById('f37yes'), document.getElementById('f37no'));
	asi_radioBtn_select(json_data.f38, document.getElementById('f38yes'), document.getElementById('f38no'));
}

function init_asi_soc2(json_data) {
	blank_init_asi(json_data.isComplete, document.getElementById('comments'));

	document.getElementById('f12').selectedIndex = json_data.f12;
	document.getElementById('f13').selectedIndex = json_data.f13;
	document.getElementById('f14').selectedIndex = json_data.f14;
	document.getElementById('f16').selectedIndex = json_data.f16;
	document.getElementById('f17').selectedIndex = json_data.f17;

	document.getElementById('f27d').selectedIndex = json_data.f27d;
	document.getElementById('f28d').selectedIndex = json_data.f28d;
	document.getElementById('f29d').selectedIndex = json_data.f29d;

	document.getElementById('f27y').selectedIndex = json_data.f27y;
	document.getElementById('f28y').selectedIndex = json_data.f28y;
	document.getElementById('f29y').selectedIndex = json_data.f28y;

	document.getElementById('f18d').selectedIndex = json_data.f18d;
	document.getElementById('f19d').selectedIndex = json_data.f19d;
	document.getElementById('f20d').selectedIndex = json_data.f20d;
	document.getElementById('f21d').selectedIndex = json_data.f21d;
	document.getElementById('f22d').selectedIndex = json_data.f22d;
	document.getElementById('f23d').selectedIndex = json_data.f23d;
	document.getElementById('f24d').selectedIndex = json_data.f24d;
	document.getElementById('f25d').selectedIndex = json_data.f25d;
	document.getElementById('f26d').selectedIndex = json_data.f26d;

	document.getElementById('f18y').selectedIndex = json_data.f18y;
	document.getElementById('f19y').selectedIndex = json_data.f19y;
	document.getElementById('f20y').selectedIndex = json_data.f20y;
	document.getElementById('f21y').selectedIndex = json_data.f21y;
	document.getElementById('f22y').selectedIndex = json_data.f22y;
	document.getElementById('f23y').selectedIndex = json_data.f23y;
	document.getElementById('f24y').selectedIndex = json_data.f24y;
	document.getElementById('f25y').selectedIndex = json_data.f25y;
	document.getElementById('f26y').selectedIndex = json_data.f26y;
}

function init_asi_psych(json_data) {
	number_init(json_data.isComplete, grab('p1'));
	number_init(json_data.isComplete, grab('p2'));
	number_init(json_data.isComplete, grab('p12'));
	blank_init_asi(json_data.isComplete, grab('comments'));

	grab('p4d').selectedIndex = json_data.p4d;
	grab('p5d').selectedIndex = json_data.p5d;
	grab('p6d').selectedIndex = json_data.p6d;
	grab('p7d').selectedIndex = json_data.p7d;
	grab('p8d').selectedIndex = json_data.p8d;
	grab('p9d').selectedIndex = json_data.p9d;
	grab('p10d').selectedIndex = json_data.p10d;
	grab('p11d').selectedIndex = json_data.p11d;

	grab('p4y').selectedIndex = json_data.p4y;
	grab('p5y').selectedIndex = json_data.p5y;
	grab('p6y').selectedIndex = json_data.p6y;
	grab('p7y').selectedIndex = json_data.p7y;
	grab('p8y').selectedIndex = json_data.p8y;
	grab('p9y').selectedIndex = json_data.p9y;
	grab('p10y').selectedIndex = json_data.p10y;
	grab('p11y').selectedIndex = json_data.p11y;

	grab('p13').selectedIndex = json_data.p13;
	grab('p14').selectedIndex = json_data.p14;
	grab('p21').selectedIndex = json_data.p21;

	asi_radioBtn_select(json_data.p3, grab('p3yes'), grab('p3no'));
	asi_radioBtn_select(json_data.p15, grab('p15yes'), grab('p15no'));
	asi_radioBtn_select(json_data.p16, grab('p16yes'), grab('p16no'));
	asi_radioBtn_select(json_data.p17, grab('p17yes'), grab('p17no'));
	asi_radioBtn_select(json_data.p18, grab('p18yes'), grab('p18no'));
	asi_radioBtn_select(json_data.p19, grab('p19yes'), grab('p19no'));
	asi_radioBtn_select(json_data.p20, grab('p20yes'), grab('p20no'));

	asi_radioBtn_select(json_data.p22, grab('p22yes'), grab('p22no'));
	asi_radioBtn_select(json_data.p23, grab('p23yes'), grab('p23no'));
}

//*********************************************** ASI POST FUNCTIONS *************************************************//
// post(isDynamic, field_type, field, trigger, target)

function processAsiAdmin() {
	post_asi(false, 'text', document.getElementById('g1'), null, null);
	post_asi(false, 'text', document.getElementById('g2'), null, null);
	post_asi(false, 'text', document.getElementById('g3'), null, null);
	post_asi(false, 'date', document.getElementById('popupDatepicker'), null, null);
	post_asi(false, 'text', document.getElementById('g11'), null, null);
}

function processAsiGeneral() {
	post_asi(false, 'number', document.getElementById('g14yrs'), null, null);
	post_asi(false, 'number', document.getElementById('g14mos'), null, null);
	post_asi(false, 'number', document.getElementById('g20'), null, null);

	post_asi(false, 'text', document.getElementById('g13'), null, null);	
	post_asi(false, 'text', document.getElementById('g21'), null, null);
	post_asi(false, 'text', document.getElementById('g22'), null, null);
	post_asi(false, 'text', document.getElementById('g23'), null, null);
	post_asi(false, 'text', document.getElementById('g24'), null, null);
	post_asi(false, 'text', document.getElementById('g25'), null, null);
	post_asi(false, 'text', document.getElementById('g26'), null, null);
	post_asi(false, 'text', document.getElementById('g27'), null, null);
	post_asi(false, 'text', document.getElementById('g28'), null, null);
	post_asi(false, 'text', document.getElementById('test1'), null, null);
	post_asi(false, 'text', document.getElementById('test2'), null, null);
	post_asi(false, 'text', document.getElementById('test3'), null, null);
}

function processAsiMedical() {
	post_asi(true, 'text', document.getElementById('m5Exp'), document.getElementById('m5yes'), document.getElementById('m_m5Exp'));
	post_asi(false, 'text', document.getElementById('comments'), null, null);

	post_asi(false, 'number', document.getElementById('m1'), null, null);
	post_asi(false, 'number', document.getElementById('m2yrs'), null, null);
	post_asi(false, 'number', document.getElementById('m2mth'), null, null);
	post_asi(false, 'number', document.getElementById('m6'), null, null);
}

// function post_asi(isDynamic, field_type, field, trigger, target)
function processAsiEmployment() {
	//PROCESS THE DYNAMIC FIELDS
	post_asi(true, 'text', document.getElementById('e3Exp'), document.getElementById('e3yes'), document.getElementById('m_e3Exp'));
	post_asi(true, 'radio', document.getElementById('e5yes'), document.getElementById('e4yes'), document.getElementById('m_e5'));
	post_asi(true, 'text', document.getElementById('e7Exp'), document.getElementById('e7yes'), document.getElementById('m_e7Exp'));
	post_asi(true, 'radio', document.getElementById('e9yes'), document.getElementById('e8yes'), document.getElementById('m_e9'));

	post_asi(false, 'number', document.getElementById('e1yrs'), null, null);
	post_asi(false, 'number', document.getElementById('e1mth'), null, null);
	post_asi(false, 'number', document.getElementById('e2'), null, null);
	post_asi(false, 'number', document.getElementById('e6yrs'), null, null);
	post_asi(false, 'number', document.getElementById('e6mth'), null, null);
	post_asi(false, 'number', document.getElementById('e11'), null, null);
	post_asi(false, 'number', document.getElementById('e12'), null, null);
	post_asi(false, 'number', document.getElementById('e13'), null, null);
	post_asi(false, 'number', document.getElementById('e14'), null, null);
	post_asi(false, 'number', document.getElementById('e15'), null, null);
	post_asi(false, 'number', document.getElementById('e16'), null, null);
	post_asi(false, 'number', document.getElementById('e17'), null, null);
	post_asi(false, 'number', document.getElementById('e18'), null, null);
	post_asi(false, 'number', document.getElementById('e19'), null, null);
}

// function post_asi(isDynamic, field_type, field, trigger, target)
function processAsiDrug1() {
	post_asi(false, 'number', document.getElementById('d1Day'), null, null);
	post_asi(false, 'number', document.getElementById('d2Day'), null, null);
	post_asi(false, 'number', document.getElementById('d3Day'), null, null);
	post_asi(false, 'number', document.getElementById('d4Day'), null, null);
	post_asi(false, 'number', document.getElementById('d5Day'), null, null);
	post_asi(false, 'number', document.getElementById('d6Day'), null, null);
	post_asi(false, 'number', document.getElementById('d7Day'), null, null);
	post_asi(false, 'number', document.getElementById('d8Day'), null, null);
	post_asi(false, 'number', document.getElementById('d9Day'), null, null);
	post_asi(false, 'number', document.getElementById('d10Day'), null, null);
	post_asi(false, 'number', document.getElementById('d11Day'), null, null);
	post_asi(false, 'number', document.getElementById('d12Day'), null, null);

	post_asi(false, 'number', document.getElementById('d1Year'), null, null);
	post_asi(false, 'number', document.getElementById('d2Year'), null, null);
	post_asi(false, 'number', document.getElementById('d3Year'), null, null);
	post_asi(false, 'number', document.getElementById('d4Year'), null, null);
	post_asi(false, 'number', document.getElementById('d5Year'), null, null);
	post_asi(false, 'number', document.getElementById('d6Year'), null, null);
	post_asi(false, 'number', document.getElementById('d7Year'), null, null);
	post_asi(false, 'number', document.getElementById('d8Year'), null, null);
	post_asi(false, 'number', document.getElementById('d9Year'), null, null);
	post_asi(false, 'number', document.getElementById('d10Year'), null, null);
	post_asi(false, 'number', document.getElementById('d11Year'), null, null);
	post_asi(false, 'number', document.getElementById('d12Year'), null, null);

	post_asi(false, 'number', document.getElementById('d15'), null, null);
	post_asi(false, 'number', document.getElementById('d16'), null, null);	
	post_asi(false, 'number', document.getElementById('d17'), null, null);
	post_asi(false, 'number', document.getElementById('d18'), null, null);
	post_asi(false, 'number', document.getElementById('d19'), null, null);
	post_asi(false, 'number', document.getElementById('d20'), null, null);
	post_asi(false, 'number', document.getElementById('d21'), null, null);
	post_asi(false, 'number', document.getElementById('d22'), null, null);
	post_asi(false, 'number', document.getElementById('d23'), null, null);
	post_asi(false, 'number', document.getElementById('d24'), null, null);
	post_asi(false, 'number', document.getElementById('d25'), null, null);
	post_asi(false, 'number', document.getElementById('d26'), null, null);
	post_asi(false, 'number', document.getElementById('d27'), null, null);

	post_asi(false, 'text', document.getElementById('comments'), null, null);
}

function processAsiLegal() {
	post_asi(false, 'number', document.getElementById('l3'), null, null);
	post_asi(false, 'number', document.getElementById('l4'), null, null);
	post_asi(false, 'number', document.getElementById('l5'), null, null);
	post_asi(false, 'number', document.getElementById('l6'), null, null);
	post_asi(false, 'number', document.getElementById('l7'), null, null);
	post_asi(false, 'number', document.getElementById('l8'), null, null);
	post_asi(false, 'number', document.getElementById('l9'), null, null);
	post_asi(false, 'number', document.getElementById('l10'), null, null);
	post_asi(false, 'number', document.getElementById('l11'), null, null);
	post_asi(false, 'number', document.getElementById('l12'), null, null);
	post_asi(false, 'number', document.getElementById('l13'), null, null);
	post_asi(false, 'number', document.getElementById('l14'), null, null);
	post_asi(false, 'number', document.getElementById('l15'), null, null);
	post_asi(false, 'number', document.getElementById('l16'), null, null);
	post_asi(false, 'number', document.getElementById('l17'), null, null);
	post_asi(false, 'number', document.getElementById('l18'), null, null);
	post_asi(false, 'number', document.getElementById('l19'), null, null);
	post_asi(false, 'number', document.getElementById('l20'), null, null);
	post_asi(false, 'number', document.getElementById('l21'), null, null);
	post_asi(false, 'number', document.getElementById('l22'), null, null);
	post_asi(false, 'number', document.getElementById('l26'), null, null);
	post_asi(false, 'number', document.getElementById('l27'), null, null);

	post_asi(false, 'text', document.getElementById('comments'), null, null);
}

function processAsiSocial1() {
	post_asi(false, 'number', document.getElementById('f2yrs'), null, null);
	post_asi(false, 'number', document.getElementById('f2mth'), null, null);
	post_asi(false, 'number', document.getElementById('f5yrs'), null, null);
	post_asi(false, 'number', document.getElementById('f5mth'), null, null);
	post_asi(false, 'number', document.getElementById('f11'), null, null);
	post_asi(false, 'number', document.getElementById('f30'), null, null);
	post_asi(false, 'number', document.getElementById('f31'), null, null);
}
function processAsiPsych() {
	post_asi(false, 'number', grab('p1'), null, null);
	post_asi(false, 'number', grab('p2'), null, null);
	post_asi(false, 'number', grab('p12'), null, null);
	
	post_asi(false, 'text', document.getElementById('comments'), null, null);
}

function processAsiFields(page) {
	page = String(page);

	if (page === '/asi_admin/') {
		processAsiAdmin();
	}
	else if (page === '/asi_general/') {
		processAsiGeneral();
	}
	else if (page === '/asi_medical/') {
		processAsiMedical();
	}
	else if (page === '/asi_employment/') {
		processAsiEmployment();
	}
	else if (page === '/asi_drug1/') {
		processAsiDrug1();
	}
	else if (page === '/asi_legal/') {
		processAsiLegal();
	}
	else if (page === '/asi_social1/') {
		processAsiSocial1();
	}
	else if (page === '/asi_psych/') {
		processAsiPsych();
	}
}

function reset_asi_subf(ftype) {
	ftype = String(ftype);

	if (ftype === 'social') {
		resetSelect(grab('f18d'));
		resetSelect(grab('f19d'));
		resetSelect(grab('f20d'));
		resetSelect(grab('f21d'));
		resetSelect(grab('f22d'));
		resetSelect(grab('f23d'));
		resetSelect(grab('f24d'));
		resetSelect(grab('f25d'));
		resetSelect(grab('f26d'));

		resetSelect(grab('f18y'));
		resetSelect(grab('f19y'));
		resetSelect(grab('f20y'));
		resetSelect(grab('f21y'));
		resetSelect(grab('f22y'));
		resetSelect(grab('f23y'));
		resetSelect(grab('f24y'));
		resetSelect(grab('f25y'));
		resetSelect(grab('f26y'));
	}
	else if (ftype === 'relate') {
		resetSelect(grab('f12'));
		resetSelect(grab('f13'));
		resetSelect(grab('f14'));
		resetSelect(grab('f16'));
		resetSelect(grab('f17'));
	}
	else if (ftype === 'abuse') {
		resetSelect(grab('f27d'));
		resetSelect(grab('f28d'));
		resetSelect(grab('f29d'));
		resetSelect(grab('f27y'));
		resetSelect(grab('f28y'));
		resetSelect(grab('f29y'));
	}
	else if (ftype === 'fh') {
		resetSelect(grab('h1a'));
		resetSelect(grab('h2a'));
		resetSelect(grab('h3a'));
		resetSelect(grab('h4a'));
		resetSelect(grab('h5a'));
		resetSelect(grab('h6a'));
		resetSelect(grab('h7a'));
		resetSelect(grab('h8a'));
		resetSelect(grab('h9a'));
		resetSelect(grab('h10a'));
		resetSelect(grab('h11a'));
		resetSelect(grab('h12a'));

		resetSelect(grab('h1d'));
		resetSelect(grab('h2d'));
		resetSelect(grab('h3d'));
		resetSelect(grab('h4d'));
		resetSelect(grab('h5d'));
		resetSelect(grab('h6d'));
		resetSelect(grab('h7d'));
		resetSelect(grab('h8d'));
		resetSelect(grab('h9d'));
		resetSelect(grab('h10d'));
		resetSelect(grab('h11d'));
		resetSelect(grab('h12d'));

		resetSelect(grab('h1p'));
		resetSelect(grab('h2p'));
		resetSelect(grab('h3p'));
		resetSelect(grab('h4p'));
		resetSelect(grab('h5p'));
		resetSelect(grab('h6p'));
		resetSelect(grab('h7p'));
		resetSelect(grab('h8p'));
		resetSelect(grab('h9p'));
		resetSelect(grab('h10p'));
		resetSelect(grab('h11p'));
		resetSelect(grab('hp12'));
	}
	else if (ftype === 'drug') {
		resetNumber(grab('d1Day'));
		resetNumber(grab('d2Day'));
		resetNumber(grab('d3Day'));
		resetNumber(grab('d4Day'));
		resetNumber(grab('d5Day'));
		resetNumber(grab('d6Day'));
		resetNumber(grab('d7Day'));
		resetNumber(grab('d8Day'));
		resetNumber(grab('d9Day'));
		resetNumber(grab('d10Day'));
		resetNumber(grab('d11Day'));
		resetNumber(grab('d12Day'));

		resetNumber(grab('d1Year'));
		resetNumber(grab('d2Year'));
		resetNumber(grab('d3Year'));
		resetNumber(grab('d4Year'));
		resetNumber(grab('d5Year'));
		resetNumber(grab('d6Year'));
		resetNumber(grab('d7Year'));
		resetNumber(grab('d8Year'));
		resetNumber(grab('d9Year'));
		resetNumber(grab('d10Year'));
		resetNumber(grab('d11Year'));
		resetNumber(grab('d12Year'));

		resetSelect(grab('d1Route'));
		resetSelect(grab('d2Route'));
		resetSelect(grab('d3Route'));
		resetSelect(grab('d4Route'));
		resetSelect(grab('d5Route'));
		resetSelect(grab('d6Route'));
		resetSelect(grab('d7Route'));
		resetSelect(grab('d8Route'));
		resetSelect(grab('d9Route'));
		resetSelect(grab('d10Route'));
		resetSelect(grab('d11Route'));
		resetSelect(grab('d12Route'));
		resetSelect(grab('d13'));
	}
	else if (ftype === 'psych') {
		resetSelect(grab('p4d'));
		resetSelect(grab('p5d'));
		resetSelect(grab('p6d'));
		resetSelect(grab('p7d'));
		resetSelect(grab('p8d'));
		resetSelect(grab('p9d'));
		resetSelect(grab('p10d'));
		resetSelect(grab('p11d'));

		resetSelect(grab('p4y'));
		resetSelect(grab('p5y'));
		resetSelect(grab('p6y'));
		resetSelect(grab('p7y'));
		resetSelect(grab('p8y'));
		resetSelect(grab('p9y'));
		resetSelect(grab('p10y'));
		resetSelect(grab('p11y'));
	}
}

//*********************************************** ASI SUPPORT FUNCTIONS *************************************************//

function openPopUp(location, url, w, h) {
	location = String(location);
	url = String(url);

	if (location === 'auto') {
		var lefts = Number((screen.width/2) - (w/2));
		var tops = Number((screen.height/2) - (h/2));
		var opWin = window.open(url, '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
		// var opWin = window.open('/hasExistingSession/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
	}
}

function getPopParent(element) {
	element = String(element);
	var result = window.opener.document.getElementById(element);
	return result;
}

function getTopParent(element) {
	element = String(element);
	var result = window.top.document.getElementById(element);
	return result;
}

function asi_radioBtn_select(sel_val, r1, r2) {
	sel_val = String(sel_val);

	if (sel_val === '1') {
		r1.checked = true;
	}
	else {
		r2.checked = true;
	}
}

function assign_radio1_9(m_val, r0, r1, r2, r3, r4, r5, r6, r7, r8, r9) {
	m_val = String(m_val);

	if (m_val === '0') {
		r0.checked = true;
	}
	else if (m_val === '1') {
		r1.checked = true;
	}
	else if (m_val === '2') {
		r2.checked = true;
	}
	else if (m_val === '3') {
		r3.checked = true;
	}
	else if (m_val === '4') {
		r4.checked = true;
	}
	else if (m_val === '5') {
		r5.checked = true;
	}
	else if (m_val === '6') {
		r6.checked = true;
	}
	else if (m_val === '7') {
		r7.checked = true;
	}
	else if (m_val === '8') {
		r8.checked = true;
	}
	else if (m_val === '9') {
		r9.checked = true;
	}
}

function m5Radio() {
	quickRadio(true, document.getElementById('m5yes'), document.getElementById('m5Exp_lab'), document.getElementById('m5Exp'));
}

function e3Radio() {
	quickRadio(true, document.getElementById('e3yes'), document.getElementById('e3Exp_lab'), document.getElementById('e3Exp'));
}

function e4Radio() {
	specialRadio(document.getElementById('e4yes'),document.getElementById('e5_lab'),document.getElementById('e5yes_lab'),document.getElementById('e5no_lab'),document.getElementById('e5no'),document.getElementById('e5yes'));
	additionalLabel(document.getElementById('e4yes'), document.getElementById('extra5'));
}

function e7Radio() {
	quickRadio(true, document.getElementById('e7yes'), document.getElementById('e7Exp_lab'), document.getElementById('e7Exp'));
}

function e8Radio() {
	specialRadio(document.getElementById('e8yes'),document.getElementById('e9_lab'),document.getElementById('e9no_lab'),document.getElementById('e9yes_lab'),document.getElementById('e9no'),document.getElementById('e9yes'));
	additionalLabel(document.getElementById('e8yes'), document.getElementById('extra9'));
}

function sessionChecking(btnType) {
	var actionApp = grab('tracking').value;
	actionApp = String(actionApp);
	btn = String(btnType);

	if (actionApp === 'Session') {
		var w = 400;
		var h = 400;
		openPopUp('auto', '/session_open_error/', w, h);
	}
	else {
		var form = grab('n_form_main');

		if (btn === 'home') {
			form.action = '/adminHome/';
		}
		else if (btn === 'bill') {
			form.action = '//'
		}
		else if (btn === 'admin') {
			form.action = '//'
		}
		else if (btn === 'appt') {
			form.action = '//'
		}
		else if (btn === 'logout') {
			form.action = '/logout/'
		}

		form.submit();
	}
}

//*********************************************** ASI PAGE SUBMITS *************************************************//

function continue_asi_form(section) {
	section = String(section);
	var form = document.getElementById('asi_form');
	var next_url = document.getElementById('next_url');
	var proceed = true;

	processAsiFields(section);

	if (proceed === true) {
		document.getElementById('save_this').value = 'true';
		form.action = next_url.value;
		form.submit();
	}
}

function continue_to_asi_form() {
	var form = document.getElementById('asi_instructions');
	form.action = '/asi_admin/';
	form.submit();
}

function sideBarASI(page) {
	document.getElementById('save_this').value = 'false';
	var form = document.getElementById('asi_form');
	form.action = page;
	form.submit();
}

//#####################################################################################################################//
//*********************************************************************************************************************//
//------------------------------------------------------ END ASI ------------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//



//#####################################################################################################################//
//*********************************************************************************************************************//
//-------------------------------------------------- SUPPORT FUNCTIONS ------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//

function ut_check_init(data, box) {
	data = String(data);

	if (data === 'true') {
		box.checked = true;
	}
	else {
		box.checked = false;
	}
}

function post_ut_check(box, target) {
	if (box.checked === true) {
		target.value = 'True';
	}
	else {
		target.value = 'False';
	}
}

function initialize_ut(json) {
	ut_check_init(json.drug1, grab('ut1'));
	ut_check_init(json.drug2, grab('ut2'));
	ut_check_init(json.drug3, grab('ut3'));
	ut_check_init(json.drug4, grab('ut4'));
	ut_check_init(json.drug5, grab('ut5'));
	ut_check_init(json.drug6, grab('ut6'));
	ut_check_init(json.drug7, grab('ut7'));
	ut_check_init(json.drug8, grab('ut8'));
	ut_check_init(json.drug9, grab('ut9'));
	ut_check_init(json.drug10, grab('ut10'));
	ut_check_init(json.drug11, grab('ut11'));
}

function doNotPayUT() {
	grab('ut_form').action = '/clientOptions/';
	grab('ut_form').submit();
}

function payUT() {
	var w = 550, h = 485;
	var lefts = Number((screen.width/2) - (w/2));
	var tops = Number((screen.height/2) - (h/2));
	var opWin = window.open('/ut_pay/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
}

function ut_was_paid() {
	document.getElementById('p_form').submit();
}

function ut_payment_accepted() {
	var form = window.opener.document.getElementById('ut_form');
	form.action = '/ut_preliminary/';
	window.close()
	form.submit();
}

function reset_ut() {
	grab('ut1').checked = false;
	grab('ut2').checked = false;
	grab('ut3').checked = false;
	grab('ut4').checked = false;
	grab('ut5').checked = false;
	grab('ut6').checked = false;
	grab('ut7').checked = false;
	grab('ut8').checked = false;
	grab('ut9').checked = false;
	grab('ut10').checked = false;
	grab('ut11').checked = false;
	grab('popupDatepicker').value = '';
}

function cancel_ut() {
	grab('ut_form').action = '/clientOptions/';
	grab('ut_form').submit();
}

function continue_ut() {
	post_ut_check(grab('ut1'), grab('m_ut1'));
	post_ut_check(grab('ut2'), grab('m_ut2'));
	post_ut_check(grab('ut3'), grab('m_ut3'));
	post_ut_check(grab('ut4'), grab('m_ut4'));
	post_ut_check(grab('ut5'), grab('m_ut5'));
	post_ut_check(grab('ut6'), grab('m_ut6'));
	post_ut_check(grab('ut7'), grab('m_ut7'));
	post_ut_check(grab('ut8'), grab('m_ut8'));
	post_ut_check(grab('ut9'), grab('m_ut9'));
	post_ut_check(grab('ut10'), grab('m_ut10'));
	post_ut_check(grab('ut11'), grab('m_ut11'));
	grab('m_date').value = grab('popupDatepicker').value;

	grab('save_this').value = 'true';
	grab('ut_form').action = '/ut_viewForm/';
	grab('ut_form').submit();
}

//#####################################################################################################################//
//*********************************************************************************************************************//
//--------------------------------------------------------- END UT ----------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//



//#####################################################################################################################//
//*********************************************************************************************************************//
//------------------------------------------------- SUPPORT FUNCTIONS ------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//

function eliminateWhiteSpace(field) {
	var result = '';
	var val = String(field.value);

	for (var i = 0; i < val.length; i++)
	{
		if (val.charAt(i) !== ' ') {
			result += val.charAt(i);
		}
	}

	return result;
}

function fieldIsEmpty(field) {
	var val = String(eliminateWhiteSpace(field));
	var fieldEmpty = false;

	if (val === null || val === '' || val === 'None') {
		fieldEmpty = true;
	}

	return fieldEmpty;
}

function quickRadioText(trigger, label, field) {
	if (trigger.checked === true) {
		field.disabled = false;
		opacityHigh(label);
		opacityHigh(field);
	}
	else {
		opacityLow(label);
		opacityLow(field);
		field.value = '';
		field.disabled = true;
	}
}

function quickRadioNumber(trigger, label, field) {
	if (trigger.checked === true) {
		field.disabled = false;
		opacityHigh(label);
		opacityHigh(field);
	}
	else {
		opacityLow(label);
		opacityLow(field);
		field.value = '0';
		field.disabled = true;
	}
}

function specialRadio(trigger, label1, label2, label3, field1, field2) {
	if (trigger.checked === true) {
		field1.disabled = false;
		field2.disabled = false;
		opacityHigh(label1);
		opacityHigh(label2);
		opacityHigh(label3);
		opacityHigh(field1);
		opacityHigh(field2);
	}
	else {
		opacityLow(label1);
		opacityLow(label2);
		opacityLow(label3);
		opacityLow(field1);
		opacityLow(field2);
		field1.checked = true;
		field1.disabled = true;
		field2.disabled = true;
	}
}

function quickRadio(isText, trigger, label1, field1) {
	if (isText === true) {
		quickRadioText(trigger, label1, field1);
	}
	else {
		quickRadioNumber(trigger, label1, field1);
	}
}

function additionalLabel(trigger, label) {
	if (trigger.checked === true) {
		opacityHigh(label);
	}
	else {
		opacityLow(label);
	}
}


function isValidNumber(m_val) {
	var isValid = false;
	val = String(m_val);

	if (val==='0'| val==='1'| val==='2'| val==='3'| val==='4'| val==='5'| val==='6'| val==='7'| val==='8'| val==='9') {
		isValid = true;
	}
	return isValid
}

function isValidDateEntry(date) {
	var year = '';
	var day = '';
	var month = '';
	var isValid = false;
	var continue_search = true;
	var d = String(date.value);
	var len = d.length;

	if (len !== 10) {
		continue_search = false;
	}

	if (continue_search === true) {
		if (d.charAt(2) !== '/' || d.charAt(5) !== '/') {
			continue_search = false;
		}
	}

	if (continue_search === true) {
		year += d.charAt(6);
		year += d.charAt(7);
		year += d.charAt(8);
		year += d.charAt(9);
		month += d.charAt(0);
		month += d.charAt(1);
		day += d.charAt(3);
		day += d.charAt(4);

		if (isValidNumberEntry(year) === false || isValidNumberEntry(month) === false || isValidNumberEntry(day) === false) {
			continue_search = false;
		}
	}

	if (continue_search === true) {
		isValid = true;
	}

	return isValid;
}

function isValidNumberEntry(field) {
	var isValid = true;
	var val = String(field.value);

	for (var i = 0; i < val.length; i++) {
		if (isValidNumber(val.charAt(i)) === false) {
			isValid = false;
			break;
		}
	}

	return isValid;
}

function correctText(field) {
	if (fieldIsEmpty(field) === true) {
		field.value = 'N/A';
	}
}

function correctText_asi(field) {
	if (fieldIsEmpty(field) === true) {
		field.value = 'N';
	}
}

function correctNumber(field) {
	if (fieldIsEmpty(field) === true || isValidNumberEntry === false) {
		field.value = '0';
	}
}

function correctDate(field) {
	if (fieldIsEmpty(field) === true || isValidDateEntry(field) === false) {
		field.value = '01/01/1900';
	}
}

function fieldCorrection(field_type, field) {
	field_type = String(field_type);

	if (field_type === 'text') {
		correctText(field);
	}
	else if (field_type === 'number') {
		correctNumber(field);
	}
	else if (field_type === 'date') {
		correctDate(field);
	}
}

function fieldCorrection_asi(field_type, field) {
	field_type = String(field_type);

	if (field_type === 'text') {
		correctText_asi(field);
	}
	else if (field_type === 'number') {
		correctNumber(field);
	}
	else if (field_type === 'date') {
		correctDate(field);
	}
}

function uniDynamicFields(field_type, field, trigger, target) {
	field_type = String(field_type);

	if (field_type === 'text') {
		postUniversalRadioText(trigger, field, target);
	}
	else if (field_type === 'number') {
		postUniversalRadioNumber(trigger, field, target);
	}
	else if (field_type === 'select') {
		postUniversalRadioText(trigger, field, target);
	}
	else if (field_type === 'checkbox') {
		postUniversalRadioText(trigger, field, target);
	}
	else if (field_type === 'radio') {
		postUniversalRadioRadio(trigger, field, target);
	}
	else if (field_type === 'date') {

	}
}

function postSuperRadioASI(trigger, radio, target) {
	if (trigger.checked === true) {
		if (radio.checked === true) {
			target.value = '1';
		}
		else {
			target.value = '0';
		}
	}
	else {
		target.value = '0';
	}
}

function uniDynamicFields_asi(field_type, field, trigger, target) {
	field_type = String(field_type);

	if (field_type === 'text') {
		postUniversalRadioText_asi(trigger, field, target);
	}
	else if (field_type === 'number') {
		postUniversalRadioNumber(trigger, field, target);
	}
	else if (field_type === 'select') {
		postUniversalRadioText_asi(trigger, field, target);
	}
	else if (field_type === 'checkbox') {
		postUniversalRadioText_asi(trigger, field, target);
	}
	else if (field_type === 'radio') {
		postSuperRadioASI(trigger, field, target);
	}
	else if (field_type === 'date') {

	}
}

function post(isDynamic, field_type, field, trigger, target) {
	if (isDynamic === true) {
		uniDynamicFields(field_type, field, trigger, target);
	}
	else {
		fieldCorrection(field_type, field);
	}
}

function post_asi(isDynamic, field_type, field, trigger, target) {
	if (isDynamic === true) {
		uniDynamicFields_asi(field_type, field, trigger, target);
	}
	else {
		fieldCorrection_asi(field_type, field);
	}
}

function blank_init(isComplete, field) {
	isComplete = String(isComplete);

	if (isComplete === 'false') {
		if (fieldIsEmpty(field) === true || field.value === 'N/A' || field.value === 'NA') {
			field.value = '';
		}
	}
}

function blank_init_asi(isComplete, field) {
	isComplete = String(isComplete);

	if (isComplete === 'false') {
		if (fieldIsEmpty(field) === true || field.value === 'X' || field.value === 'N' ) {
			field.value = '';
		}
	}
}

function number_init(isComplete, field) {
	isComplete = String(isComplete);

	if (isComplete === 'false') {
		if (fieldIsEmpty(field) === true || field.value === 'N/A' || field.value === 'NA') {
			field.value = 0;
		}
	}
}

function number_init_asi(isComplete, field) {
	isComplete = String(isComplete);

	if (isComplete === 'false') {
		if (fieldIsEmpty(field) === true || field.value === 'X' || field.value === 'N') {
			field.value = 0;
		}
	}
}

function grab(elementName) {
	var el = document.getElementById(elementName);
	return el;
}

function resetSelect(field) {
	field.selectedIndex = 0;
}

function resetNumber(field) {
	field.value = 0;
}


//=====================================================================================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//=================================================++ END POSTING =====================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//=====================================================================================================================//


//=====================================================================================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//================================================++ Client Options ++=================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//=====================================================================================================================//

function setHistorySel(json_data, sel) {
	json_data = String(json_data);

	if (json_data === 'low') {
		sel.selectedIndex = 0;
	}
	else if (json_data === 'high') {
		sel.selectedIndex = 1;
	}
}

function sort_history() {
	grab('dorder').value = grab('d_order').value;
	grab('forder').value = grab('f_order').value;
	grab('c_form').action = '/clientHistory/';
	grab('c_form').submit();
}

function init_clientHistory(json_data) {
	setHistorySel(json_data.f_order, grab('f_order'));
	setHistorySel(json_data.d_order, grab('d_order'));
}

function history_to_options() {
	grab('c_form').action = '/clientOptions/';
	grab('c_form').submit();
}


//=====================================================================================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++ END POSTING +++++++++++++++++++++++++++++++++++++++++++++++++++++//
//=====================================================================================================================//


//=====================================================================================================================//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//=====================================================================================================================//

function sideBarOption(page) {
	document.getElementById('save_this').value = 'false';

	if (String(page) === 'sapClinic') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_demographic/';
		form.submit();
	}

	else if (String(page) === 'sapSocial') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_social/';
		form.submit();
	}

	else if (String(page) === 'sapPsycho1') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_psychoactive/';
		form.submit();
	}

	else if (String(page) === 'sapPsycho2') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_psychoactive2/';
		form.submit();
	}

	else if (String(page) === 'sapSpecial') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_special/';
		form.submit();
	}

	else if (String(page) === 'sapOther') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_other/';
		form.submit();
	}

	else if (String(page) === 'sapSource') {
		var form = document.getElementById('sap_form');
		form.action = '/sap_sources/';
		form.submit();
	}
}

function sideBarMh(page){
	page = String(page);
	document.getElementById('save_this').value = 'false';
	form = document.getElementById('mh_form');
	form.action = page;
	form.submit();
}

function getFormElement(form_type) {
	var result = null;

	if (String(form_type) === 'am') {
		result = grab('am_demo');
	}
	else if (String(form_type) === 'sap') {
		result = grab('sap_form');
	}
	else if (String(form_type) === 'mh') {
		result = grab('mh_form');
	}

	else if (String(form_type) === 'asi') {
		result = grab('asi_form');
	}
	else if (String(form_type) === 'ut') {
		result = grab('ut_form')
	}
	else if (String(form_type) === 'discharge') {
		result = grab('d_form')
	}

	return result;
}

function getGenericFormID(form_type) {
	form_type = String(form_type)
	var result = null;

	if (form_type === 'mh') {
		result = 'mh_form';
	}
	else if (form_type === 'am') {
		result = 'am_form';
	}
	else if (form_type === 'sap') {
		result = 'sap_id';
	}
	else if (form_type === 'asi') {
		result = 'asi_id'
	}

	return result;
}

function universal_generic_exit(form_type, page) {
	page = String(page);
	form_type = String(form_type);

	var exit_type = document.getElementById('exit_type');
	var form = getFormElement(form_type);

	if (page === '/mh_demographic/') {
		processDynamicMhHistory();
	}
	else if (page === '/mh_education/') {
		processDynamicMhEducation();
	}
	else if (page === '/mh_stress/') {
		processDynamicMhStress();
	}
	else if (page === '/mh_familyHistory/') {
		processDynamicMhFamily();
	}
	else if (page === '/mh_legal/') {
		processDynamicMhLegal();
	}

	if (form_type === 'am') {
		universal_am_dynamic_post(page);
	}

	if (form_type === 'asi') {
		processAsiFields(page);
	}
	if (form_type === 'ut') {
		continue_ut();
	}

	form.action = '/uni_generic_exit/';
	exit_type.value = String(form_type);
	form.submit();
}


function generic_exit(form_type, section) {
	var exit_type = document.getElementById('exit_type');
	var form = getFormElement(form_type);

	form.action = '/generic_exit/';
	exit_type.value = String(form_type);
	form.submit();
}

function genericReturnToForm() {
	var form = document.getElementById('exit_form');
	var section = document.getElementById('last_section');
	var back = document.getElementById('back');
	var goToNext = document.getElementById('goToNext');

	//ACTUAL SESSION FORM DATA
	var form_id = document.getElementById('form_id').value;
	var form_type = String(document.getElementById('form_type').value);

	back.value = 'true';
	goToNext.value = 'true';
	form.action = section.value;
	form.submit();
}

function generic_to_session() {
	var form = document.getElementById('exit_form');
	var goToNext = document.getElementById('goToNext');

	goToNext.value = 'false';
	form.action = '/clientOptions/';
	form.submit();
}

function v_exit_session() {	
	var f_id = getPopParent('form_name').value;
	f_id = String(f_id);
	var form = getPopParent(f_id);

	grab('s_form').submit();
	

	form.action = '/adminHome/';
	form.submit();
}

function c_exit_session() {
	grab('s_form').submit();

	var f_id = getTopParent('form_name').value;
	f_id = String(f_id);
	var form = getTopParent(f_id);

	form.action = '/adminHome/';
	form.submit();

	grab('s_form').submit();	
}

function chooseSessionExit(answer) {
	grab('s_form').action = '/sessionClosed/';
	grab('s_form').submit();

	var f_id = getPopParent('form_name').value;
	f_id = String(f_id);

	var form = getPopParent(f_id);
	form.action = '/adminHome/';
	form.submit();
}

function generic_exit_home() {
	var w = 500, h = 250;
	var lefts = Number((screen.width/2) - (w/2));
	var tops = Number((screen.height/2) - (h/2));
	var opWin = window.open('/closeSession/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
}

function generic_delete_form() {
	var w = 450, h = 210;
	var lefts = Number((screen.width/2) - (w/2));
	var tops = Number((screen.height/2) - (h/2));
	var delWin = window.open('/genericDelete/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
}

function complete_generic_delete() {
	var form = document.getElementById('exit_g');
	document.getElementById('parent_form_type').value = window.opener.document.getElementById('form_type').value;
	document.getElementById('parent_form_id').value = window.opener.document.getElementById('form_id').value;
	form.submit();
}

function initialize_generic_popup() {
	var form_id = window.opener.document.getElementById('form_id');
	var form_type = window.opener.document.getElementById('form_type');

	document.getElementById('parent_form_id').value = form_id.value;
	document.getElementById('parent_form_type').value = form_type.value;
}

function genericReturntoSession() {
	var form = window.opener.document.getElementById('exit_form');
	form.action = '/clientOptions/';
	form.submit();
	window.close();
}

function genericEndSession() {
	var form = window.opener.document.getElementById('exit_form');
	form.action = '/comfirmSessionEnd/';
	form.submit();
	window.close();
}

function goToGenericURL() {
	var form = document.getElementById('resolve_form');
	var location = document.getElementById('save_section');
	var c1 = document.getElementById('c1');
	var c2 = document.getElementById('c2');

	if (c1.checked === true) {
		form.action = location.value;
		form.submit();
	}

	else if (c2.checked === true) {
		var w = 460, h = 250;
		var lefts = Number((screen.width/2) - (w/2));
		var tops = Number((screen.height/2) - (h/2));
		var refresh = window.open('/genericRefreshForm/', '', 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=1, copyhistory=no, width='+w+', height='+h+', top='+tops+', left='+lefts);
		form.submit();
	}

	else {
		form.action = '/clientOptions/';
		form.submit();
	}
}

function initialize_refresh_popup() {
	var form_id = window.opener.document.getElementById('form_id');
	var form_type = window.opener.document.getElementById('form_type');
	var session_id = window.opener.document.getElementById('session_id');

	document.getElementById('child_form_id').value = form_id.value;
	document.getElementById('child_form_type').value = form_type.value;
	document.getElementById('child_session_id').value = session_id.value;
}

function refreshForm() {
	var form = document.getElementById('refresh_form');
	form.submit();
}

function restart_form() {
	var form = window.opener.document.getElementById('resolve_form');
	var save_section = document.getElementById('save_section');

	window.opener.document.getElementById('back').value = 'true';
	window.opener.document.getElementById('new_form').value = 'false';

	form.action = save_section.value;
	form.submit();
	window.close();
}

function amSideBtnSubmit(url) {
	url = String(url);
	var form = document.getElementById('am_demo');
	document.getElementById('save_this').value = 'false';
	form.action = url;
	form.submit();
}

































