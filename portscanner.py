import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	# Translate hostname to IPv4
	target = socket.gethostbyname(sys.argv[1])
else: 
	print("Invalid amount of argument")
	
# Add banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
	# Scan ports between 1 and 65,535
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port " + port + " is open")
		s.close()
	
except KeyboardInterrupt:
	print("\n Exiting program!")
	sys.exit()
except socket.gaierror:
	print("\n Hostname could not be resolved!")
	sys.exit()
except socket.error:
	print("\n Server not responding!")
	sys.exit()
