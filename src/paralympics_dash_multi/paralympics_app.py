import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output
from paralympics_dash_multi.figures import line_chart, bar_gender_faceted, create_card

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap
# components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet variable to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags, use_pages=True)

# From https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Event Details", href=dash.page_registry['pages.events']['path'])),
        dbc.NavItem(dbc.NavLink("Charts", href=dash.page_registry['pages.charts']['path'])),
    ],
    brand="Paralympics Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    # Nav bar
    navbar,
    # Area where the page content is displayed
    dash.page_container
])

@app.callback(
    Output(component_id='line-chart', component_property='figure'),
    Input(component_id='type-dropdown', component_property='value')
)
def update_line_chart(chart_type):
    figure = line_chart(chart_type)
    return figure

@app.callback(
    Output(component_id='bar-chart', component_property='figure'),
    Input(component_id='checklist-input', component_property='value')
)
def update_bar_chart(selected_types):
    figure = bar_gender_faceted(selected_types)
    return figure

@app.callback(
    Output('card', 'children'),
    Input('geo-map', 'hoverData'),
)
def display_card(hover_data):
    if hover_data is not None:
        event_id = hover_data['points'][0]['customdata'][0]
        if event_id is not None:
            return create_card(event_id)

if __name__ == '__main__':
    app.run(debug=True, port=8051)


