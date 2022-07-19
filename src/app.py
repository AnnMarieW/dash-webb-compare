"""
This is an example of a multi-page app made with `pages` that does not use the pages folder.

"""

import dash
from dash import Dash, dcc, html, Output, Input
from dash_extensions import BeforeAfter
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    pages_folder="",
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server


def make_before_after(before, after):
    return html.Div(
        [
            html.Div(
                [html.Div("Hubble"), html.Div("Webb")],
                className="d-flex justify-content-between",
                style={"width": 1000},
                id="label_div"
            ),
            BeforeAfter(before=before, after=after, height=800, width=1000, id="before_after"),
        ],
        style={"marginTop": 50},
    )


descr = "James Webb Space Telescope. Compare before and after images of Hubble vs Webb.  Make an app like this with ~40 lines of Python using Plotly Dash."

dash.register_page(
    "webb_stephans_quintet",
    name="Stephans Quintet",
    description=descr,
    image="stephans_quintet_350.jpg",
    layout=make_before_after(
        "/assets/webb_stephans_quintet.jpg", "/assets/stephans_quintet.jpg"
    ),
)

dash.register_page(
    "webb_deep_field",
    name="Galaxy Cluster SMACS 0723",
    description=descr,
    image="deep_field_meta.gif",
    layout=make_before_after("/assets/webb_deep_field.jpg", "/assets/deep_field.jpg"),
    path="/",
)

dash.register_page(
    "webb_carina",
    name="Carina Nebula",
    description=descr,
    image="carina_350.jpg",
    layout=make_before_after("/assets/webb_carina.jpg", "/assets/carina.png"),
)
dash.register_page(
    "webb_southern_ring",
    name="Southern Ring Nebula",
    description=descr,
    image="southern_nebula_350.jpg",
    layout=make_before_after(
        "/assets/webb_southern_nebula.jpg", "/assets/southern_nebula.jpg"
    ),
)

header = html.Div(
    [
        html.H2("James Webb Space Telescope", className="display-3"),
        html.Div("First Images.  Compare before and after images of Hubble vs Webb."),
        dbc.Button(
            [html.I(className="bi bi-book me-2"), "webbtelescope.org"],
            color="light", className="text-white-50",
            href="https://webbtelescope.org/news/first-images/gallery",

        ),
        dbc.Button(
            [html.I(className="bi bi-github me-2"), "source code"],
            color="light", className="ms-2 text-white-50",
            href="https://github.com/AnnMarieW/webb-compare",
            title="Make an app like this with ~40 lines of Python using Plotly Dash"
        ),
    ],
)


def navbar():
    return dbc.Nav(
        [
            dbc.NavLink(
                html.Div(page["name"], className="ms-2"),
                href=page["path"],
                active="exact",
            )
            for page in dash.page_registry.values()
        ],
        pills=True,
        className="mt-5",
    )

app.layout = dbc.Container([header, navbar(), dash.page_container, dcc.Location(id="url")])


app.clientside_callback(
    """
        function(href) {
            if (window.innerWidth < 750) {
                return [500, 500]
            }
            return [1000, 800]
        }
    """,
    Output('before_after', "width"),
    Output('before_after', "height"),
    Input('url', 'href')
)





app.clientside_callback(
    """
        function(href) {
            if (window.innerWidth < 750) {                
                return {"width":500}
            }
             return {"width":1000}
        }
    """,
    Output('label_div', "style"),
    Input('url', 'href') 
)

if __name__ == "__main__":
    app.run_server(debug=True)
