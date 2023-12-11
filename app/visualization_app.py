import pandas as pd
from dash import Dash, dcc, html, Input, Output, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
import plotly.express as px
import plotly.graph_objects as go
import ipywidgets as widgets

# this should be changed before deployment to reflect path of the .pkl file
df = pd.read_pickle("../data/processed/historical_outbreaks_df.pkl")

app = JupyterDash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.COSMO])

sidebar_style = {      # this code is modified from a template from https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

content_style = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
welcome_style = {
    "text-align": "center",
    "margin-top": "16rem",
}

welcome_text_1 = """
Welcome to our Dash app! We're Team 23. Here you'll find the visualizations
we created for our capstone project that accompany our
"""
report_link = html.A(
    "final report",
    href="https://docs.google.com/document/d/1bIR_jaLaYRx6avVsLmQFBOuRI_6dxSKENzd0DeKN0oE/edit",
    target="_blank")

welcome_text_2 = """
. We used Demographic and
Health Surveys data to train a model that predicts the likelihood of an outbreak of a zoonotic
disease for a given country. We also mapped the history of major outbreaks and created visualizations of our 
findings that you can explore by navigating the menu on the left.
For more information about our project, check out our GitHub repository here:
"""

github_link = html.A(
    "https://github.com/alevine5/MADS-Capstone",
    href="https://github.com/alevine5/MADS-Capstone",
    target="_blank")

sidebar = html.Div(
    [
        html.H2("Menu", className="display-5"),
        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink("Welcome", href="/", active="exact"),
                dbc.NavLink("Risk Score Analysis", href="/page-1", active="exact"),
                dbc.NavLink("Historical Outbreaks", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=sidebar_style,
)


content = html.Div(
    style=content_style,
    id="page-content",
    children=[
    dcc.Loading(dcc.Graph(id="graph"), type="cube"),
    ]
)

welcome = html.Div(style=welcome_style, children=[
        html.H1("Predicting Zoonotic Disease Outbreaks"),
        html.H2("By Alex Levine and Samuel Buxton"),
        html.P([welcome_text_1, report_link, welcome_text_2, github_link]),
        html.Div([
            html.A("Risk Score Analysis", href="/page-1", style={'margin-right': '20px'}),
            html.A("Historical Outbreaks", href="/page-2")
        ])
    ])

page_1 = html.Div([
    html.H4("Visual coming soon!"),
])

page_2 = html.Div([
    html.H4("Historical Outbreaks"),
    html.P("Select year range:"),
    dcc.RangeSlider(
        id="year-slider",
        marks={i: str(i) for i in range(-1800, 2011, 200)},
        min=-1800,
        max=2010,
        step=1,
        value=[1800, 2010],
    ),
    
    html.Div([
        dcc.Dropdown(
            id="country-dropdown",
            options=[
                {'label': 'Country Name', 'value': 'Name'},
                {'label': 'ISO-3', 'value': 'ISO-3'}
            ],
            value='Name',
            placeholder='Country Name',
            style={'width': '120px', 'display': 'inline-block'}
        ),
    ], style={'display': 'inline-block', 'margin-right': '20px', 'margin-top':'20px'}),
    
    html.Div([
        dcc.Dropdown(
            id="speed-dropdown",
            options=[
                {'label': '.25x', 'value': 125},
                {'label': '.5x', 'value': 250},
                {'label': '.75x', 'value': 375},
                {'label': '1x', 'value': 500},
                {'label': '1.5x', 'value': 750},
                {'label': '2x', 'value': 1000},
                {'label': '3x', 'value': 1500},
                {'label': '5x', 'value': 2500}
            ],
            value=500, 
            placeholder="1x",
            style={'width': '50px', 'display': 'inline-block'}
        ),
    ], style={'display': 'inline-block', 'margin-right': '20px'}),
    
    html.Div([
        dcc.Dropdown(
            id="pastyears-dropdown",
            options=[
                {'label': '0', 'value': 0},
                {'label': '10', 'value': 10},
                {'label': '20', 'value': 20},
                {'label': '30', 'value': 30},
                {'label': '40', 'value': 40},
                {'label': 'Past Years: 50', 'value': 50},
            ],
            value=50, 
            placeholder="Past Years",
            style={'width': '120px', 'display': 'inline-block'}
        ),
    ], style={'display': 'inline-block', 'margin-right': '20px'}),
    
    html.Div([
        html.Button(
            'Generate',
            id='generate-button',
            n_clicks=0,
            style={'display': 'inline-block'}
        ),
    ], style={'align-items': 'center',}),
    
    dcc.Loading(dcc.Graph(id="graph"), type="cube"),
])


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def select_page(pathname):
    if pathname == "/":
        return welcome
    elif pathname == "/page-1":
        return page_1
    elif pathname == "/page-2":
        return page_2
    
@app.callback(
    Output("graph", "figure"), 
    Input("year-slider", "value"),
    Input("country-dropdown", "value"),
    Input("speed-dropdown", "value"),
    Input("pastyears-dropdown", "value"),
    Input("generate-button", "n_clicks"),
)

def update_graph(years, name, duration, past, clicks):
    if ctx.triggered_id and "generate-button" != ctx.triggered_id:
        raise PreventUpdate
    return generate_historical_viz(
        df,
        start=years[0],
        end=years[1],
        country_name=name,
        duration=duration,
        past_years=past
    )
        
    
if __name__ == "__main__":
    app.run_server(mode='external')
