from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/founder")
def render_founder():
    if "year" in request.args:
        return render_template('founders.html', founderFact = get_founder_facts())
    else:
        return render_template('founders.html')
   

#def get_year_options():
#    ListOfYears= [1996, 2001, 2014]
#    options = ""
#    for year in listOfYears:
 #       options = options + Markup("<option value=\"" + year + "\">" + year + "</option>")
#    return options
    
def get_founder_facts():
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    founder_pop = 0
    
    for founder in billionaires:
        if founder["year"] == year and founder["wealth"]["was founder"]== 'true':
            founder_pop = founder_pop + 1
    fun_fact = "The number of billionares who were also founders in" + year + "was" + str(founder_pop)
    return fun_fact
    
    

    




if __name__=="__main__":
    app.run(debug=False, port=54321)
