l# before running, set the FLASK_APP env var to the basename of this file $ENV:FLASK_APP="weight"
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        return render_template(
            'addweight.html',
            weight=request.form['weight'],
            date=datetime.now()
        )