from flask import Flask, render_template

app = Flask(__name__) # register current .py file as the module/app name

@app.route('/')
def index():
    # entrypoint to our website
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    # this page will get routed to when index.html is done. This is our input page.
    return render_template("main.html")

@app.route('/results')
def results():
    # this will get routed to when we are ready to display results-
    return render_template("results.html")