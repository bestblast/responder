from config import API_PASS
from config import API_URL
from config import API_LOGIN, CALLBACK_URL, PHONE_NUMBER

print API_LOGIN + API_PASS + API_URL

try:
    import ssl
except ImportError:
    class _SslDummy(object):
        def __getattr__(self, name):
            raise RuntimeError('SSL support unavailable')
    ssl = _SslDummy()
import requests
from requests.auth import HTTPBasicAuth

from flask import Flask, request,jsonify
app = Flask(__name__)

jsonData = ('{\n'
            '   "phone_number": {},\n'
            '   "callback_url": {},\n'
            '   "tag": "Campaign name",\n'
            '   "channels": [ "viber"],\n'
            '   "channel_options": {\n'
            '      "viber": {\n'
            '         "ttl": 900,\n'
            '         "img": "http://combiboilersleeds.com/images/picture/picture-0.jpg",\n'
            '         "ios_expirity_text": "Text for ios when message expires"\n'
            '      }\n'
            '   }\n'
            '}\n'
).format(PHONE_NUMBER,CALLBACK_URL)

headers = {'Content-Type': 'application/json'}


@app.route('/', methods=['GET', 'POST'])
def hello_post():
    return "Hello World!"

@app.route("/reply", methods=['GET','POST'])
def reply():

    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if request.json:
        mydata = request.json # will be 
        reply = mydata.get("text_from_subscriber")
        print reply
        r = requests.post(API_URL,headers=headers, auth=HTTPBasicAuth(API_LOGIN, API_PASS), data=jsonData)
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
    app.run(host="172.31.21.183", debug=True)
#    app.run(host="172.31.21.183",debug=True, port=5000, ssl_context='adhoc')



# accepting: POST requests in this case
#@app.route('/', methods=['GET', 'POST'])
#def helloPOST():
#    name=request.form['yourname']
#    email=request.form['youremail']
#    return render_template('form_action.html', name=name, email=email)
#    return "Hello World!"
