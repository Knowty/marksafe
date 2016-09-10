var eventSource = require('eventsource'),
    settings    = require('./settings'),
    sqlite3     = require('sqlite3');

var db = new sqlite3.Database(settings.DATABASE.path);


var source = new eventSource(settings.KONNECT.API_URL + settings.KONNECT.API_KEY + '/konnect');

source.addEventListener('open', function (event) {
    console.log('Opened' + JSON.stringify(event));
});

source.addEventListener('message', function(event) {
    console.log('Got an event = ' + event.data);

    var data = JSON.parse(event.data);

    if (data.type == 'CDR') {
        db.serialize(function() {
            console.log('Inside serialize');

            if (data.dispnumber == settings.HACKATHON.sr_number) {

                if (data.business_call_type == 'Voicemail') {
                    // 2nd Option was selected, User is not safe.
                    console.log('Its a phone.');
                    query = `UPDATE victim_victim SET safety_level = 3 where phone_number = "${data.caller_id}"`;
                    console.log(query);
                    db.run(query);

                    new_query = `SELECT phone_number FROM victim_victim WHERE phone_number = "${data.caller_id}"`;
                    db.each(new_query, function(err, row) {
                        text = `${row.name} has been marked as needs help!!`;
                        sendSms(row.notification_contact_number, text)
                    });
                }

                if (data.business_call_type == 'DTMF') {
                    // User did not answer the call
                    console.log('Its a dtmf.');
                    query = `UPDATE victim_victim SET safety_level = 2 where phone_number = "${data.caller_id}"`;
                    console.log(query);
                    db.run(query);
                }

                if (data.business_call_type == 'Sound') {
                    // User marked itself as safe.
                    console.log('Its a sound.');
                    query = `UPDATE victim_victim SET safety_level = 0 where phone_number = "${data.caller_id}"`;
                    console.log(query);
                    db.run(query);

                    new_query = `SELECT phone_number FROM victim_victim WHERE phone_number = "${data.caller_id}"`;
                    db.each(new_query, function(err, row) {
                        text = `${row.name} has been marked safe!!`;
                        sendSms(row.notification_contact_number, text)
                    });

                }
            }
        });
        console.log('Got a CDR = ' + JSON.stringify(data));
    }
});



function sendSms(number, text) {
	url = settings.SMS.API_URL + `?mobile_number=${number}&message=${text}&sms_type=t`

	console.log("Sending SMS using URL = " + url);
	http.get(url, function(response) {
			console.log('SMS API result = ' + response);
	});
}