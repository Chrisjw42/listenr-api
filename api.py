#!/usr/bin/python

import os
import random
import json
import subprocess
import time
from datetime import timedelta
from functools import update_wrapper, wraps

from flask import make_response, request, current_app, Flask, url_for, jsonify, Response
import tokens
from flask import jsonify

app = Flask(__name__)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, (str, bytes)):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, (str, bytes)):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

def CheckAuth(username, password):
    return (username == "listenr" and password=="test")

def Authenticate():
    message = {"message":"Please provide authentication information, a username and password"}
    response = jsonify(message)

    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'

    return response

def RequiresAuth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        print(auth)
        print(request)
        if not auth or not CheckAuth(auth.username, auth.password):
            return Authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route("/", methods=["GET", "POST"]) # Adds the "/" rule
def ApiRoot(): # Links the rule to this function
    
    return "hello"
    # return jsonify({"message": "You bloody gronk.\n"}) # This is what the funciton does

# @app.route("/test", methods = ["GET"]) # Adds the rule
# @RequiresAuth
# def ApiTest(): # Links the rule to this function
#     returnStr = "This is a test\n"

#     if "name" in request.args:
#         returnStr = returnStr + request.args["name"] + "\n"

#     return returnStr

# # Method for receiving images
# @app.route("/ObjectDetection", methods = ["POST"]) # Adds the rule
# @RequiresAuth
# def ApiImaggPost(): # Links the rule to this function
    
#     jsonPostData = json.loads(request.data)

#     print("The passed email was: " + jsonPostData["email"])
#     email = jsonPostData["email"]
#     image = jsonPostData["image"]

#     if email == "" or email == None:
#         return "FAIL - Please include email for results publishing\n"
#     elif image == "" or image == None:
#         return "FAIL - Please include image (base 64 encoding) for analysis\n"

#     iD = random.randint(1000000000000000000000000000000,9999999999999999999999999999999)

#     print("Passed email: {} - /it is impled that the image has been passed if an email appears <-".format(email))

#     imageHandling.DecodeJPEG(image, iD)

#     """
#     # Ensure the joblist exists
#     if not os.path.exists("/home/chris/YOLO9000"):
#         os.system("mkdir /home/chris/YOLO9000")
#     if not os.path.isfile("/home/chris/YOLO9000/joblist.txt"):
#         os.system("> /home/chris/YOLO9000/joblist.txt")

#     with open("/home/chris/YOLO9000/joblist.txt", "a+") as joblist:
#         joblist.write("{},{},{},{}\n".format(iD, email, False, image))

#     """

#     ProcessImage(iD)
#     time.sleep(2)
#     return ReadResults(iD) 

# @app.route("/dir") # Adds the "/" rule
# @RequiresAuth
# def ApiGetCWD(): # Links the rule to this function
#     return os.getcwd() + "\n" # This is what the funciton does


# @app.route("/hackathon", methods = ["GET", "OPTIONS"]) # Adds the rule
# @crossdomain(origin="*")
# def ApiHackathonTest():
#     if "product" in request.args:

#         result = hack.SearchDB(request.args["product"])
#         if result == "[]":
#             result = "No results! Please try another query!"
#         return str(result)
    
#     return "Please enter a search query!"

# @app.route("/hackathonCoords", methods = ["GET", "OPTIONS"]) # Adds the rule
# @crossdomain(origin="*")
# def ApiHackathonCoords():

#     if "lat" in request.args and "lng" in request.args:

#         result = hack.allnearestshop(request.args["lat"],request.args["lng"])
#         return str(result)
    
#     return "Please enter a search query!"

# """
# Take a saved image filename and pass it to the bash script
# """
# def ProcessImage(iD):
#     print("PY: calling subprocess")
#     subprocess.check_call(["bash", "/home/chris/scripts/yoloProcess.sh", str(iD)])
#     print("PY: finished calling subprocess")


# def ReadResults(iD):
#     filePath = "/home/chris/YOLO9000/imageAnalysis/{}.txt".format(iD)
#     results = ""

#     print("Opening read file")
#     with open(filePath, "r") as file:
#         results = file.read()

#     print("PY: Results: " + results)

#     if len(results.split("\n")) > 1:
#         return str(results.split("\n")[1:])
#     else:
#         return "NO MATCHES. " + results

if __name__ == "__main__":
    #app.run()
    print()