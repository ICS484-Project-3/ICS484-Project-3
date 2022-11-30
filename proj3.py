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
        ('js', 'John Suelen'),
        ('hb', 'Henry Blazier'),
        ('ss', 'Shane Severino'),
        ('hc', 'Hansen Cabanero'),
        ('co', 'Chad Oshiro'),
        ('zc', 'Zachary Chaikin'),
        ('mq', 'Mujtaba Quadri'),
        ('mb', 'Marcos Buccat'),
        ('jh', 'Justin Honda')
    )
]

already = [
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
        ('cs', 'tw'),
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
        ('mr', 'tw'),
        ('mr', 'cs'),
        ('js', 'ss'),
        ('js', 'mb'),
        ('js', 'co'),
        ('js', 'lr'),
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

newly = [
    {'data': {'source': source, 'target': target}, }
    for source, target in (
        ('van', 'la'),
        ('la', 'chi'),
        ('hou', 'chi'),
        ('to', 'mtl'),
        ('mtl', 'bos'),
        ('nyc', 'bos'),
        ('to', 'hou'),
        ('to', 'chi'),
        ('to', 'nyc'),
        ('la', 'nyc'),
        ('nyc', 'bos')
    )
]

# edge2...

elements = nodes + edges
# elements2 = nodes + edges2



app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Project 3 Possible Template'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1', children=[
        dcc.Tab(label='tab1', value='tab-1'),
        dcc.Tab(label='tab2', value='tab-2'),
        dcc.Tab(label='tab3', value='tab-3'),
        dcc.Tab(label='About', value='tab-4'),


    ]),
    html.Div(id='tabs-content-example-graph')
])

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Sample Network Graph '),
            dbc.Row(
            [
                dbc.Container(cyto.Cytoscape(
                    id='cytoscape-layout-1',
                    # interactivity here elements 1 or 2
                    elements=elements,
                    style={'width': '100%', 'height': '350px'},
                    layout={
                    'name': 'cose' 
                }
            )),
            ] ),  
            
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab 2 placeholder'),
            
            
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab 3 placeholder'),

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