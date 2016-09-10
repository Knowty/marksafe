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

                if (data.business_call_type == 'Phone') {
                    // 2nd Option was selected, User is not safe.
                    console.log('Its a phone.');
                    query = `UPDATE victim_victim SET safety_level = 3 where phone_number = "${data.caller_id}"`;
                    console.log(query);
                    db.run(query);

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

                }
            }
        });
        console.log('Got a CDR = ' + JSON.stringify(data));
    }
});
