import os
import time

os.system("virsh domstats vm1 --cpu-total > output1.txt")
time.sleep(5)
os.system("virsh domstats vm1 --cpu-total > output2.txt")

with open('output1.txt','r') as f1:
	for lines in f1:
		#print(lines.split('='))
		if lines.split('=')[0]=="  cpu.time":
			a=int(lines.split('=')[1])
			break

with open('output2.txt','r') as f2:
	for lines in f2:
		#print(lines.split('='))
		if lines.split('=')[0]=="  cpu.time":
			b=int(lines.split('=')[1])
			break
print((b-a)/50000000)