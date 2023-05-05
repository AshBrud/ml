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
  # Titre de la page
  page_title="Bienvenue | Alnise BITOKI house price prediction app",

  # L'icone de la page
  page_icon="img/home2.ico"
)

st.title('Prediction des prix de maison')
st.sidebar.header('Données de la maison')
image = Image.open('img/maison.jpg')
st.image(image, '')

# Fonction pour formater la sideBar
# Et Créer et formater le tableau sur l'application web
# 
def house_report():
  OverallQual = st.sidebar.slider('Etat global (OverallQual)', 1,10, 1)
  ExterQual = st.sidebar.slider('Etat externe (ExterQual)', 1,5, 1)
  Neighborhood = st.sidebar.slider('Voisinage (Neighborhood)', 1,25, 1)
  GarageCars = st.sidebar.slider('Nbr voiture du garage (GarageCars)', 0,2, 0)
  GrLivArea = st.sidebar.slider('Espace habitable (GrLivArea)', 5,9, 1)
  YearBuilt = st.sidebar.slider('Année de construction (YearBuilt)', 1900,2000, 1900) 
  TotalBsmtSF = st.sidebar.slider('Taille cour (TotalBsmtSF)', 0,9, 1)
  BsmtQual = st.sidebar.slider('Etat de la cour (BsmtQual)', 0,5, 1)
  GarageArea = st.sidebar.slider('Taille garage (GarageArea)', 0,8, 0)
  KitchenQual = st.sidebar.slider('Etat cuisine (KitchenQual)', 1,4, 1)
  stFlrSF = st.sidebar.slider('Taille du RC (1stFlrSF)', 5,9, 1)
  FullBath = st.sidebar.slider('Taille de la douche (FullBath)', 0,2, 0)

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

# Fonction pour formater le prix qui s'affiche
#
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


# Exécution de la première fonction
# Ce qui configure la SideBar
house_data = house_report()  

st.header('Données de la maison')
st.write(house_data)

house_price = model.predict(house_data)
st.subheader('Prix = :red[{}] FCFA'.format(format_price(math.floor(np.round(house_price[0], 2)))))
st.divider() # Trace une ligne
st.markdown('Fait  _par_  :green[**Alnise BITOKI**]')