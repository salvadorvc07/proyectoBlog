from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("index.html", nombre="Salvador")

@app.route("/motos")
def motos():
	return render_template("moto.html", nombre="Salvador")

@app.route("/isc")
def isc():
	return render_template("isc.html", nombre="Salvador")
	
@app.route("/tatuajes")
def tatuajes():
	return render_template("tatuajes.html", nombre="Salvador")


if __name__== "__main__":
	app.run(debug=True)