from app import app
from flask import render_template, request, redirect, url_for
@app.route('/')
@app.route('/index')
def index():
    return 'hello world'
questions = ['question: ', 'question: ', 'question: ', 'question: ', 'question: ']

@app.route('/form')
def form():
    return render_template('form.html')

def read_form():
    data = request.form
    return {
        ''
    }