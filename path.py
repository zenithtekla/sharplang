__author__ = 'Zenith'
from flask import Flask, url_for, request, render_template
from sharplang import app
from flask import SQLAlchemy

# server/question
# server: /
@app.route('/')
def hello_world():
    inputLink = '<a href=' + url_for('input') + '>Input a word</a>'
    lookupLink = '<a href=' + url_for('lookup') + '>Look up</a>'
    return '''  <html>
                    <head>
                        <title>SharpLangs</title>
                    </head>
                    <body>
                        <h1>SharpLangs WebApp</h1>
                        ''' + inputLink + '      ' + lookupLink + '''
                    </body>
                </html>'''

# /input
@app.route('/input')
def input():
    if request.method == 'GET':
        # send user the form
        return render_template('input.html')
    elif request.method == 'POST':
        # read form data and save it
        userId = request.form['userId']
        aWord = request.form['aWord']
        inLang = request.form['inLang']
        wordForm = request.form['wordForm']
        wordMeaning = request.form['wordMeaning']
        wordSample = request.form['wordSample']

        # Store data in database
        # todotodo
        return render_template('preview.html', aWord = aWord)
    else:
        return '<h2>Invalid request</h2>'

# /input
@app.route('/lookup')
def lookup():
    if request.method == 'GET':
        # send user a form
        return render_template('lookup.html')
    elif request.method == 'POST':
        # read form data and save it
        aWord = request.form['aWord']
        inLang = request.form['inLang']

        # Relate to database and find the word
        # todotodo !!
        return render_template('matrix.html', aWord = aWord)

    else:
        return '<h2>Invalid request</h2>'

# /<word>
'''@app.route('/<word>')
def translate(word):

        aWord = 'a WORD'
        # Read word from database
        return render_template()
    return 'Spreedsheet for <b>' + word + '</b> as follow'''