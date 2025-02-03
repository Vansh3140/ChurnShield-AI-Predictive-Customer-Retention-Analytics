import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
import tensorflow as tf
import streamlit as st
import pickle

# Loading the model
model = tf.keras.models.load_model('model.h5')

# One hot encoder
with open('one_hot_encoding_geo.pkl', 'rb') as file:
    one_hot_encoder_geo = pickle.load(file)

# Label gender encoder
with open('label_gender.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

# Scaler encoder
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Streamlit App
st.title('Customer Churn Predictor:')

# User Input

geography = st.selectbox('Geography', one_hot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder.classes_)
age = st.slider('Age', 18, 100)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number Of Products', 1, 4)
has_credit_card = st.selectbox('Has Credit Card?', [0,1])
is_active_member = st.selectbox('Is Active Member?', [0,1])


# Preparing the data

input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_pd = one_hot_encoder_geo.transform([[geography]])
features = one_hot_encoder_geo.get_feature_names_out(['Geography'])

geo_data = pd.DataFrame(geo_pd, columns=features)

input_data = pd.concat([input_data,geo_data], axis=1)

input_data_scaled = scaler.transform(input_data)

prediction = model.predict(input_data_scaled)

st.write(f'Churn Probability {prediction[0][0]*100}')

if prediction[0][0]>0.5:
    st.write('The customer is likely to churn!!')
else:
    st.write('The customer is not likely to churn')
