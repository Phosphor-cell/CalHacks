from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='template')

from app import routes

if __name__ == '__main__':
    app.run(debug=True)

