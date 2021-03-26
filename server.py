import socket             
from _thread import *
import threading

def isprime(num):

	s =""
	if num > 1:
	 
	    # Iterate from 2 to n / 2
	    for i in range(2, int(num/2)+1):
	 
	        # If num is divisible by any number between
	        # 2 and n / 2, it is not prime
	        if (num % i) == 0:
	            s="no"
	            break
	    else:
	        s="yes"
	 
	else:
	    s="no"
	return s

def threaded(c):
	while True:
  
		# data received from client
		data = c.recv(1024).decode('ascii')
		if not data:
			print('Bye')
			break
  
		# reverse the given string from client
		a = isprime(int(data))
		print(a)
		# send back reversed string to client
		c.send(str(a).encode('ascii'))
  
	# connection closed
	c.close()
# next create a socket object 
s = socket.socket()         
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12354
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
  
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
  
# Establish connection with client. 
	c, addr = s.accept()     
	print ('Got connection from', addr )
	msg = 'Thank you for connecting'
	start_new_thread(threaded, (c,))
	
s.close()