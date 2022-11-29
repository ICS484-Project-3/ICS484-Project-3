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
        ('la', 'Combo'),
        ('nyc', 'Mike Ehrmantrout'),
        ('to', 'Jesse Pinkman'),
        ('mtl', 'Gustavo Fring'),
        ('van', 'Hank Schraeder'),
        ('chi', 'Skinny P'),
        ('bos', 'Walter White'),
        ('hou', 'Badger')
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
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

elements = nodes + edges



app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Project 3 Possible Template'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1', children=[
        dcc.Tab(label='tab1', value='tab-1'),
        dcc.Tab(label='tab2', value='tab-2'),
        dcc.Tab(label='tab3', value='tab-3'),
        dcc.Tab(label='tab4', value='tab-4'),


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
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'cose' #grid 
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

                Data visualization by Cole Amparo, Justin Honda and Mujtaba Quadri 

                ---
                ## Sources

                ---

                Tools used for Visualization: 

                [Plotly](https://plotly.com/?_gl=1*54kric*_ga*MTUwMDA3NDI3Ni4xNjYzMjMwNTI5*_ga_6G7EE0JNSC*MTY2MzI4OTQ5NC4yLjEuMTY2MzMwNjc1NC4wLjAuMA/), 
                [Dash](https://plotly.com/dash/), 
                '''
            )
        ], style= {'width': '100%', 'height': '1000px', 'margin-top': '10', 'margin-left' : '80', 'font-size':'20px'})

        
if __name__ == '__main__':
    app.run_server(debug=True)