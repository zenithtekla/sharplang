__author__ = 'Zenith'
import random
import sys
import os
from flask import Flask, url_for, request, render_template, redirect
from sharplang import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sharplang.db'
db = SQLAlchemy(app)


class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text, unique=False)
    meanEnglish = db.Column(db.Text, unique=False)
    inLang = db.Column(db.Text, unique=False)
    form = db.Column(db.Text, unique=False)
    meaning = db.Column(db.Text, unique=False)
    postdate = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean)

    def __init__(self, word, meanEnglish, inLang, form, meaning, postdate=None):
        # def __init__(self, word,meanEnglish,inLang,form,meaning):
        self.word = word.lower()
        self.meanEnglish = meanEnglish.lower()
        self.inLang = inLang.lower()
        self.form = form.lower()
        self.meaning = meaning.lower()
        if postdate is None:
            postdate = datetime.utcnow()
        self.postdate = postdate
        self.is_completed = 0


'''@app.route('/', methods=['GET', 'POST'])
def hello_world():
    qr = Lang.query.all()
    return render_template("index.html", qr=qr)
'''

# server: /
@app.route('/')
def hello_world():
    inputLink = '<a href=' + url_for('input') + '>Input a word</a>'
    lookupLink = '<a href=' + url_for('lookup') + '>Look up</a>'
    return '''  <html>
                    <head>
                        <title>SharpLangs</title>
                        <link rel="stylesheet" href="../static/css/styles.css" type="text/css"/>
                    </head>
                    <body>
                        <h1>SharpLangs WebApp</h1>
                        ''' '<div class="vasemma">' + inputLink + '</div>&nbsp;&nbsp;<div class="vasemma">' + lookupLink + '</div>' '''
                    </body>
                </html>'''


# /add
@app.route('/add', methods=['POST'])
def add():
    word = request.form['word'].lower()
    inLang = request.form['inLang'].lower()
    qr = Lang.query.filter_by(word=word, inLang=inLang).first()
    # qr=Lang.query.filter_by(word=word).first()
    #    if qr is None or Lang.query.filter_by(inLang=inLang).first() is None:
    if qr is None:
        db.session.add(Lang(word,
                            meanEnglish=request.form['meanEnglish'],
                            inLang=request.form['inLang'],
                            form=request.form['form'],
                            meaning=request.form['meaning']))
        db.session.commit()
        return redirect('/')
    else:
        return render_template("existing.html", qr=qr)


# /add
@app.route('/filter', methods=['POST'])
def filter():
    word = request.form['word'].lower()
    qr = Lang.query.filter_by(word=word).first_or_404()
    qrs = Lang.query.filter_by(meanEnglish=qr.meanEnglish).all()
    ct = Lang.query.filter_by(meanEnglish=qr.meanEnglish).count()
    return render_template("matrix.html", qrs=qrs, ct=ct)


# /input
@app.route('/input')
def input():
    if request.method == 'GET':
        # send user the form
        return render_template('input.html')
    else:
        return '<h2>Invalid request</h2>'


# /lookup
@app.route('/lookup')
def lookup():
    if request.method == 'GET':
        # send user a form
        return render_template('lookup.html')
    else:
        return '<h2>Invalid request</h2>'


'''old code

#  /input
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
        # todotodo ! trying to figure these parts
        return render_template('preview.html', aWord = aWord)
    else:
        return '<h2>Invalid request</h2>'

# /lookup
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
@app.route('/<word>')
def translate(word):

        aWord = 'a WORD'
        # Read word from database
        return render_template()
    return 'Spreedsheet for <b>' + word + '</b> as follow

old code    '''