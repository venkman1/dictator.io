import os
import openai


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # register current .py file as the module/app name

openai.api_key = os.getenv("OPENAI_API_KEY")

def not_found(e):
    return render_template("not_found.html")
def server_error(e):
    return render_template("server_error.html")


app.register_error_handler(404, not_found)
app.register_error_handler(500, server_error)

@app.route('/')
def index():
    # entrypoint to our website
    return render_template("index.html")

@app.route('/main', methods=['GET', 'POST'])
def welcome():
    # this page will get routed to when index.html is done. This is our input page.
    # here, we need to import our AI model and use some function that we define to generate
    # our speech analysis. The input to said function will be the speech file or input that
    # the user gives us on this main endpoint.
    if request.method == 'GET':
        return render_template("main.html")
    elif request.method == 'POST':
        speech = request.form['input']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(speech),
            temperature=0.6
        )

        return redirect(url_for("results", result = response.choices[0].text))



@app.route('/results')
def results():
    # this will get routed to when we are ready to display results-
    result = request.args.get("result")
    return render_template("results.html", result=result)

# below method was used to test how to get form data from an incoming http request
@app.route('/test', methods=['GET', 'POST'])
def test_form():
    # data = request.form['input']
    if request.method == 'GET':
        print("method was get")
        return render_template("test.html")
    else:
        # post method
        data = request.form['input']
        return ("you gave data: %s"%(data))
    

def generate_prompt(speech):
    return """Decide if a Speech's sentiment is dictatorial, neutral, or democratic.
Speech: {}
Sentiment:""".format(
        speech
    )