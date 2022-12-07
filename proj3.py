# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
import networkx as nx


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

cyto.load_extra_layouts()

new_var = 'la'
nodes = [
    {
        'data': {'id': short, 'label': label}
    }
    for short, label in (
        ('jd', 'Jeremiah Dy'),
        ('hb', 'Henry Blazier'),
        ('kbr', 'Kale Beever-Riordon'),
        ('jc', 'Jade Cui'),
        ('jl', 'Jamie Laurin'),
        ('lra', 'Leeden Raquel'),
        ('ie', 'Ian Eshelman'),
        ('cs', 'Christian Siador'),
        ('jk', 'Jun Kim'),
        ('twi','Tiffany Williams'),
        ('two', 'Taylor Wong'),
        ('lre', 'Leilani Reich'),
        ('tl', 'Tony Long'),
        ('eb', 'Edward Bruffey'),
        ('ca', 'Cole Amparo'),
        ('mr', 'Michael Rogers'),
        ('sr', 'Samuel Roberts'),
        ('ss', 'Shane Severino'),
        ('hc', 'Hansen Cabanero'),
        ('co', 'Chad Oshiro'),
        ('zc', 'Zachary Chaikin'),
        ('mq', 'Mujtaba Quadri'),
        ('mb', 'Marcos Buccat'),
        ('jh', 'Justin Honda'),
        ('pg', 'Preston Garcia'),
        ('ce', 'Candace Edwards'),
        ('gb', 'Gunwook Baik'),
        ('js', 'John Suelen'),
        ('kh', 'Kelly Hwang'),
        ('nl', 'Nicholas Lee'),

    )
]

rawDataAlready = [
    {'data': {'source': source, 'target': target}, }
    for source, target in (
        ('jc', 'lre'),
        ('lra', 'mq'),
        ('lra', 'co'),
        ('lra', 'ie'),
        ('ie', 'lra'),
        ('ie', 'pg'),
        ('cs', 'pg'),
        ('cs', 'ca'),
        ('cs', 'mb'),
        ('cs', 'twi'),
        ('cs', 'js'),
        ('cs', 'mr'),
        ('cs', 'hc'),
        ('twi', 'mr'),
        ('lre', 'jd'),
        ('lre', 'kh'),
        ('tl', 'hb'),
        ('tl', 'gb'),
        ('tl', 'mq'),
        ('ca', 'hb'),
        ('ca', 'mq'),
        ('mr', 'twi'),
        ('mr', 'cs'),
        ('js', 'ss'),
        ('js', 'mb'),
        ('js', 'co'),
        ('js', 'lra'),
        ('js', 'mq'),
        ('js', 'hc'),
        ('hb', 'ss'),
        ('hb', 'ca'),
        ('hb', 'mb'),
        ('hb', 'mq'),
        ('hb', 'mr'),
        ('ss', 'hb'),
        ('ss', 'mb'),
        ('ss', 'co'),
        ('ss', 'jh'),
        ('ss', 'nl'),
        ('ss', 'mr'),
        ('hc', 'co'),
        ('co', 'pg'),
        ('co', 'mb'),
        ('co', 'lra'),
        ('co', 'hc'),
        ('mq', 'ss'),
        ('mq', 'hb'),
        ('mq', 'ca'),
        ('mq', 'lra'),
        ('mq', 'tl'),
        ('mq', 'jh'),
        ('mq', 'kh'),
        ('mq', 'nl'),
        ('mb', 'ca'),
        ('mb', 'co'),
        ('mb', 'js'),
        ('mb', 'cs')
    )
]

