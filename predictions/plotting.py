from bokeh.models import ColumnDataSource, HoverTool,GeoJSONDataSource,LinearColorMapper,ColorBar,Span
from bokeh.plotting import figure, output_notebook, show
from bokeh.palettes import inferno
import pandas as pd
import numpy as np
import geopandas as gpd
import json
from datetime import timedelta

def prediction_plot(data_prev,data_pred,target_col,date_col):
    """
    Creates a plot with two lines. One follows daily changes of the parameter, second one follows 7 day rolling mean.
    target_columns - columns to include on the plot. Date must be always included as x axis values. Supplied in format: (column name,name to display on hover tool)
    span - variable used to restrict size of the plot. Number of days to display
    """

    data_prev.rename({"date_x":"date"},axis=1,inplace=True)
    data_pred.rename({"new_cases":"new_cases_per_million"},axis=1,inplace=True)
    # calculating the rolling mean - previous data to be plotted
    data_prev["rolling"] = data_prev[target_col[0]].rolling(7).mean() * 37.9
    data_pred[target_col[0]] = data_pred[target_col[0]] * 37.9


    # defining tooltips for hover tool and data source for bokeh to use
    source_prev = ColumnDataSource(data=data_prev)
    source_preds = ColumnDataSource(data=data_pred)

    # defining fgure, scaling enabled
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_width")
    # defining lines to display - dash line represents daily values, normaln line - rolling mean
    historic = p.line(x="date",y="rolling",source=source_prev,color="grey",line_width=1,alpha=0.6,legend_label="Dane historyczne")
    hover = HoverTool(tooltips = [(target_col[1],f"@{target_col[0]}"+"{0.0}")], mode='vline',point_policy='follow_mouse',renderers=[historic])
    hover.formatters = {"@date":"datetime"}
    p.tools.append(hover)

    pred = p.line(x="date",y=target_col[0],source=source_preds,line_width=2,color="#2422bb",legend_label="Predykcje")
    hover1 = HoverTool(tooltips = [(target_col[1],f"@{target_col[0]}"+"{0.0}")], mode='vline',point_policy='follow_mouse',renderers=[pred])
    hover1.formatters = {"@date":"datetime"}
    p.tools.append(hover1)
    # creating hover tool

    p.legend.location = "top_left"
    return p