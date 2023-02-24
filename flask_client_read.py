import requests

log_file = open("log.txt", 'r')
print(log_file)

new_file = open("final.txt", 'w')

# Reading the log file
for line in log_file:
	#print(line)
	line = line[0 : len(line)-1]
	intermediate_file = open(line, 'r')
	for sub_line in intermediate_file:
		new_file.write(sub_line)
		
	
	
log_file.close()