rawDataNewly = [
    {'data': {'source': source, 'target': target}, }
    for source, target in (
        ('jd', 'pg'),
        ('jd', 'ss'),
        ('jd', 'jk'),
        ('jd', 'hb'),
        ('jd', 'ce'), 
        ('jd', 'lre'),
        ('jd', 'two'),
        ('jd', 'kbr'),
        ('jd', 'ca'),
        ('jd', 'zc'),
        ('jd', 'mb'),
        ('jd', 'ie'),
        ('jd', 'eb'),
        ('jd', 'co'),
        ('jd', 'lra'),
        ('jd', 'gb'),
        ('jd', 'mq'),
        ('jd', 'twi'),
        ('jd', 'js'),
        ('jd', 'tl'),
        ('jd', 'sr'),
        ('jd', 'jc'),
        ('jd', 'jl'),
        ('jd', 'jh'),
        ('jd', 'kh'),
        ('jd', 'nl'),
        ('jd', 'cs'),
        ('jd', 'mr'),
        ('jd', 'hc'),
        ('kbr', 'tl'),
        ('kbr', 'jc'),
        ('jc', 'jd'),
        ('jc', 'co'),
        ('jc', 'mq'),
        ('jc', 'jl'),
        ('jc', 'kh'),
        ('jc', 'hc'),
        ('jl', 'jd'),
        ('jl', 'mb'),
        ('jl', 'co'),
        ('jl', 'jc'),
        ('jl', 'kh'),
        ('lra', 'pg'),
        ('lra', 'hb'),
        ('lra', 'ca'),
        ('lra', 'kh'),
        ('lra', 'nl'),
        ('cs', 'ss'),
        ('cs', 'jk'),
        ('cs', 'hb'),
        ('cs', 'ce'), 
        ('cs', 'lre'),
        ('cs', 'two'),
        ('cs', 'kbr'),
        ('cs', 'zc'),
        ('cs', 'ie'),
        ('cs', 'eb'),
        ('cs', 'co'),
        ('cs', 'lra'),
        ('cs', 'gb'),
        ('cs', 'mq'),
        ('cs', 'tl'),
        ('cs', 'sr'),
        ('cs', 'jc'),
        ('cs', 'jl'),
        ('cs', 'jh'),
        ('cs', 'kh'),
        ('cs', 'nl'),
        ('jk', 'ce'),
        ('jk', 'eb'),
        ('twi', 'js'),
        ('twi', 'jl'),
        ('twi', 'kh'),
        ('twi', 'cs'),
        ('two', 'pg'),
        ('two', 'ss'),
        ('two', 'jk'),
        ('two', 'hb'),
        ('two', 'ce'), 
        ('two', 'lre'),
        ('two', 'kbr'),
        ('two', 'ca'),
        ('two', 'zc'),
        ('two', 'mb'),
        ('two', 'ie'),
        ('two', 'eb'),
        ('two', 'co'),
        ('two', 'lra'),
        ('two', 'gb'),
        ('two', 'mq'),
        ('two', 'twi'),
        ('two', 'js'),
        ('two', 'tl'),
        ('two', 'sr'),
        ('two', 'jc'),
        ('two', 'jl'),
        ('two', 'jh'),
        ('two', 'kh'),
        ('two', 'nl'),
        ('two', 'cs'),
        ('two', 'mr'),
        ('two', 'hc'),
        ('lre', 'ss'),
        ('lre', 'hb'),
        ('lre', 'lra'),
        ('lre', 'nl'),
        ('tl', 'pg'),
        ('tl', 'ss'),
        ('tl', 'jk'),
        ('tl', 'ce'), 
        ('tl', 'lre'),
        ('tl', 'two'),
        ('tl', 'kbr'),
        ('tl', 'ca'),
        ('tl', 'zc'),
        ('tl', 'mb'),
        ('tl', 'ie'),
        ('tl', 'eb'),
        ('tl', 'co'),
        ('tl', 'lra'),
        ('tl', 'twi'),
        ('tl', 'js'),
        ('tl', 'sr'),
        ('tl', 'jc'),
        ('tl', 'jl'),
        ('tl', 'jh'),
        ('tl', 'kh'),
        ('tl', 'nl'),
        ('tl', 'cs'),
        ('tl', 'mr'),
        ('tl', 'hc'),
        ('eb', 'jk'),
        ('eb', 'ce'),
        ('ca', 'ss'),
        ('ca', 'mb'),
        ('ca', 'co'),
        ('ca', 'lra'),
        ('ca', 'js'),
        ('ca', 'tl'),
        ('ca', 'jc'),
        ('ca', 'jh'),
        ('ca', 'kh'),
        ('ca', 'nl'),
        ('ca', 'cs'),
        ('ca', 'hc'),
        ('mr', 'pg'),
        ('mr', 'ss'),
        ('mr', 'jk'),
        ('mr', 'hb'),
        ('mr', 'ce'), 
        ('mr', 'lre'),
        ('mr', 'two'),
        ('mr', 'kbr'),
        ('mr', 'ca'),
        ('mr', 'zc'),
        ('mr', 'mb'),
        ('mr', 'ie'),
        ('mr', 'eb'),
        ('mr', 'co'),
        ('mr', 'lra'),
        ('mr', 'gb'),
        ('mr', 'mq'),
        ('mr', 'js'),
        ('mr', 'tl'),
        ('mr', 'sr'),
        ('mr', 'jc'),
        ('mr', 'jl'),
        ('mr', 'jh'),
        ('mr', 'kh'),
        ('mr', 'nl'),
        ('mr', 'hc'),
        ('js', 'ca'),
        ('js', 'twi'),
        ('js', 'cs'),
        ('js', 'mr'),
        ('hb', 'pg'),
        ('hb', 'jk'),
        ('hb', 'ce'), 
        ('hb', 'lre'),
        ('hb', 'two'),
        ('hb', 'kbr'),
        ('hb', 'zc'),
        ('hb', 'ie'),
        ('hb', 'eb'),
        ('hb', 'co'),
        ('hb', 'lra'),
        ('hb', 'gb'),
        ('hb', 'twi'),
        ('hb', 'js'),
        ('hb', 'tl'),
        ('hb', 'sr'),
        ('hb', 'jc'),
        ('hb', 'jl'),
        ('hb', 'jh'),
        ('hb', 'kh'),
        ('hb', 'nl'),
        ('hb', 'cs'),
        ('hb', 'hc'),
        ('ss', 'pg'),
        ('ss', 'jk'),
        ('ss', 'ce'),
        ('ss', 'lre'),
        ('ss', 'two'),
        ('ss', 'jd'),
        ('ss', 'kbr'),
        ('ss', 'ca'),
        ('ss', 'zc'),
        ('ss', 'ie'),
        ('ss', 'eb'),
        ('ss', 'lra'),
        ('ss', 'gb'),
        ('ss', 'mq'),
        ('ss', 'twi'),
        ('ss', 'js'),
        ('ss', 'js'),
        ('ss', 'tl'),
        ('ss', 'sr'),
        ('ss', 'jc'),
        ('ss', 'jl'),
        ('ss', 'kh'),
        ('ss', 'cs'),
        ('ss', 'hc'),
        ('hc', 'ca'),
        ('hc', 'mb'),
        ('hc', 'tl'),
        ('hc', 'jc'),
        ('hc', 'cs'),
        ('co', 'ca'),
        ('co', 'jc'),
        ('co', 'jl'),
        ('zc', 'pg'),
        ('zc', 'ss'),
        ('zc', 'jk'),
        ('zc', 'hb'),
        ('zc', 'ce'), 
        ('zc', 'lre'),
        ('zc', 'two'),
        ('zc', 'kbr'),
        ('zc', 'ca'),
        ('zc', 'mb'),
        ('zc', 'ie'),
        ('zc', 'eb'),
        ('zc', 'co'),
        ('zc', 'lra'),
        ('zc', 'gb'),
        ('zc', 'mq'),
        ('zc', 'twi'),
        ('zc', 'js'),
        ('zc', 'tl'),
        ('zc', 'sr'),
        ('zc', 'jc'),
        ('zc', 'jl'),
        ('zc', 'jh'),
        ('zc', 'kh'),
        ('zc', 'nl'),
        ('zc', 'cs'),
        ('zc', 'mr'),
        ('zc', 'hc'),
        ('mq', 'jk'),
        ('mq', 'jd'),
        ('mq', 'kbr'),
        ('mq', 'twi'),
        ('mq', 'jc'),

        ('mb', 'pg'),
        ('mb', 'ss'),
        ('mb', 'jk'),
        ('mb', 'hb'),
        ('mb', 'ce'), 
        ('mb', 'lre'),
        ('mb', 'two'),
        ('mb', 'kbr'),
        ('mb', 'zc'),
        ('mb', 'ie'),
        ('mb', 'eb'),
        ('mb', 'lra'),
        ('mb', 'gb'),
        ('mb', 'mq'),
        ('mb', 'twi'),
        ('mb', 'tl'),
        ('mb', 'sr'),
        ('mb', 'jc'),
        ('mb', 'jl'),
        ('mb', 'jh'),
        ('mb', 'kh'),
        ('mb', 'nl'),
        ('mb', 'cs'),
        ('mb', 'hc')
    )
]


