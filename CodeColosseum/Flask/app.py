from flask import Flask
app =Flask(__name__)

from controller import userController, productController  # always import after defining and initiating app aas flask firt of all serches for app



@app.route("/")
def welcome():
    return "This is my Flask Playground"


@app.route("/home")
def home():
    return "this is homeland of flask playground"

