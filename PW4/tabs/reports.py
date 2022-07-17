import dash
import plotly.express as px
import pandas as pd
from app import app
from dash import dcc, Output, Input, html
import dash_bootstrap_components as dbc    
import os,flask
import plotly
import plotly.graph_objects as go
from preprocessing import arka_preprocessing

df=arka_preprocessing.get_dataframe()

#layout of the reports tab:
reports_layout = ([
        html.Div([
            #html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id="dropdown",
                options=[
                    {'label':'oversampling','value':'oversampling'},
                    {'label':'undersampling','value':'undersampling'},
                ],
                value='oversampling',
                multi=False,
                clearable=False,
                style={'width':'50%'}
            ),
        ]),
        html.Div([
            dcc.Graph(id='bar_graph')
        ])
])


@app.callback(
    Output('bar_graph','figure'),
    [Input('dropdown','value')]
)


def update_bar_graph(dropdown):
    dff=df
    if dropdown=="oversampling":
        barchart=px.bar(
            data_frame=dff,
            x=["oversampling","combination"],
            y=['F1 score'],
            barmode='group'
        )
        barchart.update_layout(xaxis_title="F1 Score",yaxis_title="Type")

        return barchart
    if dropdown=="undersampling":
        barchart=px.bar(
            data_frame=dff,
            x=["undersampling","combination"],
            y=['F1 score'],
            barmode='group'
        )
        barchart.update_layout(xaxis_title="F1 score",yaxis_title="Type")

        return barchart
