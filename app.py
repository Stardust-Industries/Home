from flask import Flask, render_template, request
from markupsafe import escape
import sqlite3

app = Flask(__name__)

@app.route('/') # Home page
def index():
    return render_template(
        'index.html'
    )

@app.route('/Contact') # Contact Page
def contact(): 
    return render_template(
        'contact.html'
    )

# Request Page
@app.route('/Request')
def request():
    return render_template(
        'request.html'
    )

@app.route('/Request', methods=["POST"])
def request_something():

    contact_info = request.form.get("contact")
    information = request.form.get("information")

    return render_template(
        'request.html',
        contact_info=contact_info,
        information=information
    )

app.run(host='0.0.0.0', port=8080, debug=True)