modifiedDataAlready = [
    {'data': {'source': source, 'target': target}, }
    for source, target in (
        ('co', 'hc'),
        ('co', 'lra'),
        ('co', 'mb'),
        ('cs', 'mb'),
        ('cs', 'mr'),
        ('ca', 'hb'),
        ('ca', 'mb'),
        ('ca', 'mq'),
        ('hb', 'mq'),
        ('hb', 'ss'),
        ('ie', 'lra'),
        ('jd', 'lre'),
        ('js', 'mq'),
        ('lra', 'mq'),
        ('mr', 'twi'),
        ('mq', 'tl'),
        ('pg', 'co'),
        ('pg', 'cs'),
        ('pg', 'ie'),
        ('gb', 'tl'),
        ('jh', 'mq'),
        ('jh', 'ss'),
        ('kh', 'lre'),
        ('kh', 'mq'),
        ('nl', 'mq'),
        ('nl', 'ss'),
    )
]

modifiedDataNewly = [
    {'data': {'source': source, 'target': target}, }
    for source, target in (
        ('co', 'ca'),
        ('co', 'jc'),
        ('co', 'jl'),
        ('co', 'js'),
        ('co', 'ss'),
        ('cs', 'ca'),
        ('cs', 'hc'),
        ('cs', 'hb'),
        ('cs', 'js'),
        ('co', 'twi'),
        ('ca', 'hc'),
        ('ca', 'jc'),
        ('ca', 'js'),
        ('ca', 'lra'),
        ('ca', 'ss'),
        ('ca', 'tl'),
        ('eb', 'jk'),
        ('hc', 'jc'),
        ('hc', 'js'),
        ('hc', 'lra'),
        ('hc', 'mb'),
        ('hc', 'twi'),
        ('hb', 'js'),
        ('hb', 'lre'),
        ('hb', 'lra'),
        ('hb', 'mb'),
        ('hb', 'mr'),
        ('hb', 'tl'),
        ('jc', 'jl'),
        ('jc', 'jd'),
        ('jc', 'kbr'),
        ('jc', 'mq'),
        ('jl', 'jd'),
        ('jl', 'mb'),
        ('jl', 'twi'),
        ('jd', 'mq'),
        ('js', 'lra'),
        ('js', 'mb'),
        ('js', 'mr'),
        ('js', 'ss'),
        ('js', 'twi'),
        ('kbr', 'mq'),
        ('kbr', 'tl'),
        ('lre', 'lra'),
        ('lre', 'ss'),
        ('mb', 'ss'),
        ('mr', 'ss'),
        ('mq', 'ss'),
        ('pg', 'lra'),
        ('ce', 'eb'),
        ('ce', 'jk'),
        ('jh', 'ca'),
        ('jh', 'hb'),
        ('jh', 'mr'),
        ('jh', 'zc'),
        ('kh', 'ca'),
        ('kh', 'jc'),
        ('kh', 'jl'),
        ('kh', 'lra'),
        ('kh', 'twi'),
        ('nl', 'ca'),
        ('nl', 'hb'),
        ('nl', 'lre'),
        ('nl', 'lra')

    )
]

