from app import app

@app.route("/pcat/addnew")
def pcat_addnew():
    return "This battelfiled is to add new product category"