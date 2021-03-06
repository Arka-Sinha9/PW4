#from typing_extensions import Required
from dash import html
from app import app


home_layout = html.Div(children=[
    html.H1("Classification of imbalanced dataset",style={'text-align':'center'}),
    html.P("An imbalanced classification problem is an example of a classification problem where the distribution of examples across the known classes is biased or skewed. The distribution can vary from a slight bias to a severe imbalance where there is one example in the minority class for hundreds, thousands, or millions of examples in the majority class or classes.Imbalanced classifications pose a challenge for predictive modeling as most of the machine learning algorithms used for classification were designed around the assumption of an equal number of examples for each class. This results in models that have poor predictive performance, specifically for the minority class. This is a problem because typically, the minority class is more important and therefore the problem is more sensitive to classification errors for the minority class than the majority class."),
    html.Img(src="https://datascience.aero/wp-content/themes/yootheme/cache/imbalancedata-6e7d6903.png",style={'height':'400px','width':'500px','margin-left':'300px'})
])


