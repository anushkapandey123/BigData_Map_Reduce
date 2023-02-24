from flask import Flask, jsonify
from flask import request
from multiprocessing import Pool, TimeoutError
import subprocess

import time
import os
import multiprocessing


app = Flask(__name__)

	
@app.route('/process', methods=["POST"])
#def process():
def process():
	l = open("/home/pes1ug20cs072/BD_Project/log.txt", 'a')
	content = request.json
	print(content)
	
	f = open("names.txt", "w")
	l.write("/home/pes1ug20cs072/BD_Project/worker1/names.txt\n")
	for i in content:
		j = str(i)
		data = content[j]
		
		f.write(data)
		f.write('\n')
	f.close()
	print("successfully created the file")
	
	return jsonify(request.json)
	
@app.route('/mapper', methods=["POST"])
def mapper():
	content = request.json
	#print(type(content))
	
	f1 = open("mapper.py", "w")
	print("successfully created the file")
	i = 0
	
	for i in content:
		if i == len(content):
			break
		j = str(i)
		data = content[j]
		
		f1.write(data)
		f1.write('\n')
	
	f1.close()
	value = content[i]
	print(value)
	#print(value))
	subprocess.call(['python3', 'mapper.py', value])
	#p = subprocess.Popen(['python3', 'mapper.py', 'names1.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)	
	#print("p :", p)
	'''f.write(data1)
	f.write('\n')
	f.write(data2)
	f.close()'''
	
	
	return jsonify(request.json)
	
'''@app.route('/fxn')
def fxn():'''
	

@app.route('/reducer', methods=["POST"])
def reducer():
	content = request.json
	f1 = open("reducer.py", "w")
	print("successfully created the file")
	i=0
	
	for i in content:
		'''if i == len(content):
			break'''
		j = str(i)
		data = content[j]
		
		f1.write(data)
	f1.close()
	#value = content[i]
	subprocess.call(['python3', '/home/pes1ug20cs072/BD_Project/shuffle.py'])
	subprocess.call(['python3', 'reducer.py'])
	return jsonify(request.json)


if __name__ == '__main__':
	app.run(port=3001, debug=True)	


	


	

'''@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('./abc.py')
	return "<p>File received</p>"
'''





	


	


	

'''@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('./abc.py')
	return "<p>File received</p>"
'''





	
