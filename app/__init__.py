from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/results')
def form():
    return render_template('results.html')

