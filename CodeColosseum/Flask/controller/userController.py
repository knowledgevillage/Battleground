from app import app
from model.userModel import userModel
from flask import request, send_file
from datetime import datetime

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



@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def userPaginationController(limit, page):
    return obj.userPaginationModel(limit, page)


@app.route("/user/<uid>/upload/avtar", methods=["PUT"])
def userUploadAvtarController(uid):
    print(request.files)
    file=request.files['avtar']
    #file.save(f"/uploads/{file.filename}")
    print(str(datetime.now().timestamp()).replace(".",""))
    uniqueFileName=str(datetime.now().timestamp()).replace(".","")
    print(file)
    fileNameList=file.filename.split(".")
    print(fileNameList)
    fileExtention=fileNameList[-1]
    print(fileExtention)
    #file.save(f"/uploads/{file.filename}")
    finalFilePath=f"/GitRepo/Battleground/CodeColosseum/Flask/uploads/{uniqueFileName}.{fileExtention}"
    file.save(finalFilePath)
    return obj.userUploadAvtarModel(uid, finalFilePath)


@app.route("/upload/<filename>", methods=["GET"])
def userGetAvtarController(filename):
    return send_file(f"/GitRepo/Battleground/CodeColosseum/Flask/uploads/{filename}")