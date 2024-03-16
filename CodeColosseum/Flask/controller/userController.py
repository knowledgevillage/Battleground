from app import app
from model.userModel import userModel

obj = userModel()

@app.route("/user/signup")
def userSignupController():
    return obj.userSignupModel()