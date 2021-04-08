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
        return render_template('founders.html', founderFact = get_founder_facts(request.args["year"]))
    else:
        return render_template('founders.html')
   

#def get_year_options():
#    ListOfYears= [1996, 2001, 2014]
#    options = ""
#    for year in listOfYears:
 #       options = options + Markup("<option value=\"" + year + "\">" + year + "</option>")
#    return options
    
def get_founder_facts(year):
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    
    founder_pop = 0
    founder_pop2 = 0
    
    for founder in billionaires:
        if founder["year"] == int(year) and founder["wealth"]["how"]["was founder"] == True:
            founder_pop = founder_pop + 1
    fun_fact = "The number of billionares who were founders in " + year + " was " + str(founder_pop)
    
    for founder in billionaires:
        
        if founder["year"] == int(year) and founder["wealth"]["how"]["was founder"] == True and founder["company"]["sector"]== "retail":
            founder_pop2 = founder_pop2 + 1
    fun_fact2= "The number of billionares who were founders of a retail store in " + year + " was " + str(founder_pop2)
    
    return fun_fact
    
    

    




if __name__=="__main__":
    app.run(debug=False, port=54321)
