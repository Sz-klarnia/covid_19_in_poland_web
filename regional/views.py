from django.shortcuts import render
from .models import *
from chart_page.plotting import *
from .plotting import map_plot
from bokeh.embed import components
from bokeh.palettes import *
import pandas as pd
import geopandas as gpd
from shapely.wkt import loads




populations = [2900163,2072373,2108270,1011592,2454779,3410901,5423168,982626,2127164,1178353,2343928,4517635,1233961,1422737,3498733,1696193]
reg_hospitals_keys = {
    "dolnoslaskie":HospInDolnoslaskie,
    "kujawsko_pomorskie":HospInKujawskoPomorskie,
    "lubelskie":HospInLubelskie,
    "lubuskie":HospInLubelskie,
    "malopolskie":HospInMalopolskie,
    "mazowieckie":HospInMazowieckie,
    "opolskie":HospInOpolskie,
    "podkarpackie":HospInPodkarpackie,
    "podlaskie":HospInPodlaskie,
    "pomorskie":HospInPomorskie,
    "slaskie":HospInSlaskie,
    "swietokrzyskie":HospInSwietokrzyskie,
    "warminsko_mazurskie":HospInWarminskoMazurskie,
    "wielkopolskie":HospInWielkopolskie,
    "zachodniopomorskie":HospInZachodniopomorskie
}
reg_names = {
"dolnoslaskie":"Dolnośląskie",
"kujawsko_pomorskie":"Kujawsko-Pomorskie",
"lubelskie":"Lubelskie",
"lubuskie":"Lubuskie",
"lodzkie":"Łódzkie",
"malopolskie":"Małopolskie",
"mazowieckie":"Mazowieckie",
"opolskie":"Opolskie",
"podkarpackie":"Podkarpackie",
"podlaskie":"Podlaskie",
"pomorskie":"Pomorskie",
"slaskie":"Śląskie",
"swietokrzyskie":"Świętokrzyskie",
"war_maz":"Warmińsko-Mazurskie",
"wielkopolskie":"Wielkopolskie",
"zachodniopomorskie":"Zachodniopomorskie"

}






def region(request,region_id):
    # Defining plots to display on page. Fetching data from database, creating plot with a function, getting components for display

    # plot 1 - new cases
    plot_df_1 = pd.DataFrame(NewCasesRegional.objects.values("date",region_id))
    plot_1 = bar_line_plot(plot_df_1,(region_id,"Przypadki"),"date")
    script1,div1 = components(plot_1)

    # plot 2 - new deaths
    plot_df_2 = pd.DataFrame(NewDeathsRegional.objects.values("date",region_id))
    plot_2 = bar_line_plot(plot_df_2,(region_id,"Zgony"),"date")
    script2,div2 = components(plot_2)

    # plot 3 -  daily change of hospitalizations
    plot_df_3 = pd.DataFrame(reg_hospitals_keys[region_id].objects.values("date","change_d_d"))
    plot_3 = dash_line_plot(plot_df_3,("change_d_d","Zmiana obłożenia szpitali"),"date")
    script3,div3 = components(plot_3)

    # plot 4 - daily change of icu patients
    plot_df_4 = pd.DataFrame(reg_hospitals_keys[region_id].objects.values("date","icu_change_d_d"))
    plot_4 = dash_line_plot(plot_df_4,("icu_change_d_d","Zmiana zajętych respiratorów"),"date")
    script4,div4 = components(plot_4)

    # plot 5 - pct of taken beds
    plot_df_5 = pd.DataFrame(reg_hospitals_keys[region_id].objects.values("date","pct_taken_beds"))
    plot_5 = dash_line_plot(plot_df_5,("pct_taken_beds","Procent zajętych łóżek"),"date")
    script5,div5 = components(plot_5)

    # plot 6 - pct of taken icu beds
    plot_df_6 = pd.DataFrame(reg_hospitals_keys[region_id].objects.values("date","pct_taken_icu"))
    plot_6 = dash_line_plot(plot_df_6,("pct_taken_icu","Procent zajętych respiratorów"),"date")
    script6,div6 = components(plot_6)

    # plot 7 - pct of positive tests
    plot_df_7 = pd.DataFrame(DailyPositivePct.objects.values("date",region_id))
    plot_7 = dash_line_plot(plot_df_7,(region_id,"Procent testów pozytywnych"),"date")
    script7,div7 = components(plot_7)

    # plot 7 - vaccine doses given
    plot_df_8 = pd.DataFrame(Vaccinations.objects.values("date",region_id))
    plot_8 = dash_line_plot(plot_df_8,(region_id,"Liczba podanych dawek szczepionki"),"date")
    script8,div8 = components(plot_8)

    context = {
        "region":region_id.capitalize(),
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
        "script6":script6,
        "div6":div6,
        "script7":script7,
        "div7":div7,
        "script8":script8,
        "div8":div8,

    }
    
    return render(request,"regional_main.html",context)

