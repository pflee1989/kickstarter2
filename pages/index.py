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
        
            ### Reachable Success?

            You may want to know how to get most sponsors. However, some projects do not attract investors. 
            
            
            The law of supply and demand always works, but you need to know how to work this reality to your advantage. 
            
            
            Let's find out. 

                         
            """
        ),
       
        
        
        dcc.Link(dbc.Button('Predict Your Success!', color='primary'), href='/Predictions')
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