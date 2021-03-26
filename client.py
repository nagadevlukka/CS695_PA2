# Import socket module 
import socket             
  
# Create a socket object 
s = socket.socket()         
  
# Define the port on which you want to connect 
port = 12354
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

for i in range(1,10):
  
		# message sent to server
	message = str(i)
	if i==5:
		message =str(10000000)
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
   
	  