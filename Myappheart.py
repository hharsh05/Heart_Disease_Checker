#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import joblib
import yaml
import SafeLoader
null=None
from PIL import Image
with open('config.yaml') as file:
    config = yaml.load(file)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)
try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)
try:
    username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    if username_forgot_pw:
        st.success('New password sent securely')
        # Random password to be transferred to user securely
    elif username_forgot_pw == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)
try:
    username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
    if username_forgot_username:
        st.success('Username sent securely')
        # Username to be transferred to user securely
    elif username_forgot_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)
if authentication_status:
    try:
        if authenticator.update_user_details(username, 'Update user details'):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
def load_images(file_name):
    img = Image.open(file_name)
    return st.image(img,width=300)
img='heartapp.JPG'
load_images(img)
# Title
st.header("Heart Disease Checker app")
st.write("This app is intended to check wheather you are suffering from any heart disease or not")
st.write("score 0 means you are not suffering from any heart disease and score of 1 or 2 means you are suffering ")



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
            st.text("You are not suffering from heart disease")
    else:
        st.text(f"Please follow instructions")
st.text("Created by Mr.Harshit Harsh")
   

