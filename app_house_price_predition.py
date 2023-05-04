import streamlit as st
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from PIL import Image

#  Chargement des données
# 
df = pd.read_csv('full_clean_data.csv')

st.title('Prediction des prix de maison')
st.sidebar.header('Données de la maison')
image = Image.open('maison.jpg')
st.image(image, '')

def get_model(data):
  x = data.drop('SalePrice', axis=1)
  y = data['SalePrice']

  sc = StandardScaler()
  x = sc.fit_transform(x)

  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, shuffle=True, random_state=0)

  xgb = XGBRegressor()
  xgb.fit(X_train, y_train)

  return xgb

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


model = get_model(df)
house_data = house_report()
st.header('Données de la maison')
st.write(house_data)

house_price = model.predict(house_data)
st.subheader("Prix = :red[{} FCFA]".format(str(np.round(house_price[0], 2))))
st.markdown('Fait **_par_ Alnise BITOKI**.')