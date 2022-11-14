# Breast_Cancer_Prediction
MY FINAL YEAR PROJECT.

#Project Overview

From the Open Data Obtained from Kaggle Repositories, the Breast Cancer Wisconsin Dataset is choosen to be used in this project.
Data processing and model training is performed on Jupyter Notebook



##Installation

All libraries are available in Anaconda distribution of Python



##Dataset

The dataset has 3 attribute, with
Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)

b) texture (standard deviation of gray-scale values)

c) perimeter

d) area

e) smoothness (local variation in radius lengths)

f) compactness (perimeter^2 / area - 1.0)

g) concavity (severity of concave portions of the contour)

h) concave points (number of concave portions of the contour)

i) symmetry

j) fractal dimension ("coastline approximation" - 1)




##File description

- 'data.csv' : the dataset file
- 'breast_cancer_diagnosis.ipynb' : contains the code of data exploration, preparation and modelling
- 'model.pkl : the classification model
- 'app.py' : Flask API that bind between the classification model and the web page
- templates: 
          - 'index.html' 
          - 'predict.html' : web page that contains a form  for diagnosis
