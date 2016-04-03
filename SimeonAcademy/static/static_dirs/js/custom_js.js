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










