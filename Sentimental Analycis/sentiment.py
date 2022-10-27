#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st 
import joblib 
model=joblib.load('C:\\Users\\Document\\OneDrive\\Pictures\\Saved Pictures\\sentiment.joblib') 
st.title('Sentimental-Analycis')
text=st.text_input('enter the message')
predict=float(model.predict([text])) 
category='normal category' 
if predict==1.0:
    category='Positive category'
elif predict==-1.0:
    category='Negative category' 
    st.write(category) 

