import sys
import socket

def get_via_socket(address, port=80):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		if port not in range(1,65536):
			raise ConnectionRefusedError
		sock.connect((address, port))
		sock.send(b"HEAD / HTTP/1.1\r\nHost: " + bytes(address, "utf8") + b"\r\nConnection: close\r\n\r\n")
		sock.settimeout(1)
		receive = sock.recv(1000)
		recv_string = receive.decode()
		new_string = recv_string.splitlines()
		print(new_string[0])
		sock.shutdown(socket.SHUT_RDWR)
		sock.close()
	except ConnectionRefusedError:
		print("Port number is invalid - exiting")
		sys.exit(2)
	except socket.timeout:
		print("timeout")
		sys.exit(3)
	except:
		print("Due to other reasons!")
		sys.exit(4)

if len(sys.argv) not in [2,3]:
    print("- http server's address(requred)\n- port number (default to 80 if not specified)")
    sys.exit(1)

elif len(sys.argv) == 3:
	try:
		address, port = sys.argv[1], int(sys.argv[2])
		get_via_socket(address, port)
	except ValueError:
		print("Port number is invalid - exiting")
		sys.exit(2)

else:
	address = sys.argv[1]
	get_via_socket(address)
    
    
    
    
    
    
    
    
    
    
    