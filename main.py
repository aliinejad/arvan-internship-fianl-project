import nginx
from flask import Flask, jsonify, request
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route("/")
def root():
    return 'Hello World!'


@app.route('/add',methods=['POST'])
def asgher():

	data=request.get_json()
	c = nginx.Conf()
	s = nginx.Server()

	s.add(
     		nginx.Key('listen', '12346'),
     		nginx.Comment('Yes, python-nginx can read/write comments!'),
     		nginx.Key('proxy_pass', '194.5.192.202:22'),
		#     nginx.Key('proxy_protocol', 'on'),
		#     nginx.Key('set_real_ip_from', '$proxy_protocol_addr')
 		)
	c.add(s)
	nginx.dumpf(c, '/etc/nginx/stream/mysite1.conf')
	


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')
