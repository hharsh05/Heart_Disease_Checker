#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier




df = pd.read_csv('C:/Users/asus/Desktop/my patents/pupil vs wmc project/diabetes_012_health_indicators_BRFSS2015.csv')
df.head()
df.fillna(value=0, inplace=True)
X = df.iloc[:, [4,0,5,11]]
y = df.iloc[:, 7]

# splitting data into training and testing data with 30 % of data as testing data respectively
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# importing the random forest classifier model and training it on the dataset
clf = RandomForestClassifier(n_estimators= 10, criterion="entropy") 
clf.fit(X_train, y_train)

# predicting on the test dataset
y_pred = clf.predict(X_test)

# finding out the accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
# pickling the model
import joblib

joblib.dump(clf, "clf.pkl")
# In[ ]:
import os
cwd = os. getcwd()
cwd


# In[ ]:




