import pickle
import streamlit as st

# membaca model
cancer_model = pickle.load(open('cancer_model.sav', 'rb'))

# judul web
st.title('Data Mining Prediksi Breast Cancer')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    mean_radius = st.text_input ('input nilai Mean Radius (6.98-28.1)')

with col2 :
    mean_texture = st.text_input ('input nilai Mean Texture (9.71-39.3)')

with col1 :
    mean_perimeter = st.text_input ('input nilai Mean Perimeter (43.8-189)')

with col2 :
    mean_area = st.text_input ('input nilai Mean Area (144-2.5k)')

with col1 :
    mean_smoothness = st.text_input ('input nilai Mean Smoothness (0.05-0.16)')

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