def testing(request):
    geodf = pd.DataFrame(PlMap.objects.values("region","geometry"))
    geodf["geometry"] = [loads(x) for x in geodf["geometry"]]

    plot_df_1 = pd.DataFrame(pd.DataFrame(RollingMeanPer100K.objects.values()).rename(reg_names, axis=1).transpose().iloc[1:,-1])
    plot_df_1["region"] = list(plot_df_1.index)
    plot_df_1.columns = ["tests","region"]
    plot_df_1["tests"] = plot_df_1["tests"].apply(lambda x: float(x))
    plot_1 = map_plot(plot_df_1,target_col=("tests","Średnia liczba wykonanych testów"),geodf=geodf)
    script1,div1 = components(plot_1)

    plot_df_2 = pd.DataFrame(pd.DataFrame(RollingMean.objects.values()).rename(reg_names, axis=1).transpose().iloc[1:,-1])
    plot_df_2["region"] = list(plot_df_1.index)
    plot_df_2.columns = ["tests","region"]
    plot_2 = map_plot(plot_df_2,target_col=("tests","Średnia liczba wykonanych testów"),geodf=geodf)
    script2,div2 = components(plot_2)
    
    context = {
        "script1" : script1,
        "div1":div1,
        "script2":script2,
        "div2":div2
    }

    return render(request,"reg_testing.html",context)

def cases(request):

    geodf = pd.DataFrame(PlMap.objects.values("region","geometry"))
    geodf["geometry"] = [loads(x) for x in geodf["geometry"]]
    plot_df_1 = pd.DataFrame(RegCases.objects.values("region","number_7_day_mean_per_100k"))
    plot_1 = map_plot(plot_df_1,target_col=("number_7_day_mean_per_100k","Średnia nowych zachorowań na 100k mieszkańców"),geodf=geodf)
    script1,div1 = components(plot_1)

    plot_df_2 = pd.DataFrame(RegCases.objects.values("region","cases_per_1000"))
    plot_2 = map_plot(plot_df_2,target_col=("cases_per_1000","Łączna liczba przypadków na 1000 mieszkańców"),geodf=geodf)
    script2, div2 = components(plot_2)
    
    plot_df_3 = pd.DataFrame(RegCases.objects.values("region","deaths_per_1000"))
    plot_3 = map_plot(plot_df_3,target_col=("deaths_per_1000","Łączna liczba zgonów na 1000 mieszkańców"),geodf=geodf)
    script3, div3 = components(plot_3)

    plot_df_4 = pd.DataFrame(RegCases.objects.values("region","active_cases"))
    plot_4 = map_plot(plot_df_4,target_col=("active_cases","Ilość aktywnych przypadków"),geodf=geodf)
    script4, div4 = components(plot_4)

    context = {
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
        "script3":script3,
        "div3":div3,
        "script4":script4,
        "div4":div4,
    }
    
    return render(request,"reg_cases.html",context)

def hospitals(request):
    models = {
        "Dolnośląskie":HospInDolnoslaskie,
        "Kujawsko-Pomorskie":HospInKujawskoPomorskie,
        "Lubelskie":HospInLodzkie,
        "Lubuskie":HospInLubelskie,
        "Łódzkie":HospInLubuskie,
        "Małopolskie":HospInMalopolskie,
        "Mazowieckie":HospInMazowieckie,
        "Opolskie":HospInOpolskie,
        "Podkarpackie":HospInPodkarpackie,
        "Podlaskie":HospInPodlaskie,
        "Pomorskie":HospInPomorskie,
        "Śląskie":HospInSlaskie,
        "Świętokrzyskie":HospInSwietokrzyskie,
        "Warmińsko-Mazurskie":HospInWarminskoMazurskie,
        "Wielkopolskie":HospInWielkopolskie,
        "Zachodniopomorskie":HospInZachodniopomorskie
    }



    geodf = pd.DataFrame(PlMap.objects.values("region","geometry"))
    geodf["geometry"] = [loads(x) for x in geodf["geometry"]]

    plot_df_1 = pd.DataFrame({"region":[], "val":[]})
    for key,value in models.items():
        plot_df_1 = plot_df_1.append(pd.DataFrame({"region":key,"val":value.objects.latest("date").pct_taken_beds},index=[0]),ignore_index=True)
    plot_1 = map_plot(plot_df_1,target_col=("val","Procent zajętych łóżek"),geodf=geodf)
    script1,div1 = components(plot_1)

    plot_df_2 = pd.DataFrame({"region":[], "val":[]})
    for key,value in models.items():
        plot_df_2 = plot_df_2.append(pd.DataFrame({"region":key,"val":value.objects.latest("date").pct_taken_icu},index=[0]),ignore_index=True)
    plot_2 = map_plot(plot_df_2,target_col=("val","Procent zajętych respiratorów"),geodf=geodf)
    script2, div2 = components(plot_2)

    context = {
        "script1":script1,
        "div1":div1,
        "script2":script2,
        "div2":div2,
    }


    return render(request,"reg_hospitals.html",context)

