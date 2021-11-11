import os
from flask import Flask, flash, render_template, redirect, request
from tasks import add

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', "super-secret")


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/add', methods=['POST'])
def add_inputs():
    _type = int(request.form['type'])
    data = int(request.form['data'])
    add.delay({ "data": data, "type": _type })
    flash("Your addition job has been submitted.")
    return redirect('/')
