
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route("/b")
def index():
    return render_template("main_page.html")

@app.route('/')
def hello_world():
    #return 'This is my new shiny Flask app'
    return render_template("main_page.html")
