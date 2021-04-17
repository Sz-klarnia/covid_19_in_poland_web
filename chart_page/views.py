from django.shortcuts import render
from .models import Cases, Hospitalizations, Testing, Vaccinations
from .plotting import bar_line_plot, dash_line_plot,fill_under_plot,fill_under_plot_stacked,line_plot
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
import pandas as pd
# Create your views here.

# View method for cases subpage
def cases(request):
    # variable storing last values in db, used to fill statistics displayed on top of the page
    new_c = Cases.objects.latest("date")
    # variables storing 7 day means calculated from the db
    last_7_cases = sum([obj.new_cases for obj in Cases.objects.all().order_by("-date")[:7]]) /7
    last_7_deaths = sum([obj.new_deaths for obj in Cases.objects.all().order_by("-date")[:7]]) /7

    # Defining plots to display on page. Fetching data from database, creating plot with a function, getting components for display

    # plot 1 - new cases
    plot_df_1 = pd.DataFrame(Cases.objects.values("new_cases","date"))
    plot_1 = bar_line_plot(plot_df_1,target_col=("new_cases","Nowe zachorowania"),date_col="date")
    script1, div1 = components(plot_1)

    # plot 2 - week to week rise 
    plot_df_2 = pd.DataFrame(Cases.objects.values("cases_rise_week_to_week","date"))
    plot_2 = dash_line_plot(plot_df_2,target_col=("cases_rise_week_to_week","Wzrost t/t w procentach"),date_col="date",span=-60)
    script2,div2 = components(plot_2)

    # plot 3 - cases rise in pct
    plot_df_3 = pd.DataFrame(Cases.objects.values("cases_rise_pct","date"))
    plot_3 = dash_line_plot(plot_df_3,target_col=("cases_rise_pct","Wzrost w procentach"),date_col="date",span=-120)
    script3,div3 = components(plot_3)

    # plot 4 - new deaths
    plot_df_4 = pd.DataFrame(Cases.objects.values("new_deaths","date"))
    plot_4 = bar_line_plot(plot_df_4,target_col=("new_deaths","Zgony"),date_col="date")
    script4, div4 = components(plot_4)

    # plot 5 - all cases and active cases
    plot_df_5 = pd.DataFrame(Cases.objects.values("sum_cases","active_cases","date"))
    plot_5 = fill_under_plot(plot_df_5,target_col=[("sum_cases","Wszystkie przypadki"),("active_cases","aktywne")],date_col="date")
    script5, div5 = components(plot_5)

    # defining context with statistics and plot components to render on page
    context = {
        "cases":new_c,
        "avg_cases":last_7_cases,
        "avg_deaths":last_7_deaths,
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
        "div3":div3,
        "script3":script3,
        "div4":div4,
        "script4":script4,
        "div5":div5,
        "script5":script5
    }

    return render(request, 'cases.html',context)

# View method for hospitals subpage
def hospitals(request):
    # variables storing last values in db, used to fill statistics displayed on top of the page
    new_h = Hospitalizations.objects.latest("date")
    pct_icu = new_h.icu / new_h.icu_beds *100

    # Defining plots to display on page. Fetching data from database, creating plot with a function, getting components for display

    # plot 1 - hospitalizations
    plot_df_1 = pd.DataFrame(Hospitalizations.objects.values("hospitalized","beds","date"))
    plot_1 = fill_under_plot(plot_df_1,target_col=[("hospitalized","Zajęte łóżka"),("beds","Dostępne łóżka")],date_col="date",span=150)
    script1, div1 = components(plot_1)

    # plot 2 - ICU cases
    plot_df_2 = pd.DataFrame(Hospitalizations.objects.values("icu","icu_beds","date"))
    plot_2 = fill_under_plot(plot_df_2,target_col=[("icu","Zajęte respiratory"),("icu_beds","Dostępne respiratory")],date_col="date",span=150)
    script2, div2 = components(plot_2)

    # plot 3 - daily change in hospitalizations
    plot_df_3 = pd.DataFrame(Hospitalizations.objects.values("change_d_d","date"))
    plot_3 = dash_line_plot(plot_df_3,target_col=("change_d_d","Zmiana d/d"),date_col="date",span=60)
    script3, div3 = components(plot_3)

    # plot 4 - daily change in icu cases
    plot_df_4 = pd.DataFrame(Hospitalizations.objects.values("icu","date"))
    plot_df_4["change_d_d"] = [plot_df_4["icu"][i]-plot_df_4["icu"][i-1] if i>0 else 0 for i in range(len(plot_df_4))]
    plot_4 = dash_line_plot(plot_df_4,target_col=("change_d_d","Zmiana d/d"),date_col="date",span=60)
    script4, div4 = components(plot_4)
    
    # plot 5 - quarantined
    plot_df_5 = pd.DataFrame(Hospitalizations.objects.values("quarantined","date"))
    plot_5 = bar_line_plot(plot_df_5,target_col=("quarantined","W kwarantannie"),date_col="date")
    script5, div5 = components(plot_5)

    # context 
    context = {
        "hosp":new_h,
        "icu_pct":pct_icu,
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
        "script3":script3,
        "div3":div3,
        "script4":script4,
        "div4":div4,
        "script5":script5,
        "div5":div5,
    }
    return render(request, 'hospitals.html',context=context)

