import streamlit as st
import pandas as pd 
import numpy as np
import joblib
from tensorflow import keras
import tensorflow as tf



st.title('Churn prediction')

with open('pipeline.pkl', 'rb') as f:
    pipe_branch = joblib.load(f)

model = keras.models.load_model('model.h5')


membership_category = st.selectbox('kategori membership Anda: ',('No Membership','Basic Membership','Silver Membership',
       'Premium Membership','Gold Membership','Platinum Membership'))
st.write('Pilihan Anda :', membership_category)


avg_transaction_value = st.slider('Rata-rata transaksi Anda: ', 0,2000)
st.write('Transaksi Anda:', avg_transaction_value)


points_in_wallet = st.slider('Poin dompet digital Anda: ', 0,200)
st.write('Poin Anda:', points_in_wallet)


feedback = st.selectbox('Feedback Anda Anda: ', ('Poor Website', 'Poor Customer Service', 'Too many ads',
       'Poor Product Quality', 'No reason specified',
       'Products always in Stock', 'Reasonable Price',
       'Quality Customer Care', 'User Friendly Website'))
st.write('Feedback Anda:', feedback)

#Dataframe random
data = pd.DataFrame({
        'membership_category'	: [membership_category],
        'avg_transaction_value'	: [avg_transaction_value],
        'points_in_wallet' : [points_in_wallet],
        'feedback' : [feedback],
})
# res_inf = model.predict(data)

df= pipe_branch.transform(data)

if st.button('Predict'): 
    x = model.predict(df)
    hasil = tf.where(x >=0.5, 1, 0) 
    st.write('Hasil Prediksi: ')
    if hasil[0] == 1:
        message = "From the Customers information, it seems that the customers is churn."
        color = 'red'
    else:
        message = "From the Customers information, it seems that the customers is not churn."
        color = 'green'
    st.subheader('Prediction:')
    st.write(message, unsafe_allow_html=True, )
    st.markdown(f'<h1 style="color:{color};text-align:center">{hasil}</h1>', unsafe_allow_html=True)