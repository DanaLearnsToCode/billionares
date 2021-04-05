from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/founder")
def render_founder():
    return render_template('founders.html')


def get_age_options():
    listOfAges = ["1996", "2001", "2014"]
    options = listOfAges
    return options
    




if __name__=="__main__":
    app.run(debug=False, port=54321)
