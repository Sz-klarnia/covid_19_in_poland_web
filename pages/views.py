from django.shortcuts import render
from .models import Cases, Hospitalizations

# Create your views here.
def index(request):
    # fetching data to display in statistics
    new_c = Cases.objects.latest("date")
    hosp = Hospitalizations.objects.latest("date")
    week_avg = round(sum([x[0] for x in list(Cases.objects.values_list("new_cases"))[-7:]]) /7/379)

    # context variable
    context = {
        "cases":new_c,
        "hosp":hosp,
        "avg":week_avg

    }


    return render(request, 'index.html',context)

