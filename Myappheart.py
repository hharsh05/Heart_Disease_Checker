#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import joblib
null=None
def load_images(file_name):
    img = Image.open(file_name)
    return st.image(img,width=300)
img='heartapp.jpg'
load_images(img)
# Title
st.header("Heart Disease Checker app")
st.write("This app is intended to check wheather you are suffering from any heart disease or not")
st.write("score 0 means you are not suffering from any heart disease and score of 1 or 2 means you are suffering ")
st.text("Created by Mr.Harshit Harsh")


# Input bar 1
Diabetes_012 = st.number_input("Enter 1 if you suffer from diabetes else enter 0")


# Input bar 2
BMI = st.number_input("Enter BMI, BMI = Weight(Kg)/(Height*Height(metre squared))")
HvyAlcoholConsump = st.number_input("Enter 1 if you consume alcohol frequently else enter 0")
Smoker = st.number_input("Enter 1 if you are smoker  else enter 0")
if st.button("Submit"):
    
    
    if ((Diabetes_012 ==0.00 or Diabetes_012 == 1.00) and (HvyAlcoholConsump ==0.00 or HvyAlcoholConsump ==1.00) and (Smoker==0.00 or Smoker ==1.00)):
        
   
        clf = joblib.load("clf.pkl")

    # Store inputs into dataframe
        x = pd.DataFrame([[Diabetes_012,BMI,Smoker,HvyAlcoholConsump]],
                     columns = ["Diabetes_012","BMI","Smoker","HvyAlcoholConsump"])
    # Get prediction
        prediction = clf.predict(x)[0]

    # Output prediction
        st.text(f"This instance is a {prediction}")
        if (prediction == 1 ):
            st.text("Consult a Doctor")
    else:
        st.text(f"Please follow instructions")
   
           
 
        
    

