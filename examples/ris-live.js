/*
Subscribe to a RIS Live stream and output every message to the javascript console.

The exact same code will work in Node.js after running 'npm install ws' and including the following line:

const WebSocket = require('ws');
*/
var ws = new WebSocket("wss://ris-live.ripe.net/v1/ws/?client=js-example-1");
var params = {
    moreSpecific: true,
    host: "rrc21",
    socketOptions: {
        includeRaw: true
    } 
};
ws.onmessage = function(event) {
    var message = JSON.parse(event.data);
    console.log(message.type, message.data);
};
ws.onopen = function() {
    ws.send(JSON.stringify({
        type: "ris_subscribe",
        data: params
    }));
};
