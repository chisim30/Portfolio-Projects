### Introduction
A new vehicle production company are about to launch their new line of cars and would like to know how the price tag to attach to each of their car brands, and I have been asked to make a model used to predict the price of each car. This is my first data science project, I obtained this data from the IBM Data Science course hosted on Coursera, I hope to get constructive criticism and also upvotes.

### Data Cleaning
The dataset had missing values in some of the columns, so I had to fill thse values in by using the average of the values in those columns in particular. Another thing I did was to change the data types of some of the variables, numerical values got imported as objects rather than floats.

### Exploratory Data Analysis
The EDA process involved both univariate and bivariate analysis.
First off, I visualized the distribution of car prices in the dataset and discovered that most of the prices were between 5,000 and 10,000.

![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/hist_car_price.png "Logo Title Text 1")

#### Univariate Analysis
For the univariate analysis, I checked counts of the categorical variables using bar charts.

![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/bar_1.png "Logo Title Text 1")
![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/bar_2.png "Logo Title Text 1")

#### Bivariate Analysis
For the bivariate aspect of our EDA, I plot box plots of categorical variables against prices, and scatter plots for the numerical variables against prices.

![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/box_1.png "Logo Title Text 1")
![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/box_2.png "Logo Title Text 1")
![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/scatter_1.png "Logo Title Text 1")
![alt text](https://github.com/chisim30/PortfolioProject/blob/main/car_price_prediction/images/scatter_2.png "Logo Title Text 1")

In terms of the scatter plots some variables showed positive relationships with prices, while some showed no relationship or negative relationships. For the box plots we could see some key factors that affected car prices like; body style, number of cylinders, drive wheels, and engine location.

### Model Buidling 
Before the model building commenced, 3 important processes had to be done:

1. The categorical independent features had to be encoded to numerical values using Label encoder from sklearn.
2. The dataset was split into train and test sets with the test set occupying 20% of the data.
3. The independent features from the train and test set was normalized using Standard scaler after which the fitted scaler object was also saved using pickle to enable reuse.

I employed Linear Regression and Ridge Regression for this project.

### Conclusion
All predictor variables had a Pearsons coefficient greater than 0.5 and p-values of less than 0.05 which make them useful in our model development. We achieved an r2 and variance of 0.91 and 0.93 respectively, which are both desired values. We performed cros validation on our training data set to obtain a value of 0.0448 making our model more likely to predict actual observations. We also performed Ridge Regression on our model to reduce the effects of multicollinearity on our model.
