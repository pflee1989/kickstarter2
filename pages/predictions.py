from joblib import load
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from category_encoders import OrdinalEncoder

# from joblib import load
# pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app
from joblib import load

model = load('assets/model_rf_label')

category_list = ['film & video','art','technology','comics','fashion','crafts','publishing','design','food','theater','music','dance','photography']

# sub_category_list = ['illustration', 'action', 'accessories', 'radio & podcasts',
#        'hardware', 'woodworking', 'product design', 'narrative film',
#        'drinks', 'events', 'cookbooks', 'documentary', 'plays',
#        'footwear', 'mixed media', 'digital art', 'places', 'sculpture',
#        'ready-to-wear', 'shorts', 'webcomics', 'painting',
#        'performance art', 'family', 'anthologies', 'graphic design',
#        'comic books', 'apps', 'software', '3d printing', 'comedy', 'web',
#        'world music', "children's books", 'public art', 'pop', 'diy',
#        'science fiction', 'immersive', 'vegan', 'fiction', 'gadgets',
#        'wearables', 'performances', 'r&b', 'horror', 'experimental',
#        'art books', 'sound', 'festivals', 'conceptual art', 'webseries',
#        'civic design', 'apparel', 'animation', 'printing', 'nonfiction',
#        'poetry', 'graphic novels', 'musical', 'food trucks', 'photobooks',
#        'textiles', 'drama', 'music videos', 'jewelry', 'thrillers',
#        'stationery', 'movie theaters', 'periodicals', 'small batch',
#        'fantasy', 'fine art', 'farms', 'candles', 'television',
#        'installations', 'pottery', 'typography', 'rock',
#        'fabrication tools', 'diy electronics', 'crochet', 'couture',
#        'video art', 'calendars', 'community gardens', 'residencies',
#        'romance', 'bacon', 'academic', 'punk', 'literary journals',
#        'young adult', "farmer's markets", 'flight', 'interactive design',
#        'architecture', 'childrenswear', 'ceramics', 'zines', 'metal',
#        'people', 'space exploration', 'spaces', 'knitting', 'pet fashion',
#        'glass', 'robots', 'toys', 'nature', 'camera equipment',
#        'embroidery', 'makerspaces', 'restaurants', 'weaving',
#        'social practice', 'workshops', 'literary spaces', 'translations',
#        'letterpress', 'quilts']

