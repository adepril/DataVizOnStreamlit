import streamlit as st
import pandas as pd
import numpy as np

# Importation des fonctions de visualisation
from line_chart import create_line_chart
from bar_chart import create_bar_chart
from area_chart import create_area_chart
from map import create_map

st.set_page_config(layout="wide")

st.title('Application de Visualisation de Données')

# Création du menu de sélection
chart_type = st.sidebar.selectbox(
    'Choisissez une représentation graphique',
    ('Graphique Linéaire', 'Graphique à Barres', 'Graphique en Aires', 'Carte')
)

# Affichage du graphique sélectionné
if chart_type == 'Graphique Linéaire':
    create_line_chart()
elif chart_type == 'Graphique à Barres':
    create_bar_chart()
elif chart_type == 'Graphique en Aires':
    create_area_chart()
elif chart_type == 'Carte':
    create_map()