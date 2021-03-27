# Import socket module 
import socket             
import os
# Create a socket object 
s = socket.socket()         
  
# Define the port on which you want to connect 
port = 12354
  
# connect to the server on local computer 
s.connect(('192.168.122.154', port)) 

for i in range(100000):
  
		# message sent to server
	message='9791'
	s.send(message.encode('ascii'))
  
	# messaga received from server
	data = s.recv(1024)
  
		# print the received message
		# here it would be a reverse of sent message
	#print('Received from the server :',str(data.decode('ascii')))
    
		# ask the client whether he wants to continue
	# ans = input('\nDo you want to continue(y/n) :')
	# if ans == 'y':
	# 	continue
	# else:
	# 	break
	# close the connection
s.close()
   
	  