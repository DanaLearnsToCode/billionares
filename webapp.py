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
    age_fact= "early over 50 is"+str(earlyOver50_pop)+" early 50 and under is "+str(earlyUnder50_pop) + " middle 50 and under is "+str(middleUnder50_pop)+"middle 50 over is"+str(middleOver50_pop)
    
    return age_fact


    

       #early_under50 = 0
       #early_over50 = 0
       #middle_under50 = 0
       #middle_over50 = 0
       #late_under50 = 0
       #late_over50 = 0
        
      

    




if __name__=="__main__":
    app.run(debug=False, port=54321)
