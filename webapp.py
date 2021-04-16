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
        return render_template('founders.html', founderFact = get_founder_facts(request.args["year"]), founderFact2 = get_founder_facts2(request.args["year"]))
    else:
        return render_template('founders.html', ageFact = get_age_facts())
    
@app.route("/graph")
def render_graph():
    return render_template('graph.html')

@app.route("/country")
def render_country():
    if "country" in request.args:
        return render_template('country.html', options = get_country_options(), countryFact=get_country_fact(request.args["country"]))
    else:
        return render_template('country.html', options = get_country_options())
    
@app.route("/page4")
def render_page4():
    if "country" in request.args:
        return render_template('page4.html', options2 = get_country_options2(), countryFact2=get_country_fact2(request.args["country"]))
    else:
        return render_template('page4.html', options2 = get_country_options2())
   


def get_founder_facts(year):
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    
    founder_pop = 0
    
    for founder in billionaires:
        if founder["year"] == int(year) and founder["wealth"]["how"]["was founder"] == True:
            founder_pop = founder_pop + 1
    fun_fact = "The number of billionares who were founders in " + year + " was " + str(founder_pop)
     
    return fun_fact
    
    
def get_founder_facts2(year):
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    
   
    founder_pop2 = 0
    
    
    for founder in billionaires:
        
        if founder["year"] == int(year) and founder["wealth"]["how"]["was founder"] == True and founder["company"]["sector"]== "retail":
            founder_pop2 = founder_pop2 + 1
    fun_fact2= "The number of billionares who were founders of a retail company in " + year + " was " + str(founder_pop2)
    
    return fun_fact2

        
def get_country_options():
    listOfCountry = []
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    for country in billionaires:
        if country["location"]["citizenship"] not in listOfCountry:
            listOfCountry.append(country["location"]["citizenship"])
    options = ""
    for country in listOfCountry:
        options = options + Markup("<option value=\"" + country + "\">" + country + "</option>")
    return options


def get_country_options2():
    listOfCountry2 = []
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    for country in billionaires:
        if country["location"]["citizenship"] not in listOfCountry2:
            listOfCountry2.append(country["location"]["citizenship"])
    options2 = ""
    for country in listOfCountry2:
        options2 = options2 + Markup("<option value=\"" + country + "\">" + country + "</option>")
    return options2



def get_country_fact(chosenCountry):
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    country_pop = 0
    for country in billionaires:
        if country["location"]["citizenship"] == chosenCountry:
            country_pop = country_pop + 1
    countries_fact = "The # of billionaires from " + chosenCountry + " throughout 1996, 2001, and 2014 was " + str(country_pop)
    return countries_fact


def get_country_fact2(chosenCountry2):
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)
    country_pop2 = 0
    country_age2=0
    totalcountry_age=0
    for country in billionaires:
        if country["location"]["citizenship"] == chosenCountry2:
            country_pop2 = country_pop2 + 1
            country_age2 = country_age2 + country["demographics"]["age"]
            totalcountry_age= country_age2 // country_pop2
    countries_fact2 = "The average age of billionaires from " + chosenCountry2 + " throughout 1996, 2001, and 2014 was " + str(totalcountry_age)+ " years old"
    return countries_fact2



    


    
    
def get_age_facts():
    with open('billionaires.json') as billionaires_data:
        billionaires = json.load(billionaires_data)   
    
    
    earlyUnder50_pop = 0
    earlyOver50_pop = 0
    middleUnder50_pop = 0
    middleOver50_pop = 0
    lateUnder50_pop = 0
    lateOver50_pop = 0
    for founder in billionaires:
        
        if founder["year"] == 1996 and founder["demographics"]["age"] < 51:
            earlyUnder50_pop = earlyUnder50_pop + 1
        
        if founder["year"] == 1996 and founder["demographics"]["age"] > 50:
            earlyOver50_pop = earlyOver50_pop + 1
        
        if founder["year"] == 2001 and founder["demographics"]["age"] < 51:
            middleUnder50_pop = middleUnder50_pop + 1
         
        if founder["year"] == 2001 and founder["demographics"]["age"] > 50:
            middleOver50_pop = middleOver50_pop + 1    
        
        if founder["year"] == 2014 and founder["demographics"]["age"] < 51:
            lateUnder50_pop = lateUnder50_pop + 1   
            
        if founder["year"] == 2014 and founder["demographics"]["age"] > 50:
            lateOver50_pop = lateOver50_pop + 1       
    age_fact= "early over 50 is"+str(earlyOver50_pop)+" early 50 and under is "+str(earlyUnder50_pop) + " middle 50 and under is "+str(middleUnder50_pop)+"middle 50 over is"+str(middleOver50_pop)+"late under 50"+str(lateUnder50_pop)+"late over 50"+str(lateOver50_pop)
    
    return age_fact


    

        
      

 

if __name__=="__main__":
    app.run(debug=False, port=54321)
