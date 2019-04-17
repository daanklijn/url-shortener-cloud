from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import abort
from json import dumps
import random 
import string 

app = Flask(__name__)

urls = {}

def get_random_id():
	chars=string.ascii_uppercase + string.digits
	return ''.join(random.choice(chars) for x in range(8))

@app.route('/', methods=['GET'])
def get_urls():
	# return dumps(urls)
	return	render_template("index.html",urls=urls) 

@app.route('/json', methods=['GET'])
def get_json():
	return dumps(urls)

@app.route('/', methods=['POST'])
def add_url():
	index = get_random_id()
	while index in urls:
		index = get_random_id()
	try:
		url = request.args.get("url")
		urls[index]=url
	except:
		return "Failed"
	return index

@app.route('/<url_id>', methods=['GET'])
def redirect_url(url_id):
	if(url_id in urls ):
		url = urls[url_id]
		return redirect(url)
	abort(404)


@app.route('/<url_id>', methods=['DELETE'])
def delete_url(url_id):
	try:
		del urls[url_id]
	except:
		return "Failed"
	return "succes"

@app.route('/<url_id>', methods=['PUT'])
def update_url(url_id):
	try:
		url = request.args.get('url')
		urls[url_id]=url
	except:
		return "Failed"
	return "succes"
	
@app.route('/', methods=['DELETE'])
def delete_all():
	urls.clear()
	return "succes"