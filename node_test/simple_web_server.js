var http = require("http");
     
http.createServer(function(req, res) {
    res.writeHead(200, {"Content-Type": "text/plain"});
    res.write("Hel");
    res.write("lo\r\n");
     
    setTimeout(function() {
        res.write("World\r\n");
        res.end();
    }, 2000);
}).listen(8124);