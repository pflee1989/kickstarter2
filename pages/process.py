# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            We cleaned a Kickstarter dataset, preserve more than 8000 rows and place the rows into a random forest classifier. The partial dependence graph below
            
            shows the core mechanisms within the model-- only certian projcects succeeded in expanding the circle of early backers into a sphere of sponsors with 
            
            critical mass. The number of backers tend to indicate the likelihood of success for good reasons. We have yet to isolate the impact of each sub-category. 
            
            However, the model fails to highlight the behavioral reality-- subcategories that indicate market/consumer demands. Thus, we only show this colorful graph  
            
            to illustrate the most salient relationship in this project. 

            """
        ),
        html.Img(src='assets/pdp.png', className='img-fluid'),
    ],
    
)

layout = dbc.Row([column1])