
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//******************************************************* ERROR CHECKER *************************************************************//
//******************************************************* ERROR CHECKER *************************************************************//
//******************************************************* ERROR CHECKER *************************************************************//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//


function quote(value) {
	value = String(value);
	return " + " + value  + " + ";
}

function isBlankText(value) {
	var isBlank = false;
	value = String(value);	
	if (value === "" || value === " " || value === null || value === 'None') {
		isBlank = true;
	}
	return isBlank;
}

function isBlankSelect(field) {
	var isBlank = false;
	if (field.selectedIndex === 0) {
		isBlank = true;
	}
	return isBlank;
}

function numbersOnly(value) {
	var result = "";
	d = String(value);

	for (var i = 0; i < d.length; i++) {
		if (d.charAt(i)==='1' || d.charAt(i)==='2' || d.charAt(i)==='3' || d.charAt(i)==='4' || d.charAt(i)==='5' || d.charAt(i)==='6' || d.charAt(i)==='7' || d.charAt(i)==='8' || d.charAt(i)==='9' || d.charAt(i)==='0') {
			result += d.charAt(i);
		}
	}
	return result;
}

function validateNumber(value) {
	isNumber = null;
	d = String(value);

	for (var i = 0; i < d.length; i++) {
		if (d.charAt(i)==='0' || d.charAt(i)==='1' || d.charAt(i)==='2' || d.charAt(i)==='3' || d.charAt(i)==='4' || d.charAt(i)==='5' || d.charAt(i)==='6' || d.charAt(i)==='7' || d.charAt(i)==='8' || d.charAt(i)==='9') {
			isNumber = true;
		}
		else {
			isNumber = false;
			break;
		}
	}
	
	return isNumber;
}

function validatePhone(value) {
	var isGood = false;
	var phone = numbersOnly(value);

	if (val.length === 10) {
		isGood = true;
	}
	return isGood;
}

function clearWhiteSpace(value) {
	var result = "";
	value = String(value);

	for (var i = 0; i < value.length; i++) {
		if (value.charAt(i) !== " ") {
			result += value.charAt(i);
		}
	}
	return result;
}

function textErrorChecker(item) {
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;
	val = String(val);

	if (item['isDynamic'] === false) {
		if (isBlankText(val) === true) {
			setErrorDiv(item['div']);
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (isBlankText(val) === true) {
				setErrorDiv(item['div']);
			}
		}
	}
}

function hasTextError(item) {
	var numErrors = 0;
	var hasErrors = false;
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;
	val = String(val);

	if (item['isDynamic'] === false) {
		if (isBlankText(val) === true) {
			numErrors += 1;
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (isBlankText(val) === true) {
				numErrors += 1;
			}
		}
	}

	if (numErrors > 0) {
		hasErrors = true;
	}
	return hasErrors;
}

function numberErrorChecker(item) {
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;

	if (item['isDynamic'] === false) {
		if (validateNumber(val) === false || isBlankText(val) === true) {
			setErrorDiv(item['div']);
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (validateNumber(val) === false || isBlankText(val) === true) {
				setErrorDiv(item['div']);
			}
		}
	}
}

function numberErrorChecker_noZero(item) {
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;

	if (item['isDynamic'] === false) {
		if (validateNumber(val) === false || isBlankText(val) === true || String(val) === '0') {
			setErrorDiv(item['div']);
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (validateNumber(val) === false || isBlankText(val) === true || String(val) === '0') {
				setErrorDiv(item['div']);
			}
		}
	}
}

function hasNumberErrors(item) {
	var numErrors = 0;
	var hasErrors = false;
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;

	if (item['isDynamic'] === false) {
		if (validateNumber(val) === false || isBlankText(val) === true) {
			numErrors += 1;
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (validateNumber(val) === false || isBlankText(val) === true) {
				numErrors += 1;
			}
		}
	}

	if (numErrors > 0) {
		hasErrors = true;
	}
	return hasErrors;
}

function hasNumberErrors_noZero(item) {
	var numErrors = 0;
	var hasErrors = false;
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;

	if (item['isDynamic'] === false) {
		if (validateNumber(val) === false || isBlankText(val) === true || String(val) === '0') {
			numErrors += 1;
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (validateNumber(val) === false || isBlankText(val) === true || String(val) === '0') {
				numErrors += 1;
			}
		}
	}

	if (numErrors > 0) {
		hasErrors = true;
	}
	return hasErrors;
}

function selectErrorChecker(item) {
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);

	if (item['isDynamic'] === false) {
		if (field.selectedIndex === 0) {
			setErrorDiv(item['div']);
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (String(field.value) === 'None Selected') {
				setErrorDiv(item['div']);
			}
		}
	}
}

function hasSelectErrors(item) {
	var numErrors = 0;
	var hasErrors = false;
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);

	if (item['isDynamic'] === false) {
		if (field.selectedIndex === 0) {
			numErrors += 1;
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (trigger.checked === true) {
			if (String(field.value) === 'None Selected') {
				numErrors += 1;
			}
		}
	}
	if (numErrors > 0) {
		hasErrors = true;
	}
	return hasErrors;
}

function phoneErrorChecker(item) {
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;
	val = numbersOnly(val);

	if (item['isDynamic'] === false) {
		if (val.length !== 10) {
			setErrorDiv(item['div']);
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (val.length !== 10) {
			setErrorDiv(item['div']);
		}
	}
}

function hasPhoneErrors(item) {
	var numErrors = 0;
	var hasErrors = false;
	var fieldName = item['field'];
	fieldName = String(fieldName);
	var field = grab(fieldName);
	var val = field.value;
	val = numbersOnly(val);

	if (item['isDynamic'] === false) {
		if (val.length !== 10) {
			numErrors += 1;
		}
	}
	else {
		var triggerName = item['trigger'];
		triggerName = String(triggerName);
		var trigger = grab(triggerName);

		if (val.length !== 10) {
			numErrors += 1;
		}
	}
	if (numErrors > 0) {
		hasErrors = true;
	}
	return hasErrors;
}

function ssnErrorChecker(item) {
	
}

function hasSsnErrors(item) {

}

function dateErrorChecker(item) {
	
}

function hasDateErrors(item) {
	
}

function validateSSN(field) {
	var isGood = false;
	var val = numbersOnly(field);
	val = clearWhiteSpace(val);

	if (val.length === 9) {
		isGood = true;
	}
	return isGood;
}

function validateDate(field) {
	var isGood = true;
	return isGood;
}

function setErrorDiv(divName) {
	divName = String(divName);
	var div = grab(divName);
	div.className = 'iml-error-set';
}

function setErrorDivPsy(divName) {
	divName = String(divName);
	var div = grab(divName);
	div.className = 'iml-psy-hor-psy';
}

function noErrorText(divName, fieldName) {
	divName = String(divName);
	fieldName = String(fieldName);

	var div = grab(divName);
	var field = grab(fieldName);
	var val = field.value;
	val = String(val);

	if (isBlankText(val) === false) {
		div.className = '';
	}
}

function noErrorText2(groupNumber) {
	var group = get_sap_pgroupFields(groupNumber);
	var hasErrors = sap_p_hasErrors(group);
	
	if (hasErrors === false) {
		var divName = String(group[0]['div']);
		var div = grab(divName);
		div.className = 'iml-psy-hor';
	}
}

function noErrorTextMH1(divName, fieldName) {
	divName = String(divName);

	var hasError = mh_opLine_hasErrors(divName);

	if (hasError === false) {
		grab(divName).className = '';
	}
}

function noError_2gr(divName, sel1Name, sel2Name) {
	var div = grab(divName);
	var sel1 = Number(grab(sel1Name).selectedIndex);
	var sel2 = Number(grab(sel2Name).selectedIndex);

	if (sel1 > 0 && sel2 > 0) {
		div.className = '';
	}
}


function fetchAM1FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};
	var d6 = {};
	var d7 = {};
	var d8 = {};
	var d9 = {};
	var d10 = {};
	var d11 = {};
	var d12 = {};
	var d13 = {};
	var d14 = {};
	var d15 = {};
	var d16 = {};
	var d17 = {};

	d1['field'] = 'maritalStatus';
	d1['type'] = 'select';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'livingSituation';
	d2['type'] = 'select';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'months_res';
	d3['type'] = 'number';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'years_res';
	d4['type'] = 'number';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);
	d5['field'] = 'whoLivesWithClient';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);
	d6['field'] = 'num_children';
	d6['type'] = 'number';
	d6['div'] = 'e6';
	d6['isDynamic'] = false;
	d6['trigger'] = null;
	result.push(d6);
	d7['field'] = 'spouse_dep';
	d7['type'] = 'number';
	d7['div'] = 'e7';
	d7['isDynamic'] = false;
	d7['trigger'] = null;
	result.push(d7);
	d8['field'] = 'other_dependants';
	d8['type'] = 'number';
	d8['div'] = 'e8';
	d8['isDynamic'] = false;
	d8['trigger'] = null;
	result.push(d8);
	d9['field'] = 'resasonDO';
	d9['type'] = 'text';
	d9['div'] = 'e9';
	d9['isDynamic'] = true;
	d9['trigger'] = 'DO';
	result.push(d9);
	d10['field'] = 'employee';
	d10['type'] = 'text';
	d10['div'] = 'e10';
	d10['isDynamic'] = false;
	d10['trigger'] = null;
	result.push(d10);
	d11['field'] = 'job_title';
	d11['type'] = 'text';
	d11['div'] = 'e11';
	d11['isDynamic'] = false;
	d11['trigger'] = null;
	result.push(d11);
	d12['field'] = 'emp_address';
	d12['type'] = 'text';
	d12['div'] = 'e12';
	d12['isDynamic'] = false;
	d12['trigger'] = null;
	result.push(d12);
	d13['field'] = 'employed_months';
	d13['type'] = 'number';
	d13['div'] = 'e13';
	d13['isDynamic'] = false;
	d13['trigger'] = null;
	result.push(d13);
	d14['field'] = 'employed_years';
	d14['type'] = 'number';
	d14['div'] = 'e14';
	d14['isDynamic'] = false;
	d14['trigger'] = null;
	result.push(d14);
	d15['field'] = 'employer_phone';
	d15['type'] = 'phone';
	d15['div'] = 'e15';
	d15['isDynamic'] = false;
	d15['trigger'] = null;
	result.push(d15);
	d16['field'] = 'whatMedicine';
	d16['type'] = 'text';
	d16['div'] = 'e16';
	d16['isDynamic'] = true;
	d16['trigger'] = 'on_meds';
	result.push(d16);
	d17['field'] = 'health_exp';
	d17['type'] = 'text';
	d17['div'] = 'e17';
	d17['isDynamic'] = true;
	d17['trigger'] = 'not_healthy';
	result.push(d17);

	return result;
}

function fetchAM2FieldNames() {
	var result = [];
	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};
	var d6 = {};
	var d7 = {};
	var d8 = {};
	var d9 = {};
	var d10 = {};
	var d11 = {};
	var d12 = {};
	var d13 = {};

	d1['field'] = 'firstDrinkAge';
	d1['type'] = 'number';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'firstDrinkType';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'amtPerWeek';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'yesDrink';
	result.push(d3);
	d4['field'] = 'useAmt';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = true;
	d4['trigger'] = 'yesDrink';
	result.push(d4);
	d5['field'] = 'yearsQuit';
	d5['type'] = 'number';
	d5['div'] = 'e5';
	d5['isDynamic'] = true;
	d5['trigger'] = 'hasDrank';
	result.push(d5);
	d6['field'] = 'monthsQuit';
	d6['type'] = 'number';
	d6['div'] = 'e6';
	d6['isDynamic'] = true;
	d6['trigger'] = 'hasDrank';
	result.push(d6);
	d7['field'] = 'reasonQuit';
	d7['type'] = 'text';
	d7['div'] = 'e7';
	d7['isDynamic'] = true;
	d7['trigger'] = 'hasDrank';;
	result.push(d7);
	d8['field'] = 'numDUI';
	d8['type'] = 'number';
	d8['div'] = 'e8';
	d8['isDynamic'] = true;
	d8['trigger'] = 'hasDUI';
	result.push(d8);
	d9['field'] = 'BALevel';
	d9['type'] = 'text';
	d9['div'] = 'e9';
	d9['isDynamic'] = true;
	d9['trigger'] = 'hasDUI';
	result.push(d9);
	d10['field'] = 'dateTreated';
	d10['type'] = 'text';
	d10['div'] = 'e10';
	d10['isDynamic'] = true;
	d10['trigger'] = 'hadTreatment';
	result.push(d10);
	d11['field'] = 'treatmentPlace';
	d11['type'] = 'text';
	d11['div'] = 'e11';
	d11['isDynamic'] = true;
	d11['trigger'] = 'hadTreatment';
	result.push(d11);
	d12['field'] = 'reasonNotFinishedTreatment';
	d12['type'] = 'text';
	d12['div'] = 'e12';
	d12['isDynamic'] = true;
	d12['trigger'] = 'noFinish';
	result.push(d12);
	d13['field'] = 'relapseTrigger';
	d13['type'] = 'text';
	d13['div'] = 'e13';
	d13['isDynamic'] = true;
	d13['trigger'] = 'notClean';
	result.push(d13);
	return result;
}

function fetchAM3FieldNames() {
	var result = [];
	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};
	var d6 = {};
	var d7 = {};
	var d8 = {};
	var d9 = {};

	d1['field'] = 'raisedBy';
	d1['type'] = 'select';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'traumaExplain';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'yesTrauma';
	result.push(d2);
	d3['field'] = 'howLeftHome';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'num_siblings';
	d4['type'] = 'number';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);
	d5['field'] = 'siblingsRelationshipExplain';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);
	d6['field'] = 'dadCloseExplain';
	d6['type'] = 'text';
	d6['div'] = 'e6';
	d6['isDynamic'] = false;
	d6['trigger'] = null;
	result.push(d6);
	d7['field'] = 'momCloseExplain';
	d7['type'] = 'text';
	d7['div'] = 'e7';
	d7['isDynamic'] = false;
	d7['trigger'] = null;;
	result.push(d7);
	d8['field'] = 'abusedBy';
	d8['type'] = 'text';
	d8['div'] = 'e8';
	d8['isDynamic'] = true;
	d8['trigger'] = 'yesAbuse';
	result.push(d8);
	d9['field'] = 'abuseImpact';
	d9['type'] = 'text';
	d9['div'] = 'e9';
	d9['isDynamic'] = true;
	d9['trigger'] = 'yesAbuse';
	result.push(d9);
	return result;
}

function fetchAM4FieldNames() {
	var result = [];
	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};
	var d6 = {};
	var d7 = {};
	var d8 = {};
	var d9 = {};
	var d10 = {};
	var d11 = {};

	d1['field'] = 'recentIncidentV';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'recentVDate';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'recentVlocation';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'withWhomRecentV';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);
	d5['field'] = 'happenedRecentV';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);
	d6['field'] = 'otherExplainRecentV';
	d6['type'] = 'text';
	d6['div'] = 'e6';
	d6['isDynamic'] = true;
	d6['trigger'] = 'otherRecentV';
	result.push(d6);
	d7['field'] = 'typeWordsRecentV';
	d7['type'] = 'text';
	d7['div'] = 'e7';
	d7['isDynamic'] = false;
	d7['trigger'] = null;;
	result.push(d7);
	d8['field'] = 'psychoWhyRecentV';
	d8['type'] = 'text';
	d8['div'] = 'e8';
	d8['isDynamic'] = true;
	d8['trigger'] = 'yesTreated';
	result.push(d8);
	d9['field'] = 'longAgoTreatRecentVyrs';
	d9['type'] = 'number';
	d9['div'] = 'e9';
	d9['isDynamic'] = true;
	d9['trigger'] = 'yesTreated';
	result.push(d9);
	d10['field'] = 'longAgoTreatRecentVmos';
	d10['type'] = 'number';
	d10['div'] = 'e10';
	d10['isDynamic'] = true;
	d10['trigger'] = 'yesTreated';
	result.push(d10);
	d11['field'] = 'reasonNotCompleteRecentV';
	d11['type'] = 'text';
	d11['div'] = 'e11';
	d11['isDynamic'] = true;
	d11['trigger'] = 'yesComplete';
	result.push(d11);
	return result;
}

function fetchAM5FieldNames() {
	var result = [];
	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};
	var d6 = {};
	var d7 = {};

	d1['field'] = 'depress30ExplainRecentV';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'yesDepress';
	result.push(d1);
	d2['field'] = 'anxietyExplainRecentV';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'yesAnx';
	result.push(d2);
	d3['field'] = 'hallucinationLastV';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'yesHall';
	result.push(d3);
	d4['field'] = 'understandingExplainRecentV';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = true;
	d4['trigger'] = 'yesTrouble';
	result.push(d4);
	d5['field'] = 'lastTimeTroubleControl';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = true;
	d5['trigger'] = 'yesControl';
	result.push(d5);
	d6['field'] = 'controlTrigger';
	d6['type'] = 'text';
	d6['div'] = 'e6';
	d6['isDynamic'] = true;
	d6['trigger'] = 'yesControl';
	result.push(d6);
	d7['field'] = 'suicide30ExplainRecentV';
	d7['type'] = 'text';
	d7['div'] = 'e7';
	d7['isDynamic'] = true;
	d7['trigger'] = 'yesSuicide';;
	result.push(d7);
	return result;
}

function fetchAM6FieldNames() {
	var result = [];
	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};

	d1['field'] = 'homicidalExplain';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'yesHomicide';
	result.push(d1);
	d2['field'] = 'medRecentVExplain';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'yesMed';
	result.push(d2);
	d3['field'] = 'medSuccessExplainRecentV';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'yesSuccess';
	result.push(d3);
	d4['field'] = 'durationRecentV';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);
	return result;
}

function fetchAM7FieldNames() {
	var result = [];
	var d1 = {};
	d1['field'] = 'connectionExplain';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'otherConnectionsUsing';
	result.push(d1);
	return result;
}

function fetchAM8FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};
	var d6 = {};
	var d7 = {};

	d1['field'] = 'whoWorst';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'happenedWorst';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'wordThoughtWorst';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'howStartWorst';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);
	d5['field'] = 'howEndWorst';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);
	d6['field'] = 'whoUsed';
	d6['type'] = 'select';
	d6['div'] = 'e6';
	d6['isDynamic'] = true;
	d6['trigger'] = 'yesDrugs';
	result.push(d6);
	d7['field'] = 'otherWorstDescription';
	d7['type'] = 'text';
	d7['div'] = 'e7';
	d7['isDynamic'] = true;
	d7['trigger'] = 'otherWorst';
	result.push(d7);
	return result;
}

function fetchAM9FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};

	d1['field'] = 'otherWhom';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'angryOther';
	result.push(d1);
	d2['field'] = 'angryAbout';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	return result;
}

function fetchAM10FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};

	d1['field'] = 'kidDadAnger';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'kidMomAnger';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'kidSiblingAnger';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'kidOtherAnger';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);
	d5['field'] = 'learnFamilyAnger';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);
	return result;
}

function fetchAM11FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};

	d1['field'] = 'otherWhom';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'otherSeriousIllness';
	result.push(d1);
	d2['field'] = 'describeIssue';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'whichMeds';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'onMeds';
	result.push(d3);
	return result;
}

function fetchAM12FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};
	var d5 = {};

	d1['field'] = 'whatSayYou';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'talkToMyself';
	result.push(d1);
	d2['field'] = 'howLongLeaveScene';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'leaveScene';
	result.push(d2);
	d3['field'] = 'whatDoLeave';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'leaveScene';
	result.push(d3);
	d4['field'] = 'howRelax';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = true;
	d4['trigger'] = 'relax';
	result.push(d4);
	d5['field'] = 'doWhatOtherControl';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = true;
	d5['trigger'] = 'otherControlAnger';
	result.push(d5);

	return result;
}

function fetchAM13FieldNames() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};

	d1['field'] = 'anythingelse';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'changeLearn1';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'changeLearn2';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'changeLearn3';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);

	return result;
}

function fetchSpecial1_am() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};

	d1['field'] = 'childAngerExplain';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'yesAnger';
	result.push(d1);
	d2['field'] = 'otherChildExplain';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'yesOther';
	result.push(d2);
	d3['field'] = 'parentViolenceExplain';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'yesViolence';
	result.push(d3);
	d4['field'] = 'parentViolenceImpact';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = true;
	d4['trigger'] = 'yesViolence';
	result.push(d4);

	return result;
}

function fetchSpecial2_am() {
	var result = [];

	var d1 = {};
	var d2 = {};

	d1['field'] = 'suicideTodayExplainRecentV';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'yesPlan';
	result.push(d1);
	d2['field'] = 'hasAttemptedExplainRecentV';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'yesAttempt';
	result.push(d2);

	return result;
}

function fetchFieldList_am(section) {
	var result = null;
	section = String(section);

	if (section === '/am_demographic/') {
		result = fetchAM1FieldNames();
	}
	else if (section === '/am_drugHistory/') {
		result = fetchAM2FieldNames();
	}
	else if (section === '/am_childhood/') {
		result = fetchAM3FieldNames();
	}
	else if (section === '/am_angerHistory/') {
		result = fetchAM4FieldNames();
	}
	else if (section === '/am_angerHistory2/') {
		result = fetchAM5FieldNames();
	}
	else if (section === '/am_angerHistory3/') {
		result = fetchAM6FieldNames();
	}
	else if (section === '/am_connections/') {
		result = fetchAM7FieldNames();
	}
	else if (section === '/am_worst/') {
		result = fetchAM8FieldNames();
	}
	else if (section === '/am_angerTarget/') {
		result = fetchAM9FieldNames();
	}
	else if (section === '/am_familyOrigin/') {
		result = fetchAM10FieldNames();
	}
	else if (section === '/am_problems/') {
		result = fetchAM11FieldNames();
	}
	else if (section === '/am_control/') {
		result = fetchAM12FieldNames();
	}
	else if (section === '/am_final/') {
		result = fetchAM13FieldNames();
	}
	return result;
}

function fetchMhDemoFieldNames() {
	var result = [];
	var d1={}, d2={}, d3={}, d4={}, d5={}, d6={}, d7={}, d8={}, d9={}, d10={}, d11={}, d12={}, d13={}, d14={}, d15={};

	d1['field'] = 'birthplace';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	d2['field'] = 'raised';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);

	d3['field'] = 'occupation';
	d3['type'] = 'text';
	d3['div'] = 'e5';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);

	d4['field'] = 'employer';
	d4['type'] = 'text';
	d4['div'] = 'e6';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);

	d5['field'] = 'employedMo';
	d5['type'] = 'number';
	d5['div'] = 'e8';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);

	d6['field'] = 'employedYrs';
	d6['type'] = 'number';
	d6['div'] = 'e7';
	d6['isDynamic'] = false;
	d6['trigger'] = null;
	result.push(d6);

	d7['field'] = 'pastJobs';
	d7['type'] = 'text';
	d7['div'] = 'e9';
	d7['isDynamic'] = false;
	d7['trigger'] = null;
	result.push(d7);

	d8['field'] = 'motherAge';
	d8['type'] = 'number';
	d8['div'] = 'e19';
	d8['isDynamic'] = false;
	d8['trigger'] = null;
	result.push(d8);

	d9['field'] = 'motherOccupation';
	d9['type'] = 'text';
	d9['div'] = 'e20';
	d9['isDynamic'] = false;
	d9['trigger'] = null;
	result.push(d9);

	d10['field'] = 'motherCity';
	d10['type'] = 'text';
	d10['div'] = 'e21';
	d10['isDynamic'] = false;
	d10['trigger'] = null;
	result.push(d10);

	d11['field'] = 'motherState';
	d11['type'] = 'select';
	d11['div'] = 'e100';
	d11['isDynamic'] = false;
	d11['trigger'] = null;
	result.push(d11);

	d12['field'] = 'fatherAge';
	d12['type'] = 'number';
	d12['div'] = 'e22';
	d12['isDynamic'] = false;
	d12['trigger'] = null;
	result.push(d12);

	d13['field'] = 'fatherOccupation';
	d13['type'] = 'text';
	d13['div'] = 'e23';
	d13['isDynamic'] = false;
	d13['trigger'] = null;
	result.push(d13);

	d14['field'] = 'fatherCity';
	d14['type'] = 'text';
	d14['div'] = 'e24';
	d14['isDynamic'] = false;
	d14['trigger'] = null;
	result.push(d14)

	d15['field'] = 'fatherState';
	d15['type'] = 'select';
	d15['div'] = 'e101';
	d15['isDynamic'] = false;
	d15['trigger'] = null;
	result.push(d15);

	return result;
}

function fetchMhOpsFieldNames() {
	var result = [];
	var numKids = Number(grab('numKids').value);
	var numSisters = Number(grab('numSisters').value);
	var numBrothers = Number(grab('numBrothers').value);
	var totalFields = numKids + numSisters + numBrothers;

	for (var i = 1; i <= totalFields; i++) {
		dataAge = {};
		dataAge['field'] = 'age_' + String(i);
		dataAge['type'] = 'number';
		dataAge['div'] = 'e' + String(i);
		dataAge['isDynamic'] = false;
		dataAge['trigger'] = null;
		result.push(dataAge);

		dataCity = {};
		dataCity['field'] = 'city_' + String(i);
		dataCity['type'] = 'text';
		dataCity['div'] = 'e' + String(i);
		dataCity['isDynamic'] = false;
		dataCity['trigger'] = null;
		result.push(dataCity);

		dataState = {};
		dataState['field'] = 'state_' + String(i);
		dataState['type'] = 'select';
		dataState['div'] = 'e' + String(i);
		dataState['isDynamic'] = false;
		dataState['trigger'] = null;
		result.push(dataState);
	}

	return result;
}

function getDynamoErrorFields_mh() {
	var result = [];

	if (grab('married').checked === true || grab('seperated').checked === true) {
		var d1 = {}, d2 = {}, d3 = {}, d4 = {}, d5 = {}, d6 = {};
		d1['field'] = 'numMarriages';
		d1['type'] = 'number';
		d1['div'] = 'e4';
		d1['isDynamic'] = false;
		d1['trigger'] = null;
		result.push(d1);

		d2['field'] = 'spouseAge';
		d2['type'] = 'number';
		d2['div'] = 'e11';
		d2['isDynamic'] = false;
		d2['trigger'] = null;
		result.push(d2);

		d3['field'] = 'spouseOccupation';
		d3['type'] = 'text';
		d3['div'] = 'e12';
		d3['isDynamic'] = false;
		d3['trigger'] = null;
		result.push(d3);

		d4['field'] = 'spouseEmployer';
		d4['type'] = 'text';
		d4['div'] = 'e13';
		d4['isDynamic'] = false;
		d4['trigger'] = null;
		result.push(d4);

		d5['field'] = 'spouseWorkYrs';
		d5['type'] = 'number';
		d5['div'] = 'e14';
		d5['isDynamic'] = false;
		d5['trigger'] = null;
		result.push(d5);

		d6['field'] = 'spouseWorkMos';
		d6['type'] = 'number';
		d6['div'] = 'e15';
		d6['isDynamic'] = false;
		d6['trigger'] = null;
		result.push(d6);

	}
	else if (grab('divorced').checked === true || grab('widowed').checked === true) {
		var d_num = {};
		d_num['field'] = 'numMarriages';
		d_num['type'] = 'number';
		d_num['div'] = 'e4';
		d_num['isDynamic'] = false;
		d_num['trigger'] = null;
		result.push(d_num);
	}

	return result;
}

function mh_dynamo_has_errors() {
	var fields = getDynamoErrorFields_mh();
	return specialHasErrorCheck_m(fields, true);
}

function superDynamoChecker() {
	var fields = getDynamoErrorFields_mh();
	SpecialSuperErrorChecker(fields, true);
}

function fetchMhEDUFieldNames() {
	var result = [];

	var d1={}, d2={}, d3={}, d4={}, d5={}, d6={}, d7={}, d8={}, d9={}, d10={}, d11={};
	var d12={}, d13={}, d14={}, d15={}, d16={};

	var college_val = String(grab('m_college_trigger').value);
	var college_trigger = false;

	if (college_val === 'true') {
		college_trigger = true;
	}

	d1['field'] = 'FriendshipsKto6';
	d1['type'] = 'number';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	d2['field'] = 'Friendships7to9';
	d2['type'] = 'number';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);

	d3['field'] = 'Friendships10to12';
	d3['type'] = 'number';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);

	d4['field'] = 'collegeDegree';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = true;
	d4['trigger'] = 'college1';
	result.push(d4);

	d5['field'] = 'collegeMajor';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = true;
	d5['trigger'] = 'college1';
	result.push(d5);

	d6['field'] = 'collegeDegree';
	d6['type'] = 'text';
	d6['div'] = 'e4';
	d6['isDynamic'] = true;
	d6['trigger'] = 'college2';
	result.push(d6);

	d7['field'] = 'collegeMajor';
	d7['type'] = 'text';
	d7['div'] = 'e5';
	d7['isDynamic'] = true;
	d7['trigger'] = 'college2';
	result.push(d7);

	d8['field'] = 'collegeDegree';
	d8['type'] = 'text';
	d8['div'] = 'e4';
	d8['isDynamic'] = true;
	d8['trigger'] = 'college3';
	result.push(d8);

	d9['field'] = 'collegeMajor';
	d9['type'] = 'text';
	d9['div'] = 'e5';
	d9['isDynamic'] = true;
	d9['trigger'] = 'college3';
	result.push(d9);

	d10['field'] = 'collegeDegree';
	d10['type'] = 'text';
	d10['div'] = 'e4';
	d10['isDynamic'] = true;
	d10['trigger'] = 'college4';
	result.push(d10);

	d11['field'] = 'collegeMajor';
	d11['type'] = 'text';
	d11['div'] = 'e5';
	d11['isDynamic'] = true;
	d11['trigger'] = 'college4';
	result.push(d11);

	d12['field'] = 'tradeSchool';
	d12['type'] = 'text';
	d12['div'] = 'e20';
	d12['isDynamic'] = true;
	d12['trigger'] = 'yesTrade';
	result.push(d12);

	d13['field'] = 'tradeAreaStudy';
	d13['type'] = 'text';
	d13['div'] = 'e6';
	d13['isDynamic'] = true;
	d13['trigger'] = 'yesTrade';
	result.push(d13);

	d14['field'] = 'militaryBranch';
	d14['type'] = 'text';
	d14['div'] = 'e7';
	d14['isDynamic'] = true;
	d14['trigger'] = 'yesMillitary';
	result.push(d14);

	d15['field'] = 'militaryYears';
	d15['type'] = 'number';
	d15['div'] = 'e8';
	d15['isDynamic'] = true;
	d15['trigger'] = 'yesMillitary';
	result.push(d15);

	d16['field'] = 'militaryRank';
	d16['type'] = 'text';
	d16['div'] = 'e9';
	d16['isDynamic'] = true;
	d16['trigger'] = 'yesMillitary';
	result.push(d16);

	return result;
}

function fetchMhMoneyFieldNames() {
	var result = [];

	var d1={}, d2={}, d3={}, d4={}, d5={}, d6={}, d7={}, d8={}, d9={}, d10={}, d11={};
	var d12={}, d13={}, d14={}, d15={}, d16={}, d17={};

	d1['field'] = 'residence';
	d1['type'] = 'select';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	d2['field'] = 'income';
	d2['type'] = 'select';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);

	d3['field'] = 'debt';
	d3['type'] = 'select';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);

	d4['field'] = 'credit';
	d4['type'] = 'select';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);

	d5['field'] = 'healthCare';
	d5['type'] = 'select';
	d5['div'] = 'e5';
	d5['isDynamic'] = false;
	d5['trigger'] = null;
	result.push(d5);

	d6['field'] = 'otherIncome';
	d6['type'] = 'select';
	d6['div'] = 'e6';
	d6['isDynamic'] = false;
	d6['trigger'] = null;
	result.push(d6);

	d7['field'] = 'churchWeek';
	d7['type'] = 'number';
	d7['div'] = 'e7';
	d7['isDynamic'] = false;
	d7['trigger'] = null;
	result.push(d7);

	d8['field'] = 'churchMonth';
	d8['type'] = 'number';
	d8['div'] = 'e8';
	d8['isDynamic'] = false;
	d8['trigger'] = null;
	result.push(d8);

	d9['field'] = 'churchYear';
	d9['type'] = 'number';
	d9['div'] = 'e9';
	d9['isDynamic'] = false;
	d9['trigger'] = null;
	result.push(d9);

	d10['field'] = 'closeFriendNumber';
	d10['type'] = 'number';
	d10['div'] = 'e10';
	d10['isDynamic'] = false;
	d10['trigger'] = null;
	result.push(d10);

	d11['field'] = 'acqNumber';
	d11['type'] = 'number';
	d11['div'] = 'e11';
	d11['isDynamic'] = false;
	d11['trigger'] = null;
	result.push(d11);

	d12['field'] = 'interestWeek';
	d12['type'] = 'number';
	d12['div'] = 'e12';
	d12['isDynamic'] = false;
	d12['trigger'] = null;
	result.push(d12);

	d13['field'] = 'interestMonth';
	d13['type'] = 'number';
	d13['div'] = 'e13';
	d13['isDynamic'] = false;
	d13['trigger'] = null;
	result.push(d13);

	d14['field'] = 'friendActWeek';
	d14['type'] = 'number';
	d14['div'] = 'e14';
	d14['isDynamic'] = false;
	d14['trigger'] = null;
	result.push(d14);

	d15['field'] = 'friendActMonth';
	d15['type'] = 'number';
	d15['div'] = 'e15';
	d15['isDynamic'] = false;
	d15['trigger'] = null;
	result.push(d15);

	d16['field'] = 'workActWeek';
	d16['type'] = 'number';
	d16['div'] = 'e16';
	d16['isDynamic'] = false;
	d16['trigger'] = null;
	result.push(d16);

	d17['field'] = 'workActMonth';
	d17['type'] = 'number';
	d17['div'] = 'e17';
	d17['isDynamic'] = false;
	d17['trigger'] = null;
	result.push(d17);

	return result;
}

function fetchMhStressFieldNames() {
	var result = [];

	var d1={}, d2={}, d3={}, d4={}, d5={}, d6={}, d7={}, d8={}, d9={}, d10={};

	d1['field'] = 'deathStressExp';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = true;
	d1['trigger'] = 'yesDeath';
	result.push(d1);

	d2['field'] = 'divorceStressExp';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = true;
	d2['trigger'] = 'yesDivorce';
	result.push(d2);

	d3['field'] = 'moveStressExp';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = true;
	d3['trigger'] = 'yesMove';
	result.push(d3);

	d4['field'] = 'medicalStressExp';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = true;
	d4['trigger'] = 'yesMedical';
	result.push(d4);

	d5['field'] = 'familyHealthStressExp';
	d5['type'] = 'text';
	d5['div'] = 'e5';
	d5['isDynamic'] = true;
	d5['trigger'] = 'yesFamily';
	result.push(d5);

	d6['field'] = 'financialStressExp';
	d6['type'] = 'text';
	d6['div'] = 'e6';
	d6['isDynamic'] = true;
	d6['trigger'] = 'yesMoney';
	result.push(d6);

	d7['field'] = 'abuseStressExp';
	d7['type'] = 'text';
	d7['div'] = 'e7';
	d7['isDynamic'] = true;
	d7['trigger'] = 'yesAbuse';
	result.push(d7);

	d8['field'] = 'addictionFamilyStressExp';
	d8['type'] = 'text';
	d8['div'] = 'e8';
	d8['isDynamic'] = true;
	d8['trigger'] = 'yesAddiction';
	result.push(d8);

	d9['field'] = 'violenceFamilyStressExp';
	d9['type'] = 'text';
	d9['div'] = 'e9';
	d9['isDynamic'] = true;
	d9['trigger'] = 'yesViolence';
	result.push(d9);

	d10['field'] = 'otherStressExp';
	d10['type'] = 'text';
	d10['div'] = 'e10';
	d10['isDynamic'] = true;
	d10['trigger'] = 'yesOther';
	result.push(d10);

	return result;
}

function fetchMhFamilyFieldNames() {
	var d = [];

	for (var i = 0; i < 52; i++) {
		var data = {};
		d.push(data);
	}

	d[0]['field'] = 'depressSide';
	d[0]['type'] = 'select';
	d[0]['div'] = 'e1';
	d[0]['isDynamic'] = true;
	d[0]['trigger'] = 'isdepressed';

	d[1]['field'] = 'depressMember';
	d[1]['type'] = 'select';
	d[1]['div'] = 'e1';
	d[1]['isDynamic'] = true;
	d[1]['trigger'] = 'isdepressed';

	d[2]['field'] = 'sideADD';
	d[2]['type'] = 'select';
	d[2]['div'] = 'e2';
	d[2]['isDynamic'] = true;
	d[2]['trigger'] = 'isadd';

	d[3]['field'] = 'memADD';
	d[3]['type'] = 'select';
	d[3]['div'] = 'e2';
	d[3]['isDynamic'] = true;
	d[3]['trigger'] = 'isadd';

	d[4]['field'] = 'sideBed';
	d[4]['type'] = 'select';
	d[4]['div'] = 'e3';
	d[4]['isDynamic'] = true;
	d[4]['trigger'] = 'isbedWetting';

	d[5]['field'] = 'memBed';
	d[5]['type'] = 'select';
	d[5]['div'] = 'e3';
	d[5]['isDynamic'] = true;
	d[5]['trigger'] = 'isbedWetting';

	d[6]['field'] = 'sideBi';
	d[6]['type'] = 'select';
	d[6]['div'] = 'e4';
	d[6]['isDynamic'] = true;
	d[6]['trigger'] = 'isbipolar';

	d[7]['field'] = 'memBi';
	d[7]['type'] = 'select';
	d[7]['div'] = 'e4';
	d[7]['isDynamic'] = true;
	d[7]['trigger'] = 'isbipolar';

	d[8]['field'] = 'sideATT';
	d[8]['type'] = 'select';
	d[8]['div'] = 'e5';
	d[8]['isDynamic'] = true;
	d[8]['trigger'] = 'issuicideAttempt';

	d[9]['field'] = 'memATT';
	d[9]['type'] = 'select';
	d[9]['div'] = 'e5';
	d[9]['isDynamic'] = true;
	d[9]['trigger'] = 'issuicideAttempt';

	d[10]['field'] = 'sidePA';
	d[10]['type'] = 'select';
	d[10]['div'] = 'e6';
	d[10]['isDynamic'] = true;
	d[10]['trigger'] = 'isphysicalAbuse';

	d[11]['field'] = 'memPA';
	d[11]['type'] = 'select';
	d[11]['div'] = 'e6';
	d[11]['isDynamic'] = true;
	d[11]['trigger'] = 'isphysicalAbuse';

	d[12]['field'] = 'sideLaw';
	d[12]['type'] = 'select';
	d[12]['div'] = 'e7';
	d[12]['isDynamic'] = true;
	d[12]['trigger'] = 'islaw';

	d[13]['field'] = 'memLaw';
	d[13]['type'] = 'select';
	d[13]['div'] = 'e7';
	d[13]['isDynamic'] = true;
	d[13]['trigger'] = 'islaw';

	d[14]['field'] = 'sideLD';
	d[14]['type'] = 'select';
	d[14]['div'] = 'e8';
	d[14]['isDynamic'] = true;
	d[14]['trigger'] = 'isld';

	d[15]['field'] = 'memLD';
	d[15]['type'] = 'select';
	d[15]['div'] = 'e8';
	d[15]['isDynamic'] = true;
	d[15]['trigger'] = 'isld';

	d[16]['field'] = 'sideTic';
	d[16]['type'] = 'select';
	d[16]['div'] = 'e9';
	d[16]['isDynamic'] = true;
	d[16]['trigger'] = 'istic';

	d[17]['field'] = 'memTic';
	d[17]['type'] = 'select';
	d[17]['div'] = 'e9';
	d[17]['isDynamic'] = true;
	d[17]['trigger'] = 'istic';

	d[18]['field'] = 'sideThy';
	d[18]['type'] = 'select';
	d[18]['div'] = 'e10';
	d[18]['isDynamic'] = true;
	d[18]['trigger'] = 'isthyroid';

	d[19]['field'] = 'memThy';
	d[19]['type'] = 'select';
	d[19]['div'] = 'e10';
	d[19]['isDynamic'] = true;
	d[19]['trigger'] = 'isthyroid';

	d[20]['field'] = 'sideHeart';
	d[20]['type'] = 'select';
	d[20]['div'] = 'e11';
	d[20]['isDynamic'] = true;
	d[20]['trigger'] = 'isheart';

	d[21]['field'] = 'memHeart';
	d[21]['type'] = 'select';
	d[21]['div'] = 'e11';
	d[21]['isDynamic'] = true;
	d[21]['trigger'] = 'isheart';

	d[22]['field'] = 'sideOW';
	d[22]['type'] = 'select';
	d[22]['div'] = 'e12';
	d[22]['isDynamic'] = true;
	d[22]['trigger'] = 'isoverweight';

	d[23]['field'] = 'memOW';
	d[23]['type'] = 'select';
	d[23]['div'] = 'e12';
	d[23]['isDynamic'] = true;
	d[23]['trigger'] = 'isoverweight';

	d[24]['field'] = 'sideMood';
	d[24]['type'] = 'select';
	d[24]['div'] = 'e13';
	d[24]['isDynamic'] = true;
	d[24]['trigger'] = 'ismood';

	d[25]['field'] = 'memMood';
	d[25]['type'] = 'select';
	d[25]['div'] = 'e13';
	d[25]['isDynamic'] = true;
	d[25]['trigger'] = 'ismood';

	d[26]['field'] = 'sideAlc';
	d[26]['type'] = 'select';
	d[26]['div'] = 'e14';
	d[26]['isDynamic'] = true;
	d[26]['trigger'] = 'isalcohol';

	d[27]['field'] = 'memAlc';
	d[27]['type'] = 'select';
	d[27]['div'] = 'e14';
	d[27]['isDynamic'] = true;
	d[27]['trigger'] = 'isalcohol';

	d[28]['field'] = 'sideDrug';
	d[28]['type'] = 'select';
	d[28]['div'] = 'e15';
	d[28]['isDynamic'] = true;
	d[28]['trigger'] = 'isdrugs';

	d[29]['field'] = 'memDrug';
	d[29]['type'] = 'select';
	d[29]['div'] = 'e15';
	d[29]['isDynamic'] = true;
	d[29]['trigger'] = 'isdrugs';

	d[30]['field'] = 'sideSch';
	d[30]['type'] = 'select';
	d[30]['div'] = 'e16';
	d[30]['isDynamic'] = true;
	d[30]['trigger'] = 'isschizo';

	d[31]['field'] = 'memSch';
	d[31]['type'] = 'select';
	d[31]['div'] = 'e16';
	d[31]['isDynamic'] = true;
	d[31]['trigger'] = 'isschizo';

	d[32]['field'] = 'sideSe';
	d[32]['type'] = 'select';
	d[32]['div'] = 'e17';
	d[32]['isDynamic'] = true;
	d[32]['trigger'] = 'isseizures';

	d[33]['field'] = 'memSe';
	d[33]['type'] = 'select';
	d[33]['div'] = 'e17';
	d[33]['isDynamic'] = true;
	d[33]['trigger'] = 'isseizures';

	d[34]['field'] = 'sideCS';
	d[34]['type'] = 'select';
	d[34]['div'] = 'e18';
	d[34]['isDynamic'] = true;
	d[34]['trigger'] = 'iscompletedSuicide';

	d[35]['field'] = 'memCS';
	d[35]['type'] = 'select';
	d[35]['div'] = 'e18';
	d[35]['isDynamic'] = true;
	d[35]['trigger'] = 'iscompletedSuicide';

	d[36]['field'] = 'sideSex';
	d[36]['type'] = 'select';
	d[36]['div'] = 'e19';
	d[36]['isDynamic'] = true;
	d[36]['trigger'] = 'issexAbuse';

	d[37]['field'] = 'memSex';
	d[37]['type'] = 'select';
	d[37]['div'] = 'e19';
	d[37]['isDynamic'] = true;
	d[37]['trigger'] = 'issexAbuse';

	d[38]['field'] = 'sidePanick';
	d[38]['type'] = 'select';
	d[38]['div'] = 'e20';
	d[38]['isDynamic'] = true;
	d[38]['trigger'] = 'ispanic';

	d[39]['field'] = 'memPanick';
	d[39]['type'] = 'select';
	d[39]['div'] = 'e20';
	d[39]['isDynamic'] = true;
	d[39]['trigger'] = 'ispanic';

	d[40]['field'] = 'sideAnx';
	d[40]['type'] = 'select';
	d[40]['div'] = 'e21';
	d[40]['isDynamic'] = true;
	d[40]['trigger'] = 'isanxiety';

	d[41]['field'] = 'memAnx';
	d[41]['type'] = 'select';
	d[41]['div'] = 'e21';
	d[41]['isDynamic'] = true;
	d[41]['trigger'] = 'isanxiety';

	d[42]['field'] = 'sideOCD';
	d[42]['type'] = 'select';
	d[42]['div'] = 'e22';
	d[42]['isDynamic'] = true;
	d[42]['trigger'] = 'isOCD';

	d[43]['field'] = 'memOCD';
	d[43]['type'] = 'select';
	d[43]['div'] = 'e22';
	d[43]['isDynamic'] = true;
	d[43]['trigger'] = 'isOCD';

	d[44]['field'] = 'sideSugar';
	d[44]['type'] = 'select';
	d[44]['div'] = 'e23';
	d[44]['isDynamic'] = true;
	d[44]['trigger'] = 'isdiabetes';

	d[45]['field'] = 'memSugar';
	d[45]['type'] = 'select';
	d[45]['div'] = 'e23';
	d[45]['isDynamic'] = true;
	d[45]['trigger'] = 'isdiabetes';

	d[46]['field'] = 'sideCancer';
	d[46]['type'] = 'select';
	d[46]['div'] = 'e24';
	d[46]['isDynamic'] = true;
	d[46]['trigger'] = 'iscancer';

	d[47]['field'] = 'memCancer';
	d[47]['type'] = 'select';
	d[47]['div'] = 'e24';
	d[47]['isDynamic'] = true;
	d[47]['trigger'] = 'iscancer';

	d[48]['field'] = 'sideBlood';
	d[48]['type'] = 'select';
	d[48]['div'] = 'e25';
	d[48]['isDynamic'] = true;
	d[48]['trigger'] = 'ishighBloodPressure';

	d[49]['field'] = 'memBlood';
	d[49]['type'] = 'select';
	d[49]['div'] = 'e25';
	d[49]['isDynamic'] = true;
	d[49]['trigger'] = 'ishighBloodPressure';

	d[50]['field'] = 'sideAngry';
	d[50]['type'] = 'select';
	d[50]['div'] = 'e26';
	d[50]['isDynamic'] = true;
	d[50]['trigger'] = 'isanger';

	d[51]['field'] = 'memAngry';
	d[51]['type'] = 'select';
	d[51]['div'] = 'e26';
	d[51]['isDynamic'] = true;
	d[51]['trigger'] = 'isanger';

	return d;
}

function fetchMhLegalFieldNames() {
	var result = [];
	var d1={}, d2={}, d3={}, d4={}, d5={}, d6={}, d7={}, d8={}, d9={}, d10={}, d11={}, d12={};

	d1['field'] = 'num_arrest';
	d1['type'] = 'number';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	d2['field'] = 'num_convictions';
	d2['type'] = 'number';
	d2['div'] = 'e3';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);

	d3['field'] = 'num_DUI_charges';
	d3['type'] = 'number';
	d3['div'] = 'e5';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);

	d4['field'] = 'num_DUI_convictions';
	d4['type'] = 'number';
	d4['div'] = 'e6';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);

	d5['field'] = 'probationOfficer';
	d5['type'] = 'text';
	d5['div'] = 'e30';
	d5['isDynamic'] = true;
	d5['trigger'] = 'haveBeen';
	result.push(d5);

	d6['field'] = 'probationOffense';
	d6['type'] = 'text';
	d6['div'] = 'e31';
	d6['isDynamic'] = true;
	d6['trigger'] = 'haveBeen';
	result.push(d6);

	d7['field'] = 'num_suspended';
	d7['type'] = 'number';
	d7['div'] = 'e32';
	d7['isDynamic'] = true;
	d7['trigger'] = 'yesSuspended';
	result.push(d7);

	d8['field'] = 'dateBenkrupcy';
	d8['type'] = 'text';
	d8['div'] = 'e33';
	d8['isDynamic'] = true;
	d8['trigger'] = 'yesBank';
	result.push(d8);

	d9['field'] = 'explainPositiveAnswers';
	d9['type'] = 'text';
	d9['div'] = 'e34';
	d9['isDynamic'] = true;
	d9['trigger'] = 'yesSuit';
	result.push(d9);

	d10['field'] = 'explainPositiveAnswers';
	d10['type'] = 'text';
	d10['div'] = 'e34';
	d10['isDynamic'] = true;
	d10['trigger'] = 'yesDivPro';
	result.push(d10);

	d11['field'] = 'explainPositiveAnswers';
	d11['type'] = 'text';
	d11['div'] = 'e34';
	d11['isDynamic'] = true;
	d11['trigger'] = 'yesChildDis';
	result.push(d11);

	d12['field'] = 'explainPositiveAnswers';
	d12['type'] = 'text';
	d12['div'] = 'e34';
	d12['isDynamic'] = true;
	d12['trigger'] = 'yesBank';
	result.push(d12);

	return result;
}

function fetchMhPsychFieldNames() {
	var result = [];
	var d1 = {}

	d1['field'] = 'psychiatricHistory';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	return result;
}

function fetchMhUseFieldNames() {
	var result = [];

	return result;
}


function fetchFieldList_mh(section) {
	var result = null;
	section = String(section);

	if (section === '/mh_demographic/') {
		result = fetchMhDemoFieldNames();
	}
	else if (section === '/mhDemoOpPage/') {
		result = fetchMhOpsFieldNames();
	}
	else if (section === '/mh_education/') {
		result = fetchMhEDUFieldNames();
	}
	else if (section === '/mh_background/') {
		result = fetchMhMoneyFieldNames();
	}
	else if (section === '/mh_stress/') {
		result = fetchMhStressFieldNames();
	}
	else if (section === '/mh_familyHistory/') {
		result = fetchMhFamilyFieldNames();
	}
	else if (section === '/mh_legal/') {
		result = fetchMhLegalFieldNames();
	}
	else if (section === '/mh_psych/') {
		result = fetchMhPsychFieldNames();
	}
	else if (section === '/mh_useTable/') {
		result = fetchMhUseFieldNames();
	}

	return result;
}

function fetchFieldList_asi(section) {
	
}

function fetch_demoFields_sap() {
	var result = [];

	var d1 = {};
	var d2 = {};

	d1['field'] = 'problem';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'health';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);

	return result;
}

function fetch_socialFields_sap() {
	var result = [];
	var d1 = {};

	d1['field'] = 'family';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	return result;
}

function fetch_psych1Fields_sap() {
	var result = [];
	var names = [];
	var group = 1;
	names.push('alcohol');
	names.push('amph');
	names.push('caffine');
	names.push('weed');
	names.push('coke');
	names.push('hall');
	names.push('inhale');
	names.push('smoke');
	names.push('op');
	names.push('pcp');
	names.push('sed');
	names.push('other');

	var t = '';

	for (var i = 0; i < names.length; i++) {
		var d1 = {};
		var d2 = {};
		var d3 = {};
		var d4 = {};
		var d5 = {};

		var theDiv = 'e' + String(group);

		d1['field'] = String(names[i]) + 'Age';
		d2['field'] = String(names[i]) + 'Frequency';
		d3['field'] = String(names[i]) + 'Quantity';
		d4['field'] = String(names[i]) + 'Last';
		d5['field'] = String(names[i]) + 'How';

		d1['sub'] = 'Age';
		d2['sub'] = 'Frequency';
		d3['sub'] = 'Quantity';
		d4['sub'] = 'Last';
		d5['sub'] = 'How';

		d1['group'] = String(group);
		d2['group'] = String(group);
		d3['group'] = String(group);
		d4['group'] = String(group);
		d5['group'] = String(group);

		d1['type'] = 'text';
		d2['type'] = 'text';
		d3['type'] = 'text';
		d4['type'] = 'text';
		d5['type'] = 'text';

		d1['isDynamic'] = false;
		d2['isDynamic'] = false;
		d3['isDynamic'] = false;
		d4['isDynamic'] = false;
		d5['isDynamic'] = false;

		d1['div'] = theDiv;
		d2['div'] = theDiv;
		d3['div'] = theDiv;
		d4['div'] = theDiv;
		d5['div'] = theDiv;

		d1['trigger'] = null;
		d2['trigger'] = null;
		d3['trigger'] = null;
		d4['trigger'] = null;
		d5['trigger'] = null;

		result.push(d1);
		result.push(d2);
		result.push(d3);
		result.push(d4);
		result.push(d5);

		group += 1;
	}

	return result;
}

function fetch_psych2Fields_sap() {
	var result = [];
	var d1 = {};

	d1['field'] = 'psychoactive';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);

	return result;
}

function fetch_additionalFields_sap() {
	var result = [];

	var d1 = {};
	var d2 = {};
	var d3 = {};
	var d4 = {};

	d1['field'] = 'psychological';
	d1['type'] = 'text';
	d1['div'] = 'e1';
	d1['isDynamic'] = false;
	d1['trigger'] = null;
	result.push(d1);
	d2['field'] = 'gambling';
	d2['type'] = 'text';
	d2['div'] = 'e2';
	d2['isDynamic'] = false;
	d2['trigger'] = null;
	result.push(d2);
	d3['field'] = 'abilities';
	d3['type'] = 'text';
	d3['div'] = 'e3';
	d3['isDynamic'] = false;
	d3['trigger'] = null;
	result.push(d3);
	d4['field'] = 'other';
	d4['type'] = 'text';
	d4['div'] = 'e4';
	d4['isDynamic'] = false;
	d4['trigger'] = null;
	result.push(d4);

	return result;
}

function fetchFieldList_sap(section) {
	var fields = [];
	section = String(section);

	if (section === '/sap_demographic/') {
		fields = fetch_demoFields_sap();
	}
	else if (section === '/sap_social/') {
		fields = fetch_socialFields_sap();
	}
	else if (section === '/sap_psychoactive2/') {
		fields = fetch_psych2Fields_sap();
	}
	else if (section === '/sap_other/') {
		fields = fetch_additionalFields_sap();
	}
	return fields;
}

function get_sap_pgroupFields(groupNumber) {
	var plist = fetch_psych1Fields_sap();
	var result = [];

	groupNumber = Number(groupNumber);

	if (groupNumber === 1) {
		result.push(plist[0]);
		result.push(plist[1]);
		result.push(plist[2]);
		result.push(plist[3]);
		result.push(plist[4]);
	}
	else if (groupNumber === 2) {
		result.push(plist[5]);
		result.push(plist[6]);
		result.push(plist[7]);
		result.push(plist[8]);
		result.push(plist[9]);
	}
	else if (groupNumber === 3) {
		result.push(plist[10]);
		result.push(plist[11]);
		result.push(plist[12]);
		result.push(plist[13]);
		result.push(plist[14]);
	}
	else if (groupNumber === 4) {
		result.push(plist[15]);
		result.push(plist[16]);
		result.push(plist[17]);
		result.push(plist[18]);
		result.push(plist[19]);
	}
	else if (groupNumber === 5) {
		result.push(plist[20]);
		result.push(plist[21]);
		result.push(plist[22]);
		result.push(plist[23]);
		result.push(plist[24]);
	}
	else if (groupNumber === 6) {
		result.push(plist[25]);
		result.push(plist[26]);
		result.push(plist[27]);
		result.push(plist[28]);
		result.push(plist[29]);
	}
	else if (groupNumber === 7) {
		result.push(plist[30]);
		result.push(plist[31]);
		result.push(plist[32]);
		result.push(plist[33]);
		result.push(plist[34]);
	}
	else if (groupNumber === 8) {
		result.push(plist[35]);
		result.push(plist[36]);
		result.push(plist[37]);
		result.push(plist[38]);
		result.push(plist[39]);
	}
	else if (groupNumber === 9) {
		result.push(plist[40]);
		result.push(plist[41]);
		result.push(plist[42]);
		result.push(plist[43]);
		result.push(plist[44]);
	}
	else if (groupNumber === 10) {
		result.push(plist[45]);
		result.push(plist[46]);
		result.push(plist[47]);
		result.push(plist[48]);
		result.push(plist[49]);
	}
	else if (groupNumber === 11) {
		result.push(plist[50]);
		result.push(plist[51]);
		result.push(plist[52]);
		result.push(plist[53]);
		result.push(plist[54]);
	}
	else if (groupNumber === 12) {
		result.push(plist[55]);
		result.push(plist[56]);
		result.push(plist[57]);
		result.push(plist[58]);
		result.push(plist[59]);
	}

	return result;
}

function sap_p_hasErrors(groupList) {
	var hasErrors = false;

	for (var i = 0; i < groupList.length; i++) {
		var sub = String(groupList[i]['sub']);

		if (sub === 'Age') {
			hasErrors = hasNumberErrors(groupList[i]);
		}
		else {
			hasErrors = hasTextError(groupList[i]);
		}

		if (hasErrors === true) {
			break;
		}
	}

	return hasErrors;
}

function getSpecialMhLine(errorName) {
	var result = [];
	var allOpsFields = fetchFieldList_mh('/mhDemoOpPage/');
	errorName = String(errorName);

	for (var i = 0; i < allOpsFields.length; i++) {
		if (String(allOpsFields[i]['div']) === errorName) {
			result.push(allOpsFields[i]);
		}
	}

	return result;
}

function mh_opLine_hasErrors(errorName) {
	var hasErrors = false;
	var elements = getSpecialMhLine(errorName);

	for (var i = 0; i < elements.length; i++) {
		if (elements[i]['type'] === 'text') {
			hasErrors = hasTextError(elements[i]);
		}
		else if (elements[i]['type'] === 'number') {
			hasErrors = hasNumberErrors(elements[i]);
		}
		else if (elements[i]['type'] === 'select') {
			hasErrors = hasSelectErrors(elements[i]);
		}

		if (hasErrors === true) {
			break;
		}
	}
	return hasErrors;
}

function set_mh_op_errors(errorName) {
	var hasError = mh_opLine_hasErrors(errorName);

	if (hasError === true) {
		setErrorDiv(errorName);
	}
}

function encodeOpMale() {
	var result = '';
	var numKids = grab('numKids').value;
	numKids = Number(numKids);

	for (var i = 1; i <= numKids; i++) {
		var radioTag = 'male_' + String(i);
		var radio = grab(radioTag);

		if (radio.checked === true) {
			var ageTag = 'age_' + String(i);
			var cityTag = 'city_' + String(i);
			var stateTag = 'state_' + String(i);

			var age = String(grab(ageTag).value);
			var city = String(grab(cityTag).value);
			var state = String(grab(stateTag).value);

			result += age;
			result += '/';
			result += city;
			result += ', ';
			result += state;
			result += '~';
		}
	}

	return result;
}

function encodeOpFemale() {
	var result = '';
	var numKids = grab('numKids').value;
	numKids = Number(numKids);

	for (var i = 1; i <= numKids; i++) {
		var radioTag = 'female_' + String(i);
		var radio = grab(radioTag);

		if (radio.checked === true) {
			var ageTag = 'age_' + String(i);
			var cityTag = 'city_' + String(i);
			var stateTag = 'state_' + String(i);

			var age = String(grab(ageTag).value);
			var city = String(grab(cityTag).value);
			var state = String(grab(stateTag).value);

			result += age;
			result += '/';
			result += city;
			result += ', ';
			result += state;
			result += '~';
		}
	}

	return result;
}

function encodeOpSisters() {
	var result = '';
	var numKids = grab('numKids').value;
	var numSisters = grab('numSisters').value;
	var tagNumber = Number(numKids) + 1;

	numSisters = Number(numSisters);

	for (var i = 0; i < numSisters; i++) {
		var ageTag = 'age_' + String(tagNumber);
		var cityTag = 'city_' + String(tagNumber);
		var stateTag = 'state_' + String(tagNumber);

		var age = String(grab(ageTag).value);
		var city = String(grab(cityTag).value);
		var state = String(grab(stateTag).value);

		result += age;
		result += '/';
		result += city;
		result += ', ';
		result += state;
		result += '~';

		tagNumber += 1;
	}
	return result;
}

function encodeOpBrothers() {
	var result = '';
	var numKids = grab('numKids').value;
	var numSisters = grab('numSisters').value;
	var numBrothers = grab('numBrothers').value;
	numSisters = Number(numSisters);
	numBrothers = Number(numBrothers);
	var tagNumber = Number(numKids) + numSisters + 1;
	

	for (var i = 0; i < numBrothers; i++) {
		var ageTag = 'age_' + String(tagNumber);
		var cityTag = 'city_' + String(tagNumber);
		var stateTag = 'state_' + String(tagNumber);

		var age = String(grab(ageTag).value);
		var city = String(grab(cityTag).value);
		var state = String(grab(stateTag).value);

		result += age;
		result += '/';
		result += city;
		result += ', ';
		result += state;
		result += '~';

		tagNumber += 1;
	}
	return result;
}

function encode_mh_op_Results(m_type, gender) {
	var result = '';
	m_type = String(m_type);
	gender = String(gender);

	if (m_type === 'child') {
		if (gender === 'male') {
			result = encodeOpMale();
		}
		else if (gender === 'female') {
			result = encodeOpFemale();
		}
	}
	else if (m_type === 'sister') {
		result = encodeOpSisters();
	}
	else if (m_type === 'brother') {
		result = encodeOpBrothers();
	}

	return result;
}

function opHasMaleChild() {
	var hasMale = false;
	var numKids = grab('numKids').value;
	numKids = Number(numKids);

	for (var i = 1; i <= numKids; i++) {
		var yesTag = 'male_' + String(i);
		var radio = grab(yesTag);

		if (radio.checked === true) {
			hasMale = true;
			break;
		}
	}
	return hasMale;
}

function opHasFemaleChild() {
	var hasFemale = false;
	var numKids = grab('numKids').value;
	numKids = Number(numKids);

	for (var i = 1; i <= numKids; i++) {
		var yesTag = 'female_' + String(i);
		var radio = grab(yesTag);

		if (radio.checked === true) {
			hasFemale = true;
			break;
		}
	}
	return hasFemale;
}

function postMhOpgirls() {
	if (opHasFemaleChild() === true && getPopParent('yesChild').checked === true) {
		getPopParent('childrenFemale').value = encodeOpFemale();
	}
	else {
		getPopParent('childrenFemale').value = 'N/A';
	}
}

function postMhOpboys() {
	if (opHasMaleChild() === true && getPopParent('yesChild').checked === true) {
		getPopParent('childrenMale').value = encodeOpMale();
	}
	else {
		getPopParent('childrenMale').value = 'N/A';
	}
}

function postMhOpSisters() {
	if (getPopParent('yesSister').checked === true) {
		getPopParent('m_sistersFinal').value = encodeOpSisters();
	}
	else {
		getPopParent('m_sistersFinal').value = 'N/A';
	}
}

function postMhOpBrothers() {
	if (getPopParent('yesBrother').checked === true) {
		getPopParent('m_brothersFinal').value = encodeOpBrothers();
	}
	else {
		getPopParent('m_brothersFinal').value = 'N/A';
	}
}

function verify_mh_op() {
	var hasErrors = hasErrorsInForm('mh', '/mhDemoOpPage/');

	if (hasErrors === true) {
		var fields = fetchMhOpsFieldNames();
		var numToCheck = Number(fields.length) / 3;

		for (var i = 1; i <= numToCheck; i++) {
			var divName = 'e' + String(i);
			set_mh_op_errors(divName);
		}
	}
	else {
		postMhOpgirls();
		postMhOpboys();
		postMhOpSisters();
		postMhOpBrothers();

		//change the parent button to perform mh save function
		getPopParent('superBtn').innerHTML = '';
		getPopParent('superBtn').innerHTML = " <button onClick=\"javascript: post_mh_data(\'/mh_demographic/\'); return false;\">Save & Continue</button>";
		getPopParent('superBtn').className = 'pro-iml-btn';

		window.close();
	}
}

function checkAllPsyFieldsForErrors_sap() {
	var hasErrors = false;

	for (var i = 1; i <= 12; i++) {
		var group = get_sap_pgroupFields(i);
		hasErrors = sap_p_hasErrors(group);

		if (hasErrors === true) {
			break;
		}
	}
	return hasErrors;
}

function proceedWithPsychoactiveCheck(group) {
	proceed = false;
	continueSearch = true;

	var ageItem = null;
	var items = [];

	for (var i = 0; i < group.length; i++) {
		if (String(group[i]['sub']) === 'Age') {
			ageItem = group[i];
		}
		else {
			items.push(group[i]);
		}
	}

	var ageField = grab(String(ageItem['field']));
	if (String(ageField.value) !== '0') {
		continueSearch = false;
		proceed = true;
	}

	if (continueSearch === true) {
		for (var j = 0; j < items.length; j++) {
			var field = grab(String(items[j]['field']));
			if (isBlankText(field.value) === false) {
				proceed = true;
				break;
			} 
		}
	}

	return proceed;
}


function superSap_PsychErrors(groupNumber) {
	var groupList = get_sap_pgroupFields(groupNumber);
	var checkForErrors = proceedWithPsychoactiveCheck(groupList);
	var hasErrors = sap_p_hasErrors(groupList);

	if (hasErrors === true && checkForErrors === true) {
		var errorDivName = groupList[0]['div'];
		setErrorDivPsy(errorDivName);
	}
}

function checkAllSapPsych1Fields() {
	for (var i = 1; i <= 12; i++) {
		superSap_PsychErrors(i);
	}
}

function superDuperSapHasErrors(section) {
	section = String(section);
	var hasErrors = false;

	if (section === '/sap_psychoactive/') {
		hasErrors = checkAllPsyFieldsForErrors_sap();
	}
	else {
		hasErrors = hasErrorsInForm('sap', section);
	}
	return hasErrors;
}





//++++++++++++++++++++++++++++++++++++++++++++++++++++ MAIN USE ERROR CHECKING FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++++ MAIN USE ERROR CHECKING FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++++ MAIN USE ERROR CHECKING FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++++ MAIN USE ERROR CHECKING FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++++ MAIN USE ERROR CHECKING FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++//

function fetchFieldList(type, section) {
	var result = null;
	type = String(type);

	if (type === 'am') {
		result = fetchFieldList_am(section);
	}
	else if (type === 'mh') {
		result = fetchFieldList_mh(section);
	}
	else if (type === 'sap') {
		result = fetchFieldList_sap(section);
	}
	else if (type === 'asi') {
		result = fetchFieldList_asi(section);
	}

	return result;
}

function hasErrorsInForm(formType, section) {
	var isGood = false;
	var fieldList = null;
	formType = String(formType);
	section = String(section);
	fieldList = fetchFieldList(formType, section);

	for (var i = 0; i < fieldList.length; i++) {
		if (fieldList[i]['type'] === 'text') {
			isGood = hasTextError(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'number') {
			isGood = hasNumberErrors(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'select') {
			isGood = hasSelectErrors(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'ssn') {
			isGood = hasSsnErrors(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'phone') {
			isGood = hasPhoneErrors(fieldList[i]);
			}
		else if (fieldList[i]['type'] === 'date') {
			isGood = hasDateErrors(fieldList[i]);
		}

		if (isGood === true) {
			break;
		}
	}

	return isGood;
}

function specialHasErrorCheck_m(fieldList, numberOption) {
	var isGood = false;

	for (var i = 0; i < fieldList.length; i++) {
		if (fieldList[i]['type'] === 'text') {
			isGood = hasTextError(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'number') {
			if (numberOption === true) {
				isGood = hasNumberErrors_noZero(fieldList[i]);
			}
			else {
				isGood = hasNumberErrors(fieldList[i]);
			}			
		}
		else if (fieldList[i]['type'] === 'select') {
			isGood = hasSelectErrors(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'ssn') {
			isGood = hasSsnErrors(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'phone') {
			isGood = hasPhoneErrors(fieldList[i]);
			}
		else if (fieldList[i]['type'] === 'date') {
			isGood = hasDateErrors(fieldList[i]);
		}

		if (isGood === true) {
			break;
		}
	}
	return isGood;
}

function superDuperSapChecker(section) {
	section = String(section);

	if (section === '/sap_psychoactive/') {
		checkAllSapPsych1Fields();
	}
	else {
		superErrorChecker('sap', section);
	}
}

function superErrorChecker(formType, section) {
	var formType = String(formType);
	var fieldList = fetchFieldList(formType, section);

	for (var i = 0; i < fieldList.length; i++) {
		if (fieldList[i]['type'] === 'text') {
			textErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'number') {
			numberErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'select') {
			selectErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'ssn') {
			ssnErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'phone') {
			phoneErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'date') {
			dateErrorChecker(fieldList[i]);
		}
	}
}

function SpecialSuperErrorChecker(fieldList, numberOption) {

	for (var i = 0; i < fieldList.length; i++) {
		if (fieldList[i]['type'] === 'text') {
			textErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'number') {
			if (numberOption === true) {
				numberErrorChecker_noZero(fieldList[i]);
			}
			else {
				numberErrorChecker(fieldList[i]);
			}
		}
		else if (fieldList[i]['type'] === 'select') {
			selectErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'ssn') {
			ssnErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'phone') {
			phoneErrorChecker(fieldList[i]);
		}
		else if (fieldList[i]['type'] === 'date') {
			dateErrorChecker(fieldList[i]);
		}
	}
}

function runFunctionTest() {
	var section = grab('save_section').value;
	var hasErrors = superDuperSapHasErrors(section);
	if (hasErrors === true) {
		superDuperSapChecker(section);
	}
	// grab('health').value = 'Errors in form? ' + hasErrors;
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//*************************************************** END ERROR CHECKER *************************************************************//
//*************************************************** END ERROR CHECKER *************************************************************//
//*************************************************** END ERROR CHECKER *************************************************************//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//


//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//*****************************************  NOTES AND UPLOADS ******************************************************
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

function rock_new_note() {
	openPopUp('auto', "/new_note_pad/", 450, 450);
}

function hasNoteErrors(subError, bodyError) {
	var hasError = false;

	if (subError === true) {hasError = true;}
	if (bodyError === true) {hasError = true;}

	return hasError;
}

function getNoteErrors(subError, bodyError) {
	var errors = [];
	if (subError === true) {
		grab('error1').value = 'true';
	}
	else {
		grab('error1').value = 'false';
	}
	if (bodyError === true) {
		grab('error2').value = 'true';
	}
	else {
		grab('error2').value = 'false';
	}
}

function initialize_notePad_errors() {
	var div = grab('error_population');
	var error1 = String(getPopParent('error1').value);
	var error2 = String(getPopParent('error2').value);
	var msg1 = "";
	var msg2 = "";

	if (error1 === 'true') {
		msg1 = "<li>You must provide a subject</li>";
	}
	if (error2 === 'true') {
		msg2 = "<li>You must include note content</li>";
	}

	var html = "<ul>" + msg1 + msg2 + "</ul>";
	div.innerHTML = html;
}

function saveNotePadItem() {
	var subject = String(grab('subject').value);
	var body = String(grab('body').value);

	var subj_error = isBlankText(subject);
	var body_error = isBlankText(body);
	var hasErrors  = hasNoteErrors(subj_error, body_error);

	if (hasErrors === true) {
		var errors = getNoteErrors(subj_error, body_error);
		openPopUp('auto', '/notePadErrorPage/', 350, 350);
	}
	else {
		getPopParent('note_subject').value = subject;
		getPopParent('note_body').value = body;
		grab('nnform').submit();
	}
}

function deleteNotePad() {
	getPopParent('edit_enabled').value = 'false';
	getPopParent('note_subject').value = '';
	getPopParent('note_body').value = '';
	getPopParent('note_id').value = '';
	grab('nnform').action = "/notePadDeleted/";
	grab('nnform').submit();
}

function editNotePad() {
	var form = grab('nnform');
	getPopParent('edit_enabled').value = 'true';
	getPopParent('note_id').value = grab('note_id').value;
	form.action = '/new_note_pad/';
	form.submit();
}

function saveNotePadChanges() {
	getPopParent('edit_enabled').value = 'false';
	getPopParent('note_subject').value = '';
	getPopParent('note_body').value = '';
	getPopParent('note_id').value = '';
	window.close();
}

function initializeNotePadOptions() {
	getPopParent('note_id').value = grab('note_id').value;
}

function initializeNotePad() {
	var edit_enabled = String(getPopParent('edit_enabled').value);
	grab('note_id').value = getPopParent('note_id').value;
	grab('edit_enabled').value = edit_enabled;

	if (edit_enabled === 'true') {
		grab('subject').value = getPopParent('note_subject').value;
		grab('body').value = getPopParent('note_body').value;
		grab('addNoteBtn').innerHTML = 'Save Changes';
	}
}

function simpleUpload() {
	openPopUp('auto', '/simpleUpload/', 400, 200);
}

function verify_uploadTitle() {
	var title = grab('title');
	var value = String(title.value);
	var isBlank = isBlankText(value);
	var file = String(grab('upload').value);
	var noFile = isBlankText(file);

	if (isBlank === true || noFile === true) {
		openPopUp('auto', '/uploadError/', 350, 160);
	}
	else {
		grab('upload_form').submit();
	}
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//*****************************************  END NOTES ******************************************************************
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

function fetchUpdatableCoupleFields() {
	updates = [];

	updates.push('street_no');
	updates.push('street_name');
	updates.push('apartment_no');
	updates.push('city');
	updates.push('zip_code');
	updates.push('emer_contact_name');
	updates.push('probationOfficer');
	updates.push('email');

	return updates;
}

function fetchUpdatableCoupleFieldsNum() {
	updates = [];

	updates.push('emer_phone');
	updates.push('probation_phone');
	updates.push('phone');
	updates.push('work_phone');

	return updates;
}

function singlefinalizeUpdatedCoupleField(elementName) {
	elementName 	= String(elementName);
	var initialName = 'i_' + elementName;
	var inputName 	= 'input_' + elementName;
	var initial 	= grab(initialName);
	var input 		= grab(inputName);

	if (String(initial.value) !== String(input.value)) {
		input.style.color = '#983341';
		input.style.border = '1px solid red';
	}
	else {
		input.style.color = 'black';
		input.style.border = '1px solid gray';
	}
}

function singlefinalizeUpdatedCoupleFieldNum(elementName) {
	elementName 	= String(elementName);
	var initialName = 'i_' + elementName;
	var inputName 	= 'input_' + elementName;
	var initial 	= grab(initialName);
	var input 		= grab(inputName);
	var raw 		= getRawNumber(input.value);

	if (String(initial.value) !== String(raw)) {
		input.style.color = '#983341';
		input.style.border = '1px solid red';
	}
	else {
		input.style.color = 'black';
		input.style.border = '1px solid gray';
	}
}

function finalizeAllUpdatedCoupleFields() {
	finalizeUpdatedCoupleField();
	finalizeUpdatedCoupleFieldNum();
}

function finalizeUpdatedCoupleField() {
	var fields = fetchUpdatableCoupleFields();

	for (var i = 0; i < fields.length; i++) {
		singlefinalizeUpdatedCoupleField(fields[i]);
	}
}

function finalizeUpdatedCoupleFieldNum() {
	var fields = fetchUpdatableCoupleFieldsNum();

	for (var i = 0; i < fields.length; i++) {
		singlefinalizeUpdatedCoupleFieldNum(fields[i]);
	}
}

function compare_i_u(elementName) {
	elementName 	= String(elementName);
	var initialName = 'i_' + elementName;
	var inputName 	= 'input_' + elementName;
	var initial 	= grab(initialName);
	var input 		= grab(inputName);

	for (var i = 0; i < input.value.length; i++) {
		if (input.value.charAt(i) !== initial.value.charAt(i)) {
			input.style.color = '#983341';
			input.style.border = '1px solid red';
			break;
		}
		else {
			input.style.color = 'black';
			input.style.border = '1px solid gray';
		}
	}
}

function compare_i_u_num(elementName) {
	elementName 	= String(elementName);

	var initialName = 'i_' + elementName;
	var inputName 	= 'input_' + elementName;
	var initial 	= grab(initialName);
	var input 		= grab(inputName);
	var raw 		= getRawNumber(input.value);

	for (var i = 0; i < raw.length; i++) {
		if (initial.value.charAt(i) !== raw.charAt(i)) {
			input.style.color = '#983341';
			input.style.border = '1px solid red';
			break;
		}
		else {
			input.style.color = 'black';
			input.style.border = '1px solid gray';
		}
	}
}

function buildUpdateFieldValue(elementName) {
	elementName 	= String(elementName);
	var initialName = 'i_' + elementName;
	var updatedName = 'u_' + elementName;
	var inputName 	= 'input_' + elementName;

	var initialDiv 	= grab(initialName);
	var updatedDiv 	= grab(updatedName);
	var inputDiv 	= grab(inputName);

	var initialValue = String(initialDiv.value);
	var updatedValue = String(updatedDiv.value);

	if (isBlankText(updatedValue) === false && initialValue !== updatedValue) {
		inputDiv.value = updatedValue;
	}
	else {
		inputDiv.value = initialValue;
	}
	compare_i_u(elementName);
}

function buildUpdateFieldValueNum(elementName) {
	elementName 	= String(elementName);
	var initialName = 'i_' + elementName;
	var updatedName = 'u_' + elementName;
	var inputName 	= 'input_' + elementName;

	var initialDiv 	= grab(initialName);
	var updatedDiv 	= grab(updatedName);
	var inputDiv 	= grab(inputName);

	var initialValue = String(initialDiv.value);
	var updatedValue = String(updatedDiv.value);

	if (isBlankText(updatedValue) === false) {
		if (initialValue !== updatedValue) {
			inputDiv.value = properPhoneFormatDisplay(updatedValue);
		}
		else {
			inputDiv.value = properPhoneFormatDisplay(initialValue);
		}
	}
	else {
		inputDiv.value = properPhoneFormatDisplay(initialValue);
	}

	compare_i_u_num(elementName);
}

function properPhoneFormatDisplay(value) {
	var areaCode 	= '';
	var preNCode 	= '';
	var postCode 	= '';
	var proper 		= '';
	value 			= String(value);

	if (value.length === 10) {
		areaCode += value.charAt(0);
		areaCode += value.charAt(1);
		areaCode += value.charAt(2);
		preNCode += value.charAt(3);
		preNCode += value.charAt(4);
		preNCode += value.charAt(5);
		postCode += value.charAt(6);
		postCode += value.charAt(7);
		postCode += value.charAt(8);
		postCode += value.charAt(9);

		proper = "(" + areaCode + ") " + preNCode + "-" + postCode;
	}
	return proper;
}

function initializeUpdateCoupleFields() {
	var fields = fetchUpdatableCoupleFields();
	var phones = fetchUpdatableCoupleFieldsNum();

	for (var i = 0; i < fields.length; i++) {
		buildUpdateFieldValue(fields[i]);
	}

	for (var j = 0; j < phones.length; j++) {
		buildUpdateFieldValueNum(phones[j]);
	}
}

function startCoupleSession() {
	openPopUp('auto', '/startCoupleSession/', 350, 370);
}

function startCoupleSession_refresh() {
	var form = grab('c_form');
	form.action = '/startCoupleSession/';
	form.submit();
	var w = 350, h = 390;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	window.resizeTo(w, h);
	window.moveTo(l, t);
	window.focus();
}

function setCouplePair(client2_id) {
	getPopParent('c2_id').value = String(client2_id);
	getPopParent('c2Type').value = "existing";
	getPopParent('c_form').action = '/coupleSession/';
	getPopParent('c_form').submit();
	window.close();
}

function selectNewCouple() {
	var form = grab('m_form')
	form.action = '/chooseNewPair/';
	form.submit();
}

function newClientBaseless() {
	getPopParent('c2Type').value = 'new';
	var form = grab('c_form');
	form.action = '/newClientBaseless/';
	form.submit();

	var w = 500, h = 580;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	window.resizeTo(w, h);
	window.moveTo(l, t);
	window.focus();
}

function testFunction() {
	openPopUp('auto', '/viewProfile', 500, 560);
}

function isRawNumber(num) {
	isNumber = true;
	num = String(num);

	for (var i = 0; i < num.length; i++) {
		var c = num.charAt(i);

		if (c!=='0' && c!=='1' && c!=='2' && c!=='3' && c!=='4' && c!=='5' && c!=='6' && c!=='7' && c!=='8' && c!=='9') {
			isNumber = false;
			break;
		}
	}

	return isNumber;
}

function isRawSSN(num) {
	isNumber = true;
	num = clearWhiteSpace(num);
	num = String(num);

	for (var i = 0; i < num.length; i++) {
		var c = num.charAt(i);

		if (i === 3 || i ===6) {
			if (c !== "-") {
				isNumber = false;
				break;
			}
		}
		else {
			if (isRawNumber(c) === false) {
				isNumber = false;
				break;
			}
		}
	}

	return isNumber;
}

function isRawPhone(num) {
	isNumber = true;
	num = clearWhiteSpace(num);
	num = String(num);

	for (var i = 0; i < num.length; i++) {
		var c = num.charAt(i);

		if (i === 0) {
			if (c !== "(") {
				isNumber = false;
				break;
			}
		}
		if (i === 4) {
			if (c !== ")") {
				isNumber = false;
				break;
			}
		}
		if (i === 8) {
			if (c !== "-") {
				isNumber = false;
				break;
			}
		}
		if (i!==0 && i!==4 && i!==8) {
			if (isRawNumber(c) === false) {
				isNumber = false;
				break;
			}
		}
	}

	return isNumber;
}

function getRawNumber(num) {
	var modified = "";
	num = String(num);
	num = clearWhiteSpace(num);

	for (var i = 0; i < num.length; i++) {
		var c = num.charAt(i);

		if (c==='0' || c==='1' || c==='2' || c==='3' || c==='4' || c==='5' || c==='6' || c==='7' || c==='8' || c==='9') {
			modified += c;
		}
	}

	return modified;
}

function getRawSSN(ssn) {
	var modified = "";
	ssn = String(ssn);
	ssn = clearWhiteSpace(ssn);

	for (var i = 0; i < ssn.length; i++) {
		var c = ssn.charAt(i);

		if (c==='0' || c==='1' || c==='2' || c==='3' || c==='4' || c==='5' || c==='6' || c==='7' || c==='8' || c==='9' || c==='-') {
			modified += c;
		}
	}

	return modified;
}

function getRawPhone(ph) {
	var modified = "";
	ph = String(ph);
	ph = clearWhiteSpace(ph);

	for (var i = 0; i < ph.length; i++) {
		var c = ph.charAt(i);

		if (c==='0' || c==='1' || c==='2' || c==='3' || c==='4' || c==='5' || c==='6' || c==='7' || c==='8' || c==='9' || c==='-' || c==='(' || c===')' || c==='-') {
			modified += c;
		}
	}

	return modified;
}

function specialNumberError(value, numChars, ElementType, blankAllowed) {
	var hasError = false;
	var raw = null;
	var proceed = true;
	value = String(value);
	numChars = Number(numChars);
	ElementType = String(ElementType);

	if (ElementType === 'phone') {
		if (value.length > 10) {
			if (isRawPhone(value) === false) {
				proceed = false;
				hasError = true;
			}
			else {
				raw = getRawPhone(value);
				numChars = 13;
			}			
		}
		else {
			raw = getRawNumber(value);
		}
	}

	else if (ElementType === 'ssn') {
		if (value.length > 9) {
			if (isRawSSN(value) === false) {
				proceed = false;
				hasError = true;
			}
			else {
				raw = getRawSSN(value);
				numChars = 11;
			}
		}
		else {
			raw = getRawNumber(value);
		}
	}

	else if (ElementType === 'zip') {
		raw = getRawNumber(value);
	}

	if (proceed === true) {
		if (blankAllowed === false) {
			if (raw.length !== numChars || isBlankText(raw) === true || raw === null || raw === "") {
				hasError = true;
			}
		}
		else {
			if (raw.length !== numChars) {
				hasError = true;
			}
		}
	}

	return hasError;
}

function parent_newClient_specialErrors() {
	var verified 	= true;
	var zip_code 	= getPopParent('zip_code');
	var ssn 		= getPopParent('ss_num');
	var phone 		= getPopParent('phone');
	var emer_phone 	= getPopParent('emer_phone');
	var work_phone 	= getPopParent('work_phone');
	var prob_phone 	= getPopParent('probation_phone');

	if (specialNumberError(ssn.value, 9, 'ssn', false) === true) {
		verified = false;
		ssn.style.border = "2px solid red";
	}

	if (specialNumberError(zip_code.value, 5, 'zip', false) === true || isRawNumber(zip_code.value) === false) {
		verified = false;
		zip_code.style.border = "2px solid red";
	}

	if (specialNumberError(phone.value, 10, 'phone', false) === true) {
		verified = false;
		phone.style.border = "2px solid red";
	}

	if (specialNumberError(emer_phone.value, 10, 'phone', false) === true) {
		verified = false;
		emer_phone.style.border = "2px solid red";
	}

	if (isBlankText(work_phone.value) === false) {
		if (specialNumberError(work_phone.value, 10, 'phone', true) === true) {
			verified = false;
			work_phone.style.border = "2px solid red";
		}
	}

	if (isBlankText(prob_phone.value) === false) {
		if (specialNumberError(prob_phone.value, 10, 'phone', true) === true) {
			verified = false;
			prob_phone.style.border = "2px solid red";
		}
	}

	return verified;
}


function newClient_specialErrors() {
	var verified 	= true;
	var zip_code 	= grab('zip_code');
	var ssn 		= grab('ss_num');
	var phone 		= grab('phone');
	var emer_phone 	= grab('emer_phone');
	var work_phone 	= grab('work_phone');
	var prob_phone 	= grab('probation_phone');

	if (specialNumberError(ssn.value, 9, 'ssn', false) === true) {
		verified = false;
		ssn.style.border = "2px solid red";
	}

	if (specialNumberError(zip_code.value, 5, 'zip', false) === true || isRawNumber(zip_code.value) === false) {
		verified = false;
		zip_code.style.border = "2px solid red";
	}

	if (specialNumberError(phone.value, 10, 'phone', false) === true) {
		verified = false;
		phone.style.border = "2px solid red";
	}

	if (specialNumberError(emer_phone.value, 10, 'phone', false) === true) {
		verified = false;
		emer_phone.style.border = "2px solid red";
	}

	if (isBlankText(work_phone.value) === false) {
		if (specialNumberError(work_phone.value, 10, 'phone', true) === true) {
			verified = false;
			work_phone.style.border = "2px solid red";
		}
	}

	if (isBlankText(prob_phone.value) === false) {
		if (specialNumberError(prob_phone.value, 10, 'phone', true) === true) {
			verified = false;
			prob_phone.style.border = "2px solid red";
		}
	}

	return verified;
}

function newClient_fullErrorChecker() {
	var results 		= {};
	var hasErrors 		= false;
	var blankErrors 	= newClient_hasTextError();
	var formatVerified 	= newClient_specialErrors();
	var selectErrors 	= newClient_hasSelectErrors();
	var e1 = '';
	var e2 = '';

	if (blankErrors === true || formatVerified === false) {
		hasErrors = true;
		e1 = "<li><div class=\"redErrorField\">Fields that are highlighted with <span>RED</span> cannot be blank or are not in the correct format (SSN: xxx-xx-xxxx)</div></li>";
	}

	if (selectErrors === true) {
		hasErrors = true;
		e2 = "<li><div class=\"orangeErrorField\">You must make a selection from the fields highlighted with <span>ORANGE</span></div></li>"
	}

	var html = "<ul>" + e1 + e2 + "</ul>";

	results['hasErrors'] = hasErrors;
	results['html'] = html;

	return results;

}



function chooseAsIsCouple2() {
	var form = getPopParent('c_form');
	getPopParent('c2Type').value = 'existing';
	getPopParent('c2_id').value = grab('client_id').value;
	form.action = '/coupleSession/';
	form.submit();
	window.close();
}

function saveBaselessUpdates() {
	var form1 = getPopParent('c_form');
	var form2 = grab('c_form');
	var w = 250, h = 250;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));

	getPopParent('c2Type').value = 'existing';
	getPopParent('c2_id').value = grab('client_id').value;

	window.resizeTo(w, h);
	window.moveTo(l, t);
	window.focus();

	form1.action = '/coupleSession/';
	form2.action = '/baselessUpdated/';
	form1.submit();
	form2.submit();
}

function forwardToUpdateCouple2() {
	grab('c_form').submit();
}

function processNewClientFinalNumbers(div) {
	result = null;
	value = String(div.value);

	if (value.length > 0) {
		result = getRawNumber(value);
	}

	div.value = result;
}


function saveBaselessClient() {
	var report = newClient_fullErrorChecker();
	var boolText = String(report['hasErrors']);

	if (boolText === 'true') {
		var errorWindow = openPopUp('auto', '/errorLegend/', 300, 300);
	}
	else {
		if (grab('photo').value.length > 0) {
			grab('hasImage').value = "True";
		}

		processNewClientFinalNumbers(grab('ss_num'));
		processNewClientFinalNumbers(grab('phone'));
		processNewClientFinalNumbers(grab('work_phone'));
		processNewClientFinalNumbers(grab('probation_phone'));
		processNewClientFinalNumbers(grab('emer_phone'));

		var form = grab('m_form');
		form.action = '/clientCreatedBaseless/';
		form.submit();
	}
}

function initialize_newClientErrors() {
	
}

function autoFillTest() {
	grab('fname').value = "Da";
	grab('mi').value = "M";
	grab('lname').value = "Fuck";
	grab('street_no').value = "123";
	grab('street_name').value = "Shit Creek";
	grab('apartment_no').value = "4A";
	grab('city').value = "Cow Nuts";
	grab('state').selectedIndex = 12;
	grab('zip_code').value = "12345";
	grab('ss_num').value = "123-45-6789";
	grab('month').selectedIndex = 5;
	grab('year').selectedIndex = 45;
	grab('phone').value = "(810) 785-2166";
	grab('work_phone').value = "(212) 980-2323";
	grab('email').value = "email@email.com";
	grab('probationOfficer').value = "Dumb Bitch";
	grab('probation_phone').value = "(678) 967-9090";
	grab('emer_contact_name').value = "Random Hooker";
	grab('emer_phone').value = "6578979090";
	grab('reason_ref').selectedIndex = 4;
	buildDropDayList(30);
	grab('day').selectedIndex = 22;
}

function goToCoupleNewClient() {
	var form = getPopParent('c_form');
	form.action = '/coupleSession/';
	form.submit();
	window.close();
}

function editNewClientData() {
	
}

function newClientAborted() {
	var wins = [];
	wins.push(window);
	wins.push(openPopUp('auto', '/newClientAborted/', 250, 150));
	wins[0].close();
	wins[1].focus();
}

function searchLikeWow() {
	getPopParent('searchType').value = grab('searchType').value;
	var form = grab('c_form');
	form.action = '/wowSearch/';
	form.submit();
	var w = 315, h = 500;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	window.resizeTo(w, h);
	window.moveTo(l, t);
	window.focus();
}

function searchClient_shouldSearchText(value) {
	value = String(value);
	value = clearWhiteSpace(value);
	var isBlank = isBlankText(value)
	var shouldSearch = true;

	if (isBlank === true) {
		shouldSearch = false;
	}
	return shouldSearch;
}

function setWowCheck(elementName) {
	elementName = String(elementName);
	var targetName = "m_" + elementName;
	var div = grab(elementName);
	var target = grab(targetName);

	if (div.checked === true) {
		target.value = "True";
	}
	else {
		target.value = "False";
	}
}

function getWowJsonArray(page, json_data) {
	page == Number(page);
	var data = null;

	if (page === 1) {data = json_data.page_1;}
	else if (page === 2) {data = json_data.page_2;}
	else if (page === 3) {data = json_data.page_3;}
	else if (page === 4) {data = json_data.page_4;}
	else if (page === 5) {data = json_data.page_5;}
	else if (page === 6) {data = json_data.page_6;}
	else if (page === 7) {data = json_data.page_7;}
	else if (page === 8) {data = json_data.page_8;}
	else if (page === 9) {data = json_data.page_9;}
	else if (page === 10) {data = json_data.page_10;}
	else if (page === 11) {data = json_data.page_11;}
	else if (page === 12) {data = json_data.page_12;}
	else if (page === 13) {data = json_data.page_13;}
	else if (page === 14) {data = json_data.page_14;}
	else if (page === 15) {data = json_data.page_15;}
	else if (page === 16) {data = json_data.page_16;}
	else if (page === 17) {data = json_data.page_17;}
	else if (page === 18) {data = json_data.page_18;}
	else if (page === 19) {data = json_data.page_19;}
	else if (page === 20) {data = json_data.page_20;}
	else if (page === 21) {data = json_data.page_21;}
	else if (page === 22) {data = json_data.page_22;}
	else if (page === 23) {data = json_data.page_23;}
	else if (page === 24) {data = json_data.page_24;}
	else if (page === 25) {data = json_data.page_25;}
	else if (page === 26) {data = json_data.page_26;}
	else if (page === 27) {data = json_data.page_27;}
	else if (page === 28) {data = json_data.page_28;}
	else if (page === 29) {data = json_data.page_29;}
	else if (page === 30) {data = json_data.page_30;}
	else if (page === 31) {data = json_data.page_31;}
	else if (page === 32) {data = json_data.page_32;}
	else if (page === 33) {data = json_data.page_33;}
	else if (page === 34) {data = json_data.page_34;}
	else if (page === 35) {data = json_data.page_35;}
	else if (page === 36) {data = json_data.page_36;}
	else if (page === 37) {data = json_data.page_37;}
	else if (page === 38) {data = json_data.page_38;}
	else if (page === 39) {data = json_data.page_39;}
	else if (page === 40) {data = json_data.page_40;}
	else if (page === 41) {data = json_data.page_41;}
	else if (page === 42) {data = json_data.page_42;}
	else if (page === 43) {data = json_data.page_43;}
	else if (page === 44) {data = json_data.page_44;}
	else if (page === 45) {data = json_data.page_45;}
	else if (page === 46) {data = json_data.page_46;}
	else if (page === 47) {data = json_data.page_47;}
	else if (page === 48) {data = json_data.page_48;}
	else if (page === 49) {data = json_data.page_49;}
	else if (page === 50) {data = json_data.page_50;}
	else if (page === 51) {data = json_data.page_51;}
	else if (page === 52) {data = json_data.page_52;}
	else if (page === 53) {data = json_data.page_53;}
	else if (page === 54) {data = json_data.page_54;}
	else if (page === 55) {data = json_data.page_55;}
	else if (page === 56) {data = json_data.page_56;}
	else if (page === 57) {data = json_data.page_57;}
	else if (page === 58) {data = json_data.page_58;}
	else if (page === 59) {data = json_data.page_59;}
	else if (page === 60) {data = json_data.page_60;}
	else if (page === 61) {data = json_data.page_61;}
	else if (page === 62) {data = json_data.page_62;}
	else if (page === 63) {data = json_data.page_63;}
	else if (page === 64) {data = json_data.page_64;}
	else if (page === 65) {data = json_data.page_65;}
	else if (page === 66) {data = json_data.page_66;}
	else if (page === 67) {data = json_data.page_67;}
	else if (page === 68) {data = json_data.page_68;}
	else if (page === 69) {data = json_data.page_69;}
	else if (page === 70) {data = json_data.page_70;}
	else if (page === 71) {data = json_data.page_71;}
	else if (page === 72) {data = json_data.page_72;}
	else if (page === 73) {data = json_data.page_73;}
	else if (page === 74) {data = json_data.page_74;}
	else if (page === 75) {data = json_data.page_75;}
	else if (page === 76) {data = json_data.page_76;}
	else if (page === 77) {data = json_data.page_77;}
	else if (page === 78) {data = json_data.page_78;}
	else if (page === 79) {data = json_data.page_79;}
	else if (page === 80) {data = json_data.page_80;}
	else if (page === 81) {data = json_data.page_81;}
	else if (page === 82) {data = json_data.page_82;}
	else if (page === 83) {data = json_data.page_83;}
	else if (page === 84) {data = json_data.page_84;}
	else if (page === 85) {data = json_data.page_85;}
	else if (page === 86) {data = json_data.page_86;}
	else if (page === 87) {data = json_data.page_87;}
	else if (page === 88) {data = json_data.page_88;}
	else if (page === 89) {data = json_data.page_89;}
	else if (page === 90) {data = json_data.page_90;}
	else if (page === 91) {data = json_data.page_91;}
	else if (page === 92) {data = json_data.page_92;}
	else if (page === 93) {data = json_data.page_93;}
	else if (page === 94) {data = json_data.page_94;}
	else if (page === 95) {data = json_data.page_95;}
	else if (page === 96) {data = json_data.page_96;}
	else if (page === 97) {data = json_data.page_97;}
	else if (page === 98) {data = json_data.page_98;}
	else if (page === 99) {data = json_data.page_99;}
	else if (page === 100) {data = json_data.page_100;}

	return data;
}

function clearUnusedWowFields(numResults, numPerPage) {
	startIndex = Number(numResults);
	numPerPage = Number(numPerPage);

	if (startIndex < numPerPage) {
		for (var i = startIndex; i < numPerPage; i++) {
			var vari = String(i + 1);
			var number_id = 'm' + vari + '_number';
			var name_id = 'm' + vari + '_name';
			var clientID = 'm' + vari + '_clientID';
			var dob_id = 'm' + vari + '_dob';
			var photo_id = 'm' + vari + '_photo';
			var ref_id = 'm' + vari + '_ref';
			var l1 = 'clientLab' + vari;
			var l2 = 'dobLab' + vari;
			var l3 = 'refLab' + vari;
			var p = 'p' + vari;

			grab(number_id).innerHTML = '';
			grab(photo_id).src = '';
			grab(name_id).innerHTML = '';
			grab(clientID).innerHTML = '';
			grab(dob_id).innerHTML = '';
			grab(ref_id).innerHTML = '';
			grab(l1).innerHTML = '';
			grab(l2).innerHTML = '';
			grab(l3).innerHTML = '';
			grab(p).innerHTML = '';
		}
	}
}

function setEmptyImageFrame() {
	grab('test5').value = "In the empty frame function";
	// var numberResults = Number(grab('m_numMatches').value);

	// if (numberResults === 0) {
	// 	var div = grab('superWOWOverallMajorWrapper');
	// 	div.innerHTML = "Your search returned <span>0</span> matches"
	// }
}

function wowNameSort() {
	var j_data = grab('dataList');
	var aTag1 = grab('aTag1');
	var aTag2 = grab('aTag2');
	var sortOption = grab('sortOption');
	var sortOption2 = grab('sortOption2');

	if (String(j_data.value) === 'json_data') {
		j_data.value = 'json_fname';
		aTag1.href = "Javascript: prevWowPageResults({{json_fname}});";
		aTag2.href = "Javascript: nextWowPageResults({{json_fname}});";
		sortOption.href = "Javascript: wowSort({{json_fname}});";
	}
	else if (String(j_data.value) === 'json_fname') {
		j_data.value = 'json_data';
		aTag1.href = "Javascript: prevWowPageResults({{json_data}});";
		aTag2.href = "Javascript: nextWowPageResults({{json_data}});";
		sortOption.href = "Javascript: wowSort({{json_data}});";
	}
}

function wowSort(json_data) {
	var sorted = grab('sorted');
	var currentPage = Number(grab('current_page').value);

	if (String(sorted.value) === "ASC") {
		grab('sortOption').innerHTML = 'Sort Ascending'
		sorted.value = "DEC";
	}
	else if (String(sorted.value) === "DEC") {
		grab('sortOption').innerHTML = 'Sort Descending'
		sorted.value = "ASC";
	}

	loadWowResults(currentPage, json_data);
}

function reversePageElements(json_data) {
	var result = {};
	var forward = [];
	var backward = [];
	var numPages = Number(grab('m_numPages').value);
	var numMatches = Number(grab('m_numMatches').value);
	var reverseIndex = numMatches - 1;
	var forwardIndex = 0;
	var t = 0;

	for (var i = 1; i <= numPages; i++) {
		var p = getWowJsonArray(i, json_data);

		for (var j = 0; j < p.length; j++) {
			forward.push(p[j]);
		}
	}

	for (var d = 0; d < numMatches; d++) {
		backward.push(forward[reverseIndex]);
		reverseIndex = reverseIndex - 1;
	}

	for (var k = 1; k <= numPages; k++) {
		var n = getWowJsonArray(k, json_data);
		var len = n.length;
		var title = 'page_' + String(k);
		var temp = [];

		for (var l = 0; l < len; l++) {
			temp.push(backward[forwardIndex]);
			forwardIndex = forwardIndex + 1;
		}
		result[title] = temp;
	}

	return result;
}

function loadWowResults(page, json_data) {
	var sorted = String(grab('sorted').value);

	if (sorted === 'DEC') {
		json_data = reversePageElements(json_data);
	}

	var page = getWowJsonArray(page, json_data);
	var numElements = page.length;

	for (var i = 0; i < numElements; i++) {
		var vari = String(i + 1);
		var number_id = 'm' + vari + '_number';
		var name_id = 'm' + vari + '_name';
		var clientID = 'm' + vari + '_clientID';
		var dob_id = 'm' + vari + '_dob';
		var photo_id = 'm' + vari + '_photo';
		var ref_id = 'm' + vari + '_ref';
		var aTag = 'a' + vari;

		// grab(number_id).innerHTML = String(page[i]['number']) + '.';
		grab(photo_id).src = "/static/media/" + String(page[i]['photo']);
		grab(name_id).innerHTML = String(page[i]['lname']) + ', ' + String(page[i]['fname']);
		grab(clientID).innerHTML = page[i]['clientID'];
		grab(dob_id).innerHTML = page[i]['dob'];
		grab(ref_id).innerHTML = page[i]['ref'];
		grab(aTag).href = "Javascript: wowSelectSearchItem(\"" + String(page[i]['id']) + "\");";
	}

	clearUnusedWowFields(numElements, 8);
	setWowLabels(numElements);
}

function clearWowLabels() {
	for (var i = 1; i <= 8; i++) {
		var index = String(i);
		var l1 = 'clientLab' + index;
		var l2 = 'dobLab' + index;
		var l3 = 'refLab' + index;

		grab(l1).innerHTML = "";
		grab(l2).innerHTML = "";
		grab(l3).innerHTML = "";
	}
}

function setWowLabels(numResults) {
	numResults = Number(numResults);

	for (var i = 1; i <= numResults; i++) {
		var index = String(i);
		var l1 = 'clientLab' + index;
		var l2 = 'dobLab' + index;
		var l3 = 'refLab' + index;

		grab(l1).innerHTML = "Client ID:";
		grab(l2).innerHTML = "Date of Birth:";
		grab(l3).innerHTML = "Reason for Referral:";
	}
}

function buildTheWowImageDivs() {
	var html1 = "<img src=\"\" alt=\"client_img\" id=\"";
	var html2 = "\" class=\"wow-avatar-img\">";

	grab('p2').innerHTML = html1 + 'm2_photo' + html2;
	grab('p3').innerHTML = html1 + 'm3_photo' + html2;
	grab('p4').innerHTML = html1 + 'm4_photo' + html2;
	grab('p5').innerHTML = html1 + 'm5_photo' + html2;
	grab('p6').innerHTML = html1 + 'm6_photo' + html2;
	grab('p7').innerHTML = html1 + 'm7_photo' + html2;
	grab('p8').innerHTML = html1 + 'm8_photo' + html2;
	setWowLabels(8);
}

function prevWowPageResults(json_data) {
	var page = grab('current_page');

	if (Number(page.value) > 1) {
		buildTheWowImageDivs();
		var newPage = Number(page.value) - 1;
		page.value = newPage;
		loadWowResults(newPage, json_data);
		grab('currentPageDisp').innerHTML = newPage;
	}
}

function nextWowPageResults(json_data) {
	var numPages = Number(grab('m_numPages').value);
	var page = grab('current_page');

	if (Number(page.value) < numPages) {
		var newPage = Number(page.value) + 1;
		page.value = newPage;
		loadWowResults(newPage, json_data);
		grab('currentPageDisp').innerHTML = newPage;
	}
}

function phoneBuilderWow(divName) {
	divName = 'input_' + String(divName);
	var div = grab(divName);

	if (String(div.value).length === 1 && String(div.value.charAt(0)) !== "(") {
		var current = "(" + String(div.value);
			div.value = current;
	}

	if (String(div.value).length === 4) {
		var current2 = String(div.value) + ") ";
			div.value = current2;
	}

	if (String(div.value).length === 9) {
		var current3 = String(div.value) + "-";
			div.value = current3;
	}
}


function InitializeSuperWowResults(json_data) {
	var numberResults = String(grab('m_numMatches').value);

	if (numberResults === '0') {
		var div = grab('superWOWOverallMajorWrapperID');
		div.innerHTML = "<div class='fixThisInnerAlignWow'>Your search returned <span>0</span> results</div>"
		div.style.width = '95%';
		div.style.height = '70%';
		div.style.border = '1px solid gray';
		div.style.borderRadius = '5px';
		div.style.backgroundColor = "white";
	}
	else {
		loadWowResults(1, json_data);
		grab('currentPageDisp').innerHTML = 1;
	}	
}

function opacitizeImg(vari) {
	vari = String(vari);
	var imgName = 'm' + vari + '_photo';
	var titleName = 'm' + vari + '_name';
	var img = grab(imgName);
	var title = grab(titleName);

	img.style.opacity = '0.5';
	title.style.color = '#505cd8';
}

function depacitizeImg(vari) {
	vari = String(vari);
	var imgName = 'm' + vari + '_photo';
	var titleName = 'm' + vari + '_name';
	var img = grab(imgName);
	var title = grab(titleName);

	img.style.opacity = '1.0';
	title.style.color = '#824951';
}

function wowSelectSearchItem(clientID) {
	getPopParent('c2_id').value = clientID;
	getPopParent('c2Type').value = 'existing';
	var searchType = getPopParent('wowSelectSearchItem');
	var form = getPopParent('c_form');
	form.action = '/coupleSession/';
	form.submit();
	window.close();
}

function initializeWowSearch() {
	var searchVals 			= '';
	var fname 				= grab('fname').value;
	var lname 				= grab('lname').value;
	var ssn 				= grab('ss_num').value;
	var phone 				= grab('phone').value;
	var email 				= grab('email').value;
	var probationOfficer 	= grab('probationOfficer').value;
	var month 				= Number(grab('month').selectedIndex);
	var day 				= Number(grab('day').selectedIndex);
	var year 				= Number(grab('year').selectedIndex);
	var ref 				= Number(grab('ref').selectedIndex);

	if (searchClient_shouldSearchText(fname) === true) {searchVals += 'fname~';}
	if (searchClient_shouldSearchText(lname) === true) {searchVals += 'lname~';}
	if (searchClient_shouldSearchText(ssn) === true) {searchVals += 'ssn~';}
	if (searchClient_shouldSearchText(phone) === true) {searchVals += 'phone~';}
	if (searchClient_shouldSearchText(email) === true) {searchVals += 'email~';}
	if (searchClient_shouldSearchText(probationOfficer) === true) {searchVals += 'probationOfficer~';}
	if (month > 0) {searchVals += 'month~';}
	if (day > 0) {searchVals += 'day~';}
	if (year > 0) {searchVals += 'year~';}
	if (ref > 0) {searchVals += 'ref~';}

	if (month > 0 && day > 0 && year > 0) {
		grab('fullDOB').value = 'True';
	}
	else {
		grab('fullDOB').value = 'False';
	}

	var form = grab('c_form');
	form.action = "/wowSearchResults/";
	grab('searches').value = searchVals;
	grab('c_form').submit();

	var w = 800, h = 700;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	window.resizeTo(w, h);
	window.moveTo(l, t);
	window.focus();
}

function buildDropDayList(numDays) {
	numDays = Number(numDays);
	var currentIndex = grab('day').selectedIndex;
	var currentValue = Number(grab('day').value);
	var html = "<option value=\"0\">Day</option>";

	for (var i = 1; i <= numDays; i++) {
		html += "<option value=\"" + String(i) + "\">" + String(i) + "</option>";
	}

	grab('day').innerHTML = html;

	if (currentValue > numDays) {
		grab('day').selectedIndex = 0;
	}
	else {
		grab('day').selectedIndex = currentIndex;
	}
}

function addCoupleNote() {
	openPopUp('auto', '/coupleNoteDual/', 600, 410);
}


function initiateListBuilder(json_data) {
	var html = '';
	grab('totalNotes').value = json_data.length;

	for (var i = 0; i < json_data.length; i++) {
		var instance 	= Number(i + 1);
		var body 		= json_data[i]['bodyData'];
		var subject 	= json_data[i]['subject'];
		var flag 		= json_data[i]['flag'];
		var load 		= json_data[i]['load'];
		var the_id 		= json_data[i]['id']
		var hd = generateNoteHTML_couple(subject, body, flag, load, the_id, instance);
		html += String(hd['subjectHtml']);
		html += String(hd['bodyyHtml']);
		html += String(hd['saveFlag']);
		html += String(hd['load']);
		html += String(hd['id']);
	}

	grab('newNoteBuilder').innerHTML = html;
	html = '';

	for (var j = 0; j < json_data.length; j++) {
		var label = cleanCoupleNoteTitle(json_data[j]['subject']);
		var inst2 = Number(j + 1);
		html += String(generate_couple_display_select_html(label, inst2));
	}

	grab('selectListBuilder_c').innerHTML = html;
	grab('enterNumber').innerHTML = "(" + String(grab('totalNotes').value) + ")";

	// openPopUp('auto', '/errorLegend/', 400, 160);
	// createErrorWarning();
}

function createErrorWarning() {
	grab('paid_page_stuff_er').innerHTML = "WARNING";
	grab('errorBuilderMessage').innerHTML = "Do not refresh this page!";
	grab('cancelBtn').innerHTML = 'OK';
}


function generate_couple_display_select_html(subject, value) {
	var name = 'list_' + String(value);
	var realSubName = 'nnSubj_' + String(value);
	var realBodName = 'nnBody_' + String(value);
	var realSavName = 'saveNote_' + String(value);
	subject = String(subject);

	var html = "<a href=\"Javascript: retrieveNoteDynamically_couple(\'" + realSubName + "\', \'" + realBodName + "\' , \'" + realSavName + "\');\">";
	html += "<div class=\"noteItem_couple\" id=\"" + name + "\">&nbsp&nbsp&nbsp";
	html += subject;
	html += "</div></a>";

	return html;
}

function cleanCoupleNoteTitle(title) {
	title = String(title);
	var result = '';
	var len = title.length;

	if (25 <= len) {
		for (var i = 0; i < 25; i++) {
			result += title.charAt(i);
		}
		result += '...';
	}
	else {
		result = title;
	}
	return result;
}

function getCoupleSelectListTitles() {
	var totalNotes = Number(getPopParent('totalNotes').value);
	var results = [];
	var pre = 'nnSubj_';
	var loadPre = 'load_';

	for (var i = 1; i <= totalNotes; i++) {
		var loadID = loadPre + String(i);
		var load = String(getPopParent(loadID).value);

		if (load === "True") {
			var subjId = pre + String(i);
			var subject = String(getPopParent(subjId).value);
			var processed = cleanCoupleNoteTitle(subject);
			results.push(processed);
		}
	}

	return results;
}

function superCoupleSelectDisplayBuilder() {
	var titles = getCoupleSelectListTitles();
	var builder = getPopParent('selectListBuilder_c');
	var html = "";

	for (var i = 0; i < titles.length; i++) {
		var instance = i + 1;
		html += generate_couple_display_select_html(titles[i], instance);
	}
	builder.innerHTML = html;
}

function retrieveNoteDynamically_couple(subjectDivName, bodyDivName, flagDivName) {
	subjectDivName = String(subjectDivName);
	bodyDivName = String(bodyDivName);
	flagDivName = String(flagDivName);

	var subject = grab(subjectDivName).value;
	var body = grab(bodyDivName).value;
	var flag = grab(flagDivName).value;

	grab('newNoteSubject').value = subject;
	grab('newNoteBody').value = body;
	grab('newNoteFlag').value = flag;
	grab('selectedSubject').value = subjectDivName;
	grab('selectedBody').value = bodyDivName;
	grab('selectedFlag').value = flagDivName;

	openPopUp('auto', '/superNoteDisplyer/', 600, 410);
}

function initializeCoupleNoteEditor() {
	var processed = getPopParent('newNoteSubject').value;
	var subject = fetchTrueSubject(processed);
	var date = fetchTrueNoteDate(processed);
	var html = "<div><b>Date created: </b><em><span>" + date + "</span></em></div>";
	grab('editableDateDiv').innerHTML = html;
	grab('the_subject').innerHTML = subject;
	grab('the_body').innerHTML = getPopParent('newNoteBody').value;
}

function fetchTrueSubject(subject) {
	subject = String(subject);
	trueSubject = '';
	index = 0;

	for (var i = 0; i < subject.length; i++) {
		if (subject.charAt(i) === ' ') {
			index = i;
			break;
		}
	}

	index += 1;

	for (var j = index; j < subject.length; j++) {
		trueSubject += subject.charAt(j);
	}

	return trueSubject;
}

function fetchTrueNoteDate(subject) {
	subject = String(subject);
	var trueDate = null;
	var test = '';
	var index = 0;
	var mm = '';
	var dd = '';
	var yy = '';

	for (var apple = 0; apple < 5; apple++) {
		test += subject.charAt(apple);
	}

	if (test === 'Today') {
		var today = new Date()
		// mm = today.getMonth();
		// dd = today.getDay();
		mm = today.getMonth + 1;
		dd = today.getDay() + 1;
		yy = today.getFullYear();
	}
	else {
		for (var i = 0; i < subject.length; i++) {
			if (subject.charAt(i) !== "/") {
				mm += subject.charAt(i);
			}
			else {
				index = i + 1;
				break;
			}
		}

		for (var j = index; j < subject.length; j++) {
			if (subject.charAt(j) !== "/") {
				dd += subject.charAt(j);
			}
			else {
				index = j + 1;
				break;
			}
		}

		for (var k = index; k < index + 4; k++) {
			if (subject.charAt(j) !== ":") {
				yy += subject.charAt(k);
			}
		}
	}

	mm = Number(mm);

	if (mm === 1) {mm = 'January';}
	else if (mm === 2) {mm = 'February';}
	else if (mm === 3) {mm = 'March';}
	else if (mm === 4) {mm = 'April';}
	else if (mm === 5) {mm = 'May';}
	else if (mm === 6) {mm = 'June';}
	else if (mm === 7) {mm = 'July';}
	else if (mm === 8) {mm = 'August';}
	else if (mm === 9) {mm = 'September';}
	else if (mm === 10) {mm = 'October';}
	else if (mm === 11) {mm = 'November';}
	else {mm = 'December';}

	dd = String(dd);
	yy = String(yy);
	return mm + ' ' + dd + ', ' + yy;
}

function LoadTheDamnNoteData() {
	var processedSubject = String(getPopParent('newNoteSubject').value);
	var subject = fetchTrueSubject(processedSubject);
	grab('subject').value = subject;
	grab('c_body').innerHTML = getPopParent('newNoteBody').value;
}



function fetchTheDivLeadingNumber(SavName) {
	SavName = String(SavName);
	result = '';

	for (var i = 0; i < SavName.length; i++) {
		var c = SavName.charAt(i);

		if (c==='0' || c==='1' || c==='2' || c==='3' || c==='4' || c==='5' || c==='6' || c==='7' || c==='8' || c==='9') {
			result += c;
		}
	}
	return Number(result);
}

function theOnlyNoteErrorChecker() {
	hasErrors = false;
	var subjectDiv = grab('subject');
	var bodyDiv = grab('c_body');
	var subVal = String(subjectDiv.value);
	var bodVal = String(bodyDiv.value);

	if (subVal.length === 0) {
		hasErrors = true;
		subjectDiv.style.border = '1px solid red';
	}

	if (bodVal.length === 0) {
		hasErrors = true;
		bodyDiv.style.border = '1px solid red';
	}

	return hasErrors;
}

function superBorderToGray(divName) {	
	divname = String(divname);
	var div = grab(divname);
}

function coupleNoteErase() {
	var flagName = String(getPopParent('selectedFlag').value);
	getPopParent(flagName).value = "False";
	//Handle the number added if needed
	var numberLoadedNotes = Number(getPopParent('numberLoadedNotes').value);
	var leadingNumber = fetchTheDivLeadingNumber(flagName);
	var loadName = "load_" + String(leadingNumber);
	getPopParent(loadName).value = "False";

	var currentDeletes = String(getPopParent('delete_ids').value);
	var del_id = "theId_" + String(leadingNumber);
	var addToDeleteList = String(getPopParent(del_id).value);
	var newDelList = currentDeletes + addToDeleteList + '~';
	getPopParent('delete_ids').value = newDelList;

	if (leadingNumber > numberLoadedNotes) {
		var addedDiv = getPopParent('numberAdded');
		var newAdded = Number(addedDiv.value) - 1;
		addedDiv.value = newAdded;
	}

	superCoupleSelectDisplayBuilder();
	window.close();
}

function getNewNoteList() {
	var newSubject 		= grab('subject');
	var newBody 		= grab('c_body');
	var numAdded 		= getPopParent('numberAdded');
	var totalNotes 		= Number(getPopParent('totalNotes').value);
	var notes 			= [];

	var newData 		= {}
	newData['subject'] 	= "Today: " + String(newSubject.value);
	newData['body'] 	= newBody.value;
	newData['flag'] 	= "True";
	newData['load'] 	= "True";
	newData['id'] 		= "no_id";
	notes.push(newData);

	for (var i = 1; i <= totalNotes; i++) {
		var subjName 	= "nnSubj_" + String(i);
		var bodyName 	= "nnBody_" + String(i);
		var saveName 	= "saveNote_" + String(i);
		var loadName 	= "load_" + String(i);
		var noteID 		= "theId_" + String(i);
		var data 		= {}

		data['subject'] = String(getPopParent(subjName).value);
		data['body'] 	= String(getPopParent(bodyName).value);
		data['flag'] 	= String(getPopParent(saveName).value);
		data['load'] 	= String(getPopParent(loadName).value);
		data['id'] 		= String(getPopParent(noteID).value);

		notes.push(data);
	}

	var created = Number(numAdded.value);
	created = created + 1;
	numAdded.value = created;
	getPopParent('totalNotes').value = notes.length;
	return notes;
}

function generateNoteHTML_couple(subject, body, flag, load, the_id, noteInstance) {
	var result 		= {};
	subject 		= String(subject);
	body 			= String(body);
	flag 			= String(flag);
	load 			= String(load);
	the_id 			= String(the_id)
	noteInstance 	= String(noteInstance);

	var subjId = "nnSubj_" + noteInstance;
	var bodyId = "nnBody_" + noteInstance;
	var saveId = "saveNote_" + noteInstance;
	var loadId = "load_" + noteInstance;
	var noteId = "theId_" + noteInstance;

	var subInput = "<input type=\"hidden\" name=\"" + subjId + "\" ";
	subInput += "id=\"" + subjId + "\" value=\"" + subject + "\">";

	var bodInput = "<input type=\"hidden\" name=\"" + bodyId + "\" ";
	bodInput += "id=\"" + bodyId + "\" value=\"" + body + "\">";

	var saveFlag = "<input type=\"hidden\" name=\"" + saveId + "\" ";
	saveFlag += "id=\"" + saveId + "\" value=\"" + flag + "\">";

	var loadFlag = "<input type=\"hidden\" name=\"" + loadId + "\" ";
	loadFlag += "id=\"" + loadId + "\" value=\"" + load + "\">";

	var id_input = "<input type=\"hidden\" name=\"" + noteId + "\" ";
	id_input += "id=\"" + noteId + "\" value=\"" + the_id + "\">";

	result['subjectHtml'] 	= subInput;
	result['bodyyHtml'] 	= bodInput;
	result['saveFlag'] 		= saveFlag;
	result['load'] 			= loadFlag;
	result['id'] 			= id_input;

	return result;
}

function softSaveNote() {
	if (theOnlyNoteErrorChecker() === true) {
		openPopUp('auto', '/blankOnlyErrorHighlighted/', 400, 160);
	}
	else {
		var html 		= "";
		var builder 	= getPopParent('newNoteBuilder');
		var newNotes 	= getNewNoteList();
		var len = Number(newNotes.length);

		for (var i = 0; i < len; i++) {
			var instance = i + 1;
			var data = generateNoteHTML_couple(newNotes[i]['subject'], newNotes[i]['body'], newNotes[i]['flag'], newNotes[i]['load'], newNotes[i]['id'], instance);
			html += data['subjectHtml'];
			html += data['bodyyHtml'];
			html += data['saveFlag'];
			html += data['load'];
			html += data['id'];
		}

		builder.innerHTML = html;
		superCoupleSelectDisplayBuilder();
		window.close();
	}
}

function clearRedErrorBorders(divname) {
	divname = String(divname);
	grab(divname).style.border = '1px solid gray';
}

function superCoupleSaveEditor() {
	if (theOnlyNoteErrorChecker() === true) {
		openPopUp('auto', '/blankOnlyErrorHighlighted/', 400, 160);
	}
	else {
		var SubName = String(getPopParent('selectedSubject').value);
		var BodName = String(getPopParent('selectedBody').value);
		var SavName = String(getPopParent('selectedFlag').value);

		getPopParent(SubName).value = grab('subject').value;
		getPopParent(BodName).value = grab('c_body').value;
		getPopParent(SavName).value = "True";

		window.close();
	}
}

function a_imgOpacLo(divName, opacityLevel) {
	divname = String(divname);
	opacityLevel = String(opacityLevel);
	var div = grab(divname);
	div.style.opacity = opacityLevel;
}

function a_imgOpacHi(divName) {
	divname = String(divname);
	var div = grab(divname);
	div.innerHTML = "";
	// div.style.opacity = '1.0';
}

function couple_to_optionsSTUFF() {
	var form = grab('c_form');
	form.action = "/uni_generic_exit/";
	form.submit();
}

function exit_to_home_CoupleSession() {
	var form = grab('c_form');
	form.action = "/clientOptions/";
	form.submit();
}

function viewClient1Profile_couple() {
	openPopUp('auto', '/viewFullProfile_primary/', 500, 560);
}

function viewClient2Profile_couple() {
	openPopUp('auto', '/viewFullProfile_secondary/', 500, 560);
}

function cp_hoverA(clientOption) {
	var img = null;
	var bkg = null;
	clientOption = String(clientOption);

	if (clientOption === 'p') {
		img = grab('imgP');
		bkg = grab('bkgP');
	}
	else if (clientOption === 's') {
		img = grab('imgS');
		bkg = grab('bkgS');
	}

	img.style.opacity = '0.7';
	bkg.style.backgroundColor = '#d3cfc3';
	// bkg.style.backgroundColor = '#c0bfc0';
}

function cp_hoverB(clientOption) {
	var img = null;
	var bkg = null;
	clientOption = String(clientOption);

	if (clientOption === 'p') {
		img = grab('imgP');
		bkg = grab('bkgP');
	}
	else if (clientOption === 's') {
		img = grab('imgS');
		bkg = grab('bkgS');
	}

	img.style.opacity = '1.0';
	bkg.style.backgroundColor = '#c0c9c7';
}


function superNoteInit() {
	// var frame = grab('noteFrame');
	// var json_data = json_decode(grab('allNotes'));

	var arrFrames = String(parent.grab("allNotes").value);
	getDictStringThing(arrFrames);

	// grab('noteList').innerHTML = l1;

}

function populateDropDownDay(sType) {
	sType = String(sType);

	if (sType === 'month') {grab('month').style.border = '';}
	else if (sType === 'day') {grab('day').style.border = '';}
	else {grab('year').style.border = '';}

	var mm = String(grab('month').value);
	var dd = grab('')
	var html = '';
	
	if (mm === '4' || mm === '6' || mm === '9' || mm === '11') {
		buildDropDayList(30);
	}
	else if (mm !== '2') {
		buildDropDayList(31);
	}
	else {
		buildDropDayList(28);
		var yy = grab('year');

		if (Number(yy.value) % 4 == 0 && yy.selectedIndex !== 0) {
			buildDropDayList(29)
		}
	}

	dd.innerHTML = html;
}

function newClient_hasErrors() {
	var hasErrors = false;
	var textError = newClient_hasTextError();
	var sError = newClient_hasSelectErrors();

	if (textError === true || sError === true) {
		hasErrors = true;
	}
	return hasErrors;
}

function clearNC(divname) {
	divName = String(divname);
	var div = grab(divName);
	div.style.border = '';
}

function clearNCS(divName) {
	divName = String(divName);
	var div = grab(divName);
	div.style.border = '';
}


function newClient_hasTextError() {
	var textList = [];
	var hasErrors = false;

	textList.push(grab('fname'));
	textList.push(grab('lname'));
	textList.push(grab('street_no'));
	textList.push(grab('street_name'));
	textList.push(grab('city'));
	textList.push(grab('emer_contact_name'));

	for (var i = 0; i < textList.length; i++) {
		var temp = clearWhiteSpace(textList[i].value);

		if (isBlankText(temp) === true) {
			hasErrors = true;
			textList[i].style.border = "2px solid red";
		}
	}

	return hasErrors;
}

function newClient_hasSelectErrors() {
	var s_list = [];
	var hasErrors = false;

	s_list.push(grab('state'));
	s_list.push(grab('month'));
	s_list.push(grab('day'));
	s_list.push(grab('year'));
	s_list.push(grab('reason_ref'));

	for (var i = 0; i < s_list.length; i++) {
		if (s_list[i].selectedIndex === 0) {
			hasErrors = true;
			s_list[i].style.border = "1px solid orange";
		}
	}

	return hasErrors;
}


function newClient_fetchTextErrors() {
	var textList = [];

	textList.push(grab('fname'));
	textList.push(grab('lname'));
	textList.push(grab('street_no'));
	textList.push(grab('street_name'));
	textList.push(grab('city'));
	textList.push(grab('zip_code'));
	textList.push(grab('ss_num'));
	textList.push(grab('phone'));
	textList.push(grab('emer_contact_name'));
	textList.push(grab('emer_phone'));

	for (var i = 0; i < textList.length; i++) {
		var temp = clearWhiteSpace(textList[i].value);

		if (isBlankText(temp) === true) {
			textList[i].style.border = "2px solid red";
		}
	}
}

function newClient_fetchSelectErrors() {
	var sList = [];

	sList.push(grab('state'));
	sList.push(grab('month'));
	sList.push(grab('day'));
	sList.push(grab('year'));
	sList.push(grab('reason_ref'));

	for (var i = 0; i < sList.length; i++) {
		index = Number(sList[i].selectedIndex);

		if (index === 0) {
			sList[i].style.border = "1px solid orange";
		}
	}
}

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

function uniClientSearchF(sType) {
	var w = 400, h = 510;
	sType = String(sType);
	grab('cSearch').value = sType;
	openPopUp('auto', '/uniClientSearch/',w, h);
}

function snagCurrentDate() {
	var date = {};
	var today = new Date();
	date['day'] = today.getDate();
	date['month'] = today.getMonth() + 1;
	date['year'] = today.getFullYear();
	return date;
}

function fetchADate(yy, mm, dd) {
	var date = {};
	var the_date = new Date(yy, mm, dd);
	date['day'] = the_date.getDate();
	date['month'] = the_date.getMonth();
	date['year'] = the_date.getFullYear();
	return date;
}

function snagNumDays(month, year) {
	month = Number(month);
	year = Number(year);
	var days = 0;

	if (month === 2) {
		if ((year % 4) === 0) {
			days = 29;
		}
		else {
			days = 28;
		}
	}

	else if (month === 4 || month === 6 || month === 9 || month === 11) {
		days = 30;
	}

	else {
		days = 31;
	}
	return days;
}

function snagFirstDayOfWeek(mm, yy) {
	mm = mm - 1;
	var date = new Date(yy, mm, 1);
	var firstDay = date.getDay();
	return firstDay;
}

function snagLastDayOfWeek(mm, yy) {
	var lastDay = 0;
	var dd = snagNumDays(mm, yy);
	mm = mm - 1;
	var date = new Date(yy, mm, dd);
	lastDay = date.getDay();
	return lastDay;
}

function isCompleteWeekFirst(dayOfWeek) {
	var isComplete = false;
	dayOfWeek = Number(dayOfWeek);
	if (dayOfWeek === 0) {
		isComplete = true;
	}
	return isComplete;
}

function isCompleteWeekLast(dayOfWeek) {
	var isComplete = false;
	dayOfWeek = Number(dayOfWeek);
	if (dayOfWeek === 6) {
		isComplete = true;
	}
	return isComplete;
}

function fetchNumberWeeks(date) {
	var week = 1;
	var firstDay = snagFirstDayOfWeek(date['month'], date['year']);
	var numDays = snagNumDays(date['month'], date['year']);

	if (firstDay === 0) {
		week = 0;
	}

	for (var i = 0; i < numDays; i++) {
		firstDay += 1;

		if (firstDay === 7) {
			week += 1;
			firstDay = 0;
		}
	}
	return week;
}

function fetchWeekDivs(weeks) {
	result = []
	var pre = 'week';

	for (var i = 1; i <= weeks; i++) {
		var temp = pre + String(i);
		result.push(temp);
	}
	return result;
}

function previousMonth(mm, yy) {
	var result = [];
	var firstDay = snagFirstDayOfWeek(mm, yy);
	var lastDay = snagNumDays(mm, yy);
	var the_id = null, the_class = 'prevMonth';
	var test = '';

	if (mm === 1) {
		mm = 12
		yy = yy - 1;
	}
	else {
		mm = mm - 1;
	}

	var prevLastDay = snagNumDays(mm, yy);
	var start = prevLastDay - firstDay + 1;

	for (var i = start; i <= prevLastDay; i++) {
		data = {};
		the_id = String(yy) + '-' + String(mm) + '-' + String(i);

		data['id'] = the_id;
		data['class'] = the_class;
		data['day'] = i;
		result.push(data);
	}

	return result;
}

function nextMonth(mm, yy) {
	var result = [];
	var lastDayMonth = snagNumDays(mm, yy);
	var lastWeekDay = snagLastDayOfWeek(mm, yy);
	var the_class = 'nextMonth', the_id = null;

	mm += 1;

	if (mm === 13) {
		mm = 1;
		yy += 1;
	}

	for (var i = 1; i <= (6 - lastWeekDay); i++) {
		data = {};
		the_id = String(yy) + '-' + String(mm) + '-' + String(i);

		data['id'] = the_id;
		data['class'] = the_class;
		data['day'] = i;
		result.push(data);
	}

	return result;
}

function setNewWeek(calData) {
	var dayDiv = 'dayDiv';
	var startDiv = 'startDiv';
	var endDiv = 'endDiv';
	var inst = 0;

	for (var i = 0; i < calData.length; i++) {
		if ((i % 7) === 0) {
			calData[i]['newWeek'] = true;
		}
		else {
			calData[i]['newWeek'] = false;
		}

		inst = i + 1;
		inst = String(inst);
		calData[i]['startDiv'] = startDiv + inst;
		calData[i]['endDiv'] = endDiv + inst;
	}
}


function getCalendarData(yy, mm, dd) {
	var calData = [];
	var p_month = null, n_month = null;
	var today = fetchADate(yy, mm, dd);
	var numDays = snagNumDays(today['month'], today['year']);
	var firstDay = snagFirstDayOfWeek(today['month'], today['year']);
	var lastDay = snagLastDayOfWeek(today['month'], today['year']);
	var sep = '-';

	if (isCompleteWeekFirst(firstDay) === false) {
		p_month = previousMonth(today['month'], today['year']);

		for (var i = 0; i < p_month.length; i ++) {
			calData.push(p_month[i]);
		}
	}

	for (var j = 1; j <= numDays; j++) {
		data = {};
		data['id'] = String(yy) + sep + String(mm) + sep + String(j);
		data['day'] = j;

		if (today['year'] === yy && today['month'] === mm && today['day'] === j) {
			data['class'] = 'thisDay';
		}
		else if (today['day'] > j) {
			data['class'] = 'prevMonth';
		}
		else {
			data['class'] = 'normalDay';
		}

		calData.push(data);
	}

	if (isCompleteWeekLast(lastDay) === false) {
		n_month = nextMonth(today['month'], today['year']);

		for (var k = 0; k < n_month.length; k ++) {
			calData.push(n_month[k]);
		}
	}

	setNewWeek(calData);

	return calData;
}

function printJSMonth(month, year) {
	month = Number(month);
	mm = null;

	if (month === 1) {
		mm = 'January';
	}
	else if (month === 2) {
		mm = 'February';
	}
	else if (month === 3) {
		mm = 'March';
	}
	else if (month === 4) {
		mm = 'April';
	}
	else if (month === 5) {
		mm = 'May';
	}
	else if (month === 6) {
		mm = 'June';
	}
	else if (month === 7) {
		mm = 'July';
	}
	else if (month === 8) {
		mm = 'August';
	}
	else if (month === 9) {
		mm = 'September';
	}
	else if (month === 10) {
		mm = 'October';
	}
	else if (month === 11) {
		mm = 'November';
	}
	else if (month === 12) {
		mm = 'December';
	}

	return mm + ' ' + String(year);
}

function superJSdate(mm, dd, yy) {
	mm = Number(mm);
	month = null;

	if (mm === 1) {
		month = 'January';
	}
	else if (mm === 2) {
		month = 'February';
	}
	else if (mm === 3) {
		month = 'March';
	}
	else if (mm === 4) {
		month = 'April';
	}
	else if (mm === 5) {
		month = 'May';
	}
	else if (mm === 6) {
		month = 'June';
	}
	else if (mm === 7) {
		month = 'July';
	}
	else if (mm === 8) {
		month = 'August';
	}
	else if (mm === 9) {
		month = 'September';
	}
	else if (mm === 10) {
		month = 'October';
	}
	else if (mm === 11) {
		month = 'November';
	}
	else if (mm === 12) {
		month = 'December';
	}
	return month + ' ' + String(dd) + ', ' + String(yy);
}

function buildCalendarHead(month, year) {
	var head = printJSMonth(month, year);
	grab('cal_tot_head').innerHTML = head;
}

function buildCalendarCell(class_id, date_id, day, start_id, end_id) {
	var html = "<td class='" + class_id + "'>\
	<a href='javascript: workDateSelector(" + day + ")'>\
	<div id='" + date_id + "' class='dayDiv'>" + day + "</div>\
	<div id='" + start_id + "' class='startDiv'></div>\
	<div id='" + end_id + "' class='endDiv'></div>\
	</a>\
	</td>";

	return html;
}

function workDateSelector(day) {
	grab('selected_date').value = day;
	var w = 600, h = 300;
	openPopUp('auto', '/workDateSelector/', w, h);
}

function init_wd_selector() {
	var date = null;
	var year = getPopParent('year').value;
	var month = getPopParent('month').value;
	var day = getPopParent('selected_date').value;
	day = Number(day);
	date = superJSdate(month, day, year);

	grab('day').value = day;
	grab('month').value = month;
	grab('year').value = year;
	day += 1;
	grab('start').value = 'startDiv' + String(day);
	grab('end').value = 'endDiv' + String(day);
	grab('wk_date').innerHTML = date;
}

function force_a_hour() {
	var s = grab('start_s');
	var e = grab('end_s');
	var s_sel = s.selectedIndex;
	var e_sel = e.selectedIndex;
	var diff = e_sel - s_sel;

	if (diff <= 4) {
		e.selectedIndex = (s.selectedIndex + 4);
	}
}

function loadWorkFields(data) {
	var curr_mm = grab('month').value;
	var curr_yy = grab('year').value;

	curr_mm = Number(curr_mm);
	curr_yy = Number(curr_yy);

	var len = data.length;

	for (var i = 0; i < len; i++) {
		var mm = Number(data[i].month);
		var yy = Number(data[i].year);

		if (curr_mm === mm && curr_yy === yy) {
			var start_id 	= String(data[i].start_id);
			var start_val 	= String(data[i].start_val);
			var end_id 		= String(data[i].end_id);
			var end_val 	= String(data[i].end_val);

			var html1 = "<span id='in_cal'>IN: </span>" + start_val;
			var html2 = "<span id='in_cal'>OUT: </span>" + end_val;

			grab(start_id).innerHTML 	= html1;
			grab(end_id).innerHTML 		= html2;
		}
	}
}

function pre_save_sch() {
	var saveThisHtml = getPopParent('saveThis').innerHTML;
	var numSaved = getPopParent('numSaved').value;
	numSaved = Number(numSaved) + 1;
	var day = String(grab('day').value);
	var month = String(grab('month').value);
	var year = String(grab('year').value);
	var dddd = month + '/' + day + '/' + year
	var newID = 'save' + String(numSaved);
	var newEntry = dddd + '/' + '@' + String(grab('start_s').value) + '-' + String(grab('end_s').value);
	var html = "<input type='hidden' name='" + newID + "' id='" + newID + "' value='" + newEntry + "'>";
	
	if (saveThisHtml !== '' || saveThisHtml !== ' ' || saveThisHtml !== 'null' || saveThisHtml !== 'None') {
		saveThisHtml += html;
	}
	else {
		saveThisHtml = html;
	}

	getPopParent('saveThis').innerHTML = saveThisHtml;
	getPopParent('numSaved').value = numSaved;

	loadNewScheduleDate(newEntry);
	window.close();
}

function loadNewScheduleDate(value) {
	var start = snagSavedStart(value);
	var end = snagSavedEnd(value);

	var s_div = String(grab('start').value);
	var e_div = String(grab('end').value);

	getPopParent(s_div).innerHTML = '';
	getPopParent(e_div).innerHTML = '';
	getPopParent(s_div).innerHTML = "<span id='in_cal'>IN: </span>" + start;
	getPopParent(e_div).innerHTML = "<span id='in_cal'>OUT: </span>" + end;
}

function save_curr_calendar() {
	grab('c_form').submit();
}

function getRowStartIndex(row) {
	var index = 0;
	row = Number(row);
	index = (row * 7) - 7;
	return index;
}

function buildCalendarRow(week_id, data) {
	week_id = String(week_id);
	row = week_id.charAt(4);
	row = Number(row);
	var start = getRowStartIndex(row);
	var end = start + 7;
	var html = '';

	for (var i = start; i < end; i++) {
		html += buildCalendarCell(data[i]['class'], data[i]['id'], data[i]['day'], data[i]['startDiv'], data[i]['endDiv']);
	}

	grab(week_id).innerHTML = html;
}

function buildCalendar(date, weekList, data) {
	var week_id = '';
	buildCalendarHead(date['month'], date['year']);

	for (var i = 0; i < weekList.length; i++) {
		buildCalendarRow(weekList[i], data);
	}
}

function init_calendar() {
	var today = snagCurrentDate();
	var data = getCalendarData(today['year'], today['month'], today['day']);
	var weeks = fetchNumberWeeks(today);
	var weekList = fetchWeekDivs(weeks);

	clearWeeks();
	buildCalendar(today, weekList, data);

	grab('month').value = today['month'];
	grab('year').value = today['year']
	grab('numSaved').value = '0';
}

function cal_prevOn() {
	grab('cal_prevBtn').src = '/static/images/left_sOver.png';
	grab('cal_prevBtn').style.opacity = '0.8';
}

function cal_prevOff() {
	grab('cal_prevBtn').src = '/static/images/left_s.png';
	grab('cal_prevBtn').style.opacity = '1.0';
}

function cal_nextOn() {
	grab('cal_nextBtn').src = '/static/images/right_sOver.png';
	grab('cal_nextBtn').style.opacity = '0.8';
}

function cal_nextOff() {
	grab('cal_nextBtn').src = '/static/images/right_s.png';
	grab('cal_nextBtn').style.opacity = '1.0';
}

function nextMonthPayload() {
	var date = null;
	var mm = grab('month').value;
	var yy = grab('year').value;

	mm = Number(mm);
	yy = Number(yy);

	mm += 1;

	if (mm === 13) {
		mm = 1;
		yy += 1;
	}

	clearWeeks();
	today = snagCurrentDate();

	if (today['month'] === mm && today['year'] === yy) {
		date = today;
	}
	else {
		date = fetchADate(yy, mm, 1);
	}

	var data = getCalendarData(date['year'], date['month'], date['day']);
	var weeks = fetchNumberWeeks(date);
	var weekList = fetchWeekDivs(weeks);

	buildCalendar(date, weekList, data);

	grab('month').value = date['month'];
	grab('year').value = date['year']
}

function clearWeeks() {
	grab('week1').innerHTML = '';
	grab('week2').innerHTML = '';
	grab('week3').innerHTML = '';
	grab('week4').innerHTML = '';
	grab('week5').innerHTML = '';
	grab('week6').innerHTML = '';
	grab('week7').innerHTML = '';
	grab('week8').innerHTML = '';
}

function prevMonthPayload() {
	var mm = grab('month').value;
	var yy = grab('year').value;
	var date = null;

	mm = Number(mm);
	yy = Number(yy);

	mm -= 1;

	if (mm === 0) {
		mm = 12;
		yy -= 1;
	}

	clearWeeks();
	today = snagCurrentDate();

	if (today['month'] === mm && today['year'] === yy) {
		date = today;
	}
	else {
		date = fetchADate(yy, mm, 1);
	}

	var data = getCalendarData(date['year'], date['month'], date['day']);
	var weeks = fetchNumberWeeks(date);
	var weekList = fetchWeekDivs(weeks);

	buildCalendar(date, weekList, data);

	grab('month').value = date['month'];
	grab('year').value = date['year']
}

function backToClientSearch() {
	grab('b_form').submit();
	var w = 400, h = 530;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	window.resizeTo(w, h);
	window.moveTo(l, t);
	window.focus();
}

function uniFormSearchF() {
	var w = 400, h = 500;
	openPopUp('auto', '/uniFormSearch/',w, h);
}

function getClientSearchStuff() {
	var image = null;
	var sType = getPopParent('cSearch').value;
	sType = String(sType);
	
	if (sType === 'session') {
		image = '/static/images/new_images/session.png';
		header = 'Client Session'
		grab('sImage').src = image
		grab('sImage').className = 'popSearchClientSession';
		grab('sTypeText').innerHTML = 'Begin Client Session';
	}
	else if (sType === 'general') {
		image = '/static/images/new_images/searchClient.png';
		header = 'Client Database'
		grab('sImage').src = image
		grab('sImage').className = 'popSearchClientGeneral';
		grab('sTypeText').innerHTML = 'Search Client Database';
	}

	grab('useDischarged').value = grab('incD').value;
	grab('header').value = header;
	grab('image').value = image;
	grab('cSearch').value = sType;
}

function setClientSearchCheck() {
	var box = grab('incD');

	if (incD.checked === true) {
		incD.value = 'True';
	}
	else {
		incD.value = 'False';
	}
}

function submit_uniClientSearch() {
	var w = 600, h = 665;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	grab('sc_form').action = '/clientSearchResults/';
	grab('sc_form').submit();

	window.resizeTo(w, h);
	window.moveTo(l, t);
    window.focus(); 
}

function grabResultPage(pageNum, json_data) {
	var result = null;
	pageNum = Number(pageNum);
	if (pageNum === 1) {result = json_data.page1;}
	else if (pageNum === 2) {result = json_data.page2;}
	else if (pageNum === 3) {result = json_data.page3;}
	else if (pageNum === 4) {result = json_data.page4;}
	else if (pageNum === 5) {result = json_data.page5;}
	else if (pageNum === 6) {result = json_data.page6;}
	else if (pageNum === 7) {result = json_data.page7;}
	else if (pageNum === 8) {result = json_data.page8;}
	else if (pageNum === 9) {result = json_data.page9;}
	else if (pageNum === 10) {result = json_data.page10;}
	else if (pageNum === 11) {result = json_data.page11;}
	else if (pageNum === 12) {result = json_data.page12;}
	else if (pageNum === 13) {result = json_data.page13;}
	else if (pageNum === 14) {result = json_data.page14;}
	else if (pageNum === 15) {result = json_data.page15;}
	else if (pageNum === 16) {result = json_data.page16;}
	else if (pageNum === 17) {result = json_data.page17;}
	else if (pageNum === 18) {result = json_data.page18;}
	else if (pageNum === 19) {result = json_data.page19;}
	else if (pageNum === 20) {result = json_data.page20;}
	else if (pageNum === 21) {result = json_data.page21;}
	else if (pageNum === 22) {result = json_data.page22;}
	else if (pageNum === 23) {result = json_data.page23;}
	else if (pageNum === 24) {result = json_data.page24;}
	else if (pageNum === 25) {result = json_data.page25;}
	else if (pageNum === 26) {result = json_data.page26;}
	else if (pageNum === 27) {result = json_data.page27;}
	else if (pageNum === 28) {result = json_data.page28;}
	else if (pageNum === 29) {result = json_data.page29;}
	else if (pageNum === 30) {result = json_data.page30;}
	else if (pageNum === 31) {result = json_data.page31;}
	else if (pageNum === 32) {result = json_data.page32;}
	else if (pageNum === 33) {result = json_data.page33;}
	else if (pageNum === 34) {result = json_data.page34;}
	else if (pageNum === 35) {result = json_data.page35;}
	else if (pageNum === 36) {result = json_data.page36;}
	else if (pageNum === 37) {result = json_data.page37;}
	else if (pageNum === 38) {result = json_data.page38;}
	else if (pageNum === 39) {result = json_data.page39;}
	else if (pageNum === 40) {result = json_data.page40;}
	else if (pageNum === 41) {result = json_data.page41;}
	else if (pageNum === 42) {result = json_data.page42;}
	else if (pageNum === 43) {result = json_data.page43;}
	else if (pageNum === 44) {result = json_data.page44;}
	else if (pageNum === 45) {result = json_data.page45;}
	else if (pageNum === 46) {result = json_data.page46;}
	else if (pageNum === 47) {result = json_data.page47;}
	else if (pageNum === 48) {result = json_data.page48;}
	else if (pageNum === 49) {result = json_data.page49;}
	else if (pageNum === 50) {result = json_data.page50;}
	return result;
}

function grabPhoto(slot, displayPosition) {
	var result = null;
	var photo = '/static/media/';
	displayPosition = Number(displayPosition);

	if (displayPosition === 1) {result = slot.photo1;}
	else if (displayPosition === 2) {result = slot.photo2;}
	else if (displayPosition === 3) {result = slot.photo3;}
	else if (displayPosition === 4) {result = slot.photo4;}
	else if (displayPosition === 5) {result = slot.photo5;}
	else if (displayPosition === 6) {result = slot.photo6;}
	else if (displayPosition === 7) {result = slot.photo7;}
	else if (displayPosition === 8) {result = slot.photo8;}
	else if (displayPosition === 9) {result = slot.photo9;}
	else if (displayPosition === 10) {result = slot.photo10;}
	photo += String(result);
	return photo;
}

function superResultsPage(pageNum, numOnPage, json_data) {
	pageNum 	= Number(pageNum);
	numOnPage 	= Number(numOnPage);
	

	thisPage = grabResultPage(pageNum, json_data);

	for (var i = 0; i < numOnPage; i++) {
		var preURL = '/static/media/';

		grabThis 		= i + 1;
		tag_name 		= 'c_name' + String(grabThis);
		tag_ssn 		= 'c_ssn' + String(grabThis);
		tag_dob 		= 'c_dob' + String(grabThis);
		tag_phone 		= 'c_phone' + String(grabThis);
		tag_photo 		= 'c_photo' + String(grabThis);
		tag_clientID 	= 'c_clientID' + String(grabThis);
		tag_number		= 'c_number' + String(grabThis);
		tag_id 			= 'c_id' + String(grabThis);
		tag_session 	= 'hasSession' + String(grabThis);
		tag_s_id 		= 'session_id' + String(grabThis);

		grab(tag_id).value 			= thisPage[i].c_id;
		grab(tag_s_id).value 		= thisPage[i].session_id;
		grab(tag_session).value 	= thisPage[i].hasSession;
		grab(tag_number).innerHTML	= thisPage[i].c_number;
		grab(tag_name).innerHTML 	= thisPage[i].c_name;
		grab(tag_ssn).innerHTML 	= thisPage[i].c_ssn;
		grab(tag_dob).innerHTML 	= thisPage[i].c_dob;
		grab(tag_phone).innerHTML 	= thisPage[i].c_phone;
		grab(tag_photo).src 		= preURL + String(thisPage[i].c_photo);
		// grab(tag_clientID).innerHTML = thisPage[i].c_name;
	}
}

function initialize_clientResults(json_data) {
	var numOnPage = grab('pageOne').value;
	numOnPage = Number(numOnPage);
	grab('pageNumber').value = 1;

	superResultsPage(1, numOnPage, json_data);

	setPrevResultBtn();
	setNextResultBtn();
}

function prevResultHover() {
	grab('nextArrowLeft').src = '/static/images/nextLeftHover.png';
}

function prevResultOff() {
	grab('nextArrowLeft').src = '/static/images/nextLeftshort.png';
}

function nextResultHover() {
	grab('nextArrowRight').src = '/static/images/nextRightHover.png';
}

function nextResultOff() {
	grab('nextArrowRight').src = '/static/images/nextRightshort.png';
}

function setPrevResultBtn() {
	var btn = grab('nextArrowLeft');
	var currentPage = grab('pageNumber').value;
	currentPage = Number(currentPage);

	if (currentPage <= 1) {
		btn.style.opacity = '0.0';
		grab('pageNumber').value = 1;
	}
	else {
		btn.style.opacity = '1.0';
	}

	grab('thisPageNumber').innerHTML = currentPage;

	setNextResultBtn();
}

function setNextResultBtn() {
	var btn = grab('nextArrowRight');
	var currentPage = grab('pageNumber').value;
	var numPages = grab('numPages').value;

	currentPage = Number(currentPage);
	numPages = Number(numPages);

	if (currentPage >= numPages) {
		btn.style.opacity = '0.0';
		grab('pageNumber').value = numPages;
	}
	else {
		btn.style.opacity = '1.0';
	}

	grab('thisPageNumber').innerHTML = currentPage;

	setPrevResultBtn();
}

function loadPrevSearchPage(json_data) {
	var thePage 		= grab('pageNumber').value;
	var numberOfPages 	= grab('numPages').value;
	thePage 			= Number(thePage);
	numberOfPages 		= Number(numberOfPages);

	thePage = thePage - 1;
	if (thePage >= 1) {
		grab('pageNumber').value = thePage;
		page = grabResultPage(thePage, json_data);
		numOnPage = page.length;
		superResultsPage(thePage, numOnPage, json_data);
	}

	setPrevResultBtn();
}

function loadNextSearchPage(json_data) {
	var thePage 		= grab('pageNumber').value;
	var numberOfPages 	= grab('numPages').value;
	thePage 			= Number(thePage);
	numberOfPages 		= Number(numberOfPages);

	thePage += 1;
	if (thePage <= numberOfPages) {
		grab('pageNumber').value = thePage;
		page = grabResultPage(thePage, json_data);
		numOnPage = page.length;
		superResultsPage(thePage, numOnPage, json_data);
	}

	if (thePage >= numberOfPages) {
		thePage = numberOfPages;
		grab('nextArrowRight').style.opacity = '0.0';
	}

	setNextResultBtn();	
}

function correctClientDOBForm() {
	var m = grab('c_mob');
	var d = grab('c_dob');
	var y = grab('c_yob');
	var leap = (y.value) % 4;

	if (leap === 0) {
		if (m.selectedIndex === 2) {
			if (d.selectedIndex > 29) {
				d.selectedIndex = 0;
			}
		}
	}
	else if (d.selectedIndex > 28) {
		d.selectedIndex = 0;
	}

	if (m.selectedIndex === 4 && d.selectedIndex > 30) {
		d.selectedIndex = 0;
	}
	else if (m.selectedIndex === 9 && d.selectedIndex > 30) {
		d.selectedIndex = 0;
	}
	else if (m.selectedIndex === 11 && d.selectedIndex > 30) {
		d.selectedIndex = 0;
	}
}

function toClientOptions(form_id) {
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

function goHomeProfile() {
	grab('b_form').action = '/adminHome/';
	grab('b_form').submit();
}

function toClientOptions2(c_id, hasSession, session_id) {
	var search_type = grab('search_type').value;

	hasSession 	= String(hasSession.value);
	session_id 	= String(session_id.value);
	c_id 		= String(c_id.value);
	search_type = String(search_type);

	getPopParent('client_id').value 	= c_id;
	getPopParent('session_id').value 	= session_id;
	getPopParent('cSearch').value 		= search_type;
	grab('session_id').value 			= session_id;
	grab('s_option').value 				= 'Some Text for something';

	if (search_type === 'general') {
		getPopParent('hasExisting').value = hasSession;
		getPopParent('session_id').value = session_id;
		getPopParent('m_form').action = '/clientProfile/';
		getPopParent('m_form').submit();
		window.close();
	}
	else if (search_type === 'session') {
		getPopParent('m_form').action = '/clientOptions/';
		getPopParent('search_clientSession').value = 'True';

		if (hasSession === 'true') {
			grab('b_form').action = '/hasExistingSession/';
			grab('b_form').submit();
		}
		else {
			getPopParent('m_form').submit();
			window.close();
		}
	}
}

function toClientOptionsProfile() {
	var hasExisting = grab('hasExisting').value;
	hasExisting = String(hasExisting);

	if (hasExisting === 'true') {
		var w = 600, h = 665;
		var l = Number((screen.width/2) - (w/2));
		var t = Number((screen.height/2) - (h/2));
		openPopUp('auto', '/hasExistingSession/', w, h);
	}
	else {
		grab('b_form').action = '/clientOptions/';
		grab('b_form').submit();
	}
}

function updateClientStats() {
	var w = 300;
	openPopUp('auto', '/updateStatus/', w, w);
}

function initialize_statusUpdate() {
	var isPending 		= getPopParent('isPending').value;
	var isDischarged 	= getPopParent('isDischarged').value;
	isPending 			= String(isPending);
	isDischarged 		= String(isDischarged);

	grab('isPending').value 	= isPending;
	grab('isDischarged').value 	= isDischarged;
	grab('client_id').value 	= getPopParent('client_id').value;
	grab('status').className 	= getPopParent('updateClass').value;

	if (isDischarged === 'True' || isPending === 'True') {
		grab('status').innerHTML = 'ACTIVE';
		grab('newStatus').value = 'ACTIVE';
	}
	else if (isDischarged === 'False' && isPending === 'False') {
		grab('status').innerHTML = 'DISCHARGED';
		grab('newStatus').value = 'DISCHARGED';
	}

	setUpdateClass();
}

function setUpdateClass() {
	var current = getPopParent('status').className;
	current = String(current);

	if (current === 'clientNotActive') {
		grab('status').className = 'clientIsActive';
	}
	else if (current === 'clientIsActive'){
		grab('status').className = 'clientNotActive';
	}
}

function setActiveTagParent() {
	var statusClass = null;
	var isPending = grab('isPending').value;
	var isDischarged = grab('isDischarged').value;

	isPending = String(isPending);
	isDischarged = String(isDischarged);

	if (isPending === 'True') {
		statusClass = 'clientIsPending';
	}
	else if (isDischarged === 'True') {
		statusClass = 'clientNotActive';
	}
	else {
		statusClass = 'clientIsActive';
	}

	grab('status').className = statusClass;
}

function setActiveTag() {
	var statusClass = null;
	var isPending = getPopParent('isPending').value;
	var isDischarged = getPopParent('isDischarged').value;

	isPending = String(isPending);
	isDischarged = String(isDischarged);

	if (isPending === 'True') {
		statusClass = 'clientIsPending';
	}
	else if (isDischarged === 'True') {
		statusClass = 'clientNotActive';
	}
	else {
		statusClass = 'clientIsActive';
	}

	getPopParent('status').className = statusClass;
}

function proceedStatusUpdate() {
	var newStatus 	= grab('newStatus').value;
	newStatus 	= String(newStatus);
	getPopParent('status').innerHTML = newStatus;
	getPopParent('isPending').value = 'False';

	if (newStatus === 'ACTIVE') {
		getPopParent('isDischarged').value = 'False';
	}
	else if (newStatus === 'DISCHARGED') {
		getPopParent('isDischarged').value = 'True';
	}

	setActiveTag();
	grab('u_form').submit();
}

function editClientInformation() {
	w = 600, h = 655;
	openPopUp('auto', '/editClientInfo/', w, h);
}

function processEditedClientData() {

}

function deleteClientProfile() {
	w = 400;
	openPopUp('auto', '/confirmDeleteClient/', w, w);
}

function viewClientInvoices() {
	w = 600, h = 655;
	openPopUp('auto', '/clientInvoiceMain/', w, h);
}

function viewClientFiles(viewType) {
	viewType = String(viewType);
	grab('viewType').value = viewType;

	w = 600, h = 655;
	openPopUp('auto', '/clientFiles/', w, h);
}

function initialize_editClientPage(json_data) {
	grab('state').selectedIndex = json_data.state;
	grab('reasonRef').selectedIndex = json_data.ref;
	grab('c_dob').selectedIndex = json_data.day
	grab('c_mob').selectedIndex = json_data.month
	grab('c_yob').selectedIndex = json_data.year
	setRadioElement(json_data.gender, grab('male'), grab('female'));
}

function updateClientAccount() {
	var w = 400, h = 400;
	grab('b_form').submit();
	openPopUp('auto', '/clientAccountUpdated/', w, h);	
}

function setNewClientFields(data) {
	grab('b_form').submit();
}

function refreshClientParentPage(data) {
	superParent('profile-name-head').innerHTML 	= data.the_name;
	superParent('profile-email-head').innerHTML = data.email;
	superParent('address1').innerHTML 			= data.address1;
	superParent('address2').innerHTML 			= data.address2;
	superParent('profile-phone-head').innerHTML = data.phone;
	superParent('em_contact').innerHTML 		= data.em_contact;
	superParent('em_phone').innerHTML 			= data.em_phone;
	superParent('prob_off').innerHTML 			= data.probOfficer;
	superParent('prob_phone').innerHTML 		= data.prob_phone;
	superParent('f_ssn').innerHTML 				= data.ss_num;
	superParent('gender').innerHTML 			= data.gender;
	superParent('workPhone').innerHTML 			= data.work;
	superParent('dob').innerHTML				= data.dob

	closeAllWindows(2);
}

function newApptOn(btn) {
	btn = String(btn);

	if (btn === 'btn1') {
		image = '/static/images/manager/addOver.png';
		grab('btn1').src = image;
	}
}

function newApptOff(btn) {
	btn = String(btn);
}

function superParent(field) {
	field = String(field);
	return window.opener.getPopParent(field);
}

function closeAllWindows(numWindows) {
	numWindows = Number(numWindows);
	window.close();

	for (var i = 0; i < numWindows; i++) {
		window.opener.close();
	}	
}

function waitSeconds(iMilliSeconds) {
    var counter= 0
        , start = new Date().getTime()
        , end = 0;
    while (counter < iMilliSeconds) {
        end = new Date().getTime();
        counter = end - start;
    }
}

function initial_clientFiles() {
	var viewType = getPopParent('viewType').value;
	var headTag = grab('clientFilesHeader');
	viewType = String(viewType);

	if (viewType === 'history') {
		headTag.innerHTML = 'View Client History';
	}
	else if (viewType === 'incomplete') {
		headTag.innerHTML = 'View Incomplete Files';
	}
}

function appointmentsClientProfile() {
	w = 600, h = 655;
	openPopUp('auto', '/clientAppointments/', w, h);
}


function set_session_option() {
	grab('session_id').value = getPopParent('session_id').value;

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
		form.action = '/clientOptions/';
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
	var isForm = grab('completeAM').value;
	grab('fType').value = 'am';
	isForm = String(isForm);

	if (isForm === 'True') {
		var w = 550, h = 450;
		openPopUp('auto', '/form_existing/', w, h);
	}
	else if (isForm === 'False') {
		grab('c_form').action = '/am_preliminary/';
		grab('c_form').submit();
	}
}

function new_asi() {
	var isForm = grab('completeASI').value;
	grab('fType').value = 'asi';
	isForm = String(isForm);

	if (isForm === 'True') {
		var w = 550, h = 450;
		openPopUp('auto', '/form_existing/', w, h);
	}
	else if (isForm === 'False') {
		grab('c_form').action = '/asi_preliminary/';
		grab('c_form').submit();
	}
}

function new_mh() {
	var isForm = grab('completeMH').value;
	grab('fType').value = 'mh';
	isForm = String(isForm);

	if (isForm === 'True') {
		var w = 550, h = 450;
		openPopUp('auto', '/form_existing/', w, h);
	}
	else if (isForm === 'False') {
		grab('c_form').action = '/mh_preliminary/';
		grab('c_form').submit();
	}
}

function new_sap() {
	var isForm = grab('completeSAP').value;
	grab('fType').value = 'sap';
	isForm = String(isForm);

	if (isForm === 'True') {
		var w = 550, h = 450;
		openPopUp('auto', '/form_existing/', w, h);
	}
	else if (isForm === 'False') {
		grab('c_form').action = '/sap_preliminary/';
		grab('c_form').submit();
	}	
}

function new_ut() {
	var isForm = grab('completeUT').value;
	grab('fType').value = 'ut';
	isForm = String(isForm);

	if (isForm === 'True') {
		var w = 550, h = 450;
		openPopUp('auto', '/form_existing/', w, h);
	}
	else if (isForm === 'False') {
		grab('c_form').action = '/ut_preliminary/';
		grab('c_form').submit();
	}
}

function setExistingFType() {
	var fType = getPopParent('fType').value;
	grab('fType').value = fType;

	if (fType === 'am') {
		grab('formName').innerHTML = 'Anger Management Form';
		grab('formName2').innerHTML = 'Anger Management Form';
	}
	if (fType === 'mh') {
		grab('formName').innerHTML = 'Mental Health Assessment Form';
		grab('formName2').innerHTML = 'Mental Health Assessment Form';
	}
	if (fType === 'ut') {
		grab('formName').innerHTML = 'Urine Analysis Form';
		grab('formName2').innerHTML = 'Urine Analysis Form';
	}
	if (fType === 'sap') {
		grab('formName').innerHTML = 'S.A.P Form';
		grab('formName2').innerHTML = 'S.A.P Form';
	}
	if (fType === 'asi') {
		grab('formName').innerHTML = 'Addiction Severity Index Form';
		grab('formName2').innerHTML = 'Addiction Severity Index Form';
	}
}

function universalPrint() {
	var w = 1200, h = 1300;
	var fType = grab('fType').value;
	fType = String(fType);
	var location = null;

	if (fType === 'am') {
		location = '/printAM/';
	}
	else if (fType === 'mh') {
		location = '/printMH/';
	}
	else if (fType === 'ut') {
		location = '/printUT/';
	}
	else if (fType === 'asi') {
		location = '/printASI/';
	}
	else if (fType === 'sap') {
		location = '/print_sap/';
	}

	openPopUp('auto', location, w, h);
	window.close();
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
	var w = 550, h = 400;
	openPopUp('auto', '/closeSession/', w, h);
}

function delete_session() {
	var w = 550, h = 400;
	openPopUp('auto', '/deleteSession/', w, h);
}

function return_to_options2() {
	form = document.getElementById('mh_instructions');
	form.action = '/clientOptions/';
	form.submit();
}

function get_main_p_history(form_type, session_id) {
	form_type = String(form_type);
	session_id = String(session_id);

	grab('m_fType').value = form_type;
	grab('m_session_id').value = session_id;

	var w = 550, h = 450;
	openPopUp('auto', '/printLoaded/', w, h);
}

function loadPrintForm() {
	grab('form_type').value = getPopParent('m_fType').value;
	grab('session_id').value = getPopParent('m_session_id').value;
}

function showPrintable() {
	var w = 1200, h = 1300;
	var l = Number((screen.width/2) - (w/2));
	var t = Number((screen.height/2) - (h/2));
	grab('history_form').submit();

	window.resizeTo(w, h);
	window.moveTo(l, t);
    window.focus(); 
}

function initialize_options(numPages) {
	numPages = Number(numPages);

	if (numPages === 1) {
		grab('prevBtn').disabled = true;
		grab('nextBtn').disabled = true;
		grab('hisPageSelect').disabled = true;

		grab('prevBtn').className = 'phSelectDisabled';
		grab('nextBtn').className = 'phSelectDisabled';

		grab('prevBtn').style.opacity = '0.5';		
		grab('nextBtn').style.opacity = '0.5';
	}
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
	twoElementRadioSetup(grab('otherConnectionsUsing'), grab('lab1'), grab('connectionExplain'));
}


function post_dynamic_am_connections() {
	generalCheckSave(grab('angerWorse'), grab('m_angerWorse'));
	generalCheckSave(grab('troubleWhenUsing'), grab('m_troubleWhenUsing'));
	generalCheckSave(grab('lessAngry'), grab('m_lessAngry'));
	generalCheckSave(grab('othersTellMe'), grab('m_othersTellMe'));
	generalCheckSave(grab('noConnection'), grab('m_noConnection'));
	generalCheckSave(grab('otherConnectionsUsing'), grab('m_otherConnectionsUsing'));
	post(true, 'text', grab('connectionExplain'), grab('otherConnectionsUsing'), grab('m_connectionExplain'));
}

// AM WORST EPISODES FUNCTIONS
function generalCheckClear(fieldName, checkBox) {
	fieldName = String(fieldName);
	checkBox = String(checkBox);

	c = grab(checkBox);
	f = grab(fieldName);

	if (c.checked === true) {
		f.disabled = false;
		opacityHigh(f);
	}
	else {
		opacityLow(f);
		f.value = '';
		f.disabled = true;
	}
}

function worstCheck() {
	twoElementRadioSetupSelect(grab('yesDrugs'), grab('lab1'), grab('whoUsed'));
}

function worstEndSet() {
	generalCheckClear('otherWorstDescription', 'otherWorst');
}


function post_dynamic_am_worst() {
	post(false, 'text', grab('whoWorst'), null, null);
	post(false, 'text', grab('happenedWorst'), null, null);
	post(false, 'text', grab('wordThoughtWorst'), null, null);
	post(false, 'text', grab('howStartWorst'), null, null);
	post(false, 'text', grab('howEndWorst'), null, null);

	generalCheckSave(grab('physicalWorst'), grab('m_physicalWorst'));
	generalCheckSave(grab('verbalWorst'), grab('m_verbalWorst'));
	generalCheckSave(grab('propertyWorst'), grab('m_propertyWorst'));
	generalCheckSave(grab('otherWorst'), grab('m_otherWorst'));

	post(true, 'text', grab('otherWorstDescription'), grab('otherWorst'), grab('m_otherWorstDescription'));

	if (grab('yesDrugs').checked === true) {
		grab('m_whoUsed').value = grab('whoUsed').value;
	}
	else {
		grab('m_whoUsed').value = 'None Selected';
	}
	// post(true, 'select', grab('whoUsed'), grab('yesDrugs'), grab('m_whoUsed'));
}

// AM TARGET FUNCTIONS
function amTargetOther() {
	if (grab('angryOther').checked === true) {
		grab('otherWhom').disabled = false;
		opacityHigh(grab('otherWhom'));
	}
	else {
		opacityLow(grab('otherWhom'));
		grab('otherWhom').value = '';
		grab('otherWhom').disabled = true;
	}
}

function post_dynamic_am_target() {
	generalCheckSave(grab('angryPartner'), grab('m_angryPartner'));
	generalCheckSave(grab('angryParents'), grab('m_angryParents'));
	generalCheckSave(grab('angryChildren'), grab('m_angryChildren'));
	generalCheckSave(grab('angryRelatives'), grab('m_angryRelatives'));
	generalCheckSave(grab('angryEmployer'), grab('m_angryEmployer'));
	generalCheckSave(grab('angryFriends'), grab('m_angryFriends'));
	generalCheckSave(grab('angryOther'), grab('m_angryOther'));
	generalCheckSave(grab('seldomUpset'), grab('m_seldomUpset'));
	post(true, 'text', grab('otherWhom'), grab('angryOther'), grab('m_otherWhom'));
}

// AM FAMILY OF ORIGIN FUNCTIONS


function post_dynamic_am_family() {
	// Immanuel Lewis
	generalCheckSave(grab('hasLovingMother'), grab('m_hasLovingMother'));
	generalCheckSave(grab('hasLovingSiblings'), grab('m_hasLovingSiblings'));
}

//AM CURRENT PROBLEMS FUNCTIONS
function am_problems_check() {
	generalCheckClear('otherWhom', 'otherSeriousIllness');
}

function generalCheckSave(checkbox, target) {
	if (checkbox.checked === true) {
		target.value = 'True';
	}
	else {
		target.value = 'False';
	}
}

function am_problems_radio() {
	twoElementRadioSetup(grab('onMeds'), grab('lab2'), grab('whichMeds'));
}

function post_dynamic_am_final() {
	post(false, 'text', grab('anythingelse'), null, null);
	post(false, 'text', grab('changeLearn1'), null, null);
	post(false, 'text', grab('changeLearn2'), null, null);
	post(false, 'text', grab('changeLearn3'), null, null);
}


function post_dynamic_am_current() {
	post(true, 'text', grab('whichMeds'), grab('onMeds'), grab('m_whichMeds'));
	post(true, 'text', grab('otherWhom'), grab('otherSeriousIllness'), grab('m_otherWhom'));

	generalCheckSave(grab('brainInjury'), grab('m_brainInjury'));
	generalCheckSave(grab('stroke'), grab('m_stroke'));
	generalCheckSave(grab('epilepsy'), grab('m_epilepsy'));
	generalCheckSave(grab('attentionDD'), grab('m_attentionDD'));
	generalCheckSave(grab('pms'), grab('m_pms'));
	generalCheckSave(grab('depression'), grab('m_depression'));
	generalCheckSave(grab('ptsd'), grab('m_ptsd'));
	generalCheckSave(grab('otherSeriousIllness'), grab('m_otherSeriousIllness'));
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
	else if (section === '/am_control/') {
		post_dynamic_am_control();
	}
	else if (section === '/am_final/') {
		post_dynamic_am_final();
	}
}

function leaveAMViewForm() {
	grab('am_demo').action = '/clientOptions/';
	grab('am_demo').submit();
}

function initialize_saveForm() {
	grab('form_type').value = getPopParent('exit_type').value;
}

function finishSaveAMFinal() {
	var w = 500;
	openPopUp('auto', '/form_complete/', w, w);
}

function finalizeAllForms() {
	grab('s_form').submit();
	getPopParent('am_demo').action = '/clientOptions/'
	getPopParent('am_demo').submit();
}

function continue_am_form(section) {
	var current_section = String(grab('save_section').value);
	var hasErrors = hasErrorsInForm('am', section);

	if (hasErrors === true) {
		superErrorChecker('am', current_section);
		var w = 500, h = 500;
		openPopUp('auto', '/generateErrors/', w, h);
	}

	else {
		universal_am_dynamic_post(section);
		var next_url = grab('next_url');
		var form = grab('am_demo');
		grab('save_this').value = 'true';
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
function twoElementRadioSetup_no(trigger, label, field) {
	if (trigger.checked === false) {
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

function twoElementRadioSetupNumber_no(trigger, label, field) {
	if (trigger.checked === false) {
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

function twoElementRadioSetupSelect(trigger, label, field) {
	if (trigger.checked === true) {
		field.disabled = false;
		opacityHigh(label);
		opacityHigh(field);
	}

	else {
		opacityLow(label);
		opacityLow(field);
		field.selectedIndex = 0;
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

// function craxRadios(trigger, number, label1, label2, label3, radio1, radio2) {
// 	// grab()
// 	if (trigger.checked === true) {
// 		opacityLow(number);
// 		opacityLow(label1);
// 		opacityLow(label2);
// 		opacityLow(label3);
// 		opacityLow(radio1);
// 		opacityLow(radio2);
// 		radio1.disabled = true;
// 		radio2.disabled = true;
// 	}
// 	else {
// 		radio1.disabled = false;
// 		radio2.disabled = false;
// 		opacityHigh(number);
// 		opacityHigh(label1);
// 		opacityHigh(label2);
// 		opacityHigh(label3);
// 		opacityHigh(radio1);
// 		opacityHigh(radio2);
// 	}
// }

function craxRadios(trigger, number, lab1, lab2, lab3, rad1, rad2) {
	if (trigger.checked === true) {
		opacityLow(number);
		opacityLow(lab1);
		opacityLow(lab2);
		opacityLow(lab3);
		rad1.disabled = true;
		rad2.disabled = true;
	}
	else {
		rad1.disabled = false;
		rad2.disabled = false;
		opacityHigh(number);
		opacityHigh(lab1);
		opacityHigh(lab2);
		opacityHigh(lab3);
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
	twoElementRadioSetup(grab('DO'), grab('doReason_lab'), grab('resasonDO'));
}	

function healthRadioBtn() {
	twoElementRadioSetup(grab('not_healthy'), grab('healthExp_label'), grab('health_exp'));
	craxRadios(grab('healthy'), grab('num_14'), grab('num_14_lab'), grab('onMedLab'), grab('noMedLab'), grab('on_meds'), grab('no_med'));

	if (grab('healthy').checked === true) {
		grab('no_med').checked = true;
	}

	medsRadioBtn();
}

function medsRadioBtn() {
	twoElementRadioSetup(grab('on_meds'), grab('meds_leb'), grab('whatMedicine'));
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//************************************************************ AM VIEWS ***********************************************************//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//

function checkBoolInit(json_data, checkbox) {
	json_data = String(json_data);

	if (json_data === 'true' || json_data === 'True') {
		checkbox.checked = true;
	}
	else {
		checkbox.checked = false;
	}
}

function initialize_am_demo(json_data) {
	grab('maritalStatus').selectedIndex = json_data.maritalStatus;
	grab('livingSituation').selectedIndex = json_data.livingSituation;

	number_init(json_data.isComplete, grab('months_res'));
	number_init(json_data.isComplete, grab('years_res'));
	number_init(json_data.isComplete, grab('num_children'));
	number_init(json_data.isComplete, grab('spouse_dep'));
	number_init(json_data.isComplete, grab('other_dependants'));
	number_init(json_data.isComplete, grab('employed_months'));
	number_init(json_data.isComplete, grab('employed_years'));

	blank_init(json_data.isComplete, grab('whoLivesWithClient'));
	blank_init(json_data.isComplete, grab('resasonDO'));
	blank_init(json_data.isComplete, grab('job_title'));
	blank_init(json_data.isComplete, grab('employee'));
	blank_init(json_data.isComplete, grab('emp_address'));
	blank_init(json_data.isComplete, grab('employer_phone'));
	blank_init(json_data.isComplete, grab('health_exp'));
	blank_init(json_data.isComplete, grab('whatMedicine'));

	//PROCESS RADIO BUTTONS
	setRadioElement(json_data.own, grab('doesOwn'), grab('doesRent'));
	setRadioElement(json_data.health_problem, grab('not_healthy'), grab('healthy'));
	setRadioElement(json_data.medication, grab('on_meds'), grab('no_med'));

	var education = String(json_data.education);

	if (education === 'Drop out') {
		grab('DO').checked = true;
	}
	else if (education  === 'GED') {
		grab('GED').checked = true;
	}
	else if (education  === 'College') {
		grab('College').checked = true;
	}
	else {
		grab('HS').checked = true;
	}

	dropOutRadio();
	healthRadioBtn();
	medsRadioBtn();
}

function initialize_am_drug_history(json_data) {
	number_init(json_data.isComplete, grab('firstDrinkAge'));
	number_init(json_data.isComplete, grab('numDUI'));
	number_init(json_data.isComplete, grab('monthsQuit'));
	number_init(json_data.isComplete, grab('yearsQuit'));

	blank_init(json_data.isComplete, grab('firstDrinkType'));
	blank_init(json_data.isComplete, grab('amtPerWeek'));
	blank_init(json_data.isComplete, grab('useAmt'));
	blank_init(json_data.isComplete, grab('reasonQuit'));
	blank_init(json_data.isComplete, grab('BALevel'));
	blank_init(json_data.isComplete, grab('dateTreated'));
	blank_init(json_data.isComplete, grab('treatmentPlace'));
	blank_init(json_data.isComplete, grab('reasonNotFinishedTreatment'));
	blank_init(json_data.isComplete, grab('relapseTrigger'));

	setRadioElement(json_data.curUse, grab('yesDrink'), grab('noDrink'));
	setRadioElement(json_data.everDrank, grab('hasDrank'), grab('noDrank'));
	setRadioElement(json_data.DUI, grab('hasDUI'), grab('noDui'));
	setRadioElement(json_data.drugTreatment, grab('hadTreatment'), grab('noTreatment'));
	setRadioElement(json_data.finishedTreatment, grab('didFinish'), grab('noFinish'));
	setRadioElement(json_data.isClean, grab('isClean'), grab('notClean'));
	setRadioElement(json_data.drinkLastEpisode, grab('yesLast'), grab('noLast'));
	setRadioElement(json_data.drinkRelationshipProblem, grab('yesProb'), grab('noProb'));
	setRadioElement(json_data.needHelpDrugs, grab('needHelp'), grab('noHelp'));

	topLevelDH();
	dhRadio2();
	dhRadio3();

	if (grab('hadTreatment').checked === true) {
		if (grab('didFinish').checked === true) {
			if (grab('isClean').checked === true) {
				opacityLow(grab('lab17'));
				opacityLow(grab('relapseTrigger'));
				grab('relapseTrigger').value = '';
				grab('relapseTrigger').disabled = true;
			}
			else {
				opacityHigh(grab('lab17'));
				opacityHigh(grab('relapseTrigger'));
			}

			opacityLow(grab('lab16'));
			opacityLow(grab('reasonNotFinishedTreatment'));
			grab('reasonNotFinishedTreatment').value = '';
			grab('reasonNotFinishedTreatment').disabled = true;
		}
		else {
			opacityHigh(grab('lab16'));
			opacityHigh(grab('reasonNotFinishedTreatment'));
			grab('reasonNotFinishedTreatment').disabled = false;

			opacityLow(grab('super_8_label'));
			opacityLow(grab('num_8Lab'));
			opacityLow(grab('labe1'));
			opacityLow(grab('labe2'));
			opacityLow(grab('isClean'));
			opacityLow(grab('notClean'));

			grab('notClean').checked = true;

			grab('isClean').disabled = true;
			grab('notClean').disabled = true;
		}
	}
	else {
		opacityLow(grab('lab11'));
		opacityLow(grab('dateTreated'));
		opacityLow(grab('lab12'));
		opacityLow(grab('treatmentPlace'));

		opacityLow(grab('num_7'));
		opacityLow(grab('lab13'));
		opacityLow(grab('didFinish'));
		opacityLow(grab('noFinish'));
		opacityLow(grab('lab14'));
		opacityLow(grab('lab15'));
		opacityLow(grab('lab16'));
		opacityLow(grab('reasonNotFinishedTreatment'));

		opacityLow(grab('super_8_label'));
		opacityLow(grab('num_8Lab'));
		opacityLow(grab('isClean'));
		opacityLow(grab('notClean'));
		opacityLow(grab('labe1'));
		opacityLow(grab('labe2'));
		opacityLow(grab('lab17'));
		opacityLow(grab('relapseTrigger'));

		grab('dateTreated').value = '';
		grab('treatmentPlace').value = '';
		grab('reasonNotFinishedTreatment').value = '';
		grab('relapseTrigger').value = '';

		grab('didFinish').checked = true;
		grab('isClean').checked = true;

		grab('didFinish').disabled = true;
		grab('noFinish').disabled = true;
		grab('isClean').disabled = true;
		grab('notClean').disabled = true;
		grab('reasonNotFinishedTreatment').disabled = true;
		grab('relapseTrigger').disabled = true;

		grab('dateTreated').disabled = true;
		grab('treatmentPlace').disabled = true;
	}
}

function initialize_am_childhood(json_data) {
	//PROCESS THE DROPDOWN MENU
	raisedBy.selectedIndex = json_data.raisedBy;

	number_init(json_data.isComplete, grab('num_siblings'));

	blank_init(json_data.isComplete, grab('traumaExplain'));
	blank_init(json_data.isComplete, grab('howLeftHome'));
	blank_init(json_data.isComplete, grab('siblingsRelationshipExplain'));
	blank_init(json_data.isComplete, grab('dadCloseExplain'));
	blank_init(json_data.isComplete, grab('momCloseExplain'));
	blank_init(json_data.isComplete, grab('abusedBy'));
	blank_init(json_data.isComplete, grab('abuseImpact'));

	//PROCESS RADIO BUTTONS
	setRadioElement(json_data.momAlive, grab('momAlive'), grab('momNotAlive'));
	setRadioElement(json_data.dadAlive, grab('dadAlive'), grab('dadNotAlive'));
	setRadioElement(json_data.childTrama, grab('yesTrauma'), grab('noTrauma'));
	setRadioElement(json_data.siblingsClose, grab('sibsClose'), grab('sibsDistant'));
	setRadioElement(json_data.dadClose, grab('yesDad'), grab('noDad'));
	setRadioElement(json_data.momClose, grab('yesMom'), grab('noMom'));
	setRadioElement(json_data.wasAbused, grab('yesAbuse'), grab('noAbuse'));

	childTraumaRadio();
	childAbusedRadio();
}

function initialize_am_angerHistory(json_data) {
	number_init(json_data.isComplete, grab('longAgoTreatRecentVyrs'));
	number_init(json_data.isComplete, grab('longAgoTreatRecentVmos'));

	blank_init(json_data.isComplete, grab('recentIncidentV'));
	blank_init(json_data.isComplete, grab('recentVDate'));
	blank_init(json_data.isComplete, grab('recentVlocation'));
	blank_init(json_data.isComplete, grab('withWhomRecentV'));
	blank_init(json_data.isComplete, grab('happenedRecentV'));
	blank_init(json_data.isComplete, grab('otherExplainRecentV'));
	blank_init(json_data.isComplete, grab('typeWordsRecentV'));
	blank_init(json_data.isComplete, grab('psychoWhyRecentV'));
	blank_init(json_data.isComplete, grab('reasonNotCompleteRecentV'));

	checkBoolInit(json_data.wasTense, grab('wasTense'));
	checkBoolInit(json_data.hadRush, grab('hadRush'));
	checkBoolInit(json_data.feltStrong, grab('feltStrong'));
	checkBoolInit(json_data.physicalRecentV, grab('physicalRecentV'));
	checkBoolInit(json_data.verbalRecentV, grab('verbalRecentV'));
	checkBoolInit(json_data.propertyRecentV, grab('propertyRecentV'));
	checkBoolInit(json_data.otherRecentV, grab('otherRecentV'));

	setRadioElement(json_data.psychoRecentV, grab('yesTreated'), grab('noTreated'));
	setRadioElement(json_data.didCompleteTreatRecentV, grab('yesComplete'), grab('noComplete'));

	turnOnAH1();
	turnOnAH2();
	ahCk1init();
}

function initialize_am_angerHistory2(json_data) {
	blank_init(json_data.isComplete, grab('depress30ExplainRecentV'));
	blank_init(json_data.isComplete, grab('anxietyExplainRecentV'));
	blank_init(json_data.isComplete, grab('hallucinationLastV'));
	blank_init(json_data.isComplete, grab('understandingExplainRecentV'));
	blank_init(json_data.isComplete, grab('lastTimeTroubleControl'));
	blank_init(json_data.isComplete, grab('controlTrigger'));
	blank_init(json_data.isComplete, grab('suicide30ExplainRecentV'));

	setRadioElement(json_data.depress30RecentV, grab('yesDepress'), grab('noDepress'));
	setRadioElement(json_data.anxietyRecentV, grab('yesAnx'), grab('noAnx'));
	setRadioElement(json_data.hallucinationRecentV, grab('yesHall'), grab('noHall'));
	setRadioElement(json_data.understandingRecentV, grab('yesTrouble'), grab('noTrouble'));
	setRadioElement(json_data.troubleControlRecentV, grab('yesControl'), grab('noControl'));
	setRadioElement(json_data.suicide30RecentV, grab('yesSuicide'), grab('noSuicide'));

	explainDep();
	tensionRadio();
	halluRadio();
	troubleRadioAH2();
	troubleControlAH2();
	suicide30recent();
}

function initialize_am_angerHistory3(json_data) {
	blank_init(json_data.isComplete, grab('homicidalExplain'));
	blank_init(json_data.isComplete, grab('medRecentVExplain'));
	blank_init(json_data.isComplete, grab('medSuccessExplainRecentV'));
	blank_init(json_data.isComplete, grab('durationRecentV'));

	setRadioElement(json_data.homicidal, grab('yesHomicide'), grab('noHomicode'));
	setRadioElement(json_data.medRecentV, grab('yesMed'), grab('noMed'));
	setRadioElement(json_data.medSuccessRecentV, grab('yesSuccess'), grab('noSuccess'));

	var sc = Number(json_data.intensityRecentV);
	var ta = String(json_data.howOften);

	if (sc === 2) {
		grab('rad2').checked = true;
	}
	else if (sc === 3) {
		grab('rad3').checked = true;
	}
	else if (sc === 4) {
		grab('rad4').checked = true;
	}
	else if (sc === 5) {
		grab('rad5').checked = true;
	}
	else if (sc === 6) {
		grab('rad6').checked = true;
	}
	else if (sc === 7) {
		grab('rad7').checked = true;
	}
	else if (sc === 8) {
		grab('rad8').checked = true;
	}
	else if (sc === 9) {
		grab('rad9').checked = true;
	}
	else if (sc === 10) {
		grab('rad10').checked = true;
	}
	else{
		grab('rad1').checked = true;
	}

	if (ta === 'This time only') {
		grab('ho1').checked = true;
	}
	else if (ta === 'This month only') {
		grab('ho2').checked = true;
	}
	else if (ta === 'Last six months') {
		grab('ho3').checked = true;
	}
	else if (ta === 'Since childhood') {
		grab('ho4').checked = true;
	}
	else if (ta === 'Adolecent') {
		grab('ho5').checked = true;
	}
	else {
		grab('ho6').checked = true;
	}

	homicidalRadio();
	ah3number1();
	ah3number2();
}

function initalize_am_connections(json_data) {
	checkBoolInit(json_data.angerWorse, grab('angerWorse'));
	checkBoolInit(json_data.troubleWhenUsing, grab('troubleWhenUsing'));
	checkBoolInit(json_data.lessAngry, grab('lessAngry'));
	checkBoolInit(json_data.othersTellMe, grab('othersTellMe'));
	checkBoolInit(json_data.noConnection, grab('noConnection'));
	checkBoolInit(json_data.otherConnectionsUsing, grab('otherConnectionsUsing'));

	blank_init(json_data.isComplete, grab('connectionExplain'));

	connectionCheck();
}

function initalize_am_worst(json_data) {
	grab('whoUsed').selectedIndex = Number(json_data.whoUsed);

	blank_init(json_data.isComplete, grab('whoWorst'));
	blank_init(json_data.isComplete, grab('happenedWorst'));
	blank_init(json_data.isComplete, grab('wordThoughtWorst'));
	blank_init(json_data.isComplete, grab('howStartWorst'));
	blank_init(json_data.isComplete, grab('howEndWorst'));
	blank_init(json_data.isComplete, grab('otherWorstDescription'));

	setRadioElement(json_data.useWorst, grab('yesDrugs'), grab('noDrugs'));

	checkBoolInit(json_data.physicalWorst, grab('physicalWorst'));
	checkBoolInit(json_data.verbalWorst, grab('verbalWorst'));
	checkBoolInit(json_data.propertyWorst, grab('propertyWorst'));
	checkBoolInit(json_data.otherWorst, grab('otherWorst'));

	worstCheck();
	worstEndSet();
}

function initalize_am_target(json_data) {
	checkBoolInit(json_data.angryPartner, grab('angryPartner'));
	checkBoolInit(json_data.angryParents, grab('angryParents'));
	checkBoolInit(json_data.angryChildren, grab('angryChildren'));
	checkBoolInit(json_data.angryRelatives, grab('angryRelatives'));
	checkBoolInit(json_data.angryEmployer, grab('angryEmployer'));
	checkBoolInit(json_data.angryFriends, grab('angryFriends'));
	checkBoolInit(json_data.angryOther, grab('angryOther'));
	checkBoolInit(json_data.seldomUpset, grab('seldomUpset'));

	blank_init(json_data.isComplete, grab('angryAbout'));
	blank_init(json_data.isComplete, grab('otherWhom'));

	amTargetOther();
}


function initalize_family_origin(json_data) {
	blank_init(json_data.isComplete, grab('kidDadAnger'));
	blank_init(json_data.isComplete, grab('kidMomAnger'));
	blank_init(json_data.isComplete, grab('kidSiblingAnger'));
	blank_init(json_data.isComplete, grab('kidOtherAnger'));
	blank_init(json_data.isComplete, grab('learnFamilyAnger'));

	setRadioElement(json_data.suicideHistory, grab('yesAttempt'), grab('noAttempt'));

	checkBoolInit(json_data.hasLovingSiblings, grab('hasLovingSiblings'));
	checkBoolInit(json_data.hasLovingMother, grab('hasLovingMother'));
}

function initalize_am_problems(json_data) {
	checkBoolInit(json_data.brainInjury, grab('brainInjury'));
	checkBoolInit(json_data.stroke, grab('stroke'));
	checkBoolInit(json_data.epilepsy, grab('epilepsy'));
	checkBoolInit(json_data.attentionDD, grab('attentionDD'));
	checkBoolInit(json_data.pms, grab('pms'));
	checkBoolInit(json_data.depression, grab('depression'));
	checkBoolInit(json_data.ptsd, grab('ptsd'));
	checkBoolInit(json_data.otherSeriousIllness, grab('otherSeriousIllness'));

	setRadioElement(json_data.currentlyOnMeds, grab('onMeds'), grab('noMeds'));

	blank_init(json_data.isComplete, grab('describeIssue'));

	am_problems_check();
	am_problems_radio();
}

function initalize_am_control(json_data) {
	checkBoolInit(json_data.neverAttemptedControl, grab('neverAttemptedControl'));
	checkBoolInit(json_data.talkToMyself, grab('talkToMyself'));
	checkBoolInit(json_data.leaveScene, grab('leaveScene'));
	checkBoolInit(json_data.relax, grab('relax'));
	checkBoolInit(json_data.selfHelpGroup, grab('selfHelpGroup'));
	checkBoolInit(json_data.otherControlAnger, grab('otherControlAnger'));

	blank_init(json_data.isComplete, grab('whatSayYou'));
	blank_init(json_data.isComplete, grab('whatDoLeave'));
	blank_init(json_data.isComplete, grab('howRelax'));
	blank_init(json_data.isComplete, grab('doWhatOtherControl'));
	blank_init(json_data.howLongLeaveScene, grab('howLongLeaveScene'));

	talkMyself();
	leaveSceneCheckbox();
	howRelaxCheckbox();
	otherControlCheckbox();
}

function initalize_am_final() {
	blank_init(json_data.isComplete, grab('anythingelse'));
	blank_init(json_data.isComplete, grab('changeLearn1'));
	blank_init(json_data.isComplete, grab('changeLearn2'));
	blank_init(json_data.isComplete, grab('changeLearn3'));
}

function initialize_am(section, json_data) {
	section = String(section)

	if (section === '/am_demographic/') {
		initialize_am_demo(json_data);
	}
	else if (section === '/am_drugHistory/') {
		initialize_am_drug_history(json_data);
	}
	else if (section === '/am_childhood/') {
		initialize_am_childhood(json_data);
	}
	else if (section === '/am_angerHistory/') {
		initialize_am_angerHistory(json_data);
	}
	else if (section === '/am_angerHistory2/') {
		initialize_am_angerHistory2(json_data);
	}
	else if (section === '/am_angerHistory3/') {
		initialize_am_angerHistory3(json_data);
	}
	else if (section === '/am_connections/') {
		initalize_am_connections(json_data);
	}
	else if (section === '/am_worst/') {
		initalize_am_worst(json_data);
	}
	else if (section === '/am_angerTarget/') {
		initalize_am_target(json_data);
	}
	else if (section === '/am_familyOrigin/') {
		initalize_family_origin(json_data);
	}
	else if (section === '/am_problems/') {
		initalize_am_problems(json_data);
	}
	else if (section === '/am_control/') {
		initalize_am_control(json_data);
	}
	else if (section === '/am_final/') {
		initalize_am_final(json_data);
	}
}

function start_am_form() {
	var form = document.getElementById('am_instructions');
	form.action = '/am_demographic/';
	form.submit();
}

function processAMDemoData() {
	if (grab('DO').checked === false) {
		grab('m_resasonDO').value = 'N/A';
	}
	else {
		grab('m_resasonDO').value = grab('resasonDO').value;
	}

	post(true, 'text', grab('health_exp'), grab('not_healthy'), grab('m_health_exp'));

	if (grab('healthy').checked === true) {
		grab('m_medication').value = 'False';
		grab('m_whatMedicine').value = 'N/A';
	}
	else {
		post(true, 'text', grab('whatMedicine'), grab('on_meds'), grab('m_whatMedicine'));
		if (grab('on_meds').checked === true) {
			grab('m_medication').value = 'True';
		}
		else {
			grab('m_medication').value = 'False';
		}
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
	twoElementRadioSetupNumber(grab('hasDUI'), grab('lab9'), grab('numDUI'));
	twoElementRadioSetup(grab('hasDUI'), grab('lab10'), grab('BALevel'));
}

function dhRadio2() {
	twoElementRadioSetupNumber(grab('hasDrank'), grab('lab4'), grab('yearsQuit'));
	twoElementRadioSetupNumber(grab('hasDrank'), grab('lab5'), grab('monthsQuit'));
	twoElementRadioSetup(grab('hasDrank'), grab('lab6'), grab('reasonQuit'));
	twoElementRadioSetup(grab('hasDrank'), grab('lab3'), grab('reasonQuit'));
	dhRadioEFX();
}

function dhRadioEFX() {
	if (grab('noDrank').checked === true && grab('noDrink').checked === true) {
		grab('noDui').checked = true;
		dhRadio3();

		opacityLow(grab('num_5'));
		opacityLow(grab('num_5Lab'));
		opacityLow(grab('lab7'));
		opacityLow(grab('lab8'));
		opacityLow(grab('hasDUI'));
		opacityLow(grab('noDui'));
		grab('hasDUI').disabled = true;
		grab('noDui').disabled = true;
	}
	else {
		grab('hasDUI').disabled = false;
		grab('noDui').disabled = false;
		opacityHigh(grab('num_5'));
		opacityHigh(grab('num_5Lab'));
		opacityHigh(grab('lab7'));
		opacityHigh(grab('lab8'));
		opacityHigh(grab('hasDUI'));
		opacityHigh(grab('noDui'));
	}
}

function dhLeftRadio3() {
	twoElementRadioSetup(grab('notClean'), grab('lab17'), grab('relapseTrigger'));
}

function dhLeftRadio2() {
	twoElementRadioSetup(grab('noFinish'), grab('lab16'), grab('reasonNotFinishedTreatment'));

	if (grab('noFinish').checked === true) {
		opacityLow(grab('super_8_label'));
		opacityLow(grab('num_8Lab'));
		opacityLow(grab('isClean'));
		opacityLow(grab('notClean'));
		opacityLow(grab('labe1'));
		opacityLow(grab('labe2'));

		opacityHigh(grab('lab17'));
		opacityHigh(grab('relapseTrigger'));

		grab('notClean').checked = true;

		grab('isClean').disabled = true;
		grab('notClean').disabled = true;
		grab('relapseTrigger').disabled = false;
	}
	else {
		opacityHigh(grab('super_8_label'));
		opacityHigh(grab('num_8Lab'));
		opacityHigh(grab('isClean'));
		opacityHigh(grab('notClean'));
		opacityHigh(grab('labe1'));
		opacityHigh(grab('labe2'));

		grab('isClean').checked = true;
		dhLeftRadio3();

		grab('isClean').disabled = false;
		grab('notClean').disabled = false;
	}
}

function dhLeftRadio1() {
	twoElementRadioSetup(grab('hadTreatment'), grab('lab11'), grab('dateTreated'));
	twoElementRadioSetup(grab('hadTreatment'), grab('lab12'), grab('treatmentPlace'));

	if (grab('noTreatment').checked === true) {
		opacityLow(grab('num_7'));
		opacityLow(grab('super_8_label'));

		opacityLow(grab('lab13'));
		opacityLow(grab('num_8Lab'));

		opacityLow(grab('didFinish'));
		opacityLow(grab('noFinish'));
		opacityLow(grab('isClean'));
		opacityLow(grab('notClean'));

		opacityLow(grab('lab14'));
		opacityLow(grab('lab15'));
		opacityLow(grab('labe1'));
		opacityLow(grab('labe2'));

		grab('didFinish').checked = true;
		grab('isClean').checked = true;

		dhLeftRadio2();
		dhLeftRadio3();

		grab('didFinish').disabled = true;
		grab('noFinish').disabled = true;
		grab('isClean').disabled = true;
		grab('notClean').disabled = true;
	}
	else {
		opacityHigh(grab('num_7'));
		opacityHigh(grab('super_8_label'));

		opacityHigh(grab('lab13'));
		opacityHigh(grab('num_8Lab'));

		opacityHigh(grab('didFinish'));
		opacityHigh(grab('noFinish'));
		opacityHigh(grab('isClean'));
		opacityHigh(grab('notClean'));

		opacityHigh(grab('lab14'));
		opacityHigh(grab('lab15'));
		opacityHigh(grab('labe1'));
		opacityHigh(grab('labe2'));

		grab('didFinish').disabled = false;
		grab('noFinish').disabled = false;
		grab('isClean').disabled = false;
		grab('notClean').disabled = false;
	}
}

function topLevelDH() {
	twoElementRadioSetup(grab('yesDrink'), grab('oftenLab'), grab('amtPerWeek'));
	twoElementRadioSetup(grab('yesDrink'), grab('muchLab'), grab('useAmt'));
	craxRadios(grab('yesDrink'), grab('num_4'), grab('num_4Lab'), grab('r1Lab'), grab('r2Lab'), grab('hasDrank'), grab('noDrank'));

	if (grab('yesDrink').checked === true) {
		grab('noDrank').checked = true;
	}

	dhRadio2();
	dhRadioEFX();
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

function processAM_DH_data() {
	//HIDDEN FIELDS
	post(false, 'text', grab('firstDrinkType'), null, null);
	post(true, 'text', grab('amtPerWeek'), grab('yesDrink'), grab('m_amtPerWeek'));
	post(true, 'text', grab('useAmt'), grab('yesDrink'), grab('m_useAmt'));

	if (grab('noDrink').checked === true) {
		if (grab('hasDrank').checked === true) {grab('m_everDrank').value = 'True';}
		else {grab('m_everDrank').value = 'False';}
		post(true, 'number', grab('yearsQuit'), grab('hasDrank'), grab('m_yearsQuit'));
		post(true, 'number', grab('monthsQuit'), grab('hasDrank'), grab('m_monthsQuit'));
		post(true, 'text', grab('reasonQuit'), grab('hasDrank'), grab('m_reasonQuit'));
	}
	else {
		grab('m_everDrank').value = 'False';
		grab('m_monthsQuit').value = '0';
		grab('m_yearsQuit').value = '0';
		grab('m_reasonQuit').value = 'N/A';
	}

	if (grab('noDrink').checked === true) {
		if (grab('hasDrank').checked === false) {
			grab('m_DUI').value = 'False';
			grab('m_numDUI').value = '0';
			grab('m_BALevel').value = 'N/A';
		}
		else {
			if (grab('hasDUI').checked === true) {grab('m_DUI').value = 'True';}
			else {grab('m_DUI').value = 'False';}
			post(true, 'number', grab('numDUI'), grab('hasDUI'), grab('m_numDUI'));
			post(true, 'text', grab('BALevel'), grab('hasDUI'), grab('m_BALevel'));
		}
	}

	if (grab('yesDrink').checked === true) {
		post(true, 'number', grab('numDUI'), grab('hasDUI'), grab('m_numDUI'));
		post(true, 'text', grab('BALevel'), grab('hasDUI'), grab('m_BALevel'));

		if (grab('hasDUI').checked === true) {
			grab('m_DUI').value = 'True';
		}
		else {
			grab('m_DUI').value = 'False';
		}
	}

	post(true, 'text', grab('dateTreated'), grab('hadTreatment'), grab('m_dateTreated'));
	post(true, 'text', grab('treatmentPlace'), grab('hadTreatment'), grab('m_treatmentPlace'));
	
	if (grab('hadTreatment').checked === true) {
		if (grab('didFinish').checked === true) {
			grab('m_finishedTreatment').value = 'True';
			grab('m_reasonNotFinishedTreatment').value = 'N/A';

			if (grab('isClean').checked === true) {
				grab('m_isClean').value = 'True';
				grab('m_relapseTrigger').value = 'N/A';
			}
			else if (grab('isClean').checked === false) {
				grab('m_isClean').value = 'False';
				grab('m_relapseTrigger').value = grab('relapseTrigger').value;
			}
		}
		else {
			grab('m_finishedTreatment').value = 'False';
			grab('m_reasonNotFinishedTreatment').value = grab('reasonNotFinishedTreatment').value;
			grab('m_isClean').value = 'False';
			grab('m_relapseTrigger').value = grab('relapseTrigger').value;
		}
	}
}

function process_am_child_data() {	
	post(true, 'text', grab('abusedBy'), grab('yesAbuse'), grab('m_abusedBy'));
	post(true, 'text', grab('abuseImpact'), grab('yesAbuse'), grab('m_abuseImpact'));

	post(false, 'text', grab('howLeftHome'), null, null);
	post(false, 'text', grab('siblingsRelationshipExplain'), null, null);
	post(false, 'text', grab('dadCloseExplain'), null, null);
	post(false, 'text', grab('momCloseExplain'), null, null);
	post(false, 'number', grab('num_siblings'), null, null);

	post(false, 'text', grab('childAngerExplain'), null, null);
	post(false, 'text', grab('otherChildExplain'), null, null);
	post(false, 'text', grab('parentViolenceExplain'), null, null);
	post(false, 'text', grab('parentViolenceImpact'), null, null);

	post(true, 'text', grab('traumaExplain'), grab('yesTrauma'), grab('m_traumaExplain'));
}

function finishOffAmChildhood() {
	var w = 560, h = 740;
	openPopUp('auto', '/finishChildhood/', w, h);
}

function determineBool(trigger, target) {
	if (trigger.checked === true) {
		target.value = 'True';
	}
	else {
		target.value = 'False';
	}
}

function initializeFinishChildhood(data) {
	setRadioElement(data.childAnger, grab('yesAnger'), grab('noAnger'));
	setRadioElement(data.otherChild, grab('yesOther'), grab('noOther'));
	setRadioElement(data.parentViolence, grab('yesViolence'), grab('noViolence'));

	finChild1();
	finChild2();
	finChild3();
}

function finChild1() {
	twoElementRadioSetup(grab('yesAnger'), grab('lab1'), grab('childAngerExplain'));
}

function finChild2() {
	twoElementRadioSetup(grab('yesOther'), grab('lab2'), grab('otherChildExplain'));
}

function finChild3() {
	twoElementRadioSetup(grab('yesViolence'), grab('lab3'), grab('parentViolenceExplain'));
	twoElementRadioSetup(grab('yesViolence'), grab('num_4'), grab('parentViolenceImpact'));
}

function saveChildExtras() {
	var hasErrors = null;
	fields = fetchSpecial1_am();
	
	for (var i = 0; i < fields.length; i++) {
		hasErrors = hasTextError(fields[i]);

		if (hasErrors === true) {
			break;
		}
	}

	if (hasErrors === true) {
		for (var j = 0; j < fields.length; j++) {
			textErrorChecker(fields[j]);
		}

		var w = 500, h = 500;
		openPopUp('auto', '/generateErrors/', w, h);
	}
	else {
		determineBool(grab('yesAnger'), getPopParent('childAnger'));
		determineBool(grab('yesOther'), getPopParent('otherChild'));
		determineBool(grab('yesViolence'), getPopParent('parentViolence'));

		postToWindowParent('yesAnger', 'childAngerExplain', 'childAngerExplain');
		postToWindowParent('yesOther', 'otherChildExplain', 'otherChildExplain');
		postToWindowParent('yesViolence', 'parentViolenceExplain', 'parentViolenceExplain');
		postToWindowParent('yesViolence', 'parentViolenceImpact', 'parentViolenceImpact');

		getPopParent('superBtn').innerHTML = " <button onClick=\"javascript: continue_am_form(\'/am_childhood/\'); return false;\">Save & Continue</button>";
		getPopParent('superBtn').className = 'pro-iml-btn';
		window.close();
	}
}

function postToWindowParent(triggerName, fieldName, targetName) {
	triggerName 	= String(triggerName);
	fieldName 		= String(fieldName);
	targetName 		= String(targetName);

	var trigger 	= grab(triggerName);
	var field 		= grab(fieldName);
	var target 		= getPopParent(targetName);

	if (trigger.checked === true) {
		target.value = field.value;
	}
	else {
		target.value = 'N/A';
	}
}

function subPost1(type, trigger1, trigger2, field, triggerTarget, fieldTarget) {
	if (type === 'text') {
		if (trigger1.checked === true) {
			if (trigger2.checked === true) {triggerTarget.value = 'True';}
			else {triggerTarget.value = 'False';}
			post(true, 'text', field, trigger2, fieldTarget);
		}
		else {
			triggerTarget.value = 'False';
			fieldTarget.value = 'N/A';
		}
	}
	else if (type === 'number') {
		if (trigger1.checked === true) {
			if (trigger2.checked === true) {triggerTarget.value = 'True';}
			else {triggerTarget.value = 'False';}
			triggerTarget.value = 'True';
			post(true, 'number', field, trigger2, fieldTarget);
		}
		else {
			triggerTarget.value = 'False';
			fieldTarget.value = '0';
		}
	}
}

function subPost2(type1, type2, trigger1, trigger2, field1, field2, triggerTarget, ft1, ft2) {
	subPost1(type1, trigger1, trigger2, field1, triggerTarget, ft1);
	subPost1(type2, trigger1, trigger2, field2, triggerTarget, ft2);
}


// AM CHILDHOOD FUNCTIONS
function childTraumaRadio() {
	twoElementRadioSetup(grab('yesTrauma'), grab('lab1'), grab('traumaExplain'));
}

function childAbusedRadio() {
	twoElementRadioSetup(grab('yesAbuse'), grab('lab2'), grab('abusedBy'));
	twoElementRadioSetup(grab('yesAbuse'), grab('lab3'), grab('abuseImpact'));
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
	twoElementRadioSetup(grab('talkToMyself'), grab('lab1'), grab('whatSayYou'));
}

function leaveSceneCheckbox() {
	twoElementRadioSetup(grab('leaveScene'), grab('lab2'), grab('howLongLeaveScene'));
	twoElementRadioSetup(grab('leaveScene'), grab('lab3'), grab('whatDoLeave'));
}

function howRelaxCheckbox() {
	twoElementRadioSetup(grab('relax'), grab('lab4'), grab('howRelax'));
}

function otherControlCheckbox() {
	twoElementRadioSetup(grab('otherControlAnger'), grab('lab5'), grab('doWhatOtherControl'));
}



function post_dynamic_am_control() {
	generalCheckSave(grab('neverAttemptedControl'), grab('m_neverAttemptedControl'));
	generalCheckSave(grab('talkToMyself'), grab('m_talkToMyself'));
	generalCheckSave(grab('leaveScene'), grab('m_leaveScene'));
	generalCheckSave(grab('relax'), grab('m_relax'));
	generalCheckSave(grab('selfHelpGroup'), grab('m_selfHelpGroup'));
	generalCheckSave(grab('otherControlAnger'), grab('m_otherControlAnger'));

	post(true, 'text', grab('whatSayYou'), grab('talkToMyself'), grab('m_whatSayYou'));
	post(true, 'text', grab('howLongLeaveScene'), grab('leaveScene'), grab('m_howLongLeaveScene'));
	post(true, 'text', grab('whatDoLeave'), grab('leaveScene'), grab('m_whatDoLeave'));
	post(true, 'text', grab('howRelax'), grab('relax'), grab('m_howRelax'));
	post(true, 'text', grab('doWhatOtherControl'), grab('otherControlAnger'), grab('m_doWhatOtherControl'));
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
	twoElementRadioSetup(grab('yesTreated'), grab('lab1'), grab('psychoWhyRecentV'));
	twoElementRadioSetup(grab('yesTreated'), grab('lab2'), grab('psychoWhyRecentV'));
	twoElementRadioSetupNumber(grab('yesTreated'), grab('lab3'), grab('longAgoTreatRecentVyrs'));
	twoElementRadioSetupNumber(grab('yesTreated'), grab('lab4'), grab('longAgoTreatRecentVmos'));

	if (grab('noTreated').checked === true) {
		grab('noComplete').checked = true;
		turnOnAH2();
		opacityLow(grab('lab5'));
		opacityLow(grab('lab6'));
		opacityLow(grab('lab7'));
		opacityLow(grab('yesComplete'));
		opacityLow(grab('noComplete'));
		grab('yesComplete').disabled = true;
		grab('noComplete').disabled = true;
	}
	else {
		opacityHigh(grab('lab5'));
		opacityHigh(grab('lab6'));
		opacityHigh(grab('lab7'));
		opacityHigh(grab('yesComplete'));
		opacityHigh(grab('noComplete'));
		grab('yesComplete').disabled = false;
		grab('noComplete').disabled = false;
	}
}

function turnOnAH2() {
	twoElementRadioSetup(grab('yesComplete'), grab('lab8'), grab('reasonNotCompleteRecentV'));
}

function ahCk1init() {
	if (grab('otherRecentV').checked === true) {
		opacityHigh(grab('otherExplainRecentV'));
		grab('otherExplainRecentV').disabled = false;
	}
	else {
		grab('otherExplainRecentV').disabled = true;
		opacityLow(grab('otherExplainRecentV'));
		grab('otherExplainRecentV').value = '';
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


		psychoWhyRecentV.disabled = true;
		longAgoTreatRecentVmos.disabled = true;
		longAgoTreatRecentVyrs.disabled = true;
		didComplete.disabled = true;
		notCompleted.disabled = true;
	}	
}

function process_am_ah1_data() {
	post(false, 'text', grab('recentIncidentV'), null, null);
	post(false, 'text', grab('recentVDate'), null, null);
	post(false, 'text', grab('recentVlocation'), null, null);
	post(false, 'text', grab('withWhomRecentV'), null, null);
	post(false, 'text', grab('happenedRecentV'), null, null);
	post(false, 'text', grab('typeWordsRecentV'), null, null);

	generalCheckSave(grab('physicalRecentV'), grab('m_physicalRecentV'));
	generalCheckSave(grab('verbalRecentV'), grab('m_verbalRecentV'));
	generalCheckSave(grab('propertyRecentV'), grab('m_propertyRecentV'));
	generalCheckSave(grab('otherRecentV'), grab('m_otherRecentV'));	
	generalCheckSave(grab('wasTense'), grab('m_wasTense'));
	generalCheckSave(grab('hadRush'), grab('m_hadRush'));
	generalCheckSave(grab('feltStrong'), grab('m_feltStrong'));

	post(true, 'text', grab('otherExplainRecentV'), grab('otherRecentV'), grab('m_otherExplainRecentV'));
	post(true, 'text', grab('psychoWhyRecentV'), grab('yesTreated'), grab('m_psychoWhyRecentV'));
	post(true, 'number', grab('longAgoTreatRecentVyrs'), grab('yesTreated'), grab('m_longAgoTreatRecentVyrs'));
	post(true, 'number', grab('longAgoTreatRecentVmos'), grab('yesTreated'), grab('m_longAgoTreatRecentVmos'));

	if (grab('yesTreated').checked === true) {
		if (grab('yesComplete').checked === true) {
			grab('m_didCompleteTreatRecentV').value = 'True';
		}
		else {
			grab('m_didCompleteTreatRecentV').value = 'False';
		}
		post(true, 'text', grab('reasonNotCompleteRecentV'), grab('yesComplete'), grab('m_reasonNotCompleteRecentV'));
	}
	else {
		grab('m_didCompleteTreatRecentV').value = 'False';
		grab('m_reasonNotCompleteRecentV').value = 'N/A';
	}
	// subPost1('text', grab('yesTreated'), grab('yesComplete'), grab('reasonNotCompleteRecentV'), grab('m_didCompleteTreatRecentV'), grab('m_reasonNotCompleteRecentV'));
}

//AM ANGER HISTORY SECTION II FUNCTIONS
function explainDep() {
	twoElementRadioSetup(grab('yesDepress'), grab('lab1'), grab('depress30ExplainRecentV'));
}

function tensionRadio() {
	twoElementRadioSetup(grab('yesAnx'), grab('lab2'), grab('anxietyExplainRecentV'));
}

function halluRadio() {
	twoElementRadioSetup(grab('yesHall'), grab('lab3'), grab('hallucinationLastV'));
}

function troubleRadioAH2() {
	twoElementRadioSetup(grab('yesTrouble'), grab('lab4'), grab('understandingExplainRecentV'));
}

function troubleControlAH2() {
	twoElementRadioSetup(grab('yesControl'), grab('lab5'), grab('lastTimeTroubleControl'));
	twoElementRadioSetup(grab('yesControl'), grab('lab6'), grab('controlTrigger'));
}

function suicide30recent() { //top level radio button
	twoElementRadioSetup(grab('yesSuicide'), grab('lab7'), grab('suicide30ExplainRecentV'));
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


function post_am_dynamic2() {
	post(true, 'text', grab('depress30ExplainRecentV'), grab('yesDepress'), grab('m_depress30ExplainRecentV'));
	post(true, 'text', grab('anxietyExplainRecentV'), grab('yesAnx'), grab('m_anxietyExplainRecentV'));
	post(true, 'text', grab('hallucinationLastV'), grab('yesHall'), grab('m_hallucinationLastV'));
	post(true, 'text', grab('understandingExplainRecentV'), grab('yesTrouble'), grab('m_understandingExplainRecentV'));
	post(true, 'text', grab('lastTimeTroubleControl'), grab('yesControl'), grab('m_lastTimeTroubleControl'));
	post(true, 'text', grab('controlTrigger'), grab('yesControl'), grab('m_controlTrigger'));
	post(true, 'text', grab('suicide30ExplainRecentV'), grab('yesSuicide'), grab('m_suicide30ExplainRecentV'));
}


//AM ANGER HISTORY SECTION III FUNCTIONS
function homicidalRadio() {
	twoElementRadioSetup(grab('yesHomicide'), grab('lab1'), grab('homicidalExplain'));
}

function ah3number1() {
	twoElementRadioSetup(grab('yesMed'), grab('lab2'), grab('medRecentVExplain'));
	twoElementRadioSetup(grab('yesMed'), grab('lab3'), grab('yesSuccess'));
	twoElementRadioSetup(grab('yesMed'), grab('lab4'), grab('noSuccess'));
	twoElementRadioSetup(grab('yesMed'), grab('lab5'), grab('noSuccess'));
	twoElementRadioSetup(grab('yesMed'), grab('lab4'), grab('noSuccess'));

	if (grab('noMed').checked === true) {
		grab('noSuccess').checked = true;
	}

	ah3number2();
}

function ah3number2() {
	twoElementRadioSetup(grab('yesSuccess'), grab('lab6'), grab('medSuccessExplainRecentV'));
}

function post_dynamic_am_ah3() {
	post(true, 'text', grab('homicidalExplain'), grab('yesHomicide'), grab('m_homicidalExplain'));
	post(true, 'text', grab('medRecentVExplain'), grab('yesMed'), grab('m_medRecentVExplain'));
	subPost1('text', grab('yesMed'), grab('yesSuccess'), grab('medSuccessExplainRecentV'), grab('m_medSuccessRecentV'), grab('m_medSuccessExplainRecentV'));
	// subPost1('text', grab('yesMed'), grab('yesSuccess'), grab('medSuccessExplainRecentV'), grab('medSuccessRecentV'), grab('m_medSuccessExplainRecentV'));
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

function am_suicide_pop() {
	var w = 550, h = 500;
	openPopUp('auto', '/am_angerHistory2_suicide/', w, h);
}

function initializeAmSuicide(data) {
	setRadioElement(data.suicideTodayRecentV, grab('yesSuicide'), grab('noSuicide'));
	setRadioElement(data.suicideTodayPlanRecentV, grab('yesPlan'), grab('noPlan'));
	setRadioElement(data.hasAttemptedSuicide, grab('yesAttempt'), grab('noAttempt'));
	blank_init(data.isComplete, grab('suicideTodayExplainRecentV'));
	blank_init(data.isComplete, grab('hasAttemptedExplainRecentV'));

	am_suicide_radio1();
	am_suicide_radio2();
	am_suicide_radio3();
}

function am_suicide_radio1() {
	if (grab('yesSuicide').checked === true) {
		opacityHigh(grab('yesPlan'));
		opacityHigh(grab('noPlan'));
		opacityHigh(grab('label1'));
		opacityHigh(grab('subLab1'));
		opacityHigh(grab('subLab2'));
		grab('yesPlan').disabled = false;
		grab('noPlan').disabled = false;
	}
	else {
		grab('noPlan').checked = true;
		opacityLow(grab('yesPlan'));
		opacityLow(grab('noPlan'));
		opacityLow(grab('label1'));
		opacityLow(grab('subLab1'));
		opacityLow(grab('subLab2'));
		grab('yesPlan').disabled = true;
		grab('noPlan').disabled = true;
		am_suicide_radio2();
	}
}

function am_suicide_radio2() {
	twoElementRadioSetup(grab('yesPlan'), grab('lab2'), grab('suicideTodayExplainRecentV'));
}

function am_suicide_radio3() {
	twoElementRadioSetup(grab('yesAttempt'), grab('lab3'), grab('hasAttemptedExplainRecentV'));
}


function saveSuicideExtras() {
	var fields = fetchSpecial2_am();
	var hasErrors = null;

	for (var i = 0; i < fields.length; i++) {
		hasErrors = hasTextError(fields[i]);

		if (hasErrors === true) {
			break;
		}
	}

	if (hasErrors === true) {
		for (var j = 0; j < fields.length; j++) {
			textErrorChecker(fields[j]);
		}

		var w = 500, h = 500;
		openPopUp('auto', '/generateErrors/', w, h);
	}
	else {
		determineBool(grab('yesSuicide'), getPopParent('suicideTodayRecentV'));
		determineBool(grab('yesAttempt'), getPopParent('hasAttemptedSuicide'));

		if (grab('yesSuicide').checked === true) {
			determineBool(grab('yesPlan'), getPopParent('suicideTodayPlanRecentV'));
			postToWindowParent('yesPlan', 'suicideTodayExplainRecentV', 'suicideTodayExplainRecentV');
		}
		else {
			getPopParent('suicideTodayExplainRecentV').value = 'N/A';
			getPopParent('suicideTodayPlanRecentV').value = 'False';
		}

		postToWindowParent('yesAttempt', 'hasAttemptedExplainRecentV', 'hasAttemptedExplainRecentV');

		getPopParent('superBtn').innerHTML = " <button onClick=\"javascript: continue_am_form(\'/am_angerHistory2/\'); return false;\">Save & Continue</button>";
		getPopParent('superBtn').className = 'pro-iml-btn';
		window.close();
	}
}


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//*********************************************************** SAP FUNCTIONS ***********************************************************//
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function initialize_sap(section, json_data) {
	section = String(section);

	if (section === '/sap_demographic/') {
		init_sap_demo(json_data);
	}
	else if (section === '/sap_social/') {
		init_sap_social(json_data);
	}
	else if (section === '/sap_psychoactive/') {
		init_sap_psych1(json_data);
	}
	else if (section === '/sap_psychoactive2/') {
		init_sap_psych2(json_data);
	}
	else if (section === '/sap_special/') {
		init_sap_special(json_data);
	}
	else if (section === '/sap_other/') {
		init_sap_other(json_data);
	}
	else if (section === '/sap_sources/') {
		init_sap_sources(json_data);
	}
	else if (section === '/sap_viewForm/') {
		init_sap_viewForm(json_data);
	}
}

function init_sap_demo(json_data) {
	blank_init(json_data.clinicalComplete, grab('problem'));
	blank_init(json_data.clinicalComplete, grab('health'));
}

function init_sap_social(json_data) {
	blank_init(json_data.socialComplete, grab('family'));
}

function init_sap_psych1(json_data) {
	blank_init(json_data.psychoComplete, grab('alcoholFrequency'));
	blank_init(json_data.psychoComplete, grab('alcoholQuantity'));
	blank_init(json_data.psychoComplete, grab('alcoholLast'));
	blank_init(json_data.psychoComplete, grab('alcoholHow'));
	number_init(json_data.psychoComplete, grab('alcoholAge'));

	blank_init(json_data.psychoComplete, grab('amphFrequency'));
	blank_init(json_data.psychoComplete, grab('amphQuantity'));
	blank_init(json_data.psychoComplete, grab('amphLast'));
	blank_init(json_data.psychoComplete, grab('amphHow'));
	number_init(json_data.psychoComplete, grab('amphAge'));

	blank_init(json_data.psychoComplete, grab('caffineFrequency'));
	blank_init(json_data.psychoComplete, grab('caffineQuantity'));
	blank_init(json_data.psychoComplete, grab('caffineLast'));
	blank_init(json_data.psychoComplete, grab('caffineHow'));
	number_init(json_data.psychoComplete, grab('caffineAge'));

	blank_init(json_data.psychoComplete, grab('weedFrequency'));
	blank_init(json_data.psychoComplete, grab('weedQuantity'));
	blank_init(json_data.psychoComplete, grab('weedLast'));
	blank_init(json_data.psychoComplete, grab('weedHow'));
	number_init(json_data.psychoComplete, grab('weedAge'));

	blank_init(json_data.psychoComplete, grab('cokeFrequency'));
	blank_init(json_data.psychoComplete, grab('cokeQuantity'));
	blank_init(json_data.psychoComplete, grab('cokeLast'));
	blank_init(json_data.psychoComplete, grab('cokeHow'));
	number_init(json_data.psychoComplete, grab('cokeAge'));

	blank_init(json_data.psychoComplete, grab('hallFrequency'));
	blank_init(json_data.psychoComplete, grab('hallQuantity'));
	blank_init(json_data.psychoComplete, grab('hallLast'));
	blank_init(json_data.psychoComplete, grab('hallHow'));
	number_init(json_data.psychoComplete, grab('hallAge'));

	blank_init(json_data.psychoComplete, grab('inhaleFrequency'));
	blank_init(json_data.psychoComplete, grab('inhaleQuantity'));
	blank_init(json_data.psychoComplete, grab('inhaleLast'));
	blank_init(json_data.psychoComplete, grab('inhaleHow'));
	number_init(json_data.psychoComplete, grab('inhaleAge'));

	blank_init(json_data.psychoComplete, grab('smokeFrequency'));
	blank_init(json_data.psychoComplete, grab('smokeQuantity'));
	blank_init(json_data.psychoComplete, grab('smokeLast'));
	blank_init(json_data.psychoComplete, grab('smokeHow'));
	number_init(json_data.psychoComplete, grab('smokeAge'));

	blank_init(json_data.psychoComplete, grab('opFrequency'));
	blank_init(json_data.psychoComplete, grab('opQuantity'));
	blank_init(json_data.psychoComplete, grab('opLast'));
	blank_init(json_data.psychoComplete, grab('opHow'));
	number_init(json_data.psychoComplete, grab('opAge'));

	blank_init(json_data.psychoComplete, grab('pcpFrequency'));
	blank_init(json_data.psychoComplete, grab('pcpQuantity'));
	blank_init(json_data.psychoComplete, grab('pcpLast'));
	blank_init(json_data.psychoComplete, grab('pcpHow'));
	number_init(json_data.psychoComplete, grab('pcpAge'));

	blank_init(json_data.psychoComplete, grab('sedFrequency'));
	blank_init(json_data.psychoComplete, grab('sedQuantity'));
	blank_init(json_data.psychoComplete, grab('sedLast'));
	blank_init(json_data.psychoComplete, grab('sedHow'));
	number_init(json_data.psychoComplete, grab('sedAge'));

	blank_init(json_data.psychoComplete, grab('otherFrequency'));
	blank_init(json_data.psychoComplete, grab('otherQuantity'));
	blank_init(json_data.psychoComplete, grab('otherLast'));
	blank_init(json_data.psychoComplete, grab('otherHow'));
	number_init(json_data.psychoComplete, grab('otherAge'));
}

function init_sap_psych2(json_data) {
	blank_init(json_data.psycho2Complete, grab('psychoactive'));
}

function init_sap_special(json_data) {
	blank_init(json_data.specialComplete, grab('special'));

	initializeAllCheckBoxes(json_data.isChild, grab('isChild'));
	initializeAllCheckBoxes(json_data.isSenior, grab('isSenior'));
	initializeAllCheckBoxes(json_data.isDual, grab('isDual'));
	initializeAllCheckBoxes(json_data.isOther, grab('isOther'));
	initializeAllCheckBoxes(json_data.isNone, grab('isNone'));

	disable_sap_special();
}

function init_sap_other(json_data) {
	blank_init(json_data.otherComplete, grab('psychological'));
	blank_init(json_data.otherComplete, grab('gambling'));
	blank_init(json_data.otherComplete, grab('abilities'));
	blank_init(json_data.otherComplete, grab('other'));
}

function init_sap_sources(json_data) {
	blank_init(json_data.sourcesComplete, grab('source1'));
	blank_init(json_data.sourcesComplete, grab('source2'));
	blank_init(json_data.sourcesComplete, grab('relationship1'));
	blank_init(json_data.sourcesComplete, grab('relationship2'));
}

function init_sap_viewForm(json_data) {
	
}


function postSapFields(page) {
	page = String(page);

	if (page === '/sap_demographic/') {
		postSapDemo();
	}
	else if (page === '/sap_social/') {
		postSapSocial();
	}
	else if (page === '/sap_psychoactive/') {
		postSapPsycho1();
	}
	else if (page === '/sap_psychoactive2/') {
		postSapPsycho2();
	}
	else if (page === '/sap_special/') {
		postSapSpecial();
	}
	else if (page === '/sap_other/') {
		postSapOther();
	}
	else if (page === '/sap_sources/') {
		postSapSources();
	}
	else if (page === '/sap_viewForm/') {
		postSapViewForm();
	}
}

function uni_sap_proceed(section) {
	section = String(section);
	var hasErrors 	= superDuperSapHasErrors(section);

	if (hasErrors === true) {
		var w = 500;
		superDuperSapChecker(section);
		openPopUp('auto', '/generateErrors/', w, w);
	}
	else {
		postSapFields(section);
		var form 		= grab('sap_form');
		var next_url 	= grab('next_url');

		grab('save_this').value = 'true';
		form.action 			= next_url.value;
		form.submit();
	}
}

// function post(isDynamic, field_type, field, trigger, target)

function postSapDemo() {
	post(false, 'text', grab('problem'), null, null);
	post(false, 'text', grab('health'), null, null);
}

function postSapSocial() {
	post(false, 'text', grab('family'), null, null);
}

function postSapPsycho1() {
	post(false, 'text', grab('alcoholFrequency'), null, null);
	post(false, 'text', grab('alcoholQuantity'), null, null);
	post(false, 'text', grab('alcoholLast'), null, null);
	post(false, 'text', grab('alcoholHow'), null, null);
	post(false, 'number', grab('alcoholAge'), null, null);

	post(false, 'text', grab('amphFrequency'), null, null);
	post(false, 'text', grab('amphQuantity'), null, null);
	post(false, 'text', grab('amphLast'), null, null);
	post(false, 'text', grab('amphHow'), null, null);
	post(false, 'number', grab('amphAge'), null, null);

	post(false, 'text', grab('caffineFrequency'), null, null);
	post(false, 'text', grab('caffineQuantity'), null, null);
	post(false, 'text', grab('caffineLast'), null, null);
	post(false, 'text', grab('caffineHow'), null, null);
	post(false, 'number', grab('caffineAge'), null, null);

	post(false, 'text', grab('weedFrequency'), null, null);
	post(false, 'text', grab('weedQuantity'), null, null);
	post(false, 'text', grab('weedLast'), null, null);
	post(false, 'text', grab('weedHow'), null, null);
	post(false, 'number', grab('weedAge'), null, null);

	post(false, 'text', grab('cokeFrequency'), null, null);
	post(false, 'text', grab('cokeQuantity'), null, null);
	post(false, 'text', grab('cokeLast'), null, null);
	post(false, 'text', grab('cokeHow'), null, null);
	post(false, 'number', grab('cokeAge'), null, null);

	post(false, 'text', grab('hallFrequency'), null, null);
	post(false, 'text', grab('hallQuantity'), null, null);
	post(false, 'text', grab('hallLast'), null, null);
	post(false, 'text', grab('hallHow'), null, null);
	post(false, 'number', grab('hallAge'), null, null);

	post(false, 'text', grab('inhaleFrequency'), null, null);
	post(false, 'text', grab('inhaleQuantity'), null, null);
	post(false, 'text', grab('inhaleLast'), null, null);
	post(false, 'text', grab('inhaleHow'), null, null);
	post(false, 'number', grab('inhaleAge'), null, null);

	post(false, 'text', grab('smokeFrequency'), null, null);
	post(false, 'text', grab('smokeQuantity'), null, null);
	post(false, 'text', grab('smokeLast'), null, null);
	post(false, 'text', grab('smokeHow'), null, null);
	post(false, 'number', grab('smokeAge'), null, null);

	post(false, 'text', grab('opFrequency'), null, null);
	post(false, 'text', grab('opQuantity'), null, null);
	post(false, 'text', grab('opLast'), null, null);
	post(false, 'text', grab('opHow'), null, null);
	post(false, 'number', grab('opAge'), null, null);

	post(false, 'text', grab('pcpFrequency'), null, null);
	post(false, 'text', grab('pcpQuantity'), null, null);
	post(false, 'text', grab('pcpLast'), null, null);
	post(false, 'text', grab('pcpHow'), null, null);
	post(false, 'number', grab('pcpAge'), null, null);

	post(false, 'text', grab('sedFrequency'), null, null);
	post(false, 'text', grab('sedQuantity'), null, null);
	post(false, 'text', grab('sedLast'), null, null);
	post(false, 'text', grab('sedHow'), null, null);
	post(false, 'number', grab('sedAge'), null, null);

	post(false, 'text', grab('otherFrequency'), null, null);
	post(false, 'text', grab('otherQuantity'), null, null);
	post(false, 'text', grab('otherLast'), null, null);
	post(false, 'text', grab('otherHow'), null, null);
	post(false, 'number', grab('otherAge'), null, null);
}

function postSapPsycho2() {
	post(false, 'text', grab('psychoactive'), null, null);
}

function postSapSpecial() {
	if (String(special.value) === '' || String(special.value) === null) {
		m_special.value = 'N/A';
	}
	else {
		m_special.value = special.value;
	}

	postCheckboxValue(grab('isChild'), grab('m_isChild'));
	postCheckboxValue(grab('isSenior'), grab('m_isSenior'));
	postCheckboxValue(grab('isDual'), grab('m_isDual'));
	postCheckboxValue(grab('isOther'), grab('m_isOther'));
	postCheckboxValue(grab('isNone'), grab('m_isNone'));
}

function postSapOther() {
	post(false, 'text', grab('psychological'), null, null);
	post(false, 'text', grab('gambling'), null, null);
	post(false, 'text', grab('abilities'), null, null);
	post(false, 'text', grab('other'), null, null);
}

function postSapSources() {
	post(false, 'text', grab('source1'), null, null);
	post(false, 'text', grab('source2'), null, null);
	post(false, 'text', grab('relationship1'), null, null);
	post(false, 'text', grab('relationship2'), null, null);
}

function postSapViewForm() {
	
}

function reverseCheckBox(trigger, label, field) {
	if (trigger.checked === true) {
		opacityLow(label);
		opacityLow(field);
		field.checked = false;
		field.disabled = true;
	}
	else {
		opacityHigh(label);
		opacityHigh(field);
		field.disabled = false;
	}
}

function killCheckboxSubText(trigger, label, textarea) {
	if (trigger.checked === true) {
		opacityLow(label);
		opacityLow(textarea);
		textarea.value = '';
		textarea.disabled = true;
	}
	else {
		opacityHigh(label);
		opacityHigh(textarea);
		textarea.disabled = false;
	}
}

function disable_sap_special() {
	reverseCheckBox(grab('isNone'), grab('label1'), grab('isChild'));
	reverseCheckBox(grab('isNone'), grab('label2'), grab('isSenior'));
	reverseCheckBox(grab('isNone'), grab('label3'), grab('isDual'));
	reverseCheckBox(grab('isNone'), grab('label4'), grab('isOther'));
	killCheckboxSubText(grab('isNone'), grab('label5'), grab('special'));
}

function continue_to_sap_form() {
	grab('sap_instructions').submit();
}



//#####################################################################################################################//
//*********************************************************************************************************************//
//-------------------------------------------------- MH FUNCTIONS -----------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//

function mh_initialize(section, json_data) {
	section = String(section);

	if (section == '/mh_demographic/') {
		d_init_mh_demo(json_data);
	}
	else if (section == '/mh_education/') {
		initialize_mh_education(json_data);
	}
	else if (section == '/mh_background/') {
		initialize_mh_background(json_data);
	}
	else if (section == '/mh_stress/') {
		initialize_mh_stress(json_data);
	}
	else if (section == '/mh_familyHistory/') {
		initialize_mh_family(json_data);
	}
	else if (section == '/mh_legal/') {
		initialize_mh_legal(json_data);
	}
	else if (section == '/mh_psych/') {
		d_init_mh_psych(json_data);
	}
	else if (section == '/mh_useTable/') {
		initialize_mh_use(json_data);
	}
}

function eval_parent(yesName, typeName) {
	var yesRadio = grab(yesName);
	var element = grab(typeName);

	if (yesRadio.checked === true) {
		element.innerHTML = 'Age:';
	}
	else {
		element.innerHTML = 'Age at Death:';
	}
}

function d_init_mh_demo(json_data) {
	blank_init(json_data.isComplete, grab('birthplace'));
	blank_init(json_data.isComplete, grab('raised'));
	blank_init(json_data.isComplete, grab('occupation'));
	blank_init(json_data.isComplete, grab('employer'));
	blank_init(json_data.isComplete, grab('pastJobs'));
	blank_init(json_data.isComplete, grab('recentMove'));
	blank_init(json_data.isComplete, grab('spouseOccupation'));
	blank_init(json_data.isComplete, grab('spouseEmployer'));
	blank_init(json_data.isComplete, grab('motherOccupation'));
	blank_init(json_data.isComplete, grab('motherCity'));
	blank_init(json_data.isComplete, grab('fatherOccupation'));
	blank_init(json_data.isComplete, grab('fatherCity'));

	number_init(json_data.isComplete, grab('numMarriages'));
	number_init(json_data.isComplete, grab('employedMo'));
	number_init(json_data.isComplete, grab('employedYrs'));
	number_init(json_data.isComplete, grab('spouseAge'));
	number_init(json_data.isComplete, grab('spouseWorkMos'));
	number_init(json_data.isComplete, grab('spouseWorkYrs'));
	number_init(json_data.isComplete, grab('motherAge'));
	number_init(json_data.isComplete, grab('fatherAge'));

	motherState.selectedIndex = json_data.motherState;
	fatherState.selectedIndex = json_data.fatherState;

	if (String(json_data.maritalStatus) === 'Married') {
		grab('married').checked = true;
	}
	else if (String(json_data.maritalStatus) === 'Divorced') {
		grab('divorced').checked = true;
	}
	else if (String(json_data.maritalStatus) === 'Widowed') {
		grab('widowed').checked = true;
	}
	else if (String(json_data.maritalStatus) === 'Seperated') {
		grab('seperated').checked = true;
	}
	else {
		grab('single').checked = true;
	}

	if (isBlankText(json_data.sisters) === true || String(json_data.sisters) === 'N/A') {
		grab('noSister').checked = true;
		grab('m_sistersFinal').value = 'N/A';
	}
	else {
		grab('yesSister').checked = true;
	}

	if (isBlankText(json_data.bothers) === true || String(json_data.bothers) === 'N/A') {
		grab('noBrother').checked = true;
		grab('m_brothersFinal').value = 'N/A';
	}
	else {
		grab('yesBrother').checked = true;
	}

	if ((isBlankText(json_data.childrenMale) === true && isBlankText(json_data.childrenFemale) === true) || (String(json_data.childrenMale) === 'N/A' && String(json_data.childrenFemale) === 'N/A')) {
		grab('noChild').checked = true;
		grab('childrenFemale').value = 'N/A';
		grab('childrenMale').value = 'N/A';
	}
	else {
		grab('yesChild').checked = true;
	}

	setRadioElement(json_data.motherLiving, grab('momIsLiving'), grab('momNotLiving'));
	setRadioElement(json_data.fatherLiving, grab('dadIsLiving'), grab('dadNotLiving'));

	if (String(json_data.motherAge) === '0') {
		grab('motherAge').value = String(json_data.motherAgeDeath);
	}

	if (String(json_data.fatherAge) === '0') {
		grab('fatherAge').value = String(json_data.fatherAgeDeath);
	}

	mhSpouse();
	eval_parent('momIsLiving', 'mom_age_type');
	eval_parent('dadIsLiving', 'dad_age_type');
}

function build_op_radio(relative, title, radioDivName, labelDivName) {
	var error = '';
	radioDivName 	= String(radioDivName);
	labelDivName 	= String(labelDivName);	
	relative 		= String(relative);	
	title 			= String(title);

	if (relative === 'child') {
		error = 'e_c';
	}

	else if (relative === 'brother') {
		error = 'e_b';
	}

	else if (relative === 'sister') {
		error = 'e_s';
	}

	var radio_div = grab(radioDivName);
	var label_div = grab(labelDivName);

	var label_Html = "<div id=\"" + error + "\"><div class=\'new_radio_iml_label\'>" + title + "</div></div>";

	var radio_Html = "<div><input type=\'radio\' name=\'relationship\' id=\'" + relative + "\' value=\'" + relative + "\' \
	onClick=\"javascript: change_relative_radio(\'" + relative + "\');\"></div>";

	label_div.innerHTML = label_Html;
	radio_div.innerHTML = radio_Html;
}

function set_op_relativeRadio() {
	var hasChildren = getPopParent('yesChild').checked;
	var hasSisters = getPopParent('yesSister').checked;
	var hasBrothers = getPopParent('yesBrother').checked;
	var radios = [];

	if (hasChildren === true) {
		var data1 = {}
		data1['field'] = grab('child');
		data1['value'] = 'child';
		radios.push(data1);
	}

	if (hasSisters === true) {
		var data2 = {}
		data2['field'] = grab('sister');
		data2['value'] = 'sister';
		radios.push(data2);
	}

	if (hasBrothers === true) {
		var data3 = {}
		data3['field'] = grab('brother');
		data3['value'] = 'brother';
		radios.push(data3);
	}

	radios[0]['field'].checked = true;
	change_relative_radio(radios[0]['value']);
	set_m_op_gender();
}

function set_m_op_gender() {
	if(grab('male').checked === true) {
		grab('m_gender').value = 'Male';
	}
	else {
		grab('m_gender').value = 'Female';
	}
}


function change_relative_radio(selectedName) {
	name = String(selectedName);
	var age_label = grab('age_label');
	
	if (name === 'child') {
		age_label.innerHTML = "Child\'s Age:";
		grab('gender_div_iml').style.opacity = '1.0';
		grab('selectedRel').value = 'Child';
	}
	else if (name === 'sister') {
		age_label.innerHTML = "Sister\'s Age:";
		grab('gender_div_iml').style.opacity = '0.0';
		grab('selectedRel').value = 'Sister';
	}
	else if (name === 'brother') {
		age_label.innerHTML = "Brother\'s Age:";
		grab('gender_div_iml').style.opacity = '0.0';
		grab('selectedRel').value = 'Brother';
	}

	grab('e_city').className = '';
	grab('e_state').className = '';
	grab('e_age').className = '';

	grab('age').value = 0;
	grab('city').value = '';
	grab('state').selectedIndex = 0;
}

function snag_indexed_item_mhOp(index) {
	var select = fetchSelectedOpElement_mh(index);
	clear_op_selected_mh();
	select['div'].className = 'selected_op_iml';
}

function clear_selected_opElement(index) {
	var select = fetchSelectedOpElement_mh(index);
	clear_op_selected_mh();
	select['div'].className = 'selected_op_iml';
}

function grab_selected_opElement(index) {
	index = Number(index);
	var loc = index + 1;
	var divName = 'item_' + String(loc);
	var div = grab(divName);
	grab('currently_selected').value = index;
	return div;
}

function highlightOpSelection_m(index) {
	var element = grab_selected_opElement(index);
	ClearAllOpFields_data();
	element.className = 'selected_op_iml';
	grab('currently_selected').value = index;
}


function ClearAllOpFields_data() {
	var listSize = Number(grab('num_items').value); 

	for (var i = 0; i < listSize; i++) {
		var element = grab_selected_opElement(i);
		element.className = 'iml_normal_nonOp';
	}
}

function fetchSelectedOpElement_mh(index) {
	var e_list = fetch_opBuilder_elements();
	index = Number(index);
	grab('currently_selected').value = index;
	return e_list[index];
}

function remove_commas(text) {
	var result = '';
	text = String(text);

	for (var i = 0; i < text.length; i++) {
		if (text.charAt(i) !== ',') {
			result += text.charAt(i);
		}
	}

	return result;
}

function getSingleOpData(index) {
	index = Number(index);
	spec = String(index + 1);
	var div_id = 'item_' + spec;
	var div = grab(div_id);
	var city_id = 'city_' + spec;
	var city_div = grab(city_id);
	var state_id = 'state_' + spec;
	var state_div = grab(state_id);
	var age_id = 'age_' + spec;
	var age_div = grab(age_id);
	var type_id = 'type_' + spec;
	var type_div = grab(type_id);

	var city = remove_commas(city_div.innerHTML);
	var state = state_div.innerHTML;
	var type = type_div.innerHTML;
	var age = numbersOnly(age_div.innerHTML);

	data = {};
	data['age'] = age;
	data['g_type'] = type;
	data['city'] = city;
	data['state'] = state;

	return data;
}

function getOpBuilderArray() {
	var result = [];
	var size = Number(grab('num_items').value);
	var start = size - 1;
	var spec = size;

	for (var i = 0; i < size; i++) {
		var item = getSingleOpData(start);
		result.push(item);
		start = start - 1;
		spec = spec - 1;
	}
	return result;
}

function reset_opItem_ids(new_list) {
	var size = new_list.length;
	var spec = size;
	var index = size - 1;

	for (var i = 0; i < size; i ++) {
		new_list[i]['age_id'] = 'age_' + String(spec);
		new_list[i]['type_id'] = 'type_' + String(spec);
		new_list[i]['city_id'] = 'city_' + String(spec);
		new_list[i]['state_id'] = 'state_' + String(spec);
		new_list[i]['item_id'] = 'item_' + String(spec);
		new_list[i]['index'] = index;
		spec -= 1;
		index -= 1;
	}

	return new_list;
}


function supremeOpListBuilder(eList, isInitial) {
	var html = '';
	var heading = "<table>";
	var tail = "</table>";
	var size = eList.length;
	var highlight = size - 1;

	grab('num_items').value = size;

	if (isInitial === true) {
		for (var i = 0; i < eList.length; i++) {
			html += singleOpElementBuilder(eList[i]);
		}

		var render = heading + html + tail;

		grab('item_builder').innerHTML = render;
		highlightOpSelection_m(highlight);
	}

	else {
		for (var j = 0; j < eList.length; j++) {
			html += singleOpElementBuilder(eList[j]);
		}

		var new_index = Number(grab('currently_selected').value);
		var render2 = heading + html + tail;
		grab('item_builder').innerHTML = render2;

		if (grab('math_type').value === 'add') {
			new_index = Number(eList[0]['index']);
		}
		else {
			if (new_index !== 0) {
				new_index -= 1;
			}
		}

		highlightOpSelection_m(new_index);
	}
}

function singleOpElementBuilder(item) {
	var html = "<tr>\
	<td>\
	<a href=\"javascript: highlightOpSelection_m(\'" + item['index'] + "\');\">\
	<div id=\"" + item['item_id'] + "\" class=\"iml_normal_nonOp\">\
	<table>\
	<tr>\
	<td>\
	<div class=\"opPosition1\" name=\"" + item['type_id']  + "\" id=\"" + item['type_id'] + "\" value=\'" + item['g_type'] + "\'>" + item['g_type'] + "</div>\
	</td>\
	<td><div class=\"opPosition2\" name=\"" + item['age_id'] + "\" id=\"" + item['age_id'] + "\" value=\'" + item['age'] + "\'><span>Age:" + item['age'] + "</span></div><td>\
	<td><div class=\'opPosition2\' name=\'" + item['city_id'] + "\' id=\'" + item['city_id'] + "\' value=\'" + item['city'] + "\'>" + item['city'] + ", </div></td>\
	<td><div class=\'opPosition2\' name=\'" + item['state_id'] + "\' id=\'" + item['state_id'] + "\' value=\'" + item['state'] + "\'>" + item['state'] + "</div></td>\
	</tr>\
	</table>\
	</div>\
	</a>\
	</td>\
	</tr>"

	return html;
}


function build_op_item_list() {
	var m_gender = '';
	var selectedRel = String(grab('selectedRel').value);
	var age = String(grab('age').value);
	var city = String(grab('city').value);
	var state = String(grab('state').value);
	var old_html = String(grab('item_builder').innerHTML);
	var index = Number(grab('num_items').value);
	var num_items = index + 1;
	grab('num_items').value = num_items;
	index = String(index);
	var new_id = 'item_' + String(num_items);
	var age_id = 'age_' + String(num_items);
	var type_id = 'type_' + String(num_items);
	var city_id = 'city_' + String(num_items);
	var state_id = 'state_' + String(num_items);
	var gender_id = 'gender_' + String(num_items);
	grab('currently_selected').value = index;

	if (selectedRel === 'Child') {
		m_gender = String(grab('m_gender').value);
	}

	var html = "<div class=\'selected_op_iml\' id=\'" + new_id + "\'>\
	<a href=\"javascript: snag_indexed_item_mhOp(\'" + index + "\');\">\
	<input type=\'hidden\' name=\'" + age_id + "\' id=\'" + age_id + "\' value=\'" + age + "\'>\
	<input type=\'hidden\' name=\'" + type_id + "\' id=\'" + type_id + "\' value=\'" + selectedRel + "\'>\
	<input type=\'hidden\' name=\'" + city_id + "\' id=\'" + city_id + "\' value=\'" + city + "\'>\
	<input type=\'hidden\' name=\'" + state_id + "\' id=\'" + state_id + "\' value=\'" + state + "\'>\
	<input type=\'hidden\' name=\'" + gender_id + "\' id=\'" + gender_id + "\' value=\'" + m_gender + "\'>\
	<table>\
	<tr>\
	<td><div class=\'opPosition1\'>" + m_gender + "</div></td>\
	<td><div class=\'opPosition1\'>" + selectedRel + "</div></td>\
	<td><div class=\'opPosition2\' style=\'margin-left:10px;\'><span>Age:" + age + "</span></div></td>\
	<td><div class=\'opPosition2\' style=\'margin-left:10px;\'>" + city + ", </div></td>\
	<td><div class=\'opPosition2\'>" + state + "</div></td>\
	</tr>\
	</table>\
	</a>\
	</div>";

	var new_html = html + old_html;
	grab('item_builder').innerHTML = new_html;
}

function initialize_mhDemoOps_compact(json_data) {
	var hasChildren = getPopParent('yesChild').checked;
	var hasSisters = getPopParent('yesSister').checked;
	var hasBrothers = getPopParent('yesBrother').checked;

	if (hasBrothers === true) {
		build_op_radio('brother', 'Brother', 'brother_builder', 'brother_header');
	}

	if (hasSisters === true) {
		build_op_radio('sister', 'Sister', 'sister_builder', 'sister_header');
	}

	if (hasChildren === true) {
		build_op_radio('child', 'Child', 'child_builder', 'child_header');
	}

	set_op_relativeRadio();

	//HERE BREAK UP EXISTING PARTS AND CREATE LIST
	var eList = preliminaryOpBuilder_mh(json_data);
	grab('num_items').value = String(eList.length);
	supremeOpListBuilder(eList, true);

	set_op_relative_values();

}

function seperateOpText_mh(text) {
	result = [];
	var t = '';
	text = String(text);

	for (var i = 0; i < text.length; i++) {
		if (text.charAt(i) === '~') {
			result.push(t);
			t = '';
		}
		else {
			t += text.charAt(i);
		}
	}

	return result;
}

function decodeAndBuild_mh(text) {
	var result = [];
	var dList = seperateOpText_mh(text);

	for (var i = 0; i < dList.length; i++) {
		m_text = dList[i];
		var data = {};
		var i_city = 0;
		var i_state = 0;
		var type = m_text.charAt(0);
		var age = '';
		var city = '';
		var state = '';
		var g_type = null;

		for (var j = 1; j < m_text.length; j++) {
			if (m_text.charAt(j) === '/') {
				i_city = j + 1;
				break;
			}
			else {
				age += m_text.charAt(j);
			}
		}

		for(var k = i_city; k < m_text.length; k++) {
			if (m_text.charAt(k) === ',') {
				i_state = k + 1;
				break;
			}
			else {
				city += m_text.charAt(k);
			}
		}

		for (var l = i_state; l < m_text.length; l++) {
			state += m_text.charAt(l);
		}

		if (type === 'f') {
			g_type = 'Female Child';
		}
		else if (type === 'm') {
			g_type = 'Male Child';
		}
		else if (type === 's') {
			g_type = 'Sister';
		}
		else if (type === 'b') {
			g_type = 'Brother';
		}

		data['g_type'] = g_type;
		data['type'] = type;
		data['age'] = age;
		data['city'] = city;
		data['state'] = state;
		result.push(data);
	}

	return result;
}

function fetch_itemized_opElement(text) {
	var eList = decodeAndDestroy_mh(text);

	for (var i = 0; i < eList.length; i++) {
		var v_curr = i + 1;
		eList[i]['age_id'] = 'age_' + String(v_curr);
		eList[i]['city_id'] = 'city_' + String(v_curr);
		eList[i]['type_id'] = 'type_' + String(v_curr);
		eList[i]['item_id'] = 'item_' + String(v_curr);
		eList[i]['state_id'] = 'state_' + String(v_curr);
		eList[i]['index'] = 0;
	}

	return eList;
}

function preliminaryOpBuilder_mh(json_data) {
	var result = [];
	var m = decodeAndBuild_mh(String(json_data.male));
	var f = decodeAndBuild_mh(String(json_data.female));
	var s = decodeAndBuild_mh(String(json_data.sister));
	var b = decodeAndBuild_mh(String(json_data.brother));
	
	if (getPopParent('yesChild').checked === true) {
		for (var i = 0; i < m.length; i++) {
			result.push(m[i]);
		}
	}

	if (getPopParent('yesChild').checked === true) {
		for (var j = 0; j < f.length; j++) {
			result.push(f[j]);
		}
	}

	if (getPopParent('yesSister').checked === true) {
		for (var k = 0; k < s.length; k++) {
			result.push(s[k]);
		}
	}

	if (getPopParent('yesBrother').checked === true) {
		for (var l = 0; l < b.length; l++) {
			result.push(b[l]);
		}
	}

	var v_curr = Number(result.length);

	for (var n = 0; n < result.length; n++) {
		var age_id = 'age_' + String(v_curr);
		var type_id = 'type_' + String(v_curr);
		var city_id = 'city_' + String(v_curr);
		var state_id = 'state_' + String(v_curr);
		var item_id = 'item_' + String(v_curr);
		var gender_id = 'gender_' + String(v_curr);

		result[n]['gender_id'] = gender_id;
		result[n]['age_id'] = age_id;
		result[n]['type_id'] = type_id;
		result[n]['city_id'] = city_id;
		result[n]['state_id'] = state_id;
		result[n]['item_id'] = item_id;
		result[n]['index'] = String(v_curr - 1);

		v_curr = v_curr - 1;
	}

	return result;
}


function fetch_opBuilder_elements() {
	var result = [];
	var numElements = Number(grab('num_items').value);

	for (var i = 0; i < numElements; i++) {
		var index = i + 1;
		var data = {};
		var entry = '';
		var age_id = 'age_' + String(index);
		var type_id = 'type_' + String(index);
		var city_id = 'city_' + String(index);
		var state_id = 'state_' + String(index);
		var gender_id = 'gender_' + String(index);
		var div_id = 'item_' + String(index);

		var g_type = null;

		var age = String(grab(age_id).value);
		var type = String(grab(type_id).value);
		var city = String(grab(city_id).value);
		var state = String(grab(state_id).value);
		var gender = String(grab(gender_id).value);
		var div = grab(div_id);

		if (gender === 'Male') {
			g_type = 'm';
		}
		else if (gender === 'Female') {
			g_type = 'f';
		}

		if (type === 'Sister') {
			g_type = 's';
		}
		else if (type === 'Brother') {
			g_type = 'b';
		}

		entry = age + '/' + city + ', ' + state;

		data['item'] = entry;
		data['type'] = g_type;
		data['div'] = div;
		result.push(data);
	}

	return result;
}

function clear_op_selected_mh() {
	var elements = fetch_opBuilder_elements();

	for (var i = 0; i < elements.length; i++) {
		elements[i]['div'].className = '';
	}
}

function determine_opList_initialization(g_type) {
	var initialize = false;
	g_type = String(g_type);

	if (g_type === 'Male Child') {
		var blank_m = String(getPopParent('childrenMale').value);

		if (blank_m === 'N/A') {
			initialize = true;
		}
	}

	else if (g_type === 'Female Child') {
		var blank_f = String(getPopParent('childrenFemale').value);

		if (blank_f === 'N/A') {
			initialize = true;
		}
	}

	else if (g_type === 'Sister') {
		var blank_s = String(getPopParent('m_sistersFinal').value);

		if (blank_s === 'N/A') {
			initialize = true;
		}
	}

	else if (g_type === 'Brother') {
		var blank_b = String(getPopParent('m_brothersFinal').value);

		if (blank_b === 'N/A') {
			initialize = true;
		}
	}

	return initialize;
}

function set_op_relative_values() {
	var e = seperateElemental_op_mh();

	var m = e['m'].length;
	var f = e['f'].length;
	var s = e['s'].length;
	var b = e['b'].length;

	var num_kids = m + s;

	grab('numSisters').value = s;
	grab('numBrothers').value = b;
	grab('numKids').value = num_kids;

	if (num_kids > 0) {
		grab('e_c').className = '';
	}
	if (s > 0) {
		grab('e_s').className = '';
	}
	if (b > 0) {
		grab('e_b').className = '';
	}
}
 

function post_op_data_mh() {
	var data = seperateElemental_op_mh();
	var maleKids = final_mh_op_encoder(data['m']);
	var femaleKids = final_mh_op_encoder(data['f']);
	var sisters = final_mh_op_encoder(data['s']);
	var brothers = final_mh_op_encoder(data['b']);

	getPopParent('childrenMale').value = maleKids;
	getPopParent('childrenFemale').value = femaleKids;
	getPopParent('m_sistersFinal').value = sisters;
	getPopParent('m_brothersFinal').value = brothers;
}

function isValidNumber_no_zero_allowed(value) {
	var isValid = true;
	var test =  Number(value);

	if (test === 0) {
		isValid = false;
	}
	return isValid;
}

function op1_hasInputError() {
	var hasError = false;
	var cityBlank = isBlankText(grab('city').value);
	var state = Number(grab('state').selectedIndex);
	var age = String(grab('age').value);
	var validAge = isValidNumber_no_zero_allowed(age);

	if (state === 0 || cityBlank === true || validAge === false) {
		hasError = true;
	}

	return hasError;
}

function has_single_op_value_error(trigger, num_elements) {
	var hasError = false;
	num_elements = Number(num_elements);

	if (trigger === true && num_elements === 0) {
		hasError = true;
	}

	return hasError;
}

function op1_hasTypeError() {
	var hasError = false;
	var hasChildren = getPopParent('yesChild').checked;
	var hasSister = getPopParent('yesSister').checked;
	var hasBrother = getPopParent('yesBrother').checked;
	var num_kids = grab('numKids').value;
	var num_sisters = grab('numSisters').value;
	var num_brothers = grab('numBrothers').value;

	var ek = has_single_op_value_error(hasChildren, num_kids);
	var es = has_single_op_value_error(hasSister, num_sisters);
	var eb = has_single_op_value_error(hasBrother, num_brothers);

	if (ek === true || es === true || eb === true) {
		hasError = true;
	}

	return hasError;
}

function op1_input_errorChecker() {
	var cityError = isBlankText(grab('city').value);
	var stateError = false;
	var ageError = false;

	if (Number(grab('state').selectedIndex) === 0) {
		stateError = true;
	}

	if (isValidNumber_no_zero_allowed(grab('age').value) === false) {
		ageError = true;
	}

	if (cityError === true) {
		setErrorDiv('e_city');
	}

	if (stateError === true) {
		setErrorDiv('e_state');
	}

	if (ageError === true) {
		setErrorDiv('e_age');
	}
}

function op1_type_errorChecker() {
	var errorList = [];
	var html = '';
	var hasChildren = getPopParent('yesChild').checked;
	var hasSister = getPopParent('yesSister').checked;
	var hasBrother = getPopParent('yesBrother').checked;
	var num_kids = grab('numKids').value;
	var num_sisters = grab('numSisters').value;
	var num_brothers = grab('numBrothers').value;

	var ek = has_single_op_value_error(hasChildren, num_kids);
	var es = has_single_op_value_error(hasSister, num_sisters);
	var eb = has_single_op_value_error(hasBrother, num_brothers);

	if (ek === true) {
		setErrorDiv('e_c');
		html += "<li>You must add at least one child.</li>"
	}

	if (es === true) {
		setErrorDiv('e_s');
		html += "<li>You must add at least one sister.</li>"
	}

	if (eb === true) {
		setErrorDiv('e_b');
		html += "<li>You must add at least one brother.</li>"
	}

	return html;
}

function prepare_op_duplicate(text) {
	text = clearWhiteSpace(text);
	text = text.toLowerCase();
	return text;
}

function isDuplicateOpItem(item, list) {
	var isDuplicate = false;

	var age 	= prepare_op_duplicate(item['age']);
	var city 	= prepare_op_duplicate(item['city']);
	var state 	= prepare_op_duplicate(item['state']);
	var g_type 	= prepare_op_duplicate(item['g_type']);

	for (var i = 0; i < list.length; i++) {
		var a = prepare_op_duplicate(list[i]['age']);
		var c = prepare_op_duplicate(list[i]['city']);
		var s = prepare_op_duplicate(list[i]['state']);
		var g = prepare_op_duplicate(list[i]['g_type']);

		if (a === age && c === city && s === state && g === g_type) {
			isDuplicate = true;
			break;
		}
	}

	return isDuplicate;
}


function add_new_op_item() {
	if (op1_hasInputError() === true) {
		op1_input_errorChecker();
		openPopUp('auto', '/op_input_error/', 500, 150);
	}

	else {
		var age = grab('age').value;
		var city = grab('city').value;
		var state = grab('state').value;
		var g_type = find_op_gType();
		var index = grab('num_items').value;
		var spec = Number(index) + 1;
		var item = create_op_item_single_mh(age, city, state, g_type, index, spec);
		var eList = get_existing_op_items();
		var new_list = [];
		var initialize_list = determine_opList_initialization(g_type);

		grab('math_type').value = 'add';
		new_list.push(item);

		for (var j = 0; j < eList.length; j++) {
			new_list.push(eList[j]);
		}

		var isDuplicate = isDuplicateOpItem(item, eList);

		if (isDuplicate === true) {
			openPopUp('auto', '/op_item_exist/', 500, 150);
		}
		else {
			supremeOpListBuilder(new_list, initialize_list);
			set_op_relative_values();
			post_op_data_mh();
			grab('city').value = '';
			grab('state').selectedIndex = 0;
			grab('age').value = 0;
		}		
	}	
}


function delete_op_item() {
	var numElements = Number(grab('num_items').value);
	grab('math_type').value = 'delete';

	if (numElements > 1) {
		index = Number(grab('currently_selected').value);
		var data = getOpBuilderArray();
		var new_list = kill_unwanted_opElement(index, data);
		var process_this = reset_opItem_ids(new_list);
		grab('item_builder').innerHTML = '';
		supremeOpListBuilder(process_this, false);
	}
	else {
		grab('num_items').value = 0;
		grab('item_builder').innerHTML = '';
	}

	set_op_relative_values();
	post_op_data_mh();
}

function final_save_mh_op() {
	grab('e_city').className = '';
	grab('e_state').className = '';
	grab('e_age').className = '';
	post_op_data_mh();

	if (op1_hasTypeError() === true) {
		grab('type_errors').value = op1_type_errorChecker();
		openPopUp('auto', '/op_type_error/', 400, 400);
	}

	else {
		var next_url = getPopParent('next_url');
		var form = getPopParent('mh_form');
		getPopParent('save_this').value = 'true';
		form.action = next_url.value;
		form.submit();
		window.close();
	}
}

function initialize_op_type_errors() {
	var messages = String(getPopParent('type_errors').value);
	grab('errors').innerHTML = messages;
}


function final_mh_op_encoder(sep_list) {
	result = '';

	for (var i = 0; i < sep_list.length; i++) {
		var g_type = sep_list[i]['g_type'];
		g_type = encode_g_type_mh(g_type);

		result += g_type;
		result += sep_list[i]['age'];
		result += '/';
		result += sep_list[i]['city'];
		result += ',';
		result += sep_list[i]['state'];
		result += '~';
	}
	result = clearWhiteSpace(result);
	return result;
}

function encode_g_type_mh(g_type) {
	var result = null;
	g_type = String(g_type);

	if (g_type === 'Male Child') {
		result = 'm';
	}
	else if (g_type === 'Female Child') {
		result = 'f';
	}
	else if (g_type === 'Sister') {
		result = 's';
	}
	else if (g_type === 'Brother') {
		result = 'b';
	}

	return result;
}

function seperateElemental_op_mh() {
	var data = {};
	var m = [];
	var f = [];
	var s = [];
	var b = [];
	var e = get_existing_op_items();

	for (var i = 0; i < e.length; i++) {
		if (e[i]['g_type'] === 'Male Child') {
			m.push(e[i]);
		}
		else if (e[i]['g_type'] === 'Female Child') {
			f.push(e[i]);
		}
		else if (e[i]['g_type'] === 'Brother') {
			b.push(e[i]);
		}
		else if (e[i]['g_type'] === 'Sister') {
			s.push(e[i]);
		}
	}

	data['m'] = m;
	data['f'] = f;
	data['b'] = b;
	data['s'] = s;

	return data;
}

function get_existing_op_items() {
	var data = getOpBuilderArray();
	var result = reset_opItem_ids(data);
	return result;
}

function create_op_item_single_mh(age, city, state, g_type, index, spec) {
	var data = {};
	data['age'] = age;
	data['city'] = city;
	data['state'] = state;
	data['g_type'] = g_type;
	data['index'] = index;
	data['type_id'] = 'type_' + spec;
	data['age_id'] = 'age_' + spec;
	data['city_id'] = 'city_' + spec;
	data['state_id'] = 'state_' + spec;
	data['item_id'] = 'item_' + spec;
	return data;
}

function find_op_gType() {
	var type = null;

	var isChild = false;
	var isSister = false;
	var isBrother = false;
	var isMale = false;

	if (getPopParent('yesChild').checked === true) {
		isChild = grab('child').checked;
		isMale = grab('male').checked;
	}

	if (getPopParent('yesSister').checked === true) {
		isSister = grab('sister').checked;
	}

	if (getPopParent('yesBrother').checked === true) {
		isBrother = grab('brother').checked;
	}

	// var isChild = grab('child').checked;
	// var isSister = grab('sister').checked;
	// var isMale = grab('male').checked;

	if (isChild === true) {
		if (isMale === true) {
			type = 'Male Child';
		}
		else {
			type = 'Female Child';
		}
	}

	else if (isSister === true) {
		type = 'Sister';
	}

	else if (isBrother === true){
		type = 'Brother';
	}

	return type;
}

function prepare_op_html(html) {
	html = clearWhiteSpace(html);
	
	var result = '';
	var end = (html.length) - 16;

	if (html.length > 30 && isBlankText(html) === false) {
		for (var i = 14; i < end; i++) {
			result += html.charAt(i);
		}
	}

	return result;
}

function kill_unwanted_opElement(index, old_list) {
	var result = [];
	var back = old_list.length - 1;
	index = Number(index);

	for (var j = 0; j < index; j++) {
		back = back - 1;
	}

	for (var i = 0; i < old_list.length; i++) {
		if (back !== i) {
			result.push(old_list[i]);
		}
	}
	return result;
}

function kidsRock() {

	if (grab('yesChild').checked === true || grab('yesSister').checked === true || grab('yesBrother').checked === true) {
		//DO COMPLETE ERROR CHECK HERE...
		var section = grab('save_section').value;

		if (hasErrorsInForm('mh', section) === true || mh_dynamo_has_errors() === true) {
			superErrorChecker('mh', section);
			superDynamoChecker();
			var w = 500, h = 500;
			openPopUp('auto', '/generateErrors/', w, h);
		}
		else {
			postMhFields(section);
			var wk = 750, hk = 620;
			openPopUp('auto', '/mhDemoOpPage/', wk, hk);
		}		
	}
	else {
		post_mh_data(grab('save_section').value);
	}
}

function ut_choice_check(val) {
	val = String(val);
	var fieldName = 'u' + val;
	var targetName = 'm' + val;
	var field = grab(fieldName);
	var target = grab(targetName);

	if (field.checked === true) {
		target.value = 'true';
	}
	else {
		target.value = 'false';
	}

	grab('clear_all').checked = false;
}

function turn_on_ut_text() {
	var field = grab('u21');
	var text = grab('useOther');

	if (field.checked === true) {
		text.disabled = false;
		opacityHigh(text);
	}
	else {
		opacityZero(text);
		text.value = '';
		text.disabled = true;
		grab('e1').className = '';
	}
}

function shouldCreateUTTable() {
	var shouldCreate = false;

	for (var i = 1; i <= 21; i++) {
		var name = 'u' + String(i);
		var field = grab(name);

		if (field.checked === true) {
			shouldCreate = true;
			break;
		}
	}

	return shouldCreate;
}

function fetch_dynamo_ut_data() {
	var poz_answers = [];

	for (var i = 1; i <= 20; i++) {
		var name = 'm' + String(i);
		var field = getPopParent(name);

		if (String(field.value) === 'true') {
			var data = {};
			var targetName = 'l' + String(i);
			data['title'] = String(getPopParent(targetName).innerHTML);
			data['f1'] = 'howMuch' + String(i);
			data['f2'] = 'howOften' + String(i);
			data['f3'] = 'howLong' + String(i);
			data['f4'] = 'howOld' + String(i);
			data['f5'] = 'lastTime' + String(i);
			data['a1'] = 'fields.howMuch' + String(i);
			data['a2'] = 'fields.howOften' + String(i);
			data['a3'] = 'fields.howLong' + String(i);
			data['a4'] = 'fields.howOld' + String(i);
			data['a5'] = 'fields.lastTime' + String(i);
			data['p1'] = 'm_howMuch' + String(i);
			data['p2'] = 'm_howOften' + String(i);
			data['p3'] = 'm_howLong' + String(i);
			data['p4'] = 'm_howOld' + String(i);
			data['p5'] = 'm_lastTime' + String(i);
			data['errorDiv'] = 'e' + String(i);
			data['number'] = String(i);
			poz_answers.push(data);
		}
	}

	if (getPopParent('u21').checked === true) {
		var data1 = {};
		data1['title'] = String(getPopParent('useOther').value);
		data1['f1'] = 'howMuch21';
		data1['f2'] = 'howOften21';
		data1['f3'] = 'howLong21';
		data1['f4'] = 'howOld21';
		data1['f5'] = 'lastTime21';
		data1['a1'] = 'fields.howMuch21';
		data1['a2'] = 'fields.howOften21';
		data1['a3'] = 'fields.howLong21';
		data1['a4'] = 'fields.howOld21';
		data1['a5'] = 'fields.lastTime21';
		data1['p1'] = 'm_howMuch21';
		data1['p2'] = 'm_howOften21';
		data1['p3'] = 'm_howLong21';
		data1['p4'] = 'm_howOld21';
		data1['p5'] = 'm_lastTime21';
		data1['errorDiv'] = 'e21';
		data1['number'] = '21';
		poz_answers.push(data1);
	}

	return poz_answers;
}


function create_ut_single_cell(field) {
	var html = "<tr>\
	<td><div id=\'" + field['errorDiv'] + "\'><div class=\'ut_field_title\'>" + field['title'] + "</div></div></td>\
	<td><div><input type=\"text\" name=\"" + field['f1'] + "\" id=\"" + field['f1'] + "\" value=\"\" oninput=\"javascript: setParentUt(\'" + field['p1']+ "\', \'" + field['f1'] + "\'); runUTErrors(\'" + field['number'] + "\');\"></div></td>\
	<td><div><input type=\"text\" name=\"" + field['f2'] + "\" id=\"" + field['f2'] + "\" value=\"\" oninput=\"javascript: setParentUt(\'" + field['p2']+ "\', \'" + field['f2'] + "\'); runUTErrors(\'" + field['number'] + "\');\"></div></td>\
	<td><div><input type=\"text\" name=\"" + field['f3'] + "\" id=\"" + field['f3'] + "\" value=\"\" oninput=\"javascript: setParentUt(\'" + field['p3']+ "\', \'" + field['f3'] + "\'); runUTErrors(\'" + field['number'] + "\');\"></div></td>\
	<td><div><input type=\"number\" name=\"" + field['f4'] + "\" id=\"" + field['f4'] + "\" value=\"\" oninput=\"javascript: setParentUt(\'" + field['p4']+ "\', \'" + field['f4'] + "\'); runUTErrors(\'" + field['number'] + "\');\"></div></td>\
	<td><div><input type=\"text\" name=\"" + field['f5'] + "\" id=\"" + field['f5'] + "\" value=\"\" oninput=\"javascript: setParentUt(\'" + field['p5']+ "\', \'" + field['f5'] + "\'); runUTErrors(\'" + field['number'] + "\');\"></div></td>\
	</tr>";

	return html;
}

function useTableBuilder(fields) {
	var inner = '';
	var top = "<table class=\"dynamo_useTable_table\">\
	<tr>\
	<th><div class=\"use_th1\">Substance</div></th>\
	<th><div class=\"use_th2\">How Much I Use</div></th>\
	<th><div class=\"use_th2\">How Often I Use</div></th>\
	<th><div class=\"use_th2\">How Long I have Used</div></th>\
	<th><div class=\"use_th2\">Age Started</div></th>\
	<th><div class=\"use_th2\">When I Last Used</div></th>\
	</tr>";
	var bottom = "</table>";

	for (var i = 0; i < fields.length; i++) {
		inner += create_ut_single_cell(fields[i]);
	}

	var html = top + inner + bottom;

	grab('ut_builder').innerHTML = html;
}

function fetch_ut_post_values() {
	var result = [];

	for (var i = 1; i <= 21; i++) {
		var boxName = 'u' + String(i);
		var box = getPopParent(boxName);

		if (box.checked === true) {
			var data = {};

			var data = {};
			var n1 = 'm_howMuch' + String(i);
			var n2 = 'm_howOften' + String(i);
			var n3 = 'm_howLong' + String(i);
			var n4 = 'm_howOld' + String(i);
			var n5 = 'm_lastTime' + String(i);

			data['a1'] = String(getPopParent(n1).value);
			data['a2'] = String(getPopParent(n2).value);
			data['a3'] = String(getPopParent(n3).value);
			data['a4'] = String(getPopParent(n4).value);
			data['a5'] = String(getPopParent(n5).value);
			data['number'] = String(i);

			result.push(data);
		}
	}

	return result;
}

function hasUtLineError(field) {
	var hasError = false;

	for (var i = 1; i <= 5; i++) {
		var name = 'f' + String(i);
		var element = grab(field[name]);

		if (isBlankText(element.value) === true || element.value === null) {
			hasError = true;
			break;
		}
	}

	if (hasError === false) {
		var age = Number(grab(field['f4']).value);

		if (age < 1) {
			hasError = true;
		}
	}

	return hasError;
}

function set_ut_error_div_single(field) {
	if (hasUtLineError(field) === true) {
		setErrorDiv(field['errorDiv']);
	}
}

function calculate_ut_line_errors() {
	var fields = fetch_dynamo_ut_data();

	for (var i = 0; i < fields.length; i++) {
		set_ut_error_div_single(fields[i]);
	}
}

function runUTErrors(itemNumber) {
	itemNumber = String(itemNumber);
	var data = {};
	data['f1'] = 'howMuch' + itemNumber;
	data['f2'] = 'howOften' + itemNumber;
	data['f3'] = 'howLong' + itemNumber;
	data['f4'] = 'howMuch' + itemNumber;
	data['f5'] = 'howMuch' + itemNumber;
	error = 'e' + itemNumber;

	if (hasUtLineError(data) === false) {
		grab(error).className = '';
	}
}

function utLineHasErrors() {
	var hasError = false;
	var fields = fetch_dynamo_ut_data();

	for (var i = 0; i < fields.length; i++) {
		if (hasUtLineError(fields[i]) === true) {
			hasError = true;
			break;
		}
	}

	return hasError;
}

function setParentUt(parentName, value_Name) {
	parentName = String(parentName);
	value_Name = String(value_Name);

	getPopParent(parentName).value = grab(value_Name).value;
}

function set_use_table_existing_values() {
	var data = fetch_ut_post_values();

	for (var i = 0; i < data.length; i++) {
		var n1 = 'howMuch' + String(data[i]['number']);
		var n2 = 'howOften' + String(data[i]['number']);
		var n3 = 'howLong' + String(data[i]['number']);
		var n4 = 'howOld' + String(data[i]['number']);
		var n5 = 'lastTime' + String(data[i]['number']);

		var m1 = 'm_' + n1;
		var m2 = 'm_' + n2;
		var m3 = 'm_' + n3;
		var m4 = 'm_' + n4;
		var m5 = 'm_' + n5;

		grab(n1).value = getPopParent(m1).value;
		grab(n2).value = getPopParent(m2).value;
		grab(n3).value = getPopParent(m3).value;
		grab(n4).value = getPopParent(m4).value;
		grab(n5).value = getPopParent(m5).value;
	}
}

function ut_text_init(fieldName) {
	fieldName = String(fieldName);
	var field = grab(fieldName);

	if (String(field.value) === 'N/A') {
		field.value = '';
	}
}

function initialize_dynamo_ut() {
	var fields = fetch_dynamo_ut_data();
	useTableBuilder(fields);
	set_use_table_existing_values();

	for (var i = 0; i < fields.length; i++) {
		ut_text_init(fields[i]['f1']);
		ut_text_init(fields[i]['f2']);
		ut_text_init(fields[i]['f3']);
		ut_text_init(fields[i]['f5']);
	}
}


function use_table_setup() {
	var proceed = true;

	if (shouldCreateUTTable() === true) {
		var main_height = 198;
		var table_height = 0;
		var total_height = 0;

		if (grab('u21').checked === true) {
			var other = grab('useOther');

			if (isBlankText(other.value) === true) {
				proceed = false;
				setErrorDiv('e1');
				openPopUp('auto', '/generateErrors/', 500, 500);
			}
		}

		if (proceed === true) {
			var numPositives = 0;

			for (var i = 1; i <= 21; i++) {
				var name = 'm' + String(i);
				var target = grab(name);

				if (String(target.value) === 'true') {
					numPositives += 1;
				}
			}

			table_height = (27 * numPositives);
			total_height = main_height + table_height;
			openPopUp('auto', '/dynamic_useTable/', 1000, total_height);
		}
	}
	else {
		grab('save_this').value = 'true';
		grab('mh_form').action = grab('next_url').value;
		grab('mh_form').submit();
	}
}

function setNewUTData() {
	var hasErrors = utLineHasErrors();

	if (hasErrors === true) {
		calculate_ut_line_errors();
		openPopUp('auto', '/generateErrors/', 500, 500);
	}
	else {
		getPopParent('save_this').value = 'true';
		getPopParent('mh_form').action = getPopParent('next_url').value;
		getPopParent('mh_form').submit();
		window.close();
	}
}

function clear_ut_checks() {
	for (var i = 1; i <= 21; i++) {
		var name = 'u' + String(i);
		var field = grab(name);
		field.checked = false;
		ut_choice_check(i);
	}
	grab('e1').className = '';
	grab('select_all').checked = false;
	turn_on_ut_text();
}

function sel_all_ut_checks() {
	for (var i = 1; i <= 21; i++) {
		var name = 'u' + String(i);
		grab(name).checked = true;
		ut_choice_check(i);
	}
	grab('clear_all').checked = false;
	turn_on_ut_text();
}

function buildChildHeader(header, divName, numEntries, errorList, state_html) {
	divName = String(divName);
	header = String(header);
	var html = getChildElementHtml(numEntries, errorList, state_html);
	var table = header + '_table';

	var div = grab(divName);

	div.innerHTML = "<div class=\'clHeadMh\'>" + header + "</div>\
	<div class=\'clbodyMh\'>\
	<table id=\'" + table + "\'>\
	<tr>\
	<th><div style=\'width:80px;\'></div></th>\
	<th><div style=\'width:60px;\'>Age</div></th>\
	<th><div style=\'width:80px;\'>Gender</div></th>\
	<th><div style=\'width:120px;\'>City</div></th>\
	<th><div style=\'width:70px;\'>State</div></th>\
	</tr>" + html + "\
	</table>\
	</div>";
}

function buildSiblingHeader(header, divName, numEntries, sibType, state_html) {
	divName = String(divName);
	header = String(header);
	var html = getSiblingElementHtml(numEntries, sibType, state_html);
	var table = header + '_table';

	var div = grab(divName);

	div.innerHTML = "<div class=\'clHeadMh\'>" + header + "</div>\
	<div class=\'clbodyMh\'>\
	<table id=\'" + table + "\'>\
	<tr>\
	<th><div style=\'width:80px;\'></div></th>\
	<th><div style=\'width:60px;\'>Age</div></th>\
	<th><div style=\'width:120px;\'>City</div></th>\
	<th><div style=\'width:70px;\'>State</div></th>\
	</tr>" + html + "\
	</table>\
	</div>";
}

function singleEntryChildHtml(e_id, errorTag, state_html) {
	e_id = String(e_id);
	errorTag = String(errorTag);
	var head = 'Child ' + e_id;
	var genderName = 'gender_' + e_id;
	var male = 'male_' + e_id;
	var female = 'female_' + e_id;
	var age = 'age_' + e_id;
	var city = 'city_' + e_id;
	var state = 'state_' + e_id;

	var html = "<tr>\
	<td><div id=\'" + errorTag + "\'><div class=\'mhpopyo\'>" + head + "</div></div></td>\
	<td><div><input type=\'number\' style=\'width:60px;\' name=\'" + age + "\' id=\'" + age + "\' value=\'0\' \
	oninput=\"javascript: noErrorTextMH1(\'" + errorTag + "\', \'" + age + "\');\"></div></td>\
	<td>\
	<table>\
	<tr>\
	<td><input type=\'radio\' name=\'" + genderName + "\' id=\'" + male + "\' checked value=\'Male\'><td>\
	<td><div class='mhOprad'>Male</div></td>\
	<td><input type=\'radio\' name=\'" + genderName + "\' id=\'" + female + "\' value=\'Female\'><td>\
	<td><div class='mhOprad'>Female</div></td>\
	</tr>\
	</table>\
	</td>\
	<td><div><input type=\'text\' name=\'" + city + "\' id=\'" + city + "\' style=\'width:120px;\' oninput=\"javascript: noErrorTextMH1(\'" + errorTag + "\', \'" + city + "\');\"></div></td>\
	<td>\
	<div>\
	<select name=\'" + state + "\' id=\'" + state + "\' style=\'width:70px;\' onChange=\"javascript: noErrorTextMH1(\'" + errorTag + "\', \'" + state + "\');\">\
	<option value=\'None Selected\'>Select</option>" + state_html + "\
	</select>\
	</div>\
	</td>\
	</tr>";

	return html;
}

function singleEntrySiblingHtml(e_id, siblingType, errorTag, state_html) {
	e_id = String(e_id);
	errorTag = String(errorTag);
	siblingType = String(siblingType);
	var tagNumber = '';
	var head =  siblingType + ' ' + e_id;

	for (var j = 1; j < errorTag.length; j++) {
		tagNumber += errorTag.charAt(j);
	}

	var age = 'age_' + tagNumber;
	var city = 'city_' + tagNumber;
	var state = 'state_' + tagNumber;

	var html = "<tr>\
	<td><div id=\'" + errorTag + "\'><div class=\'mhpopyo\'>" + head + "</div></div></td>\
	<td><div><input type=\'number\' style=\'width:60px;\' name=\'" + age + "\' id=\'" + age + "\' value=\'0\' \
	oninput=\"javascript: noErrorTextMH1(\'" + errorTag + "\', \'" + age + "\');\"></div></td>\
	<td><div><input type=\'text\' name=\'" + city + "\' id=\'" + city + "\' style=\'width:120px;\' \
	oninput=\"javascript: noErrorTextMH1(\'" + errorTag + "\', \'" + city + "\');\"></div></td>\
	<td>\
	<div>\
	<select name=\'" + state + "\' id=\'" + state + "\' onChange=\"javascript: noErrorTextMH1(\'" + errorTag + "\', \'" + state + "\');\">\
	<option value=\'None Selected\'>Select</option>" + state_html +"\
	</select>\
	</div>\
	</td>\
	</tr>";

	return html;
}

function getChildElementHtml(numEntries, errorList, state_html) {
	numEntries = Number(numEntries);
	var html = '';

	for (var i = 1; i <= numEntries; i++) {
		var errorIndex = Number(i) - 1;
		html += singleEntryChildHtml(i, errorList[errorIndex], state_html);
	}
	return html;
}

function getSiblingElementHtml(numEntries, sibType, state_html) {
	numEntries = Number(numEntries);
	var html = '';
	var errorNumber = 0;
	sibType = String(sibType);

	if (sibType === 'Sister') {
		var numKids = getPopParent('numChildren').value;
		numKids = Number(numKids);
		errorNumber = numKids + 1;
	}
	else if (sibType === 'Brother') {
		var numKids = getPopParent('numChildren').value;
		var numSisters = getPopParent('numSisters').value;

		numKids = Number(numKids);
		numSisters = Number(numSisters);
		errorNumber = numKids + numSisters + 1;
	}

	for (var i = 1; i <= numEntries; i++) {
		var errorName = 'e' + String(errorNumber);
		html += singleEntrySiblingHtml(i, sibType, errorName, state_html);
		errorNumber += 1;
	}
	return html;
}

function buildChildList(numEntries, errorList, state_html) {
	buildChildHeader('Children', 'childBuilder', numEntries, errorList, state_html);
}

function buildSisterList(numEntries, state_html) {
	var div = grab('sisterBuilder');
	buildSiblingHeader('Sisters', 'sisterBuilder', numEntries, 'Sister', state_html);
}

function buildBrotherList(numEntries, stateList) {
	var div = grab('brotherBuilder');
	buildSiblingHeader('Brothers', 'brotherBuilder', numEntries, 'Brother', stateList);
}

function generateStateHtml(states) {
	var html = '';

	for (var i = 0; i < states.length; i++) {
		html += "<option value=\'" + String(states[i]) + "\'>" + String(states[i]) + "</option>";
	}

	return html;
}

function initialize_mhDemoOps() {
	var reconstruct = String(getPopParent('reconstruct').value);
	var state_html = generateStateHtml(states);

	if (reconstruct === 'false') {
		var hasChildren = getPopParent('yesChild').checked;
		var hasSisters = getPopParent('yesSister').checked;
		var hasBrothers = getPopParent('yesBrother').checked;
		var numChildren = getPopParent('numChildren').value;
		var numSisters = getPopParent('numSisters').value;
		var numBrothers = getPopParent('numBrothers').value;
		var totalErrorDivs = Number(numChildren) + Number(numSisters) + Number(numBrothers);

		var errorList = creatErrorDivsMhOp(totalErrorDivs);

		grab('numKids').value = numChildren;
		grab('numSisters').value = numSisters;
		grab('numBrothers').value = numBrothers;


		if (hasChildren === true) {		
			buildChildList(numChildren, errorList, state_html);
		}

		if (hasSisters === true) {		
			buildSisterList(numSisters, state_html);
		}

		if (hasBrothers === true) {		
			buildBrotherList(numBrothers, state_html);
		}
	}
	else {
		resonstruct_mhOpPage(state_html);
	}
}

function resonstruct_mhOpPage(state_html) {
	var changeKids = shouldReconstruct_childWindow_mh('yesChild', 'numChildren', 'm_numChildren');
	var changeSisters = shouldReconstruct_childWindow_mh('yesSister', 'numSisters', 'm_numSisters');
	var changeBrothers = shouldReconstruct_childWindow_mh('yesBrother', 'numBrothers', 'm_numBrothers');
	
	if (changeKids === true) {
		var numChildren = Number(getPopParent('numChildren').value);
		var totalErrorDivs = fetch_num_reconstuct_errorDivs(changeKids, changeSisters, changeBrothers);
		var errorList = creatErrorDivsMhOp(totalErrorDivs);
		getPopParent('m_numChildren').value = numChildren;
		buildChildList(numChildren, errorList, state_html);
	}

	if (changeSisters === true) {
		var numSisters = Number(getPopParent('numSisters').value);
		getPopParent('m_numSisters').value = numSisters;
		buildSisterList(numSisters, m_states);
	}

	if (changeBrothers === true) {
		var numBrothers = Number(getPopParent('numBrothers').value);
		getPopParent('m_numBrothers').value = numBrothers;
		buildBrotherList(numBrothers, m_states);
	}
}

function fetch_num_reconstuct_errorDivs(newChild, newSister, newBrother) {
	var numChildren = 0;
	var numSisters = 0;
	var numBrothers = 0;
	var result = 0;

	if (newChild === true) {
		numChildren = Number(getPopParent('numChildren').value);
	}

	if (newSister === true) {
		numSisters = Number(getPopParent('numSisters').value);
	}

	if (newBrother === true) {
		numBrothers = Number(getPopParent('numBrothers').value);
	}

	result = numChildren + numSisters + numBrothers;

	return result;
}

function creatErrorDivsMhOp(numberDivs) {
	var results = [];
	numberDivs = Number(numberDivs);

	for (var i = 1; i <= numberDivs; i++) {
		results.push('e' + String(i));
	}
	return results;
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

	//SET THE GRADE RADIO FIELDS
	grabGradeRadio(json_data.GradesKto6, a, b, c, d, e, f);
	grabGradeRadio(json_data.Grades7to9, g7a, g7b, g7c, g7d, g7e, g7f);
	grabGradeRadio(json_data.Grades10to12, g10a, g10b, g10c, g10d, g10e, g10f);

	if (String(json_data.collegeYears) === '1') {grab('college1').checked = true;}
	else if (String(json_data.collegeYears) === '2') {grab('college2').checked = true;}
	else if (String(json_data.collegeYears) === '3') {grab('college3').checked = true;}
	else if (String(json_data.collegeYears) === '4') {grab('college4').checked = true;}
	else {grab('collegeNone').checked = true;}

	setRadioElement(json_data.BehaviorProblemsKto6, grab('behaved'), grab('notBehaved'));
	setRadioElement(json_data.AcademicProblemsKto6, grab('yesAcademic'), grab('noAcademic'));
	setRadioElement(json_data.BehaviorProblems7to9, grab('behaved2'), grab('notBehaved2'));
	setRadioElement(json_data.AcademicProblems7to9, grab('yesAcademic2'), grab('noAcademic2'));
	setRadioElement(json_data.BehaviorProblems10to12, grab('behaved3'), grab('notBehaved3'));
	setRadioElement(json_data.AcademicProblems10to12, grab('yesAcademic3'), grab('noAcademic3'));

	setRadioElement(json_data.advanceDegree, grab('yesAdvanced'), grab('noAdvanced'));
	setRadioElement(json_data.tradeSch, grab('yesTrade'), grab('noTrade'));
	setRadioElement(json_data.military, grab('yesMillitary'), grab('noMillitary'));
	setRadioElement(json_data.honorableDischarge, grab('yesHonor'), grab('noHonor'));

	mhCollegeRadio();
	mhTrade();
	mhMilitary();
}

function set_single_bool_val_wData(data, triggerName, s1, s2, i1, i2) {
	data 		= String(data);
	triggerName = String(triggerName);

	var trigger = grab(triggerName);
	trigger.checked = false;

	if (data === 'true') {
		s1 = String(s1);
		s2 = String(s2);
		i1 = Number(i1);
		i2 = Number(i2);

		var select_1 = grab(s1);
		var select_2 = grab(s2);

		trigger.checked = true;
		select_1.selectedIndex = i1;
		select_2.selectedIndex = i2;
	}
}

function m_dataMHF(checkName, targetName) {
	checkName 	= String(checkName);
	targetName 	= String(targetName);

	var checkBox 	= grab(checkName);
	var target 		= grab(targetName);

	if (checkBox.checked === true) {
		target.value = 'True';
	}
	else {
		target.value = 'False';
	}
}

function initialize_mh_family(json_data) {
	set_single_bool_val_wData(json_data.isdepressed, 'isdepressed', 'depressSide', 'depressMember', json_data.depressedS, json_data.depressedM);
	set_single_bool_val_wData(json_data.isadd, 'isadd', 'sideADD', 'memADD', json_data.addS, json_data.addM);
	set_single_bool_val_wData(json_data.isbedWetting, 'isbedWetting', 'sideBed', 'memBed', json_data.bedWettingS, json_data.bedWettingM);
	set_single_bool_val_wData(json_data.isbipolar, 'isbipolar', 'sideBi', 'memBi', json_data.bipolarS, json_data.bipolarM);
	set_single_bool_val_wData(json_data.issuicideAttempt, 'issuicideAttempt', 'sideATT', 'memATT', json_data.suicideAttemptS, json_data.suicideAttemptM);
	set_single_bool_val_wData(json_data.isphysicalAbuse, 'isphysicalAbuse', 'sidePA', 'memPA', json_data.physicalAbuseS, json_data.physicalAbuseM);
	set_single_bool_val_wData(json_data.islaw, 'islaw', 'sideLaw', 'memLaw', json_data.lawS, json_data.lawM);
	set_single_bool_val_wData(json_data.isld, 'isld', 'sideLD', 'memLD', json_data.ldS, json_data.ldM);
	set_single_bool_val_wData(json_data.istic, 'istic', 'sideTic', 'memTic', json_data.ticS, json_data.ticM);
	set_single_bool_val_wData(json_data.isthyroid, 'isthyroid', 'sideThy', 'memThy', json_data.thyroidS, json_data.thyroidM);
	set_single_bool_val_wData(json_data.isheart, 'isheart', 'sideHeart', 'memHeart', json_data.heartS, json_data.heartM);
	set_single_bool_val_wData(json_data.isoverweight, 'isoverweight', 'sideOW', 'memOW', json_data.overweightS, json_data.overweightM);
	set_single_bool_val_wData(json_data.ismood, 'ismood', 'sideMood', 'memMood', json_data.moodS, json_data.moodM);
	set_single_bool_val_wData(json_data.isalcohol, 'isalcohol', 'sideAlc', 'memAlc', json_data.alcoholS, json_data.alcoholM);
	set_single_bool_val_wData(json_data.isdrugs, 'isdrugs', 'sideDrug', 'memDrug', json_data.drugsS, json_data.drugsM);
	set_single_bool_val_wData(json_data.isschizo, 'isschizo', 'sideSch', 'memSch', json_data.schizoS, json_data.schizoM);
	set_single_bool_val_wData(json_data.isseizures, 'isseizures', 'sideSe', 'memSe', json_data.seizuresS, json_data.seizuresM);
	set_single_bool_val_wData(json_data.iscompletedSuicide, 'iscompletedSuicide', 'sideCS', 'memCS', json_data.completedSuicideS, json_data.completedSuicideM);
	set_single_bool_val_wData(json_data.issexAbuse, 'issexAbuse', 'sideSex', 'memSex', json_data.sexAbuseS, json_data.sexAbuseM);
	set_single_bool_val_wData(json_data.ispanic, 'ispanic', 'sidePanick', 'memPanick', json_data.panicS, json_data.panicM);
	set_single_bool_val_wData(json_data.isanxiety, 'isanxiety', 'sideAnx', 'memAnx', json_data.anxietyS, json_data.anxietyM);
	set_single_bool_val_wData(json_data.isOCD, 'isOCD', 'sideOCD', 'memOCD', json_data.OCDS, json_data.OCDM);
	set_single_bool_val_wData(json_data.isdiabetes, 'isdiabetes', 'sideSugar', 'memSugar', json_data.diabetesS, json_data.diabetesM);
	set_single_bool_val_wData(json_data.iscancer, 'iscancer', 'sideCancer', 'memCancer', json_data.cancerS, json_data.cancerM);
	set_single_bool_val_wData(json_data.ishighBloodPressure, 'ishighBloodPressure', 'sideBlood', 'memBlood', json_data.highBloodPressureS, json_data.highBloodPressureM);
	set_single_bool_val_wData(json_data.isanger, 'isanger', 'sideAngry', 'memAngry', json_data.angerS, json_data.angerM);

	kill_selects_mh('isdepressed', 'depressSide', 'depressMember', 'e1');
	kill_selects_mh('isadd', 'sideADD', 'memADD', 'e2');
	kill_selects_mh('isbedWetting', 'sideBed', 'memBed', 'e3');
	kill_selects_mh('isbipolar', 'sideBi', 'memBi', 'e4');
	kill_selects_mh('issuicideAttempt', 'sideATT', 'memATT', 'e5');
	kill_selects_mh('isphysicalAbuse', 'sidePA', 'memPA', 'e6');
	kill_selects_mh('islaw', 'sideLaw', 'memLaw', 'e7');
	kill_selects_mh('isld', 'sideLD', 'memLD', 'e8');
	kill_selects_mh('istic', 'sideTic', 'memTic', 'e9');
	kill_selects_mh('isthyroid', 'sideThy', 'memThy', 'e10');
	kill_selects_mh('isheart', 'sideHeart', 'memHeart', 'e11');
	kill_selects_mh('isoverweight', 'sideOW', 'memOW', 'e12');
	kill_selects_mh('ismood', 'sideMood', 'memMood', 'e13');
	kill_selects_mh('isalcohol', 'sideAlc', 'memAlc', 'e14');
	kill_selects_mh('isdrugs', 'sideDrug', 'memDrug', 'e15');
	kill_selects_mh('isschizo', 'sideSch', 'memSch', 'e16');
	kill_selects_mh('isseizures', 'sideSe', 'memSe', 'e17');
	kill_selects_mh('iscompletedSuicide', 'sideCS', 'memCS', 'e18');
	kill_selects_mh('issexAbuse', 'sideSex', 'memSex', 'e19');
	kill_selects_mh('ispanic', 'sidePanick', 'memPanick', 'e20');
	kill_selects_mh('isanxiety', 'sideAnx', 'memAnx', 'e21');
	kill_selects_mh('isOCD', 'sideOCD', 'memOCD', 'e22');
	kill_selects_mh('isdiabetes', 'sideSugar', 'memSugar', 'e23');
	kill_selects_mh('iscancer', 'sideCancer', 'memCancer', 'e24');
	kill_selects_mh('ishighBloodPressure', 'sideBlood', 'memBlood', 'e25');
	kill_selects_mh('isanger', 'sideAngry', 'memAngry', 'e26');

	m_dataMHF('isdepressed', 'check1');
	m_dataMHF('isadd', 'check2');
	m_dataMHF('isbedWetting', 'check3');
	m_dataMHF('isbipolar', 'check4');
	m_dataMHF('issuicideAttempt', 'check5');
	m_dataMHF('isphysicalAbuse', 'check6');
	m_dataMHF('islaw', 'check7');
	m_dataMHF('isld', 'check8');
	m_dataMHF('istic', 'check9');
	m_dataMHF('isthyroid', 'check10');
	m_dataMHF('isheart', 'check11');
	m_dataMHF('isoverweight', 'check12');
	m_dataMHF('ismood', 'check13');
	m_dataMHF('isalcohol', 'check14');
	m_dataMHF('isdrugs', 'check15');
	m_dataMHF('isschizo', 'check16');
	m_dataMHF('isseizures', 'check17');
	m_dataMHF('iscompletedSuicide', 'check18');
	m_dataMHF('issexAbuse', 'check19');
	m_dataMHF('ispanic', 'check20');
	m_dataMHF('isanxiety', 'check21');
	m_dataMHF('isOCD', 'check22');
	m_dataMHF('isdiabetes', 'check23');
	m_dataMHF('iscancer', 'check24');
	m_dataMHF('ishighBloodPressure', 'check25');
	m_dataMHF('isanger', 'check26');
}

function initialize_mh_background(json_data) {
	blank_init(json_data.isComplete, grab('interest'));
	blank_init(json_data.isComplete, grab('friendAct'));
	blank_init(json_data.isComplete, grab('workAct'));
	blank_init(json_data.isComplete, grab('churchAffiliation'));

	number_init(json_data.isComplete, grab('closeFriendNumber'));
	number_init(json_data.isComplete, grab('acqNumber'));
	number_init(json_data.isComplete, grab('interestWeek'));
	number_init(json_data.isComplete, grab('interestMonth'));
	number_init(json_data.isComplete, grab('friendActWeek'));
	number_init(json_data.isComplete, grab('friendActMonth'));
	number_init(json_data.isComplete, grab('workActWeek'));
	number_init(json_data.isComplete, grab('workActMonth'));
	number_init(json_data.isComplete, grab('churchWeek'));
	number_init(json_data.isComplete, grab('churchMonth'));
	number_init(json_data.isComplete, grab('churchYear'));

	grab('residence').selectedIndex = json_data.residence;
	grab('income').selectedIndex = json_data.income;
	grab('debt').selectedIndex = json_data.debt;
	grab('credit').selectedIndex = json_data.credit;
	grab('healthCare').selectedIndex = json_data.healthCare;
	grab('otherIncome').selectedIndex = json_data.otherIncome;
	grab('closeFriendVisit').selectedIndex = json_data.closeFriendVisit;
	grab('acqVisit').selectedIndex = json_data.acqVisit;

	grabMhRelationshipRadios(json_data.spouseRelationship, grab('isPoorSpouse'), grab('isAvgSpouse'), grab('isGoodSpouse'));
	grabMhRelationshipRadios(json_data.parentsRelationship, grab('isPoorParents'), grab('isAvgParents'), grab('isGoodParents'));
	grabMhRelationshipRadios(json_data.brothersRelationship, grab('isPoorBro'), grab('isAvgBro'), grab('isGoodBro'));
	grabMhRelationshipRadios(json_data.sistersRelationship, grab('isPoorSis'), grab('isAvgSis'), grab('isGoodSis'));
	grabMhRelationshipRadios(json_data.childrenRelationship, grab('isPoorKids'), grab('isAvgKids'), grab('isGoodKids'));
	grabMhRelationshipRadios(json_data.exRelationship, grab('isPoorEx'), grab('isAvgEx'), grab('isGoodEx'));
}

function initialize_mh_stress(json_data) {
	setRadioElement(json_data.deathStress, grab('yesDeath'), grab('noDeath'));
	setRadioElement(json_data.divorceStress, grab('yesDivorce'), grab('noDivorce'));
	setRadioElement(json_data.moveStress, grab('yesMove'), grab('noMove'));
	setRadioElement(json_data.medicalStress, grab('yesMedical'), grab('noMedical'));
	setRadioElement(json_data.familyHealthStress, grab('yesFamily'), grab('noFamily'));
	setRadioElement(json_data.financialStress, grab('yesMoney'), ('noMoney'));
	setRadioElement(json_data.abuseStress, grab('yesAbuse'), grab('noAbuse'));
	setRadioElement(json_data.addictionFamilyStress, grab('yesAddiction'), grab('noAddiction'));
	setRadioElement(json_data.violenceFamilyStress, grab('yesViolence'), grab('noViolence'));
	setRadioElement(json_data.otherStress, grab('yesOther'), grab('noOther'));

	blank_init(json_data.isComplete, grab('deathStressExp'));
	blank_init(json_data.isComplete, grab('divorceStressExp'));
	blank_init(json_data.isComplete, grab('moveStressExp'));
	blank_init(json_data.isComplete, grab('medicalStressExp'));
	blank_init(json_data.isComplete, grab('familyHealthStressExp'));
	blank_init(json_data.isComplete, grab('financialStressExp'));
	blank_init(json_data.isComplete, grab('abuseStressExp'));
	blank_init(json_data.isComplete, grab('addictionFamilyStressExp'));
	blank_init(json_data.isComplete, grab('violenceFamilyStressExp'));
	blank_init(json_data.isComplete, grab('otherStressExp'));


	mhStressRadio('yesDeath', 'deathStressExp', 'b1');
	mhStressRadio('yesDivorce', 'divorceStressExp', 'b2');
	mhStressRadio('yesMove', 'moveStressExp', 'b3');
	mhStressRadio('yesMedical', 'medicalStressExp', 'b4');
	mhStressRadio('yesFamily', 'familyHealthStressExp', 'b5');
	mhStressRadio('yesMoney', 'financialStressExp', 'b6');
	mhStressRadio('yesAbuse', 'abuseStressExp', 'b7');
	mhStressRadio('yesAddiction', 'addictionFamilyStressExp', 'b8');
	mhStressRadio('yesViolence', 'violenceFamilyStressExp', 'b9');
	mhStressRadio('yesOther', 'otherStressExp', 'b10');
}


function initialize_mh_legal(json_data) {
	blank_init(json_data.isComplete, grab('arrestCharges'));
	blank_init(json_data.isComplete, grab('convictionCharges'));

	number_init(json_data.isComplete, grab('num_arrest'));
	number_init(json_data.isComplete, grab('num_convictions'));
	number_init(json_data.isComplete, grab('num_DUI_charges'));
	number_init(json_data.isComplete, grab('num_DUI_convictions'));

	setRadioElement(json_data.probationPast, grab('haveBeen'), grab('haveNotBeen'));
	setRadioElement(json_data.everSuspended, grab('yesSuspended'), grab('noSuspended'));
	setRadioElement(json_data.hasLawsuit, grab('yesSuit'), grab('noSuit'));
	setRadioElement(json_data.inDivorce, grab('yesDivPro'), grab('noDivPro'));
	setRadioElement(json_data.childCustody, grab('yesChildDis'), grab('noChildDis'));
	setRadioElement(json_data.hasBankrupcy, grab('yesBank'), grab('noBank'));

	if (Number(json_data.num_suspended) > 0) {
		grab('yesSuspended').checked = true;
	}
	else {
		grab('noSuspended').checked = true;
	}

	if (grab('yesCurrentProb').checked === true) {
		setRadioElement(json_data.probationPresent, grab('yesCurrentProb'), grab('noCurrentProb'));
	}
	if (grab('yesSuspended').checked === true) {
		setRadioElement(json_data.suspendedDrivePresent, grab('yesCurrentSus'), grab('noCurrentSus'));
	}
	if (grab('yesSuit').checked === true) {
		setRadioElement(json_data.lawsuitStress, grab('yesStress'), grab('noStress'));
	}

	mhProbation();
	mhSuspension1();
	mhLawsuits();
	mhBank();
	p_answer1_mh();
}

function d_init_mh_psych(json_data) {
	blank_init(json_data.isComplete, grab('psychiatricHistory'));
}

function setUp_use_hidden() {
	var div = grab('c_fields');
	var html = '';

	for (var i = 1; i <= 21; i++) {
		var n1 = 'm_howMuch' + String(i);
		var n2 = 'm_howOften' + String(i);
		var n3 = 'm_howLong' + String(i);
		var n4 = 'm_howOld' + String(i);
		var n5 = 'm_lastTime' + String(i);

		var line = "<input type=\'hidden\' name=\'" + n1 + "\' id=\'" + n1 + "\' value=\"\">\
		<input type=\'hidden\' name=\'" + n2 + "\' id=\'" + n2 + "\' value=\"\">\
		<input type=\'hidden\' name=\'" + n3 + "\' id=\'" + n3 + "\' value=\"\">\
		<input type=\'hidden\' name=\'" + n4 + "\' id=\'" + n4 + "\' value=\"\">\
		<input type=\'hidden\' name=\'" + n5 + "\' id=\'" + n5 + "\' value=\"\">\
		";
		html += line;
	}

	div.innerHTML = html;
}

function set_hidden_useTable_data(data) {
	grab('m_howMuch1').value = data.howMuch1;
	grab('m_howMuch2').value = data.howMuch2;
	grab('m_howMuch3').value = data.howMuch3;
	grab('m_howMuch4').value = data.howMuch4;
	grab('m_howMuch5').value = data.howMuch5;
	grab('m_howMuch6').value = data.howMuch6;
	grab('m_howMuch7').value = data.howMuch7;
	grab('m_howMuch8').value = data.howMuch8;
	grab('m_howMuch9').value = data.howMuch9;
	grab('m_howMuch10').value = data.howMuch10;
	grab('m_howMuch11').value = data.howMuch11;
	grab('m_howMuch12').value = data.howMuch12;
	grab('m_howMuch13').value = data.howMuch13;
	grab('m_howMuch14').value = data.howMuch14;
	grab('m_howMuch15').value = data.howMuch15;
	grab('m_howMuch16').value = data.howMuch16;
	grab('m_howMuch17').value = data.howMuch17;
	grab('m_howMuch18').value = data.howMuch18;
	grab('m_howMuch19').value = data.howMuch19;
	grab('m_howMuch20').value = data.howMuch20;
	grab('m_howMuch21').value = data.howMuch21;

	grab('m_howOften1').value = data.howOften1;
	grab('m_howOften2').value = data.howOften2;
	grab('m_howOften3').value = data.howOften3;
	grab('m_howOften4').value = data.howOften4;
	grab('m_howOften5').value = data.howOften5;
	grab('m_howOften6').value = data.howOften6;
	grab('m_howOften7').value = data.howOften7;
	grab('m_howOften8').value = data.howOften8;
	grab('m_howOften9').value = data.howOften9;
	grab('m_howOften10').value = data.howOften10;
	grab('m_howOften11').value = data.howOften11;
	grab('m_howOften12').value = data.howOften12;
	grab('m_howOften13').value = data.howOften13;
	grab('m_howOften14').value = data.howOften14;
	grab('m_howOften15').value = data.howOften15;
	grab('m_howOften16').value = data.howOften16;
	grab('m_howOften17').value = data.howOften17;
	grab('m_howOften18').value = data.howOften18;
	grab('m_howOften19').value = data.howOften19;
	grab('m_howOften20').value = data.howOften20;
	grab('m_howOften21').value = data.howOften21;

	grab('m_howLong1').value = data.howLong1;
	grab('m_howLong2').value = data.howLong2;
	grab('m_howLong3').value = data.howLong3;
	grab('m_howLong4').value = data.howLong4;
	grab('m_howLong5').value = data.howLong5;
	grab('m_howLong6').value = data.howLong6;
	grab('m_howLong7').value = data.howLong7;
	grab('m_howLong8').value = data.howLong8;
	grab('m_howLong9').value = data.howLong9;
	grab('m_howLong10').value = data.howLong10;
	grab('m_howLong11').value = data.howLong11;
	grab('m_howLong12').value = data.howLong12;
	grab('m_howLong13').value = data.howLong13;
	grab('m_howLong14').value = data.howLong14;
	grab('m_howLong15').value = data.howLong15;
	grab('m_howLong16').value = data.howLong16;
	grab('m_howLong17').value = data.howLong17;
	grab('m_howLong18').value = data.howLong18;
	grab('m_howLong19').value = data.howLong19;
	grab('m_howLong20').value = data.howLong20;
	grab('m_howLong21').value = data.howLong21;

	grab('m_howOld1').value = data.howOld1;
	grab('m_howOld2').value = data.howOld2;
	grab('m_howOld3').value = data.howOld3;
	grab('m_howOld4').value = data.howOld4;
	grab('m_howOld5').value = data.howOld5;
	grab('m_howOld6').value = data.howOld6;
	grab('m_howOld7').value = data.howOld7;
	grab('m_howOld8').value = data.howOld8;
	grab('m_howOld9').value = data.howOld9;
	grab('m_howOld10').value = data.howOld10;
	grab('m_howOld11').value = data.howOld11;
	grab('m_howOld12').value = data.howOld12;
	grab('m_howOld13').value = data.howOld13;
	grab('m_howOld14').value = data.howOld14;
	grab('m_howOld15').value = data.howOld15;
	grab('m_howOld16').value = data.howOld16;
	grab('m_howOld17').value = data.howOld17;
	grab('m_howOld18').value = data.howOld18;
	grab('m_howOld19').value = data.howOld19;
	grab('m_howOld20').value = data.howOld20;
	grab('m_howOld21').value = data.howOld21;

	grab('m_lastTime1').value = data.lastTime1;
	grab('m_lastTime2').value = data.lastTime2;
	grab('m_lastTime3').value = data.lastTime3;
	grab('m_lastTime4').value = data.lastTime4;
	grab('m_lastTime5').value = data.lastTime5;
	grab('m_lastTime6').value = data.lastTime6;
	grab('m_lastTime7').value = data.lastTime7;
	grab('m_lastTime8').value = data.lastTime8;
	grab('m_lastTime9').value = data.lastTime9;
	grab('m_lastTime10').value = data.lastTime10;
	grab('m_lastTime11').value = data.lastTime11;
	grab('m_lastTime12').value = data.lastTime12;
	grab('m_lastTime13').value = data.lastTime13;
	grab('m_lastTime14').value = data.lastTime14;
	grab('m_lastTime15').value = data.lastTime15;
	grab('m_lastTime16').value = data.lastTime16;
	grab('m_lastTime17').value = data.lastTime17;
	grab('m_lastTime18').value = data.lastTime18;
	grab('m_lastTime19').value = data.lastTime19;
	grab('m_lastTime20').value = data.lastTime20;
	grab('m_lastTime21').value = data.lastTime21;
}

function set_init_useTable_checkboxes(f1, f2, f3, f4, f5, boxName) {
	// fieldName = String(fieldName);
	f1 = String(f1);
	f2 = String(f2);
	f3 = String(f3);
	f4 = String(f4);
	f5 = String(f5);
	boxName = String(boxName);

	var field1 = grab(f1);
	var field2 = grab(f2);
	var field3 = grab(f3);
	var field4 = grab(f4);
	var field5 = grab(f5);
	var box = grab(boxName);

	if (isBlankText(field1.value) === false && field1.value !== null && field1.value !== 'N/A') {
		box.checked = true;
	}
	else {
		box.checked = false;
		field1.value = 'N/A';
		field2.value = 'N/A';
		field3.value = 'N/A';
		field4.value = 0;
		field5.value = 'N/A';
	}
}

function initialize_m_field(boxName, targetName) {
	boxName = String(boxName);
	targetName = String(targetName);

	var box = grab(boxName);
	var target = grab(targetName);

	if (box.checked === true) {
		target.value = 'true';
	}
	else {
		target.value = 'false';
	}
}


function initialize_mh_use(json_data) {
	setUp_use_hidden();
	set_hidden_useTable_data(json_data);

	set_init_useTable_checkboxes('m_howMuch1','m_howOften1', 'm_howLong1', 'm_howOld1', 'm_lastTime1', 'u1');
	set_init_useTable_checkboxes('m_howMuch2','m_howOften2', 'm_howLong2', 'm_howOld2', 'm_lastTime2', 'u2');
	set_init_useTable_checkboxes('m_howMuch3','m_howOften3', 'm_howLong3', 'm_howOld3', 'm_lastTime3', 'u3');
	set_init_useTable_checkboxes('m_howMuch4','m_howOften4', 'm_howLong4', 'm_howOld4', 'm_lastTime4', 'u4');
	set_init_useTable_checkboxes('m_howMuch5','m_howOften5', 'm_howLong5', 'm_howOld5', 'm_lastTime5', 'u5');
	set_init_useTable_checkboxes('m_howMuch6','m_howOften6', 'm_howLong6', 'm_howOld6', 'm_lastTime6', 'u6');
	set_init_useTable_checkboxes('m_howMuch7','m_howOften7', 'm_howLong7', 'm_howOld7', 'm_lastTime7', 'u7');
	set_init_useTable_checkboxes('m_howMuch8','m_howOften8', 'm_howLong8', 'm_howOld8', 'm_lastTime8', 'u8');
	set_init_useTable_checkboxes('m_howMuch9','m_howOften9', 'm_howLong9', 'm_howOld9', 'm_lastTime9', 'u9');
	set_init_useTable_checkboxes('m_howMuch10','m_howOften10', 'm_howLong10', 'm_howOld10', 'm_lastTime10', 'u10');
	set_init_useTable_checkboxes('m_howMuch11','m_howOften11', 'm_howLong11', 'm_howOld11', 'm_lastTime11', 'u11');
	set_init_useTable_checkboxes('m_howMuch12','m_howOften12', 'm_howLong12', 'm_howOld12', 'm_lastTime12', 'u12');
	set_init_useTable_checkboxes('m_howMuch13','m_howOften13', 'm_howLong13', 'm_howOld13', 'm_lastTime13', 'u13');
	set_init_useTable_checkboxes('m_howMuch14','m_howOften14', 'm_howLong14', 'm_howOld14', 'm_lastTime14', 'u14');
	set_init_useTable_checkboxes('m_howMuch15','m_howOften15', 'm_howLong15', 'm_howOld15', 'm_lastTime15', 'u15');
	set_init_useTable_checkboxes('m_howMuch16','m_howOften16', 'm_howLong16', 'm_howOld16', 'm_lastTime16', 'u16');
	set_init_useTable_checkboxes('m_howMuch17','m_howOften17', 'm_howLong17', 'm_howOld17', 'm_lastTime17', 'u17');
	set_init_useTable_checkboxes('m_howMuch18','m_howOften18', 'm_howLong18', 'm_howOld18', 'm_lastTime18', 'u18');
	set_init_useTable_checkboxes('m_howMuch19','m_howOften19', 'm_howLong19', 'm_howOld19', 'm_lastTime19', 'u19');
	set_init_useTable_checkboxes('m_howMuch20','m_howOften20', 'm_howLong20', 'm_howOld20', 'm_lastTime20', 'u20');
	set_init_useTable_checkboxes('m_howMuch21','m_howOften21', 'm_howLong21', 'm_howOld12', 'm_lastTime12', 'u21');

	if (grab('u21').checked === true) {
		grab('useOther').value = json_data.name21;
	}

	for (var i = 1; i <= 21; i++) {
		var boxName = 'u' + String(i);
		var targetName = 'm' + String(i);

		initialize_m_field(boxName, targetName);
	}

	turn_on_ut_text();
}


//++++++++++++++++++++++++++++++++++++++++++++++++++ MH Post Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++ MH Post Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++ MH Post Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++//
//++++++++++++++++++++++++++++++++++++++++++++++++++ MH Post Functions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++//

function postMhFields(section) {
	section = String(section);

	if (section == '/mh_demographic/') {
		mh_continue_demographic();
	}
	else if (section == '/mh_education/') {
		proceed_mh_education();
	}
	else if (section == '/mh_background/') {
		proceed_mh_background();
	}
	else if (section == '/mh_stress/') {
		proceed_mh_stress();
	}
	else if (section == '/mh_familyHistory/') {
		proceed_mh_familyHistory();
	}
	else if (section == '/mh_legal/') {
		proceed_mh_legalHistory();
	}
	else if (section == '/mh_psych/') {
		proceed_mh_psychHistory();
	}
	else if (section == '/mh_useTable/') {
		proceed_mh_useTable();
	}
}

function shouldReconstruct_childWindow_mh(radioName, valName, targetName) {
	radioName = String(radioName);
	valName = String(valName);
	targetName = String(targetName);
	var radio = getPopParent(radioName);
	var target = String(getPopParent(targetName).value);
	var data = String(getPopParent(valName).value);
	var reconstruct = true;

	if (target === data) {
		reconstruct = false;
	}

	return reconstruct;
}

function discard_mh_changes() {

}

function keep_mh_changes() {
	getPopParent('reconstruct').value = true;
	grab('s_form').submit();
}

function do_all_rocks() {
	kill_selects_mh('isdepressed', 'depressSide', 'depressMember', 'e1');
	kill_selects_mh('isadd', 'sideADD', 'memADD', 'e2');
	kill_selects_mh('isbedWetting', 'sideBed', 'memBed', 'e3');
	kill_selects_mh('isbipolar', 'sideBi', 'memBi', 'e4');
	kill_selects_mh('issuicideAttempt', 'sideATT', 'memATT', 'e5');
	kill_selects_mh('isphysicalAbuse', 'sidePA', 'memPA', 'e6');
	kill_selects_mh('islaw', 'sideLaw', 'memLaw', 'e7');
	kill_selects_mh('isld', 'sideLD', 'memLD', 'e8');
	kill_selects_mh('istic', 'sideTic', 'memTic', 'e9');
	kill_selects_mh('isthyroid', 'sideThy', 'memThy', 'e10');
	kill_selects_mh('isheart', 'sideHeart', 'memHeart', 'e11');
	kill_selects_mh('isoverweight', 'sideOW', 'memOW', 'e12');
	kill_selects_mh('ismood', 'sideMood', 'memMood', 'e13');
	kill_selects_mh('isalcohol', 'sideAlc', 'memAlc', 'e14');
	kill_selects_mh('isdrugs', 'sideDrug', 'memDrug', 'e15');
	kill_selects_mh('isschizo', 'sideSch', 'memSch', 'e16');
	kill_selects_mh('isseizures', 'sideSe', 'memSe', 'e17');
	kill_selects_mh('iscompletedSuicide', 'sideCS', 'memCS', 'e18');
	kill_selects_mh('issexAbuse', 'sideSex', 'memSex', 'e19');
	kill_selects_mh('ispanic', 'sidePanick', 'memPanick', 'e20');
	kill_selects_mh('isanxiety', 'sideAnx', 'memAnx', 'e21');
	kill_selects_mh('isOCD', 'sideOCD', 'memOCD', 'e22');
	kill_selects_mh('isdiabetes', 'sideSugar', 'memSugar', 'e23');
	kill_selects_mh('iscancer', 'sideCancer', 'memCancer', 'e24');
	kill_selects_mh('ishighBloodPressure', 'sideBlood', 'memBlood', 'e25');
	kill_selects_mh('isanger', 'sideAngry', 'memAngry', 'e26');
}

function rock_checkboxes1(option) {
	var newVal = null;
	option = String(option);

	if (option === 'clear') {
		grab('isdepressed').checked = false;
		grab('isadd').checked = false;
		grab('isbedWetting').checked = false;
		grab('isbipolar').checked = false;
		grab('issuicideAttempt').checked = false;
		grab('isphysicalAbuse').checked = false;
		grab('islaw').checked = false;
		grab('isld').checked = false;
		grab('istic').checked = false;
		grab('isthyroid').checked = false;
		grab('isheart').checked = false;
		grab('isoverweight').checked = false;
		grab('ismood').checked = false;
		grab('isalcohol').checked = false;
		grab('isdrugs').checked = false;
		grab('isschizo').checked = false;
		grab('isseizures').checked = false;
		grab('iscompletedSuicide').checked = false;
		grab('issexAbuse').checked = false;
		grab('ispanic').checked = false;
		grab('isanxiety').checked = false;
		grab('isOCD').checked = false;
		grab('isdiabetes').checked = false;
		grab('iscancer').checked = false;
		grab('ishighBloodPressure').checked = false;
		grab('isanger').checked = false;
		grab('checkAll').checked = false;
		newVal = 'False';
	}

	else if (option === 'check') {
		grab('isdepressed').checked = true;
		grab('isadd').checked = true;
		grab('isbedWetting').checked = true;
		grab('isbipolar').checked = true;
		grab('issuicideAttempt').checked = true;
		grab('isphysicalAbuse').checked = true;
		grab('islaw').checked = true;
		grab('isld').checked = true;
		grab('istic').checked = true;
		grab('isthyroid').checked = true;
		grab('isheart').checked = true;
		grab('isoverweight').checked = true;
		grab('ismood').checked = true;
		grab('isalcohol').checked = true;
		grab('isdrugs').checked = true;
		grab('isschizo').checked = true;
		grab('isseizures').checked = true;
		grab('iscompletedSuicide').checked = true;
		grab('issexAbuse').checked = true;
		grab('ispanic').checked = true;
		grab('isanxiety').checked = true;
		grab('isOCD').checked = true;
		grab('isdiabetes').checked = true;
		grab('iscancer').checked = true;
		grab('ishighBloodPressure').checked = true;
		grab('isanger').checked = true;
		grab('clearAll').checked = false;
		newVal = 'True';
	}

	for (var i = 1; i < 27; i++) {
		var name = 'check' + String(i);
		grab(name).value = newVal;
	}

	do_all_rocks();
}

function flick_family_switch() {
	grab('clearAll').checked = false;
	grab('checkAll').checked = false;
}

function number_min_error(minimum, data) {
	var hasError = false;
	data = Number(data);
	minimum = Number(minimum);

	if (data <= minimum) {
		hasError = true;
	}

	return hasError;
}

function grab_mh_demo_zeros() {
	var result = [];

	var d1 = {};
	d1['value'] = Number(grab('numMarriages').value);
	d1['minVal'] = 1;
	d1['isDynamic'] = true;
	di['trigger'] = grab('married').checked;
	d2['div'] = 'e4';
	result.push(d1);

	var d2 = {};
	d2['value'] = Number(grab('numMarriages').value);
	d2['minVal'] = 1;
	d2['isDynamic'] = true;
	d2['trigger'] = grab('divorced').checked;
	d2['div'] = 'e4';
	result.push(d2);

	var d3 = {};
	d3['value'] = Number(grab('numMarriages').value);
	d3['minVal'] = 1;
	d3['isDynamic'] = true;
	d3['trigger'] = grab('widowed').checked;
	d3['div'] = 'e4';
	result.push(d3);

	var d4 = {};
	d4['value'] = Number(grab('numMarriages').value);
	d4['minVal'] = 1;
	d4['isDynamic'] = true;
	d4['trigger'] = grab('seperated').checked;
	d4['div'] = 'e4';
	result.push(d4);

	var d5 = {};
	d5['value'] = Number(grab('spouseAge').value);
	d5['minVal'] = 12;
	d5['isDynamic'] = true;
	d5['trigger'] = grab('married').checked;
	d5['div'] = 'e11';
	result.push(d5);

	var d6 = {};
	d6['value'] = Number(grab('spouseAge').value);
	d6['minVal'] = 12;
	d6['isDynamic'] = true;
	d6['trigger'] = grab('seperated').checked;
	d6['div'] = 'e11';
	result.push(d6);

	return result;
}

function grab_mh_edu_zeros() {
	var result = [];
	var d1 = {}, d2 = {}, d3 = {};

	d1['value'] = Number(grab('numMore').value);
	d1['minVal'] = 5;
	d1['isDynamic'] = true;
	d1['trigger'] = grab('friendMore').checked;
	d1['div'] = 'e1';
	result.push(d1);

	d2['value'] = Number(grab('numMoreg7').value);
	d2['minVal'] = 5;
	d2['isDynamic'] = true;
	d2['trigger'] = grab('friendMoreg7').checked;
	d2['div'] = 'e2';
	result.push(d2);

	d3['value'] = Number(grab('numMoreg10').value);
	d3['minVal'] = 5;
	d3['isDynamic'] = true;
	d3['trigger'] = grab('friendMoreg10').checked;
	d3['div'] = 'e3';
	result.push(d3);

	return result;
}

function grab_mh_legal_zeros() {
	var result = [];

	var d1 = {};
	d1['value'] = Number(grab('num_suspended').value);
	d1['minVal'] = 1;
	d1['isDynamic'] = true;
	d1['trigger'] = grab('yesSuspended').checked;
	d1['div'] = 'e32';
	result.push(d1);

	return result;
}

function grab_mh_use_zeros() {
	var result = [];

	return result;
}

function fetch_min_zero_fields_mh(section) {
	var result = [];
	section = String(section);

	if (section === '/mh_demographic/') {
		result = grab_mh_demo_zeros();
	}
	else if (section === '/mh_education/') {
		result = grab_mh_edu_zeros();
	}
	else if (section === '/mh_legal/') {
		result = grab_mh_legal_zeros();
	}
	else if (section === '/mh_useTable/') {
		result = grab_mh_use_zeros();
	}

	return result;
}

function snag_min_fields_uni(fType, section) {
	var result = [];
	section = String(section);
	fType = String(fType);

	if (fType === 'mh') {
		result = fetch_min_zero_fields_mh(section);
	}
	else if (fType === 'asi') {

	}
	else if (fType === 'am') {

	}
	else if (fType === 'sap') {

	}

	return result;
}

function openMinErrorWindow(fList) {
	var openWindow = false;
	
	for (var i = 0; i < fList.length; i++) {
		if (fList[i]['isDynamic'] === true && fList[i]['trigger'] === true) {
			if (fList[i]['value'] < fList[i]['minVal']) {
				openWindow = true;
				break;
			}
			else {
				if (fList[i]['value'] < fList['minVal']) {
					openWindow = true;
					break;
				}
			}
		}
	}

	return openWindow;
}

function set_min_val_errors(item) {
	if (item['isDynamic'] === true && item['trigger'] === true) {
		if (Number(item['value']) < Number(item['minVal'])) {
			setErrorDiv(item['div']);
		}
	}
	// else {
	// 	if (Number(item['value']) < Number(item['minVal'])) {
	// 		setErrorDiv(item['div']);
	// 	}
	// }
}

function run_min_val_check(fType, section) {
	fType = String(fType);
	section = String(section);
	var fList = snag_min_fields_uni(fType, section);

	for (var i = 0; i < fList.length; i++) {
		set_min_val_errors(fList[i]);
	}
}


function post_mh_data(section) {
	section = String(section);

	if (section === '/mh_demographic/') {
		postMhFields(section);
		var next_url = grab('next_url');
		var form = grab('mh_form');
		grab('save_this').value = 'true';
		form.action = next_url.value;
		form.submit();
	}

	else {
		if (hasErrorsInForm('mh', section) === true) {
			superErrorChecker('mh', section);
			var w = 500, h = 500;
			openPopUp('auto', '/generateErrors/', w, h);
		}

		else {
			if (String(grab('min_checker').value) === 'true') {
				var fList = snag_min_fields_uni('mh', section);
				if (openMinErrorWindow(fList) === true) {
					run_min_val_check('mh', section);
					openPopUp('auto', '/generateErrors/', 500, 500);
				}
				else {
					postMhFields(section);
					var next_url = grab('next_url');
					var form = grab('mh_form');
					grab('save_this').value = 'true';
					form.action = next_url.value;
					form.submit();
				}
				
			}

			else {
				postMhFields(section);
				var next_url = grab('next_url');
				var form = grab('mh_form');
				grab('save_this').value = 'true';
				form.action = next_url.value;
				form.submit();
			}			
		}
	}
}


function set_op_value_null(triggerName, targetName) {
	targetName = String(targetName);
	triggerName = String(triggerName);
	var target = grab(targetName);
	var trigger = grab(triggerName);

	if (trigger.checked === true) {
		target.value = 'N/A';
	}
}

function run_parentAge_validation(liveRadioName, value, targetLifeName, targetDeathName) {
	value = Number(value);
	liveRadioName = String(liveRadioName);
	targetLifeName = String(targetLifeName);
	targetDeathName = String(targetDeathName);

	var liveRadio = grab(liveRadioName);
	var target_life = grab(targetLifeName);
	var target_death = grab(targetDeathName);

	if (liveRadio.checked === true) {
		target_life.value = value;
		target_death.value = 0;
	}
	else {
		target_life.value = 0;
		target_death.value = value;
	}
}

function run_marriage_validation_mh() {
	if (grab('divorced').checked === true || grab('widowed').checked === true) {
		grab('m_numMarriages').value = grab('numMarriages').value;
		grab('m_spouseOccupation').value = 'N/A';
		grab('m_spouseEmployer').value = 'N/A';
		grab('m_spouseAge').value = '0';
		grab('m_spouseWorkMos').value = '0';
		grab('m_spouseWorkYrs').value = '0';
	}

	else if (grab('married').checked === true || grab('seperated').checked === true) {
		grab('m_numMarriages').value = grab('numMarriages').value;
		grab('m_spouseOccupation').value = grab('spouseOccupation').value;
		grab('m_spouseEmployer').value = grab('spouseEmployer').value;
		grab('m_spouseAge').value = grab('spouseAge').value;
		grab('m_spouseWorkMos').value = grab('spouseWorkMos').value;
		grab('m_spouseWorkYrs').value = grab('spouseWorkYrs').value;
	}

	else {
		grab('m_numMarriages').value = '0';
		grab('m_spouseOccupation').value = 'N/A';
		grab('m_spouseEmployer').value = 'N/A';
		grab('m_spouseAge').value = '0';
		grab('m_spouseWorkMos').value = '0';
		grab('m_spouseWorkYrs').value = '0';
	}
}

function mh_continue_demographic() {
	//POST NON-DYNAMIC TEXT FIELDS
	post(false, 'text', grab('birthplace'), null, null);
	post(false, 'text', grab('raised'), null, null);
	post(false, 'text', grab('occupation'), null, null);
	post(false, 'text', grab('employer'), null, null);
	post(false, 'text', grab('pastJobs'), null, null);
	post(false, 'text', grab('recentMove'), null, null);
	post(false, 'text', grab('motherOccupation'), null, null);
	post(false, 'text', grab('motherCity'), null, null);
	post(false, 'text', grab('fatherOccupation'), null, null);
	post(false, 'text', grab('fatherCity'), null, null);

	//POST NON-DYNAMIC NUMBER FIELDS
	post(false, 'number', grab('employedMo'), null, null);
	post(false, 'number', grab('employedYrs'), null, null);

	//POST RADIO BUTTONS
	run_parentAge_validation('momIsLiving', grab('motherAge').value, 'm_motherAge', 'm_motherAgeDeath');
	run_parentAge_validation('dadIsLiving', grab('fatherAge').value, 'm_fatherAge', 'm_fatherAgeDeath');

	grab('d_mom_state').value = grab('motherState').value;
	grab('d_dad_state').value = grab('fatherState').value;

	run_marriage_validation_mh();
}

function proceed_mh_background() {
	post(false, 'text', grab('interest'), null, null);
	post(false, 'text', grab('friendAct'), null, null);
	post(false, 'text', grab('workAct'), null, null);
	post(false, 'text', grab('churchAffiliation'), null, null);

	post(false, 'number', grab('closeFriendNumber'), null, null);
	post(false, 'number', grab('acqNumber'), null, null);
	post(false, 'number', grab('interestWeek'), null, null);
	post(false, 'number', grab('interestMonth'), null, null);
	post(false, 'number', grab('friendActWeek'), null, null);
	post(false, 'number', grab('friendActMonth'), null, null);
	post(false, 'number', grab('workActWeek'), null, null);
	post(false, 'number', grab('workActMonth'), null, null);
	post(false, 'number', grab('churchWeek'), null, null);
	post(false, 'number', grab('churchMonth'), null, null);
	post(false, 'number', grab('churchYear'), null, null);
}

function shouldKillZeros_post(triggerName, fieldName) {
	triggerName = String(triggerName);
	fieldName 	= String(fieldName);

	var shouldKill = false;
	var trigger = grab(triggerName);
	var field 	= grab(fieldName);
	var val 	= Number(field.value);

	if (trigger.checked === true && val < 5) {
		shouldKill = true;
	}
	return shouldKill;
}

function kill_zeros_during_post(triggerName, fieldName, divName) {
	triggerName = String(triggerName);
	fieldName 	= String(fieldName);
	divName 	= String(divName);

	var trigger = grab(triggerName);
	var field 	= grab(fieldName);
	var val 	= Number(field.value);

	if (trigger.checked === true && val < 5) {
		setErrorDiv(divName);
	}
}

function kill_mh_ed_zeros() {
	kill_zeros_during_post('friendMore', 'numMore', 'e1');
	kill_zeros_during_post('friendMoreg7', 'numMoreg7', 'e2');
	kill_zeros_during_post('friendMoreg10', 'numMoreg10', 'e3');
	openPopUp('auto', '/error_zero/', 500, 500);
}


function post_operation_has_erZero() {
	var hasError = false;

	var er_k = shouldKillZeros_post('friendMore', 'numMore');
	var er_m = shouldKillZeros_post('friendMoreg7', 'numMoreg7');
	var er_h = shouldKillZeros_post('friendMoreg10', 'numMoreg10');

	if (er_k === true || er_m === true || er_h === true) {
		hasError = true;
	}

	return hasError;
}

function set_m_honorable() {
	if (grab('yesHonor').checked === true) {
		grab('m_honorableDischarge').value = 'True';
	}
	else {
		grab('m_honorableDischarge').value = 'False';
	}
}

function set_college_m_data() {
	if (grab('collegeNone').checked === true) {
		grab('m_college_trigger').value = 'false';
	}
	else {
		grab('m_college_trigger').value = 'true';
	}
}

function proceed_mh_education() {
	// var fk1 = document.getElementById('friend1');
	// var fk2 = document.getElementById('friend2');
	// var fk3 = document.getElementById('friend3');
	// var fk4 = document.getElementById('friend4');
	// var fkm = document.getElementById('friendMore');
	// var numMore = document.getElementById('numMore');
	// var m_FriendshipsKto6 = document.getElementById('m_FriendshipsKto6');
	// var f7g1 = document.getElementById('friend1g7');
	// var f7g2 = document.getElementById('friend2g7');
	// var f7g3 = document.getElementById('friend3g7');
	// var f7g4 = document.getElementById('friend4g7');
	// var f7gm = document.getElementById('friendMoreg7');
	// var numMoreg7 = document.getElementById('numMoreg7');
	// var m_Friendships7to9 = document.getElementById('m_Friendships7to9');
	// var f10g1 = document.getElementById('friend1g10');
	// var f10g2 = document.getElementById('friend2g10');
	// var f10g3 = document.getElementById('friend3g10');
	// var f10g4 = document.getElementById('friend4g10');
	// var f10gm = document.getElementById('friendMoreg10');
	// var numMoreg10 = document.getElementById('numMoreg10');
	// var Friendships10to12 = document.getElementById('m_Friendships10to12');	

	// postMhEducationFriendNumber(fk1, fk2, fk3, fk4, fkm, numMore, m_FriendshipsKto6);
	// postMhEducationFriendNumber(f7g1, f7g2, f7g3, f7g4, f7gm, numMoreg7, m_Friendships7to9);
	// postMhEducationFriendNumber(f10g1, f10g2, f10g3, f10g4, f10gm, numMoreg10, Friendships10to12);

	post(true, 'text', grab('tradeSchool'), grab('yesTrade'), grab('m_tradeSchool'));
	post(true, 'text', grab('tradeAreaStudy'), grab('yesTrade'), grab('m_tradeAreaStudy'));
	post(true, 'text', grab('militaryBranch'), grab('yesMillitary'), grab('m_militaryBranch'));
	post(true, 'number', grab('militaryYears'), grab('yesMillitary'), grab('m_militaryYears'));
	post(true, 'text', grab('militaryRank'), grab('yesMillitary'), grab('m_militaryRank'));
	post(true, 'text', grab('militaryRank'), grab('yesMillitary'), grab('m_militaryRank'));

	if (String(grab('m_college_trigger').value) === 'true') {
		grab('m_collegeDegree').value = grab('collegeDegree').value;
		grab('m_collegeMajor').value = grab('collegeMajor').value;
		
		if (grab('yesAdvanced').checked === true) {
			grab('m_advanceDegree').value = 'True';
		}
		else {
			grab('m_advanceDegree').value = 'False';
		}
	}
	else {
		grab('m_collegeDegree').value = 'N/A';
		grab('m_collegeMajor').value = 'N/A';
		grab('m_advanceDegree').value = 'False';
	}
}

function proceed_mh_stress() {
	post(true, 'text', grab('deathStressExp'), grab('yesDeath'), grab('m_deathStressExp'));
	post(true, 'text', grab('divorceStressExp'), grab('yesDivorce'), grab('m_divorceStressExp'));
	post(true, 'text', grab('moveStressExp'), grab('yesMove'), grab('m_moveStressExp'));
	post(true, 'text', grab('medicalStressExp'), grab('yesMedical'), grab('m_medicalStressExp'));
	post(true, 'text', grab('familyHealthStressExp'), grab('yesFamily'), grab('m_familyHealthStressExp'));
	post(true, 'text', grab('financialStressExp'), grab('yesMoney'), grab('m_financialStressExp'));
	post(true, 'text', grab('abuseStressExp'), grab('yesAbuse'), grab('m_abuseStressExp'));
	post(true, 'text', grab('addictionFamilyStressExp'), grab('yesAddiction'), grab('m_addictionFamilyStressExp'));
	post(true, 'text', grab('violenceFamilyStressExp'), grab('yesViolence'), grab('m_violenceFamilyStressExp'));
	post(true, 'text', grab('otherStressExp'), grab('yesOther'), grab('m_otherStressExp'));
}

function proceed_mh_familyHistory() {
	combineFamilyValues(grab('isdepressed'), grab('depressSide'), grab('depressMember'), grab('depressed'));
	combineFamilyValues(grab('isadd'), grab('sideADD'), grab('memADD'), grab('add'));
	combineFamilyValues(grab('isbedWetting'), grab('sideBed'), grab('memBed'), grab('bedWetting'));
	combineFamilyValues(grab('isbipolar'), grab('sideBi'), grab('memBi'), grab('bipolar'));
	combineFamilyValues(grab('issuicideAttempt'), grab('sideATT'), grab('memATT'), grab('suicideAttempt'));
	combineFamilyValues(grab('isphysicalAbuse'), grab('sidePA'), grab('memPA'), grab('physicalAbuse'));
	combineFamilyValues(grab('islaw'), grab('sideLaw'), grab('memLaw'), grab('law'));
	combineFamilyValues(grab('isld'), grab('sideLD'), grab('memLD'), grab('ld'));
	combineFamilyValues(grab('istic'), grab('sideTic'), grab('memTic'), grab('tic'));
	combineFamilyValues(grab('isthyroid'), grab('sideThy'), grab('memThy'), grab('thyroid'));
	combineFamilyValues(grab('isheart'), grab('sideHeart'), grab('memHeart'), grab('heart'));
	combineFamilyValues(grab('isoverweight'), grab('sideOW'), grab('memOW'), grab('overweight'));
	combineFamilyValues(grab('ismood'), grab('sideMood'), grab('memMood'), grab('mood'));
	combineFamilyValues(grab('isalcohol'), grab('sideAlc'), grab('memAlc'), grab('alcohol'));
	combineFamilyValues(grab('isdrugs'), grab('sideDrug'), grab('memDrug'), grab('drugs'));
	combineFamilyValues(grab('isschizo'), grab('sideSch'), grab('memSch'), grab('schizo'));
	combineFamilyValues(grab('isseizures'), grab('sideSe'), grab('memSe'), grab('seizures'));
	combineFamilyValues(grab('iscompletedSuicide'), grab('sideCS'), grab('memCS'), grab('completedSuicide'));
	combineFamilyValues(grab('issexAbuse'), grab('sideSex'), grab('memSex'), grab('sexAbuse'));
	combineFamilyValues(grab('ispanic'), grab('sidePanick'), grab('memPanick'), grab('panic'));
	combineFamilyValues(grab('isanxiety'), grab('sideAnx'), grab('memAnx'), grab('anxiety'));
	combineFamilyValues(grab('isOCD'), grab('sideOCD'), grab('memOCD'), grab('OCD'));
	combineFamilyValues(grab('isdiabetes'), grab('sideSugar'), grab('memSugar'), grab('diabetes'));
	combineFamilyValues(grab('iscancer'), grab('sideCancer'), grab('memCancer'), grab('cancer'));
	combineFamilyValues(grab('ishighBloodPressure'), grab('sideBlood'), grab('memBlood'), grab('highBloodPressure'));
	combineFamilyValues(grab('isanger'), grab('sideAngry'), grab('memAngry'), grab('anger'));
}

function proceed_mh_legalHistory() {
	post(false, 'text', grab('arrestCharges'), null, null);
	post(false, 'text', grab('convictionCharges'), null, null);

	post(true, 'text', grab('probationOfficer'), grab('haveBeen'), grab('m_probationOfficer'));
	post(true, 'text', grab('probationOffense'), grab('haveBeen'), grab('m_probationOffense'));
	post(true, 'text', grab('dateBenkrupcy'), grab('yesBank'), grab('m_dateBenkrupcy'));

	post(true, 'number', grab('num_suspended'), grab('yesSuspended'), grab('m_num_suspended'));

	if (grab('yesSuit').checked===true || grab('yesDivPro').checked===true || grab('yesChildDis').checked===true || grab('yesBank').checked === true) {
		grab('m_positive').value = grab('explainPositiveAnswers').value;
	}
	else {
		grab('m_positive').value = 'N/A';
	}

	if (grab('haveBeen').checked === true) {
		if (grab('yesCurrentProb').checked === true) {
			grab('m_nowProb').value = 'True';
		}
		else {
			grab('m_nowProb').value = 'False';
		}
	}
	else {grab('m_nowProb').value = 'False';}
	
	if (grab('yesSuspended').checked === true) {
		if (grab('yesCurrentSus').checked === true) {
			grab('m_currSus').value = 'True';
		}
		else {
			grab('m_currSus').value = 'False';
		}
	}
	else {grab('m_currSus').value = 'False';}

	if (grab('yesSuit').checked === true) {
		if (grab('yesStress').checked === true) {
			grab('m_lawsuitStress').value = 'True';
		}
		else {
			grab('m_lawsuitStress').value = 'False';
		}
	}
	else {grab('m_lawsuitStress').value = 'False';}
}

function proceed_mh_psychHistory() {
	post(false, 'text', grab('psychiatricHistory'), null, null);
}

function proceed_mh_useTable() {
	
}

//******************************** MH SUPPORT FUNCTIONS ************************************************
//******************************** MH SUPPORT FUNCTIONS ************************************************
//******************************** MH SUPPORT FUNCTIONS ************************************************
//******************************** MH SUPPORT FUNCTIONS ************************************************

function killLabel_no(trigger, label) {
	if (trigger.checked === false) {
		opacityHigh(label);
	}
	else {
		opacityLow(label);
	}
}

function killLabel(trigger, label) {
	if (trigger.checked === true) {
		opacityHigh(label);
	}
	else {
		opacityLow(label);
	}
}

function mhSinglePlay() {
	twoElementRadioSetupNumber_no(grab('single'), grab('numMarriages_label'), grab('numMarriages'));
	twoElementRadioSetupNumber_no(grab('single'), grab('spouseAge_label'), grab('spouseAge'));
	twoElementRadioSetupNumber_no(grab('single'), grab('syears'), grab('spouseWorkYrs'));
	twoElementRadioSetupNumber_no(grab('single'), grab('smonths'), grab('spouseWorkMos'));
	twoElementRadioSetup_no(grab('single'), grab('spouseEmployer_label'), grab('spouseEmployer'));
	twoElementRadioSetup_no(grab('single'), grab('spouseOccupation_label'), grab('spouseOccupation'));
	killLabel_no(grab('single'), grab('num12'));
	killLabel_no(grab('single'), grab('num13'));
	killLabel_no(grab('single'), grab('num14'));
	killLabel_no(grab('single'), grab('num15'));
	killLabel_no(grab('single'), grab('spouseWorkMos_label'));
	killLabel_no(grab('single'), grab('num4'));
}

function mhMarriedPlay() {
	twoElementRadioSetupNumber(grab('married'), grab('numMarriages_label'), grab('numMarriages'));
	twoElementRadioSetupNumber(grab('married'), grab('spouseAge_label'), grab('spouseAge'));
	twoElementRadioSetupNumber(grab('married'), grab('syears'), grab('spouseWorkYrs'));
	twoElementRadioSetupNumber(grab('married'), grab('smonths'), grab('spouseWorkMos'));
	twoElementRadioSetup(grab('married'), grab('spouseEmployer_label'), grab('spouseEmployer'));
	twoElementRadioSetup(grab('married'), grab('spouseOccupation_label'), grab('spouseOccupation'));
	killLabel(grab('married'), grab('num4'));
	killLabel(grab('married'), grab('num12'));
	killLabel(grab('married'), grab('num13'));
	killLabel(grab('married'), grab('num14'));
	killLabel(grab('married'), grab('num15'));
	killLabel(grab('married'), grab('spouseWorkMos_label'));
}

function mhBreakPlay() {
	twoElementRadioSetupNumber(grab('seperated'), grab('numMarriages_label'), grab('numMarriages'));
	twoElementRadioSetupNumber(grab('seperated'), grab('spouseAge_label'), grab('spouseAge'));
	twoElementRadioSetupNumber(grab('seperated'), grab('syears'), grab('spouseWorkYrs'));
	twoElementRadioSetupNumber(grab('seperated'), grab('smonths'), grab('spouseWorkMos'));
	twoElementRadioSetup(grab('seperated'), grab('spouseEmployer_label'), grab('spouseEmployer'));
	twoElementRadioSetup(grab('seperated'), grab('spouseOccupation_label'), grab('spouseOccupation'));
	killLabel(grab('seperated'), grab('num4'));
	killLabel(grab('seperated'), grab('num12'));
	killLabel(grab('seperated'), grab('num13'));
	killLabel(grab('seperated'), grab('num14'));
	killLabel(grab('seperated'), grab('num15'));
	killLabel(grab('seperated'), grab('spouseWorkMos_label'));
}

function mhDivorcePlay() {
	twoElementRadioSetupNumber(grab('divorced'), grab('numMarriages_label'), grab('numMarriages'));
	killLabel(grab('divorced'), grab('num4'));

	twoElementRadioSetupNumber_no(grab('divorced'), grab('spouseAge_label'), grab('spouseAge'));
	twoElementRadioSetupNumber_no(grab('divorced'), grab('syears'), grab('spouseWorkYrs'));
	twoElementRadioSetupNumber_no(grab('divorced'), grab('smonths'), grab('spouseWorkMos'));
	twoElementRadioSetup_no(grab('divorced'), grab('spouseEmployer_label'), grab('spouseEmployer'));
	twoElementRadioSetup_no(grab('divorced'), grab('spouseOccupation_label'), grab('spouseOccupation'));

	killLabel_no(grab('divorced'), grab('num12'));
	killLabel_no(grab('divorced'), grab('num13'));
	killLabel_no(grab('divorced'), grab('num14'));
	killLabel_no(grab('divorced'), grab('num15'));
	killLabel_no(grab('divorced'), grab('spouseWorkMos_label'));
}

function mhWidowPlay() {
	twoElementRadioSetupNumber(grab('widowed'), grab('numMarriages_label'), grab('numMarriages'));
	killLabel(grab('widowed'), grab('num4'));

	twoElementRadioSetupNumber_no(grab('widowed'), grab('spouseAge_label'), grab('spouseAge'));
	twoElementRadioSetupNumber_no(grab('widowed'), grab('syears'), grab('spouseWorkYrs'));
	twoElementRadioSetupNumber_no(grab('widowed'), grab('smonths'), grab('spouseWorkMos'));
	twoElementRadioSetup_no(grab('widowed'), grab('spouseEmployer_label'), grab('spouseEmployer'));
	twoElementRadioSetup_no(grab('widowed'), grab('spouseOccupation_label'), grab('spouseOccupation'));

	killLabel_no(grab('widowed'), grab('num12'));
	killLabel_no(grab('widowed'), grab('num13'));
	killLabel_no(grab('widowed'), grab('num14'));
	killLabel_no(grab('widowed'), grab('num15'));
	killLabel_no(grab('widowed'), grab('spouseWorkMos_label'));
}

function mhSpouse() {
	if (grab('single').checked === true) {
		mhSinglePlay();
	}
	else if (grab('married').checked === true) {
		mhMarriedPlay();
	}
	else if (grab('seperated').checked === true) {
		mhBreakPlay();
	}
	else if (grab('divorced').checked === true) {
		mhDivorcePlay();
	}
	else if (grab('widowed').checked === true){
		mhWidowPlay();
	}
}

function mhChildren() {
	if (grab('yesChild').checked === true) {
		grab('childrenMale').value = grab('m_holder').value;
		grab('childrenFemale').value = grab('f_holder').value;
		grab('m_holder').value = 'N/A';
		grab('f_holder').value = 'N/A';
	}
	else if (grab('noChild').checked === true) {
		grab('m_holder').value = grab('childrenMale').value;
		grab('f_holder').value = grab('childrenFemale').value;
		grab('childrenMale').value = 'N/A';
		grab('childrenFemale').value = 'N/A';
	}
}

function mhSister() {
	if (grab('yesSister').checked === true) {
		grab('m_sistersFinal').value = grab('s_holder').value;
	}
	else if (grab('noSister').checked === true) {
		grab('s_holder').value = grab('m_sistersFinal').value;
		grab('m_sistersFinal').value = 'N/A';
	}
}

function mhBrother() {
	if (grab('yesBrother').checked === true) {
		grab('m_brothersFinal').value = grab('b_holder').value;
	}
	else if (grab('noBrother').checked === true) {
		grab('b_holder').value = grab('m_brothersFinal').value;
		grab('m_brothersFinal').value = 'N/A';
	}
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

	if (grab('friendMore').checked === false) {
		opacityZero(grab('numMore_label'));
		opacityZero(grab('numMore'));
		grab('e1').className = '';
	}

	if (grab('friendMoreg7').checked === false) {
		opacityZero(grab('numMore_labelg7'));
		opacityZero(grab('numMoreg7'));
		grab('e2').className = '';
	}

	if (grab('friendMoreg10').checked === false) {
		opacityZero(grab('numMore_labelg10'));
		opacityZero(grab('numMoreg10'));
		grab('e3').className = '';
	}
}

function set_college_stats_mh() {
	if (grab('collegeNone').checked === true) {
		grab('m_college_trigger').value = 'false';
	}
	else {
		grab('m_college_trigger').value = 'true';
	}
}

function mhCollegeRadio() {
	var yr1 = grab('college1');
	var yr2 = grab('college2');
	var yr3 = grab('college3');
	var yr4 = grab('college4');

	if (yr1.checked===true || yr2.checked===true || yr3.checked===true || yr4.checked===true) {
		grab('collegeDegree').disabled = false;
		grab('collegeMajor').disabled = false;
		grab('yesAdvanced').disabled = false;
		grab('noAdvanced').disabled = false;

		opacityHigh(grab('colGradLab1'));
		opacityHigh(grab('colMaj1'));
		opacityHigh(grab('advDeg1'));
		opacityHigh(grab('collegeDegree'));
		opacityHigh(grab('collegeMajor'));
		opacityHigh(grab('yesAdvanced'));
		opacityHigh(grab('noAdvanced'));
		opacityHigh(grab('labM1'));
		opacityHigh(grab('labM2'));
	}
	else {
		grab('collegeDegree').value = '';
		grab('collegeMajor').value = '';
		grab('noAdvanced').checked = true;

		grab('collegeDegree').disabled = true;
		grab('collegeMajor').disabled = true;
		grab('yesAdvanced').disabled = true;
		grab('noAdvanced').disabled = true;

		opacityLow(grab('colGradLab1'));
		opacityLow(grab('colMaj1'));
		opacityLow(grab('advDeg1'));
		opacityLow(grab('collegeDegree'));
		opacityLow(grab('collegeMajor'));
		opacityLow(grab('yesAdvanced'));
		opacityLow(grab('noAdvanced'));
		opacityLow(grab('labM1'));
		opacityLow(grab('labM2'));

		grab('noAdvanced').checked = true;
	}

	set_college_stats_mh();
}

function mhTrade() {
	twoElementRadioSetup(grab('yesTrade'), grab('ts1'), grab('tradeAreaStudy'));
	twoElementRadioSetup(grab('yesTrade'), grab('ts2'), grab('tradeSchool'));
}

function mhMilitary() {
	twoElementRadioSetup(grab('yesMillitary'), grab('mt1'), grab('militaryBranch'));
	twoElementRadioSetupNumber(grab('yesMillitary'), grab('mt2'), grab('militaryYears'));
	twoElementRadioSetup(grab('yesMillitary'), grab('mt3'), grab('militaryRank'));
	twoElementRadioSetup(grab('yesMillitary'), grab('mt5'), grab('yesHonor'));
	twoElementRadioSetup(grab('yesMillitary'), grab('mt6'), grab('noHonor'));

	if (grab('yesMillitary').checked === true) {
		opacityHigh(grab('mt4'));
		opacityHigh(grab('mt7'));
	}
	else {
		opacityLow(grab('mt4'));
		opacityLow(grab('mt7'));
		grab('noHonor').checked = true;
	}
}

function grabGradeRadio(grade, r1, r2, r3, r4, r5, r6) {
	grade = String(grade);

	if (grade === 'F') {
		r6.checked = true;
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
		r1.checked = true;
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
	else {
		r3.checked = true;
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

function postUniversalRadioSEL(trigger, textField, m_post) {
	if (trigger.checked === true) {
		m_post.value = textField.value;
	}
	else {
		m_post.value = 'None Selected';
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




function combineFamilyValues(trigger, fSide, fMem, m_post) {
	if (trigger.checked === true) {
		temp = String(fSide.value) + ' ' + String(fMem.value);
		m_post.value = temp;
	}

	else {
		m_post.value = 'N/A';
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

function opacityZero(element) {
	element.style.opacity = '0.0';
}


function mhStressRadio(triggerName, elementName, borderName) {
	triggerName = String(triggerName);
	elementName = String(elementName);
	borderName = String(borderName);

	var trigger = grab(triggerName);
	var element = grab(elementName);
	var border = grab(borderName);

	if (trigger.checked === true) {
		element.disabled = false;
		opacityHigh(element);
		border.style.borderColor = '#5cd65c';
	}
	else {
		opacityLow(element);
		element.value = '';
		element.disabled = true;
		border.style.borderColor = 'red';
	}
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
	twoElementRadioSetup(grab('haveBeen'), grab('p2'), grab('yesCurrentProb'));
	twoElementRadioSetup(grab('haveBeen'), grab('p3'), grab('noCurrentProb'));
	twoElementRadioSetup(grab('haveBeen'), grab('p4'), grab('probationOfficer'));
	twoElementRadioSetup(grab('haveBeen'), grab('p5'), grab('probationOffense'));

	if (grab('haveBeen').checked === true) {
		opacityHigh(grab('p1'));
	}
	else {
		opacityLow(grab('p1'));
		grab('noCurrentProb').checked = true;
	}
}

function mhSuspension1() {
	twoElementRadioSetupNumber(grab('yesSuspended'), grab('s1'), grab('num_suspended'));
	twoElementRadioSetup(grab('yesSuspended'), grab('s3'), grab('yesCurrentSus'));
	twoElementRadioSetup(grab('yesSuspended'), grab('s4'), grab('noCurrentSus'));

	if (grab('yesSuspended').checked === true) {
		opacityHigh(grab('s2'));
	}
	else {
		opacityLow(grab('s2'));
		grab('noCurrentSus').checked = true;
	}
}

function mhLawsuits() {
	twoElementRadioSetup(grab('yesSuit'), grab('ls1'), grab('yesStress'));
	twoElementRadioSetup(grab('yesSuit'), grab('ls2'), grab('noStress'));

	if (grab('yesSuit').checked === true) {
		opacityHigh(grab('ls3'));
	}
	else {
		opacityLow(grab('ls3'));
		grab('noStress').checked = true;
	}
}

function mhBank() {
	twoElementRadioSetup(grab('yesBank'), grab('blab1'), grab('dateBenkrupcy'));
}

function p_answer1_mh() {
	var t1 = grab('yesSuit').checked;
	var t2 = grab('yesDivPro').checked;
	var t3 = grab('yesChildDis').checked;
	var t4 = grab('yesBank').checked;

	if (t1===true || t2===true || t3===true || t4===true) {
		grab('explainPositiveAnswers').disabled = false;
		opacityHigh(grab('epa1'));
		opacityHigh(grab('explainPositiveAnswers'));
	}
	else if (t1===false && t2===false && t3===false && t4===false) {
		opacityLow(grab('epa1'));
		opacityLow(grab('explainPositiveAnswers'));
		grab('explainPositiveAnswers').value = '';
		grab('explainPositiveAnswers').disabled = true;
	}
}

function kill_selects_mh(triggerName, sel1Name, sel2Name, errorName) {
	var trigger = grab(triggerName);
	var sel1 	= grab(sel1Name);
	var sel2 	= grab(sel2Name);
	var erDiv 	= grab(errorName);

	if (trigger.checked === true) {
		sel1.disabled = false;
		sel2.disabled = false;
		opacityHigh(sel1);
		opacityHigh(sel2);
	}
	else {
		opacityZero(sel1);
		opacityZero(sel2);
		sel1.selectedIndex = 0;
		sel2.selectedIndex = 0;
		sel1.disabled = true;
		sel2.disabled = true;
		erDiv.className = '';
	}
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

function roommate_search() {
	var form = grab('c_form');
	form.action = '/roommate_page/';
	form.submit();
}

function exit_roommate_page() {
	var form = grab('r_form');
	form.action = '/adminHome/';
	form.submit();
}

function exit_roommate_sub() {
	var form = grab('r_form');
	form.action = '/roommate_page/';
	form.submit();
}

function roommate_new() {
	var form = grab('r_form');
	form.action = '/roommate_new/';
	form.submit();
}

function roommate_ref() {
	var form = grab('r_form');
	form.action = '/roommate_ref/';
	form.submit();
}

function roommate_eval() {
	var form = grab('r_form');
	form.action = '/roommate_eval/';
	form.submit();
}

function roommate_all() {
	var form = grab('r_form');
	form.action = '/roommate_all/';
	form.submit();
}

function roommate_win() {
	var form = grab('r_form');
	form.action = '/roommate_win/';
	form.submit();
}

function setCandidiate() {
	var box = grab('isCandidate');

	if (box.checked === true) {
		box.value = 'True';
	}
	else {
		box.value = 'False';
	}
}

function auth_creditCheck() {
	var box = grab('isAuthorized');

	if (box.checked === true) {
		box.value = 'True';
	}
	else {
		box.value = 'False';
	}
}

function choose_applicant(fname, lname, photoName, a_id) {
	fname = String(fname);
	lname = String(lname);
	photoName = String(photoName);
	var name = fname + ' ' + lname;
	grab('a_name').innerHTML = name;
	grab('a_name').className = 'applicant_name';
	grab('a_photo_wrapper').className = 'applicant_photo';
	grab('a_photo').src = '/static/media/' + photoName;
	grab('current').value = a_id;
}

function save_new_candidate() {
	grab('save_this').value = 'new_roommate';
	grab('r_form').action = '/roommate_page/';
	grab('r_form').submit();
}

function initialize_new_save_rm(saveType) {
	saveType = String(saveType);
	grab('header_type').innerHTML = saveType;
}

function save_application() {
	grab('save_this').value = 'new_application';
	grab('r_form').action = '/roommate_page/';
	grab('r_form').submit();
}

function continue_app_eval() {
	if (String(grab('current').value) !== '') {
		grab('r_form').action = '/roommate_profile/';
		grab('r_form').submit();
	}	
}

function save_rm_evaluation2() {
	grab('save_this').value = 'save_evaluation';
	grab('r_form').action = '/roommate_eval/';
	grab('r_form').submit();
}

function set_rm_checkBox(divName, checked) {
	checked = String(checked);
	divName = String(divName);

	box = grab(divName);

	if (checked === 'True') {
		box.checked = true;
	}
	else {
		box.checked = false;
	}
}

function initialize_rm_profile() {
	stub = String(grab('stub').value);
	credit = String(grab('credit').value);
	d_id = String(grab('d_id').value);
	ref1 = String(grab('ref1').value);
	ref2 = String(grab('ref2').value);
	ref3 = String(grab('ref3').value);
	work = String(grab('work').value);
	pNality = String(grab('pNality').value);
	candidate = String(grab('candidate').value);
	notes = String(grab('d_notes').value);

	set_rm_checkBox('hasCheckstubs', stub);
	set_rm_checkBox('hasCredit', credit);
	set_rm_checkBox('hasId', d_id);
	set_rm_checkBox('ref1_verified', ref1);
	set_rm_checkBox('ref2_verified', ref2);
	set_rm_checkBox('ref3_verified', ref3);
	set_rm_checkBox('work_verified', work);
	set_rm_checkBox('personality', pNality);
	set_rm_checkBox('isCandidate', candidate);

	rm_verify_check('hasCheckstubs');
	rm_verify_check('hasCredit');
	rm_verify_check('hasId');
	rm_verify_check('ref1_verified');
	rm_verify_check('ref2_verified');
	rm_verify_check('ref3_verified');
	rm_verify_check('work_verified');
	rm_verify_check('personality');
	rm_verify_check('isCandidate');

	if (notes === 'None' || notes === null) {
		grab('notes').innerHTML = '';
	}
}

function rm_verify_check(boxName) {
	boxName = String(boxName);
	var box = grab(boxName);

	if (box.checked === true) {
		box.value = 'True';
	}
	else {
		box.value = 'False';
	}
}

function rm_image_over() {
	var image = grab('a_photo');
	image.style.opacity = '0.5';
}

function rm_image_off() {
	var image = grab('a_photo');
	image.style.opacity = '1.0';
}

function view_rm_application() {
	grab('r_form').action = '/roommate_view_application/';
	grab('r_form').submit();
}

function clear_ratings() {
	for (var i = 1; i <=5; i++) {
		var imageName = 'f' + String(i);
		var divName = 'd' + String(i);

		var image = grab(imageName);
		var div = grab(divName);

		image.className = 'fa fa-star-o';
		div.className = 'rate_rm1';
	}
}

function rate_rm(rating) {
	rating = Number(rating);
	grab('rating').value = rating;
	clear_ratings();

	for (var i = 1; i <= rating; i++) {
		var imageName = 'f' + String(i);
		var divName = 'd' + String(i);

		var image = grab(imageName);
		var div = grab(divName);

		image.className = 'fa fa-star';
		div.className = 'rate_rm2';
	}
}

function set_re_val(position, applicant_id) {
	position = String(position);
	applicant_id = String(applicant_id);
	var divName = 're' + position;
	var div = grab(divName);

	if (grab(position).checked === true) {
		div.value = applicant_id;
	}
	else {
		div.value = 'empty';
	}
}

function remove_candidates() {
	var willRemove = false;

	for (var i = 1; i <= 12; i++) {
		var name = 're' + String(i);
		var div = grab(name);
		var value = String(div.value);

		if (value !== 'empty') {
			willRemove = true;
			break;
		}
	}

	if (willRemove === true) {
		openPopUp('auto', '/verify_rm_delete/', 400, 400);
	}
	else {
		grab('save_this').value = '';
		var form = grab('r_form');
		form.action = '/roommate_page/';
		form.submit();
	}
}

function initialize_rm_delete_page() {
	var mainDiv = grab('remove_list');
	var mainDivRight = grab('remove_list2');

	var r_list = [];
	var html_left = '';
	var html_right = '';

	for (var i = 1; i <= 12; i++) {
		var name = 're' + String(i);
		var value = String(getPopParent(name).value);

		if (value !== 'empty') {
			var name_id = 'nm_id' + String(i);
			var nameDiv = getPopParent(name_id);
			var nameVal = String(nameDiv.innerHTML);
			r_list.push(nameVal);
		}
	}

	var left_length = r_list.length;
	var fill_right = false;

	if (left_length > 6) {
		left_length = 6;
		fill_right = true;
	}

	for (var j = 0; j < left_length; j++) {
		html_left += "<li>" + r_list[j] + "</li>"
	}

	if (fill_right === true) {
		for (var k = 6; k < r_list.length; k++) {
			html_right += "<li>" + r_list[k] + "</li>"
		}
	}

	mainDiv.innerHTML = html_left;
	mainDivRight.innerHTML = html_right;
}

function initialize_rm_application(rating, isCandidate) {
	isCandidate = String(isCandidate);
	rate_rm(rating);

	if (isCandidate === 'True') {
		grab('isCandidate').checked = true;
	}
	else {
		grab('isCandidate').checked = false;
	}
}

function complete_candidate_removal() {
	var r_list = [];

	for (var i = 1; i <= 12; i++) {
		var name = 're' + String(i);
		var value = String(getPopParent(name).value);

		if (value !== 'empty') {
			var div = grab(name);
			div.value = value;
		}
	}

	grab('r_form').submit();
}

function reload_rm_all() {
	window.parent.opener.location.reload();
	window.close();
}

function rate_applicant_return() {
	var form = grab('r_form');
	grab('save_this').value = 'rate_applicant';
	form.action = '/roommate_win/';
	form.submit();
}

function rm_home_buttons(next_page) {
	next_page = String(next_page);
	var form = grab('r_form');
	form.action = next_page;
	form.submit();
}





function add_asi_comments() {
	openPopUp('auto', '/new_comment/', 600, 400);
}

function fetch_asi_comment_title() {
	var page = String(getPopParent('save_section').value);
	var title = null;

	if (page === '/asi_medical/') {
		title = 'ASI: Medical Status Comments';
	}
	else if (page === '/asi_employment/') {
		title = 'ASI: Employment/Support Status Comments';
	}
	else if (page === '/asi_drug1/') {
		title = 'ASI: Drug/Alcohol Use Comments';
	}
	else if (page === '/asi_legal/') {
		title = 'ASI: Legal Status Comments';
	}
	else if (page === '/asi_social1/' || page === '/asi_social2/') {
		title = 'ASI: Family/Social Relationships Comments';
	}
	else if (page === '/asi_psych/') {
		title = 'ASI: Psychiatric Status Comments';
	}

	return title;
}

function initialize_asi_comment_popup() {
	grab('comment_title').innerHTML = fetch_asi_comment_title();
	grab('asi_comment').innerHTML = String(getPopParent('comments').value);
}

function save_asi_comment() {
	getPopParent('comments').value = grab('asi_comment').value;
	window.close();
}

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

	document.getElementById('g17').selectedIndex = json_data.g17;
	document.getElementById('g18').selectedIndex = json_data.g18;
	document.getElementById('g19').selectedIndex = json_data.g19;

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

function init_main_nav_exit() {
	grab('exit_to').value = getPopParent('exit_to').value;
}

function sessionChecking(btnType) {
	var actionApp = grab('tracking').value;
	actionApp = String(actionApp);
	btn = String(btnType);
	grab('exit_to').value = btn;

	if (actionApp === 'Session') {	
		var w = 500;
		var h = 500;
		openPopUp('auto', '/session_open_error/', w, h);
	}
	else {
		var form = grab('n_form_main');

		if (btn === 'home') {
			form.action = '/adminHome/';
		}
		else if (btn === 'bill') {
			form.action = '/billingMain/'
		}
		else if (btn === 'admin') {
			form.action = '/AdministrativeMain/'
		}
		else if (btn === 'appt') {
			form.action = '/appointmentMain/'
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
//----------------------------------------------------- UT FUNCTIONS --------------------------------------------------//
//*********************************************************************************************************************//
//#####################################################################################################################//

function ut_complete_options() {
	var w = 550, h = 400;
	openPopUp('auto', '/UT_complete/', w, h);
}

function end_ut_session() {
	getPopParent('ut_form').action = '/adminHome/';
	getPopParent('ut_form').submit();
	window.close();
}

function cont_during_ut() {
	getPopParent('ut_form').action = '/clientOptions/';
	getPopParent('ut_form').submit();
	window.close();
}

function finalize_ut() {
	var w = 1100, h = 1300;
	openPopUp('auto', '/printUT/', w, h);
}

function back_from_ut() {
	grab('ut_form').action = '/clientOptions/';
	grab('ut_form').submit();
}

function edit_ut() {
	grab('ut_form').action = '/ut_preliminary/';
	grab('ut_form').submit();
}

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

function eliminateWhiteSpaceText(val) {
	var result = '';
	var val = String(val);

	for (var i = 0; i < val.length; i++)
	{
		if (val.charAt(i) !== ' ') {
			result += val.charAt(i);
		}
	}

	return result;
}



function snagSavedDay(val) {
	var result = '';
	val = String(val);
	val = eliminateWhiteSpaceText(val);

	for (var i = 0; i < val.length; i++) {
		if (val.charAt(i) !== '@') {
			result += val.charAt(i);
		}
		else {
			break;
		}
	}
	return result;
}

function getSepIndexSave(val) {
	var index = 0;
	val = eliminateWhiteSpaceText(val);

	for (var i = 0; i < val.length; i ++) {
		if (val.charAt(i) === '-') {
			index = i + 1;
			break;
		}
	}
	return index;
}

function getAfterCharIndexSave(val) {
	var index = 0;
	val = eliminateWhiteSpaceText(val);

	for (var i = 0; i < val.length; i++) {
		if (val.charAt(i) === '@') {
			index = i + 1;
			break
		}
	}
	return index;
}

function snagSavedStart(val) {
	var result = '';
	val = eliminateWhiteSpaceText(val);
	var start = getAfterCharIndexSave(val);
	var end = getSepIndexSave(val) - 1;

	for (var i = start; i < end; i++) {
		result += val.charAt(i);
	}
	return result
}

function snagSavedEnd(val) {
	var result = '';
	val = eliminateWhiteSpaceText(val);
	var index = getSepIndexSave(val);

	for (var i = index; i < val.length; i++) {
		result += val.charAt(i);
	}

	return result
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
		postUniversalRadioSEL(trigger, field, target);
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

	if (form_type === 'am') {
		universal_am_dynamic_post(page);
	}
	else if (form_type === 'asi') {
		processAsiFields(page);
	}
	else if (form_type === 'ut') {
		continue_ut();
	}
	else if (form_type === 'mh') {
		postMhFields(page);
	}
	else if (form_type === 'sap') {
		postSapFields(page);
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
	var shouldDelete = grab('shouldDelete').value;
	shouldDelete = String(shouldDelete);
	
	if (shouldDelete === 'False') {
		grab('s_form').submit();
	}
	else {
		var f_id = getPopParent('form_name').value;
		f_id = String(f_id);
		var form = getPopParent(f_id);
		form.action = '/adminHome/';
		grab('s_form').action = '/sessionClosed/';
		grab('s_form').submit();
		form.submit();
	}
}

function generalSessionExitOptions() {
	var w = 500;
	openPopUp('auto', '/uni_exit_session/', w, w);
}

function chooseSessionExit(answer) {
	answer = String(answer);
	var nextUrl = grab('exit_to').value;
	nextUrl = String(nextUrl);

	if (answer === 'False') {
		grab('s_form').action = '/sessionClosedAlt/';
	}

	else {
		grab('s_form').action = '/sessionClosed/';
	}

	var f_id = getPopParent('form_name').value;
	f_id = String(f_id);

	var form = getPopParent(f_id);
	var multiNav = grab('multiNav').value;

	if (multiNav === 'True') {
		if (nextUrl === 'bill') {
			form.action = '/billingMain/';
		}
		else if (nextUrl === 'admin') {
			form.action = '/AdministrativeMain/';
		}
		else if (nextUrl === 'appt') {
			form.action = '/appointmentMain/';
		}
		else if (nextUrl === 'logout') {
			form.action = '/logout/';
		}
		else {
			form.action = '/adminHome/';
		}
	}
	else {
		form.action = '/adminHome/';
	}	

	grab('s_form').submit();
	form.submit();
}

function generic_exit_home() {
	var w = 500, h = 500;
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
	var form = grab('resolve_form');
	var location = grab('save_section');
	var c1 = grab('c1');
	var c2 = grab('c2');

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
	var form = grab('refresh_form');
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

function verified_form() {
	var w = 550, h = 400;
	openPopUp('auto', '/form_complete/', w, h);
}


function save_uni_form() {
	var form_type = getPopParent('exit_type').value;
	grab('exit_type').value = form_type;
	grab('s_form').submit();
}

function final_session_view() {
	grab('s_form').action = '/uni_exit_session/';
	grab('s_form').submit();
}

function go_to_print(fType) {
	var w = 1200, h = 1300;
	openPopUp('auto', '/print_form/', w, h);
	window.close();
}

function uni_continue_back_session() {
	var form = getPopParent('sap_form');
	var eType = getPopParent('exit_type').value;
	eType = String(eType);

	if (eType === 'sap') {
		form = getPopParent('sap_form');
	}
	else if (eType === 'asi') {
		form = getPopParent('asi_form');
	}

	else if (eType === 'am') {
		form = getPopParent('am_demo');
	}

	else if (eType === 'mh') {
		form = getPopParent('mh_form');
	}

	else if (eType === 'ut') {
		form = getPopParent('ut_form');
	}

	form.action = '/clientOptions/';
	form.submit();
	window.close();
}

































