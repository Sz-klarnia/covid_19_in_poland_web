# Django web page to display current COVID-19 statistics in Poland. Based on data collected by Michał Rogalski.

## URL
http://www.dane-covid-19.pl/

## Technology
Frontend made with bootstrap template with changes in layout.  
Backend written using Django with PostgreSQL.  
Deployed using gunicorn and nginx.  

## About
This Django application was made to gather, process and display COVID-19 statistics, for clear and up-to-date overview of COVID-19 in Poland.

## Features

1. Background processes gathering new data based on AdvancedPythonScheduler. Modelling data update once every 24h, other statistics update every hour. Working on updating on every change, awaiting permissions.
2. Background process generating new predictions every 24h, after modelling data update. Written and trained using TensorFlow, source code to be pushed to github soon. 
3. Inspectable plots generated from database using Bokeh library.
4. Inspectable maps generated from database using Bokeh and GeoPandas.
5. Statistics counters generated from database. 

## Data sources
Plots:  
Covid-19 w Polsce - google spreadsheet made by Michał Rogalski

Modelling data:
Our World in Data
Google COVID-19 Mobility Report
COVID Government Response Tracker by Blatnik School of Government
