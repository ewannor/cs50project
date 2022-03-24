import os
import urllib.parse
import time
import random

from cs50 import SQL
from flask import redirect, render_template, sessions
from functools import wraps


def apology( code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code,), code


def greeting():
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    if current_hour < 12:
        greet = 'morning'
    elif current_hour < 17:
        greet = 'afternoon'
    else:
        greet = 'evening'
    return greet


# Configure CS50 Library TO use SQLite database
db = SQL("sqlite:///dictionary.db")

def main():
    random_word()

def search(word):
    """ Use SQLite queries to find word in dictionary"""
    entries = db.execute('SELECT * FROM entries WHERE word = ?', word)
    return entries

def random_word():
    """Randomly selects word from database"""
    words = db.execute('SELECT word FROM entries GROUP BY word')
    #list_words
    random_number = random.randint(0, len(words))
    return words[random_number]['word']




if __name__ == "__main__":
    main()