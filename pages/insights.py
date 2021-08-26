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
        
            ## Insights
            
            The picture below demonstrates the important features in our model, a random forest classifier. The graph illustrates the time-tested truth that fund-rasing success is in the number of willing investors. However, the reality is much more intricate. The 4th most important factor, the subcategory, which shows the backers' demands, in reality often makes 
            or break the deal. 
            
            
            In plain English, the classifers detect failures (about 40% of total cases) in a human-like manner, by looking at the obvious. Meanwhile, the sub-categories, which is ranked as the 4th most important feature, is the factor most sensitive to the backers' demand. As analysts and investors, we live with the best tools and their limits. In this case, our
            models thinks like us-- thus, we must look beyond human impulses. After all as in all good investments, honesty is in details, and good projects are highly tailored to specific needs. Let us all judge investments with caution. 
            
            
            
             

            """
        
        ), 
    
    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

    html.Img(src='assets/model_rf_feature_importances_3.png', className='img-fluid')
    
    ],
)



       
layout = dbc.Row([column1])