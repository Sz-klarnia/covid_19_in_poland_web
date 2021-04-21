from django.shortcuts import render
from .models import *
from .plotting import *
from bokeh.embed import components

# Create your views here.

# Create your views here.
def predictions(request):
    historical = pd.DataFrame(ModellingData.objects.values("new_cases_per_million","date_x","hosp_patients_per_million")).iloc[:90,:]
    scenarios = {"Scenario1":"Scenariusz 1",
    "Scenario2":"Scenariusz 2",
    "Scenario3":"Scenariusz 3",
    "Scenario4":"Scenariusz 4",
    "Scenario5":"Scenariusz 5",
    "Scenario6":"Scenariusz 6",
    "Scenario7":"Scenariusz 7",
    "Scenario8":"Scenariusz 8",
    "Scenario9":"Scenariusz 9",
    "Scenario10":"Scenariusz 10",
    "Scenario11":"Scenariusz 11",
    "Scenario12":"Scenariusz 12",
    }
    scenarios_models = {"Scenario1":Scenario1,
    "Scenario2":Scenario2,
    "Scenario3":Scenario3,
    "Scenario4":Scenario4,
    "Scenario5":Scenario5,
    "Scenario6":Scenario6,
    "Scenario7":Scenario7,
    "Scenario8":Scenario8,
    "Scenario9":Scenario9,
    "Scenario10":Scenario10,
    "Scenario11":Scenario11,
    "Scenario12":Scenario12}

    if 'Scenario' in request.GET:
        scenario = scenarios_models[request.GET["Scenario"]]
        preds = pd.DataFrame(scenario.objects.values())
        p = prediction_plot(historical,preds,("new_cases_per_million","Nowe przypadki"),"date")
        script1,div1 = components(p)
        context = {
        "scenarios":scenarios,
        "script1":script1,
        "div1":div1
    }

    else:
      context = {
        "scenarios":scenarios,

    }  





    
    return render(request,"predictions.html",context)