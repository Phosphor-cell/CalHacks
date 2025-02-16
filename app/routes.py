from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

questions = ['What are your main concerns regarding living in Canada?', # pick from Financial, Living, Employment, stuff like that (multiple choice)
             
             # provide resources for immigrant services (along with specific support in later questions)
             'Have you had access to services who are offering support to immigrants (e.g. english classes, support for financial, employment, or living needs)? If so, how helpful have they been?', 

             # provide resources for application for citizenship
             'Do you plan on being a Canadian Citizen? If so, have you applied for, or are eligible for Canadian Citizenship yet?', 

             # provide resources for employment
             'What is your current employment status?', 
             'Have you applied, or own a Work Permit?',

             # provide resources for finance  
             'Do you have access to financial services such as a bank?', 

             # provide resources for language
             'How fluent are you in English or French, even if it is not your first language?', 
             'Are you currently enrolled in a language class right now? If so how helpful have they been for you?',

             # provide resources for living needs
             'What kind of housing unit do you live in right now (e.g. apartment, house, etc.)?',
             'Do you feel safe with your current living conditions?',
             'How affordable are you finding your current housing situation?',
             'Do you have good access to healthcare services?', 
             'Have you applied for any form of insurance?'
             ]

@app.route('/form')
def form():
    return render_template('form.html')

def read_form():
    data = request.form
    return {
        ''
    }