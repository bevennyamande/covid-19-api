from flask import Flask,request,render_template
import json
from main import total,covid_info,t_active_detail
from india import india_covid as ic
from usa import usa_covid as uc
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
	return render_template("index.html")

@app.route("/india",methods=["POST"])
def india():
	if request.method == "POST":
		return json.dumps({"total":covid_info["india"],"states":ic})

@app.route("/usa",methods=["POST"])
def usa():
	if request.method == "POST":
		return json.dumps({"total":covid_info["usa"],"states":uc})

@app.route("/world",methods=["POST"])
def world():
	if request.method == "POST":
		return json.dumps({"total":covid_info,"total_active_detail":t_active_detail,"country":covid_info})


if __name__ == '__main__':
	app.run(debug=True)