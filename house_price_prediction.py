import streamlit as st
import pickle
import pandas as pd
import numpy as np
import math
from PIL import Image

model = pickle.load(open('model/regression_model.sav', 'rb'))

#  Configuration générale de la page
# 
st.set_page_config(
  page_title="Bienvenue | Alnise BITOKI house price prediction app",
  page_icon="img/home2.ico",
  # layout="wide",
  # initial_sidebar_state="expand",
)

st.title('Prediction des prix de maison')
st.sidebar.header('Données de la maison')
image = Image.open('img/maison.jpg')
st.image(image, '')

def house_report():
  OverallQual = st.sidebar.slider('(OverallQual)', 1,10, 1)
  ExterQual = st.sidebar.slider('(ExterQual)', 1,4, 1)
  Neighborhood = st.sidebar.slider('(Neighborhood)', 1,24, 1)
  GarageCars = st.sidebar.slider('(GarageCars)', 0,2, 0)
  GrLivArea = st.sidebar.slider('(GrLivArea)', 5,9, 1)
  YearBuilt = st.sidebar.slider('(YearBuilt)', 1900,2000, 1900) 
  TotalBsmtSF = st.sidebar.slider('(TotalBsmtSF)', 0,9, 1)
  BsmtQual = st.sidebar.slider('(BsmtQual)', 0,5, 1)
  GarageArea = st.sidebar.slider('(GarageArea)', 0,8, 0)
  KitchenQual = st.sidebar.slider('(KitchenQual)', 1,4, 1)
  stFlrSF = st.sidebar.slider('(1stFlrSF)', 5,9, 1)
  FullBath = st.sidebar.slider('(FullBath)', 0,2, 0)

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

def format_price(number, spacing = ' '):
  number_reversed = str(number)[::-1]
  ret_str = ''
  count = 1

  if len(number_reversed) > 3:
    ret = ''
    for c in number_reversed:
      ret = ret + c + (spacing if count == 3 else '')

      if count == 3: count = 0
      count = count + 1

    ret_str = ret[::-1]
  else:
    ret_str = str(number)

  return ret_str[1:] if ret_str[0] == ' ' else ret_str

house_data = house_report()
st.header('Données de la maison')
st.write(house_data)

house_price = model.predict(house_data)
st.subheader("Prix = {} FCFA".format(str(np.round(house_price[0], 2))))
st.markdown('Fait **_par_ Alnise BITOKI**.')
