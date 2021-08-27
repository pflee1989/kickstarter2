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

            We combined a crosssection of Kickstarter's data from 2015 to 2021, one dataset from the mid year per year, except in 2015 wherein the earliest dataset was for Oct. 
            The end result is a dataset of nearly 10,000 rows after the cleaning. The random forest classifier was the chosen model. After extensive testing, we decided to limit the test range to $55,000.00, which is most meaningful for most startup projects. In addition, we limit the number of backers down to 100 to realisitically simulate the results.
            
            
            However, due to subdependency issues, we cannot produce a partial dependence graph for this project. The partial dependence graph below is from another Kickstarter success project, but the end result was basically identical. Namely, the mathematical relationship between backers_count and pledged amounts should be either similar,
            or even identical.  
            
            
            The graph below shows the core mechanisms within the model-- only certian projcects succeeded in expanding the circle of early backers into a sphere of sponsors with 
            critical mass. The number of backers tend to indicate the likelihood of success for good reasons. We have yet to isolate the impact of each sub-category. However, the model fails to highlight the behavioral reality-- subcategories that indicate market/consumer demands. Thus, we only show this colorful graph to illustrate the most salient relationship in this project. 

            """
        ),
        html.Img(src='assets/pdp.png', className='img-fluid'),
    ],
    
)

layout = dbc.Row([column1])