sub_category_list= [
# 1 Art--Done
[{'label': 'ceramics', 'value': 16},
{'label': 'conceptual art', 'value': 24},
{'label': 'digital art', 'value': 29}, {'label': 'illustration', 'value': 58},
{'label': 'mixed media', 'value': 71}, {'label': 'painting', 'value': 79}, 
{'label': 'performance art', 'value': 81},
{'label': 'public art', 'value': 95}, {'label': 'sculpture', 'value': 107}, 
{'label': 'social practice', 'value': 110},
{'label': 'textiles', 'value': 118}, {'label': 'video art', 'value': 124}],
# 2 Comic
 [{'label': 'anthologies', 'value': 5}, {'label': 'comic books', 'value': 22}, 
  {'label': 'events', 'value': 36}, {'label': 'graphic novels', 'value': 54}, 
  {'label': 'webcomics', 'value': 128}],
# 3 Crafts
 [{'label': 'candles', 'value': 15}, {'label': 'crochet', 'value': 28},
  {'label': 'diy', 'value': 30},  {'label': 'glass', 'value': 52},
  {'label': 'knitting', 'value': 65}, {'label': 'pottery', 'value': 91}, {'label': 'Printing', 'value': 93},
  {'label': 'stationery', 'value': 115}, {'label': 'woodworking', 'value': 130}],
# 4 Dance
 [{'label': 'performances', 'value': 82}, 
  {'label': 'residencies', 'value': 101}, {'label': 'spaces', 'value': 114}, 
  {'label': 'workshops', 'value': 131}],
#  5 Design
 [{'label': 'architecture', 'value': 8}, {'label': 'design', 'value': 4}, 
  {'label': 'graphic design', 'value': 53}, {'label': 'interactive design', 'value': 61}, 
  {'label': 'product design', 'value': 94}, {'label': 'Typography', 'value': 121}],
# 6 Fashion   
[{'label': 'accessories', 'value': 1}, {'label': 'apparel', 'value': 6},
 {'label': 'childrenswear', 'value': 18},
  {'label': 'couture', 'value': 27}, {'label': 'footwear', 'value': 49},
  {'label': 'jewelry', 'value': 63}, {'label': 'Ready-To-Wear', 'value': 100}],
# 7 Films and Videos
 [{'label': 'action', 'value': 2}, {'label': 'animation', 'value': 4},
  {'label': 'comedy', 'value': 21},
  {'label': 'documentary', 'value': 32}, {'label': 'drama', 'value': 33}, 
  {'label': 'experimental', 'value': 37},
  {'label': 'family', 'value': 40}, {'label': 'fantasy', 'value': 41}, 
  {'label': 'festivals', 'value': 44},
  {'label': 'horror', 'value': 57}, 
  {'label': 'movie theaters', 'value': 73},
  {'label': 'music videos', 'value': 74}, {'label': 'narrative film', 'value': 75}, 
  {'label': 'romance', 'value': 105},
  {'label': 'science fiction', 'value': 106}, {'label': 'shorts', 'value': 108}, 
  {'label': 'television', 'value': 117},
  {'label': 'thrillers', 'value': 119}, {'label': 'webseries', 'value': 129}],
 # 7 Food
 [{'label': 'bacon', 'value': 11}, {'label': 'community gardens', 'value': 23}, 
  {'label': 'cookbooks', 'value': 25},
  {'label': 'drinks', 'value': 34}, {'label': 'events', 'value': 36}, 
  {'label': "farmer's markets", 'value': 42},
  {'label': 'farms', 'value': 43}, 
  {'label': 'food trucks', 'value': 48},
  {'label': 'restaurants', 'value': 102}, {'label': 'small batch', 'value': 109}, 
  {'label': 'spaces', 'value': 114},
  {'label': 'vegan', 'value': 122}],
 # 8 Games
 [{'label': 'gaming hardware', 'value': 51}, 
  {'label': 'live games', 'value': 68},
  {'label': 'mobile games', 'value': 72}, {'label': 'playing cards', 'value': 87}, 
  {'label': 'puzzles', 'value': 97},
  {'label': 'tabletop games', 'value': 116}, {'label': 'video games', 'value': 125}],
 #  Journalism
 [ {'label': 'audio', 'value': 10}, 
  {'label': 'photo', 'value': 84},
  {'label': 'print', 'value': 92}, {'label': 'video', 'value': 123}, 
  {'label': 'web', 'value': 127}],
 #  Music
 [{'label': 'blues', 'value': 10}, 
  {'label': 'classical music', 'value': 20},
  {'label': 'comedy', 'value': 21}, {'label': 'country & folk', 'value': 26}, 
  {'label': 'electronic music', 'value': 35},
  {'label': 'faith', 'value': 39}, {'label': 'hip-hop', 'value': 56}, 
  {'label': 'indie rock', 'value': 60},
  {'label': 'jazz', 'value': 62}, {'label': 'kids', 'value': 64}, 
  {'label': 'latin', 'value': 66},
  {'label': 'metal', 'value': 70}, 
  {'label': 'pop', 'value': 90},
  {'label': 'punk', 'value': 96}, {'label': 'r&b', 'value': 98}, 
  {'label': 'rock', 'value': 104},
  {'label': 'world music', 'value': 132}],
 #  Photography
 [{'label': 'animals', 'value': 3}, {'label': 'fine art', 'value': 46}, 
  {'label': 'nature', 'value': 77},
  {'label': 'people', 'value': 80}, {'label': 'photobooks', 'value': 85}, 
  {'label': 'places', 'value': 105}],
 #  Publishing
 [{'label': 'anthologies', 'value': 5}, 
  {'label': 'art books', 'value': 9},
  {'label': 'calendars', 'value': 13}, {'label': "children's books", 'value': 17}, 
  {'label': 'comedy', 'value': 21},
  {'label': 'fiction', 'value': 45}, 
  {'label': 'literary journals', 'value': 67},
  {'label': 'nonfiction', 'value': 78}, 
  {'label': 'periodicals', 'value': 83},
  {'label': 'poetry', 'value': 89}, 
  {'label': 'radio & podcasts', 'value': 99},
  {'label': 'translations', 'value': 120}, {'label': 'young adult', 'value': 133}, 
  {'label': 'zines', 'value': 134}],
 #  Technology
 [{'label': '3d printing', 'value': 0}, {'label': 'apps', 'value': 7}, 
  {'label': 'camera equipment', 'value': 14},
  {'label': 'diy electronics', 'value': 31}, {'label': 'fabrication tools', 'value': 38},
  {'label': 'flight', 'value': 47},
  {'label': 'gadgets', 'value': 50}, {'label': 'hardware', 'value': 55}, 
  {'label': 'makerspaces', 'value': 69},
  {'label': 'robots', 'value': 103}, {'label': 'software', 'value': 111},
  {'label': 'sound', 'value': 112},
  {'label': 'space exploration', 'value': 113},  
  {'label': 'wearables', 'value': 126},
  {'label': 'web', 'value': 127}],
 #  Theater
 [{'label': 'comedy', 'value': 21}, {'label': 'experimental', 'value': 37},
  {'label': 'festivals', 'value': 44},
  {'label': 'immersive', 'value': 59}, {'label': 'musical', 'value': 75},
  {'label': 'plays', 'value': 88},
  {'label': 'spaces', 'value': 114}]]

