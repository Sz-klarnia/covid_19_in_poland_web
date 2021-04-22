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
    "Scenario5":"Scenariusz 5"
    }
    scenarios_models = {"Scenario1":Scenario1,
    "Scenario2":Scenario2,
    "Scenario3":Scenario3,
    "Scenario4":Scenario4,
    "Scenario5":Scenario5,
}

    if 'Scenario' in request.GET:
        scenario = scenarios_models[request.GET["Scenario"]]
        preds = pd.DataFrame(scenario.objects.values())
        print(scenario)
        p = prediction_plot(historical,preds,("new_cases_per_million","Nowe przypadki"),"date")
        script1,div1 = components(p)
        p = prediction_plot(historical,preds,("hosp_patients_per_million","Liczba hospitalizowanych"),"date")
        script2,div2 = components(p)
        context = {
        "scenarios":scenarios,
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2
    }

    else:
      context = {
        "scenarios":scenarios,

    }  




    return render(request,"predictions.html",context)