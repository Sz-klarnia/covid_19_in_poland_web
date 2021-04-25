from bokeh.models import ColumnDataSource, HoverTool,GeoJSONDataSource,LinearColorMapper,ColorBar,Span
from bokeh.plotting import figure, output_notebook, show
from bokeh.palettes import inferno
import pandas as pd
import numpy as np
import geopandas as gpd
import json
from datetime import timedelta


def map_plot(data,target_col,geodf):
    """
    Function enables creation of inspectable maps depicting statistical values using bokeh plotting library and geopandas to supply vector maps
    of polish regions
    data - data to use as a base for the plot
    target_col - column in supplied data with value of depicted statistic
    geodf - geopandas dataframe with vectors
    palet - color palette fro bokeh to use - color(<size of palette>)
    """
    
    # merging dataframes, creating source
    geodf = gpd.GeoDataFrame(geodf.merge(data,on="region")).to_json()
    source = GeoJSONDataSource(geojson=geodf)

    # defining figure
    p = figure(plot_height = 500, plot_width = 500 , toolbar_location = "below",sizing_mode="scale_both")
    # defining color palette
    palette = inferno(8)
    palette = palette[::-1]

    # defining color mapper to turn values into colors
    color_mapper = LinearColorMapper(palette = palette, low = 0, high = max(data[target_col[0]])*1.1)
    # creating color bar to display below of the plot
    color_bar = ColorBar(color_mapper = color_mapper, 
                         label_standoff = 8,
                         border_line_color = None,
                         location = (0,0), 
                         orientation = "vertical")

    # Add patch renderer to figure.
    plska = p.patches("xs","ys", source = source,
                       fill_color ={"field":target_col[0],
                                   "transform":color_mapper},
                       line_color = "grey", 
                       line_width = 0.25, 
                       fill_alpha = 1)
    # Create hover tool
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.axis.visible=False
    p.add_tools(HoverTool(renderers = [plska],
                          tooltips = [('Województwo','@region'),
                                    (target_col[1],f'@{target_col[0]}')]))

    # add color bar to the layot
    p.add_layout(color_bar,"right")
    return(p)