# {'label': i, 'value': i} for i in category_list
column1 = dbc.Col(
    [
        dcc.Markdown('''###### Category'''),
         dcc.Dropdown(
        id='category-dropdown',
        options=[
                {'label': 'art', 'value': 0},
                {'label': 'comics', 'value': 1},
                {'label': 'crafts', 'value': 2},
                {'label': 'dance', 'value': 3},
                {'label': 'design', 'value': 4},
                {'label': 'fashion', 'value': 5},
                {'label': 'film & video', 'value': 6},
                {'label': 'food', 'value': 7},
                {'label': 'games', 'value': 8},
                {'label': 'journalism', 'value': 9},
                {'label': 'music', 'value': 10},
                {'label': 'photography', 'value': 11},
                {'label': 'publishing', 'value': 12},
                {'label': 'technology', 'value': 13},
                {'label': 'theater', 'value': 14},
        ],
        value=0,
        className='mb-4'), 

        
    #     dcc.Markdown('''###### Sub Category'''),
    #      dcc.Dropdown(
    #     id='sub-category-dropdown',
    #     options=[
    #     {'label': i, 'value': i} for i in sub_category_list
    #    ],
    #     value='diy',
    #     className='mb-4'), 

        dcc.Markdown('#### What is the sub-category?'), 
        dcc.Dropdown(
            id='sub-category-dropdown',
            className='mb-5',
        value=0
        ), 



        dcc.Markdown('''###### Goal (USD)'''),
        dcc.Slider(
            id='goal-slider',
            min=0,
            max=2000000,
            step=50000,
            value=1000,
        ),
        dcc.Markdown('', id='goal-slider-container'),


        dcc.Markdown('''###### Campaign Duration'''),
        dcc.Slider(
            id='campaign-duration-slider',
            min=2,
            max=100,
            step=10,
            value=2,
        ),
        dcc.Markdown('', id='campaign-duration-slider-container'),

        ],
    )

