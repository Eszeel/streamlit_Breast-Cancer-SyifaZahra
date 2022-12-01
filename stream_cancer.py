import pickle
import streamlit as st

# membaca model
cancer_model = pickle.load(open('cancer_model.sav', 'rb'))

# judul web
st.title('Data Mining Prediksi Breast Cancer')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    mean_radius = st.number_input ('input nilai mean_radius')

with col2 :
    mean_texture = st.number_input ('input nilai mean_texture')

with col1 :
    mean_perimeter = st.number_input ('input nilai mean_perimeter')

with col2 :
    mean_area = st.number_input ('input nilai mean_area')

with col1 :
    mean_smoothness = st.number_input ('input nilai mean_smoothness')

# code untuk prediksi
cancer_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Breast Cancer'):
    cancer_prediction = cancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])

    if(cancer_prediction[0] == 1):
        cancer_diagnosis = 'Pasien mengidap Breast Cancer'
    else :
        cancer_diagnosis = 'Pasien tidak mengidap Breast Cancer'

    st.success(cancer_diagnosis)
