import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from tabs import home,reports
from elements import navbar,footer
from app import app


url_content_layout = html.Div(children=[
    navbar.navbar,
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div"),
    #footer.footer
])

app.layout = url_content_layout

app.validation_layout = html.Div([

    url_content_layout,
    home.home_layout,
    reports.reports_layout
])


@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/reports":
        return  reports.reports_layout
    else:
        return home.home_layout

if __name__ == "__main__":
    app.run_server(debug=True)
    