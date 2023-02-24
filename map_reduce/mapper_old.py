import sys

def foo(file_name):
	f = open(file_name, 'r')
	f1 = open('inter_file.txt', 'w')
	for line in f:
		words = line.lower().strip().split()
		for word in words:
			print(f"{word},1")
			f1.write(f"{word},1")
			f1.write('\n')
	
			
			
			
my_input = sys.argv
file_name = my_input[1]
foo(file_name)


