### Scenario
Imagine that you are a medical researcher compiling data for a study. You have collected data about a set of patients, all of whom suffered from the same illness. During their course of treatment, each patient responded to one of 5 medications, Drug A, Drug B, Drug c, Drug x and y.

Part of your job is to build a model to find out which drug might be appropriate for a future patient with the same illness. The features of this dataset are Age, Sex, Blood Pressure, and the Cholesterol of the patients, and the target is the drug that each patient responded to.

### Data Cleaning
The data was quite clean already, I just did checks for;

1. check for null/missing values
2. check for unique values in the categorical variables
3. confirming data types for each variable


### Exploratory Data Analysis
By carrying out EDA on this data set I was able to check the distribution of the Age variable and also the Na_to_K variables using histograms


![alt text](https://github.com/chisim30/PortfolioProject/blob/main/drug_selection_classifier/images/Histogram.png "Logo Title Text 1")


Further in my EDA process I checked the count of Sex, Cholesterol, and Drug types variables in the data set using Bar charts.

![alt text](https://github.com/chisim30/PortfolioProject/blob/main/drug_selection_classifier/images/counts.png "Logo Title Text 1")

I also had to compare Cholesterol, Blood Pressure and Drug variables with the Age column using Box plots, I could not establish any relationship between the Cholesterol and Blood Pressure levels with Age, but with the drugs I noticed that older patients were likely to be given drug B and younger patients for Drug A, while the remaining drugs didn't show any strong relationship with Age.

![alt text](https://github.com/chisim30/PortfolioProject/blob/main/drug_selection_classifier/images/boxx.png "Logo Title Text 1")


### Model Building
For this data set I decided Decision Trees would be the best fit for the scenario. First of all I had to assign X  to the predictor variables and Y to the target variable which is 'Drug'. After that I did label encoding on the categorical predictor variables becasue Decision Trees don't work with categorical data. I then fit the model into the decision tree algorithm and ran predcitions.
![alt text](https://github.com/chisim30/PortfolioProject/blob/main/drug_selection_classifier/images/tree.png "Logo Title Text 1")


#### Model Evaluation
I evaluated my model by checking the f1 score and jaccard index of the tests set output variable and the predcitions, I got values for f1 and jaccard index of 0.98 and 0.96 respectively, which are desirable results.

### Conclusion
Using Decision trees I have been able to create  model that can predict the specific drug to give to a patient in a similar condition based on their Age, Blood pressure levels, sodium-potassium pump, and cholesterol levels
