function updateSS() {
	var ss_num = document.getElementById('ss_num');
	// var fname = document.getElementById('fname');
	// var lname = document.getElementById('lname');
	// var dob = document.getElementById('dob');
	// var client_ID = document.getElementById('client_ID');

	ss_num.disabled = false;
	ss_num.value = "Got it!!!";
	// fname.disabled = true;
	// lname.disabled = true;
	// dob.disabled = true;
	// client_ID.disabled = true;
}

function updateName() {
	var ss_num = document.getElementById('ss_num');
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');

	ss_num.disabled = true;
	fname.disabled = false;
	lname.disabled = false;
	dob.disabled = true;
	client_ID.disabled = true;
}

function updateDOB() {
	var ss_num = document.getElementById('ss_num')
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');

	ss_num.disabled = true;
	fname.disabled = true;
	lname.disabled = true;
	dob.disabled = false;
	client_ID.disabled = true;
}

function updateID() {
	var ss_num = document.getElementById('ss_num')
	var fname = document.getElementById('fname');
	var lname = document.getElementById('lname');
	var dob = document.getElementById('dob');
	var client_ID = document.getElementById('client_ID');

	ss_num.disabled = true;
	fname.disabled = true;
	lname.disabled = true;
	dob.disabled = true;
	client_ID.disabled = false;
}

function submit_session() {
	document.getElementById('client-search').submit();
}










