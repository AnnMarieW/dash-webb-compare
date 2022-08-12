"""
This is an example of a multi-page app made with `pages` that does not use the pages folder.

"""

import dash
from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
from dash_before_after import BeforeAfter
from whitenoise import WhiteNoise


deep_field = "https://user-images.githubusercontent.com/72614349/179115661-f8de6e4c-0dca-4628-ab67-3d525f5ac049.jpg"
stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115662-32d348da-fa8b-481d-b4fc-9f7414f49de0.jpg"
webb_stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115663-71578706-1ab5-45a5-b809-812c7c3028a7.jpg"
carina = "https://user-images.githubusercontent.com/72614349/179115665-9800b45c-e1dc-4aa7-8b34-885d48c61221.png"
southern_nebula = "https://user-images.githubusercontent.com/72614349/179115666-fdd204fc-e33d-4524-9ba5-a2611740f8a7.jpg"
webb_deep_field = "https://user-images.githubusercontent.com/72614349/179115668-2630e3e4-3a9f-4c88-9494-3412e606450a.jpg"
webb_southern_nebula = "https://user-images.githubusercontent.com/72614349/179115670-ef5bc561-d957-4e88-82dc-53ca53541b04.jpg"
webb_carina = "https://user-images.githubusercontent.com/72614349/179115673-15eaccb9-d17d-4667-84fb-e0a46fd444e8.jpg"


app = Dash(
    __name__,
    use_pages=True,
    pages_folder="",
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="assets/")


def make_before_after(before, after):
    return html.Div(
        [
            html.Div(
                [html.Div("Hubble"), html.Div("Webb")],
                className="d-flex justify-content-between",
                style={"width": "auto"},
                id="label_div"
            ),
            BeforeAfter(before=before, after=after, id="before_after"),
        ],
        style={"marginTop": 50},
    )


descr = "James Webb Space Telescope. Compare before and after images of Hubble vs Webb.  Make an app like this with ~40 lines of Python using Plotly Dash."

dash.register_page(
    "webb_stephans_quintet",
    name="Stephans Quintet",
    description=descr,
    image="webb_stephans_quintet_350.jpg",
    layout=make_before_after(
        #"/assets/stephans_quintet.jpg", "/assets/webb_stephans_quintet.jpg"
        stephans_quintet, webb_stephans_quintet

    ),
)

dash.register_page(
    "webb_deep_field",
    name="Galaxy Cluster SMACS 0723",
    description=descr,
    image="deep_field_meta.gif",
    layout=make_before_after(
       # "/assets/deep_field.jpg", "/assets/webb_deep_field.jpg"
        deep_field, webb_deep_field
    ),
    path="/",
)

dash.register_page(
    "webb_carina",
    name="Carina Nebula",
    description=descr,
    image="webb_carina_350.jpg",
    layout=make_before_after(
      #  "/assets/carina.png", "/assets/webb_carina.jpg"
        carina, webb_carina
    ),
)
dash.register_page(
    "webb_southern_ring",
    name="Southern Ring Nebula",
    description=descr,
    image="webb_southern_nebula_350.jpg",
    layout=make_before_after(
     #   "/assets/southern_nebula.jpg", "/assets/webb_southern_nebula.jpg"
        southern_nebula, webb_southern_nebula
    ),
)

dash.register_page(
    "cartwheel",
    name="Cartwheel Gallery",
    description=descr,
    image="webb_cartwheel_350.jpg",
    layout=make_before_after("/assets/cartwheel.png", "/assets/webb_cartwheel.png"),
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

app.layout = dbc.Container([header, navbar(), dash.page_container, dcc.Location(id="url")], style={"max-width": 1000})

if __name__ == "__main__":
    app.run_server(debug=True)
