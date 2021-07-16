import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import test_page1, test_page2, home_page, test_page3

from dash_extensions import Lottie
import dash_bootstrap_components as dbc

B = "https://assets2.lottiefiles.com/packages/lf20_Pth0RM.json"
B1 = "https://assets1.lottiefiles.com/packages/lf20_ffpacwo2.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# styling the sidebar
SIDEBAR_STYLE = {
    "background-color": "#f8f9fa",
}

# padding for the page content
# CONTENT_STYLE = {
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# }

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/apps/", active="exact"),
                dbc.NavLink("Page 1", href="/apps/Eff_by", active="exact"),
                dbc.NavLink("Page 2", href="/apps/rate_by", active="exact"),
                dbc.NavLink("Page 3", href="/apps/map", active="exact"),
                dbc.DropdownMenu(
                    [dbc.DropdownMenuItem(dbc.NavLink("Page 1", href="/apps/Eff_by", active="exact"),),
                     dbc.DropdownMenuItem("Item 2")],
                    label="Dropdown",
                    nav=True,
                ),
            ],
            vertical=False,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H2("Rate by year"),
        html.Img(src="/assets/A.png")
    ], className="banner"),
    html.Div(sidebar),
    html.Div(id='page-content', children=[]),

],className="body")


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/Eff_by':
        return test_page1.layout
    if pathname == '/apps/rate_by':
        return test_page2.layout
    if pathname == '/apps/map':
        return test_page3.layout
    else:
        return home_page.layout




if __name__ == '__main__':
    app.run_server(debug=True,port=8051)

