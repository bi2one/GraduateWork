HOST = null;
PORT = 8124;
DB_NAME = 'hospital'
DB_USER = 'root'
DB_PASSWORD = 'dkdnsmrep2'

var fu = require("./libserver/fu"),
    qs = require("querystring"),
    url = require("url"),
    client = require('mysql').client,
    sys = require('sys');

client.user = DB_USER;
client.password = DB_PASSWORD;
client.connect();
client.query('USE ' + DB_NAME);

client.query('SELECT * FROM treatment_patient').addCallback(
	     function(results) {
		 for (var i = 0, l = results.ROWS.length; i < 1; i++) {
		     var result = results[i];
		     sys.write(result.id);
		 }
	     });

// var state = new function() {
//     var 
// }

// fu.listen(PORT, HOST);

// fu.get("/fetch_state", function(req, res) {
//     if (!qs.parse(url.parse(req.url).query).lastId) {
// 	res.simpleJSON(400, {
// 	    error: "Must supply lastId parameter"
// 	});
// 	return;
//     }

//     var lastId = parseInt(qs.parse(url.parse(req.url).query).lastId, 10);

    
// });