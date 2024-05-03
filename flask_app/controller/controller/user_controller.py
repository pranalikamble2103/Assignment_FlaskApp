from model.user_model import userModel
from flask import request
from app import app


user_obj = userModel()

@app.route("/user/getall")
def user_getall_controller():
    return user_obj.user_getall_model()

@app.route("/user/add", methods=["POST"])
def user_add_controller():
    return user_obj.user_add_model(request.form)
    
@app.route("/user/insert", methods=["POST"])
def user_insert_controller():
    return user_obj.user_insert_model(request.form)