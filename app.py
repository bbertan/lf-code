from flask import Flask, request, json, jsonify
app = Flask(__name__)
import sys
import os
import requests

def is_integer(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

@app.route("/")
def challenge():
    return "LightFeather challenge"


@app.route("/api/supervisors", methods=['GET'])
def supervisors():

    # jfile = open('response.json',)
    # jdata = json.load(jfile)

    print("supervisors post")

    r = requests.get(url = 'https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers')
    jdata = r.json()

    supervisors = [(super['jurisdiction'], super['lastName'], super['firstName']) 
                  for super in jdata if not is_integer(super['jurisdiction'])]
    
    sorted_supervisors = sorted(supervisors, key = lambda x: (x[0], x[2], x[1]))
    formatted = ["{} - {}, {}".format(*super) for super in sorted_supervisors]
    return(jsonify(formatted))

@app.route("/api/submit", methods=['POST'])
def submit():

    try:
        jdata = request.get_json()
        first = jdata["firstName"]
        print("First Name: {}".format(first), file=sys.stdout)
        last  = jdata["lastName"]
        print("Last Name: {}".format(last), file=sys.stdout)
        if "email" in jdata:
            email = jdata["email"]
            print("Email: {}".format(email), file=sys.stdout)
        if "phone" in jdata:
            phone = jdata["phone"]
            print("Phone number: {}".format(phone), file=sys.stdout)
        supervisor  = jdata["supervisor"]
        print("Supervisor: {}".format(supervisor), file=sys.stdout)
        return ""

    except Exception as ex:
        print(ex, file=sys.stderr)

if __name__ == "__main__":
    print (os.getcwd())
    app.run()