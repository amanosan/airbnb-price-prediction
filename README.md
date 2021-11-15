# Airbnb Price Prediction

## 1. Problem Statement
To predict the Airbnb rental prices using Machine Learning.

The data - https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data.
***
## 2. Data Preprocessing and Cleaning

The data is in the `AB_NYC_2019.csv`. After cleaning the data and preprocessing the data, the code for which is available in the notebooks - `data_cleanup.ipynb`, `data_preparation.ipynb` and `data_preprocessing.ipynb` notebooks - the clean and processed data is found in the following pickle files:
- `final_with_neighbourhood.pkl` - this data contains all the features including the Neighbourhood feature which had the most unique values.
- `final_without_neighbourhood.pkl` - this data has all features except the Neighbourhood feature.
***
## 3. EDA
The Exploratory Data Analysis can be found in the `data_exploration_geospatial.ipynb` and `data_exploration.ipynb` notebooks. 
***
## 4. Machine Learning
### 4.1 Machine Learning Task 
The machine learning task is a Regression task where we need to predict the prices of the Airbnb rentals.

### 4.2 Performance Metrics used
- Mean Squared Error
- R2 score.
  
### 4.3 Models Used
- Linear Regression - Ordinary Least Squares (OLS)
- Ridge Regression
- Lasso Regression
- RandomForest Regression
- XGBoost Regression
  
***The Model which performed the best was XGBoost using all the features. All the metrics can be found in the `notebooks/metrics_with_all_features.csv` file.*** 