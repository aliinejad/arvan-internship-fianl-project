import nginx
import os
from flask import Flask, jsonify, request
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route("/")
def root():
    return 'Hello World!'


@app.route('/add',methods=['POST'])
def add():

	data=request.get_json()
	input_port = data['input_port']
	upstream = data['upstream']+ ":" + data['upstream_port']
	path = "/config/" + input_port + ".conf"
	
	c = nginx.Conf()
	s = nginx.Server()

	s.add(
     		nginx.Key('listen', input_port),
     		nginx.Key('proxy_pass', upstream ),
		nginx.Key('proxy_protocol', 'on'),
 		)
	c.add(s)
	nginx.dumpf(c, path )
	return "Done!"
	


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')
