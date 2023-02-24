import requests
import json
import sys

'''response = requests.post('http://localhost:3000/process',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps({'data': 2}))'''


#map file
map_file = sys.argv[1]
f = open(map_file, 'r')
dict1 = {}
i=0
#reading the mapper file
for line in f:
	dict1[i] = line
	i=i+1
f.close()
	
#reducer file and reducing file
red_file = sys.argv[2]
f = open(red_file, 'r')
i=0
dict2 = {}
for line in f:
	dict2[i] = line
	i=i+1
f.close()
	


#input file
dict1[i] = sys.argv[3]
print(dict[i])	
response = requests.post('http://localhost:3000/process_mapper',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(dict1))


response = requests.post('http://localhost:3000/process_reducer',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(dict2))
                         
        	



#print(response.json())


