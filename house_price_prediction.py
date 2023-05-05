import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open('model/regression_model.sav', 'rb'))

st.title('Prediction des prix de maison')
st.sidebar.header('Données de la maison')
image = Image.open('img/maison.jpg')
st.image(image, '')

def house_report():
  OverallQual = st.sidebar.slider('OverallQual', 1,10, 1)
  ExterQual = st.sidebar.slider('ExterQual', 1,4, 1)
  Neighborhood = st.sidebar.slider('Neighborhood', 1,24, 1)
  GarageCars = st.sidebar.slider('GarageCars', 0,2, 0)
  GrLivArea = st.sidebar.slider('GrLivArea', 5,9, 1)
  YearBuilt = st.sidebar.slider('YearBuilt', 1900,2000, 1900) 
  TotalBsmtSF = st.sidebar.slider('TotalBsmtSF', 0,9, 1)
  BsmtQual = st.sidebar.slider('BsmtQual', 0,5, 1)
  GarageArea = st.sidebar.slider('GarageArea', 0,8, 0)
  KitchenQual = st.sidebar.slider('KitchenQual', 1,4, 1)
  stFlrSF = st.sidebar.slider('1stFlrSF', 5,9, 1)
  FullBath = st.sidebar.slider('FullBath', 0,2, 0)



  house_report_data = {
      'OverallQual':OverallQual,
      'ExterQual':ExterQual,
      'Neighborhood':Neighborhood,
      'GarageCars':GarageCars,
      'GrLivArea':GrLivArea,
      'YearBuilt':YearBuilt,
      'TotalBsmtSF':TotalBsmtSF,
      'BsmtQual':BsmtQual,
      'GarageArea':GarageArea,
      'KitchenQual':KitchenQual,
      'stFlrSF':stFlrSF,
      'FullBath':FullBath
  }
  report_data = pd.DataFrame(house_report_data, index=[0])
  return report_data

house_data = house_report()
st.header('Données de la maison')
st.write(house_data)

house_price = model.predict(house_data)
st.subheader('Prix = :red[{} FCFA]'.format(str(np.round(house_price[0], 2))))
st.markdown('Fait **_par_ Alnise BITOKI**.')