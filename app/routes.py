from app import app
from flask import render_template, request, redirect, url_for
@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/form')
def form():
    return render_template('form.html')