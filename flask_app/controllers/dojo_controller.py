from flask_app import app
from flask import render_template,redirect,request
# from flask_app.models.[name of class file] import [class name]
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# put your app.route logic here:

@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    dojos = Dojo.read_all_dojos()
    return render_template("dojos.html",dojos=dojos)

@app.route('/dojo/<int:id>')
def dojo(id):
    data = {
        "id":id
    }
    dojo = Dojo.read_dojo(data)
    return render_template("dojo.html",dojo=dojo)

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.read_all_dojos()
    return render_template("new_ninja.html",dojos=dojos)

@app.route('/add_ninja', methods=["POST"])
def add_ninja():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    return redirect("/dojos")

@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    data = {
        "name":request.form["dojo_name"]
    }
    Dojo.create_dojo(data)
    return redirect("/dojos")