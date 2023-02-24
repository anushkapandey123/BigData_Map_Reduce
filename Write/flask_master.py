from flask import Flask, jsonify
from flask import request, send_file, abort
from multiprocessing import Pool, TimeoutError

import time
import os
import multiprocessing


app = Flask(__name__)
port = 3000


@app.route('/download')
def downloadFile():
	try:
	    path = "log.txt"
	    return send_file(path, as_attachment=True)
	    
	except FileNotFoundError:
		abort(404)
		
		

@app.route('/', methods=["GET"])
def message():
	list = []
	list.append("3001")
	list.append("3002")
	return list
	
@app.route('/process', methods=["POST"])
#def process():
def process():
	content = request.json
	print(content)
	
	data1 = content['0']
	data2 = content['1']
	print(data1)
	print(data2)
	
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





	
