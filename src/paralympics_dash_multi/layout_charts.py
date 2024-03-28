""" Contains variables for all the rows and elements in the 'charts' page """
import dash_bootstrap_components as dbc
from dash import Input, Output, html, dcc
from paralympics_dash_multi.figures import line_chart, bar_gender_faceted

# Create the Plotly Express line chart object, e.g. to show number of sports
line = line_chart("sports")

# Create the Plotly Express stacked bar chart object to show gender split of participants for the type of event
bar = bar_gender_faceted(["winter"])

line_chart_dropdown = dbc.Select(
    id="type-dropdown",  # id uniquely identifies the element, will be needed later
    options=[
        {"label": "Events", "value": "events"},
        # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events"  # The default selection
)

type_checklist = dbc.Checklist(
    options=[
        {"label": "Summer", "value": "summer"},
        {"label": "Winter", "value": "winter"},
    ],
    value=["summer"],  # Values is a list as you can select both winter and summer
    id="checklist-input",
)

row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Charts"), html.P(
            "Try to answer the questions using the charts below.")
                 ], width=12),
    ]),
)

row_two = html.Div(
    dbc.Row([
        dbc.Col(children=[
            line_chart_dropdown
        ], width=2),
        dbc.Col(children=[
            # Chart replaced the placeholder image
            dcc.Graph(figure=line, id="line-chart"),
        ], width=4),
        dbc.Col(children=[
            type_checklist,
        ], width=2),
        dbc.Col(children=[
            # Chart replaced the placeholder image
            dcc.Graph(figure=bar, id="bar-chart"),
        ], width=4),
    ], align="start")
)
