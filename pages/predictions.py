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

# category_list = ['film & video','art','technology','comics','fashion','crafts',
#                  'publishing','design','food','theater','music','dance','photography']

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
[{'label': 'Ceramics', 'value': 16},
{'label': 'Conceptual Art', 'value': 24},
{'label': 'Digital Art', 'value': 29}, {'label': 'Illustration', 'value': 58},
{'label': 'Mixed Media', 'value': 71}, {'label': 'Painting', 'value': 79}, 
{'label': 'Performance Art', 'value': 81},
{'label': 'Public Art', 'value': 95}, {'label': 'Sculpture', 'value': 107}, 
{'label': 'Social Practice', 'value': 110},
{'label': 'Textiles', 'value': 118}, {'label': 'Video Art', 'value': 124}],
# 2 Comic
 [{'label': 'Anthologies', 'value': 5}, {'label': 'Comic books', 'value': 22}, 
  {'label': 'Events', 'value': 36}, {'label': 'Graphic Novels', 'value': 54}, 
  {'label': 'Webcomics', 'value': 128}],
# 3 Crafts
 [{'label': 'Candles', 'value': 15}, {'label': 'Crochet', 'value': 28},
  {'label': 'DIY', 'value': 30},  {'label': 'Glass', 'value': 52},
  {'label': 'Knitting', 'value': 65}, {'label': 'Pottery', 'value': 91}, 
  {'label': 'Printing', 'value': 93},
  {'label': 'Stationery', 'value': 115}, {'label': 'Woodworking', 'value': 130}],
# 4 Dance
 [{'label': 'Performances', 'value': 82}, 
  {'label': 'Residencies', 'value': 101}, {'label': 'Spaces', 'value': 114}, 
  {'label': 'Workshops', 'value': 131}],
#  5 Design
 [{'label': 'Architecture', 'value': 8}, {'label': 'Design', 'value': 4}, 
  {'label': 'Graphic Design', 'value': 53}, {'label': 'Interactive Design', 'value': 61}, 
  {'label': 'Product Design', 'value': 94}, {'label': 'Typography', 'value': 121}],
# 6 Fashion   
[{'label': 'Accessories', 'value': 1}, {'label': 'Apparel', 'value': 6},
 {'label': 'Childrenswear', 'value': 18},
  {'label': 'Couture', 'value': 27}, {'label': 'Footwear', 'value': 49},
  {'label': 'Jewelry', 'value': 63}, {'label': 'Ready-to-Wear', 'value': 100}],
# 7 Films and Videos
 [{'label': 'Action', 'value': 2}, {'label': 'Animation', 'value': 4},
  {'label': 'Comedy', 'value': 21},
  {'label': 'Documentary', 'value': 32}, {'label': 'Drama', 'value': 33}, 
  {'label': 'Experimental', 'value': 37},
  {'label': 'Family', 'value': 40}, {'label': 'Fantasy', 'value': 41}, 
  {'label': 'Festivals', 'value': 44},
  {'label': 'Horror', 'value': 57}, 
  {'label': 'Movie Theaters', 'value': 73},
  {'label': 'Music Videos', 'value': 74}, {'label': 'Narrative Film', 'value': 75}, 
  {'label': 'Romance', 'value': 105},
  {'label': 'Science Fiction', 'value': 106}, {'label': 'Shorts', 'value': 108}, 
  {'label': 'Television', 'value': 117},
  {'label': 'Thrillers', 'value': 119}, {'label': 'Webseries', 'value': 129}],
 # 7 Food
 [{'label': 'Bacon', 'value': 11}, {'label': 'Community-Gardens', 'value': 23}, 
  {'label': 'Cookbooks', 'value': 25},
  {'label': 'Drinks', 'value': 34}, {'label': 'Events', 'value': 36}, 
  {'label': "Farmer's Markets", 'value': 42},
  {'label': 'Farms', 'value': 43}, 
  {'label': 'Food Trucks', 'value': 48},
  {'label': 'Restaurants', 'value': 102}, {'label': 'Small Batch', 'value': 109}, 
  {'label': 'Spaces', 'value': 114},
  {'label': 'Vegan', 'value': 122}],
 # 8 Games
 [{'label': 'Gaming Hardware', 'value': 51}, 
  {'label': 'Live Games', 'value': 68},
  {'label': 'Mobile Games', 'value': 72}, {'label': 'Playing Cards', 'value': 87}, 
  {'label': 'Puzzles', 'value': 97},
  {'label': 'Tabletop Games', 'value': 116}, {'label': 'Video Games', 'value': 125}],
 #  Journalism
 [ {'label': 'Audio', 'value': 10}, 
  {'label': 'Photo', 'value': 84},
  {'label': 'Print', 'value': 92}, {'label': 'Video', 'value': 123}, 
  {'label': 'Web', 'value': 127}],
 #  Music
 [{'label': 'Blues', 'value': 10}, 
  {'label': 'Classical Music', 'value': 20},
  {'label': 'Country & Folk', 'value': 26}, 
  {'label': 'Electronic Music', 'value': 35},
  {'label': 'Faith', 'value': 39}, {'label': 'Hip-Hop', 'value': 56}, 
  {'label': 'Indie Rock', 'value': 60},
  {'label': 'Jazz', 'value': 62}, {'label': 'Kids', 'value': 64}, 
  {'label': 'Latin', 'value': 66},
  {'label': 'Metal', 'value': 70}, 
  {'label': 'Pop', 'value': 90},
  {'label': 'Punk', 'value': 96}, {'label': 'R&B', 'value': 98}, 
  {'label': 'Rock', 'value': 104},
  {'label': 'World Music', 'value': 132}],
 #  Photography
 [{'label': 'Animals', 'value': 3}, {'label': 'Fine Art', 'value': 46}, 
  {'label': 'Nature', 'value': 77},
  {'label': 'People', 'value': 80}, {'label': 'Photobooks', 'value': 85}, 
  {'label': 'Places', 'value': 105}],
 #  Publishing
 [{'label': 'Anthologies', 'value': 5}, 
  {'label': 'Art Books', 'value': 9},
  {'label': 'Calendars', 'value': 13}, {'label': "Children's Books", 'value': 17}, 
  {'label': 'Fiction', 'value': 45}, 
  {'label': 'Literary Journals', 'value': 67},
  {'label': 'Nonfiction', 'value': 78}, 
  {'label': 'Periodicals', 'value': 83},
  {'label': 'Poetry', 'value': 89}, 
  {'label': 'Radio & Podcasts', 'value': 99},
  {'label': 'Translations', 'value': 120}, {'label': 'Young Adult', 'value': 133}, 
  {'label': 'Zines', 'value': 134}],
 #  Technology
 [{'label': '3D Printing', 'value': 0}, {'label': 'Apps', 'value': 7}, 
  {'label': 'Camera Equipment', 'value': 14},
  {'label': 'DIY Electronics', 'value': 31}, {'label': 'Fabrication Tools', 'value': 38},
  {'label': 'Flight', 'value': 47},
  {'label': 'Gadgets', 'value': 50}, {'label': 'Hardware', 'value': 55}, 
  {'label': 'Makerspaces', 'value': 69},
  {'label': 'Robots', 'value': 103}, {'label': 'Software', 'value': 111},
  {'label': 'Sound', 'value': 112},
  {'label': 'Space Exploration', 'value': 113},  
  {'label': 'Wearables', 'value': 126},
  {'label': 'Web', 'value': 127}],
 #  Theater
 [{'label': 'Comedy', 'value': 21}, {'label': 'Experimental', 'value': 37},
  {'label': 'Festivals', 'value': 44},
  {'label': 'Immersive', 'value': 59}, {'label': 'Musical', 'value': 75},
  {'label': 'Plays', 'value': 88},
  {'label': 'Spaces', 'value': 114}]]

