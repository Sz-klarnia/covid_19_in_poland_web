from bokeh.models import ColumnDataSource, HoverTool,GeoJSONDataSource,LinearColorMapper,ColorBar,Span
from bokeh.plotting import figure, output_notebook, show
from bokeh.palettes import inferno
import pandas as pd
import numpy as np
import geopandas as gpd
import json
from datetime import timedelta


def bar_line_plot(data,target_col,date_col,span=500):
    """
    Creates a plot with bars and a line. Bars represent daily values, line represents 7 day rolling mean
    Data - dataframe with datta to use in plotting
    target_columns - columns to include on the plot. Date is always included as x axis values. Columns supplied in format:
    (column name,name to display on hover tool)
    date_col - column with dates
    span - variable used to restrict size of the plot. Number of days to display
    """

    # calculating rolling mean
    data["rolling_mean"] = data[target_col[0]].rolling(7).mean()

    # clipping data to have length equal to span supplied
    data = data.iloc[-span:,:]

    # defining tooltips
    tooltips = [("Data","@date{%F}"),((target_col[1],f"@{target_col[0]}"+"{0,0}")),("Średnia 7-dniowa",'@rolling_mean{0,0}')]
    source = ColumnDataSource(data=data)

    # creating figure, enabling sizing plots to fit containers on site
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_both")
    # creatin bars and line plot
    bars = p.vbar(x="date",top=target_col[0],source=source,color="#2422bb",alpha=0.5,width=timedelta(days=1),legend_label=target_col[1])
    line = p.line(x="date",y="rolling_mean",source=source,line_width=2,color="black",legend_label="Średnia 7-dniowa")
    # creating hoover tool 
    hover = HoverTool(tooltips = tooltips, mode='vline',point_policy='follow_mouse',renderers=[line])
    hover.formatters = {"@date":"datetime"} # specyfying datetime formater for date field in hoover tool
    p.tools.append(hover)
    # returning plot
    p.legend.location = "top_left"
    return p

def dash_line_plot(data,target_col,date_col,span=500):
    """
    Creates a plot with two lines. One follows daily changes of the parameter, second one follows 7 day rolling mean.
    target_columns - columns to include on the plot. Date must be always included as x axis values. Supplied in format: (column name,name to display on hover tool)
    span - variable used to restrict size of the plot. Number of days to display
    """
    # calculating the rolling mean
    data["rolling_mean"] = data[target_col[0]].rolling(7).mean()
    # clipping data to match span lenght
    data = data.iloc[-span:,:]

    # defining tooltips for hover tool and data source for bokeh to use
    tooltips = [("Data","@date{%F}"),((target_col[1],f"@{target_col[0]}"+"{0.0}")),("Średnia 7-dniowa",'@rolling_mean'+"{0.0}")]
    source = ColumnDataSource(data=data)

    # defining fgure, scaling enabled
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_width")
    # defining lines to display - dash line represents daily values, normaln line - rolling mean
    line_dash = p.line(x="date",y=target_col[0],source=source,color="grey",line_width=1,alpha=0.6,legend_label=target_col[1])
    line = p.line(x="date",y="rolling_mean",source=source,line_width=2,color="#2422bb",legend_label="Średnia 7-dniowa")
    # plot often used to display values around zero - plotting horizontal line at zero
    hline = Span(location=0, dimension='width', line_color='black', line_width=1)
    p.renderers.extend([hline])
    # creating hover tool
    hover = HoverTool(tooltips = tooltips, mode='vline',point_policy='follow_mouse',renderers=[line])
    hover.formatters = {"@date":"datetime"}
    p.tools.append(hover)
    p.legend.location = "top_left"
    return p
