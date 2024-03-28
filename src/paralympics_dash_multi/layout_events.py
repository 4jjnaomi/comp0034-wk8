""" Contains variables for all the rows and elements in the 'charts' page """
import dash_bootstrap_components as dbc
from dash import html, dcc, get_asset_url
from paralympics_dash_multi.figures import scatter_geo, get_event_data

# Create the scatter map
map = scatter_geo()

row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Event Details"), html.P(
            "Event details. Select a marker on the map to display the event highlights and summary data.")
                 ], width=12),
    ]),
)

row_two = html.Div(
    dbc.Row([
        dbc.Col(children=[
            # Chart replaced the placeholder image
            dcc.Graph(figure=map, id="geo-map"),
        ], width=8),
        dbc.Col(children=[
        html.Br(),
        html.Div(id='card'),
        ], width=4),
    ], align="start")
)
