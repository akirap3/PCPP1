import sys, requests, json

def get_via_requests(address):
	reply = requests.get(address)
	return reply

if len(sys.argv) != 2:
    print("- http server's address(requred)\n- port number (default to 80 if not specified)")
    sys.exit(1)
else:
	address = sys.argv[1]
	try:		
		r = get_via_requests(address)
		headers_json = json.dumps(dict(r.headers))
		headers_dict = json.loads(headers_json)
		
		for (k, v) in zip(headers_dict.keys(), headers_dict.values()):
			print(f'{k}'.ljust(20)+f'{v}')

	except requests.exceptions.InvalidURL:
		print('Recipient unknown!')
	except requests.exceptions.ConnectionError:
		print('Nobody\'s home, sorry!')
	except requests.exceptions.Timeout:
		print('Timeout!!')
	except requests.RequestException:
		print("Communitation error")