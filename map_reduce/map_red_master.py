from flask import Flask, jsonify
from flask import request, send_file, abort
from multiprocessing import Pool, TimeoutError
import requests
import json

import time
import os
import multiprocessing


app = Flask(__name__)
port = 3000


@app.route('/process_mapper', methods=["POST"])
#def process():
def process_mapper():
	content = request.json
	print(type(content))
	
	response = requests.post('http://localhost:3001/mapper',headers={'Content-Type': 'application/json'},
data=json.dumps(content))
	
	response = requests.post('http://localhost:3002/mapper',headers={'Content-Type': 'application/json'},
data=json.dumps(content))


	f1 = open("/home/pes1ug20cs072/BD_Project/final_log.txt", 'w')
	f1.write("Map Job Completed\n")
	f1.close()
	
                       
                         

	
	return jsonify(request.json)

@app.route('/process_reducer', methods=["POST"])
#def process():
def process_reducer():
	content = request.json
	
	response = requests.post('http://localhost:3001/reducer',headers={'Content-Type': 'application/json'},
data=json.dumps(content))

	response = requests.post('http://localhost:3002/reducer',headers={'Content-Type': 'application/json'},
data=json.dumps(content))
	
	
	f3 = open("/home/pes1ug20cs072/BD_Project/final_log.txt", 'a')
	f3.write("Reduce Job Completed")
	f3.close()
	
	return jsonify(request.json)



if __name__ == '__main__':
	app.run(port=port, debug=True)	


	


	

'''@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('./abc.py')
	return "<p>File received</p>"
'''





	
