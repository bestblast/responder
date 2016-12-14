# -*- coding: utf-8 -*-

from config import API_URL, API_LOGIN,API_PASS, CALLBACK_URL

try:
    import ssl
except ImportError:
    class _SslDummy(object):
        def __getattr__(self, name):
            raise RuntimeError('SSL support unavailable')
    ssl = _SslDummy()
import requests
from requests.auth import HTTPBasicAuth
from flask import Response
from flask import Flask, request,jsonify
app = Flask(__name__)

from google_get_url import *

def jsonData(subscriber,text_query):
    resp = '{\
   "phone_number": %s,\
   "callback_url": \"%s\",\
   "tag": "Campaign name",\
   "channels": [ "viber"],\
   "channel_options": {\
      "viber": {\
         "ttl": 900,\
         "img": \"%s\",\
         "ios_expirity_text": "Text for ios when message expires"\
      }\
   }\
}\
' % (subscriber, CALLBACK_URL, get_url_from_query(text_query))
    return resp

headers = {'Content-Type': 'application/json'}


@app.route('/', methods=['GET', 'POST'])
def hello_post():
    json = request.json
    print(json)
    return "Hello World!"

@app.route("/reply", methods=['GET','POST'])
def reply():
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)
    if request.json:
        mydata = request.json # will be 
        reply = mydata.get("text_from_subscriber")
        subscriber = mydata.get("phone").split("+")[1]
        text_query = reply
	print reply
        print subscriber
        r = requests.post(API_URL,headers=headers, auth=HTTPBasicAuth(API_LOGIN, API_PASS), data=jsonData(subscriber,reply))
        print jsonData(subscriber,text_query)
	print r.status_code
        print r.text
        return "Thanks. Your message is %s" % reply
    else:
        return "no json received"


@app.route("/json", methods=['GET','POST'])
def json():
    
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)
    
    if request.json:
        mydata = request.json # will be 
        
        return "Thanks. Your age is %s" % mydata.get("alpha_name")

    else:
        return "no json received"

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    jsonBody = request.get_json
    content = request.json
    print content
    print(content)
    return jsonify(content)

@app.route("/a")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="172.31.21.183", port=8880, debug=True)
#    app.run(host="172.31.21.183",debug=True, port=5000, ssl_context='adhoc')



# accepting: POST requests in this case
#@app.route('/', methods=['GET', 'POST'])
#def helloPOST():
#    name=request.form['yourname']
#    email=request.form['youremail']
#    return render_template('form_action.html', name=name, email=email)
#    return "Hello World!"
