import sys
import os
import requests
from flask import Flask, request, json, jsonify

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True


# Test if string can be converted to integer.
def is_integer(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

@app.route("/")
def challenge():
    return "LightFeather challenge"

@app.errorhandler(404)
def not_found_error(error):
    return "404 error"

'''
Retrieve a list of supervisors from:
   https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/
and return as json containing a list of supervisor strings formatted as:
    "{jurisdiction} - {lastName}, {firstName}"
Sort alphabetcally by juristiction, lastName and firstName
Numeric jurisdictions should not be included in the response
'''
@app.route("/api/supervisors", methods=['GET'])
def supervisors():
    try:
        # Print to show request
        print("supervisors post")

        # Retrieve supervisor data as json.
        r = requests.get(url = 'https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers')
        jdata = r.json()

        # Create list of supervisors tuples while filtering integer juristictions
        supervisors = [(super['jurisdiction'], super['lastName'], super['firstName']) 
                    for super in jdata if not is_integer(super['jurisdiction'])]
        
        # Sort
        sorted_supervisors = sorted(supervisors, key = lambda x: (x[0], x[2], x[1]))
        
        # Format
        formatted = ["{} - {}, {}".format(*super) for super in sorted_supervisors]
        
        # Return list as json.
        return jsonify(formatted)

    except Exception as ex:
        print("Error in API supervisors:", file=sys.stderr)
        print(ex, file=sys.stderr)
        return jsonify({"api" : "supervisors", "status" : 500}), 500

'''
Accepts input json formatted as in this example:
    {
        "firstName" : "Dwight",
        "lastName" : "Schrute",
        "email" : "dwight.schrute@dundermifflin.com",
        "phone" : "555-555-1234",
        "supervisor" : "Michael Scott"
    }
("email" and "phone" are optional) and prints to the console.
'''
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
        
        # Empty data string returned
        return jsonify({"api" : "submit", "status" : 200})

    except Exception as ex:
        print("Error in API submit:", file=sys.stderr)
        print(ex, file=sys.stderr)
        return jsonify({"api" : "submit", "status" : 500}), 500

if __name__ == "__main__":
    print (os.getcwd())
    app.run()