rawDataNewlyElements = nodes + rawDataNewly
rawDataAlreadyElements = nodes + rawDataAlready
modifiedDataNewlyElements = nodes + modifiedDataNewly
modifiedDataAlreadyElements = nodes + modifiedDataAlready




app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Project 3 Possible Template'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1', children=[
        dcc.Tab(label='Modfied Data Graphs', value='tab-1'),
        dcc.Tab(label='tab2', value='tab-2'),
        dcc.Tab(label='Raw Data Graphs', value='tab-3'),
        dcc.Tab(label='About', value='tab-4'),


    ]),
    html.Div(id='tabs-content-example-graph')
])

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Newly Acquainted Network (Modified Data)', style={'text-align': 'center', 'color': '#E58F13'}),
            html.P('This network depicts the total number of connections after the start of ICS390.', style={'text-align': 'center', 'color': '#E58F13'}),
            dbc.Row(
            [
                dbc.Container(cyto.Cytoscape(
                    id='cytoscape-layout-1',
                    # interactivity here elements 1 or 2
                    elements=modifiedDataNewlyElements,
                    style={'width': '100%', 'height': '1000px'},
                    layout={
                    'name': 'circle' 
                }
            )),
            ] ),  
            html.H3('Previously Acquainted Network (Modified Data)', style={'text-align': 'center', 'color': '#E58F13'}),
            html.P('This network depicts the total number of connections before the start of ICS390.', style={'text-align': 'center', 'color': '#E58F13'}),            dbc.Row(
            [
                dbc.Container(cyto.Cytoscape(
                    id='cytoscape-layout-1',
                    # interactivity here elements 1 or 2
                    elements=modifiedDataAlreadyElements,
                    style={'width': '100%', 'height': '600px'},
                    layout={
                    'name': 'grid' 
                }
            )),
            ] ),       
            
        ], style={"border":"2px black solid"})
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab 2 placeholder'),
            
            
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Newly Accquainted Graph Raw Data'),
            dbc.Row(
            [
                dbc.Container(cyto.Cytoscape(
                    id='cytoscape-layout-1',
                    # interactivity here elements 1 or 2
                    elements=rawDataNewlyElements,
                    style={'width': '100%', 'height': '2000px'},
                    layout={
                    'name': 'spread' 
                }
            )),
            ] ),  
            html.H3('Already Accquainted Graph Raw Data'),
            dbc.Row(
            [
                dbc.Container(cyto.Cytoscape(
                    id='cytoscape-layout-1',
                    # interactivity here elements 1 or 2
                    elements=rawDataAlreadyElements,
                    style={'width': '100%', 'height': '350px'},
                    layout={
                    'name': 'spread' 
                }
            )),
            ] ),       
        ])
    elif tab == 'tab-4':
        return html.Div([
            dcc.Markdown(
                '''

                > ### Data visualization by:
                >
                > - Cole Amparo
                > - Justin Honda
                > - Mujtaba (Abdullah) Quadri

                ---
                ### Sources

                ---

                > ### Tools used for Visualization: 
                >
                > - [Plotly](https://plotly.com/?_gl=1*54kric*_ga*MTUwMDA3NDI3Ni4xNjYzMjMwNTI5*_ga_6G7EE0JNSC*MTY2MzI4OTQ5NC4yLjEuMTY2MzMwNjc1NC4wLjAuMA/), 
                > - [Dash](https://plotly.com/dash/), 
                '''
            )
        ], style= {'width': '100%', 'height': '1000px', 'margin-top': '10', 'margin-left' : '80', 'font-size':'20px'})

        
if __name__ == '__main__':
    app.run_server(debug=True)