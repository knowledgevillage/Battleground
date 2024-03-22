from app import app
from model.userModel import userModel
from flask import request

obj = userModel()

@app.route("/user/getall")
def userGetAllController():
    return obj.userGetAllModel()


@app.route("/user/addone", methods=["POST"])
def userAddOneController():
    return obj.userAddOneModel(request.form)


@app.route("/user/update", methods=["PUT"])
def userUpdateController():
    return obj.userUpdateModel(request.form)


@app.route("/user/delete/<id>", methods=["DELETE"])
def userDeleteController(id):
    return obj.userDeleteModel(id)

@app.route("/user/patch/<id>", methods=["PATCH"])
def userPatchController(id):
    return obj.userPatchModel(request.form,id)