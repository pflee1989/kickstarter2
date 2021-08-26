# Kickstarter Success Predictor for Lambda School Build Week

![image](https://user-images.githubusercontent.com/24326725/123136442-44d62580-d496-11eb-8198-8a80ec62f64e.png)

Kickstarter.com is one of the world's top crowdfunding platforms, allowing direct-from-consumer funding for new products and services of all kinds. Never before in history has it been so easy to ideate, fund, and build new products and services. Over 16 million people across the globe have contributed to 150,000+ successful Kickstarter campaigns.


## Lambda School Reference 
[Instructions](https://lambdaschool.github.io/ds/unit2/dash-template/)

## Link to Our App on Heroku
https://kickstarter-predict-success.herokuapp.com/Predictions

## About Us

Philip Lee, Jake Harris and Royce Roberts completed optimized the previous work by Philip Lee, Rhia Goerge and Lucas Chatam on https://github.com/pflee1989/kickstarter_dash. 

We optimized two features-- 

### 1. Sub-Category Display Only Shows the Options Within the Category
We placed an additional callback to limit the display of subcategories to the corresponding category of projects. 

### 2. Limited Maximal Values to Maximize Realistic Prediction
We limited fund-raising goal (world_wide but counted in USD) and pledged amount (world_wide but also counted in USD) both to $250,000.00. 

In addition, we limited the backers_count up to 400 backer's only. 