column2 = dbc.Col(
    [
        dcc.Markdown('''###### Backers Count'''),
        dcc.Slider(
            id='backers-count-slider',
            min=0,
            max=60,
            step=10,
            value=25,
        ),
        dcc.Markdown('', id='backers-count-slider-container'),


        dcc.Markdown('''###### Blurb Length'''),
        dcc.Slider(
            id='blurb-length-slider',
            min=0,
            max=50,
            step=10,
            value=25,
        ),
        dcc.Markdown('', id='blurb-length-slider-container'),


        dcc.Markdown('''###### Pledged Amount'''),
        
        dcc.Slider(
            id='usd_pledged-slider',
            min=5,
            max=2000000,
            step=1000,
            value=500,
        ),
        dcc.Markdown('', id='pledged-amount-slider-container'),


        # dcc.Markdown('',id='prediction-content', style={
        # 'textAlign':'center',
        # 'font-size':30}), 

        # html.H2('Possibility of Success', className='mb-5'),
        # html.Div(id='prediction-content', className='lead') 
        
        ],
    
    )

column3 = dbc.Col(
    [
        
        # dcc.Markdown('',id='prediction-content', style={
        # 'textAlign':'center',
        # 'font-size':30}), 

        html.H2('Likely to Succeed?', className='mb-5'),
        html.Div(id='prediction-content', className='lead') 
        
        ],
    
    )

# Creates options for sub category based on category list
@app.callback(
    Output('sub-category-dropdown', 'options'),
    [Input('category-dropdown', 'value')])
def set_cities_options(select_category):
    print(select_category)
    return sub_category_list[select_category]

# Inputs sub category options into dropdown menu
# @app.callback(
#     Output('sub-category-dropdown', 'value'),
#     [Input('sub_category', 'options')])
# def set_cities_value(available_options):
#     return available_options[0]['value']



# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('goal-slider-container', 'children'),
    [dash.dependencies.Input('goal-slider', 'value')])
def update_output(value):
    return 'Goal(USD) = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('campaign-duration-slider-container', 'children'),
    [dash.dependencies.Input('campaign-duration-slider', 'value')])
def update_output(value):
    return 'Campaign Duration = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('backers-count-slider-container', 'children'),
    [dash.dependencies.Input('backers-count-slider', 'value')])
def update_output(value):
    return 'Backers Count = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('blurb-length-slider-container', 'children'),
    [dash.dependencies.Input('blurb-length-slider', 'value')])
def update_output(value):
    return 'Blurb Length = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('pledged-amount-slider-container', 'children'),
    [dash.dependencies.Input('usd_pledged-slider', 'value')])
def update_output(value):
    return 'Pledged Amount = "{}"'.format(value)


@app.callback(
    Output('prediction-content','children'),
    [ Input('backers-count-slider', 'value'),
      Input('category-dropdown', 'value'),
      Input('campaign-duration-slider', 'value'),
       Input('goal-slider', 'value'),
       Input('blurb-length-slider', 'value'),
       Input('sub-category-dropdown', 'value'),
      Input('usd_pledged-slider', 'value'),
            
    
     ])

def predict(backers_count, category, campaign_duration, 
    goal_in_usd, blurb_length, sub_category, usd_pledged):
    # backers_count, category, campaign_duration, 
    # goal_in_usd, blurb_length, sub_category, usd_pledged, 
    df = pd.DataFrame(columns=["backers_count", "category", "campaign_duration", 
    "goal_in_usd", "blurb_length", "sub_category", "usd_pledged"],
    data=[[backers_count, category, campaign_duration, 
    goal_in_usd, blurb_length, sub_category, usd_pledged]])
    y_pred = model.predict(df)[0]
    y_pred_prob = model.predict_proba(df)[0]*100
    if y_pred == 1:
        return "You Are {}% Likely to Succeed.".format(round(y_pred_prob[1],2))
    else:
        return "You Are {}% Likely to Fail.".format(round(y_pred_prob[1],2))
    # print(df)
    # return  print(df)

layout = dbc.Row([column1, column2, column3])