from django.shortcuts import render
from .models import *
from .plotting import *
from bokeh.embed import components

# View method for predictions page
def predictions(request):
    # getting historical data from the DB
    historical = pd.DataFrame(ModellingData.objects.values("new_cases_per_million","date_x","hosp_patients_per_million","new_deaths_per_million")).iloc[:90,:]
    # Translating scenarios to polish to display on page
    scenarios = {"Scenario1":"Scenariusz 1",
    "Scenario2":"Scenariusz 2",
    "Scenario3":"Scenariusz 3",
    "Scenario4":"Scenariusz 4",
    "Scenario5":"Scenariusz 5"
    }
    # Assigning model from db to each scenario
    scenarios_models = {"Scenario1":Scenario1,
    "Scenario2":Scenario2,
    "Scenario3":Scenario3,
    "Scenario4":Scenario4,
    "Scenario5":Scenario5,
}

    # if scenario is chosen by user
    if 'Scenario' in request.GET:
        # get model of correct scenatio
        scenario = scenarios_models[request.GET["Scenario"]]
        # get predictions from model
        preds = pd.DataFrame(scenario.objects.values())
        # plot predicted new cases
        p = prediction_plot(historical,preds,("new_cases_per_million","Nowe przypadki"),"date")
        script1,div1 = components(p)
        # plot predicted hospitalizations
        p = prediction_plot(historical,preds,("hosp_patients_per_million","Liczba hospitalizowanych"),"date")
        script2,div2 = components(p)
        # plot predicted new deaths
        p = prediction_plot(historical,preds,("new_deaths_per_million","Nowe zgony"),"date")
        script3,div3 = components(p)
        context = {
        "scenarios":scenarios,
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
        "script3":script3,
        "div3":div3
    }

    else:
      context = {
        "scenarios":scenarios,

    }  




    return render(request,"predictions.html",context)

def model_info(request):

    return render(request,"model_desc.html")