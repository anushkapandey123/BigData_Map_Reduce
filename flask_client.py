import requests
import json
import sys

'''response = requests.post('http://localhost:3000/process',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps({'data': 2}))'''

response = requests.get('http://localhost:3000')
print(response)

#opening the file
#path = sys.argv[1]
file1 = open("file1.txt", "r")
print(file1)                        


#counting the number of lines
c=0
for count, line in enumerate(file1):
	c+=1
	#pass
	
print('Total Lines', c)
no_of_lines_for_each_worker = (c)/2


#converting to json and sending to the worker nodes
dict1 = {}
file1 = open("file1.txt", "r")
c=1
i=0
j=1
for count,line in enumerate(file1):
	if c == no_of_lines_for_each_worker+1:
		print(dict1)
		ch = str(j)
		response = requests.post('http://localhost:300' + ch +'/process',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(dict1))
		print("partition now")
		j+=1
		
		dict1= {}
		c=1
		i=0
	#else :
	description = line.strip('\n')
	dict1[i] = description
	print(type(dict1[i]))
	c+=1
	i+=1
	
print(dict1)
response = requests.post('http://localhost:3002/process',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(dict1))
			


#print(response.json())


