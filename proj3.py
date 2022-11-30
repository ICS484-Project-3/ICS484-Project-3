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
        ('jd', 'pg'),
        ('jd', 'ss'),
        ('jd', 'jk'),
        ('jd', 'hb'),
        ('jd', 'ce'), 
        ('jd', 'lre'),
        ('jd', 'two'),
        ('jd', 'kbe'),
        ('jd', 'ca'),
        ('jd', 'zc'),
        ('jd', 'mb'),
        ('jd', 'ie'),
        ('jd', 'eb'),
        ('jd', 'co'),
        ('jd', 'lr'),
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
        ('kbe', 'tl'),
        ('kbe', 'jc'),
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
        ('lr', 'pg'),
        ('lr', 'hb'),
        ('lr', 'ca'),
        ('lr', 'kh'),
        ('lr', 'nl'),
        ('cs', 'ss'),
        ('cs', 'jk'),
        ('cs', 'hb'),
        ('cs', 'ce'), 
        ('cs', 'lre'),
        ('cs', 'two'),
        ('cs', 'kbe'),
        ('cs', 'zc'),
        ('cs', 'ie'),
        ('cs', 'eb'),
        ('cs', 'co'),
        ('cs', 'lr'),
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
        ('two', 'kbe'),
        ('two', 'ca'),
        ('two', 'zc'),
        ('two', 'mb'),
        ('two', 'ie'),
        ('two', 'eb'),
        ('two', 'co'),
        ('two', 'lr'),
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
        ('lre', 'lr'),
        ('lre', 'nl'),
        ('tl', 'pg'),
        ('tl', 'ss'),
        ('tl', 'jk'),
        ('tl', 'ce'), 
        ('tl', 'lre'),
        ('tl', 'two'),
        ('tl', 'kbe'),
        ('tl', 'ca'),
        ('tl', 'zc'),
        ('tl', 'mb'),
        ('tl', 'ie'),
        ('tl', 'eb'),
        ('tl', 'co'),
        ('tl', 'lr'),
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
        ('ca', 'lr'),
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
        ('mr', 'kbe'),
        ('mr', 'ca'),
        ('mr', 'zc'),
        ('mr', 'mb'),
        ('mr', 'ie'),
        ('mr', 'eb'),
        ('mr', 'co'),
        ('mr', 'lr'),
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
        ('hb', 'kbe'),
        ('hb', 'zc'),
        ('hb', 'ie'),
        ('hb', 'eb'),
        ('hb', 'co'),
        ('hb', 'lr'),
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
        ('ss', 'lr'),
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