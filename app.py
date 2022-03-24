# Imports
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp


# Import helpers
import helpers

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = 0
    response.headers['Pragma'] = 'no-cache'
    return response

# Configure session to use filesystem (instead fo signed cookies)
app.config['SESSION_FILE_DIR'] = mkdtemp()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL('sqlite:///dictionary.db')

@app.route("/")
def index():
    """Generates index / home page"""

    try:
        greet = helpers.greeting()
        rand_word = helpers.random_word()

        return render_template('index.html', greeting=greet.upper(), random_word=rand_word)
        #return render_template('index.html', greeting=greet.upper())

    except:
        return helpers.apology()

@app.route("/entry")
def entry():
    try:
        """Generates entry/ dictionary definition page"""
        search_word = request.args.get("w")

        try:
            # If word is valid or found in dictionary
            entry = helpers.search(search_word)

            word = entry[0]['word']

            definitions = []
            for i in range(len(entry)):
                definitions.append(entry[i]['definition'])

            wordtype = entry[0]['wordtype']

            print(f"\n\n\nsearch word: {definitions}\n\n")

            return render_template('entry.html', name=word.lower(), definitions=definitions, wordtype=wordtype)

        except:
            # Search word not found
            return render_template('notfound.html', word=search_word)

    except:
        return helpers.apology()

@app.route("/more")
def more():
    try:
        return render_template('more.html')
    except:
        return helpers.apology()