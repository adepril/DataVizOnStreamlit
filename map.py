import streamlit as st 
import pandas as pd 
import numpy as np  

def create_map():
    # Step 4: Adding a Map Visualization 
    st.subheader('Visualisation sur Carte')
    st.write("Les visualisations sur carte sont utiles pour représenter des données géographiques.")  

    # Sample data for Map  
    map_data = pd.DataFrame({
        # Generate random latitudes around Paris (approx. 48,8566°N)
        'lat': np.random.randn(50) / 50 + 48.8566,
        'lon': np.random.randn(50) / 50 + 2.3522   # Generate random longitudes around Paris (approx. 2,3522°E) 
    })

    # Adding a Map  
    st.map(map_data)  