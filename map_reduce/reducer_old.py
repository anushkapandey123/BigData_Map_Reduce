import sys

#query_word = sys.argv[1]
#total_count = 0

f = open('o1.txt', 'r')
readline=f.readlines()
myListofTuples = list()
for line in readline:
    myListofTuples.append(line.rstrip().split(','))

sorted_list=sorted(myListofTuples, key=lambda x: x[0])
print(sorted_list)


#sorted_list = [['a', 1], ['a', 1], ['b', 1]]

d = {}
f_red = open("/home/pes1ug20cs072/BD_Project/output.txt", 'a')

for i in sorted_list:
	if(i[0] not in list(d.keys())):
		d[i[0]] = 1
	else :
		d[i[0]] += 1

for i in d:
	s = i + "," + str(d.get(i)) + '\n'
	f_red.write(s)
		
	


		
		
