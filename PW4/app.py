import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.long_callback import DiskcacheLongCallbackManager

#figure template also uses lux:
load_figure_template('LUX')

#import diskcache
#cache = diskcache.Cache("./cache")
#long_callback_manager = DiskcacheLongCallbackManager(cache)

#initializing the app:
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX,dbc.icons.BOOTSTRAP])
server = app.server
#, long_callback_manager=long_callback_manager