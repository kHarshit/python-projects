# python program to get IP address

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Your computer name is: ", hostname)
print("Your computer's IP address is: ", IP)
