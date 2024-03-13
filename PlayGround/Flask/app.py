from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcom():
    return "Welcome to Flask Playground"


@app.route("/home")
def display():
    return "Welcome to the homeland of Flask Playground"

#import controller.user_controller as user_controller  # importing user controller page in after initiating the app variable since that is defined in line app = Flask(__name__) hence importing it below

#import controller.product_controller as product_controller


# above multiple lines can be written as 

from controller import user_controller, product_controller