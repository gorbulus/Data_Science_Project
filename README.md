# Data Science Project

William Ponton
2.17.19

Exploring Pandas and Visualizations using a Wine Review dataset found on www.kaggle.com 

<p align="center">
  <img width="180" src="beep_boop.png">
</p>

## Wine Review Data Science
Author: William Ponton

2.17.19

### Contact

Email: [waponton](waponton@gmail.com)

Github: [gorbulus](https://github.com/gorbulus)

## Description
Welcome to my RMOTR Data Science Project.  I will be exploring a dataset found on [kaggle](https://www.kaggle.com/zynicide/wine-reviews)

## Content

# This dataset contains two files:

    ```winemag-data-130k-v2.csv``` contains 10 columns and 130k rows of wine reviews.

    ```winemag-data_first150k.csv``` contains 10 columns and 150k rows of wine reviews.

## Acknowledgements

The data was scraped from WineEnthusiast during the week of June 15th, 2017. The code for the scraper can be found here if you have any more specific questions about data collection that I didn't address.

UPDATE 11/24/2017 After feedback from users of the dataset I scraped the reviews again on November 22nd, 2017. This time around I collected the title of each review, which you can parse the year out of, the tasters name, and the taster's Twitter handle. This should also fix the duplicate entry issue.
Inspiration

I think that this dataset offers some great opportunities for sentiment analysis and other text related predictive models. My overall goal is to create a model that can identify the variety, winery, and location of a wine based on a description. If anyone has any ideas, breakthroughs, or other interesting insights/models please post them.


## Project goals

1. Successfully load a csv file into a project.
2. Use pandas and numpy to analyze the dataset.
3. Use matplotlib and pandas to generate visualizations.
4. Create a program to analyze results using Test Driven Design.
5. Use scientific method to provide insightful interpretation.

## Column descriptions

The following are a brief summary of the 13 different columns of data included in the dataset:

- country

The country that the wine is from

- description

A description of the wine's flavor profile

- designation

The vineyard within the winery where the grapes that made the wine are from
points

- points

The number of points WineEnthusiast rated the wine on a scale of 1-100 (though they say they only post reviews for wines that score >=80)
price

- price

The cost for a bottle of the wine

- province

The province or state that the wine is from

- region_1

The wine growing area in a province or state (ie Napa)

- region_2

Sometimes there are more specific regions specified within a wine growing area (ie Rutherford inside the Napa Valley), but this value can sometimes be blank

- taster_name

The name of the wine reviewer

- taster_twitter_handle

The wine reviewer's Twitter handle (if available)

- title

The title of the wine review, which often contains the vintage if you're interested in extracting that feature

- variety

The type of grapes used to make the wine (ie Pinot Noir)

- winery

The winery that made the wine


## Dependencies
If you want to run tests.py ```pip install -r requirements.txt```

### Support

Having trouble with Data_Science_Project? 

Get help at: [gorbulus](waponton@gmail.com) and we’ll help you sort it out.