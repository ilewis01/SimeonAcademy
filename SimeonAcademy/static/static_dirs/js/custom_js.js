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
	}
}

function initalize_am_connections() {
	connectionCheck();
}

function continue_to_worst() {
	document.getElementById('am_demo').submit();
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
	var selectBox = document.getElementById('iUsedWorst');
	var label = document.getElementById('iUsedLabel');

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

function initalize_am_worst() {
	worstCheck();
	activateWorstRadio();
}

function continue_to_target() {
	document.getElementById('am_demo').submit();
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

function initalize_am_target() {
	amTargetOther();
}

function continue_to_am_family() {
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

function continue_am_dh() {
	var first_drink_age = document.getElementById('first_drink');
	var m_first_drink_age = document.getElementById('m_first_drink');
	m_first_drink_age.value = first_drink_age.value;
	// var proceed = true;
	// var continue_test = true;
	// var check_next = true;
	
	// var first_drink = document.getElementById('first_drink');	
	// var first_use_type = document.getElementById('first_use_type');

	// var m_first_drink = document.getElementById('m_first_drink');
	// var m_first_use_type = document.getElementById('m_first_use_type');

	// if (evaluate_field(first_drink, m_first_drink, "(age of first drink)") === false) {
	// 	continue_test = false;
	// 	proceed = false;
	// }
	// if (continue_test === true) {
	// 	if (evaluate_field(first_use_type, m_first_use_type, "(what client used | first drink)") === false) {
	// 		continue_test = false;
	// 		proceed = false;
	// 	}
	// }

	// if (continue_test === true) {
	// 	var sub_cont = true;
	// 	var what_you_use = document.getElementById('what-you-use');
	// 	var how_often_you_use = document.getElementById('how-often-you-use');
	// 	var how_much_you_use = document.getElementById('how-much-you-use');
	// 	var quitMos = document.getElementById('quitMos');
	// 	var quitYrs = document.getElementById('quitYrs');
	// 	var reason_quit = document.getElementById('reason_quit');

	// 	var m_what_you_use = document.getElementById('m-what-you-use');
	// 	var m_how_often_you_use = document.getElementById('m-how-often-you-use');
	// 	var m_how_much_you_use = document.getElementById('m-how-much-you-use');
	// 	var m_quitMos = document.getElementById('m_quitMos');
	// 	var m_quitYrs = document.getElementById('m_quitYrs');
	// 	var m_reason_quit = document.getElementById('m_reason_quit');

	// 	var does_drink = document.getElementById('current_use');
	// 	var ever_drank = document.getElementById('has_used');

	// 	proceed = evaluate_checked_true(does_drink, what_you_use, m_what_you_use, "(what client currently uses)");
	// 	sub_cont = proceed;

	// 	if (sub_cont === true) {
	// 		proceed = evaluate_checked_true(does_drink, how_often_you_use, m_how_often_you_use, "(how often client uses)");
	// 		sub_cont = proceed;
	// 	}

	// 	if (sub_cont === true) {
	// 		proceed = evaluate_checked_true(does_drink, how_much_you_use, m_how_much_you_use, "(how much client uses)");
	// 		sub_cont = proceed;
	// 	}

	// 	if (sub_cont === true) {
	// 		m_quitMos.value = '0';
	// 		m_quitYrs.value = '0';
	// 		m_reason_quit.value = '';
	// 	}

	// 	if (sub_cont === true) {
	// 		sub_2_cont = true;

	// 		if (does_drink.checked === false) {
	// 			proceed = evaluate_checked_true(ever_drank, quitMos, m_quitMos, "(months client has been abstinent)");
	// 			sub_2_cont = proceed;
	// 		}

	// 		if (sub_2_cont === true) {
	// 			proceed = evaluate_checked_true(ever_drank, quitYrs, m_quitYrs, "(years client has been abstinent)");
	// 			sub_2_cont = proceed;
	// 		}

	// 		if (sub_2_cont === true) {
	// 			proceed = evaluate_checked_true(ever_drank, reason_quit, m_reason_quit, "(reason client stopped using)");
	// 			sub_2_cont = proceed;
	// 		}

	// 		if (sub_2_cont === true) {
	// 			m_what_you_use.value = '';
	// 			m_how_much_you_use.value = '';
	// 			m_how_often_you_use.value = '';
	// 		}
	// 		continue_test = sub_2_cont;
	// 	}

	// 	if (continue_test === true) {
	// 		var sub3 = true;
	// 		var has_dui = document.getElementById('dui');
	// 		var dui_amount = document.getElementById('dui_amount');
	// 		var BAL = document.getElementById('BAL');
	// 		var m_dui_amount = document.getElementById('m_dui_amount');
	// 		var m_BAL = document.getElementById('m_BAL');

	// 		proceed = evaluate_checked_true(has_dui, dui_amount, m_dui_amount, "(number of DUI's)");
	// 		sub3 = proceed;

	// 		if (sub3 === true) {
	// 			proceed = evaluate_checked_true(has_dui, BAL, m_BAL, "(blood alcohol level)");
	// 		}
	// 		else {
	// 			m_dui_amount.value = '0';
	// 			m_BAL.value = '';
	// 		}
	// 		continue_test = proceed;
	// 	}

	// 	if (continue_test === true) {
	// 		var sub4 = true;
	// 		var had_treatment = document.getElementById('had_treatment');
	// 		var completed_treatment = document.getElementById('did_complete');
	// 		var not_abstinent = document.getElementById('not_abstinent');

	// 		var when_treated = document.getElementById('when_treated');
	// 		var where_treated = document.getElementById('where_treated');
	// 		var no_treat_explain = document.getElementById('no_treat_explain');
	// 		var relapse_explain = document.getElementById('relapse_explain');

	// 		var m_when_treated = document.getElementById('m_when_treated');
	// 		var m_where_treated = document.getElementById('m_where_treated');
	// 		var m_no_treat_explain = document.getElementById('m_no_treat_explain');
	// 		var m_relapse_explain = document.getElementById('m_relapse_explain');

	// 		proceed = evaluate_checked_true(had_treatment, when_treated, m_when_treated, "(when did client receive treatment)");
	// 		sub4 = proceed;

	// 		if (sub4 === true) {
	// 			proceed = evaluate_checked_true(had_treatment, where_treated, m_where_treated, "(where did the client receive treatment)");
	// 			sub4 = proceed;
	// 		}

	// 		if (sub4 === true) {
	// 			if (completed_treatment.checked === true) {
	// 				m_no_treat_explain.innerHTML = '';
	// 				m_relapse_explain.innerHTML = '';
	// 			}
	// 			else {
	// 				if (not_abstinent.checked === true) {
	// 					proceed = evaluate_field(relapse_explain, m_relapse_explain, "(why did client relapse)");
	// 				}
	// 			}
	// 		}
	// 	}
	// }


	// if (proceed === true) {
	// 	document.getElementById('am_demo').submit();
	// }
	document.getElementById('am_demo').submit();
}