# View method for testing subpage
def testing(request):
    # variables storing last values in db, used to fill statistics displayed on top of the page
    new_t = Testing.objects.latest("date")

    # Defining plots to display on page. Fetching data from database, creating plot with a function, getting components for display

    # plot 1 - number of tests in last day
    plot_df_1 = pd.DataFrame(Testing.objects.values("tests_in_24h","date"))
    plot_1 = bar_line_plot(plot_df_1,target_col=("tests_in_24h","Ilość wykonanych testów"),date_col="date")
    script1, div1 = components(plot_1)

    # plot 2 - pct of positive tests
    plot_df_2 = pd.DataFrame(Testing.objects.values("pct_24h_positivity_rate","date"))
    plot_2 = dash_line_plot(plot_df_2,target_col=("pct_24h_positivity_rate","Procent testów pozytywnych"),date_col="date",span=150)
    script2, div2 = components(plot_2)

    # plot 3 - poz orders
    plot_df_3 = pd.DataFrame(Testing.objects.values("poz_orders_24h","date"))
    plot_3 = dash_line_plot(plot_df_3,target_col=("poz_orders_24h","Zlecenia POZ"),date_col="date",span=120)
    script3, div3 = components(plot_3)

    # context
    context={
        "tests":new_t,
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
        "script3":script3,
        "div3":div3,
    }
    return render(request, 'testing.html',context=context)

# View method for vaccinations subpage
def vacc(request):
    # variables storing last values in db, used to fill statistics displayed on top of the page
    new_vacc = Vaccinations.objects.latest("date")
    pct = (new_vacc.number_2_doses / 37900000)*100

    # Defining plots to display on page. Fetching data from database, creating plot with a function, getting components for display

    # plot 1 - daily vaccinations
    plot_df_1 = pd.DataFrame(Vaccinations.objects.values("daily_vacc","date"))
    plot_1 = bar_line_plot(plot_df_1,target_col=("daily_vacc","Podane szczepionki"),date_col="date",span=90)
    script1, div1 = components(plot_1)

    # plot 2 - doses delivered to Poland and used
    plot_df_2 = pd.DataFrame(Vaccinations.objects.values("doses_delivered","used","date"))
    plot_2 = fill_under_plot(plot_df_2,target_col=[("doses_delivered","Dostarczone dawki"),("used","Podano")],date_col="date",span=90)
    script2, div2 = components(plot_2)

    # plot 3 - vaccinated with one and both doses
    plot_df_3 = pd.DataFrame(Vaccinations.objects.values("number_1_dose","number_2_doses","date"))
    plot_3 = fill_under_plot_stacked(plot_df_3,target_col=[("number_1_dose","Zaszczepieni jedną dawką"),("number_2_doses","Zaszczepieni obiema dawkami")],date_col="date",span=60)
    script3, div3 = components(plot_3)

    # plot 4 - NOP cases vs all jabs
    plot_df_4 = pd.DataFrame(Vaccinations.objects.values("used","nop_light","nop_severe","date"))
    plot_4 = fill_under_plot(plot_df_4,target_col=[("used","Podane dawki"),("nop_light","Lekki NOP"),("nop_severe","Ciężki NOP")],date_col="date",span=60)
    script4, div4 = components(plot_4)
    
    # plot 5 - pct of vaccinated Poles
    plot_df_5 = pd.DataFrame(Vaccinations.objects.values("number_2_doses","date"))
    plot_df_5["pct"] = plot_df_5["number_2_doses"] / 379000
    plot_5 = line_plot(plot_df_5,target_col=[("pct","Procent zaszczepionych osób")],date_col="date",target_value=70)
    script5, div5 = components(plot_5)

    # number of citizens in each group in database, source: GUS
    age_gr = [5600000,6100000,5600000,4600000,5100000,1724000,2474000]

    # plot 6 - pct vaccinated in each age group
    plot_df_6 = pd.DataFrame(Vaccinations.objects.values("number_18_30","number_31_40","number_41_50","number_51_60","number_61_70","number_71_75",
"number_75_field","date"))
    for i in range(len(age_gr)):
        plot_df_6.iloc[:,i] = plot_df_6.iloc[:,i] / age_gr[i] * 100
    plot_6 = line_plot(plot_df_6,target_col=[("number_18_30","18-30"),("number_31_40","31-40"),("number_41_50","41-50")
    ,("number_51_60","51-60"),("number_61_70","61-70"),("number_71_75","71-75"),("number_75_field","Powyżej 75")],
    date_col="date")
    script6, div6 = components(plot_6)
    
    context = {
        "vacc":new_vacc,
        "pct":pct,"script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
        "script3":script3,
        "div3":div3,
        "script4":script4,
        "div4":div4,
        "script5":script5,
        "div5":div5,
        "script6":script6,
        "div6":div6

    }
    return render(request, 'vacc.html',context)