# {'label': i, 'value': i} for i in category_list
column1 = dbc.Col(
    [
        dcc.Markdown('''###### Category'''),
         dcc.Dropdown(
        id='category-dropdown',
        options=[
                {'label': 'Art', 'value': 0},
                {'label': 'Comics', 'value': 1},
                {'label': 'Crafts', 'value': 2},
                {'label': 'Dance', 'value': 3},
                {'label': 'Design', 'value': 4},
                {'label': 'Fashion', 'value': 5},
                {'label': 'Films & Videos', 'value': 6},
                {'label': 'Food', 'value': 7},
                {'label': 'Games', 'value': 8},
                {'label': 'Journalism', 'value': 9},
                {'label': 'Music', 'value': 10},
                {'label': 'Photography', 'value': 11},
                {'label': 'Publishing', 'value': 12},
                {'label': 'Technology', 'value': 13},
                {'label': 'Theater', 'value': 14},
        ],        value=0,
        className='mb-4'), 

        
    #     dcc.Markdown('''###### Sub Category'''),
    #      dcc.Dropdown(
    #     id='sub-category-dropdown',
    #     options=[
    #     {'label': i, 'value': i} for i in sub_category_list
    #    ],
    #     value='diy',
    #     className='mb-4'), 

        dcc.Markdown('###### Sub-Category'), 
        dcc.Dropdown(
            id='sub-category-dropdown',
            className='mb-5',
        value=0
        ), 



        dcc.Markdown('''###### Goal (All Counted in USD)'''),
        dcc.Slider(
            id='goal-slider',
            min=0,
            max=60000,
            step=100,
            value=100,
        ),
        dcc.Markdown('', id='goal-slider-container'),


        dcc.Markdown('''###### Campaign Duration'''),
        dcc.Slider(
            id='campaign-duration-slider',
            min=2,
            max=100,
            step=1,
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
            max=100,
            step=1,
            value=0,
        ),
        dcc.Markdown('', id='backers-count-slider-container'),


        dcc.Markdown('''###### Blurb Length'''),
        dcc.Slider(
            id='blurb-length-slider',
            min=0,
            max=50,
            step=5,
            value=25,
        ),
        dcc.Markdown('', id='blurb-length-slider-container'),


        dcc.Markdown('''###### Pledged Amount'''),
        
        dcc.Slider(
            id='usd_pledged-slider',
            min=0,
            max=60000,
            step=100,
            value=100,
        ),
        dcc.Markdown('', id='pledged-amount-slider-container'),

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
        return "Great! {}% Likely to Make It!".format(round(y_pred_prob[1],2))
    else:
        return "Failure Detected. {}% Likely to Fail.".format(round(y_pred_prob[0],2))
 

layout = dbc.Row([column1, column2, column3])