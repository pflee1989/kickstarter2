# {'Art': [{'installations': 73,
#   'conceptual art': 28,
#   'ceramics': 18,
#   'performance art': 98,
#   'illustration': 70,
#   'social practice': 131,
#   'sculpture': 128,
#   'art': 10,
#   'textiles': 141,
#   'video art': 149,
#   'public art': 114,
#   'mixed media': 87,
#   'painting': 96,
#   'digital art': 36},]
#  '1': {'webcomics': 154,
#   'graphic novels': 66,
#   'events': 44,
#   'anthologies': 6,
#   'comics': 26,
#   'comic books': 25},
#  '2': {'taxidermy': 138,
#   'glass': 64,
#   'woodworking': 156,
#   'knitting': 79,
#   'diy': 37,
#   'weaving': 152,
#   'printing': 112,
#   'crafts': 32,
#   'quilts': 118,
#   'candles': 17,
#   'crochet': 33,
#   'stationery': 136,
#   'pottery': 110,
#   'embroidery': 43},
#  '3': {'residencies': 122,
#   'dance': 34,
#   'workshops': 157,
#   'performances': 99,
#   'spaces': 135},
#  '4': {'interactive design': 74,
#   'product design': 113,
#   'civic design': 22,
#   'architecture': 9,
#   'design': 35,
#   'toys': 144,
#   'typography': 146,
#   'graphic design': 65},
#  '5': {'couture': 31,
#   'pet fashion': 101,
#   'jewelry': 76,
#   'footwear': 60,
#   'accessories': 2,
#   'ready-to-wear': 121,
#   'childrenswear': 20,
#   'fashion': 52,
#   'apparel': 7},
#  '6': {'fantasy': 49,
#   'shorts': 129,
#   'science fiction': 127,
#   'documentary': 39,
#   'horror': 69,
#   'television': 140,
#   'family': 48,
#   'thrillers': 143,
#   'music videos': 91,
#   'experimental': 45,
#   'drama': 40,
#   'film & video': 55,
#   'animation': 5,
#   'action': 3,
#   'festivals': 53,
#   'comedy': 24,
#   'narrative film': 93,
#   'romance': 126,
#   'movie theaters': 89,
#   'webseries': 155},
#  '7': {'food': 58,
#   'vegan': 147,
#   'cookbooks': 29,
#   'restaurants': 123,
#   'small batch': 130,
#   'farms': 51,
#   'food trucks': 59,
#   'spaces': 135,
#   'community gardens': 27,
#   "farmer's markets": 50,
#   'drinks': 41,
#   'bacon': 13,
#   'events': 44},
#  '8': {'live games': 84,
#   'playing cards': 106,
#   'video games': 150,
#   'gaming hardware': 63,
#   'tabletop games': 137,
#   'puzzles': 117,
#   'mobile games': 88,
#   'games': 62},
#  '9': {'audio': 12,
#   'journalism': 77,
#   'video': 148,
#   'print': 111,
#   'web': 153,
#   'photo': 102},
#  '10': {'country & folk': 30,
#   'faith': 47,
#   'chiptune': 21,
#   'rock': 125,
#   'r&b': 119,
#   'music': 90,
#   'metal': 86,
#   'latin': 80,
#   'classical music': 23,
#   'world music': 158,
#   'indie rock': 72,
#   'blues': 14,
#   'pop': 109,
#   'punk': 116,
#   'hip-hop': 68,
#   'electronic music': 42,
#   'comedy': 24,
#   'kids': 78,
#   'jazz': 75},
#  '11': {'people': 97,
#   'places': 105,
#   'photography': 104,
#   'animals': 4,
#   'fine art': 56,
#   'nature': 94,
#   'photobooks': 103},
#  '12': {'nonfiction': 95,
#   'calendars': 15,
#   'art books': 11,
#   'fiction': 54,
#   'radio & podcasts': 120,
#   'translations': 145,
#   'publishing': 115,
#   'poetry': 108,
#   "children's books": 19,
#   'comedy': 24,
#   'literary journals': 82,
#   'young adult': 159,
#   'zines': 160,
#   'letterpress': 81,
#   'literary spaces': 83,
#   'periodicals': 100,
#   'anthologies': 6,
#   'academic': 1},
#  '13': {'camera equipment': 16,
#   'wearables': 151,
#   'space exploration': 134,
#   'technology': 139,
#   'robots': 124,
#   'web': 153,
#   'fabrication tools': 46,
#   'makerspaces': 85,
#   '3d printing': 0,
#   'apps': 8,
#   'gadgets': 61,
#   'hardware': 67,
#   'flight': 57,
#   'software': 132,
#   'diy electronics': 38,
#   'sound': 133},
#  '14': {'plays': 107,
#   'immersive': 71,
#   'spaces': 135,
#   'theater': 142,
#   'experimental': 45,
#   'musical': 92,
#   'festivals': 53,
#   'comedy': 24}}


# @app.callback(
#     Output('sub_category', 'options'),
#     Input('category', 'value'))
# def set_cities_options(select_category):
#     return sub_category_list[select_category]
# # Inputs sub category options into dropdown menu
# @app.callback(
#     Output('sub_category', 'value'),
#     Input('sub_category', 'options'))
# def set_cities_value(available_options):
#     return available_options[0]['value']