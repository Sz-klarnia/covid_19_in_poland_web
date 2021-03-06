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
    Creates a plotwith prediction and true values for 60 days ahead


    Args:
    data_prev: historic true values of variable
    data_pred: predictions of variable
    target_col: column from which data will be displayed in format (column name, name to display in hoover tool)
    data_col: coulmn with datetime data
    """

    data_prev.rename({"date_x":"date"},axis=1,inplace=True)

    # function used to plot values supplied in per_million format, multiplying values by 37.9 to get real values
    data_prev[target_col[0]] = data_prev[target_col[0]] * 37.9
    data_pred[target_col[0]] = data_pred[target_col[0]] * 37.9



    # defining tooltips for hover tool and data source for bokeh to use
    source_prev = ColumnDataSource(data=data_prev)
    source_preds = ColumnDataSource(data=data_pred)

    # defining fgure, scaling enabled
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_width")
    # historic line and it's hover tool
    historic = p.line(x="date",y=target_col[0],source=source_prev,color="grey",line_width=2,legend_label="Dane historyczne")
    hover = HoverTool(tooltips = [(target_col[1],f"@{target_col[0]}"+"{0.0}")], mode='vline',point_policy='follow_mouse',renderers=[historic])
    hover.formatters = {"@date":"datetime"}
    p.tools.append(hover)
    #  predictions line and it's hover tool
    pred = p.line(x="date",y=target_col[0],source=source_preds,line_width=2,color="#2422bb",legend_label="Prognoza")
    hover1 = HoverTool(tooltips = [(target_col[1],f"@{target_col[0]}"+"{0.0}")], mode='vline',point_policy='follow_mouse',renderers=[pred])
    hover1.formatters = {"@date":"datetime"}
    p.tools.append(hover1)



    # creating hover tool

    p.legend.location = "top_left"
    return p