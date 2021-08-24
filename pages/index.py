# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Not All Plans Succeed in Raising Funds, But Some Do. 

            You May Be Interested to Know Which Plans Get More Pledges and Sponsors, and Which Plans Don't. 
            
            
            We find that the bench-mark for fund-raising does not necessarily make success harder, because the law of supply and demand always works. 
            
            
            Let's find out. 

                         
            """
        ),
       
        
        
        dcc.Link(dbc.Button('Predict Your Possible Success', color='primary'), href='/Predictions')
    ],
    md=5,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
    
    
    ],
md=1,
)

column3 = dbc.Col(
    [
     html.Img(src='assets/ksr.png', className='img-fluid'),

       ],
md=6,
)

layout = dbc.Row([column1,column2, column3])