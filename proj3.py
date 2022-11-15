# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
import networkx as nx


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

G = nx.random_geometric_graph(200, 0.125)

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Template Network Graph',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                #annotations=[ dict(
                  #  text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                   # showarrow=False,
                   # xref="paper", yref="paper",
                   # x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )


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
                dbc.Container([dcc.Graph(
                figure=fig
            )]),
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