def line_plot(data,target_col,date_col,target_value=None,span=500):
    """
    Single or multiple line plot with option of defining target value to display on the plot. Separate Hover Tool for each line on the plot, vline 
    rendered
    data: data to construct the plot
    target_col: tagret columns to display on the plot, (name,hover plot name)
    date_col: column with datetime data
    target_value: optional - display target value to which the plot coincides to
    span: span of the dataframe to use for plotting
    """
    # defining range of data to use
    data = data.iloc[-span:,:]
    # creating source
    source = ColumnDataSource(data=data)
    # defining figure
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_both")
    # plotting target line if chosen
    if target_value != None:
        target_line = p.line(x="date",y=target_value,source=source,color="black")

    # in loop - defining plots, saving them inside dictionary, creating hover tool based on dictionary
    colors = ["#2422bb","green","red","grey","yellow","black","purple"]
    plots = {}
    for i in range(len(target_col)):
        plots[i] = p.line(x="date",y=target_col[i][0],source=source,line_width=1,color=colors[i],legend_label=target_col[i][1])
        if i == 0:
            tooltips = [("Data","@date{%F}"),(target_col[i][1],f"@{target_col[i][0]}"+"{0.0}")]
        else:
            tooltips = [(target_col[i][1],f"@{target_col[i][0]}"+"{0.0}")]
        p.add_tools(HoverTool(tooltips = tooltips, mode='vline',point_policy='follow_mouse',renderers=[plots[i]],formatters={"@date":"datetime"}))
    
    p.legend.location="top_left"
    p.legend.click_policy="hide"
    return p

def fill_under_plot(data,target_col,date_col,span=500):
    """
    Creates a plot with two number of lines and fills spaces between them. Separate Hover Tool for each line
    Data: dataframe with datta to use in plotting. Minimal number of lines - 2
    target_columns: columns to include on the plot. Date is always included as x axis values. Columns supplied in format:
    (column name,name to display on hover tool)
    date_col: column with datetime data
    span: how much data to view on the plot [negative indexed]
    """
    # defining data range
    data = data.iloc[-span:,:]
    # defining data source
    source = ColumnDataSource(data=data)
    # defining figure
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_both")

    # color values to use in plot
    colors = ["grey","#babbd6","#9b9deb","#2422bb"]


    # in loop - plotting lines and areas, creating hover tools
    plots ={}
    for i in range(len(target_col)):
        if i == 0:                      #first one always grey
            color = "grey"
        if i == len(target_col)-1:        #last one always "#2422bb"
            color = "#2422bb"
        else: 
            color = colors[i]
        plots[i] = p.line(x="date",y=target_col[i][0],source=source,color=color,line_width=2,legend_label=target_col[i][1])
        if i+1 > len(target_col)-1:
            p.varea(x="date",y1=0,y2=target_col[i][0],fill_color=color,alpha=0.2,source=source)
        else:
            p.varea(x="date",y1=target_col[i+1][0],y2=target_col[i][0],fill_color=color,alpha=0.2,source=source)
        if i == 0:
            tooltips = [(target_col[i][1],f"@{target_col[i][0]}"+"{0.0}"),("Data","@date{%F}")]
        else:
            tooltips = [(target_col[i][1],f"@{target_col[i][0]}"+"{0.0}")]
        p.add_tools(HoverTool(tooltips = tooltips, mode='vline',point_policy='follow_mouse',renderers=[plots[i]],formatters={"@date":"datetime"}))
    p.legend.location = "top_left"
    return p

def fill_under_plot_stacked(data,target_col,date_col,span=500):
    """
    Creates a plot with two lines and fills spaces between them. Stacks values
    Data - dataframe with datta to use in plotting
    target_columns - columns to include on the plot. Date is always included as x axis values. Columns supplied in format:
    (column name,name to display on hover tool)
    span - how much data to view on the plot [negative indexed]
    """
    # calculating values of the higher plot
    data[target_col[0][0]] = data[target_col[0][0]]+data[target_col[1][0]]
    # defining data range
    data = data.iloc[-span:,:]
    # defining tooltips
    tooltips = [("Data","@date{%F}"),(target_col[0][1],f"@{target_col[0][0]}"+"{0.0}"),(target_col[1][1],f"@{target_col[1][0]}"+"{0.0}")]
    # defining data source
    source = ColumnDataSource(data=data)

    # defining plot
    p = figure(plot_width=900, plot_height=400,x_axis_type="datetime",sizing_mode="scale_both")
    # plotting lines and areas
    line_1 = p.line(x="date",y=target_col[0][0],source=source,color="grey",line_width=2)
    line_2 = p.line(x="date",y=target_col[1][0],source=source,line_width=2,color="#2422bb")
    area_1 = p.varea(x="date",y1=target_col[0][0],y2=target_col[1][0],fill_color='grey',alpha=0.2,source=source)
    area_2 = p.varea(x="date",y1=0,y2=target_col[1][0],fill_color="#2422bb",alpha=0.2,source=source)
    # defining hover tools
    hover = HoverTool(tooltips = tooltips, mode='vline',point_policy='follow_mouse',renderers=[line_1])
    hover.formatters = {"@date":"datetime"}
    p.tools.append(hover)
    return p


