import json

try:
	import websocket
except ImportError:
	raise SystemExit('missing websocket-client')

ws = websocket.WebSocket()
ws.connect('wss://ris-live.ripe.net/v1/ws/?client=bgpexample')

params = {
	'moreSpecific': True,
	'host': 'rrc21',
	'socketOptions': {
		'includeRaw': True
	}
}

ws.send(json.dumps({
		'type': 'ris_subscribe',
		'data': params
}))

for data in ws:
	parsed = json.loads(data)
	print(parsed['type'], parsed['data'])
