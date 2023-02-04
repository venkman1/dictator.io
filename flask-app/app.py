from flask import Flask, render_template

app = Flask(__name__) # register current .py file as the module/app name

@app.route('/')
def hello():
    # entrypoint to our website
    return render_template("index.html")